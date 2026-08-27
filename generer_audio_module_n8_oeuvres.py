#!/usr/bin/env python3
"""
Générateur d'audio — module « Ce que l'œuvre ne dit pas » (niveau 8)
(module-n8-oeuvres, activité 123).

Deux familles de fichiers, comme dans les autres modules :

  1. les répliques des quatre extraits → <module>/<dialId>/line_NN_<perso>.mp3
  2. les mots, phrases et mini-leçons  → <module>/sons/<fileId>.mp3

Les dialogues ne sont pas recopiés ici : ils sont lus dans
`build/contenu/module-n8-oeuvres/dialogues.js`, la source unique.

Niveau 8 : cent six répliques sur quatre extraits, vingt-huit dans trois
d'entre eux. Le Défi 2 est **presque un monologue** — la chronique radio de
Gaspard Thivierge, quatorze répliques d'affilée coupées par deux questions de
l'animatrice. C'est la forme que le programme appelle « suivre le déroulement
d'exposés bien structurés », et elle a une conséquence directe sur le
casting : le locuteur du monologue ne prend **pas** `enseignante`, que
`voix_lente.py` ralentit à 0,85 — quatorze répliques ralenties d'affilée
seraient interminables. Il prend `narrateur`.

Le relevé des sons (famille 2) n'a **pas** été fait par le navigateur ni par
`build/collecte_sons.py`, qu'il ne faut pas lancer :

    node build/releve_sons.js module-n8-oeuvres > sons_module_n8_oeuvres.json

Vingt lignes de node sur `exos.js`, `carrier.js` et `plus.js`, qui reproduisent
les trois endroits du gabarit appelant `playWord`. Pas de port à réserver, pas
de processus à arrêter, pas d'envoi tardif qui écraserait un relevé complet par
un relevé partiel — les deux incidents que `CLAUDE.md` raconte. Le relevé rend
**287 clés** pour ce module.

Usage :  python3 generer_audio_module_n8_oeuvres.py [--force] [--only prefixe,...]
"""
import json
import os
import re
import sys
import time
import unicodedata
from pathlib import Path

import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))

RACINE = Path(__file__).resolve().parent
SORTIE = RACINE / "assets/interactive/module-n8-oeuvres"
MANIFESTE = RACINE / "sons_module_n8_oeuvres.json"
DIALOGUES_JS = RACINE / "build/contenu/module-n8-oeuvres/dialogues.js"

# Mêmes identifiants que les autres modules, pour que les voix soient les
# mêmes d'un module à l'autre.
VOIX = {
    "enseignante": "mActWQg9kibLro6Z2ouY",   # 👩 féminine #1
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 féminine #2
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # 👨 masculin #1
    "narrateur":   "IPgYtHTNLjC7Bq7IPHrm",   # 👨 narrateur
}

# Quatre personnages, quatre voix : **aucun partage**, donc aucune
# vérification de croisement à faire. Le casting a tout de même été compté par
# extrait et par genre AVANT d'écrire une seule réplique, comme `CLAUDE.md` le
# demande depuis `module-n7-habitation` — le dépôt n'a que deux voix
# féminines, et un extrait à trois femmes est impossible.
#
#   prep  FATOUMATA, JOSYANE            t1  FATOUMATA, LÉANDRE
#   t2    JOSYANE, GASPARD              t3  FATOUMATA, JOSYANE, LÉANDRE
#
# Le Défi 3 réunit trois personnages dont **deux femmes** : c'est la limite
# exacte du dépôt, et elle tient parce que Fatoumata prend `enseignante` et
# Josyane `feminin_2`. Une troisième femme aurait été impossible ; cela s'est
# vérifié avant d'écrire, et n'a rien coûté.
#
# Le choix de qui prend `enseignante` n'est pas neutre : c'est la voix que
# `voix_lente` ralentit à 0,85. Elle va à Fatoumata, qui anime le cercle, pose
# les questions et récapitule — un rôle d'explication, où le débit posé sert.
#
# GASPARD prend `narrateur`, et c'est délibéré. Ses quatorze répliques
# d'affilée du Défi 2 sont une chronique de radio : un exposé suivi, que
# l'élève écoute trois fois avec une consigne différente. Cette voix n'est pas
# ralentie, et c'est la seule configuration écoutable pour un passage de cette
# longueur — la note de l'activité 119 le disait déjà pour sa séance
# d'information.
VOIX_PERSO = {
    "FATOUMATA":  "enseignante",
    "JOSYANE":    "feminin_2",
    "LÉANDRE":    "masculin_1",
    "GASPARD":    "narrateur",
}

# Voix des mots isolés et des mini-leçons : celle de l'enseignante.
VOIX_MOTS = VOIX["enseignante"]


