# -*- coding: utf-8 -*-
"""C1 · Le futur proche.
Bloc C « Défi 2 · La langue » · couleur ambre (écriture) · 75 min.
Source du module : exercice `l1` et sa mini-leçon « Le futur proche ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='ambre',
        titre='Le futur proche',
        chapeau="« Je vais voir le médecin jeudi. » Deux verbes qui travaillent "
                "ensemble : le premier se conjugue, le second ne bouge jamais.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2. Annoncer le programme : quatre points de langue, "
                  "tous tirés des deux dialogues déjà entendus. Rien de nouveau à "
                  "comprendre, seulement à nommer.")

    d.objectifs([
        "former le futur proche avec aller + infinitif ;",
        "conjuguer aller au présent, aux six personnes ;",
        "parler d'un rendez-vous à venir ;",
        "reconnaître la négation du futur proche.",
    ])

    d.regle('La règle',
            "aller au présent + un verbe à l'infinitif.",
            precision="« Je vais prendre un rendez-vous. » Seul « aller » change avec la "
                      "personne. Le deuxième verbe reste à l'infinitif, toujours.",
            notes="La diapositive à photographier. Tout le reste de la séance en "
                  "découle.")

    d.tableau('Analyse', "Aller au présent — les six personnes",
              ['La personne', 'Le futur proche'],
              [["je", "je vais prendre"],
               ["tu", "tu vas appeler"],
               ["il / elle", "elle va voir"],
               ["nous", "nous allons attendre"],
               ["vous", "vous allez recevoir"],
               ["ils / elles", "ils vont arriver"]],
              cle=0,
              notes="Le deuxième verbe est identique dans les six lignes : le faire "
                    "remarquer à voix haute, c'est tout le point du tableau. Puis "
                    "couvrir la colonne de droite et redire les six formes de mémoire. "
                    "Deux minutes, debout.")

    d.pratique('Pratique · 1 de 4', "Complétez",
               "Le verbe au futur proche.", [
        ("Demain, je ___ un rendez-vous.", "je vais prendre un rendez-vous"),
        ("Tu ___ la clinique.", "tu vas appeler la clinique"),
        ("Elle ___ le médecin jeudi.", "elle va voir le médecin jeudi"),
        ("Nous ___ notre tour.", "nous allons attendre notre tour"),
        ("Vous ___ vos résultats bientôt.", "vous allez recevoir vos résultats bientôt"),
        ("Les patients ___ à neuf heures.", "les patients vont arriver à neuf heures"),
    ], corrige=True,
       notes="C'est l'exercice 1 du défi 2. Le faire à l'écrit, puis relire à voix "
             "haute : la forme s'entend mieux qu'elle ne se voit.")

    d.piege("Le piège du deuxième verbe conjugué",
            "Je vais prends un rendez-vous.",
            "Je vais prendre un rendez-vous.",
            "Après « aller », le deuxième verbe ne se conjugue jamais. Un seul verbe "
            "porte la personne dans la phrase, et c'est « aller ».",
            notes="Erreur la plus fréquente, dans toutes les langues d'origine. La "
                  "traiter longuement, elle revient jusqu'à la fin du module.")

    d.piege("Le piège du « à »",
            "Je vais à prendre un rendez-vous.",
            "Je vais prendre un rendez-vous.",
            "Rien ne s'intercale entre les deux verbes. « Je vais à la clinique » est "
            "correct — mais là, « aller » garde son vrai sens de déplacement, et il est "
            "suivi d'un lieu, pas d'un verbe.",
            notes="La comparaison des deux emplois d'« aller » éclaire : déplacement "
                  "vers un lieu, ou futur devant un verbe.")

    d.pratique('Pratique · 2 de 4', "Déplacement ou futur ?",
               "Qu'est-ce que « aller » veut dire ici ?", [
        ("Je vais à la pharmacie.", "déplacement — un vrai trajet"),
        ("Je vais prendre mon comprimé.", "futur proche — ça va arriver bientôt"),
        ("Nous allons à la clinique jeudi.", "déplacement"),
        ("Nous allons attendre dans la salle d'attente.", "futur proche"),
    ], corrige=True,
       notes="Le test : ce qui suit est-il un lieu ou un verbe ? Simple et fiable.")

    d.pratique('Pratique · 3 de 4', "À la forme négative",
               "La négation entoure « aller ».", [
        ("Je vais attendre.", "Je ne vais pas attendre."),
        ("Elle va prendre ce médicament.", "Elle ne va pas prendre ce médicament."),
        ("Nous allons arriver en retard.", "Nous n'allons pas arriver en retard."),
        ("Vous allez boire de l'alcool.", "Vous n'allez pas boire d'alcool."),
    ], corrige=True,
       notes="Le « ne » se perd à l'oral rapide, mais il s'écrit. Le dire clairement : "
             "ce n'est pas une faute de l'omettre en parlant, c'en est une à l'écrit.")

    d.pratique('Pratique · 4 de 4', "Votre semaine",
               "Quatre phrases au futur proche, sur votre vraie semaine.", [
        ("Un rendez-vous", "Je vais voir le dentiste mardi."),
        ("Un appel", "Je vais appeler la clinique demain matin."),
        ("Un médicament", "Je vais finir ma boîte vendredi."),
        ("Autre chose", "n'importe quoi, du moment que c'est vrai"),
    ], corrige=False,
       notes="Dix minutes. Ramasser à la fin de la séance pour repérer les « vais "
             "prends » qui subsistent.")

    d.billet(
        "Écrivez trois choses que vous allez faire cette semaine pour votre santé.",
        exemples=[
            "Trois phrases au futur proche.",
            "Un rendez-vous, un appel, un médicament — ou autre chose.",
        ],
        notes="Ramasser. Le repérage des erreurs sur ces trois phrases prend deux "
              "minutes et dit exactement qui a compris.")

    return d.save(dossier)
