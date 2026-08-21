# -*- coding: utf-8 -*-
"""A3 · Les mots du rendez-vous.
Bloc A « Je découvre » · couleur framboise · 75 min. Vocabulaire.
Source : `FC_CARDS`, exercices `prVocab` et `prImg`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-rendezvous/images/')


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Les mots du rendez-vous",
        chapeau="Seize mots, et pas un de médical. Ce sont ceux de "
                "l'accueil, du téléphone et du calendrier — ceux qu'on "
                "entend avant même d'avoir vu un médecin.",
        duree='75 minutes')

    d.titre(notes="Troisième séance. Ramasser les enregistrements de A2 s'il y en a, et "
                  "en faire écouter deux. Puis annoncer : aujourd'hui, aucun mot "
                  "compliqué de médecine — que des mots de bureau et de téléphone.")

    d.objectifs([
        "nommer les seize mots du module et les associer à leur définition ;",
        "reconnaître ces mots sur une image ou dans une phrase ;",
        "employer l'article juste avec chacun ;",
        "distinguer un étourdissement d'une perte de connaissance.",
    ])

    d.declencheur(
        'Observation', "Cet objet, on vous le demande à chaque rendez-vous. Comment "
                       "s'appelle-t-il exactement ?",
        image=IMG + 'carte-main.jpg',
        pistes=[
            "Comment l'appelez-vous, vous ?",
            "Qu'est-ce qu'il y a dessus ?",
            "Que se passe-t-il si la date est passée ?",
            "Où le gardez-vous ?",
        ],
        notes="Beaucoup d'élèves disent « la carte soleil » ou « ma carte du docteur ». "
              "Accueillir toutes les formes, puis donner le nom complet et l'écrire.")

    d.vocabulaire('Vocabulaire · 1 de 4', "Où s'adresser", [
        ("un GMF", "Une clinique où plusieurs médecins et infirmières suivent les mêmes patients."),
        ("la carte d'assurance maladie", "La carte qui donne droit aux soins payés ; elle a un numéro et une date de fin."),
        ("le sans-rendez-vous", "Le service où l'on est reçu le jour même, sans avoir réservé."),
        ("un étourdissement", "Le moment où la tête tourne et où il faut se tenir à quelque chose."),
    ], notes="Faire répéter chaque mot avec son article. « Un GMF » se dit lettre par "
             "lettre : gé-ème-effe.")

    d.vocabulaire('Vocabulaire · 2 de 4', "Au téléphone", [
        ("un symptôme", "Ce que le corps montre ou fait sentir quand quelque chose ne va pas."),
        ("une disponibilité", "Un moment libre qu'on peut vous offrir dans un horaire."),
        ("un rendez-vous de suivi", "Un deuxième rendez-vous, pour revoir un problème déjà examiné."),
        ("une agente administrative", "La personne qui répond au téléphone d'une clinique et donne les rendez-vous."),
    ], notes="« Disponibilité » est le mot que l'agente emploie et que les élèves ne "
             "comprennent presque jamais. Le travailler deux fois.")

    d.vocabulaire('Vocabulaire · 3 de 4', "Dans le bureau", [
        ("un rappel automatisé", "Un message envoyé par une machine, la veille du rendez-vous."),
        ("la tension artérielle", "La force du sang, mesurée avec un brassard autour du bras."),
        ("une prise de sang", "L'examen où l'on prélève un peu de sang pour l'analyser."),
        ("à jeun", "Sans avoir rien mangé depuis plusieurs heures ; on peut boire de l'eau."),
    ], notes="« À jeun » ne prend pas d'article : c'est une locution. Le dire, sinon les "
             "élèves écrivent « un jeun ».")

    d.vocabulaire('Vocabulaire · 4 de 4', "Déplacer ou annuler", [
        ("une ordonnance", "Le papier signé par un médecin qui autorise un examen ou un médicament."),
        ("déplacer un rendez-vous", "Le garder, mais à un autre jour ou à une autre heure."),
        ("des frais d'absence", "L'argent demandé à qui ne s'est pas présenté sans prévenir à temps."),
        ("une boîte vocale", "Le répondeur qui enregistre le message quand personne ne répond."),
    ], notes="« Déplacer » et « annuler » ne veulent pas dire la même chose : c'est tout "
             "le défi 3. Poser la question maintenant, sans répondre.")

    # `capture` n'existe que dans theme.Deck : les présentations la portent, les
    # fiches imprimées non (build/powerpoints/fiche.py n'a pas la méthode). Une
    # fiche noir et blanc n'a de toute façon rien à faire d'une capture d'écran.
    if hasattr(d, 'capture'):
        d.capture('prImg', "Les images du rendez-vous",
                  consigne="Glissez chaque photo sur la phrase qui la décrit.",
                  notes="Projeter avant d'ouvrir les tablettes : le groupe décrit deux ou "
                        "trois images à l'oral, puis chacun continue à l'écran.")

    d.piege("Confondre étourdissement et perte de connaissance",
            "« J'ai perdu connaissance » quand la tête a seulement tourné.",
            "« Je me tiens au mur, mais je sais toujours où je suis. »",
            "Les deux n'envoient pas au même endroit : un étourdissement s'examine en "
            "clinique, une perte de connaissance mène souvent à l'urgence. Quand on "
            "n'est pas certain du mot, on décrit ce qu'on a vécu.",
            notes="Règle générale du module, à répéter : si le mot est incertain, décrire "
                  "vaut mieux que nommer.")

    d.pratique('Vocabulaire', "De quel mot s'agit-il ?",
               "Écoutez la définition et donnez le mot, avec son article.", [
        ("Le papier signé qui autorise un examen.", "une ordonnance"),
        ("Sans avoir rien mangé depuis plusieurs heures.", "à jeun"),
        ("La personne qui répond au téléphone de la clinique.", "une agente administrative"),
        ("Un moment libre dans un horaire.", "une disponibilité"),
        ("Le garder, mais à un autre jour.", "déplacer un rendez-vous"),
        ("Le répondeur qui enregistre les messages.", "une boîte vocale"),
    ], corrige=True,
       notes="Exiger l'article à chaque réponse. Sans article, la réponse ne compte pas — "
             "l'annoncer avant de commencer.")

    d.billet(
        "Choisissez trois mots du jour et écrivez une phrase avec chacun.",
        exemples=[
            "Des phrases vraies si possible : votre carte, votre clinique, votre horaire.",
            "Soulignez le mot dans chaque phrase.",
        ],
        notes="Ramasser et relire avant B1 : les erreurs d'article se corrigent en trente "
              "secondes au début de la séance suivante.")

    return d.save(dossier)
