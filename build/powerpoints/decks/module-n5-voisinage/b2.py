# -*- coding: utf-8 -*-
"""B2 · « Oui, non, ou jeudi »
Bloc B « Défi 1 · L'invitation » · couleur acier · 75 min.
Source : exercice `t1acc`, mini-leçon `t1acc`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='acier',
        titre="« Oui, non, ou jeudi »",
        chapeau="Devant une invitation, il n'existe que trois réponses "
                "utiles : oui, non, ou « laissez-moi jusqu'à jeudi ». La "
                "quatrième — « on verra » — n'est pas une réponse : elle "
                "transfère le travail à l'autre.",
        duree='75 minutes')

    d.titre(notes="Séance culturellement délicate et centrale. Beaucoup d'élèves viennent "
                  "de cultures où un refus direct est impoli et où « peut-être » est la "
                  "façon polie de dire non. Ne jamais présenter cela comme une erreur : "
                  "présenter la règle québécoise comme une convention locale, aussi "
                  "arbitraire que les autres, mais qu'il faut connaître.")

    d.objectifs([
        "accepter une invitation en trois temps ;",
        "refuser en quatre temps, sans fermer la porte ;",
        "demander un délai qui porte une date ;",
        "reconnaître les réponses qui n'en sont pas.",
    ], notes="Le quatrième objectif est le plus utile aux élèves qui reçoivent, un jour, "
             "un « je vais essayer » de la part d'un francophone : ils sauront que ça veut "
             "dire non.")

    d.regle("Accepter en trois temps",
            "Le oui, le plaisir ou le merci, puis ce que vous ferez.",
            precision="C'est oui, avec plaisir. Merci de m'avoir invitée : "
                      "j'apporterai un plat pour six personnes. Le troisième temps "
                      "est celui qu'on oublie, et c'est le plus utile : il dit à "
                      "l'organisateur ce qu'il peut inscrire sur sa liste.",
            notes="Faire répéter la formule complète à voix haute, en chœur, deux fois. "
                  "Elle doit devenir automatique : c'est une phrase qu'on dit debout, dans "
                  "un escalier, sans temps de préparation.")

    d.regle("Refuser en quatre temps",
            "Le merci, le refus net, la raison en une phrase, la porte "
            "laissée ouverte.",
            precision="Merci beaucoup de l'invitation. Malheureusement, je ne "
                      "pourrai pas venir : je travaille ce jour-là. On se reprend "
                      "cet été ? L'ordre compte : le merci vient avant le refus, "
                      "sinon le refus arrive comme une porte qui claque.",
            notes="C'est exactement ce que fait madame Faye dans le dialogue du défi 1, et "
                  "Réjean le remarque : « Elle a bien fait de me le dire tout de suite. » "
                  "Faire relire cette réplique.")

    d.cartes("Demander à réfléchir", "Un délai, ce n'est pas un flou", [
        ("Un vrai délai",
         "Est-ce que je peux vous répondre d'ici jeudi ?"),
        ("Un engagement de rappel",
         "Je vérifie mon horaire et je vous le dis demain sans faute."),
        ("Ce qui n'est pas un délai",
         "Je vais voir. Peut-être. Si j'ai le temps. On verra bien."),
        ("La règle",
         "Un délai porte une date. Sans date, ce n'est pas un délai."),
    ], notes="Insister sur la dernière carte, et ajouter la suite : il faut tenir le "
             "délai. Une réponse donnée jeudi comme promis vaut mieux qu'un oui donné "
             "tout de suite et repris le vendredi.")

    d.tableau('Trois colonnes', "Ce que fait vraiment chaque réponse",
              ['La phrase', 'Ce qu\'elle fait'],
              [["C'est oui, avec plaisir. J'apporte un dessert.", "Accepter"],
               ["Merci beaucoup, je travaille ce samedi-là.", "Refuser"],
               ["Je peux vous répondre d'ici jeudi ?", "Demander à réfléchir"],
               ["Je ne pourrai pas, mais on se reprend ?", "Refuser sans fermer"],
               ["Je vais essayer.", "Rien du tout"]],
              cle=1,
              notes="La dernière ligne est le cœur de la séance. Demander au groupe ce que "
                    "l'organisateur doit faire de cette réponse : il doit revenir "
                    "demander, et souvent il n'ose pas — donc il compte une chaise de "
                    "trop, ou une de moins.")

    d.pratique('Classement', "Accepter, refuser, ou demander à réfléchir ?",
               "Pour chaque réponse, dites ce qu'elle fait.", [
        ("C'est oui, avec plaisir. Je vais apporter un dessert.", "accepter"),
        ("Merci beaucoup, mais je travaille ce samedi-là.", "refuser"),
        ("Est-ce que je peux vous répondre d'ici jeudi ?", "demander à réfléchir"),
        ("Volontiers ! J'y serai vers midi et demi.", "accepter"),
        ("C'est gentil, malheureusement je suis prise cette fin de semaine.", "refuser"),
        ("Je vérifie mon horaire et je vous le dis demain sans faute.", "demander à réfléchir"),
        ("Je ne pourrai pas venir, mais on se reprend cet été ?", "refuser"),
    ], corrige=True,
       notes="Exercice t1acc de l'activité, à trois tuiles. Faire dire chaque phrase à "
             "voix haute avant de la classer : l'intonation travaillée en A2 se réinvestit "
             "ici, en particulier sur les questions.")

    d.piege("Répondre « peut-être » pour être poli",
            "Peut-être, on verra bien.",
            "Merci de l'invitation, mais je ne pourrai pas venir.",
            "Dans beaucoup de cultures, « peut-être » veut dire non et un refus direct "
            "est impoli. Ici, « peut-être » veut dire « peut-être » : on vous "
            "inscrira sur la liste et on vous attendra. Un non clair est reçu comme "
            "une politesse.",
            notes="Le point le plus important de la séance, et le plus délicat à dire. Ne "
                  "pas dire que l'usage québécois est meilleur : dire qu'il est différent, "
                  "et qu'un malentendu coûte une chaise vide et une déception.")

    d.piege("Refuser sans remercier",
            "Non, je peux pas, je travaille.",
            "Merci de l'invitation, mais je travaille ce jour-là.",
            "Ce n'est pas le non qui blesse, c'est le merci qui manque. Une seconde de "
            "plus, et la même phrase devient chaleureuse.",
            notes="Faire pratiquer en binôme : l'un invite, l'autre refuse, deux fois — "
                  "une fois sans le merci, une fois avec. Faire dire à celui qui invite "
                  "ce qu'il a ressenti.")

    d.billet(
        "Écrivez un refus complet en quatre temps, pour une invitation vraie.",
        exemples=[
            "Merci, refus, raison en une phrase, contre-proposition.",
            "Quatre lignes au maximum. La raison ne doit pas dépasser une phrase.",
        ],
        notes="Ramasser et lire deux ou trois refus à voix haute à la séance suivante, "
              "sans nommer les auteurs. Ils servent d'exemples pour B3.")

    return d.save(dossier)
