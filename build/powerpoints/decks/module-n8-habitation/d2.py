# -*- coding: utf-8 -*-
"""D2 · Le subjonctif de ce qu'on demande
Bloc D « Défi 3 · Porter la décision plus haut » · couleur ambre · 75 min.
Source : exercice `t3sub` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Je demande que le dossier soit rouvert",
        chapeau="Le subjonctif ne dit pas le doute. Il dit que la phrase ne "
                "se contente pas de rapporter un fait — et une demande de "
                "révision en est pleine.",
        duree='75 minutes')

    d.titre(notes="Dernière séance avant les productions. Commencer par défaire "
                  "l'explication habituelle : « le subjonctif exprime le doute » est "
                  "faux, et cette phrase-là a fait perdre du temps à beaucoup de "
                  "gens.")

    d.objectifs([
        "employer le subjonctif après un verbe de volonté ;",
        "connaître les deux expressions impersonnelles qui font exception ;",
        "employer le subjonctif après un verbe d'opinion nié ;",
        "distinguer les conjonctions qui l'exigent de celles qui le refusent.",
    ], notes="Les trois demandes de la lettre du bloc E sont au subjonctif. C'est la "
             "séance qui les rend possibles.")

    d.declencheur(
        'Observation', "« Je veux qu'il vienne. » Y a-t-il un doute dans cette phrase ?",
        pistes=[
            "Est-ce qu'on doute de sa venue ?",
            "Alors pourquoi le subjonctif ?",
            "Comparez : « je sais qu'il vient » et « je veux qu'il vienne ».",
            "Qu'est-ce qui change, dans le premier verbe ?",
        ],
        notes="Laisser le groupe buter, puis donner la réponse : c'est le verbe "
              "introducteur qui commande le mode, jamais la probabilité de ce qui "
              "suit. Une fois ceci posé, la suite de la séance est mécanique.")

    d.regle("Ce n'est pas le doute, c'est le verbe qui précède",
            "Après une volonté, une nécessité, une émotion ou certaines "
            "conjonctions, le français change de mode — que le fait se "
            "réalise ou non.",
            precision="« Je veux qu'il vienne » n'exprime aucun doute sur sa venue. "
                      "« Je sais qu'il vient » est certain, et c'est le verbe "
                      "« savoir » qui l'impose, pas le monde.",
            notes="Diapositive à photographier. C'est le seul point théorique de la "
                  "séance ; tout le reste est une liste à connaître.")

    d.tableau('Déclencheurs', "Quatre familles, et leurs exceptions",
              ['Famille', 'Exemples'],
              [["Volonté, demande", "je demande que · je souhaite que · je tiens à ce que"],
               ["Impersonnelles", "il faut que · il est important que — sauf il paraît que, il me semble que"],
               ["Adjectif + que", "je suis surprise que — sauf les adjectifs de certitude"],
               ["Conjonctions", "afin que · bien que · avant que · jusqu'à ce que — mais après que veut l'indicatif"]],
              cle=0,
              notes="Diapositive à photographier. Les exceptions ont un point commun "
                    "qu'il vaut la peine de nommer : elles RAPPORTENT quelque chose "
                    "plutôt que de le vouloir. La règle générale les explique.")

    d.pratique('Grammaire', "Subjonctif ou indicatif ?",
               "Mettez le verbe au mode qui convient.", [
        ("Je demande que le dossier ___ (être) rouvert et réexaminé.", "soit"),
        ("Je souhaite qu'une autre personne l'___ (examiner).", "examine"),
        ("Il est important que la réponse me ___ (parvenir) par écrit.", "parvienne"),
        ("Afin que le dossier ___ (être) complet, je joins la facture.", "soit"),
        ("Je ne crois pas que cette conclusion ___ (être) fondée.", "soit"),
        ("Il me semble que le rapport ___ (parler) d'un autre drain.", "parle"),
        ("Je suis certaine que la facture ___ (se trouver) au dossier.", "se trouve"),
        ("Après que la réponse ___ (arriver), je déciderai de la suite.", "sera arrivée"),
    ], corrige=True,
       notes="Les trois derniers sont les exceptions, et ils sont volontairement "
             "groupés à la fin. Faire nommer l'exception à chaque fois plutôt que de "
             "seulement corriger la forme.")

    d.tableau('Formes', "Les subjonctifs qui reviennent dans la lettre",
              ['Infinitif', 'Après « que »'],
              [["être", "que je sois · qu'il soit · qu'ils soient"],
               ["avoir", "que j'aie · qu'il ait · qu'ils aient"],
               ["faire", "que je fasse · qu'il fasse · qu'ils fassent"],
               ["parvenir", "que je parvienne · qu'il parvienne"],
               ["recevoir", "que je reçoive · qu'il reçoive"]],
              cle=0,
              notes="Diapositive à photographier. Cinq verbes suffisent pour écrire la "
                    "lettre du bloc E. Les faire réciter une fois, pas plus.")

    d.piege(
        'Mode',
        "après que le dossier soit rouvert",
        "après que le dossier sera rouvert",
        "« Après que » veut l'indicatif : ce qui suit est présenté comme "
        "réalisé. « Avant que », lui, veut le subjonctif — ce qui n'est pas "
        "encore arrivé. La faute avec « après que » est si répandue qu'on "
        "l'entend partout, y compris à la radio ; à l'écrit soutenu, "
        "l'indicatif reste la forme attendue.",
        notes="Ne pas dramatiser : signaler que la faute est en train de gagner, et "
              "que l'écrit d'affaires reste en retard sur l'oral. C'est un fait de "
              "langue, pas une faute morale.")

    d.cartes('Modèles', "Les trois demandes d'une lettre de révision", [
        ("La première",
         "« Je demande que le dossier soit rouvert. » Verbe de volonté, "
         "« que », subjonctif. Rien d'autre dans la phrase."),
        ("La deuxième",
         "« … que la contre-expertise jointe soit examinée par une personne "
         "n'ayant pas participé à la première décision. » On ne répète pas "
         "« je demande » : le « que » suffit."),
        ("La troisième",
         "« … et qu'une réponse finale écrite et motivée me soit transmise "
         "dans le délai de soixante jours. » Le délai est rappelé ici, et "
         "nulle part ailleurs."),
    ], cols=1,
       notes="Faire écrire les trois au tableau, numérotées. Elles se recopient telles "
             "quelles dans la lettre du bloc E, avec le dossier de chacun.")

    d.billet(
        "Écrivez vos trois demandes, au subjonctif, sur une seule phrase.",
        exemples=[
            "Commencez par « Je demande en conséquence que… ».",
            "Puis « que… » et « et que… », sans répéter le verbe.",
        ],
        notes="C'est le dernier paragraphe de la lettre du bloc E, écrit deux séances "
              "à l'avance. À la fin du bloc D, il ne reste plus à écrire que l'objet "
              "et la citation du motif.")

    return d.save(dossier)
