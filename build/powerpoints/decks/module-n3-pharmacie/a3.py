# -*- coding: utf-8 -*-
"""A3 · Les seize mots de la pharmacie.
Bloc A « Je découvre » · couleur framboise (vocabulaire) · 75 min.
Source : banc `FC_CARDS`, exercices `prVocab` et `prImg`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-pharmacie/images/')


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre='Les seize mots de la pharmacie',
        chapeau="Quatre familles : l'endroit, le corps, l'ordonnance, "
                "l'étiquette. Seize mots qui reviendront dans les trois "
                "défis, et qu'on n'apprendra pas deux fois.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Prévoir les cartes mémoire du module "
                  "interactif pour la fin de la séance. Les seize mots viennent du "
                  "lexique que le programme rattache à cette situation.")

    d.objectifs([
        "nommer les seize mots du module et leur article ;",
        "associer chaque mot à une photo ;",
        "ranger les mots en quatre familles ;",
        "employer cinq mots dans une phrase complète.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'on voit dans cette allée ?",
        image=IMG + 'allee-sirops.jpg',
        pistes=[
            "Combien de bouteilles différentes voyez-vous ?",
            "Comment savoir laquelle prendre ?",
            "Est-ce qu'il faut une ordonnance pour ces bouteilles-là ?",
        ],
        notes="La photo répond visuellement à la question de la séance A1 : dix "
              "bouteilles sur la tablette, et une seule qui convient. C'est l'argument "
              "en faveur du conseil du pharmacien.")

    d.vocabulaire("Famille 1", "L'endroit et les papiers", [
        ("une ordonnance", "le papier signé par le médecin"),
        ("le comptoir des ordonnances", "le comptoir du fond, où on parle au pharmacien"),
        ("la carte d'assurance maladie", "la carte du gouvernement, à présenter chaque fois"),
        ("un médicament en vente libre", "un médicament qui s'achète sans ordonnance"),
    ], notes="Faire répéter avec l'article. « Une » ordonnance, « la » carte : les deux "
             "sont féminins et se disent souvent ensemble.")

    d.vocabulaire("Famille 2", "Le corps et les malaises", [
        ("tousser", "faire un bruit fort avec la gorge, sans le vouloir"),
        ("avoir de la fièvre", "avoir le corps trop chaud parce qu'on est malade"),
        ("un rhume", "le nez qui coule, la gorge irritée — une semaine environ"),
        ("un pansement", "le petit morceau collant qu'on met sur une coupure"),
    ], notes="Ces quatre mots viennent directement de la liste du programme. « Tousser » "
             "et « avoir de la fièvre » sont des verbes : les faire employer dans une "
             "phrase, pas seulement nommer.")

    d.vocabulaire("Famille 3", "Le renouvellement", [
        ("un renouvellement", "recevoir encore une fois le même médicament"),
        ("le dossier", "la liste que la pharmacie garde de tes médicaments"),
        ("l'assurance médicaments", "ce qui paie une partie du prix"),
        ("le pharmacien", "la personne qui prépare et qui conseille"),
    ], notes="Le mot « dossier » surprend souvent : la pharmacie garde une trace de tout "
             "ce qu'on a pris. C'est ce qui lui permet de repérer les mélanges dangereux.")

    d.vocabulaire("Famille 4", "L'étiquette", [
        ("la posologie", "ce qui dit combien en prendre, et quand"),
        ("un comprimé", "le petit rond dur qu'on avale avec de l'eau"),
        ("une étiquette", "le papier collé sur le flacon, avec ton nom"),
        ("un effet secondaire", "ce qu'un médicament peut faire d'autre"),
    ], notes="« Posologie » est un mot long et savant, mais il est écrit partout : mieux "
             "vaut le reconnaître que l'éviter. Le défi 3 lui est consacré.")

    d.pratique('Association', "Le mot et la photo",
               "Dites quel mot va avec chaque photo décrite.", [
        ("Un petit flacon orange avec une étiquette blanche.", "une étiquette, un comprimé"),
        ("Une main qui tend une carte verte par-dessus le comptoir.", "la carte d'assurance maladie"),
        ("Un pansement collé sur un doigt.", "un pansement"),
        ("Des chaises vides près du comptoir du fond.", "la salle d'attente"),
        ("Un sac de papier blanc agrafé en haut.", "le sac de la pharmacie"),
    ], corrige=True,
       notes="Reprend l'exercice interactif `prImg` sous forme orale. Les élèves qui "
             "hésitent devant l'écran répondent souvent mieux à l'oral, en groupe.")

    d.pratique('Emploi', "Une phrase avec le mot",
               "Faites une phrase complète avec chaque mot.", [
        ("une ordonnance", "« Mon ordonnance est finie depuis samedi. »"),
        ("tousser", "« Je tousse depuis quatre jours. »"),
        ("un renouvellement", "« Est-ce qu'il me reste un renouvellement ? »"),
        ("la posologie", "« Je ne comprends pas la posologie. »"),
        ("un effet secondaire", "« Ce médicament a un effet secondaire : il donne sommeil. »"),
    ], corrige=True,
       notes="Accepter toute phrase juste et complète. Écrire au tableau celles qui "
             "serviront au défi 1.")

    d.billet(
        "Choisissez quatre mots de la séance et écrivez une phrase pour chacun.",
        exemples=[
            "Prenez un mot par famille.",
            "Employez « mon », « ma » ou « mes » dans au moins une phrase.",
        ],
        notes="Devoir court. Les phrases produites servent d'exemples réels à la "
              "séance A4 et au défi 1.")

    return d.save(dossier)
