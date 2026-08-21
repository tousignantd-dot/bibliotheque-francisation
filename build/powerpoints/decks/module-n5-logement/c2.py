# -*- coding: utf-8 -*-
"""C2 · Décrire un logement.
Bloc C « Défi 2 · La visite » · couleur framboise · 75 min.
Source : exercices `t2decrire` et `t2img`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-logement/images/')


def build(dossier):
    d = Deck(
        code='C2', section='framboise',
        titre="Décrire un logement",
        chapeau="« C'est beau », « c'est correct », « c'est pas cher » : trois "
                "phrases qui ne disent rien. Décrire, c'est donner des mots "
                "qui se comparent et des chiffres qui se notent.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire de la description. Elle prépare la production "
                  "orale finale, où l'élève fait visiter un logement.")

    d.objectifs([
        "employer les adjectifs qui décrivent un logement ;",
        "distinguer ce que chaque adjectif dit vraiment ;",
        "nommer les éléments qu'on regarde pendant une visite ;",
        "remplacer une impression par un renseignement.",
    ])

    d.declencheur(
        'Observation', "Décrivez ce que vous voyez en trois phrases précises.",
        image=IMG + 'plancher-bois-franc.jpg',
        pistes=[
            "« C'est beau » — qu'est-ce que ça apprend à quelqu'un ?",
            "De quoi le plancher est-il fait ?",
            "Est-ce que c'est du vrai bois ?",
            "Comment le dit-on dans une annonce ?",
        ],
        notes="Refuser les trois premières réponses vagues, gentiment mais fermement. "
              "Demander chaque fois : « et qu'est-ce que ça apprend à quelqu'un qui n'est "
              "pas là ? » C'est le fil de toute la séance.")

    d.tableau('Les adjectifs de l\'annonce', "Ce qu'ils disent vraiment",
              ['L\'adjectif', 'Ce que ça veut dire'],
              [["ensoleillé", "le soleil entre une bonne partie de la journée"],
               ["insonorisé", "on n'entend pas les voisins"],
               ["meublé", "les meubles sont là — mais pas les électroménagers"],
               ["chauffé", "le chauffage est compris dans le loyer"],
               ["rénové", "les planchers et la cuisine ont été refaits"],
               ["en demi-sous-sol", "le logement est à moitié sous le niveau du sol"],
               ["non-fumeur", "il n'y a jamais eu de fumée dans le logement"],
               ["accessible", "un ascenseur, et pas de marches à l'entrée"]],
              cle=0,
              note="« Rénové » ne dit pas quand. Demandez toujours l'année.",
              notes="Diapositive à photographier. Insister sur « meublé » : c'est l'erreur "
                    "de la séance A3, et elle coûte cher.")

    d.cartes("Ce qu'on regarde", "Six éléments d'une visite", [
        ("La fenêtre",
         "On l'ouvre et on la ferme. Si elle coince, l'hiver sera froid."),
        ("La hotte",
         "Au-dessus du poêle : elle aspire la fumée et les odeurs de cuisson."),
        ("La plinthe électrique",
         "Le chauffage le long du mur, au ras du plancher. C'est ce qui fait la facture."),
        ("Le panneau de disjoncteurs",
         "La boîte grise où l'on remet le courant quand tout s'éteint."),
        ("La tache d'humidité",
         "Une marque au plafond : demandez d'où elle vient et si c'est réparé."),
        ("L'escalier extérieur",
         "À monter chargé de sacs, et à déneiger tout l'hiver."),
    ], cols=2,
       notes="Projeter les six photos du module en parallèle. Faire nommer chaque élément "
             "avant d'afficher le nom.")

    d.regle("Un chiffre vaut mieux qu'une impression",
            "« Environ cent dollars par mois l'hiver » se compare ; « c'est pas cher à "
            "chauffer » ne veut rien dire.",
            precision="Chaque fois que vous décrivez quelque chose de mesurable — un coût, "
                      "une surface, une distance, une année de rénovation —, donnez le "
                      "chiffre. C'est la différence entre une description d'adulte et une "
                      "impression.",
            notes="Diapositive à photographier. C'est la règle qui structure la production "
                  "orale finale, et le premier critère de correction.")

    d.pratique('Vocabulaire', "L'adjectif juste",
               "Complétez avec un adjectif de la séance.", [
        ("Le soleil entre du matin jusqu'à quatre heures : le salon est …", "ensoleillé"),
        ("On entend marcher au-dessus : l'immeuble n'est pas …", "insonorisé"),
        ("Un lit, une table et une commode sont fournis : le logement est …", "meublé"),
        ("Le chauffage est compris dans le loyer : le logement est …", "chauffé"),
        ("La cuisine a été refaite l'an dernier : elle a été …", "rénovée"),
        ("Le logement est à moitié sous le sol : il est en …", "demi-sous-sol"),
        ("Il y a un ascenseur et pas de marches : l'immeuble est …", "accessible"),
        ("Personne n'a jamais fumé dedans : c'est un logement …", "non-fumeur"),
    ], corrige=True,
       notes="Faire accorder les adjectifs à l'oral : ensoleillée, rénovée, insonorisés. "
             "L'accord du participe passé employé comme adjectif est un savoir du niveau 5.")

    d.piege("Décrire par ce qu'on ressent",
            "C'est chaleureux, c'est charmant, c'est correct.",
            "Quatre et demie, deux chambres, bois franc, ensoleillé jusqu'à seize heures.",
            "Une impression ne se compare pas et ne se note pas. Un visiteur qui n'est pas "
            "là a besoin de choses mesurables : le nombre de pièces, l'orientation, l'état "
            "des planchers, ce qui est inclus.",
            notes="Ce n'est pas que l'impression soit interdite : c'est qu'elle vient "
                  "après. D'abord les faits, ensuite « et je m'y suis senti bien ».")

    d.pratique('Production', "Décrivez en quatre phrases précises",
               "Choisissez un logement — le vôtre, ou un de vos trois annonces.", [
        ("Phrase 1 · les pièces", "C'est un quatre et demie avec deux chambres."),
        ("Phrase 2 · la lumière", "Le salon donne au sud, il est ensoleillé jusqu'à seize heures."),
        ("Phrase 3 · ce qui est inclus", "Le chauffage n'est pas inclus : environ cent dollars par mois."),
        ("Phrase 4 · un défaut", "L'immeuble n'est pas insonorisé : on entend marcher au-dessus."),
    ], corrige=False,
       notes="Faire lire trois ou quatre productions à voix haute. Corriger en groupe une "
             "seule chose : la présence d'un chiffre. C'est le critère du jour.")

    d.billet(
        "Écrivez l'annonce de votre logement actuel, comme si vous le louiez.",
        exemples=[
            "Employez les abréviations de la séance A4.",
            "Puis écrivez en dessous ce que l'annonce ne dit pas.",
        ],
        notes="Devoir en deux temps, et le deuxième est le plus formateur : les élèves "
              "découvrent qu'ils cachent naturellement les mêmes choses que les "
              "propriétaires. Bon point de départ pour la séance E1.")

    return d.save(dossier)
