#!/usr/bin/env python3
"""
Générateur d'audio — module « Faire parler l'équipe » (niveau 7)
(module-n7-classe, activité 117).

Deux familles de fichiers, comme dans les autres modules :

  1. les répliques des quatre extraits → <module>/<dialId>/line_NN_<perso>.mp3
  2. les mots, phrases et mini-leçons  → <module>/sons/<fileId>.mp3

Les dialogues ne sont pas recopiés ici : ils sont lus dans
`build/contenu/module-n7-classe/dialogues.js`, la source unique.

Niveau 7, donc des **discours longs** : les quatre extraits font de vingt et
une à vingt-deux répliques, dont plusieurs de quatre ou cinq phrases. Le défi 1
est une rencontre avec une personne invitée en classe : ses répliques sont les
plus longues du module, et c'est voulu — l'élève doit apprendre à tenir le fil
d'un exposé, pas d'un échange.

**Le casting a été compté avant l'écriture des dialogues**, comme le demande le
journal de l'activité 115, et c'est ce qui a décidé du genre de Miguel Ospina.
Une salle de classe réunit naturellement trois ou quatre personnes, et le dépôt
n'a que deux voix féminines : les quatre extraits sont donc répartis pour ne
jamais mettre trois voix du même genre dans une même scène. Voir la table
`VOIX_PERSO` ci-dessous, qui le vérifie extrait par extrait.

Le relevé des sons (famille 2) n'a **pas** été fait par le navigateur ni par
`build/collecte_sons.py`, qu'il ne faut pas lancer :

    node build/releve_sons.js module-n7-classe > sons_module_n7_classe.json

Vingt lignes de node sur `exos.js`, `carrier.js` et `plus.js`, qui reproduisent
les trois endroits du gabarit appelant `playWord`. Pas de port à réserver, pas
de processus à arrêter, pas d'envoi tardif qui écraserait un relevé complet par
un relevé partiel — les deux incidents que `CLAUDE.md` raconte.

Usage :  python3 generer_audio_module_n7_classe.py [--force] [--only prefixe,...]
"""
import json
import os
import re
import sys
import time
import unicodedata
from pathlib import Path

try:
    import requests
except ImportError:
    print("❌ pip install requests"); sys.exit(1)

from voix_lente import ralentir_si_enseignante
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))
from voix import enrichir  # contexte français pour les mots isolés

RACINE = Path(__file__).resolve().parent
SORTIE = RACINE / "assets/interactive/module-n7-classe"
MANIFESTE = RACINE / "sons_module_n7_classe.json"
DIALOGUES_JS = RACINE / "build/contenu/module-n7-classe/dialogues.js"

# Mêmes identifiants que les autres modules, pour que les voix soient les
# mêmes d'un module à l'autre.
VOIX = {
    "enseignante": "K7gx0ylJdff0yjM2uVQS",   # 👩 féminine #1
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 féminine #2
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # 👨 masculin #1
    "narrateur":   "IPgYtHTNLjC7Bq7IPHrm",   # 👨 narrateur
}

