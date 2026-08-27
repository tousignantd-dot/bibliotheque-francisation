"""Registre des appels d'API payants du serveur — un appel, une ligne.

Pourquoi ce fichier existe : jusqu'ici, personne ne comptait. La page
« Le prix d'un module » (assets/presentations/prix-dun-module.html) chiffre
un module à 36 $ pour vingt élèves, mais sur des **hypothèses d'usage
inventées** — vingt tours d'assistant, vingt répliques de jeu de rôle. Un
ordre de grandeur, pas une mesure. Ce registre remplace l'hypothèse par le
compte réel.

Même parti pris que `~/Claude/generations/journal_appels.py`, qui tient le
registre des images : **une ligne par tentative**, réussie ou non. Un appel
qui échoue après que le modèle a lu la requête est facturé quand même ; ne
compter que les succès sous-estimerait la facture, ce qui est exactement le
défaut que le registre des images a été écrit pour corriger.

Trois règles qui ne changent pas :

1. **Aucun texte n'entre ici.** Ni la phrase de l'élève, ni la correction,
   ni la question posée à l'assistant. Le registre compte des jetons, il ne
   garde pas ce qui a été dit — les corrections IA restent privées, comme
   partout ailleurs dans ce dépôt.
2. **Aucun code d'élève non plus.** Le code à six caractères *authentifie* :
   l'écrire dans un journal reviendrait à écrire un mot de passe. On garde
   l'`id` de l'élève et celui de son groupe, qui ne servent qu'à recouper
   avec `students.json`.
3. **Les jetons sont ceux que l'API renvoie**, jamais une estimation.
   `usage` arrive dans la réponse ; on le recopie tel quel. Le montant en
   dollars, lui, est calculé à partir d'une table de tarifs écrite ici — donc
   il vieillit, et c'est un montant estimé, jamais la facture.
"""

import json
import os
import threading
from datetime import datetime, timezone
from pathlib import Path

# ── Tarifs ───────────────────────────────────────────────────────────────
# En dollars US par million de jetons. Relevés le 25 août 2026. Ils
# vieillissent : un tarif qui change ici ne réécrit pas les lignes déjà
# posées, qui gardent le montant calculé le jour de l'appel — c'est voulu,
# une ligne du registre dit ce qu'on croyait payer ce jour-là.
#
# Le cache suit la règle d'Anthropic : l'écriture coûte 1,25 fois l'entrée,
# la lecture un dixième. La consigne système du jeu de rôle et de
# l'assistant est mise en cache, d'où l'intérêt de les compter à part.
TARIFS = {
    "claude-haiku-4-5-20251001": {
        "entree": 1.00, "sortie": 5.00,
        "cache_ecriture": 1.25, "cache_lecture": 0.10,
    },
    "claude-opus-5": {
        "entree": 5.00, "sortie": 25.00,
        "cache_ecriture": 6.25, "cache_lecture": 0.50,
    },
}

# La synthèse vocale facture au caractère et ne renvoie aucun montant : c'est
# nous qui multiplions. Un tarif par modèle, donc, et non un seul nombre — le
# 27 août 2026 la route `/api/voix` est passée d'ElevenLabs à Azure, et
# confondre les deux ferait lire l'ancienne dépense au nouveau prix.
#
#   ElevenLabs : 220 $ le million de caractères (déduit du chantier du 24 août,
#                un ordre de grandeur, pas un relevé de facture)
#   Azure      : 16 $ le million, tarif publié pour les voix neuronales
TARIF_VOIX = {
    "eleven_multilingual_v2": 0.00022,
    "azure-fr-CA-neural":     0.000016,
}

# Conservé : d'anciennes lignes du registre n'ont pas de modèle reconnu, et
# les compter à zéro effacerait une dépense réelle.
TARIF_VOIX_PAR_CARACTERE = TARIF_VOIX["eleven_multilingual_v2"]


def tarif_voix(modele):
    return TARIF_VOIX.get(modele, TARIF_VOIX_PAR_CARACTERE)

