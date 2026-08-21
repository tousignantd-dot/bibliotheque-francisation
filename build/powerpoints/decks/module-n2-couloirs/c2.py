# -*- coding: utf-8 -*-
"""C2 · Indiquer le chemin.
Bloc C « Défi 2 · Demander son chemin » · couleur ambre · 75 min.
Source : dialogue `t2b`, exercices `t2chemin` et `t2ilya`, mini-leçons
`t2chemin` et `t2ilya`.

Le renversement du module a lieu ici : jusqu'à présent, l'élève demandait ;
maintenant il répond. C'est la deuxième intention de production orale du
programme - donner des renseignements sur la localisation.

Deux points de langue : les verbes de direction à l'impératif, qui sont les
mêmes que les consignes de la salle de classe, et le couple « il y a » /
« c'est », qui permet de décrire un bâtiment entier sans un verbe de plus.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-couloirs/images/')


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Indiquer le chemin",
        chapeau="Répondre à quelqu'un qui cherche son chemin, en deux "
                "phrases : l'étage, puis le côté.",
        duree='75 minutes')

    d.titre(notes="Séance de renversement. Le dire au groupe dès le début : aujourd'hui, "
                  "c'est vous qui savez, et quelqu'un d'autre qui est perdu.")

    d.objectifs([
        "employer les quatre verbes du chemin à l'impératif ;",
        "donner l'étage d'abord, le côté ensuite ;",
        "dire il y a pour ce qui existe, c'est pour situer ;",
        "indiquer un chemin en deux phrases, pas plus.",
    ])

    d.declencheur(
        'Renversement', "Quelqu'un vous demande son chemin. Vous dites quoi ?",
        image=IMG + 'corridor-etage.jpg',
        pistes=[
            "Qu'est-ce que vous dites en premier ?",
            "Est-ce qu'il faut tout dire d'un coup ?",
            "Qu'est-ce que la personne peut retenir ?",
            "Qu'est-ce qu'elle fera si elle a oublié ?",
        ],
        notes="Les deuxième et troisième pistes portent toute la séance. Faire essayer "
              "une indication longue, puis demander au groupe de la répéter : personne "
              "n'y arrive, et la règle s'impose d'elle-même.")

    d.dialogue('Dialogue', "Cette fois, c'est Soraya qui répond", [
        ("AMINA", "Excusez-moi, c'est où, la bibliothèque ?", True),
        ("SORAYA", "Au premier étage. C'est le local 108.", True),
        ("AMINA", "C'est loin ?", True),
        ("SORAYA", "Non. Prenez l'escalier, puis à gauche.", True),
        ("AMINA", "Merci ! Et le secrétariat ?", True),
        ("SORAYA", "Ici, au rez-de-chaussée. Le 005, en face de l'accueil.", True),
    ], consigne="Écoutez, puis comptez les phrases de Soraya.",
       notes="Deux phrases par réponse, jamais trois. Faire compter par le groupe : "
             "c'est le modèle de la production orale du bloc E.")

    d.tableau('Analyse', "Les quatre verbes du chemin",
              ["On dit", "Ce que la personne fait"],
              [["Prenez l'escalier.", "elle monte les marches"],
               ["Continuez tout droit.", "elle marche devant elle, sans tourner"],
               ["Tournez à droite.", "elle change de direction"],
               ["Descendez au rez-de-chaussée.", "elle redescend jusqu'en bas"]],
              cle=1,
              note="Ce sont les mêmes formes que les consignes de la classe : ouvrez, "
                   "écoutez, prenez. La terminaison -ez se dit « é ».",
              notes="Diapositive à photographier. Faire jouer les quatre lignes pour "
                    "vrai, dans la classe : le verbe se dit, le geste se fait.")

    d.regle("L'étage d'abord, le côté ensuite",
            "Deux phrases, et la personne part sans se perdre.",
            precision="« C'est au deuxième étage. Prenez l'escalier, puis à droite. » "
                      "Deux informations, deux phrases. Trois indications d'un coup ne "
                      "se retiennent pas, et la personne devra redemander vingt mètres "
                      "plus loin.",
            notes="Diapositive à photographier. C'est la conduite que le jeu de rôle en "
                  "ligne vérifie : l'assistant, qui joue le concierge, fait pareil.")

    d.tableau('Analyse', "Il y a, ou c'est ?",
              ["On dit", "Pour"],
              [["Il y a un ascenseur.", "dire qu'une chose existe"],
               ["Il y a trois étages.", "dire combien il y en a"],
               ["C'est la cafétéria.", "nommer un endroit"],
               ["C'est au deuxième étage.", "situer un endroit"],
               ["Il n'y a pas de local 240.", "dire que ça n'existe pas"]],
              cle=1,
              note="« Il y a » ne change jamais : ni au pluriel, ni au féminin.",
              notes="Diapositive à photographier. Faire produire dix phrases sur le "
                    "vrai centre, cinq de chaque sorte.")

    d.piege('Le piège du jour',
            "« tout droit » pour « à droite »",
            "deux directions différentes",
            "<b>Tout droit</b>, c'est devant soi, sans tourner. <b>À droite</b>, c'est "
            "un virage. Les deux expressions se ressemblent à l'oreille et s'échangent "
            "sans arrêt : le seul remède est de faire le geste en même temps que le "
            "mot, chaque fois.",
            notes="Faire dire les deux, avec le geste, dix fois de suite, de plus en "
                  "plus vite. C'est bête et ça marche.")

    d.pratique('Pratique', "Indiquez le chemin en deux phrases",
               "Une personne cherche. Vous répondez.", [
        ("le local 214", "C'est au deuxième étage. Prenez l'escalier, puis à droite."),
        ("la bibliothèque", "C'est au premier étage. Montez un étage, puis à gauche."),
        ("la cafétéria", "C'est au rez-de-chaussée. Continuez tout droit, à côté des casiers."),
        ("les toilettes", "Il y en a à chaque étage. Au bout du corridor, en face de l'ascenseur."),
        ("la sortie", "C'est au rez-de-chaussée. Descendez, c'est à côté de l'accueil."),
    ], corrige=True, cols=1,
       notes="Cinq items. Exiger exactement deux phrases : compter à voix haute avec le "
             "groupe la première fois.")

    d.pratique('Pratique · à deux, debout', "L'un cherche, l'autre répond",
               "Puis on échange les rôles.", [
        ("Étape 1", "A demande un endroit du vrai centre, avec excusez-moi."),
        ("Étape 2", "B répond en deux phrases : l'étage, puis le côté."),
        ("Étape 3", "A redit l'indication dans ses mots pour vérifier."),
        ("Étape 4", "On échange, et on recommence avec un autre endroit."),
    ], cols=1,
       notes="Vingt minutes. L'étape 3 est la stratégie du module au complet : redire "
             "pour vérifier. Elle se retrouve telle quelle dans la grille du bloc E.")

    d.billet(
        "Écrivez en deux phrases où est votre local, pour quelqu'un qui arrive demain.",
        exemples=[
            "C'est au deuxième étage.",
            "Prenez l'escalier, puis à droite.",
        ],
        notes="Devoir court, et brouillon direct de la production écrite du bloc E. "
              "Ceux qui le font n'auront qu'à le reprendre et l'allonger.")

    return d.save(dossier)
