# -*- coding: utf-8 -*-
"""C2 · Appuyer, insérer, verrouiller, confirmer
Bloc C « Défi 2 » · couleur framboise · 75 min. Le vocabulaire des appareils.
Source : exercice `t2mode`, mini-leçon `t2mode`.

Les quatre verbes du titre sont ceux que le programme nomme lui-même dans les
savoirs du niveau 5, sous « vocabulaire lié aux directives d'utilisation ».
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-travail/images/')


def build(dossier):
    d = Deck(
        code='C2', section='framboise',
        titre="Appuyer, insérer, verrouiller, confirmer",
        chapeau="Un mode d'emploi n'emploie qu'une trentaine de verbes, et "
                "les mêmes reviennent d'un appareil à l'autre : sur le "
                "photocopieur, le guichet de la banque, le terminal du "
                "dépanneur. Les apprendre une fois sert partout.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire du défi 2. Commencer par demander au groupe de "
                  "nommer tous les appareils qu'ils ont utilisés depuis hier matin : "
                  "guichet, terminal de paiement, four à micro-ondes, distributrice, "
                  "borne de métro. Tous emploient les mêmes verbes.")

    d.objectifs([
        "comprendre huit verbes de directives et leur préposition ;",
        "employer chaque verbe dans une consigne d'appareil ;",
        "reconnaître ces verbes sur d'autres appareils que le photocopieur ;",
        "distinguer annuler et éteindre.",
    ])

    d.declencheur(
        'Observation', "Un écran, des boutons, un tiroir ouvert. Quels "
                       "verbes vous viennent ?",
        image=IMG + 'photocopieur-corridor.jpg',
        pistes=[
            "Que fait-on avec le doigt ? Avec la main entière ?",
            "Quel verbe vient toujours avec « sur » ?",
            "Quel geste tous les appareils publics demandent-ils à la fin ?",
            "Quel verbe entend-on au guichet de la banque, et ici aussi ?",
        ],
        notes="La troisième piste amène « retirer » : retirer sa carte, son original, "
              "sa monnaie. C'est le verbe des choses qu'on oublie, et l'exemple le plus "
              "parlant de la séance.")

    d.vocabulaire('Vocabulaire · 1 de 2', "Les verbes du doigt et de la main", [
        ("appuyer sur", "Presser un bouton ou une touche avec le doigt."),
        ("insérer dans", "Faire entrer une carte ou une feuille dans une fente."),
        ("retirer", "Sortir ce qui était resté dans l'appareil."),
        ("placer", "Mettre à l'endroit précis qui est indiqué."),
    ], notes="Chaque verbe traîne sa préposition, et elle ne se choisit pas : appuyer "
             "sur, insérer dans, retirer de. Faire répéter le verbe avec sa préposition, "
             "comme un seul mot.")

    d.vocabulaire('Vocabulaire · 2 de 2', "Les verbes de la décision", [
        ("confirmer", "Dire oui une seconde fois, pour valider un choix."),
        ("annuler", "Arrêter une opération avant qu'elle soit faite."),
        ("verrouiller", "Bloquer l'accès, ou protéger par un code."),
        ("refermer", "Remettre en place la porte ou le couvercle ouvert."),
    ], notes="Confirmer et annuler sont presque toujours côte à côte sur un écran, et "
             "leur place change d'un appareil à l'autre. Le dire : c'est ce qui fait "
             "appuyer sur le mauvais bouton.")

    d.regle("Le verbe s'apprend avec sa préposition",
            "On appuie sur, on insère dans, on place dans ou sur, on retire de.",
            precision="Séparés, le verbe et sa préposition se mélangent. « Appuyez le "
                      "bouton vert » se comprend, mais s'entend tout de suite.",
            notes="Faire produire par le groupe une consigne avec chacun des quatre "
                  "verbes prépositionnels, à voix haute. C'est la seule façon de les "
                  "installer.")

    d.tableau('Le même verbe, ailleurs', "Quatre appareils, les mêmes mots",
              ['Appareil', 'Ce qu\'il vous demande'],
              [["Le photocopieur", "Placez la feuille. Appuyez sur Numériser."],
               ["Le guichet de la banque", "Insérez votre carte. Confirmez le montant."],
               ["Le terminal du dépanneur", "Insérez ou approchez. Retirez votre carte."],
               ["La borne du métro", "Appuyez sur l'écran. Confirmez. Retirez le titre."]],
              cle=1,
              notes="Ce tableau est la vraie valeur de la séance : les élèves y "
                    "reconnaissent des situations qu'ils vivent chaque semaine. Leur "
                    "demander d'ajouter un cinquième appareil.")

    d.piege("Confondre annuler et éteindre",
            "J'appuie trois secondes sur le bouton d'arrêt pour annuler ma copie.",
            "J'appuie sur Annuler : ça arrête seulement ma tâche.",
            "« Annuler » arrête une seule opération ; éteindre coupe tout, et le "
            "collègue qui attendait ses vingt copies recommence depuis le début.",
            notes="Faute réelle et coûteuse en milieu de travail. Demander si quelqu'un "
                  "l'a déjà faite — il y a presque toujours quelqu'un.")

    d.pratique('Vocabulaire', "Le verbe et le geste",
               "Reliez chaque verbe au geste qu'il désigne.", [
        ("appuyer sur", "presser un bouton avec le doigt"),
        ("insérer dans", "faire entrer une carte dans une fente"),
        ("retirer", "sortir ce qui était resté dedans"),
        ("verrouiller", "bloquer l'accès, ou protéger par un code"),
        ("confirmer", "dire oui une seconde fois"),
        ("annuler", "arrêter avant que ce soit fait"),
        ("placer", "mettre à l'endroit indiqué"),
        ("refermer", "remettre en place ce qu'on a ouvert"),
    ], cols=2, corrige=True,
       notes="Les huit paires sont celles de l'exercice interactif. Faire l'oral d'abord, "
             "avec les gestes : les élèves miment, la classe nomme.")

    d.pratique('Production', "Six consignes d'appareil",
               "Complétez avec le verbe et la préposition qui conviennent.", [
        ("___ le bouton vert.", "Appuyez sur"),
        ("___ votre carte ___ la fente.", "Insérez … dans"),
        ("___ la feuille face vers le bas.", "Placez"),
        ("___ l'adresse courriel.", "Confirmez"),
        ("___ bien la porte de côté.", "Refermez"),
        ("___ votre original avant de partir.", "Retirez"),
    ], cols=2, corrige=True,
       notes="Le dernier est celui à souligner : c'est la consigne que tous les appareils "
             "publics donnent et que presque personne n'écoute.")

    d.billet(
        "Écrivez les trois gestes que demande un appareil que vous utilisez souvent.",
        exemples=[
            "Employez trois verbes différents de la séance, avec leur préposition.",
            "Un guichet, un terminal de paiement, une machine à laver du sous-sol.",
        ],
        notes="Les billets serviront de matière première en C3, où les élèves mettront "
              "leurs gestes en ordre avec des marqueurs de temps.")

    return d.save(dossier)
