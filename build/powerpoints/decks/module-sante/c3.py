# -*- coding: utf-8 -*-
"""C3 · Avoir besoin de.
Bloc C « Défi 2 · La langue » · couleur teal (écoute et réponds) · 60 min.
Source du module : exercice `l3` et sa mini-leçon « Avoir besoin de ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='teal',
        titre='Avoir besoin de',
        chapeau="La phrase qui ouvre presque toutes les demandes : à l'accueil, au "
                "comptoir, au téléphone. Et le petit mot « de » ne tombe jamais.",
        duree='60 minutes')

    d.titre(notes="Séance la plus immédiatement utile du défi 2. Le dire : ce qu'on "
                  "apprend aujourd'hui sert dès la sortie du cours.")

    d.objectifs([
        "employer avoir besoin de + nom ;",
        "employer avoir besoin de + infinitif ;",
        "faire l'élision devant une voyelle ;",
        "formuler une demande claire et polie.",
    ])

    d.regle('La règle',
            "avoir besoin + de + ce qu'il vous faut.",
            precision="Un nom (« j'ai besoin d'un rendez-vous ») ou un verbe à "
                      "l'infinitif (« j'ai besoin de me reposer »). Le « de » reste dans "
                      "les deux cas.",
            notes="La diapositive à photographier. Insister sur « avoir » : c'est un "
                  "verbe, et « besoin » n'en est pas un.")

    d.tableau('Analyse', "Ce qui suit le « de »",
              ['Ce qu\'on met après', 'Exemple'],
              [["un nom", "j'ai besoin de médicaments"],
               ["un nom qui commence par une voyelle", "j'ai besoin d'aide"],
               ["un déterminant + nom", "j'ai besoin d'un rendez-vous"],
               ["un verbe à l'infinitif", "j'ai besoin de me reposer"]],
              cle=0,
              note="Devant une voyelle, « de » devient « d' ». Devant un verbe, jamais.",
              notes="La dernière ligne règle une question fréquente : on n'écrit pas "
                    "« d'aller », mais bien « de dormir », « de me reposer ».")

    d.pratique('Pratique · 1 de 4', "Complétez",
               "Avec « de + nom » ou « de + infinitif ».", [
        ("J'ai besoin ___ avec le médecin.", "j'ai besoin d'un rendez-vous"),
        ("J'ai besoin ___ quelques jours.", "j'ai besoin de me reposer"),
        ("J'ai besoin ___ pour la toux.", "j'ai besoin de médicaments"),
        ("J'ai besoin ___ au moins huit heures.", "j'ai besoin de dormir"),
        ("J'ai besoin ___ pour remplir le formulaire.", "j'ai besoin d'aide"),
    ], corrige=True,
       notes="C'est l'exercice 3 du défi 2. Faire justifier chaque forme : nom ou "
             "infinitif, voyelle ou consonne.")

    d.piege("Le piège du « de » qui saute",
            "J'ai besoin un rendez-vous.",
            "J'ai besoin d'un rendez-vous.",
            "C'est le « de » qui relie « besoin » à la suite. Sans lui, la phrase "
            "s'arrête net et l'interlocuteur attend la fin.",
            notes="Erreur la plus fréquente et la plus audible. Faire répéter la bonne "
                  "forme trois fois, à voix haute.")

    d.piege("Le piège du verbe manquant",
            "Je besoin d'un médicament.",
            "J'ai besoin d'un médicament.",
            "« Besoin » est un nom, pas un verbe. Il lui faut « avoir » devant : j'ai, "
            "tu as, il a, nous avons, vous avez, ils ont.",
            notes="Conjuguer les six formes au tableau : j'ai besoin, tu as besoin… "
                  "Trente secondes, et ça se règle.")

    d.pratique('Pratique · 2 de 4', "Transformez la demande",
               "Dites-le avec « avoir besoin de ».", [
        ("Je voudrais un rendez-vous.", "J'ai besoin d'un rendez-vous."),
        ("Je dois me reposer.", "J'ai besoin de me reposer."),
        ("Il me faut de l'aide.", "J'ai besoin d'aide."),
        ("Nous voulons des explications.", "Nous avons besoin d'explications."),
    ], corrige=True,
       notes="Faire remarquer que les quatre formulations de départ sont correctes "
             "aussi. On ajoute un outil, on n'en retire pas.")

    d.pratique('Pratique · 3 de 4', "Au comptoir et au téléphone",
               "Formulez la demande complète.", [
        ("À la clinique, vous voulez voir un médecin cette semaine.",
         "J'ai besoin d'un rendez-vous cette semaine, s'il vous plaît."),
        ("À la pharmacie, votre ordonnance est terminée.",
         "J'ai besoin d'un renouvellement de mon ordonnance."),
        ("Au travail, vous voulez deux jours de congé.",
         "J'ai besoin de me reposer deux jours."),
        ("À l'accueil, vous ne comprenez pas le formulaire.",
         "J'ai besoin d'aide pour remplir le formulaire."),
    ], corrige=True,
       notes="La deuxième prépare directement le courriel de E1. Le dire au groupe.")

    d.pratique('Pratique · 4 de 4', "Vos vrais besoins",
               "Quatre phrases, sur vous, aujourd'hui.", [
        ("Un besoin de santé", "un rendez-vous, un médicament, du repos"),
        ("Un besoin au travail", "un horaire, une explication, un papier"),
        ("Un besoin pour vos études", "de l'aide, du temps, un document"),
        ("Un besoin pour votre famille", "n'importe lequel, du moment qu'il est vrai"),
    ], corrige=False,
       notes="Dix minutes. Circuler et vérifier une seule chose : le « de » est-il "
             "là ? C'est le critère de la séance.")

    d.billet(
        "Écrivez deux besoins réels : un avec un nom, un avec un verbe.",
        exemples=[
            "« J'ai besoin d'un… » et « j'ai besoin de… ».",
            "Des besoins vrais, que vous pourriez formuler demain.",
        ],
        notes="Ramasser. Ces deux phrases entrent telles quelles dans le courriel de E1.")

    return d.save(dossier)
