#!/usr/bin/env python3
"""
Générateur d'audio — la banque du niveau 1 (ateliers 124 à 145).

Un seul générateur pour toute la banque, au lieu d'un par atelier. Ce que les
ateliers ont en commun est exactement ce dont l'audio a besoin : une liste
d'items, chacun avec un slug et un texte à dire. Le reste — la forme de
l'exercice — ne le regarde pas.

    python3 generer_audio_banque_n1.py                 # tout ce qui manque
    python3 generer_audio_banque_n1.py heure dates     # seulement ces ateliers
    python3 generer_audio_banque_n1.py --compter       # chiffre sans rien payer
    python3 generer_audio_banque_n1.py --force         # refait même ce qui existe

**Il n'a jamais été lancé.** Le compte ElevenLabs était à zéro crédit
(401 `quota_exceeded`) le 24 août 2026, et la consigne de production était de
tout préparer sans produire un seul MP3. `--compter` donne le volume et le
coût sans appeler l'API : à passer avant de recharger le compte.

Ce qui est dit
--------------
Le champ **`dit`** d'un item, s'il existe ; sinon son `nom`. La nuance n'est
pas cosmétique : « app. » lu à voix haute ne donne aucun mot français, donc
les abréviations portent un `dit` qui est le mot entier. Une liste de mots
isolés passe par `enrichir()`, qui donne au modèle du français avant et après
sans le faire prononcer — sans quoi « radio », « six » ou « un » ressortent à
l'anglaise ou à l'espagnole.

La voix est celle de l'enseignante, ralentie à 0,85 par `voix_lente` : la même
que les mots isolés des quatre modules du niveau 1, pour qu'un mot ne change
pas de bouche en changeant d'activité.

**Le bac à sable réseau bloque `api.elevenlabs.io`.** Lancer avec
`dangerouslyDisableSandbox`, comme le dit `docs/deux-agents-en-parallele.md`.
"""
import json
import os
import sys
import time
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
INTER = RACINE / "assets/interactive"

VOIX_ENSEIGNANTE = "mActWQg9kibLro6Z2ouY"   # 👩 féminine #1, ralentie à 0,85

ESSAIS = 5           # tentatives par extrait
ATTENTE_BASE_S = 4   # doublée à chaque échec : 4, 8, 16, 32 s

# ElevenLabs facture au caractère. Le tarif observé sur ce compte, en août
# 2026, tourne autour de 0,00018 $ par caractère — il sert à donner un ordre
# de grandeur avec `--compter`, pas à prédire une facture.
DOLLARS_PAR_CARACTERE = 0.00018

# Les ateliers de la banque et la façon de lire leur contenu. `polices-n1` est
# le seul à porter son contenu dans `mots.json` — il est antérieur au format
# commun `contenu.json`, et le renommer casserait une activité livrée.
ATELIERS = {
    # Famille A — apparier. Le texte dit est le `nom` de la chose.
    'polices-n1':        ('mots.json',    'terme'),
    'heure-n1':          ('contenu.json', 'nom'),
    'abreviations-n1':   ('contenu.json', 'nom'),
    'dates-n1':          ('contenu.json', 'nom'),
    'chiffres-n1':       ('contenu.json', 'nom'),
    'panneaux-n1':       ('contenu.json', 'nom'),
    'lettres-n1':        ('contenu.json', 'nom'),
    # Famille C — construire une phrase. Le texte dit est la phrase entière,
    # avec sa ponctuation : c'est le modèle que l'élève doit pouvoir répéter.
    'phrase-ordre-n1':   ('contenu.json', 'phrase'),
    'question-n1':       ('contenu.json', 'phrase'),
    'negatif-n1':        ('contenu.json', 'phrase'),
    'possessifs-n1':     ('contenu.json', 'phrase'),
    'feminin-n1':        ('contenu.json', 'phrase'),
    'nombres-phrase-n1': ('contenu.json', 'phrase'),
    'syllabes-n1':       ('contenu.json', 'phrase'),
    # Famille B — écouter. Ici le champ `dit` est obligatoire et il gagne
    # toujours : il porte la forme orale réelle (« Chu mécanicien »), qui
    # n'est justement pas ce qui est écrit sur le bouton.
    'voyelles-n1':       ('contenu.json', 'dit'),
    'consonnes-n1':      ('contenu.json', 'dit'),
    'e-muet-n1':         ('contenu.json', 'dit'),
    'intonation-n1':     ('contenu.json', 'dit'),
    'formes-rapides-n1': ('contenu.json', 'dit'),
    'jean-dit-n1':       ('contenu.json', 'dit'),
}


def taches_de(slug):
    """Les extraits d'un atelier : (slug de l'item, texte dit, chemin du MP3)."""
    fichier, defaut = ATELIERS[slug]
    chemin = INTER / slug / fichier
    if not chemin.exists():
        return []
    brut = json.loads(chemin.read_text(encoding="utf-8"))
    items = brut if isinstance(brut, list) else brut.get('items', [])
    out = []
    for it in items:
        texte = it.get('dit') or it.get(defaut) or it.get('nom')
        rel = it.get('audio') or ('audio/%s.mp3' % it['slug'])
        out.append((it['slug'], texte, INTER / slug / rel))
    return out


def parle(cle, texte, voix, chemin):
    """Un extrait, avec reprise sur coupure réseau.

    Copiée de `generer_audio_module_n2_autobus.py`, comme le demande
    `docs/deux-agents-en-parallele.md` : ElevenLabs coupe la liaison par
    intermittence. Une panne passagère du fournisseur n'est pas une erreur du
    programme — on réessaie en doublant l'attente, échec après cinq essais.
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


def compter(slugs):
    """Le volume et l'ordre de grandeur du coût, sans appeler l'API."""
    total_c = total_n = deja = 0
    print("  atelier             manquants   caractères")
    for slug in slugs:
        taches = taches_de(slug)
        manquants = [t for t in taches if not t[2].exists()]
        deja += len(taches) - len(manquants)
        c = sum(len(t[1]) for t in manquants)
        total_c += c; total_n += len(manquants)
        print("  %-18s %9d %12d" % (slug, len(manquants), c))
    print("  %-18s %9d %12d" % ('TOTAL', total_n, total_c))
    print("\n%d extrait(s) déjà sur le disque, jamais repayé(s)." % deja)
    print("Ordre de grandeur : %.2f $ à %.5f $/caractère." %
          (total_c * DOLLARS_PAR_CARACTERE, DOLLARS_PAR_CARACTERE))
    print("Ce n'est pas une facture — voir la mémoire « coût des médias ».")
    return 0


def main():
    argv = sys.argv[1:]
    voulus = [a for a in argv if not a.startswith('--')]
    slugs = [s for s in ATELIERS if not voulus or any(v in s for v in voulus)]
    if not slugs:
        sys.exit("❌ aucun atelier ne correspond à %s" % ', '.join(voulus))

    if '--compter' in argv:
        return compter(slugs)

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

    force = "--force" in argv
    ok = saute = echec = 0
    for slug in slugs:
        taches = taches_de(slug)
        print(f"\n🔊 {slug} — {len(taches)} extraits")
        for nom, texte, chemin in taches:
            if chemin.exists() and not force:
                saute += 1
                continue
            print(f"  · {texte[:34]:<36}", end="", flush=True)
            if parle(cle, texte, VOIX_ENSEIGNANTE, chemin):
                print(" ✅"); ok += 1
            else:
                echec += 1

    print(f"\n{ok} écrits · {saute} déjà là · {echec} en échec")
    return 1 if echec else 0


if __name__ == "__main__":
    sys.exit(main())
