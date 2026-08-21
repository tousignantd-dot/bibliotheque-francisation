# -*- coding: utf-8 -*-
"""B2 · Ce qui s'ajoute au tarif.
Bloc B « Défi 1 · Le camion » · couleur acier · 75 min.
Source : exercices `t1calcul` et `t1quest`, mini-leçon `t1calcul`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='acier',
        titre="Ce qui s'ajoute au tarif",
        chapeau="Le premier chiffre n'est jamais le vrai chiffre. Il en manque "
                "toujours trois autres.",
        duree='75 minutes')

    d.titre(notes="Séance de calcul et de questions. Prévoir une calculatrice par table : "
                  "le but n'est pas l'arithmétique, c'est de voir l'écart entre le tarif "
                  "annoncé et le total réel.")

    d.objectifs([
        "distinguer le tarif horaire du total à payer ;",
        "nommer les quatre choses qui s'ajoutent au tarif ;",
        "calculer un total à voix haute avec son interlocutrice ;",
        "poser les sept questions qui évitent une surprise.",
    ])

    d.tableau('Le tarif', "Ce qu'il comprend, ce qu'il ne comprend jamais",
              ['Compris dans le tarif', "Jamais compris"],
              [["deux hommes et le camion", "les boîtes"],
               ["l'essence", "le papier d'emballage"],
               ["les couvertures", "le ruban adhésif"],
               ["le diable", "le troisième homme"]],
              cle=0,
              note="Les boîtes s'achètent, ou se ramassent gratuitement derrière une "
                   "épicerie deux semaines d'avance.",
              notes="La colonne de droite est celle qui coûte : elle s'achète, et elle "
                    "s'achète tard, donc cher.")

    d.cartes("Les quatre choses qui s'ajoutent", "Chacune se demande avant", [
        ("Le minimum de trois heures",
         "Un déménagement d'une heure et demie se paie trois heures. Le camion a été "
         "sorti pour vous."),
        ("Le temps de déplacement",
         "Une heure de plus, au tarif horaire : l'aller au garage et le retour."),
        ("Les suppléments",
         "Un homme de plus, un piano, un escalier extérieur, un étage de plus."),
        ("La protection complète",
         "L'assurance de base est comprise, mais elle couvre 0,60 $ la livre."),
    ], notes="Faire calculer ce que rapporte l'assurance de base pour un téléviseur de "
             "dix kilos : treize dollars. Le chiffre frappe plus que l'explication.")

    d.regle("La question qui rapporte le plus",
            "« Est-ce qu'il y a autre chose qui s'ajoute au tarif ? »",
            precision="Aucune compagnie ne cache ces frais : elles les disent quand on les "
                      "demande. Le problème n'est jamais l'honnêteté, c'est la question "
                      "qui n'a pas été posée.",
            notes="Diapositive à photographier. Faire répéter la phrase par tout le "
                  "groupe, deux fois, avec l'intonation d'un appel.")

    d.pratique('Calcul', "Combien ça coûte, en tout ?",
               "Le tarif est de 145 $ l'heure, minimum trois heures, plus une heure "
               "de déplacement.", [
        ("3 h de travail, deux hommes", "3 h + 1 h = 4 h × 145 $ = 580 $"),
        ("4 h de travail, deux hommes", "4 h + 1 h = 5 h × 145 $ = 725 $"),
        ("4 h de travail, trois hommes", "5 h × 190 $ = 950 $, mais souvent moins d'heures"),
        ("6 h de travail, deux hommes", "6 h + 1 h = 7 h × 145 $ = 1 015 $"),
        ("4 h + protection complète", "725 $ + 45 $ = 770 $"),
        ("2 h de travail seulement", "minimum 3 h + 1 h = 4 h × 145 $ = 580 $"),
    ], corrige=True,
       notes="Le dernier cas est le plus instructif : deux heures de travail coûtent le "
             "même prix que trois. Faire dire pourquoi.")

    d.piege("Croire que le tarif est le total",
            "145 de l'heure, quatre heures, ça fait 580 $.",
            "145 de l'heure, quatre heures plus une, ça fait 725 $.",
            "Il manque l'heure de déplacement, et souvent un supplément d'escalier. "
            "L'écart est de cent quarante-cinq dollars sur ce seul exemple — le prix "
            "d'une semaine d'épicerie.",
            notes="Écrire les deux totaux au tableau, l'un sous l'autre. L'écart se voit "
                  "mieux qu'il ne s'explique.")

    d.pratique('Questions', "La question et ce qu'elle vous évite",
               "L'enseignante donne ce qu'on veut savoir ; le groupe formule la "
               "question.", [
        ("Savoir combien vous paierez vraiment",
         "Est-ce qu'il y a autre chose qui s'ajoute au tarif ?"),
        ("Savoir si trois heures seront facturées pour deux",
         "Y a-t-il un minimum d'heures ?"),
        ("Savoir ce qui arrive si un meuble est abîmé",
         "Qu'est-ce que l'assurance de base couvre exactement ?"),
        ("Savoir combien d'argent sortir aujourd'hui",
         "Quel dépôt faut-il verser pour réserver ?"),
        ("Savoir si vous pouvez encore changer d'idée",
         "Jusqu'à quand puis-je annuler sans perdre le dépôt ?"),
        ("Savoir si votre escalier coûtera plus cher",
         "Y a-t-il un supplément pour un escalier extérieur ?"),
    ], corrige=True,
       notes="C'est l'exercice t1quest du module. Exiger la question complète, pas le mot "
             "clé : c'est la formulation qui s'apprend ici.")

    d.billet(
        "Trouvez le numéro d'une vraie compagnie de déménagement de votre quartier.",
        exemples=[
            "Notez son nom et son numéro dans votre carnet.",
            "N'appelez pas encore : on le fera ensemble au bloc E.",
        ],
        notes="Le devoir ancre le module dans le vrai. Certains appelleront quand même — "
              "c'est très bien, leur faire raconter la semaine suivante.")

    return d.save(dossier)
