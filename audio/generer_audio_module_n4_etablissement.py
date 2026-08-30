"""
[Obsolète depuis le 26 août 2026 — l'audio vient d'Azure Speech.]
Ce qui suit décrit la synthèse par ElevenLabs, remplacée depuis. Le contexte
français (`charge_utile`, `previous_text`/`next_text`) n'a plus lieu d'être :
le `xml:lang="fr-CA"` du SSML tient la langue des mots isolés. Le ralenti ne
se fait plus à l'`atempo` après coup mais à la synthèse, par `<prosody rate>`.
Le raisonnement pédagogique du texte reste valable ; les moyens ont changé.
Voir `build/azure_voix.py`.

Générateur d'audio — module « Prévenir le centre »
(module-n4-etablissement, niveau 4, activité 108).

Deux familles de fichiers, comme dans les autres modules :

  1. les répliques des quatre dialogues → <module>/<dialId>/line_NN_<perso>.mp3
  2. les mots, phrases et mini-leçons   → <module>/sons/<fileId>.mp3

Les dialogues sont lus dans `build/contenu/module-n4-etablissement/dialogues.js` :
une seule source.

`sons_module_n4_etablissement.json` a été relevé **hors navigateur**, par
`node build/releve_sons.js module-n4-etablissement`. 247 extraits de la
famille 2, plus 68 répliques — 315 extraits en tout.

──────────────────────────────────────────────────────────────────────────────
ÉTAT À LA LIVRAISON : AUCUN EXTRAIT N'A ENCORE ÉTÉ PRODUIT.

Le module a été livré complet et sans audio. Le compte ElevenLabs était à zéro
au moment de la production (22 août 2026, avant 23 h 15) : le relevé est fait,
ce script est écrit et relançable, et il ne reste qu'à le lancer — par
`build/audio_tous.py` avec les autres modules de la vague 7, ou seul :

    python3 generer_audio_module_n4_etablissement.py

Rien n'existe encore dans `prep/`, `t1/`, `t2/`, `t3/` ni `sons/`, donc rien
n'est à sauter : la première exécution produira les 315 extraits d'un coup.

Vérifier le compte avant de lancer, pour ne pas relire 315 échecs :

    python3 generer_audio_module_n4_etablissement.py --only pr1_savoir_0_0

Le script est **relançable sans risque** : un extrait déjà présent est sauté,
et une interruption ne coûte que l'extrait en cours.
──────────────────────────────────────────────────────────────────────────────

Quatre avertissements repris des modules précédents, et vérifiés ici :

- **`build/collecte_sons.py` n'a pas été lancé, et ne doit pas l'être.** Il
  attend un envoi et réécrit `sons_<slug>.json` quand il arrive, même
  longtemps après — il a écrasé en silence le relevé d'un *autre* module deux
  fois dans la nuit du 21 août. `build/releve_sons.js` rend le même relevé
  sans ouvrir de port.
- **Tout bloc `ana` porte son champ `say:`.** Les blocs `ana` des quatorze
  mini-leçons ont été vérifiés par `node build/coherence.js`, qui ne signale
  que les images.
- **Les clés de `CARRIER_PHRASES` sont les mots accentués**, tels qu'ils
  paraissent dans les listes `savoir[…][2]`. Le relevé croisé des seize mots
  du banc contre les seize clés a été fait dans les deux sens : aucun mot sans
  phrase porteuse, aucune clé inutilisée. Cinq clés portent un accent qui
  compte — « la boîte vocale », « un répondeur », « un empêchement », « un
  motif », « les coordonnées » — et sont écrites à l'identique de
  `fccards.js`.
- **`charge_utile()` de `build/voix.py` est appelé sur chaque extrait.** Ce module
  en a plus besoin que les autres : son exercice de phonétique fait dire des
  mots courts et nus — « bonjour », « cinq », « la main », « avant » — dont
  plusieurs existent en anglais ou en espagnol. Sans contexte français, ils
  sortiraient à l'anglaise, et c'est précisément la prononciation française
  que l'élève doit entendre.

`parle()` réessaie cinq fois en doublant l'attente : ElevenLabs coupe la
liaison par intermittence, et une panne du fournisseur n'est pas une erreur du
programme. Un 401 n'est en revanche **pas** réessayé — c'est le quota, et
insister ne le recharge pas.

Usage :  python3 generer_audio_module_n4_etablissement.py [--force] [--only prefixe,...]
"""

