"""
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))
from voix import enrichir  # contexte français pour les mots isolés
Générateur d'audio — module « Régler une affaire au centre »
(module-n5-ecole, niveau 5, activité 74).

Deux familles de fichiers, comme dans les autres modules :

  1. les répliques des cinq dialogues → <module>/<dialId>/line_NN_<perso>.mp3
  2. les mots, phrases et mini-leçons  → <module>/sons/<fileId>.mp3

Les dialogues sont lus dans `build/contenu/module-n5-ecole/dialogues.js` :
une seule source.

`sons_module_n5_ecole.json` a été relevé **hors navigateur**, par
`node build/releve_sons.js module-n5-ecole`. 217 extraits de la famille 2,
plus 80 répliques — 297 extraits en tout.

──────────────────────────────────────────────────────────────────────────────
ÉTAT À LA LIVRAISON : AUCUN EXTRAIT N'A ENCORE ÉTÉ PRODUIT.

Le module a été livré complet et sans audio : le relevé est fait, ce script
est écrit et relançable, et il ne reste qu'à le lancer. Aucun fichier
n'existe encore dans `prep/`, `t1/`, `t2/`, `t3/`, `appli/` ni `sons/`, donc
rien n'est à sauter : la première exécution produira les 297 extraits d'un
coup.

    python3 generer_audio_module_n5_ecole.py

Vérifier le compte ElevenLabs avant de lancer, pour ne pas relire 297 échecs :

    python3 generer_audio_module_n5_ecole.py --only pr1_savoir_1_0

Le script est **relançable sans risque** : un extrait déjà présent est sauté,
et une interruption ne coûte que l'extrait en cours.
──────────────────────────────────────────────────────────────────────────────

Trois avertissements repris des modules précédents, et vérifiés ici :

- **`build/collecte_sons.py` n'a pas été lancé, et ne doit pas l'être.** Il
  attend un envoi et réécrit `sons_<slug>.json` quand il arrive, même
  longtemps après — il a écrasé en silence le relevé d'un *autre* module deux
  fois dans la nuit du 21 août. `build/releve_sons.js` rend le même relevé
  sans ouvrir de port.
- **Tout bloc `ana` porte son champ `say:`.** Les blocs `ana` des dix
  mini-leçons ont été vérifiés sur le relevé : aucune valeur ne contient de
  balise HTML, ce qui est la signature d'un `say:` manquant.
- **Les clés de `CARRIER_PHRASES` sont les mots accentués**, tels qu'ils
  paraissent dans les listes `savoir[…][2]`. Le relevé croisé des seize mots
  du banc contre les seize clés a été fait **dans les deux sens** : aucun mot
  sans phrase porteuse, aucune clé inutilisée. Sept clés portent un accent qui
  compte — « le secrétariat », « une conseillère », « une pièce
  justificative », « une échéance », « un relevé », « un délai », « un
  motif » — et sont écrites à l'identique de `fccards.js`.

`parle()` réessaie cinq fois en doublant l'attente : ElevenLabs coupe la
liaison par intermittence, et une panne du fournisseur n'est pas une erreur du
programme. Un 401 n'est en revanche **pas** réessayé — c'est le quota, et
insister ne le recharge pas.

Usage :  python3 generer_audio_module_n5_ecole.py [--force] [--only prefixe,...]
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

RACINE = Path(__file__).resolve().parent
SORTIE = RACINE / "assets/interactive/module-n5-ecole"
MANIFESTE = RACINE / "sons_module_n5_ecole.json"
DIALOGUES_JS = RACINE / "build/contenu/module-n5-ecole/dialogues.js"

# Mêmes identifiants que les autres modules, pour que les voix soient les
# mêmes d'un module à l'autre.
VOIX = {
    "enseignante": "mActWQg9kibLro6Z2ouY",   # 👩 féminine #1
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 féminine #2
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # 👨 masculin #1
    "narrateur":   "IPgYtHTNLjC7Bq7IPHrm",   # 👨 narrateur
}

# Quatre personnages, quatre voix : aucune n'est partagée, la règle des
# personnages qui ne se répondent jamais n'a donc pas à servir ici.
#
# AMELIA traverse les cinq dialogues — c'est elle qu'on suit — et elle prend
# la voix féminine #2, qui n'est ralentie nulle part : elle parle comme
# l'élève voudrait parler.
#
# JOCELYNE PARADIS, au comptoir du secrétariat, prend la voix « enseignante »,
# ralentie à 0,85 par voix_lente.py. Ce n'est pas un pis-aller : c'est elle
# qui explique les formulaires, les échéances et ce qu'il faut rapporter, et
# c'est d'elle que l'élève doit tirer une information exacte. Un débit posé
# est exactement ce que le module demande à cet endroit.
#
# RÉMI GAUTHIER, le conseiller, est seul avec Amelia dans `t2` et `t3` : voix
# masculine #1. KOFFI, le camarade du corridor, n'apparaît que dans `prep`,
# avec Amelia : voix du narrateur. Les deux hommes ne se croisent jamais, mais
# ils gardent quand même deux voix distinctes — l'élève doit entendre la
# différence entre le camarade qui tutoie et le bureau qui vouvoie.
VOIX_PERSO = {
    "AMELIA":   "feminin_2",
    "JOCELYNE": "enseignante",
    "RÉMI":     "masculin_1",
    "KOFFI":    "narrateur",
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


def parle(cle, texte, voix, chemin):
    """Un extrait, avec reprise sur coupure réseau.

    Le 20 août 2026, l'API d'ElevenLabs a coupé la liaison en plein
    téléversement (`SSLEOFError`) pendant une bonne heure, par intermittence.
    Une panne passagère du fournisseur n'est pas une erreur du programme : on
    réessaie, en doublant l'attente, et on ne déclare l'échec qu'après cinq
    tentatives.
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
            # Une coupure TLS n'est pas un refus de débit : la liaison revient
            # d'elle-même en quelques secondes. On garde le doublement, sur
            # une base plus courte que celle des 429.
            attente = ATTENTE_RESEAU_S * (2 ** (essai - 1))
            print(f"⏳{attente}s", end="", flush=True)
            time.sleep(attente)
            continue

        # 429 (débit) et 5xx (panne du service) valent une reprise ; un 401 ou
        # un 422 sont des erreurs à nous, inutile d'insister.
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
              f"lancer node build/releve_sons.js module-n5-ecole")
        sys.exit(1)
    sons = json.loads(MANIFESTE.read_text(encoding="utf-8"))
    for file_id, texte in sons.items():
        taches.append((f"sons/{file_id}", texte, VOIX_MOTS,
                       SORTIE / "sons" / f"{file_id}.mp3"))

    print(f"🔊 module-n5-ecole — {len(taches)} extraits "
          f"({sum(len(v) for v in dialogues.values())} répliques "
          f"sur {len(dialogues)} dialogues + {len(sons)} sons)\n")

    ok = saute = echec = 0
    for etiquette, texte, voix, chemin in taches:
        if only and not any(etiquette.startswith(o) or
                            chemin.stem.startswith(o) for o in only):
            continue
        # `--only` ne veut pas dire « refais-les » : il veut dire « ne regarde
        # que ceux-là ». Pour refaire un extrait, c'est `--force`.
        if chemin.exists() and not force:
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
