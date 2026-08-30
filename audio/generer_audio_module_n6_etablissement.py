"""
[Obsolète depuis le 26 août 2026 — l'audio vient d'Azure Speech.]
Ce qui suit décrit la synthèse par ElevenLabs, remplacée depuis. Le contexte
français (`charge_utile`, `previous_text`/`next_text`) n'a plus lieu d'être :
le `xml:lang="fr-CA"` du SSML tient la langue des mots isolés. Le ralenti ne
se fait plus à l'`atempo` après coup mais à la synthèse, par `<prosody rate>`.
Le raisonnement pédagogique du texte reste valable ; les moyens ont changé.
Voir `build/azure_voix.py`.

Générateur d'audio — module « Choisir la suite »
(module-n6-etablissement, niveau 6, activité 102).

Deux familles de fichiers, comme dans les autres modules :

  1. les répliques des quatre dialogues → <module>/<dialId>/line_NN_<perso>.mp3
  2. les mots, phrases et mini-leçons → <module>/sons/<fileId>.mp3

**255 extraits attendus** : 80 répliques sur quatre dialogues, et 175 sons.

Les dialogues sont lus dans `build/contenu/module-n6-etablissement/dialogues.js` :
une seule source, comme partout depuis le niveau 2.

Les identifiants de la famille 2 ne s'inventent pas — ils sont produits par le
moteur au rendu. `sons_module_n6_etablissement.json` a été produit **hors
navigateur**, par :

    node build/releve_sons.js module-n6-etablissement > sons_module_n6_etablissement.json

**`build/collecte_sons.py` n'a pas à être lancé** — il n'expire pas, il attend
un seul envoi, et il a déjà écrasé un relevé complet par un relevé partiel
longtemps après qu'on avait cessé d'y penser.

**Ce que ce module a de particulier.**
Les dialogues sont longs : dix-neuf à vingt et une répliques chacun, dont
plusieurs de cinquante mots — un entretien d'orientation et une rencontre à
quatre ne se découpent pas en saynètes de trois répliques. Le coût par extrait
est donc plus élevé qu'aux niveaux 2 et 3 à nombre d'extraits égal.

**Les mots isolés passent par `charge_utile()` de `build/voix.py`**, qui
donne aussi aux répliques de dialogue leurs voisines de scène.** L'exercice de
graphie-phonie de « Je découvre » envoie **seuls** à la synthèse des mots
courts que l'anglais connaît aussi — « six », « dix », « un short », « un
shampoing » : le relevé rend `prGraphie_gr11 → un short`, pas une phrase
porteuse, parce que le gabarit lit le texte de la rangée pour un `vf` à
`cards:true listen:true`. Sans le contexte français d'`charge_utile()`, ces mots
sortiraient à l'anglaise — et c'est justement la prononciation française que
l'élève doit entendre. `charge_utile()` pose `previous_text` et `next_text` autour
de tout extrait de quatre mots ou moins ; rien de ce contexte n'est prononcé
ni facturé.

**Les 28 phrases porteuses de `carrier.js`** servent les seize pastilles des
bandeaux de savoir. Les douze clés des mots de la graphie-phonie sont donc
**inutilisées par le moteur** et gardées pour mémoire ;
`node build/coherence.js` ne les compte pas comme un écart, à raison.

**Six voix pour quatre timbres** — deux personnages ne partagent un timbre que
s'ils ne se répondent jamais, c'est vérifié :

    prep  BINTOU, RÉAL              t1  BINTOU, PASCAL
    t2    BINTOU, ROSA              t3  BINTOU, PASCAL, MARC-OLIVIER, AMÉLIE

RÉAL et MARC-OLIVIER partagent `masculin_1` sans jamais se croiser ; ROSA et
AMÉLIE partagent `enseignante`, de même. C'est un choix et non un pis-aller :
ROSA est une camarade de classe qui lit un document officiel à voix haute avec
son amie, et AMÉLIE est la responsable de l'admission dans une réunion
formelle — un débit posé y est un avantage. La voix « enseignante » est
ralentie à 0,85 par `voix_lente.py` ; le paramètre `speed` d'ElevenLabs ne
fonctionne pas avec `eleven_multilingual_v2`. BINTOU et PASCAL, eux, gardent un
débit normal : au niveau 6, la compétence vise le débit normal.

**État au 22 août 2026 : aucun extrait n'a encore été produit.** Ce script est
écrit et son relevé est fait, mais il n'a pas été lancé — la production des
MP3 coûte de l'argent réel et n'était pas au mandat. Le module est donc livré
muet, et le son se rattrape d'un seul coup :

    python3 generer_audio_module_n6_etablissement.py

Le script est relançable : ce qui existe déjà est sauté, `--force` refait,
`--only prefixe,...` restreint sans repayer le reste.

`parle()` réessaie cinq fois : une coupure TLS repart sur une base courte
(1, 2, 4, 8 s) parce que la liaison revient d'elle-même en quelques secondes,
tandis qu'un 429 ou un 5xx garde l'attente longue (4, 8, 16, 32 s), où
insister trop vite aggrave vraiment les choses.

Usage :  python3 generer_audio_module_n6_etablissement.py [--force] [--only prefixe,...]
"""
import json
import os
import re
import sys
import time
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))
import unicodedata
from pathlib import Path


