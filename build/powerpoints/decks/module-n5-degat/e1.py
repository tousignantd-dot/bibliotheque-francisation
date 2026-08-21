# -*- coding: utf-8 -*-
"""E1 · Signaler un dégât, à voix haute.
Bloc E « Je me lance » · couleur framboise · 75 min. Production orale.
Source : bloc « Je me lance » du module — jeu de rôle `degat` et production orale.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-degat/images/')


def build(dossier):
    d = Deck(
        code='E1', section='framboise',
        titre="Signaler un dégât, à voix haute",
        chapeau="Le jeu de rôle sert de répétition, l'enregistrement sert de "
                "preuve. On joue les deux rôles : au niveau 5, il faut savoir "
                "exposer et savoir questionner.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Ouvrir le module interactif dès le début : la "
                  "séance se passe surtout dedans. Les diapositives servent de cadre et "
                  "de rappel, pas de contenu neuf.")

    d.objectifs([
        "mener un appel de signalement du début à la fin ;",
        "tenir les deux rôles, locataire et propriétaire ;",
        "raconter un dégât en mêlant l'imparfait et le passé composé ;",
        "terminer par une demande justifiée.",
    ])

    d.tableau('Les sept sujets · 1 de 2', "Raconter et décrire",
              ['Le sujet', 'Ce qu\'on attend'],
              [["ce qui est arrivé, et quand", "imparfait puis passé composé"],
               ["ce qu'on voit aujourd'hui", "pièce par pièce, le verbe juste"],
               ["ce qu'on a déjà fait", "photos, chaudière, rien de jeté"],
               ["la cause, si on la connaît", "sans accuser personne"]],
              cle=0,
              note="Les sept sont cochables dans le module, un à un.",
              notes="Faire ouvrir la liste dans le module et cocher au fur et à mesure : "
                    "c'est ce qui empêche les appels qui s'arrêtent au troisième sujet.")

    d.tableau('Les sept sujets · 2 de 2', "Obtenir quelque chose",
              ['Le sujet', 'Ce qu\'on attend'],
              [["ce que ça empêche", "la ligne qui fonde la demande"],
               ["la date de l'intervention", "et ce qui se passe en attendant"],
               ["la compensation demandée", "avec sa raison"]],
              cle=0,
              note="Les trois derniers sont ceux qu'on oublie.",
              notes="Un appel qui s'arrête avant ces trois-là n'a obtenu qu'une promesse "
                    "de réparation — la moitié de ce à quoi le locataire a droit.")

    d.cartes("Trois situations au choix", "La même démarche, trois dégâts", [
        ("Le plafond de la chambre",
         "Un cerne d'un mètre, le plancher qui gondole, un matelas humide. La fuite venait du chauffe-eau du dessus."),
        ("Le refoulement au sous-sol",
         "Cinq centimètres d'eau sale après un orage, un tapis à jeter, une odeur qui ne part pas."),
        ("Le boyau de la laveuse",
         "L'eau a traversé le plancher : la peinture cloque, l'armoire du bas est gonflée."),
    ], cols=1,
       notes="Les élèves qui ont déjà vécu un dégât peuvent raconter le leur : c'est "
             "toujours meilleur. Les autres prennent une des trois.")

    d.regle("On joue les deux rôles",
            "Savoir exposer, et savoir questionner.",
            precision="Côté locataire, on raconte, on décrit, on demande. Côté "
                      "propriétaire, on écoute, on relance sur ce qui manque, on ne "
                      "propose rien avant qu'on ait demandé. Le second rôle est le plus "
                      "formateur : il oblige à repérer ce qu'un récit ne dit pas.",
            notes="Insister pour que chacun fasse les deux. La tentation est de rester du "
                  "côté du locataire, qui est plus confortable.")

    d.declencheur(
        'Avant de commencer', "Votre appel doit finir par quoi ?",
        image=IMG + 'chaudiere-sous-fuite.jpg',
        pistes=[
            "Une date ?",
            "Un nom d'entreprise ?",
            "Un geste de votre part ?",
            "Une demande de compensation ?",
        ],
        notes="Les quatre. Le rappeler avant que le premier binôme se lance : un appel "
              "qui finit sans suite est un appel à refaire.")

    d.tableau('Les phrases à réutiliser', "Elles viennent des quatre blocs",
              ['Le moment', 'La phrase'],
              [["le décor", "Il faisait encore noir et l'eau coulait déjà."],
               ["l'événement", "Je me suis levée à six heures et j'ai mis une chaudière."],
               ["la simultanéité", "En rentrant du travail, j'ai vu que la tache avait doublé."],
               ["ce qui compte", "Ce qui m'inquiète, c'est l'humidité dans le matelas."],
               ["la demande", "Trois nuits sans chambre : par conséquent, je demande une réduction."]],
              cle=0,
              note="Cinq phrases, cinq points de langue du module.",
              notes="Laisser cette diapositive affichée pendant les jeux de rôle. Elle "
                    "sert de béquille, et c'est très bien ainsi.")

    d.piege("Attendre qu'on vous propose quelque chose",
            "Il va bien me dire ce qu'il compte faire.",
            "Je demande une date, et je demande une compensation.",
            "Le propriétaire du jeu de rôle ne propose jamais d'argent le premier — et "
            "c'est fidèle à la réalité. Une compensation se demande, avec une raison et "
            "un chiffre. Sans demande, la conversation se termine sur une promesse de "
            "réparation, ce qui n'est que la moitié de ce à quoi vous avez droit.",
            notes="Prévenir avant le premier essai : sinon la moitié du groupe termine "
                  "l'appel sans avoir rien demandé, et il faut tout recommencer.")

    d.billet(
        "Enregistrez votre récit dans le module, écoutez-vous, recommencez une fois.",
        exemples=[
            "Environ une minute : le décor, l'événement, les dommages, la demande.",
            "La deuxième version est toujours meilleure que la première.",
        ],
        notes="L'enregistrement se dépose à l'enseignant depuis le module. Rappeler que "
              "la rétroaction de l'IA reste privée tant que l'élève n'envoie rien.")

    return d.save(dossier)
