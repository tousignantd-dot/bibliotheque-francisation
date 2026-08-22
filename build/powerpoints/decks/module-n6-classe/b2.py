# -*- coding: utf-8 -*-
"""B2 · Ce que dit la consigne, exactement
Bloc B « Défi 1 » · couleur teal · 75 min. Compréhension écrite d'un texte suivi.
Source du module : exercice `t1cons` (type `texte`) et la mini-leçon `t1cons`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='teal',
        titre="Ce que dit la consigne, exactement",
        chapeau="Une page et demie, sept obligations, et rien n'est dit deux "
                "fois. Une consigne ne se lit pas : elle se démonte, une "
                "ligne à la fois.",
        duree='75 minutes')

    d.titre(notes="C'est la séance qui porte l'unique intention de "
                  "communication que le programme rattache à cette situation "
                  "au niveau 6 : comprendre de l'information liée à un sujet "
                  "de recherche. Elle commence par la consigne.")

    d.objectifs([
        "lire une consigne une ligne à la fois, un crayon à la main ;",
        "relever les verbes qui ordonnent et en faire une liste ;",
        "retrouver dans le texte le passage qui répond à une question ;",
        "relire les trois endroits qu'on saute toujours.",
    ], notes="Le module fait cliquer l'élève dans le texte ; en classe, on "
             "fait souligner sur la feuille. Le geste est le même.")

    d.declencheur(
        'Pour commencer', "Où se cache l'information qu'on ne trouve jamais ?",
        pistes=[
            "Après un point-virgule ?",
            "Après le mot « et » ?",
            "Dans la dernière ligne de la page ?",
        ],
        notes="Les trois réponses sont bonnes, et ce sont les trois seules. "
              "Laisser chercher deux minutes avant de le dire.")

    d.tableau('Analyse', "La consigne, paragraphe par paragraphe",
              ['Le paragraphe', 'Ce qu\'il vous oblige à faire'],
              [["l'en-tête", "former une équipe de trois, le 30 octobre"],
               ["le deuxième", "faire approuver le sujet, puis chercher trois sources"],
               ["le troisième", "remettre un texte de deux pages ET le plan"],
               ["le dernier", "présenter cinq minutes, et remettre avant le 24"]],
              cle=0,
              note="Quatre paragraphes, sept obligations. Aucune n'est répétée ailleurs.",
              notes="Diapositive à photographier. Faire compter les "
                    "obligations à voix haute : le chiffre sept surprend "
                    "toujours.")

    d.regle("Chaque verbe qui ordonne se souligne",
            "choisira · cherchera · remettra · présentera · sera organisé — cinq verbes, et votre plan de travail est écrit.",
            precision="Cette liste-là, personne ne vous demande de "
                      "l'inventer : elle est déjà dans la consigne. Il suffit "
                      "de la recopier dans l'ordre sur une feuille à part.",
            notes="Diapositive à photographier. Faire faire l'exercice sur la "
                  "vraie feuille de consigne, crayon en main, avant de "
                  "continuer.")

    d.tableau('Analyse', "Les trois endroits qu'on saute",
              ['L\'endroit', 'Pourquoi il se perd'],
              [["après un point-virgule", "l'œil s'arrête au point et repart à la ligne"],
               ["après le mot « et »", "la deuxième moitié d'une longue phrase"],
               ["la dernière ligne", "on croit la page finie quand elle finit"]],
              cle=0,
              note="Relire ces trois endroits avant de ranger la feuille : deux minutes.",
              notes="Diapositive à photographier. C'est le conseil le plus "
                    "rentable de tout le module, et il ne demande aucune "
                    "connaissance de français.")

    d.pratique('Pratique', "Trouvez le passage qui répond",
               "Pour chaque question, dites où se trouve la réponse dans la consigne.", [
        ("Combien de personnes par équipe ?", "« Les équipes sont de trois personnes »"),
        ("Que faut-il faire avant le 3 novembre ?", "« Le sujet devra être approuvé par l'enseignante »"),
        ("Combien de sources, et de quel genre ?", "« au moins trois sources de genres différents »"),
        ("Qu'est-ce qu'il faut remettre ?", "« un texte de deux pages et le plan »"),
        ("Que se passe-t-il après le 24 novembre ?", "« Aucun travail ne sera reçu »"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t1cons` du module, du type `texte` : à "
             "l'écran, l'élève choisit une question puis clique le passage. "
             "En classe, il souligne sur sa feuille avec la même couleur.")

    d.cartes('Six questions', "À poser à n'importe quelle consigne", [
        ("Quoi ?", "Combien de documents, sous quelle forme, quelle longueur."),
        ("Avec qui ?", "Seul, à deux, à trois — et qui forme les équipes."),
        ("Pour quand ?", "La date, et ce qui arrive après cette date."),
        ("Dans quel ordre ?", "Ce qui doit être fini avant que le reste commence."),
        ("Évalué comment ?", "Le barème, ligne par ligne."),
        ("Et si ça bloque ?", "Ce que la consigne prévoit : il y a presque toujours une phrase."),
    ], cols=3,
       notes="Faire recopier ces six questions au dos de la feuille de "
             "consigne. Elles servent pour tous les cours, et pour bien des "
             "papiers en dehors de l'école.")

    d.piege('Lecture',
            "ranger la feuille une fois qu'on l'a lue",
            "la ressortir avant d'écrire, et avant de remettre",
            "Une consigne se lit trois fois : au début, avant d'écrire, et "
            "une dernière fois la feuille à la main juste avant de remettre. "
            "La troisième lecture prend quatre minutes et rattrape chaque "
            "session ce qui aurait coûté des points.",
            notes="Le dire maintenant, et le redire à la séance E2 : c'est "
                  "là que la troisième lecture doit avoir lieu.")

    d.billet(
        "Recopie la phrase de la consigne que tu avais mal comprise.",
        exemples=[
            "Puis écris, en dessous, ce qu'elle veut dire vraiment.",
            "Si tu n'en as aucune, écris celle qui te semble la plus facile à manquer.",
        ],
        notes="Trois minutes. Ces billets disent exactement où la classe "
              "achoppe, et ils orientent la révision de la séance E2.")

    return d.save(dossier)
