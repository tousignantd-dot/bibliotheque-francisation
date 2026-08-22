# -*- coding: utf-8 -*-
"""B3 · La grille, ligne par ligne
Bloc B « Défi 1 » · couleur teal · 75 min. Compréhension écrite d'un texte suivi.
Source du module : exercice `t1grille` (type `texte`) et la mini-leçon `t1grille`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='teal',
        titre="La grille, ligne par ligne",
        chapeau="Quatre lignes, vingt points. Lue avant d'écrire, une grille "
                "dit où mettre son temps ; lue après la note, elle ne fait "
                "qu'expliquer ce qu'on ne peut plus changer.",
        duree='75 minutes')

    d.titre(notes="Beaucoup d'adultes n'ont jamais vu une grille d'évaluation "
                  "avant leur note. Le dire : ce n'est pas une faveur qu'on "
                  "leur fait, c'est la façon normale de travailler.")

    d.objectifs([
        "lire une grille avant d'écrire ;",
        "trouver dans chaque ligne le mot qui décide ;",
        "répartir son temps selon le barème ;",
        "savoir ce qui n'est jamais évalué.",
    ], notes="Le dernier point vaut la séance à lui seul : l'accent et la "
             "vitesse ne sont évalués nulle part, et cette inquiétude fait "
             "taire des adultes qui auraient beaucoup à dire.")

    d.declencheur(
        'Pour commencer', "Sur quoi croyez-vous qu'un travail écrit est noté ?",
        pistes=[
            "Le nombre de pages ?",
            "Le nombre de fautes ?",
            "Autre chose ?",
        ],
        notes="Noter les réponses au tableau et les comparer à la grille. "
              "L'écart est le vrai contenu de la séance.")

    d.tableau('Analyse', "Vingt points, quatre lignes",
              ['La ligne', 'Ce qu\'elle demande'],
              [["Contenu — 8", "rapporter les sources et distinguer le fait de l'avis"],
               ["Sources — 4", "trois sources nommées, avec leur date"],
               ["Langue — 4", "la phrase, les accords, la ponctuation"],
               ["Organisation — 4", "un paragraphe par idée, des mots qui relient"]],
              cle=0,
              note="La note va à chaque personne selon sa partie, pas à l'équipe en bloc.",
              notes="Diapositive à photographier. La note du bas est celle "
                    "que les élèves retiennent le mieux, et elle change "
                    "l'ambiance des équipes.")

    d.regle("Chaque ligne contient un mot qui décide",
            "Contenu : distingue. Sources : nommée. Organisation : relient.",
            precision="Soulignez ce mot-là. C'est lui que la personne qui "
                      "corrige cherchera dans votre texte, et rien d'autre.",
            notes="Diapositive à photographier. Faire chercher le mot de la "
                  "ligne « langue » : il n'y en a pas un seul, et c'est "
                  "justement ce qui rend cette ligne la moins claire.")

    d.tableau('Analyse', "Où mettre son temps",
              ['Ce qu\'on fait', 'Ce que ça rapporte'],
              [["lire et comparer", "8 points, et deux semaines de travail"],
               ["nommer ses sources", "4 points, quelques minutes par source"],
               ["relire sa langue", "4 points, une heure à trois"],
               ["découper et aérer", "4 points, vingt minutes le dernier soir"]],
              cle=1,
              note="Les quatre derniers points sont les moins chers du barème — et les plus souvent perdus.",
              notes="Diapositive à photographier. Ce n'est pas un conseil "
                    "pour travailler moins : c'est un conseil pour ne pas "
                    "remettre deux semaines de travail habillées en dix "
                    "minutes.")

    d.pratique('Pratique', "Trouvez le passage qui répond",
               "Pour chaque question, dites où se trouve la réponse dans la grille.", [
        ("Sur combien de points ?", "« Le travail est noté sur vingt points »"),
        ("Que demande la ligne contenu ?", "« rapporte ce que disent ses sources et distingue »"),
        ("Quelles conditions pour les sources ?", "« trois au moins, de genres différents, nommées »"),
        ("Qu'est-ce qui est évalué en langue ?", "« la construction de la phrase, les accords, la ponctuation »"),
        ("Comment gagner les points d'organisation ?", "« un paragraphe par idée, un blanc, des mots qui relient »"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t1grille` du module, du type `texte`. En "
             "classe, faire surligner les cinq passages sur la feuille de "
             "grille distribuée.")

    d.piege('Évaluation',
            "s'inquiéter de son accent avant de remettre",
            "relire ce que la grille évalue vraiment",
            "L'accent n'est évalué nulle part, ni dans cette grille ni dans "
            "aucun critère du programme. La vitesse non plus. Un exposé lent "
            "et clair vaut mieux qu'un exposé rapide, et la ligne « langue » "
            "ne parle que de phrases, d'accords et de ponctuation.",
            notes="À dire lentement et une seule fois. C'est souvent la "
                  "phrase la plus utile de tout le module.")

    d.billet(
        "Sur quelle ligne de la grille ton équipe va-t-elle perdre des points ?",
        exemples=[
            "Nomme la ligne, puis dis ce que vous allez faire pour l'éviter.",
            "Deux phrases.",
        ],
        notes="Trois minutes. Les réponses honnêtes sont presque toujours "
              "« organisation » : c'est le moment de rappeler que ces "
              "quatre points-là se gagnent en vingt minutes.")

    return d.save(dossier)