FOURNISSEURS = {
    "claude-haiku-4-5-20251001": "anthropic",
    "claude-opus-5": "anthropic",
    "eleven_multilingual_v2": "elevenlabs",
    "azure-fr-CA-neural": "azure",
    "azure-stt-fr-CA": "azure",
}

# ── Le fichier ───────────────────────────────────────────────────────────
# Posé par le serveur au démarrage (volume Railway en production). Tant
# qu'il n'est pas posé, `noter()` ne fait rien : un registre absent ne doit
# jamais empêcher un élève de faire corriger sa phrase.
_FICHIER = None
_VERROU = threading.Lock()


def configurer(chemin):
    """Dit où écrire. Appelé une fois par le serveur, au démarrage."""
    global _FICHIER
    _FICHIER = Path(chemin)
    try:
        _FICHIER.parent.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print("[WARN] registre des appels indisponible : %s" % e, flush=True)
        _FICHIER = None
    return _FICHIER


def chemin():
    return _FICHIER


def cout_anthropic(modele, usage):
    """Le coût d'un appel, à partir du `usage` renvoyé par l'API.

    Les quatre compteurs sont facturés à quatre tarifs différents ; les
    additionner comme s'ils étaient un seul nombre de jetons d'entrée
    surestime d'un facteur dix sur une conversation bien mise en cache.
    """
    t = TARIFS.get(modele)
    if not t or not isinstance(usage, dict):
        return None
    par_million = (
        (usage.get("input_tokens") or 0) * t["entree"]
        + (usage.get("output_tokens") or 0) * t["sortie"]
        + (usage.get("cache_creation_input_tokens") or 0) * t["cache_ecriture"]
        + (usage.get("cache_read_input_tokens") or 0) * t["cache_lecture"]
    )
    return round(par_million / 1_000_000, 8)


def noter(route, modele, eleve_id=None, groupe_id=None, module=None,
          usage=None, caracteres=None, statut="ok", http=None):
    """Pose une ligne. N'échoue jamais l'appelant.

    Un registre qui fait planter le geste qu'il enregistre est pire que pas
    de registre : on perdrait l'appel *et* la trace. Même règle que
    `journal()` pour l'audit du réseau.
    """
    if _FICHIER is None:
        return
    try:
        ligne = {
            "quand": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "route": route,
            "fournisseur": FOURNISSEURS.get(modele, "inconnu"),
            "modele": modele,
            "eleve": eleve_id,
            "groupe": groupe_id,
            "module": module,
            "statut": statut,
            "http": http,
        }
        if caracteres is not None:
            # Voix : ElevenLabs compte des caractères, pas des jetons.
            ligne["caracteres"] = caracteres
            ligne["cout_usd"] = round(caracteres * tarif_voix(modele), 8)
        else:
            u = usage if isinstance(usage, dict) else {}
            ligne["jetons"] = {
                "entree": u.get("input_tokens"),
                "sortie": u.get("output_tokens"),
                "cache_ecriture": u.get("cache_creation_input_tokens"),
                "cache_lecture": u.get("cache_read_input_tokens"),
            }
            ligne["cout_usd"] = cout_anthropic(modele, u)
        if statut != "ok":
            # Un appel servi par le cache n'a jamais atteint le fournisseur ;
            # un appel refusé (401, quota épuisé) n'a rien produit. Les deux
            # gardent leur nombre de caractères — c'est ce qui permet de dire
            # ce que le cache a épargné — mais leur montant tombe à zéro.
            ligne["cout_usd"] = 0.0
        with _VERROU:
            with open(_FICHIER, "a", encoding="utf-8") as f:
                f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    except (OSError, TypeError, ValueError) as e:
        print("[WARN] registre des appels : %s" % e, flush=True)


# ── Lecture ──────────────────────────────────────────────────────────────

