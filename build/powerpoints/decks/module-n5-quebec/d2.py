# -*- coding: utf-8 -*-
"""D2 · Ce que j'ai fait, et ce qu'il y avait autour
Bloc D « Défi 3 » · couleur ambre · 75 min. Écriture et grammaire.
Source : exercices `t3ger`, `t3pc`, `t3quest` et `t3rac`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Ce que j'ai fait, et ce qu'il y avait autour",
        chapeau="Raconter sa journée demande deux temps à la fois : le passé "
                "composé pour ce qu'on a fait, l'imparfait pour ce qu'il y "
                "avait pendant qu'on le faisait. « J'ai visité le phare "
                "pendant qu'il pleuvait. »",
        duree='75 minutes')

    d.titre(notes="Dernière séance avant « Je me lance ». Deux points de grammaire "
                  "y tiennent : le gérondif et le couple passé composé / imparfait. "
                  "Le second est le plus lourd ; lui réserver la moitié de la séance.")

    d.objectifs([
        "employer le gérondif pour dire comment ou en même temps ;",
        "raconter au passé composé ce qu'on a fait ;",
        "décrire à l'imparfait ce qu'il y avait autour ;",
        "poser à quelqu'un de la région les questions qui font parler.",
    ], notes="Le troisième objectif est celui qu'on n'ose pas : les élèves racontent "
             "au passé composé seulement, et le récit reste plat. L'imparfait est ce "
             "qui met du décor autour de l'action.")

    d.regle("Le gérondif : « en » plus la forme en -ant",
            "En marchant, comptez quarante minutes. En passant par le petit "
            "chemin, vous coupez dix minutes.",
            precision="Il dit comment on fait quelque chose, ou ce qu'on fait en "
                      "même temps. Le sujet est le même pour les deux verbes.",
            notes="Diapositive à photographier. La contrainte du sujet unique est ce "
                  "qui bloque : « en marchant, le chemin est plus court » est faux, "
                  "parce que le chemin ne marche pas.")

    d.tableau('Deux usages', "Le gérondif dit comment, ou quand",
              ['La phrase', 'Ce qu\'il dit'],
              [["En marchant, comptez quarante minutes", "Comment : à pied"],
               ["En passant par l'église, vous coupez", "Comment : par où"],
               ["Elle regardait dehors en voyageant", "Quand : en même temps"],
               ["On voit les phoques en arrivant tôt", "Condition : si on arrive tôt"]],
              cle=1,
              notes="La quatrième ligne montre un troisième usage, plus subtil : le "
                    "gérondif peut poser une condition. Ne pas l'enseigner, seulement "
                    "le signaler pour la compréhension.")

    d.regle("Deux temps pour un seul récit",
            "Passé composé : ce que j'ai fait, une action terminée. "
            "Imparfait : ce qu'il y avait autour, le décor.",
            precision="« J'ai visité le phare pendant qu'il pleuvait. » La visite "
                      "est finie ; la pluie était là tout le temps.",
            notes="Diapositive à photographier. L'image du décor et de l'action est la "
                  "plus efficace : l'imparfait plante le décor, le passé composé y fait "
                  "entrer quelqu'un.")

    d.tableau('Le récit de Thuy', "Ce qu'elle a fait, ce qu'il y avait",
              ["Passé composé", "Imparfait"],
              [["J'ai fait le sentier", "il faisait beau"],
               ["J'ai visité le phare", "il pleuvait"],
               ["Je suis montée au belvédère", "on voyait les îles"],
               ["J'ai pris l'autocar", "je regardais dehors"]],
              cle=1,
              notes="Toutes ces phrases sont dans les dialogues du module. Faire relier "
                    "chaque paire par « pendant que » ou par une virgule, et lire à voix "
                    "haute : le récit prend du relief immédiatement.")

    d.pratique('Choix du temps', "Passé composé ou imparfait ?",
               "À l'oral, puis à l'écrit.", [
        ("Hier, j'… (visiter) le phare.", "j'ai visité — une action terminée"),
        ("Il … (pleuvoir) toute la journée.", "il pleuvait — le décor"),
        ("Nous … (arriver) à trois heures.", "nous sommes arrivés — une action"),
        ("Le fleuve … (être) très large.", "était — une description"),
        ("Elle … (regarder) dehors pendant tout le trajet.", "regardait — une durée"),
        ("J'… (monter) au belvédère ce matin.", "je suis monté — une action terminée"),
    ], corrige=True,
       notes="Faire dire à chaque fois pourquoi, en un mot : « action » ou « décor ». "
             "C'est la question qui décide, et elle est plus fiable que les listes de "
             "mots déclencheurs.")

    d.piege("Raconter seulement au passé composé",
            "J'ai pris l'autocar. J'ai marché. J'ai vu des phoques.",
            "J'ai pris l'autocar : je regardais dehors, le fleuve était immense.",
            "Une suite d'actions sans décor ressemble à une liste de tâches. "
            "L'imparfait est ce qui fait qu'on écoute jusqu'au bout — et le "
            "niveau 5 demande un récit, pas un relevé.",
            notes="Faire lire les deux versions à voix haute par deux élèves. La "
                  "différence s'entend sans qu'on l'explique, et c'est le meilleur "
                  "argument de la séance.")

    d.cartes("Questions qui font parler", "À poser à quelqu'un de la région", [
        ("Qu'est-ce qu'il faut voir ici ?",
         "Ouverte : on ne peut pas répondre par oui ou non."),
        ("Vous venez ici depuis longtemps ?",
         "Elle invite à raconter, pas seulement à dater."),
        ("Qu'est-ce que vous préférez, vous ?",
         "Le « vous » final rend la question personnelle."),
        ("C'est comment en hiver ?",
         "Elle porte sur ce qu'on ne verra pas soi-même."),
    ], notes="La quatrième est la meilleure : elle demande une chose que le vacancier "
             "ne peut pas voir, ce qui force un vrai récit. Faire trouver au groupe "
             "deux autres questions du même genre.")

    d.pratique('Production', "Racontez votre journée d'hier, en quatre phrases",
               "Deux au passé composé, deux à l'imparfait. À l'oral, par deux.", [
        ("Avez-vous dit ce que vous avez fait ?", "passé composé"),
        ("Avez-vous dit le temps qu'il faisait ?", "imparfait"),
        ("Avez-vous dit ce que vous voyiez ?", "imparfait"),
        ("Avez-vous posé une question à votre voisin ?", "une question ouverte"),
        ("Avez-vous vouvoyé ?", "on joue des inconnus"),
    ], corrige=True,
       notes="Faire changer de partenaire une fois. Raconter deux fois la même journée "
             "à deux personnes différentes est le meilleur entraînement qui soit, et la "
             "seconde version est toujours meilleure.")

    d.billet(
        "En quatre phrases : ce que vous avez fait en fin de semaine, et ce qu'il y avait autour.",
        exemples=[
            "Deux phrases au passé composé, deux à l'imparfait.",
            "Soulignez les verbes avant de remettre.",
        ],
        notes="Ramasser les billets : c'est le brouillon du récit demandé en E1 et du "
              "courriel de E2. Souligner les verbes est ce qui rend la correction "
              "rapide et lisible pour l'élève.")

    return d.save(dossier)