def slug(nom):
    """Même règle que charSlug() dans le HTML — sinon le fichier n'est pas trouvé.

    À ne surtout pas « améliorer » avec une expression régulière qui
    normaliserait tout : charSlug garde le trait d'union, et le module
    voisin a bien un `line_03_jean-philippe.mp3`.
    """
    s = unicodedata.normalize("NFD", nom.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.replace("'", "").replace(" ", "_")


def lire_dialogues():
    """Les dialogues du module, lus dans le fichier de contenu.

    Un parseur JavaScript complet serait absurde ici : le fichier est écrit à
    la main dans une forme stable — un bloc par dialogue, une paire
    ["PERSO","texte"] par réplique. On vérifie tout de même que chaque bloc
    rend des répliques, plutôt que de produire un module muet en silence.
    """
    if not DIALOGUES_JS.exists():
        sys.exit("❌ %s introuvable" % DIALOGUES_JS)
    src = DIALOGUES_JS.read_text(encoding="utf-8")
    blocs = list(re.finditer(r'^  (\w+): \{', src, re.M))
    if not blocs:
        sys.exit("❌ aucun dialogue trouvé dans %s" % DIALOGUES_JS.name)
    dialogues = {}
    for i, m in enumerate(blocs):
        debut = m.end()
        fin = blocs[i + 1].start() if i + 1 < len(blocs) else len(src)
        lignes = re.findall(r'\["([^"]+)","((?:[^"\\]|\\.)*)"\]', src[debut:fin])
        if not lignes:
            sys.exit("❌ le dialogue « %s » ne rend aucune réplique — "
                     "la forme du fichier a changé" % m.group(1))
        dialogues[m.group(1)] = [(p, t.replace('\\"', '"')) for p, t in lignes]
    return dialogues


ESSAIS = 5           # tentatives par extrait
ATTENTE_BASE_S = 4   # doublée à chaque échec : 4, 8, 16, 32 s


# L'audio du cours vient d'Azure Speech depuis le 26 août 2026. `parle_compat`
# porte la signature qu'avait la fonction locale — `cle` et le contexte
# `avant`/`apres` sont acceptés et ignorés, le SSML n'en a plus besoin.
from azure_voix import parle_compat as parle  # noqa: E402


def main():
    cle = os.environ.get("AZURE_SPEECH_KEY", "").strip()
    if not cle:
        env = Path.home() / "Claude" / ".env"
        if env.exists():
            for ligne in env.read_text(encoding="utf-8").splitlines():
                if ligne.strip().startswith("AZURE_SPEECH_KEY="):
                    cle = ligne.split("=", 1)[1].strip().strip("\"'")
    if not cle:
        print("❌ AZURE_SPEECH_KEY absente (variable d'environnement ou .env)")
        sys.exit(1)

    force = "--force" in sys.argv
    only = []
    for i, a in enumerate(sys.argv):
        if a == "--only" and i + 1 < len(sys.argv):
            only = [x.strip() for x in sys.argv[i + 1].split(",") if x.strip()]

    dialogues = lire_dialogues()
    inconnus = {p for lignes in dialogues.values() for p, _ in lignes} - set(VOIX_PERSO)
    if inconnus:
        sys.exit("❌ personnage sans voix : %s" % ", ".join(sorted(inconnus)))

    taches = []
    for dial_id, lignes in dialogues.items():
        for i, (perso, texte) in enumerate(lignes, 1):
            nom = f"line_{i:02d}_{slug(perso)}.mp3"
            # `avant` et `apres` ne servent plus depuis le passage à Azure :
            # c'était le `previous_text` / `next_text` d'ElevenLabs, du
            # français qui conditionnait la synthèse sans être prononcé, pour
            # qu'un mot isolé ne sorte pas à l'anglaise. Le `xml:lang="fr-CA"`
            # du SSML le fait désormais. On les calcule encore parce que la
            # signature les accepte, et `parle_compat` les ignore.
            avant = lignes[i - 2][1] if i >= 2 else None
            apres = lignes[i][1] if i < len(lignes) else None
            taches.append((f"{dial_id}/{nom}", texte,
                           VOIX[VOIX_PERSO[perso]], SORTIE / dial_id / nom,
                           avant, apres))

    if not MANIFESTE.exists():
        print(f"❌ {MANIFESTE.name} introuvable — "
              f"lancer node build/releve_sons.js module-n8-oeuvres")
        sys.exit(1)
    sons = json.loads(MANIFESTE.read_text(encoding="utf-8"))
    for file_id, texte in sons.items():
        taches.append((f"sons/{file_id}", texte, VOIX_MOTS,
                       SORTIE / "sons" / f"{file_id}.mp3", None, None))

    print(f"🔊 module-n8-oeuvres — {len(taches)} extraits "
          f"({sum(len(v) for v in dialogues.values())} répliques "
          f"sur {len(dialogues)} dialogues + {len(sons)} sons)\n")

    ok = saute = echec = 0
    for etiquette, texte, voix, chemin, avant, apres in taches:
        if only and not any(etiquette.startswith(o) or
                            chemin.stem.startswith(o) for o in only):
            continue
        if chemin.exists() and not force and not only:
            saute += 1
            continue
        print(f"  {etiquette:34s} « {texte[:40]} » → ", end="", flush=True)
        if parle(cle, texte, voix, chemin, avant, apres):
            print("✓"); ok += 1
        else:
            print("✗"); echec += 1
        time.sleep(0.35)

    print(f"\n✅ {ok} générés · {saute} déjà présents · {echec} en échec")
    if echec:
        sys.exit(1)


if __name__ == "__main__":
    main()
