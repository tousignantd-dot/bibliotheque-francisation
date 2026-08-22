# -*- coding: utf-8 -*-
"""A4 · Les six étapes, et les questions qui vont avec
Bloc A « Je découvre » · couleur teal · 75 min. Séance de synthèse du bloc.
Source : exercices `prEtapes` et `prImg`, mini-leçon `prEtapes`, les seize
cartes de FC_CARDS de la section « Je découvre ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre="Les six étapes, et les questions qui vont avec",
        chapeau="Chaque étape produit un objet et se prépare par une "
                "question. Une étape dont il ne reste rien d'écrit n'a pas "
                "eu lieu.",
        duree='75 minutes')

    d.titre(notes="Séance de synthèse du bloc A. Reprendre au tableau la liste des "
                  "six étapes avant de commencer, sans regarder les notes : le "
                  "groupe la reconstitue en trois minutes.")

    d.objectifs([
        "remettre les six étapes dans l'ordre ;",
        "dire ce que chacune produit et ce qu'elle ne produit pas ;",
        "poser la question qui prépare chaque étape ;",
        "décrire les lieux du chantier avant qu'il commence.",
    ], notes="Le troisième objectif annonce le bloc D : on y reviendra, et il vaut "
             "mieux que le groupe le sache dès maintenant.")

    d.declencheur(
        'Observation', "Vous avez une soumission en main. Que reste-t-il à faire avant de signer ?",
        pistes=[
            "Que savez-vous de l'état réel du bâtiment ?",
            "Que savez-vous de l'entreprise elle-même ?",
            "Que savez-vous de ce que la ville demandera ?",
        ],
        notes="Trois questions, trois étapes oubliées. Le groupe trouvera "
              "l'inspection ; la licence et le permis viennent plus difficilement.")

    d.tableau('Analyse', "Ce que chaque étape produit",
              ["L'étape", 'Ce qu\'elle produit'],
              [["L'inspection", "un rapport écrit, sans prix"],
               ["La licence", "une vérification, en deux minutes"],
               ["La soumission", "un prix par ligne, et des exclusions"],
               ["Le permis", "un accord, et un délai"],
               ["L'échéancier", "une date par étape"]],
              cle=0,
              note="La sixième étape, la réunion de chantier, arrive quand les travaux sont commencés.",
              notes="Diapositive à photographier. Ne pas ajouter la sixième rangée : "
                    "elle se traite en D1, et la diapositive à six rangées avec une "
                    "note passe mal.")

    d.tableau('Analyse', "Ce qu'une inspection ne fait pas",
              ['Elle ne fait pas', 'Pourquoi'],
              [["chiffrer les travaux", "ce serait le travail de l'entrepreneur"],
               ["recommander quelqu'un", "elle aurait alors un intérêt dans le chantier"],
               ["voir derrière les murs", "elle est visuelle et non destructive"],
               ["valoir deux ans plus tard", "elle décrit l'état à une date précise"]],
              cle=0,
              note="Ce qu'elle ne fait pas est exactement ce qui lui donne sa valeur.",
              notes="Diapositive à photographier. C'est le point le plus mal compris "
                    "du bloc : beaucoup d'élèves trouvent qu'une inspection qui ne "
                    "propose rien coûte cher pour rien. Prendre le temps.")

    d.regle("Une étape dont il ne reste rien n'a pas eu lieu",
            "Un papier, une date ou une confirmation : chaque étape laisse une trace.",
            precision="Un prix donné de vive voix n'engage personne. Une licence "
                      "« sûrement bonne » ne se vérifie pas. Un permis « qu'on "
                      "demandera plus tard » retarde tout le chantier. La trace "
                      "écrite n'est pas de la méfiance : c'est ce qui permet à tout "
                      "le monde de travailler.",
            notes="Diapositive à photographier. C'est la règle du bloc A au complet.")

    d.pratique('Pratique', "Quelle question, à quelle étape ?",
               "Associez chaque question à l'étape qu'elle prépare.", [
        ("Est-ce que votre rapport écrit ce que vous n'avez pas pu voir ?", "l'inspection"),
        ("Quel est votre numéro de licence ?", "la vérification"),
        ("Quelles sont les exclusions ?", "la soumission"),
        ("Quel délai je dois prévoir ?", "le permis"),
        ("Le séchage est-il compté dans les six semaines ?", "l'échéancier"),
        ("Vous m'écrivez ça aujourd'hui ?", "la réunion de chantier"),
    ], corrige=True,
       notes="Faire poser les questions à voix haute, en se regardant deux par deux. "
             "C'est la première fois de la session que les élèves formulent une "
             "question de chantier ; elles reviendront toutes en D2 et en E1.")

    d.vocabulaire('Vocabulaire', "Les mots du départ, révision", [
        ("un entrepreneur général", "Celui qui prend le chantier en charge et qui fait venir chaque métier."),
        ("un corps de métier", "Une spécialité du bâtiment : maçonnerie, plomberie, électricité."),
        ("une soumission", "Le prix écrit, avec le détail de ce qui sera fait."),
        ("un permis de rénovation", "L'autorisation de la municipalité, qui se demande à elle seule."),
    ], notes="Révision rapide, cinq minutes. Puis faire décrire à voix haute les cinq "
             "lieux de l'exercice 4 du module : le sous-sol, le mur de fondation, le "
             "terrain, la table de cuisine, le plancher ouvert.")

    d.pratique('Écriture', "Décrire ce qu'on voit",
               "Écrivez une phrase par lieu, comme dans un rapport.", [
        ("le sous-sol non aménagé", "Le sous-sol n'est pas fini : plancher de béton, murs de fondation apparents."),
        ("le mur de fondation nord", "Une fissure oblique traverse le mur sur environ un mètre."),
        ("la bande de terre le long du mur", "Le sol descend vers la maison et l'eau s'accumule au pied du mur."),
        ("la table de cuisine du soir", "Deux documents sont ouverts côte à côte, avec une calculatrice."),
    ], corrige=True,
       notes="Exercice d'écriture court, mais c'est le premier du module. Insister sur "
             "un point : une phrase de rapport donne un chiffre ou une mesure quand "
             "elle le peut. « Un mètre », « deux mètres », « quarante centimètres ».")

    d.billet(
        "Laquelle des six étapes serais-tu tenté de sauter, et pourquoi ?",
        exemples=[
            "Sois honnête : tout le monde en saute au moins une.",
            "Dis ce que ça pourrait coûter.",
        ],
        notes="Trois minutes. Fin du bloc A. Annoncer le bloc B : à partir de la "
              "prochaine séance, on entre dans le sous-sol avec l'entrepreneur, et "
              "on écoute une explication de vingt minutes.")

    return d.save(dossier)
