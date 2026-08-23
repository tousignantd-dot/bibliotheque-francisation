# -*- coding: utf-8 -*-
"""B4 · Jusqu'où ça va, et ce que ça entraîne
Bloc B « Défi 1 · Frapper à la porte d'en haut » · couleur teal · écoute et
réponds · 75 min.
Source : exercices `t1inten` et `t1que`, et leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='teal',
        titre="Jusqu'où ça va, et ce que ça entraîne",
        chapeau="« C'est insupportable » ne fait voir absolument rien. "
                "« C'est assez fort pour faire bouger le luminaire du salon » "
                "met l'image dans la tête de l'autre, et il ne peut plus la "
                "retirer.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 1. Elle réunit deux points de langue qui "
                  "servent à la même chose : rendre visible ce que l'autre n'a jamais "
                  "entendu.")

    d.objectifs([
        "employer tellement… que, si… que, assez… pour, trop… pour ;",
        "choisir entre « pour » et « pour que » selon le sujet ;",
        "employer « ne… que » pour restreindre sans nier ;",
        "remplacer un adjectif par une démonstration.",
    ], notes="Le troisième objectif commence par un contresens à défaire : « ne… que » "
             "n'est pas une négation.")

    d.declencheur(
        'Observation', "Comment décrire un bruit à quelqu'un qui ne l'a jamais entendu ?",
        pistes=[
            "Est-ce que « très fort » lui apprend quelque chose ?",
            "Et « assez fort pour faire bouger le luminaire » ?",
            "Qu'est-ce qui a changé entre les deux ?",
            "Essaie avec un bruit de chez toi.",
        ],
        notes="La bonne réponse est toujours la même : on décrit l'effet, pas le bruit. "
              "C'est la suite directe de la séance A3.")

    d.regle("L'intensité appelle sa conséquence",
            "Si ou tellement + adjectif + que ; assez + adjectif + pour.",
            precision="« Le bruit est tellement régulier qu'il me réveille avant de "
                      "commencer. » La conséquence est un fait, donc à l'indicatif. "
                      "Avec un nom, « tellement » prend « de » : tellement de matins. "
                      "« Assez fort pour traverser le plancher » : le seuil est atteint.",
            notes="Diapositive à photographier. Faire produire une phrase de chaque "
                  "forme sur le bruit du dossier, avant la pratique.")

    d.tableau('Analyse', "Pour ou pour que ?",
              ['La question à se poser', 'La réponse'],
              [["Même sujet ?", "assez fort pour me réveiller"],
               ["Sujet différent ?", "assez sérieux pour qu'elle soit avisée"],
               ["Le seuil est atteint ?", "assez, suffisamment"],
               ["Le seuil est dépassé ?", "trop tôt pour me rendormir"]],
              note="Le même test vaut pour « avant de / avant que » et « afin de / "
                   "afin que ». Une question, trois structures réglées.",
              cle=1,
              notes="Diapositive à photographier. Le test se fait en une seconde : qui "
                    "fait l'action de la conséquence ?")

    d.regle("« ne… que » veut dire « seulement »",
            "Je n'entends que le moteur : j'entends le moteur, et rien d'autre.",
            precision="Ce n'est pas une négation, malgré le « ne ». Le « que » se place "
                      "devant ce qu'on restreint, et non après l'auxiliaire comme "
                      "« pas ». Deux usages : désamorcer — « je ne me plains que du "
                      "matin » — et montrer ce qui manque — « il n'a posé que le "
                      "caoutchouc ».",
            notes="Diapositive à photographier. Le test qui ne rate jamais : remplacer "
                  "mentalement par « seulement ».")

    d.piege('Compréhension',
            "Je n'entends que le moteur = je n'entends rien",
            "Je n'entends que le moteur = j'entends le moteur, et rien d'autre",
            "Le contresens est fréquent parce que le « ne » ressemble à celui de "
            "« ne… pas ». Deux phrases opposées à comparer : « je n'entends pas le "
            "moteur » et « je n'entends que le moteur ». La seconde est positive.",
            notes="Faire produire trois phrases avec « seulement », puis les faire "
                  "réécrire avec « ne… que ». C'est l'exercice le plus efficace.")

    d.pratique('Pratique', "Complétez, puis restreignez",
               "Les cinq premières portent sur l'intensité, les trois dernières sur la restriction.", [
        ("Il est ___ régulier que je me réveille avant qu'il commence.", "tellement (ou si)"),
        ("La rampe résonne ___ fort que je l'entends du deuxième étage.", "si (ou tellement)"),
        ("Elle a noté ___ de matins que son carnet est presque plein.", "tellement (ou tant)"),
        ("C'est ___ sérieux pour que la propriétaire en soit avisée.", "assez (ou suffisamment)"),
        ("Quinze matins de suite, c'est ___ répétitif pour passer pour un accident.", "trop"),
        ("Je me plains seulement du matin.", "Je ne me plains que du matin."),
        ("Il a fait seulement une des trois choses promises.", "Il n'a fait qu'une des trois choses promises."),
        ("Je demande seulement une heure de sommeil de plus.", "Je ne demande qu'une heure de sommeil de plus."),
    ], corrige=True,
       notes="Les trois dernières se corrigent à l'oral, puis se réécrivent. Faire "
             "remarquer où se déplace le « que » à chaque fois.")

    d.billet(
        "Décris un bruit de chez toi sans employer un seul adjectif.",
        exemples=[
            "Emploie « assez… pour » ou « tellement… que ».",
            "Donne un effet que quelqu'un pourrait constater.",
        ],
        notes="Deux minutes. Fin du défi 1 : le groupe sait maintenant parler au "
              "voisin. Le défi 2 lui apprend à rapporter ce qu'il a répondu.")

    return d.save(dossier)
