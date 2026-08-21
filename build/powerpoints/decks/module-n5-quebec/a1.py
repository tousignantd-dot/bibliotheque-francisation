# -*- coding: utf-8 -*-
"""A1 · « Tu n'es jamais sortie de l'île ? »
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-quebec/images/')


def img(nom):
    """Le chemin d'une illustration, ou None si elle n'a pas encore été
    produite. Les séances se construisent sans les images et les reprennent
    d'elles-mêmes à la reconstruction."""
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="« Tu n'es jamais sortie de l'île ? »",
        chapeau="Thuy Pham est arrivée du Viêt Nam il y a trois ans. Elle "
                "habite Villeray, elle est aide-cuisinière à Rosemont, et "
                "elle connaît quatre rues et deux stations de métro. Fin "
                "septembre, elle a une semaine de congé — et sa collègue "
                "Camille lui pose la question qui la prend de court.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir en demandant au groupe, à main "
                  "levée, qui est sorti de la région de Montréal depuis son arrivée au "
                  "Québec. La réponse surprend chaque fois, y compris les élèves "
                  "eux-mêmes. Ne pas juger et ne pas plaindre : le module ne dit pas "
                  "qu'il faut voyager, il donne les mots pour le faire si on le veut.")

    d.objectifs([
        "nommer quelques régions du Québec et dire ce qu'on y trouve ;",
        "comprendre une conversation où quelqu'un décrit sa région ;",
        "dire une distance et une durée de trajet avec des chiffres ;",
        "reconnaître les mots du paysage : le fleuve, un cap, une anse, un phare.",
    ], notes="Le troisième objectif est celui qu'on sous-estime. « C'est loin » ne veut "
             "rien dire ; « cinq cent trente kilomètres, sept heures d'autocar » veut "
             "dire quelque chose. Tout le module tient sur cette différence.")

    d.declencheur(
        'Observation', "Le fleuve, si large qu'on ne voit pas l'autre rive. "
                       "Où pensez-vous que c'est ?",
        image=img('phare-cap.jpg'),
        pistes=[
            "Est-ce que c'est la mer, ou est-ce que c'est le fleuve ?",
            "À quelle distance de Montréal, à votre avis ?",
            "Comment est-ce qu'on s'y rend, sans auto ?",
            "Qu'est-ce qu'on peut y faire pendant une semaine ?",
        ],
        notes="Presque tout le monde répond « la mer ». C'est le fleuve, à Rimouski, où "
              "il fait quarante kilomètres de large. Cette surprise-là est le meilleur "
              "point de départ du module : le Québec est beaucoup plus grand que la "
              "ville où l'on vit.")

    d.dialogue('Dialogue · 1 de 3', "Laval, ce n'est pas sortir de l'île", [
        ("CAMILLE", "Une semaine de congé à la fin septembre ! Tu t'en vas "
                    "où ?", True),
        ("THUY", "Nulle part. Je vais dormir, je pense. Ranger "
                 "l'appartement.", True),
        ("CAMILLE", "Thuy. Trois ans au Québec et tu n'es jamais sortie de "
                    "l'île ?", True),
        ("THUY", "Je suis allée à Laval une fois. Chez la cousine de mon "
                 "mari.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer le ton de Camille : elle taquine, elle ne reproche pas. "
             "C'est une conversation entre collègues qui s'aiment bien. Le tutoiement "
             "est normal ici, et il ne le sera plus au comptoir de la gare : la "
             "frontière se travaille dès maintenant.")

    d.dialogue('Dialogue · 2 de 3', "Cinq cent trente kilomètres", [
        ("CAMILLE", "Moi je viens de Rimouski.", True),
        ("THUY", "C'est loin, ça ?", True),
        ("CAMILLE", "Cinq cent trente kilomètres. Sept heures d'autocar, "
                    "huit avec les arrêts. C'est dans le Bas-Saint-Laurent, "
                    "sur la rive sud du fleuve.", True),
    ], notes="Voici la séance en une réplique. Camille ne dit pas « c'est loin » : elle "
             "donne un nombre de kilomètres, une durée, une région et un côté du fleuve. "
             "Faire relever les quatre informations au tableau.")

    d.dialogue('Dialogue · 3 de 3', "Des phoques. Au Québec.", [
        ("CAMILLE", "Un parc national. Des caps, des baies, des îles, des "
                    "sentiers dans la montagne. Les phoques se couchent sur "
                    "les roches à marée basse.", True),
        ("THUY", "Des phoques. Au Québec.", True),
        ("CAMILLE", "À trois cents mètres du stationnement. En septembre il "
                    "n'y a plus personne, l'air est frais, les couleurs "
                    "commencent.", False),
    ], notes="Laisser la surprise vivre. Beaucoup d'élèves ignorent qu'on voit des "
             "phoques depuis la rive au Québec. Demander ensuite ce que chacun croyait "
             "trouver dans son pays d'accueil et ne connaît toujours pas.")

    d.regle("Dire où c'est, et à quelle distance",
            "Une région, un côté du fleuve, un nombre de kilomètres, une "
            "durée de trajet.",
            precision="« C'est loin » ne renseigne personne. Quatre précisions "
                      "suffisent, et elles se disent en une seule phrase.",
            notes="Diapositive à photographier. Elle revient en B1, quand il faudra "
                  "exposer sa demande d'un seul tenant au comptoir.")

    d.cartes("Le paysage du fleuve", "Quatre mots à voir avant de les dire", [
        ("Le fleuve",
         "Le grand cours d'eau qui traverse le Québec et va à la mer."),
        ("Un cap",
         "Une pointe de roche qui avance dans l'eau."),
        ("Une anse",
         "Un petit creux de la côte, où l'eau est calme."),
        ("Un phare",
         "La tour dont la lumière tourne pour guider les bateaux."),
    ], notes="Faire répéter avec l'article. « Un cap » et « une anse » ne s'apprennent "
             "nulle part ailleurs et reviennent dans tout le bloc C, quand il faudra "
             "lire la fiche du parc.")

    d.tableau('Deux échelles', "Sortir de la ville, ou changer de pont",
              ['Aller à Laval', 'Aller à Rimouski'],
              [["Vingt minutes", "Sept à huit heures"],
               ["Quinze kilomètres", "Cinq cent trente kilomètres"],
               ["On traverse un pont", "On traverse quatre régions"],
               ["On revient le soir", "On reste une semaine"]],
              cle=1,
              notes="Faire compléter la colonne de droite avant de l'afficher. La blague "
                    "de Camille — « c'est changer de pont » — devient claire une fois le "
                    "tableau au tableau.")

    d.piege("Croire qu'il faut une auto pour sortir de la ville",
            "Je n'ai pas d'auto, donc je ne peux pas partir.",
            "L'autocar part tous les jours et me laisse au centre-ville.",
            "C'est la phrase exacte de Thuy, et c'est ce qui l'a retenue trois ans. "
            "L'autocar interurbain dessert la plupart des villes du Québec, et le "
            "gîte va souvent chercher les gens à la gare.",
            notes="Ce piège-là est le vrai obstacle du module, plus que la grammaire. "
                  "Demander qui a déjà pris un autocar interurbain au Québec : c'est "
                  "presque toujours une ou deux personnes, et elles racontent.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Thuy est au Québec depuis trois ans.", "vrai"),
        ("Thuy est déjà allée à Rimouski.", "faux — à Laval, une fois"),
        ("Camille est née à Rimouski.", "vrai"),
        ("Rimouski est sur la rive nord du fleuve.", "faux — sur la rive sud"),
        ("Le trajet dure environ huit heures avec les arrêts.", "vrai"),
        ("Il faut une auto pour se rendre au parc.", "faux — le gîte va la chercher"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la réplique exacte. La quatrième et la "
             "sixième sont celles que le groupe manque : on lit vite et on retient "
             "« nord » pour « sud ».")

    d.billet(
        "Écrivez le nom d'une région du Québec que vous aimeriez voir, et pourquoi.",
        exemples=[
            "Une seule région, et une seule raison.",
            "Si vous n'en connaissez aucune, écrivez la question que vous poseriez.",
        ],
        notes="Ramasser les billets : ils servent en A4, où chacun devra dire « je vais "
              "à… », « je vais en… », « je vais au… » avec sa propre région.")

    return d.save(dossier)
