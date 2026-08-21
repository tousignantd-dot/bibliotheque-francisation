# -*- coding: utf-8 -*-
"""E2 · « Des nouvelles de la ruelle »
Bloc E « Je me lance » · couleur framboise · 75 min. Dernière séance.
Source : production écrite (courriel de nouvelles), banc de vocabulaire,
autoévaluation.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="« Des nouvelles de la ruelle »",
        chapeau="Dernière séance. Un courriel de six à neuf phrases à une "
                "personne du cours : ce qui est arrivé, comment c'était, une "
                "félicitation, ce que vous ferez cet été, et une question "
                "ouverte pour qu'elle réponde.",
        duree='75 minutes')

    d.titre(notes="Séance de clôture. Prévoir trois temps : l'écriture du courriel, la "
                  "révision du vocabulaire par les cartes mémoire, puis "
                  "l'autoévaluation. Ne pas sacrifier le troisième : c'est lui qui dit à "
                  "l'élève ce qu'il a gagné en quatre semaines.")

    d.objectifs([
        "écrire un bref courriel qui donne des nouvelles ;",
        "raconter au passé composé et à l'imparfait dans le même texte ;",
        "féliciter quelqu'un par écrit, avec l'accord de « quel » ;",
        "faire le bilan de ce qu'on est maintenant capable de faire.",
    ], notes="Le troisième objectif est le seul endroit du module où l'accord de « quel » "
             "se voit vraiment. Le rappeler avant l'écriture, pas après.")

    d.regle("Cinq mouvements dans un courriel de nouvelles",
            "L'objet · la salutation · les nouvelles au passé · ce qui vient "
            "ensuite au futur · la question ouverte et la signature.",
            precision="Un objet vide fait passer le courriel pour une publicité. Et "
                      "c'est la question finale qui décide s'il y aura une réponse : "
                      "sans elle, votre courriel se lit comme une carte postale.",
            notes="Diapositive à photographier, et à laisser affichée pendant l'écriture. "
                  "Les cinq mouvements sont les six exigences cochables de la carte de "
                  "production écrite.")

    d.tableau('Le plan', "Ce que chaque phrase doit faire",
              ['La phrase', 'Son rôle'],
              [["Objet : Des nouvelles de la ruelle", "Annoncer, pas raconter"],
               ["Bonjour Amina,", "Une ligne, pas trois"],
               ["Samedi, je suis allée à la fête.", "Un événement, au passé composé"],
               ["Il y avait vingt-deux personnes.", "Le décor, à l'imparfait"],
               ["Quelle belle nouvelle pour toi !", "La félicitation, accordée"],
               ["Et toi, comment va ton emploi ?", "La question qui appelle une réponse"]],
              cle=1,
              notes="Faire écrire le courriel en suivant le tableau ligne par ligne, la "
                    "première fois. Les élèves rapides peuvent ensuite en écrire un second "
                    "sans le tableau.")

    d.cartes("Trois détails qui changent tout", "Ce qui distingue un courriel qui reçoit une réponse", [
        ("Un décor, pas une appréciation",
         "« Il y avait vingt-deux personnes » vaut mieux que « c'était le fun »."),
        ("Une félicitation seule",
         "Elle vit une phrase entière avant qu'on passe à autre chose."),
        ("Une question ouverte",
         "« Comment se passe ton emploi ? », pas « ça va bien ? »."),
        ("Une signature",
         "Votre prénom, et le lien : ta voisine de cours, du mardi."),
    ], notes="La première carte est la plus transférable : elle vaut pour tous les récits, "
             "à l'oral comme à l'écrit. Un détail concret fait voir la scène ; un "
             "adjectif ne fait rien voir.")

    d.pratique('Vérification', "Avant d'envoyer votre courriel",
               "Six choses à vérifier, dans l'ordre.", [
        ("L'objet dit-il de quoi il s'agit ?", "sinon, on ne l'ouvre pas"),
        ("Y a-t-il deux phrases au passé composé ?", "les événements"),
        ("Y a-t-il une phrase à l'imparfait ?", "le décor : qui, combien, comment c'était"),
        ("La félicitation est-elle accordée ?", "quel, quelle, quels, quelles"),
        ("Y a-t-il une phrase au futur simple ?", "ce que vous ferez cet été"),
        ("Le courriel finit-il par une question ?", "c'est elle qui appelle la réponse"),
    ], corrige=True,
       notes="Les six points sont exactement ceux de la carte de production écrite de "
             "l'activité. Faire cocher avant de demander la correction assistée : l'élève "
             "corrige d'abord lui-même.")

    d.vocabulaire('Bilan · 1 de 2', "Les mots à emporter", [
        ("une ruelle verte", "Le passage derrière les immeubles, planté et entretenu par les voisins."),
        ("un empêchement", "Ce qui vous oblige à dire non alors que vous auriez voulu dire oui."),
        ("un répondeur", "Le service qui enregistre les appels quand personne ne décroche."),
        ("un mot", "Le petit papier écrit à la main qu'on laisse pour informer quelqu'un."),
    ], notes="Quatre des seize mots, choisis parce qu'ils reviendront dans la vie de "
             "l'élève dès la semaine prochaine. Renvoyer aux cartes mémoire pour les "
             "douze autres.")

    d.vocabulaire('Bilan · 2 de 2', "Les phrases à emporter", [
        ("Merci de l'invitation, mais...", "Le refus commence toujours par le merci."),
        ("Est-ce que je peux vous répondre d'ici jeudi ?", "Un délai porte une date."),
        ("Quelle bonne nouvelle ! Félicitations !", "La réaction vient avant la question."),
        ("C'est Marisol Vergara, votre voisine du deuxième.", "La première phrase d'un message."),
    ], notes="Ces quatre phrases sont l'essentiel du module en quatre lignes. Les faire "
             "recopier dans le cahier : ce sont celles qui serviront dès le lendemain.")

    d.piege("Terminer un courriel sans question",
            "Voilà les nouvelles. À bientôt !",
            "Et toi, comment se passe ton nouvel emploi ?",
            "Sans question, votre courriel se lit comme une carte postale : agréable, "
            "et sans suite. La question ouverte est ce qui transforme un message en "
            "conversation.",
            notes="Dernier piège du module, et le plus facile à corriger. Faire ajouter "
                  "une question à tous les courriels qui n'en ont pas avant de les "
                  "envoyer.")

    d.billet(
        "Nommez une chose que vous ferez cette semaine grâce à ce module.",
        exemples=[
            "Une chose concrète : un bonjour, un message, un mot laissé sur une table.",
            "Écrivez à qui, et quel jour.",
        ],
        notes="Fin du module. Ramasser les billets et y revenir la semaine suivante : "
              "demander qui l'a fait. C'est la seule évaluation qui compte vraiment pour "
              "un module de relations sociales.")

    return d.save(dossier)
