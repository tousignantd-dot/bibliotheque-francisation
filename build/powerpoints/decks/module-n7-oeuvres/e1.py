# -*- coding: utf-8 -*-
"""E1 · Présentez une œuvre à la classe
Bloc E « Je me lance » · couleur teal · production orale · 75 min.
Source : section `appli` (jeu de rôle et production orale).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Présentez une œuvre à la classe",
        chapeau="Deux minutes debout : ce que l'œuvre raconte, ce que vous en "
                "pensez, le moment qui l'appuie, et le point que vous accordez "
                "à ceux qui pensent autrement.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Rendre les billets de A1 à D2 : chaque "
                  "élève a déjà écrit les quatre morceaux, il ne reste qu'à les "
                  "mettre bout à bout et à les dire.")

    d.objectifs([
        "présenter une œuvre en une minute trente, sans lire ses notes ;",
        "résumer sans dévoiler la fin ;",
        "appuyer son avis sur un moment précis ;",
        "répondre à une objection en accordant d'abord un point.",
    ], notes="Le quatrième objectif se joue après l'exposé : prévoir une question du "
             "groupe à chaque présentateur, et exiger une concession dans la réponse.")

    d.declencheur(
        'Préparation', "Qu'est-ce qui rend un exposé écoutable ?",
        pistes=[
            "Sa longueur ? Son sujet ? Le fait qu'on sente une personne derrière ?",
            "Combien de temps dure votre attention pour quelqu'un qui lit ses notes ?",
            "Qu'est-ce qui vous fait relever la tête, quand quelqu'un parle ?",
            "Est-ce qu'on peut parler d'une œuvre que l'auditoire ne connaît pas ?",
        ],
        notes="La dernière piste amène le résumé : oui, à condition de le donner en "
              "premier. C'est exactement ce que Marilou a fait en D1.")

    d.tableau('Analyse', "Le plan, en quatre temps",
              ['Le temps', 'Ce qu\'on y dit'],
              [["Temps 1", "de quoi il s'agit, en deux ou trois phrases, sans la fin"],
               ["Temps 2", "ce que vous en pensez, annoncé comme un avis"],
               ["Temps 3", "le moment précis qui l'appuie, raconté en une phrase"],
               ["Temps 4", "ce que vous accordez, et ce que vous maintenez"]],
              cle=0,
              note="Une minute trente. Au-delà, l'auditoire décroche avant le temps 4.",
              notes="Diapositive à photographier, et à laisser affichée pendant les "
                    "présentations : elle sert de grille aux auditeurs autant qu'aux "
                    "présentateurs.")

    d.cartes('Analyse', "Ce qu'on dit à chaque temps", [
        ("Temps 1", "J'ai vu un film qui s'appelle... Ça se passe..."),
        ("Temps 2", "J'ai trouvé que... Ce qui m'a convaincu, c'est..."),
        ("Temps 3", "À la quatrième nuit, il... En dix secondes, on comprend..."),
        ("Temps 4", "Bien que le début soit lent, le film tient."),
    ], cols=1,
       notes="Les amorces sont à afficher. Elles évitent le blanc du début, qui est "
             "ce qui fait renoncer les élèves les plus hésitants.")

    d.regle("On ne lit pas un exposé, on le dit",
            "Quatre amorces sur un papier suffisent. Le reste se raconte.",
            precision="Un texte lu à voix haute perd son auditoire en trente "
                      "secondes, parce que la voix cesse de s'adresser à quelqu'un. "
                      "Quatre débuts de phrase notés au crayon donnent la sécurité "
                      "sans le récitatif.",
            notes="Diapositive à photographier. Faire préparer le papier en classe : "
                  "quatre lignes, pas davantage, et le vérifier avant de commencer.")

    d.piege('Oral',
            "« C'est un très bon film, il faut vraiment le voir. »",
            "« J'ai trouvé la deuxième heure très forte : à la quatrième nuit... »",
            "La première phrase est un goût déguisé en conseil : elle ne dit "
            "rien de l'œuvre et rien de vous. La seconde donne un jugement, "
            "puis la scène qui le justifie. C'est la différence entre une "
            "recommandation et un commentaire.",
            notes="Reprend la règle de A4, une dernière fois. C'est la faute qui "
                  "revient le plus dans les exposés, même après quinze séances.")

    d.pratique('Jeu de rôle', "Deux minutes avec quelqu'un qui n'est pas d'accord",
               "En dyades, puis avec l'assistant du module.", [
        ("Le spectacle d'humour", "l'autre a pris l'ironie au premier degré"),
        ("Le tour de chant", "l'autre trouve qu'elle chante faux à la fin"),
        ("Le long métrage", "l'autre dit qu'on peut regarder un film chez soi"),
        ("Dans les trois cas", "accordez un point vrai avant de répondre"),
    ], corrige=False,
       notes="Le module porte le même jeu de rôle avec l'assistant, qui ne cède que "
             "devant un moment précis. Faire d'abord la version humaine : elle est "
             "plus rapide et plus drôle.")

    d.pratique('Production orale', "Votre présentation",
               "Une minute trente, debout, quatre amorces sur un papier.", [
        ("Avant de commencer", "vérifiez que votre résumé ne donne pas la fin"),
        ("Pendant", "regardez la salle, pas votre papier"),
        ("À la fin", "attendez une question, et accordez un point avant d'y répondre"),
        ("Après", "notez ce que vous changeriez, en une phrase"),
    ], corrige=False,
       notes="Le module permet de s'enregistrer, d'obtenir une rétroaction et de "
             "déposer l'enregistrement. En classe, faire passer six ou sept élèves ; "
             "les autres déposent depuis la maison.")

    d.billet(
        "Quelle présentation vous a donné envie de voir une œuvre, et pourquoi ?",
        exemples=[
            "Nommez la personne et l'œuvre.",
            "Dites quel moment de sa présentation a fonctionné.",
        ],
        notes="Billet qui fait travailler l'écoute et qui vaut mieux qu'une note : "
              "les présentateurs apprennent ce qui a porté, et personne n'est jugé "
              "sur sa langue.")

    return d.save(dossier)