RACINE = Path(__file__).resolve().parent
SORTIE = RACINE / "assets/interactive/module-n6-etablissement"
MANIFESTE = RACINE / "sons_module_n6_etablissement.json"
DIALOGUES_JS = RACINE / "build/contenu/module-n6-etablissement/dialogues.js"

# Mêmes identifiants que les autres modules, pour que les voix soient les
# mêmes d'un module à l'autre.
VOIX = {
    "enseignante": "mActWQg9kibLro6Z2ouY",   # 👩 féminine #1
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 féminine #2
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # 👨 masculin #1
    "narrateur":   "IPgYtHTNLjC7Bq7IPHrm",   # 👨 narrateur
}

# Six personnages pour quatre timbres. Deux peuvent partager une voix
# seulement s'ils ne se répondent jamais dans un même dialogue ; c'est
# vérifié dans le docstring.
VOIX_PERSO = {
    "BINTOU":       "feminin_2",
    "RÉAL":         "masculin_1",
    "PASCAL":       "narrateur",
    "ROSA":         "enseignante",
    "MARC-OLIVIER": "masculin_1",
    "AMÉLIE":       "enseignante",
}

# Voix des mots isolés et des mini-leçons : celle de l'enseignante.
VOIX_MOTS = VOIX["enseignante"]


def slug(nom):
    """Même règle que charSlug() dans le HTML — sinon le fichier n'est pas trouvé.

    À ne surtout pas « améliorer » avec une expression régulière qui
    normaliserait tout : charSlug garde le trait d'union, et ce module a bien
    un `line_06_marc-olivier.mp3`.
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
ATTENTE_BASE_S = 4   # 429 et 5xx, doublée à chaque échec : 4, 8, 16, 32 s
ATTENTE_RESEAU_S = 1  # coupure TLS : 1, 2, 4, 8 s — voir parle()


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
        print(f"❌ {MANIFESTE.name} introuvable — le produire par "
              f"« node build/releve_sons.js module-n6-etablissement > "
              f"{MANIFESTE.name} », jamais par build/collecte_sons.py")
        sys.exit(1)
    sons = json.loads(MANIFESTE.read_text(encoding="utf-8"))
    for file_id, texte in sons.items():
        taches.append((f"sons/{file_id}", texte, VOIX_MOTS,
                       SORTIE / "sons" / f"{file_id}.mp3", None, None))

    print(f"🔊 module-n6-etablissement — {len(taches)} extraits "
          f"({sum(len(v) for v in dialogues.values())} répliques "
          f"sur {len(dialogues)} dialogues + {len(sons)} sons)\n")

    ok = saute = echec = 0
    for etiquette, texte, voix, chemin, avant, apres in taches:
        if only and not any(etiquette.startswith(o) or
                            chemin.stem.startswith(o) for o in only):
            continue
        # `--only` ne veut pas dire « refais-les » : il veut dire « ne
        # regarde que ceux-là ». Sans cette nuance, partitionner le
        # travail entre plusieurs processus repayait tout ce qui était
        # déjà produit. Pour refaire un extrait, c'est `--force`.
        if chemin.exists() and not force:
            saute += 1
            continue
        print(f"  {etiquette:38s} « {texte[:40]} » → ", end="", flush=True)
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
