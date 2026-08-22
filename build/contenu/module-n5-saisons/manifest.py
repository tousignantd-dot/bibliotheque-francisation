# -*- coding: utf-8 -*-
"""Identité de module-n5-saisons — « Quand la météo décide » (niveau 5).

La situation du programme est « Météo », domaine général de formation
« Culture et médias ». `build/cadre.py 5 "Météo"` rend un cadre très étroit :
**une seule intention de communication**, en compréhension orale — « Écouter
un bulletin météo à la radio ». Aucune production, aucune compréhension
écrite, et zéro entrée de lexique rattachée.

C'est donc le reste du cadre qui a décidé de la forme du module. Le savoir de
lexique « Écoute d'un bulletin météorologique » donne les trois champs à
couvrir : le vocabulaire des prévisions et de l'état des routes, les régions
et les villes du Québec, et la localisation temporelle et spatiale. Les
attentes de fin de cours du niveau 5 ajoutent ce que le module doit faire
produire : l'adulte « écrit un texte descriptif simple pour décrire ses
projets à court terme en employant de manière appropriée le futur simple ou le
futur proche », il « emploie de façon correcte les temps de l'indicatif et de
l'impératif selon la situation de communication » et il « utilise le gérondif
pour marquer la simultanéité ou la manière ». Trois défis en sortent : ce que
l'avertissement annonce, ce qu'on décide, ce qu'on demande d'apporter.

Le voisin, et ce qui l'en sépare :

· `module-meteo` (activité 34, niveau 4) écoute le bulletin et le comprend :
  quel temps il fait, combien de degrés, quoi mettre pour sortir. La météo y
  est une information. Ici, elle est une **contrainte** : quelqu'un attend une
  décision, et cette décision engage trente personnes. On ne demande plus
  « quel temps fera-t-il ? » mais « est-ce qu'on y va ? », et il faut savoir
  dire pourquoi. C'est la différence entre le stade débutant et le stade
  intermédiaire : un discours simple mais **organisé**, tenu d'un seul tenant
  devant quelqu'un qui n'a pas écouté la radio.
· `module-n2-neige` (niveau 2) partage la même situation deux stades plus bas
  et n'en garde que les trois mots du matin — il neige, il vente, il fait
  froid. Son scénario `meteo` de `server.py` ne convenait donc pas : le
  scénario `saisons` a été ajouté pour ce module.
· `module-n5-transport` (activité 69, même niveau) écoute un bulletin de
  circulation pour refaire son trajet du matin même. La décision y porte sur
  soi et sur l'heure qui vient ; ici elle porte sur un groupe et sur la
  semaine prochaine, ce qui oblige au futur simple plutôt qu'au présent.

Les faits du Québec sont vérifiés, jamais devinés : Environnement Canada émet
des **veilles** (les conditions sont favorables, le phénomène est possible) et
des **avertissements** (le phénomène est imminent ou en cours) — les deux mots
ne veulent pas dire la même chose et le module en fait un exercice entier.
Les intitulés employés sont ceux du service : avertissement de tempête
hivernale, avertissement de pluie verglaçante, avertissement de chaleur
extrême, bulletin météorologique spécial. Le refroidissement éolien, la
poudrerie, la crue printanière et l'indice UV sont les termes officiels. Le
parc national du Bic et la promenade de la mer existent à Rimouski et servent
de destinations. En revanche, les personnes, le Centre communautaire de la
Pointe, les dates, les températures annoncées et les sorties sont inventés :
un avertissement attribué à une vraie journée serait une fausse information.
"""

MANIFESTE = {
    'slug': 'module-n5-saisons',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.
    'theme': 'Météo',

    # Sarcelle : la couleur du niveau 5. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#0D7A6F',
    'accent_doux': '#DCF2EF',

    'ia_oral': "L'élève laisse un message au groupe qui doit partir en sortie : "
               "il annonce d'abord la décision — la sortie est maintenue, "
               "reportée ou annulée — puis il dit ce qu'annonce la météo au "
               "futur simple, il donne la raison de la décision avec un "
               "connecteur de cause, il emploie au moins une phrase "
               "impersonnelle, il dit à l'impératif ce qu'il faut apporter et "
               "il ajoute une manière au gérondif. Il vouvoie le groupe.",

    'jr_cas': 'verglas',
    'jr_role': 'rejean',
    'jr_scenario': 'saisons',
    'ia_jeu_de_role': "L'élève doit décider si une sortie de groupe a lieu, "
                      "malgré ce qu'annonce la météo : il dit ce qui est "
                      "annoncé et pour quand, il pose les questions qui lui "
                      "manquent, il annonce sa décision et il la justifie, "
                      "puis il dit ce que les gens devront apporter.",

    'bravo': "🎉 Bravo, vous avez terminé le module « Quand la météo décide » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
