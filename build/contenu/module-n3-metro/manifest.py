# -*- coding: utf-8 -*-
"""Identité de module-n3-metro — « Le bon titre de transport » (niveau 3).

La situation du programme est « Déplacement dans une ville ». Au niveau 3, elle
est **beaucoup plus étroite** qu'au niveau 4, et c'est `build/cadre.py 3` qui
le dit : trois intentions, et une seule idée dans les trois — « demander et
comprendre de l'information pour acheter un titre de transport » en
compréhension orale, la même en production orale, et « lire l'information pour
acheter un titre de transport » en compréhension écrite. Le module ne parle
donc **pas du trajet** : il parle du guichet, du prix, de la carte et de la
grille des tarifs. Les trois défis sont les trois intentions, dans cet ordre.

Ce module a trois voisins dans le dépôt, et il ne recoupe aucun des trois :

- `module-deplacement` (niveau 4) fait le trajet complet — demander son chemin,
  expliquer un itinéraire, comprendre les annonces du métro et lire un horaire.
  Il ne s'arrête jamais à un guichet et ne nomme aucun prix. Ici, il n'y a ni
  itinéraire, ni direction, ni terminus : il y a un comptoir, une carte, une
  grille de tarifs et de l'argent.
- `module-n2-autobus` (niveau 2) demande son chemin dans la rue et lit l'heure
  du prochain passage. Aucune carte OPUS, aucun titre, aucun tarif.
- `module-n2-couloirs` (niveau 2) se repère à des numéros à l'intérieur d'un
  bâtiment. Rien du transport collectif.

Le lexique que le programme rattache à cette situation est court et il a servi
tel quel : les titres de transport (tarif mensuel, tarif réduit), les
catégories d'âge, le transport adapté (place pour personnes à mobilité
réduite, femmes enceintes, personnes âgées), le parcours, et les verbes
« se renseigner », « se déplacer », « repérer », « se perdre ».

Les faits québécois sont vérifiés, pas inventés. Ils viennent de la grille
tarifaire de l'ARTM en vigueur le 1er juillet 2026 et des pages de la STM :
quatre zones tarifaires (A — agglomération de Montréal ; B — Laval et
l'agglomération de Longueuil ; C — couronnes nord et sud ; D — hors
territoire) ; en zone A, un passage Tous modes A coûte 3,75 $, dix passages
35,00 $, l'hebdo 33,25 $ du lundi au dimanche et le mensuel 110,00 $ ; le
titre 24 h coûte 11,25 $, la Soirée illimitée 6,75 $ de 18 h à 5 h, et le
Week-end illimité 17,00 $ du vendredi 16 h au lundi 5 h ; les quatre
catégories tarifaires sont Ordinaire, Réduit 6-17 ans, Réduit étudiant
18 ans et plus, Réduit 65 ans et plus, et le tarif réduit exige une carte
OPUS **avec photo** ; les enfants de 11 ans et moins voyagent gratuitement
s'ils sont accompagnés d'une personne de 14 ans et plus, qui ne peut pas en
accompagner plus de cinq ; la correspondance est de 120 minutes à partir de
la validation, enregistrée automatiquement sur la carte, et elle ne permet
pas de refaire le même parcours en sens inverse.
"""

MANIFESTE = {
    'slug': 'module-n3-metro',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Déplacement dans une ville',

    # Ambre : la couleur du niveau 3. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#B45309',
    'accent_doux': '#FBEEDC',

    'ia_oral': "L'élève parle au point de service du transport collectif : il "
               "salue, il dit ce dont il a besoin, il dit combien de fois par "
               "semaine il se déplace, il demande le prix d'un titre et s'il "
               "a droit au tarif réduit, puis il répète le prix pour "
               "vérifier.",

    'jr_cas': 'mensuel',
    'jr_role': 'client',
    'jr_scenario': 'titre',
    'ia_jeu_de_role': "L'élève est au comptoir d'un point de service du "
                      "transport collectif : il achète un titre de transport, "
                      "il demande le prix, il se renseigne sur le tarif "
                      "réduit et sur la carte OPUS, et il vérifie ce qu'il a "
                      "compris avant de payer.",

    'bravo': "🎉 Bravo, tu as terminé le module « Le bon titre de transport » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
