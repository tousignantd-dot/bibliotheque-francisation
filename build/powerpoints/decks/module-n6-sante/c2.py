# -*- coding: utf-8 -*-
"""C2 · Ce qui se travaille et ce qui ne se travaille pas
Bloc C « Défi 2 » · couleur teal · 75 min. Écoute et réponse.
Source : exercice `t2precis` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='teal',
        titre="Ce qui se travaille et ce qui ne se travaille pas",
        chapeau="La personne devant vous n'a que ce que vous dites. Ce que "
                "vous ne dites pas n'existe pas, et ce que vous dites en "
                "adjectifs ne se compare à rien dans six semaines.",
        duree='75 minutes')

    d.titre(notes="Séance charnière du module. Elle est courte en grammaire et longue "
                  "en reformulation : prévoir au moins trente minutes de pratique "
                  "orale à deux.")

    d.objectifs([
        "donner un repère de temps plutôt qu'une durée floue ;",
        "décrire un changement plutôt qu'un état ;",
        "raconter une scène plutôt que donner un adjectif ;",
        "décrire avec ses mots quand le mot juste manque.",
    ], notes="Les trois premiers objectifs sont trois réflexes, dans cet ordre. Le "
             "quatrième est celui qui libère : on peut tout dire sans connaître le "
             "vocabulaire médical.")

    d.declencheur(
        'Observation', "« Je ne veux pas déranger » — d'où vient cette phrase ?",
        pistes=[
            "Est-ce qu'on vous a appris à ne pas se plaindre ?",
            "Qui dérange-t-on, au juste, dans un rendez-vous prévu pour vous ?",
            "Est-ce que vous diriez la même chose dans votre première langue ?",
        ],
        notes="Cinq minutes. C'est la phrase notée en C1. Ne pas la moquer : elle "
              "vient d'une éducation, et souvent d'une bonne. La retourner : dans un "
              "rendez-vous, vous n'êtes pas un dérangement, vous êtes le rendez-vous.")

    d.tableau('Analyse', "Trois réflexes, trois transformations",
              ['Ce qu\'on dit', 'Ce qui peut servir'],
              [["Depuis un bout de temps", "depuis février, le mois où mon fils est parti"],
               ["Je suis fatiguée", "vers dix heures, il faut que je m'assoie"],
               ["Je manque de souffle", "je montais douze marches en parlant, maintenant non"],
               ["Je ne prends rien", "rien d'ordonnance, mais des vitamines l'hiver"]],
              cle=0,
              note="Un repère de temps, un changement, une scène : trois réflexes et rien de plus.",
              notes="Diapositive à photographier. C'est le tableau le plus utile du "
                    "module hors de la classe. Le faire recopier à la main.")

    d.regle("On ne compare pas votre fatigue à celle des autres",
            "On la compare à la vôtre d'avant.",
            precision="C'est pour cela qu'un changement vaut dix adjectifs : il a une "
                      "date, il se vérifie, et il se recompare dans six semaines. "
                      "« Avant je ne m'assoyais pas » est un renseignement ; « je "
                      "suis fatiguée » n'en est pas un.",
            notes="Diapositive à photographier. Faire produire trois exemples par le "
                  "groupe, sur des sujets non médicaux, avant de revenir au dossier "
                  "de Leyla.")

    d.cartes('Méthode', "Quatre façons de rendre une phrase utilisable", [
        ("Accrocher à un évènement", "Personne ne se trompe sur le mois où son fils a déménagé."),
        ("Nommer un avant et un maintenant", "Avant je faisais ceci, maintenant je ne le fais plus."),
        ("Donner un lieu et un nombre", "Chez ma cliente, il y a douze marches."),
        ("Décrire quand le mot manque", "C'est comme quand on se lève trop vite."),
    ], notes="La quatrième carte est celle qui libère. Faire dire la phrase à voix "
             "haute par tout le groupe : « Je ne connais pas le mot, mais c'est comme "
             "quand… »")

    d.piege('Communication',
            "ce n'est pas si pire, il y a plus malade que moi",
            "ça dure depuis huit mois et ça change ma façon de travailler",
            "Minimiser fait sortir un problème du dossier. Ce n'est pas de la "
            "modestie mal placée : c'est un renseignement qui n'est pas donné, "
            "et personne ne pourra le deviner. Vous ne dérangez pas — le "
            "rendez-vous existe pour cela.",
            notes="La correction la plus importante de la séance. La faire reformuler "
                  "par trois élèves. Plusieurs auront envie de raconter une fois où "
                  "ça leur a coûté cher : laisser la place.")

    d.pratique('Reformulation', "Rendez la phrase utilisable",
               "À deux. Une personne lit, l'autre reformule.", [
        ("Je suis fatiguée.", "vers dix heures, il faut que je m'assoie ; avant, non"),
        ("Ça fait un bout de temps.", "depuis février, le mois où mon fils a déménagé"),
        ("Je manque de souffle.", "je montais douze marches en parlant, maintenant j'arrête"),
        ("Je ne prends rien.", "rien d'ordonnance, mais des vitamines l'hiver"),
        ("Des fois ça va, des fois moins.", "le samedi est meilleur, les autres jours se ressemblent"),
        ("Ce n'est pas si pire.", "ça dure depuis huit mois et ça change mon travail"),
    ], corrige=True,
       notes="Vingt minutes à deux avant d'afficher la correction. Insister : il n'y "
             "a pas une seule bonne reformulation, seulement des phrases qui "
             "contiennent une date, un avant, ou une scène.")

    d.pratique('Pratique orale', "Votre propre changement, en trois phrases",
               "À deux, chacun son tour. L'autre écoute et redemande.", [
        ("Phrase 1 : depuis quand, accroché à un évènement.", ""),
        ("Phrase 2 : ce qui a changé, avant et maintenant.", ""),
        ("Phrase 3 : une scène, avec un lieu et un nombre.", ""),
    ],
       notes="Quinze minutes. Le sujet peut être n'importe quoi : le sommeil, le dos, "
             "le trajet, le français. Celui qui écoute a une seule consigne : "
             "redemander une précision, une seule fois.")

    d.billet(
        "Écrivez la phrase que vous diriez en entrant dans le bureau.",
        exemples=[
            "Une seule phrase, la vôtre.",
            "Elle doit contenir une date ou un changement.",
        ],
        notes="Deux minutes. Ces billets serviront directement au jeu de rôle de E1 : "
              "chacun entrera avec sa propre première phrase, écrite trois semaines "
              "plus tôt.")

    return d.save(dossier)
