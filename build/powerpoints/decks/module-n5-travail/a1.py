# -*- coding: utf-8 -*-
"""A1 · « Maintenant, c'est écrit. »
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-travail/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="« Maintenant, c'est écrit. »",
        chapeau="Dorine Kabeya travaille depuis dix-huit mois à la "
                "Coopérative d'aide à domicile de Rosemont. Lundi, elle "
                "passe de l'entretien à l'accueil : un bureau, un "
                "téléphone, un poste à elle. Et presque tout ce qui "
                "change s'écrit.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : à votre "
                  "travail, comment savez-vous ce que vous avez à faire aujourd'hui ? "
                  "Quelqu'un vous le dit, ou c'est écrit quelque part ? L'écart entre les "
                  "réponses dit exactement ce que le module va travailler. Ne juger aucune "
                  "réponse : beaucoup d'emplois ne demandent effectivement rien par écrit.")

    d.objectifs([
        "comprendre ce qu'un poste de bureau demande par écrit ;",
        "nommer le matériel, les tâches et les directives d'un poste ;",
        "reconnaître le registre à tenir au téléphone et par écrit ;",
        "repérer ce qui change entre un poste d'exécution et un poste d'accueil.",
    ], notes="Le quatrième objectif est celui qui surprend le plus les élèves. La plupart "
             "ont déjà travaillé au Québec ; peu ont occupé un poste où l'on répond au "
             "téléphone au nom d'une organisation.")

    d.declencheur(
        'Observation', "Un comptoir, une plante, un classeur. Qu'est-ce qui "
                       "change quand ce bureau devient le vôtre ?",
        image=IMG + 'bureau-accueil.jpg',
        pistes=[
            "Qui vous dira quoi faire, le matin ?",
            "Qui répond quand vous n'êtes pas à votre place ?",
            "Où sont écrites vos heures de travail ?",
            "Si vous prenez un message pour quelqu'un, qui le lira ?",
        ],
        notes="Les quatre pistes annoncent les quatre séances du bloc A. La deuxième "
              "— « qui répond quand vous n'êtes pas là ? » — amène la boîte vocale, qui "
              "est tout le défi 1. Compter les mains à « avez-vous déjà enregistré un "
              "message d'accueil ? » : presque aucune, en général.")

    d.dialogue('Dialogue · 1 de 3', "Un bureau, et un peu de peur", [
        ("GHISLAIN", "Bonjour Dorine. Assoyez-vous, c'est votre bureau maintenant.", True),
        ("DORINE", "Merci. J'ai un peu peur, je vous le dis franchement.", True),
        ("GHISLAIN", "Peur de quoi ? Vous connaissez la coopérative mieux que moi.", True),
        ("DORINE", "Je connais les logements, les horaires, les gens. Je ne connais "
                   "pas le bureau.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer la distinction que fait Dorine : elle connaît le travail, "
             "pas le bureau. C'est exactement la situation de beaucoup d'élèves qui "
             "changent de poste. Demander qui a déjà eu cette peur-là.")

    d.dialogue('Dialogue · 2 de 3', "Ce qui change : tout est écrit", [
        ("GHISLAIN", "C'est vrai que ça change. Avant, on vous disait quoi faire le "
                     "matin. Maintenant, c'est écrit.", True),
        ("DORINE", "Écrit où ?", True),
        ("GHISLAIN", "Partout. Vos tâches sont dans un tableau. Les directives des "
                     "appareils sont sur le mur. Vos heures sont au registre. Et les "
                     "demandes passent par des formulaires.", True),
        ("DORINE", "Et le téléphone ?", True),
    ], notes="Faire relever les quatre écrits nommés par Ghislain : le tableau des tâches, "
             "les directives, le registre des heures, les formulaires. Les écrire au "
             "tableau : ce sont quatre des seize mots du module.")

    d.dialogue('Dialogue · 3 de 3', "On vouvoie, même les gens qu'on connaît", [
        ("GHISLAIN", "Une dernière. Au téléphone et par écrit, vous vouvoyez tout le "
                     "monde, même les gens que vous connaissez. Ici, on se tutoie ; "
                     "là, non.", True),
        ("DORINE", "Même madame Thériault ? Je lui parle depuis un an.", True),
        ("GHISLAIN", "Même madame Thériault. Ce n'est pas Dorine qui répond au poste "
                     "vingt-deux : c'est la coopérative.", False),
    ], notes="La dernière réplique est la phrase à retenir de la séance. Elle explique le "
             "vouvoiement autrement que par la politesse : au téléphone, on parle au nom "
             "d'une organisation. C'est le sujet de la séance A4.")

    d.regle("Ce qui n'est pas écrit n'a pas eu lieu",
            "À un poste de bureau, une entente de corridor ne vaut rien : "
            "seule la trace écrite compte.",
            precision="Une note prise, un formulaire signé, un courriel de "
                      "confirmation : trois façons de rendre une chose vraie pour "
                      "tout le monde, et pas seulement pour soi. C'est la phrase la "
                      "plus utile d'un premier mois de bureau.",
            notes="Diapositive à photographier. Elle reviendra au défi 3, quand Ghislain "
                  "refusera d'accorder un congé de vive voix.")

    d.cartes("Quatre écrits", "Ce que chacun sert à faire", [
        ("Le tableau des tâches",
         "Il dit ce qu'il y a à faire, et il change chaque semaine."),
        ("Les directives",
         "Elles disent comment le faire, et elles ne changent presque jamais."),
        ("Le registre des heures",
         "Il compte les heures faites, reprises et absentes de chaque personne."),
        ("Le formulaire",
         "Il porte une demande, avec des cases et une place pour signer."),
    ], notes="Insister sur la différence entre la première et la deuxième carte : une "
             "tâche est ce qu'il y a à faire, des directives disent comment. Les élèves "
             "confondent souvent les deux mots.")

    d.tableau('Deux postes', "Ce qui change à l'accueil",
              ['Avant, à l\'entretien', 'Maintenant, à l\'accueil'],
              [["On me dit quoi faire", "Je lis mes tâches"],
               ["Je travaille seule", "Je réponds pour tout le monde"],
               ["Mon horaire est affiché", "Mes heures sont au registre"],
               ["Je demande de vive voix", "Je remplis un formulaire"],
               ["Je tutoie mes collègues", "Je vouvoie au téléphone"]],
              cle=1,
              notes="Faire compléter le tableau par le groupe avant de l'afficher : "
                    "demander ce qui change quand on passe d'un travail d'exécution à un "
                    "travail de bureau. Beaucoup d'élèves ont vécu ce passage.")

    d.piege("Croire qu'on retiendra sans écrire",
            "Il me l'a dit ce matin, je m'en souviens.",
            "Je le note tout de suite, avec la date.",
            "Une consigne entendue le lundi se déforme d'ici le jeudi, et personne ne "
            "peut prouver ce qui a été dit. Écrire prend dix secondes.",
            notes="Demander au groupe qui a déjà perdu une information de travail faute de "
                  "l'avoir écrite. Les exemples sortent seuls et ils sont parlants.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Dorine travaillait déjà à la coopérative avant lundi.", "vrai"),
        ("Elle connaît mal les logements et les horaires.", "faux — elle les connaît bien"),
        ("À son nouveau poste, on lui dira chaque matin quoi faire.", "faux — c'est écrit"),
        ("Le téléphone du poste vingt-deux est le sien.", "vrai"),
        ("Une note prise à l'accueil doit se comprendre sans elle.", "vrai"),
        ("Elle peut tutoyer les gens qu'elle connaît depuis un an.", "faux — au téléphone, on vouvoie"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte du dialogue. La "
             "dernière est celle qui fait le plus discuter : garder la discussion pour A4.")

    d.billet(
        "Écrivez trois choses qui, à votre travail, sont écrites quelque part.",
        exemples=[
            "Dites où elles sont écrites : un tableau, un mur, un cahier, un courriel.",
            "Ajoutez une chose qui n'est jamais écrite, et qui devrait l'être.",
        ],
        notes="Le billet sert de vérification de fin de séance et de matière pour A4. "
              "Ramasser les billets : les exemples des élèves valent mieux que les "
              "exemples inventés pour les séances suivantes.")

    return d.save(dossier)