# Cinq locuteurs pour quatre voix. Deux ne peuvent partager une voix que s'ils
# ne se répondent jamais dans un même extrait ; c'est vérifié extrait par
# extrait :
#
#   prep  GHISLAINE, NEUSA, YOUSSOUF     t1  PERRINE, NEUSA, MIGUEL
#   t2    GHISLAINE, NEUSA, MIGUEL       t3  NEUSA, YOUSSOUF, MIGUEL
#
# GHISLAINE et PERRINE partagent `enseignante` sans jamais se croiser : la
# seule scène où elles auraient pu l'être — la classe pendant la conférence —
# n'a pas été écrite ainsi, précisément pour cette raison. YOUSSOUF et MIGUEL,
# eux, se répondent constamment : ils ont donc chacun leur voix masculine.
#
# **C'est ce comptage qui a décidé du genre de Miguel Ospina**, et il a été
# fait AVANT que les dialogues soient écrits. Une salle de classe réunit
# naturellement trois ou quatre personnes ; avec deux voix féminines au dépôt,
# une équipe de trois femmes aurait été impossible à monter, et la correction
# après coup coûte quatre fichiers de contenu. Le journal de l'activité 115 le
# dit, ce module l'a appliqué : compter les locuteurs par extrait est gratuit
# avant, c'est une réécriture après.
#
# Le choix de qui prend `enseignante` n'est pas neutre : c'est la voix que
# `voix_lente` ralentit à 0,85. Elle va à Ghislaine Turcotte, l'enseignante qui
# explique le rôle d'animatrice puis la façon de résumer, et à Perrine Auclair,
# la personne-ressource qui expose un contenu neuf devant une classe de
# francisation — les deux rôles exacts pour lesquels un débit posé a été
# introduit. Neusa, dont l'élève suit le point de vue, prend l'autre voix
# féminine ; elle parle à sa vitesse à elle.
VOIX_PERSO = {
    "NEUSA":     "feminin_2",
    "GHISLAINE": "enseignante",
    "PERRINE":   "enseignante",
    "YOUSSOUF":  "masculin_1",
    "MIGUEL":    "narrateur",
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


def parle(cle, texte, voix, chemin):
    """Un extrait, avec reprise sur coupure réseau.

    Le 20 août 2026, l'API d'ElevenLabs a coupé la liaison en plein
    téléversement (`SSLEOFError`) pendant une bonne heure, par intermittence.
    Le script s'arrêtait alors sur la trace d'une exception, au milieu d'une
    série de deux cents extraits — il fallait le relancer à la main, et il
    reprenait où il en était, mais sans personne pour le surveiller il ne
    faisait rien. Une panne passagère du fournisseur n'est pas une erreur du
    programme : on réessaie, en doublant l'attente, et on ne déclare l'échec
    qu'après cinq tentatives.
    """
    for essai in range(1, ESSAIS + 1):
        try:
            r = requests.post(
                f"https://api.elevenlabs.io/v1/text-to-speech/{voix}",
                json=enrichir({"text": texte, "model_id": "eleven_multilingual_v2",
                      "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}),
                headers={"xi-api-key": cle, "Content-Type": "application/json"},
                timeout=60)
        except requests.exceptions.RequestException as e:
            if essai == ESSAIS:
                print(f"   ❌ réseau après {ESSAIS} essais : {type(e).__name__}")
                return False
            attente = ATTENTE_BASE_S * (2 ** (essai - 1))
            print(f"⏳{attente}s", end="", flush=True)
            time.sleep(attente)
            continue

        # 429 (débit) et 5xx (panne du service) valent aussi une reprise ;
        # un 401 ou un 422 sont des erreurs à nous, inutile d'insister.
        if r.status_code in (429, 500, 502, 503, 504) and essai < ESSAIS:
            attente = ATTENTE_BASE_S * (2 ** (essai - 1))
            print(f"⏳{r.status_code}/{attente}s", end="", flush=True)
            time.sleep(attente)
            continue
        if r.status_code != 200:
            print(f"   ❌ {r.status_code}: {r.text[:150]}")
            return False

        chemin.parent.mkdir(parents=True, exist_ok=True)
        chemin.write_bytes(r.content)
        ralentir_si_enseignante(chemin, voix)
        return True
    return False


def main():
    cle = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not cle:
        env = RACINE / ".env"
        if env.exists():
            for ligne in env.read_text(encoding="utf-8").splitlines():
                if ligne.strip().startswith("ELEVENLABS_API_KEY="):
                    cle = ligne.split("=", 1)[1].strip().strip("\"'")
    if not cle:
        print("❌ ELEVENLABS_API_KEY absente (variable d'environnement ou .env)")
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
            taches.append((f"{dial_id}/{nom}", texte,
                           VOIX[VOIX_PERSO[perso]], SORTIE / dial_id / nom))

    if not MANIFESTE.exists():
        print(f"❌ {MANIFESTE.name} introuvable — "
              f"lancer build/collecte_sons.py module-n7-classe")
        sys.exit(1)
    sons = json.loads(MANIFESTE.read_text(encoding="utf-8"))
    for file_id, texte in sons.items():
        taches.append((f"sons/{file_id}", texte, VOIX_MOTS,
                       SORTIE / "sons" / f"{file_id}.mp3"))

    print(f"🔊 module-n7-classe — {len(taches)} extraits "
          f"({sum(len(v) for v in dialogues.values())} répliques "
          f"sur {len(dialogues)} dialogues + {len(sons)} sons)\n")

    ok = saute = echec = 0
    for etiquette, texte, voix, chemin in taches:
        if only and not any(etiquette.startswith(o) or
                            chemin.stem.startswith(o) for o in only):
            continue
        if chemin.exists() and not force and not only:
            saute += 1
            continue
        print(f"  {etiquette:34s} « {texte[:40]} » → ", end="", flush=True)
        if parle(cle, texte, voix, chemin):
            print("✓"); ok += 1
        else:
            print("✗"); echec += 1
        time.sleep(0.35)

    print(f"\n✅ {ok} générés · {saute} déjà présents · {echec} en échec")
    if echec:
        sys.exit(1)


if __name__ == "__main__":
    main()
