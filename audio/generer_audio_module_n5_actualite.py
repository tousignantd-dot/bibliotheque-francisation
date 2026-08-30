"""
Générateur d'audio — module « L'Écho des Cantons »
(module-n5-actualite, niveau 5).

Écrit le 28 août 2026, après coup : c'était le **dernier module du dépôt sans
générateur**. Les quatre-vingts répliques de ses cinq dialogues et ses deux
cent quatorze sons n'avaient jamais été produits, non pas parce qu'un appel
échouait, mais parce que rien ne les demandait. `build/audio_manquant.py` le
nommait ; le tableau de bord, lui, ne voyait que « aucune piste audio ».

L'audio vient d'Azure Speech (décidé le 26 août 2026, voir `build/azure_voix.py`) :
ce générateur naît donc après la bascule et ne porte pas l'avertissement
d'obsolescence des cent neuf autres, qui décrivent encore ElevenLabs en tête.

Deux familles de fichiers, comme partout ailleurs :

  1. les répliques des cinq dialogues → <module>/<dialId>/line_NN_<perso>.mp3
  2. les mots, phrases et mini-leçons → <module>/sons/<fileId>.mp3

Les dialogues sont lus dans `build/contenu/module-n5-actualite/dialogues.js` :
une seule source. `sons_module_n5_actualite.json` a été relevé **hors
navigateur**, par `node build/releve_sons.js module-n5-actualite` — 214
extraits, dont 150 de mini-leçons.

Trois vérifications faites avant d'écrire une ligne, et refaites ici :

- **`build/collecte_sons.py` n'a pas été lancé, et ne doit pas l'être.** Il
  n'expire pas : il attend un envoi et réécrit `sons_<slug>.json` quand il
  arrive, même longtemps après. Il a écrasé en silence le relevé d'un *autre*
  module deux fois dans la nuit du 21 août.
- **Aucune valeur du relevé ne contient de balise HTML** — c'est la signature
  d'un `say:` manquant dans un bloc `ana`. Les 214 ont été passées au filtre :
  zéro balise, zéro valeur vide, la plus longue fait 204 caractères.
- **Le motif des répliques tolère l'espace après la virgule.** Celui des
  générateurs plus anciens exigeait `["PERSO","texte"]` et s'arrêtait net sur
  un fichier écrit `["PERSO", "texte"]` — c'est ce qui a rendu
  `module-n6-habitation` muet jusqu'au 28 août. Le fichier d'ici s'écrit sans
  espace, mais un motif qui dépend de la mise en forme est un piège qu'on ne
  repose pas.

Usage :  python3 generer_audio_module_n5_actualite.py [--force] [--only prefixe,...]
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
SORTIE = RACINE / "assets/interactive/module-n5-actualite"
MANIFESTE = RACINE / "sons_module_n5_actualite.json"
DIALOGUES_JS = RACINE / "build/contenu/module-n5-actualite/dialogues.js"

# Mêmes identifiants que les autres modules, pour que les voix soient les
# mêmes d'un module à l'autre. Ce sont d'anciens identifiants ElevenLabs :
# `parle_compat` les traduit en rôles Azure, et c'est la table
# `DEPUIS_ELEVENLABS` de `build/azure_voix.py` qui fait le pont. On les garde
# plutôt que d'écrire les rôles en clair, pour qu'un seul endroit du dépôt
# décide de la correspondance.
VOIX = {
    "enseignante": "mActWQg9kibLro6Z2ouY",   # 👩 féminine #1
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 féminine #2
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # 👨 masculin #1
    "narrateur":   "IPgYtHTNLjC7Bq7IPHrm",   # 👨 narrateur
}

# Trois personnages, trois voix, aucun croisement possible.
#
# MARISOL Ferreira traverse les cinq dialogues : voix féminine #2, la même
# qu'elle porte déjà dans n3-epicerie, n3-electro, n3-loisirs, n5-saisons et
# n5-voisinage. C'est le même personnage d'un module à l'autre, et l'élève
# qui la reconnaît à l'oreille n'apprend pas ça pour rien.
#
# SYLVAIN Ouellet, le cuisinier, est dans quatre dialogues sur cinq : voix
# masculine #1, comme dans n7-recherche.
#
# TERESA n'apparaît qu'au défi 2, et seulement face à Marisol. Il lui faut donc
# un timbre féminin distinct de `feminin_2` : c'est `enseignante`. Les deux
# sont la même comédienne Azure à sept pour cent d'écart de hauteur — la
# parade documentée dans build/azure_voix.py, et le seul recours tant qu'Azure
# ne publie qu'une voix féminine en fr-CA. Le rôle s'appelle « enseignante »
# pour des raisons historiques : il ne ralentit rien ici, le ralenti se
# demande par `palier` et n'est pas demandé.
VOIX_PERSO = {
    "MARISOL": "feminin_2",
    "SYLVAIN": "masculin_1",
    "TERESA":  "enseignante",
}

# Voix des mots isolés et des mini-leçons : celle de l'enseignante.
VOIX_MOTS = VOIX["enseignante"]


def slug(nom):
    """Même règle que charSlug() dans le HTML — sinon le fichier n'est pas trouvé."""
    s = unicodedata.normalize("NFD", nom.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.replace("'", "").replace(" ", "_")


def lire_dialogues():
    """Les dialogues du module, lus dans le fichier de contenu."""
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
        # L'espace après la virgule est facultatif — voir l'en-tête.
        lignes = re.findall(r'\[\s*"([^"]+)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\]',
                            src[debut:fin])
        if not lignes:
            sys.exit("❌ le dialogue « %s » ne rend aucune réplique — "
                     "la forme du fichier a changé" % m.group(1))
        dialogues[m.group(1)] = [(p, t.replace('\\"', '"')) for p, t in lignes]
    return dialogues


ESSAIS = 5           # tentatives par extrait
ATTENTE_BASE_S = 4   # 429 et 5xx, doublée à chaque échec : 4, 8, 16, 32 s
ATTENTE_RESEAU_S = 1  # coupure TLS : 1, 2, 4, 8 s — voir parle()

# `parle_compat` porte la signature qu'avaient les fonctions locales des autres
# générateurs — `cle` et le contexte `avant`/`apres` sont acceptés et ignorés,
# le SSML n'en a plus besoin.
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
            avant = lignes[i - 2][1] if i >= 2 else None
            apres = lignes[i][1] if i < len(lignes) else None
            taches.append((f"{dial_id}/{nom}", texte,
                           VOIX[VOIX_PERSO[perso]], SORTIE / dial_id / nom,
                           avant, apres))

    if not MANIFESTE.exists():
        print(f"❌ {MANIFESTE.name} introuvable — "
              f"lancer node build/releve_sons.js module-n5-actualite")
        sys.exit(1)
    sons = json.loads(MANIFESTE.read_text(encoding="utf-8"))
    for file_id, texte in sons.items():
        taches.append((f"sons/{file_id}", texte, VOIX_MOTS,
                       SORTIE / "sons" / f"{file_id}.mp3", None, None))

    print(f"🔊 module-n5-actualite — {len(taches)} extraits "
          f"({sum(len(v) for v in dialogues.values())} répliques "
          f"sur {len(dialogues)} dialogues + {len(sons)} sons)\n")

    ok = saute = echec = 0
    for etiquette, texte, voix, chemin, avant, apres in taches:
        if only and not any(etiquette.startswith(o) or
                            chemin.stem.startswith(o) for o in only):
            continue
        # `--only` ne veut pas dire « refais-les » : il veut dire « ne
        # regarde que ceux-là ». Pour refaire un extrait, c'est `--force`.
        if chemin.exists() and not force:
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