def lire(depuis=None, fichier=None):
    """Rend les lignes du registre, les plus anciennes d'abord.

    `depuis` est une date ISO (« 2026-08-25 ») : les lignes antérieures sont
    sautées. La comparaison est lexicographique, ce qui marche parce que les
    horodatages sont en ISO et tous en temps universel.
    """
    f = Path(fichier) if fichier else _FICHIER
    if not f or not f.exists():
        return []
    lignes = []
    try:
        with open(f, encoding="utf-8") as fh:
            for brute in fh:
                brute = brute.strip()
                if not brute:
                    continue
                try:
                    d = json.loads(brute)
                except json.JSONDecodeError:
                    continue  # une ligne tronquée ne condamne pas le reste
                if depuis and (d.get("quand") or "") < depuis:
                    continue
                lignes.append(d)
    except OSError as e:
        print("[WARN] registre des appels illisible : %s" % e, flush=True)
    return lignes


def _vide():
    return {"appels": 0, "echecs": 0, "cache": 0, "cout_usd": 0.0,
            "economie_cache_usd": 0.0,
            "jetons_entree": 0, "jetons_sortie": 0, "caracteres": 0,
            "parRoute": {}}


def _ajouter(seau, d):
    seau["appels"] += 1
    statut = d.get("statut")
    if statut == "cache":
        seau["cache"] += 1
        seau["economie_cache_usd"] += ((d.get("caracteres") or 0)
                                       * tarif_voix(d.get("modele")))
    elif statut != "ok":
        seau["echecs"] += 1
    seau["cout_usd"] += d.get("cout_usd") or 0
    j = d.get("jetons") or {}
    seau["jetons_entree"] += (j.get("entree") or 0) + (j.get("cache_lecture") or 0) \
        + (j.get("cache_ecriture") or 0)
    seau["jetons_sortie"] += j.get("sortie") or 0
    seau["caracteres"] += d.get("caracteres") or 0
    r = seau["parRoute"].setdefault(
        d.get("route") or "?", {"appels": 0, "cout_usd": 0.0})
    r["appels"] += 1
    r["cout_usd"] = round(r["cout_usd"] + (d.get("cout_usd") or 0), 6)


def _arrondir(seau):
    seau["cout_usd"] = round(seau["cout_usd"], 6)
    seau["economie_cache_usd"] = round(seau["economie_cache_usd"], 6)
    return seau


def par_eleve(lignes, eleves=None):
    """Regroupe par élève. `eleves` restreint à un ensemble d'`id`.

    Rend un dictionnaire `{id: seau}` plus le seau `total`. Un appel sans
    élève — le tri d'un signalement, par exemple — tombe dans `sansEleve` :
    il est payé, il doit se voir, mais il n'est imputable à personne.
    """
    par = {}
    total = _vide()
    for d in lignes:
        eid = d.get("eleve")
        if eleves is not None and eid is not None and eid not in eleves:
            continue
        cle = eid if eid is not None else "sansEleve"
        _ajouter(par.setdefault(cle, _vide()), d)
        _ajouter(total, d)
    for seau in par.values():
        _arrondir(seau)
    return {"parEleve": par, "total": _arrondir(total)}


def par_cle(lignes, cle_de_ligne):
    """Regroupe par une clé que l'appelant calcule lui-même.

    `par_eleve` répond à « combien cet élève a-t-il coûté ? ». La direction
    d'un centre pose la même question d'un cran plus haut — par enseignant,
    par centre — et le registre ne porte ni l'un ni l'autre : il note l'élève
    et le **groupe**. La clé se dérive donc (groupe → titulaire, groupe →
    centre) et se passe ici, plutôt que d'ajouter au registre deux champs qui
    seraient faux le jour où un groupe change de titulaire.

    Une ligne dont la clé est None tombe dans `sansCle` : elle est payée, elle
    doit se voir, et elle n'est imputable à personne — le tri d'un signalement
    en est un cas. La rendre invisible ferait un total qui ne se recompose pas.
    """
    par = {}
    total = _vide()
    for d in lignes:
        cle = cle_de_ligne(d)
        _ajouter(par.setdefault(cle if cle is not None else "sansCle", _vide()), d)
        _ajouter(total, d)
    for seau in par.values():
        _arrondir(seau)
    return {"parCle": par, "total": _arrondir(total)}
