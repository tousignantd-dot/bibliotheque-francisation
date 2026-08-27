#!/usr/bin/env python3
"""Ce qu'un groupe coûte en mode IA, pour une session — un modèle, pas un relevé.

    python3 build/cout_groupe.py                    # 20 élèves, niveau 5
    python3 build/cout_groupe.py --eleves 30 --modules 16
    python3 build/cout_groupe.py --voix elevenlabs  # l'ancienne facture, pour comparer

Pourquoi un script et non un chiffre
------------------------------------
La page « Le prix d'un module » annonce 36 $ sans dire d'où ça sort, et le
registre des appels compte six lignes — dont quatre en échec. Personne ne
**sait** ce que coûte le mode IA. Ce script ne le sait pas davantage : il rend
le calcul explicite, avec ses hypothèses en clair, pour qu'on puisse les
discuter une par une et les remplacer par des mesures dès qu'on en aura.

Les tarifs, eux, ne sont pas des hypothèses : ils viennent de `journal_api.py`,
qui sert aussi à facturer les appels réels.

Ce qui est solide et ce qui ne l'est pas
----------------------------------------
**Solide** : les tarifs, le nombre de modules par niveau, le fait que chaque
module câble un jeu de rôle, une lecture et une analyse d'erreurs.

**Fragile** : combien de tours dure un jeu de rôle, combien de fois un élève
demande une correction, la longueur d'une réplique. Ce sont les trois nombres
qui décident du résultat, et aucun n'est mesuré. Ils sont donc en tête du
fichier, nommés, et le script affiche à quel point le total y est sensible.

Le jeu de rôle domine tout
--------------------------
Il tourne sur `claude-opus-5` — 5 $ le million en entrée, 25 $ en sortie —
alors que les corrections utilisent Haiku, vingt-cinq fois moins cher en
sortie. Un seul échange de dix tours pèse plus que toutes les corrections d'un
module. C'est là qu'est le levier, pas dans les corrections.
"""
import argparse
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import journal_api  # noqa: E402

# ── Les hypothèses. C'est ici qu'on discute. ────────────────────────────────
TOURS_JEU_DE_ROLE = 10      # répliques de l'assistant dans un échange
CARACTERES_REPLIQUE = 120   # longueur d'une réplique lue à voix haute
CORRECTIONS_ECRITES = 3     # productions écrites soumises par module
CORRECTIONS_COURTES = 20    # phrases corrigées au fil des exercices

# Jetons par appel — ordres de grandeur, à remplacer par des mesures.
# L'entrée du jeu de rôle grandit avec l'historique : 800 est la moyenne d'un
# échange de dix tours, pas le premier tour.
JETONS = {
    "jeu-de-role":      {"entree": 800, "sortie": 200, "systeme": 300},
    "analyser-erreurs": {"entree": 600, "sortie": 400, "systeme": 300},
    "corriger-phrase":  {"entree": 200, "sortie": 60,  "systeme": 180},
}

MODULES_PAR_NIVEAU = {5: 14}


def cout_appel(modele, entree, sortie, systeme=0, cache=False):
    """Le coût d'un appel. `cache` : la consigne système est relue, pas réécrite."""
    t = journal_api.TARIFS[modele]
    if cache:
        sys_cout = systeme * t["cache_lecture"]
    else:
        sys_cout = systeme * t["cache_ecriture"]
    return (entree * t["entree"] + sortie * t["sortie"] + sys_cout) / 1_000_000


def par_eleve_par_module(voix="azure"):
    """Détail du coût d'un élève sur un module. Renvoie (postes, total)."""
    postes = {}

    # 1. Le jeu de rôle : un tour paie l'écriture du cache, les autres la lecture.
    j = JETONS["jeu-de-role"]
    postes["jeu de rôle (opus-5)"] = (
        cout_appel("claude-opus-5", j["entree"], j["sortie"], j["systeme"])
        + (TOURS_JEU_DE_ROLE - 1)
        * cout_appel("claude-opus-5", j["entree"], j["sortie"], j["systeme"],
                     cache=True))

    # 2. La voix de l'assistant, une par tour.
    modele_voix = ("azure-fr-CA-neural" if voix == "azure"
                   else "eleven_multilingual_v2")
    postes["voix lue (%s)" % voix] = (
        TOURS_JEU_DE_ROLE * CARACTERES_REPLIQUE
        * journal_api.tarif_voix(modele_voix))

    # 3. Les corrections, toutes sur Haiku.
    a = JETONS["analyser-erreurs"]
    postes["analyses d'écrit (haiku)"] = CORRECTIONS_ECRITES * cout_appel(
        "claude-haiku-4-5-20251001", a["entree"], a["sortie"], a["systeme"],
        cache=True)
    c = JETONS["corriger-phrase"]
    postes["corrections courtes (haiku)"] = CORRECTIONS_COURTES * cout_appel(
        "claude-haiku-4-5-20251001", c["entree"], c["sortie"], c["systeme"],
        cache=True)
    return postes, sum(postes.values())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--eleves", type=int, default=20)
    ap.add_argument("--modules", type=int, default=MODULES_PAR_NIVEAU[5])
    ap.add_argument("--voix", choices=("azure", "elevenlabs"), default="azure")
    a = ap.parse_args()

    postes, unite = par_eleve_par_module(a.voix)
    print("Hypothèses : %d tours de jeu de rôle, %d caractères par réplique,"
          % (TOURS_JEU_DE_ROLE, CARACTERES_REPLIQUE))
    print("             %d écrits et %d phrases corrigées par module.\n"
          % (CORRECTIONS_ECRITES, CORRECTIONS_COURTES))
    print("%-30s %12s %10s" % ("poste", "$/élève/mod", "part"))
    print("-" * 54)
    for k, v in sorted(postes.items(), key=lambda x: -x[1]):
        print("%-30s %12.4f %9.0f %%" % (k, v, v / unite * 100))
    print("-" * 54)
    print("%-30s %12.4f\n" % ("total", unite))

    total = unite * a.modules * a.eleves
    print("%d élèves × %d modules = %s **%.2f $** pour la session"
          % (a.eleves, a.modules, " " * 6, total))
    print("   soit %.2f $ par élève, %.2f $ par module et par élève"
          % (unite * a.modules, unite))

    # La sensibilité : ce sont les hypothèses qui décident, pas les tarifs.
    print("\nSi les hypothèses bougent de moitié ou du double :")
    for nom, mult in (("moitié moins d'usage", 0.5), ("deux fois plus", 2.0)):
        print("   %-24s %8.2f $" % (nom, total * mult))

    if a.voix == "azure":
        _, avant = par_eleve_par_module("elevenlabs")
        ecart = (avant - unite) * a.modules * a.eleves
        print("\nAvec l'ancienne voix ElevenLabs : %.2f $ — la bascule du "
              "27 août en épargne %.2f $ (%.0f %%)."
              % (avant * a.modules * a.eleves, ecart,
                 ecart / (avant * a.modules * a.eleves) * 100))
    return 0


if __name__ == "__main__":
    sys.exit(main())
