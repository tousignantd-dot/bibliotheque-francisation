# -*- coding: utf-8 -*-
"""A4 · Un fait, ou une opinion ?
Bloc A « Je découvre » · couleur teal · écoute et réponds · 75 min.
Source : exercices `prFaitOpinion` et `prImg`, mini-leçon `prFaitOpinion`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n7-actualite/images/')


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre="Un fait, ou une opinion ?",
        chapeau="Une seule question sépare les deux, et elle tient en six "
                "mots : est-ce que je pourrais aller vérifier ? Tout le reste "
                "du module repose sur ce tri.",
        duree='75 minutes')

    d.titre(notes="Séance charnière du bloc A. Si une seule chose doit rester du module "
                  "dans dix ans, c'est celle-ci. Prendre le temps.")

    d.objectifs([
        "distinguer un fait d'une opinion par un test unique ;",
        "repérer les mots qui trahissent un jugement ;",
        "reconnaître un jugement déguisé en constat ;",
        "accepter qu'un fait puisse être faux sans cesser d'être un fait.",
    ], notes="Le quatrième objectif désarçonne toujours. Il est pourtant décisif : "
             "confondre « fait » et « vérité » empêche de comprendre ce qu'est une "
             "vérification.")

    d.declencheur(
        'Observation', "Ces deux phrases se ressemblent. En quoi diffèrent-elles ?",
        image=IMG + 'journal-etale.jpg',
        pistes=[
            "« Le local est vide depuis deux ans. »",
            "« Ce local vide fait honte au quartier. »",
            "Laquelle pourriez-vous aller vérifier ?",
            "Laquelle deux personnes raisonnables pourraient-elles contester ?",
        ],
        notes="Écrire les deux phrases au tableau et ne rien expliquer avant que le "
              "groupe ait cherché. La différence doit se trouver, pas s'annoncer.")

    d.regle("Le test unique",
            "Est-ce que je pourrais aller vérifier ?",
            precision="Si oui, c'est un fait. Si la réponse dépend de qui on interroge, "
                      "c'est une opinion. Un fait n'est pas forcément vrai : « la "
                      "consigne est de trente cents » est un fait, et il est faux. Ce "
                      "qui le définit, c'est qu'on peut aller le contredire.",
            notes="Diapositive à photographier. La phrase sur la consigne à trente "
                  "cents fait toujours réagir ; c'est exactement pour cela qu'elle est "
                  "là.")

    d.tableau('Analyse', "Ce qui trahit l'un et l'autre",
              ['Le fait', 'L\'opinion'],
              [["des chiffres : huit places, quinze minutes", "des adjectifs de valeur : ridicule, scandaleux"],
               ["des dates : le 14 octobre", "des adverbes : trop, enfin, encore une fois"],
               ["des noms précis : le conseil municipal", "des verbes : je trouve, il faudrait"],
               ["un verbe neutre : est, a été retenu", "une question qui n'attend pas de réponse"]],
              cle=0,
              note="Le fait n'a besoin d'aucun adjectif pour tenir debout.",
              notes="Diapositive à photographier. Faire chercher dans le journal du jour "
                    "un exemple de chaque colonne, si le groupe en a un sous la main.")

    d.piege("Le jugement déguisé en constat",
            "Ce projet a été imposé au quartier.",
            "Ce projet a été recommandé par le comité.",
            "Les deux phrases ont la même forme grammaticale : une phrase passive au "
            "passé composé. Mais « recommander » se constate, tandis qu'« imposer » "
            "suppose déjà qu'on a mal agi. Le test qui les sépare : remplacez le mot "
            "par un synonyme neutre. Si le sens change beaucoup, il y avait un jugement "
            "caché.",
            notes="C'est le cas difficile de la séance, et celui qui revient en D1 avec "
                  "la chronique. Le poser ici, sans exiger qu'il soit maîtrisé.")

    d.pratique('Tri', "Fait ou opinion ?",
               "Pour chaque phrase, appliquez le test.", [
        ("La consigne est de vingt-cinq cents sur le verre de 500 ml et plus.", "fait - vérifiable"),
        ("Le quartier attend ce service depuis bien trop longtemps.", "opinion - « trop » ne se mesure pas"),
        ("Le local de la rue Boisjoli est vide depuis deux ans.", "fait - on peut aller voir"),
        ("La Ville a encore une fois décidé sans consulter personne.", "opinion - « encore une fois » juge"),
        ("Le dépanneur d'en face dispose de huit places.", "fait - ça se compte"),
        ("Quinze minutes, c'est ridicule pour décharger des sacs.", "opinion - « ridicule » est une appréciation"),
        ("Le conseil doit se prononcer le 14 octobre.", "fait - c'est une date"),
        ("Il serait scandaleux de fermer le dépôt à dix-sept heures.", "opinion - jugement et réclamation"),
    ], corrige=True,
       notes="Corrigé masqué au premier passage. Faire nommer, pour chaque opinion, le "
             "mot exact qui la trahit : c'est ce repérage qui s'exporte.")

    d.cartes("Les faits du dossier, vérifiés", "Ce qu'on peut affirmer sans risque", [
        ("La consigne ordinaire",
         "Dix cents sur les contenants visés, depuis le 1er novembre 2023."),
        ("Le verre de 500 ml et plus",
         "Vingt-cinq cents, depuis la même date."),
        ("Le plastique",
         "Consigné depuis le 1er mars 2025."),
        ("Le verre et le multicouche",
         "S'ajouteront en mars 2027."),
    ], notes="Ces quatre données sont vérifiées sur les sites officiels et ne "
             "s'inventent pas. Elles servent de banc d'essai : ce sont des faits, et "
             "l'élève peut les citer sans crainte.")

    d.billet(
        "Reprenez la nouvelle que vous avez notée en A1. Écrivez-en un fait, puis une opinion.",
        exemples=[
            "Le fait : quelque chose que je pourrais aller vérifier.",
            "L'opinion : ce que j'en pense, annoncé comme tel.",
        ],
        notes="Devoir de fin de bloc. Ramasser : ces deux lignes disent exactement où "
              "en est chaque élève avant d'attaquer le reportage.")

    return d.save(dossier)
