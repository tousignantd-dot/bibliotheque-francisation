# -*- coding: utf-8 -*-
"""B1 · « Quel est l'endroit de votre urgence ? »
Bloc B « Défi 1 · L'appel au 9-1-1 » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-urgence/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="« Quel est l'endroit de votre urgence ? »",
        chapeau="Deux heures du matin. Un appel au 9-1-1 n'est pas une "
                "conversation : c'est le répartiteur qui mène, et sa "
                "première question ne porte pas sur ce qui se passe.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Rendre les billets de A4 et faire lire deux "
                  "ouvertures d'appel au 8-1-1. Puis annoncer : au 9-1-1, ces deux "
                  "phrases arrivent trop tôt. La séance explique pourquoi.")

    d.objectifs([
        "donner l'endroit exact avant tout le reste ;",
        "dire en une seule phrase ce qui se passe ;",
        "répondre par oui ou par non aux questions fermées ;",
        "comprendre pourquoi on ne raccroche pas.",
    ])

    d.declencheur(
        'Écoute', "« Neuf un un, quel est l'endroit de votre urgence ? » Pourquoi "
                  "pas « qu'est-ce qui se passe ? »",
        image=IMG + 'escalier.jpg',
        pistes=[
            "Que se passe-t-il si la ligne se coupe après trente secondes ?",
            "Qu'est-ce qui permet à quelqu'un de partir tout de suite ?",
            "Une adresse suffit-elle pour trouver la personne ?",
            "Qu'est-ce qu'on peut faire pendant qu'on attend ?",
        ],
        notes="La première piste donne la réponse : tant que l'adresse n'est pas prise, "
              "personne ne part, et si l'appel tombe, il ne reste rien. Le dire une fois "
              "suffit ; les élèves ne l'oublient plus.")

    d.dialogue('Dialogue · 1 de 3', "L'endroit, puis le numéro", [
        ("VINCENT", "Neuf un un, quel est l'endroit de votre urgence ?", True),
        ("MARISOL", "Cinq mille quatre cent douze, rue des Ormeaux, à Saint-Léonard. "
                    "Appartement deux, en bas de l'escalier intérieur.", True),
        ("VINCENT", "Cinq mille quatre cent douze, rue des Ormeaux. Quel est le "
                    "numéro de téléphone d'où vous appelez ?", True),
        ("MARISOL", "Cinq un quatre, cinq cinq cinq, zéro un neuf huit.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer deux choses : Marisol donne l'appartement et l'étage sans "
             "qu'on les demande, et Vincent répète l'adresse. C'est le seul moment où "
             "une erreur de chiffre se rattrape.")

    d.dialogue('Dialogue · 2 de 3', "Une phrase, puis les deux questions", [
        ("VINCENT", "Merci. Dites-moi ce qui se passe.", True),
        ("MARISOL", "Ma mère est tombée dans l'escalier. Elle a soixante et onze ans. "
                    "Elle est par terre et elle ne peut pas se relever.", True),
        ("VINCENT", "Est-ce qu'elle est consciente ? Est-ce qu'elle vous répond ?", True),
        ("MARISOL", "Oui, elle me répond. Elle a mal à la hanche droite, elle dit que "
                    "sa jambe ne bouge plus.", True),
    ], notes="Compter les mots de la réponse de Marisol : trois phrases courtes, aucune "
             "mention de la fièvre des deux derniers jours. Ce détail-là ira au triage, "
             "pas ici.")

    d.dialogue('Dialogue · 3 de 3', "Les consignes, et l'interdiction de raccrocher", [
        ("VINCENT", "D'accord. Écoutez-moi bien : ne la déplacez pas, ne la faites pas "
                    "asseoir, ne lui donnez rien à boire. Restez près d'elle et "
                    "couvrez-la avec une couverture.", True),
        ("MARISOL", "Je ne la bouge pas, je la couvre. C'est fait.", True),
        ("VINCENT", "Alors restez en ligne avec moi jusqu'à leur arrivée. Ne "
                    "raccrochez pas.", True),
        ("MARISOL", "Je reste. Ils arrivent dans combien de temps ?", False),
    ], notes="Marisol dit à voix haute ce qu'elle fait. C'est le geste à copier : le "
             "répartiteur ne voit rien, et il note tout ce qu'il entend.")

    d.regle("L'endroit avant tout le reste",
            "Tant que l'adresse n'est pas prise, personne ne part.",
            precision="Le numéro, la rue, la ville, puis l'appartement et l'étage. Si "
                      "l'appel se coupe, l'adresse est la seule chose qui permette "
                      "d'envoyer quelqu'un — même sur un téléphone cellulaire, la "
                      "localisation reste approximative.",
            notes="Diapositive à photographier. C'est la règle la plus contre-intuitive "
                  "du module : l'instinct pousse à raconter d'abord.")

    d.cartes("L'ordre des questions", "Toujours le même, quel que soit l'appel", [
        ("1 · Où ?", "L'adresse complète, puis le détail : étage, appartement, porte."),
        ("2 · Votre numéro de téléphone", "Pour vous rappeler si la ligne se coupe."),
        ("3 · Que se passe-t-il ?", "Une seule phrase : qui, quoi, où."),
        ("4 · Est-elle consciente ?", "Oui ou non, puis une précision de quatre mots."),
        ("5 · Respire-t-elle ?", "Oui ou non. Ces deux questions décident de l'équipe."),
        ("6 · Le reste", "Âge, médicaments, saignement, coup à la tête, accès à "
                         "l'immeuble."),
    ], cols=3,
       notes="Faire copier cet ordre dans le cahier. Il sera repris tel quel à la séance "
             "B2, puis servira de grille au jeu de rôle de E1.")

    d.piege("Commencer par le récit",
            "Bonjour, alors voilà, depuis mercredi ma mère fait de la fièvre et…",
            "5412, rue des Ormeaux, appartement 2, à Saint-Léonard.",
            "Le répartiteur vous coupera pour demander l'adresse. La donner d'emblée, "
            "sans qu'on la demande, fait gagner vingt secondes — et vingt secondes, la "
            "nuit, c'est beaucoup.",
            notes="Faire jouer la mauvaise version par deux élèves : elle est drôle, et "
                  "elle se retient.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'appel.", [
        ("La première question porte sur l'endroit de l'urgence.", "vrai"),
        ("Marisol précise où sa mère se trouve dans l'immeuble.", "vrai"),
        ("Marisol raconte au répartiteur toute la journée de sa mère.", "faux — trois phrases"),
        ("Le répartiteur demande de faire asseoir Amparo.", "faux — surtout pas"),
        ("Marisol doit couvrir sa mère et rester près d'elle.", "vrai"),
        ("Elle raccroche dès que les ambulanciers sont en route.", "faux — elle reste en ligne"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. La quatrième est la "
             "plus importante : déplacer quelqu'un peut aggraver une fracture.")

    d.billet(
        "Écrivez l'adresse exacte où vous êtes en ce moment, comme au 9-1-1.",
        exemples=[
            "Numéro, rue, ville — puis l'étage, le local, et par où entrer.",
            "Ajoutez un repère visible de la rue.",
        ],
        notes="Exercice court et concret : beaucoup d'élèves découvrent qu'ils ne "
              "connaissent pas le numéro civique de leur école ou de leur travail.")

    return d.save(dossier)
