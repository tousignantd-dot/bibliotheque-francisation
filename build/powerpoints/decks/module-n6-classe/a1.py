# -*- coding: utf-8 -*-
"""A1 · Un travail de recherche, et les mots qui vont avec
Bloc A « Je découvre » · couleur framboise · 75 min. Vocabulaire.
Source du module : `FC_CARDS` (prep) et l'exercice `prVocab`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='framboise',
        titre="Un travail de recherche, et les mots qui vont avec",
        chapeau="Trois semaines, une équipe de trois, un texte et cinq "
                "minutes devant la classe. Avant de commencer, il faut "
                "savoir de quoi on parle.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ne pas annoncer le travail de "
                  "recherche comme un examen : c'est une tâche qui s'apprend, "
                  "et la moitié de la classe n'en a jamais fait.")

    d.objectifs([
        "nommer les cinq mots du travail de recherche ;",
        "distinguer un sujet de recherche d'un simple thème ;",
        "dire ce qu'on attend d'un compte rendu et d'un exposé ;",
        "comprendre ce qu'une échéance engage.",
    ], notes="Le programme ne rattache qu'un seul point de lexique à cette "
             "situation : « vocabulaire lié aux sujets de recherche ». Les "
             "seize mots du module en sortent tous.")

    d.declencheur(
        'Pour commencer', "Qu'est-ce que vous savez déjà sur le compostage ?",
        pistes=[
            "Qui a un bac brun à la maison ?",
            "Qu'est-ce qui a le droit d'aller dedans, selon vous ?",
            "Comment feriez-vous pour en être sûr ?",
        ],
        notes="La troisième question est la seule qui compte : elle amène "
              "l'idée de source. Laisser venir « je demanderais à quelqu'un » "
              "avant de parler de documents.")

    d.vocabulaire('Vocabulaire', 'Les cinq mots du travail', [
        ("un travail de recherche", "On cherche soi-même l'information, puis on rend compte de ce qu'on a trouvé."),
        ("un sujet de recherche", "La question précise sur laquelle l'équipe va chercher."),
        ("un compte rendu", "Ce qu'on rapporte : ce qui a été trouvé, dit ou décidé."),
        ("un exposé", "Une présentation orale devant un groupe, préparée et organisée."),
        ("une échéance", "La date avant laquelle il faut remettre, et après laquelle on ne reçoit plus."),
    ], notes="Faire répéter chaque mot avec son article. Insister sur « compte "
             "rendu », que beaucoup confondent avec « résumé ».")

    d.regle("Un sujet de recherche est une question, pas un thème",
            "« Le bac brun » n'est pas un sujet. « Qu'est-ce qui a le droit d'aller dans le bac brun, et pourquoi ? » en est un.",
            precision="Un thème ne dit pas quand on a fini de chercher ; une "
                      "question, oui. C'est la seule différence, et c'est "
                      "celle qui décide de la longueur du travail.",
            notes="Diapositive à photographier. Faire transformer trois thèmes "
                  "en questions, à l'oral, avant de passer à la suite.")

    d.tableau('Analyse', "Ce que chaque mot engage",
              ['Le mot', 'Ce qu\'il vous oblige à faire'],
              [["un sujet", "poser une question, et savoir quand on y a répondu"],
               ["une source", "noter le titre, l'auteur et la date"],
               ["un compte rendu", "dire d'où vient chaque chose que vous rapportez"],
               ["un exposé", "parler sans lire, donc répéter avant"],
               ["une échéance", "remettre ce jour-là, quoi qu'il arrive"]],
              cle=0,
              note="Cinq mots, cinq obligations. Aucune ne se rattrape la veille.",
              notes="Diapositive à photographier. Demander laquelle des cinq "
                    "obligations leur semble la plus difficile : la réponse "
                    "dit beaucoup sur l'expérience scolaire de chacun.")

    d.cartes('Attention', "Compte rendu ou résumé ?", [
        ("Un résumé", "raccourcit un texte qui existe déjà. On n'y met rien de soi."),
        ("Un compte rendu", "rapporte un travail : ce qu'on a cherché, trouvé, et ce qu'on en conclut."),
        ("Ce qui se passe", "Une équipe qui fait un résumé au lieu d'un compte rendu perd les points de contenu."),
        ("Le test", "Est-ce que votre texte pourrait être écrit par quelqu'un qui n'a rien cherché ?"),
    ], cols=2,
       notes="La confusion est très fréquente et elle coûte cher. Le test de "
             "la dernière carte est le plus rapide à appliquer.")

    d.pratique('Pratique', "Le mot et sa définition",
               "Reliez chaque mot à ce qu'il veut dire.", [
        ("un travail de recherche", "on cherche soi-même, puis on rend compte"),
        ("un sujet de recherche", "la question précise à laquelle on répond"),
        ("un compte rendu", "ce qu'on rapporte d'un travail"),
        ("un exposé", "une présentation orale préparée"),
        ("une échéance", "la date après laquelle on ne reçoit plus"),
    ], corrige=True, cols=1,
       notes="Faire à l'oral d'abord, puis à l'écrit. C'est l'exercice "
             "`prVocab` du module, dans sa version projetée.")

    d.billet(
        "Écris ton sujet de recherche sous la forme d'une question.",
        exemples=[
            "Commence par « Qu'est-ce que… », « Pourquoi… » ou « Comment… ».",
            "Une seule phrase, avec un point d'interrogation à la fin.",
        ],
        notes="Trois minutes. Ramasser et lire rapidement : ceux qui écrivent "
              "encore un thème plutôt qu'une question se repèrent d'un coup "
              "d'œil, et on les reprend individuellement en A4.")

    return d.save(dossier)
