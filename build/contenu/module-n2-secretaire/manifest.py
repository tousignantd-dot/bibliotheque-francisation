# -*- coding: utf-8 -*-
"""Identité de module-n2-secretaire — « Je vais au secrétariat ».

Dixième et dernier module du niveau 2. La situation du programme est
« Communication avec le personnel de l'établissement de formation », domaine
« Éducation et monde du travail ». Elle porte **trois** intentions, et elles
décident de tout :

  · s'informer sur le fonctionnement de l'établissement — en compréhension
    orale **et** en production orale : c'est le comptoir du secrétariat, et
    c'est le Défi 1 ;
  · comprendre de l'information sur ce fonctionnement, à l'écrit — l'horaire
    d'ouverture affiché, la fiche du cours ;
  · **lire un avis simple** de l'établissement — le papier collé sur la porte
    un matin de congé. C'est le Défi 2, avec le fait de prévenir d'une
    absence.

Le lexique du programme est repris tel quel, sans rien y ajouter : le
secrétariat, le couloir, le premier étage, le rez-de-chaussée, le personnel de
l'établissement, l'horaire et le lieu du cours, les verbes *comprendre,
arriver, apprendre, écrire, fermer, inscrire, aller, partir, savoir, ouvrir,
demander*, les consignes (*lisez, ouvrez, fermez, écoutez, écrivez*) et les
quatre mots du règlement : *c'est permis, interdit, autorisé, possible*.

**Ce qui distingue ce module de ses voisins.** `module-n3-secretariat`
(niveau 3, activité 86) traite l'absence de Nawel : elle téléphone avant,
apporte un billet du médecin, puis annonce qu'elle doit arrêter — trois
démarches, avec des raisons, des justifications et du passé composé. Ici, on
ne justifie rien et on ne raconte rien : on se présente **au comptoir**, on
demande un papier en une phrase, on entend une réponse de trois mots, et on
lit un avis de quatre lignes sur une porte. `module-n2-inscription`
(activité 91) s'inscrit une fois, au début ; `module-n2-couloirs`
(activité 90) cherche son chemin sans parler à personne. Ce module-ci est
celui d'après : on connaît le centre, et on vient y demander quelque chose.
"""

MANIFESTE = {
    'slug': 'module-n2-secretaire',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': "Communication avec le personnel de l'établissement",

    # Couleur du niveau 2, posée par `build/couleurs_niveau.py`.
    'accent': '#A83A22',
    'accent_doux': '#FBEAE4',

    'ia_oral': "L'élève se présente au comptoir du secrétariat : il salue, il "
               "dit son nom, il demande un papier ou un renseignement en une "
               "seule phrase (« Je voudrais… », « Est-ce que… ? », « À quelle "
               "heure… ? »), il répète le jour et l'heure de la réponse pour "
               "vérifier, et il remercie avant de partir. Phrases très "
               "courtes, au présent, sans subordonnée. Le vouvoiement doit "
               "être tenu du début à la fin : le secrétariat est un bureau.",

    'jr_cas': 'papier',
    'jr_role': 'moi',
    'jr_scenario': 'secretaire',
    'ia_jeu_de_role': "L'élève parle à la secrétaire du centre : il salue et "
                      "dit son nom, il demande un papier ou un "
                      "renseignement, il demande où et à quelle heure, il "
                      "répète ce qu'il a entendu pour vérifier, il demande de "
                      "répéter quand ça va trop vite, et il remercie avant de "
                      "partir.",

    'bravo': "🎉 Bravo, tu as terminé le module « Je vais au secrétariat » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
