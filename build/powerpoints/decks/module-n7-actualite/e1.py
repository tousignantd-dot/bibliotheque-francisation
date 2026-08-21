# -*- coding: utf-8 -*-
"""E1 · Discuter d'une nouvelle, et en faire le compte rendu
Bloc E « Je me lance » · couleur teal · 75 min.
Source : bloc `appli` — jeu de rôle `actualite` et production orale.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n7-actualite/images/')


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Discuter d'une nouvelle, et en faire le compte rendu",
        chapeau="Tout ce qui précède servait à ça : pouvoir raconter une "
                "nouvelle à quelqu'un, séparer ce qui est sûr de ce qui ne "
                "l'est pas, et donner son avis en disant que c'en est un.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Deux productions aujourd'hui : la discussion "
                  "avec l'assistant, qui sert de répétition, puis le compte rendu oral "
                  "enregistré. La seconde est évaluée, la première non.")

    d.objectifs([
        "résumer une nouvelle en deux ou trois phrases ;",
        "dire d'où vient l'information et si elle est confirmée ;",
        "réagir à un avis contraire sans le rejeter ;",
        "donner son opinion en la présentant comme une opinion.",
    ], notes="Le troisième objectif est le plus difficile à l'oral : sous la pression "
             "de l'échange, les élèves oublient de concéder. Le jeu de rôle est là pour "
             "l'entraîner sans risque.")

    d.declencheur(
        'Mise en situation', "Votre voisin n'a rien suivi, et il n'est pas d'accord",
        image=IMG + 'micro-trottoir.jpg',
        pistes=[
            "Par où commencez-vous : les faits, ou votre avis ?",
            "Que faites-vous s'il affirme quelque chose de faux ?",
            "Comment lui donnez-vous raison sur un point ?",
            "Quelle question aimeriez-vous qu'il retienne ?",
        ],
        notes="Faire répondre à l'oral avant de lancer le jeu de rôle. Les réponses "
              "montrent qui a compris que les faits viennent avant l'opinion.")

    d.tableau('Analyse', "Les trois temps du compte rendu",
              ['Le temps', 'Ce qu\'on y met'],
              [["1. De quoi il s'agit, et d'où je le sais",
                "« Il y a un reportage à la radio du quartier sur un point de dépôt, rue Boisjoli. »"],
               ["2. Ce qui est établi, puis ce qui ne l'est pas",
                "« Le comité a retenu le local. Par contre, les heures ne seraient pas fixées. »"],
               ["3. Mon opinion, annoncée comme une opinion",
                "« Bien que le projet soit une bonne chose, je trouve qu'il manque une réponse. »"]],
              cle=0,
              note="Quatre-vingt-dix secondes suffisent. Ce qui manque le plus souvent, c'est le temps 2.",
              notes="Diapositive à photographier. C'est la grille d'évaluation du "
                    "compte rendu oral : la donner avant, pas après.")

    d.cartes("Les trois situations du jeu de rôle", "Choisissez la vôtre", [
        ("Le point de dépôt",
         "Le comité recommande le local de la rue Boisjoli. Le conseil tranche le 14 octobre. Les heures ne sont pas fixées."),
        ("Les huit places",
         "Deux des huit places seraient réservées, quinze minutes. Le commerçant craint de perdre des clients."),
        ("La chronique de samedi",
         "Elle écrit que le projet a été « imposé ». Ses chiffres sont exacts ; le mot, lui, se discute."),
    ], notes="Chaque élève choisit sa situation et son rôle : le citoyen informé ou le "
             "voisin sceptique. Jouer le sceptique est plus difficile et plus formateur "
             "- le proposer aux plus avancés.")

    d.regle("Marquez ce qui n'est pas confirmé",
            "Un conditionnel, et votre interlocuteur sait à quoi s'en tenir.",
            precision="« Selon ce que j'ai entendu, le local serait loué pour cinq "
                      "ans. » En une phrase, vous avez donné l'information et signalé "
                      "que vous ne la garantissez pas. C'est ce qui distingue quelqu'un "
                      "qui informe de quelqu'un qui propage une rumeur, et ça ne coûte "
                      "que deux syllabes.",
            notes="Diapositive à photographier. C'est le savoir le plus exportable du "
                  "module : il servira dans toutes les conversations de la vie réelle.")

    d.cartes("Cinq phrases à réutiliser", "Prêtes à l'emploi", [
        ("Marquer le non confirmé",
         "Selon ce que j'ai entendu, le local serait loué pour cinq ans."),
        ("Rapporter une parole",
         "La conseillère a dit que la décision serait prise le 14 octobre."),
        ("Concéder avant d'objecter",
         "Bien que le projet soit utile, personne ne connaît les heures."),
        ("Mettre en avant",
         "Ce qui m'inquiète, c'est l'heure de fermeture."),
        ("Restreindre",
         "La Ville ne fournit que le local ; l'exploitation revient à quelqu'un d'autre."),
    ], notes="Ces cinq phrases sont affichées dans l'activité interactive, sous le jeu "
             "de rôle. Faire lire à voix haute avant de commencer.")

    d.piege("Donner son avis avant les faits",
            "Moi je trouve que c'est n'importe quoi, ils ont décidé sans nous.",
            "Le comité a recommandé le local ; le conseil tranche le 14 octobre. Moi, je trouve que...",
            "Celui qui commence par son opinion se fait classer en deux secondes, et "
            "plus personne n'écoute ses faits. Celui qui pose d'abord ce qui est établi "
            "peut ensuite dire ce qu'il veut : il a montré qu'il savait de quoi il "
            "parlait. L'ordre n'est pas de la politesse, c'est de l'efficacité.",
            notes="Piège le plus fréquent dans le jeu de rôle. Le nommer avant de "
                  "commencer, puis le rappeler à ceux qui y tombent.")

    d.pratique('Production orale', "Quatre-vingt-dix secondes, enregistrées",
               "Faites le compte rendu de la nouvelle à quelqu'un qui n'a rien suivi.", [
        ("Temps 1", "de quoi il s'agit, et d'où vous le savez"),
        ("Temps 2", "les faits établis, puis ce qui ne l'est pas"),
        ("Temps 3", "votre opinion, annoncée comme une opinion"),
        ("Au moins un conditionnel", "pour marquer ce qui n'est pas confirmé"),
        ("Au moins une parole rapportée", "« la conseillère a dit que... »"),
        ("Au moins une concession", "« bien que » ou « même si »"),
    ], corrige=False,
       notes="L'élève s'enregistre dans l'activité, s'écoute, recommence autant qu'il "
             "veut, puis envoie à l'enseignant. L'assistant donne une rétroaction "
             "immédiate ; cette rétroaction n'est pas conservée.")

    d.billet(
        "Quelle est la question que personne n'a posée ?",
        exemples=[
            "Une seule question, la vôtre.",
            "Elle sera la dernière ligne de votre billet, demain.",
        ],
        notes="Ce billet est le pont vers E2. Le ramasser et le rendre en début de "
              "séance suivante.")

    return d.save(dossier)
