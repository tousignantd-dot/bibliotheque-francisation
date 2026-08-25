"""
Générateur d'audio — module « Six mois ailleurs »
(module-n6-logement, niveau 6, activité 105).

Deux familles de fichiers, comme dans les autres modules :

  1. les répliques des quatre dialogues → <module>/<dialId>/line_NN_<perso>.mp3
  2. les mots, phrases et mini-leçons → <module>/sons/<fileId>.mp3

**284 extraits attendus** : 83 répliques sur quatre dialogues, et 201 sons.

Les dialogues sont lus dans `build/contenu/module-n6-logement/dialogues.js` :
une seule source, comme partout depuis le niveau 2.

Les identifiants de la famille 2 ne s'inventent pas — ils sont produits par le
moteur au rendu. `sons_module_n6_logement.json` a été produit **hors
navigateur**, par :

    node build/releve_sons.js module-n6-logement > sons_module_n6_logement.json

**`build/collecte_sons.py` n'a pas à être lancé** — il n'expire pas, il attend
un seul envoi, et il a déjà écrasé un relevé complet par un relevé partiel
longtemps après qu'on avait cessé d'y penser.

**Les mots isolés passent par `charge_utile()` de `build/voix.py`**, qui
donne aussi aux répliques de dialogue leurs voisines de scène.** L'exercice de
graphie-phonie de ce module envoie **seuls** à la synthèse « un sushi », « un
flash », « un t-shirt » et « un schéma » : pour un `vf` à cartes, le relevé
rend le texte de la rangée, pas la phrase porteuse de `carrier.js`. Trois de
ces quatre mots existent en anglais, et sans contexte français ils sortiraient
à l'anglaise — c'est-à-dire exactement à l'envers de ce que l'exercice veut
faire entendre. `charge_utile()` pose `previous_text` et `next_text` autour de tout
extrait de quatre mots ou moins ; rien de ce contexte n'est prononcé ni
facturé. Le pilote du niveau 6 a payé cette découverte ; aucun module du niveau
ne doit s'en passer.

**Les 28 clés de `carrier.js`** se partagent en deux : les seize premières —
les mots des bandeaux de savoir — sont lues par le moteur ; les douze de la
graphie-phonie ne le sont pas, pour la raison ci-dessus. Elles restent au
fichier pour mémoire, et `node build/coherence.js` a raison de ne pas les
compter comme un écart.

**Cinq personnages, quatre timbres** :

    prep  FARIDA, GILLES            t1   FARIDA, MYLÈNE
    t2    FARIDA, LUCIEN            t2b  FARIDA, NICOLAS

GILLES et LUCIEN partagent la voix « masculin_1 » : ils ne paraissent jamais
dans le même dialogue, et aucun des deux ne répond à l'autre. C'est la seule
mise en commun, et elle est sans risque.

MYLÈNE POITRAS, la préposée au service de renseignements, prend la voix
« enseignante », ralentie à 0,85 par `voix_lente.py`. C'est un choix, pas un
défaut : c'est elle qui énonce la démarche et les délais que l'élève doit
pouvoir redire dans « Je me lance », et un débit posé sert cet extrait-là. Les
trois autres gardent un débit normal — au niveau 6, la compétence vise le débit
normal.

**État au 22 août 2026 : aucun extrait n'a encore été produit.** Ce script est
écrit et son relevé est fait, mais il n'a pas été lancé — la production des MP3
coûte de l'argent réel et n'était pas au mandat. Le module est donc livré muet,
et le son se rattrape d'un seul coup :

    python3 generer_audio_module_n6_logement.py

Le script est relançable : ce qui existe déjà est sauté, `--force` refait,
`--only prefixe,...` restreint sans repayer le reste.

`parle()` réessaie cinq fois en doublant l'attente : ElevenLabs coupe la
liaison par intermittence, et une panne du fournisseur n'est pas une erreur du
programme.

Usage :  python3 generer_audio_module_n6_logement.py [--force] [--only prefixe,...]
"""
import json
import os
import re
import sys
import time
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))
from voix import charge_utile  # contexte français, générique ou de dialogue
import unicodedata
from pathlib import Path

try:
    import requests
except ImportError:
    print("❌ pip install requests"); sys.exit(1)