# Ces deux lignes étaient prisonnières de la docstring — donc jamais
# exécutées. Le défaut ne se voyait pas tant que rien n'en dépendait.
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))
import json
import os
import re
import sys
import time
import unicodedata
from pathlib import Path


RACINE = Path(__file__).resolve().parent
SORTIE = RACINE / "assets/interactive/module-n4-etablissement"
MANIFESTE = RACINE / "sons_module_n4_etablissement.json"
DIALOGUES_JS = RACINE / "build/contenu/module-n4-etablissement/dialogues.js"

# Mêmes identifiants que les autres modules, pour que les voix soient les
# mêmes d'un module à l'autre.
VOIX = {
    "enseignante": "mActWQg9kibLro6Z2ouY",   # 👩 féminine #1
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 féminine #2
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # 👨 masculin #1
    "narrateur":   "IPgYtHTNLjC7Bq7IPHrm",   # 👨 narrateur
}

# Cinq personnages pour quatre voix : une seule est partagée, et la règle des
# personnages qui ne se répondent jamais a servi ici pour la première fois de
# la vague.
#
# NOURHANE traverse les quatre dialogues — c'est elle qu'on suit — et elle
# prend la voix féminine #2, qui n'est ralentie nulle part : elle parle comme
# l'élève voudrait parler.
#
# MURIELLE SANSREGRET, la secrétaire, prend la voix « enseignante », ralentie
# à 0,85 par voix_lente.py. Ce n'est pas un pis-aller : ses deux messages
# portent les seules consignes du module qu'il faut noter mot pour mot — la
# note écrite avant vendredi, l'abandon par écrit avant la fin du mois. Un
# débit posé est exactement ce que l'exercice d'écoute demande.
#
# FABIEN CORRIVEAU, l'enseignant, est seul avec Nourhane dans `t3` : voix
# masculine #1.
#
# WILNER CÉLESTE, le camarade du corridor, n'apparaît que dans `prep`, et
# VOIX — le système téléphonique du centre — n'apparaît que dans `t1` et
# `t2`. **Ils ne se croisent jamais**, et c'est la seule raison pour laquelle
# ils partagent la voix du narrateur. Vérifié dialogue par dialogue : `prep`
# ne contient que NOURHANE et WILNER ; `t1` que VOIX et NOURHANE ; `t2` que
# NOURHANE, VOIX, MURIELLE et FABIEN. Si un dialogue devait un jour mettre
# Wilner et le répondeur dans la même scène, il faudrait une cinquième voix.
VOIX_PERSO = {
    "NOURHANE": "feminin_2",
    "MURIELLE": "enseignante",
    "FABIEN":   "masculin_1",
    "WILNER":   "narrateur",
    "VOIX":     "narrateur",
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
        print(f"❌ {MANIFESTE.name} introuvable — "
              f"lancer node build/releve_sons.js module-n4-etablissement")
        sys.exit(1)
    sons = json.loads(MANIFESTE.read_text(encoding="utf-8"))
    for file_id, texte in sons.items():
        taches.append((f"sons/{file_id}", texte, VOIX_MOTS,
                       SORTIE / "sons" / f"{file_id}.mp3", None, None))

    print(f"🔊 module-n4-etablissement — {len(taches)} extraits "
          f"({sum(len(v) for v in dialogues.values())} répliques "
          f"sur {len(dialogues)} dialogues + {len(sons)} sons)\n")

    ok = saute = echec = 0
    for etiquette, texte, voix, chemin, avant, apres in taches:
        if only and not any(etiquette.startswith(o) or
                            chemin.stem.startswith(o) for o in only):
            continue
        # `--only` ne veut pas dire « refais-les » : il veut dire « ne regarde
        # que ceux-là ». Pour refaire un extrait, c'est `--force`.
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
