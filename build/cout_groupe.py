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

# Jetons par appel. Le jeu de rôle est **mesuré** : six tours joués contre
# `claude-opus-5` le 27 août 2026, sur le scénario « louer / cas A », avec les
# phrases fautives d'un vrai élève de niveau 5. Total relevé : 1 405 jetons
# d'entrée, 531 de sortie, 5 820 lus en cache, pour 0,023 21 $.
#
# La mesure a corrigé une erreur d'un facteur 2,4 : j'avais supposé 800 jetons
# d'entrée et 200 de sortie par tour, la réalité est 234 et 88. Une réplique de
# jeu de rôle est courte — deux phrases — et l'historique part en cache dès le
# deuxième tour, où il coûte le dixième. Supposer large n'est pas « prudent »,
# c'est faux.
#
# Les deux routes de correction, elles, restent des hypothèses : personne ne
# les a mesurées. Elles pèsent 14 % du total, donc l'erreur qu'elles portent
# est bornée.
JETONS = {
    "jeu-de-role":      {"entree": 234, "sortie": 88, "cache_lu": 970,
                         "mesure": True},
    "analyser-erreurs": {"entree": 600, "sortie": 400, "systeme": 300},
    "corriger-phrase":  {"entree": 200, "sortie": 60,  "systeme": 180},
}

MODULES_PAR_NIVEAU = {5: 14}

# Le modèle du jeu de rôle. `server.py` emploie Opus-5 ; Haiku est l'option
# étudiée. Attention : ce n'est **pas** une constante à changer telle quelle —
# le serveur envoie `"thinking": {"type": "adaptive"}`, que Haiku 4.5 refuse
# avec un 400. Basculer demande aussi de retirer ce paramètre.
MODELE_JEU_DE_ROLE = "claude-opus-5"


def cout_appel(modele, entree, sortie, systeme=0, cache=False, cache_lu=0):
    """Le coût d'un appel.

    `cache_lu` est le nombre de jetons **relevés** en lecture de cache ; il
    prend le pas sur `systeme`, qui n'est qu'une estimation de la consigne.
    """
    t = journal_api.TARIFS[modele]
    if cache_lu:
        sys_cout = cache_lu * t["cache_lecture"]
    elif cache:
        sys_cout = systeme * t["cache_lecture"]
    else:
        sys_cout = systeme * t["cache_ecriture"]
    return (entree * t["entree"] + sortie * t["sortie"] + sys_cout) / 1_000_000


def par_eleve_par_module(voix="azure"):
    """Détail du coût d'un élève sur un module. Renvoie (postes, total)."""
    postes = {}

    # 1. Le jeu de rôle, sur les jetons relevés. Le cache lu par tour est une
    #    moyenne : il grandit avec l'historique, donc un échange plus long
    #    coûte un peu plus que proportionnellement. L'écart reste sous 10 %
    #    jusqu'à une quinzaine de tours.
    j = JETONS["jeu-de-role"]
    postes["jeu de rôle (%s)" % MODELE_JEU_DE_ROLE.split("-")[1]] = (
        TOURS_JEU_DE_ROLE
        * cout_appel(MODELE_JEU_DE_ROLE, j["entree"], j["sortie"],
                     cache_lu=j["cache_lu"]))

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
    ap.add_argument("--tours", type=int, default=TOURS_JEU_DE_ROLE)
    ap.add_argument("--modele-jeu", default=MODELE_JEU_DE_ROLE,
                    choices=tuple(journal_api.TARIFS))
    a = ap.parse_args()
    globals()["TOURS_JEU_DE_ROLE"] = a.tours
    globals()["MODELE_JEU_DE_ROLE"] = a.modele_jeu

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