from voix_lente import ralentir_si_enseignante

RACINE = Path(__file__).resolve().parent
SORTIE = RACINE / "assets/interactive/module-n6-logement"
MANIFESTE = RACINE / "sons_module_n6_logement.json"
DIALOGUES_JS = RACINE / "build/contenu/module-n6-logement/dialogues.js"

# Mêmes identifiants que les autres modules, pour que les voix soient les
# mêmes d'un module à l'autre.
VOIX = {
    "enseignante": "mActWQg9kibLro6Z2ouY",   # 👩 féminine #1
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 féminine #2
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # 👨 masculin #1
    "narrateur":   "IPgYtHTNLjC7Bq7IPHrm",   # 👨 narrateur
}

# Cinq personnages, quatre timbres. GILLES (prep) et LUCIEN (t2) partagent
# « masculin_1 » : ils ne se répondent jamais et ne paraissent jamais dans le
# même dialogue.
#
# MYLÈNE prend la voix « enseignante », ralentie à 0,85 par `voix_lente.py` —
# c'est elle qui énonce les délais que l'élève devra redire.
VOIX_PERSO = {
    "FARIDA":  "feminin_2",
    "GILLES":  "masculin_1",
    "MYLÈNE":  "enseignante",
    "LUCIEN":  "masculin_1",
    "NICOLAS": "narrateur",
}

# Voix des mots isolés et des mini-leçons : celle de l'enseignante.
VOIX_MOTS = VOIX["enseignante"]


def slug(nom):
    """Même règle que charSlug() dans le HTML — sinon le fichier n'est pas trouvé.

    À ne surtout pas « améliorer » avec une expression régulière qui
    normaliserait tout : charSlug garde le trait d'union, et un module voisin a
    bien un `line_03_jean-philippe.mp3`.
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


def parle(cle, texte, voix, chemin, avant=None, apres=None):
    """Un extrait, avec reprise sur coupure réseau.

    Une panne passagère du fournisseur n'est pas une erreur du programme : on
    réessaie en doublant l'attente, et on ne déclare l'échec qu'après cinq
    tentatives. La base est courte pour les coupures TLS (la liaison revient
    d'elle-même en quelques secondes) et longue pour les 429 et les 5xx, où
    insister trop vite aggrave les choses.
    """
    for essai in range(1, ESSAIS + 1):
        try:
            r = requests.post(
                f"https://api.elevenlabs.io/v1/text-to-speech/{voix}",
                json=charge_utile(texte, voix, avant=avant, apres=apres),
                headers={"xi-api-key": cle, "Content-Type": "application/json"},
                timeout=60)
        except requests.exceptions.RequestException as e:
            if essai == ESSAIS:
                print(f"   ❌ réseau après {ESSAIS} essais : {type(e).__name__}")
                return False
            attente = ATTENTE_RESEAU_S * (2 ** (essai - 1))
            print(f"⏳{attente}s", end="", flush=True)
            time.sleep(attente)
            continue

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
            # La réplique d'avant et celle d'après partent avec l'extrait, en
            # `previous_text` / `next_text` : du français qui conditionne la
            # synthèse sans être prononcé. Sur un mot isolé, `charge_utile`
            # retombe sur sa phrase de classe générique ; ici on a mieux à
            # offrir — la scène elle-même.
            avant = lignes[i - 2][1] if i >= 2 else None
            apres = lignes[i][1] if i < len(lignes) else None
            taches.append((f"{dial_id}/{nom}", texte,
                           VOIX[VOIX_PERSO[perso]], SORTIE / dial_id / nom,
                           avant, apres))

    if not MANIFESTE.exists():
        print(f"❌ {MANIFESTE.name} introuvable — le produire par "
              f"« node build/releve_sons.js module-n6-logement > "
              f"{MANIFESTE.name} », jamais par build/collecte_sons.py")
        sys.exit(1)
    sons = json.loads(MANIFESTE.read_text(encoding="utf-8"))
    for file_id, texte in sons.items():
        taches.append((f"sons/{file_id}", texte, VOIX_MOTS,
                       SORTIE / "sons" / f"{file_id}.mp3", None, None))

    print(f"🔊 module-n6-logement — {len(taches)} extraits "
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
