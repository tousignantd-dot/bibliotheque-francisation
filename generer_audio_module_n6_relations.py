"""
Générateur d'audio — module « Reprendre le fil »
(module-n6-relations, niveau 6, activité 101, situation « Relations sociales »).

Deux familles de fichiers, comme dans les autres modules :

  1. les répliques des quatre dialogues → <module>/<dialId>/line_NN_<perso>.mp3
  2. les mots, phrases et mini-leçons → <module>/sons/<fileId>.mp3

**249 extraits attendus** : 78 répliques sur quatre dialogues (20 + 20 + 20 +
18) et 171 sons.

Les dialogues sont lus dans `build/contenu/module-n6-relations/dialogues.js` :
une seule source, comme aux niveaux 2, 3 et 5.

Les identifiants de la famille 2 ne s'inventent pas — ils sont produits par le
moteur au rendu. `sons_module_n6_relations.json` a été produit **hors
navigateur**, par :

    node build/releve_sons.js module-n6-relations > sons_module_n6_relations.json

**`build/collecte_sons.py` n'a pas à être lancé** — il n'expire pas, il attend
un seul envoi, et il a déjà écrasé un relevé complet par un relevé partiel
longtemps après qu'on avait cessé d'y penser.

**Quatre personnages, quatre voix, aucun partage.** MARISOL, OUSMANE et
GHISLAIN se parlent ; la NARRATRICE ne dit que des textes écrits — le courriel
d'Ousmane au Défi 1, l'article de L'Écho de la Yamaska au Défi 3. C'est elle
qui prend la voix « enseignante », ralentie à 0,85 par `voix_lente.py` : lire
un texte écrit à voix haute demande un débit posé. Les trois autres gardent un
débit normal, puisque le niveau 6 vise la compréhension au débit normal.

    prep  MARISOL, GHISLAIN            t1  MARISOL, OUSMANE
    t2    MARISOL, GHISLAIN            t3  MARISOL, GHISLAIN, NARRATRICE

**Les mots isolés passent par `enrichir()` de `build/voix.py`.** L'exercice de
graphie-phonie de « Je découvre » envoie **seuls** à la synthèse des mots
courts que l'anglais connaît aussi — « six », « dix », « un short », « du
shampoing » : le relevé rend `prGraphie_gr9 → un short`, pas la phrase
porteuse, parce que le gabarit lit le texte de la rangée pour un `vf` à
`cards:true listen:true`. Sans contexte français, « un short » et « du
shampoing » sortent à l'anglaise — et c'est précisément la prononciation
française que l'élève doit entendre. `enrichir()` pose `previous_text` et
`next_text` autour de tout extrait de quatre mots ou moins ; rien de ce
contexte n'est prononcé ni facturé.

**Les douze clés de graphie-phonie de `carrier.js` sont donc inutilisées par
le moteur** et gardées pour mémoire ; `node build/coherence.js` ne les compte
pas comme un écart, à raison. Les dix-neuf autres, elles, servent bel et bien
les pastilles des bandeaux de savoir.

**État au 22 août 2026 : aucun extrait n'a encore été produit.** Ce script est
écrit et son relevé est fait, mais il n'a pas été lancé — la production des
MP3 coûte de l'argent réel et n'était pas au mandat. Le module est donc livré
muet, et le son se rattrape d'un seul coup :

    python3 generer_audio_module_n6_relations.py

Le script est relançable : ce qui existe déjà est sauté, `--force` refait,
`--only prefixe,...` restreint sans repayer le reste.

`parle()` réessaie cinq fois en doublant l'attente : ElevenLabs coupe la
liaison par intermittence, et une panne du fournisseur n'est pas une erreur du
programme.

Usage :  python3 generer_audio_module_n6_relations.py [--force] [--only prefixe,...]
"""

import json
import os
import re
import sys
import time
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))
from voix import enrichir  # contexte français pour les mots isolés
import unicodedata
from pathlib import Path

try:
    import requests
except ImportError:
    print("❌ pip install requests"); sys.exit(1)

from voix_lente import ralentir_si_enseignante

RACINE = Path(__file__).resolve().parent
SORTIE = RACINE / "assets/interactive/module-n6-relations"
MANIFESTE = RACINE / "sons_module_n6_relations.json"
DIALOGUES_JS = RACINE / "build/contenu/module-n6-relations/dialogues.js"

# Mêmes identifiants que les autres modules, pour que les voix soient les
# mêmes d'un module à l'autre.
VOIX = {
    "enseignante": "mActWQg9kibLro6Z2ouY",   # 👩 féminine #1
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 féminine #2
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # 👨 masculin #1
    "narrateur":   "IPgYtHTNLjC7Bq7IPHrm",   # 👨 narrateur
}

# Quatre personnages, quatre timbres : aucun partage, donc aucune règle de
# non-croisement à vérifier. Seule NARRATRICE prend la voix de l'enseignante,
# ralentie à 0,85 par voix_lente.py — elle ne dit que des **textes écrits**,
# le courriel du Défi 1 et l'article du Défi 3, et un débit posé y est un
# avantage. Les trois personnes qui se parlent gardent un débit normal : au
# niveau 6, la compétence vise le débit normal.
VOIX_PERSO = {
    "MARISOL":    "feminin_2",
    "OUSMANE":    "narrateur",
    "GHISLAIN":   "masculin_1",
    "NARRATRICE": "enseignante",
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
ATTENTE_BASE_S = 4   # 429 et 5xx, doublée à chaque échec : 4, 8, 16, 32 s
ATTENTE_RESEAU_S = 1  # coupure TLS : 1, 2, 4, 8 s — voir parle()


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
            # Une coupure TLS n'est pas un refus de débit : rien ne se calme en
            # attendant une minute, la liaison revient d'elle-même en quelques
            # secondes. Le 21 août, la panne d'ElevenLabs faisait échouer une
            # requête sur deux, et l'attente de 4-8-16-32 s coûtait plus de
            # temps que la génération elle-même — huit extraits par tranche de
            # dix minutes. On garde le doublement, sur une base plus courte.
            # Le 429 et les 5xx, eux, gardent l'attente longue plus bas : là,
            # insister trop vite aggrave vraiment les choses.
            attente = ATTENTE_RESEAU_S * (2 ** (essai - 1))
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
        print(f"❌ {MANIFESTE.name} introuvable — le produire par "
              f"« node build/releve_sons.js module-n6-relations > "
              f"{MANIFESTE.name} », jamais par build/collecte_sons.py")
        sys.exit(1)
    sons = json.loads(MANIFESTE.read_text(encoding="utf-8"))
    for file_id, texte in sons.items():
        taches.append((f"sons/{file_id}", texte, VOIX_MOTS,
                       SORTIE / "sons" / f"{file_id}.mp3"))

    print(f"🔊 module-n6-relations — {len(taches)} extraits "
          f"({sum(len(v) for v in dialogues.values())} répliques "
          f"sur {len(dialogues)} dialogues + {len(sons)} sons)\n")

    ok = saute = echec = 0
    for etiquette, texte, voix, chemin in taches:
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
