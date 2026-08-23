# -*- coding: utf-8 -*-
"""B1 · Trois façons d'emprunter
Bloc B « Défi 1 · Emprunter moins cher » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf` et son bandeau de quatre mots.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Trois façons d'emprunter",
        chapeau="Une dette ne se règle pas seulement en payant plus : elle se "
                "règle souvent en la remplaçant par une dette moins chère.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc B. Rappeler d'abord le calcul de A1 : 5 640 $ "
                  "versés dans l'année, 400 $ de dette en moins. C'est le problème que "
                  "ce bloc résout.")

    d.objectifs([
        "distinguer une marge de crédit d'un prêt personnel ;",
        "comparer deux taux et dire ce que l'écart représente ;",
        "comprendre ce qu'un dossier de crédit décide ;",
        "employer quatre mots de l'emprunt avec leur article.",
    ], notes="Le deuxième objectif est celui qui demande le plus de travail : comparer "
             "deux taux ne veut rien dire tant qu'on ne les a pas ramenés à des "
             "dollars.")

    d.declencheur(
        'Observation', "Quelle est la différence entre emprunter et devoir ?",
        pistes=[
            "As-tu déjà emprunté sans avoir l'impression d'emprunter ?",
            "Une carte de crédit, est-ce un emprunt ?",
            "Qu'est-ce qui change quand la dette a une date de fin ?",
            "Est-ce qu'un taux plus bas est toujours le meilleur choix ?",
        ],
        notes="La deuxième question surprend : une carte de crédit est un emprunt, et "
              "presque personne ne la nomme ainsi. Le laisser venir du groupe.")

    d.dialogue('Dialogue · 1 de 3', "Trois façons, pas une", [
        ("DAMIEN", "Vous vouliez parler d'une carte de crédit, si j'ai bien lu la note.", True),
        ("MARLÈNE", "Oui. J'ai neuf mille quatre cents dollars à dix-neuf et quatre-vingt-dix, et je paie le minimum depuis trois ans.", True),
        ("DAMIEN", "Le paiement minimum sert à garder le compte en règle, pas à rembourser la dette.", True),
        ("MARLÈNE", "Trois façons ? Je pensais qu'il y avait juste payer plus vite.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="La troisième réplique reprend mot pour mot la conclusion de A1. Le "
             "signaler : le conseiller dit la même chose que la collègue.")

    d.dialogue('Dialogue · 2 de 3', "La marge et le prêt", [
        ("DAMIEN", "La marge, c'est une réserve où vous piochez, et vous payez de l'intérêt seulement sur ce que vous avez pris. Ici, neuf et quarante-cinq.", True),
        ("MARLÈNE", "Neuf et quarante-cinq au lieu de dix-neuf et quatre-vingt-dix. C'est la moitié.", True),
        ("DAMIEN", "Le piège de la marge, c'est qu'elle ne vous oblige à rien. Le prêt personnel, lui, a une date de fin.", True),
        ("MARLÈNE", "Donc la marge est moins chère, mais le prêt me force à finir.", True),
    ], notes="Faire reformuler la dernière réplique par un autre élève. C'est le résumé "
             "de tout le bloc, et il est dit par Marlène, pas par le conseiller.")

    d.dialogue('Dialogue · 3 de 3', "Une question sur vous", [
        ("MARLÈNE", "Vous, vous me conseilleriez lequel ?", True),
        ("DAMIEN", "Je vous poserais une question avant : est-ce que vous avez déjà remboursé une marge au complet dans votre vie ?", True),
        ("MARLÈNE", "Non. Jamais eu de marge.", True),
        ("DAMIEN", "Alors le prêt est probablement plus prudent. Ce n'est pas une question de taux, c'est une question de discipline.", True),
    ], notes="Diapositive à commenter. Un bon conseiller pose une question sur la "
             "personne avant de recommander un produit. C'est ce qu'il faut attendre, "
             "et ce qu'il faut exiger.")

    d.tableau('Analyse', "Les deux produits, côte à côte",
              ['Ce qu\'on compare', 'Marge et prêt'],
              [['le taux', '9,45 % variable contre 11,20 % fixe'],
               ['le versement', 'libre contre 152 $ par mois'],
               ['la fin', 'aucune date contre 80 versements'],
               ["l'intérêt", 'sur la part prise contre sur le tout'],
               ['payer plus vite', 'possible dans les deux cas']],
              cle=0,
              notes="Diapositive à photographier. Elle est le corrigé du travail de B2, "
                    "où le même contenu est lu sur un document.")

    d.vocabulaire('Vocabulaire', "Quatre mots de l'emprunt", [
        ("le taux d'intérêt", "Le prix de l'argent emprunté, dit en pourcentage et calculé pour une année."),
        ("une marge de crédit", "Une réserve d'argent où l'on prend ce qu'on veut, et où l'on ne paie d'intérêt que sur ce qui est pris."),
        ("un prêt personnel", "Une somme prêtée d'un coup, remboursée par versements égaux jusqu'à une date écrite au contrat."),
        ("la cote de crédit", "Le chiffre, entre 300 et 900, qui résume la façon dont une personne a remboursé ses dettes."),
    ], notes="« La cote de crédit » se dit aussi « le pointage ». Donner les deux : les "
             "élèves entendront l'un ou l'autre selon l'institution.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la rencontre avec monsieur Rouillard.", [
        ("La marge offerte est à neuf et quarante-cinq pour cent.", "vrai"),
        ("Le prêt personnel est moins cher que la marge.", "faux - il est un peu plus cher"),
        ("Le prêt se termine à une date écrite au contrat.", "vrai"),
        ("Le conseiller recommande le prêt à cause du taux.", "faux - à cause de la discipline"),
        ("Il demande la permission avant de regarder le dossier de crédit.", "vrai"),
        ("Demander son propre dossier fait baisser le pointage.", "faux - cela n'a aucun effet"),
    ], corrige=True,
       notes="Le dernier énoncé revient en B4 avec sa règle complète. Ne pas le "
             "développer ici : le noter et passer.")

    d.billet("En une phrase : lequel des deux prendrais-tu, et pourquoi ?",
             exemples=["Je prendrais le prêt parce que je veux une date de fin.",
                       "Je prendrais la marge parce que je paie vite."],
             notes="Deux minutes. Garder les billets : ils servent de point de départ à "
                   "la production orale de E1, où la même question est posée en "
                   "quatre-vingt-dix secondes.")

    return d.save(dossier)
