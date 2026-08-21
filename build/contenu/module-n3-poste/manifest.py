# -*- coding: utf-8 -*-
"""Identité de module-n3-poste — « Le colis de Yassine » (niveau 3).

La situation du programme est « Démarches à la poste ». C'est
`build/cadre.py 3 "Démarches à la poste"` qui a décidé de la forme du module,
et son verdict est le plus étroit de tout le niveau : **une seule intention de
communication**, inscrite deux fois — « s'informer pour obtenir un produit ou
un service », en compréhension orale et en production orale. Ni compréhension
écrite, ni production écrite. Le module est donc entièrement une affaire de
comptoir parlé : on demande, on écoute la réponse, on redemande. Les trois
défis sont les trois moments de cette même intention — se renseigner avant de
choisir, choisir et payer, obtenir un service — et rien n'a été inventé autour.

Le lexique que le programme rattache à cette situation est court mais très
concret, et il a servi tel quel : « préposé », « envoi : colis, mandat-poste,
courrier recommandé », les verbes **timbrer** et **affranchir**, et trois
tournures qui sont à elles seules la matière du Défi 2 — « Donnez-moi… »,
« Je vais le prendre », « Je vais en prendre trois ». Les verbes rattachés
(vouloir, contenir, mettre, ajouter, il y a, aider, écrire, retourner) portent
les mini-leçons.

**Aucun module voisin.** La situation « Démarches à la poste » n'existe qu'aux
niveaux 2 et 3 du programme : le niveau 4 ne la traite pas, et aucun module du
dépôt ne l'avait abordée. Ce qui sépare ce module des six autres comptoirs du
niveau 3 — épicerie, vêtements, appareils, restaurant, pharmacie, métro — tient
en une phrase : partout ailleurs on repart avec ce qu'on a acheté, tandis qu'ici
l'objet part sans vous, et tout ce qui se dit au comptoir porte sur un moment
qu'on ne verra pas — un délai, un prix pour un service rendu ailleurs, une
signature à l'autre bout du pays.

Les faits de Postes Canada sont vérifiés, pas devinés : le timbre du régime
intérieur coûte 1,24 $ en carnet, en rouleau ou en feuillet et 1,44 $ à
l'unité ; le Courrier recommandé coûte 13,15 $ en sus de l'affranchissement et
comprend la signature du destinataire, un numéro de repérage et une couverture
de 100 $ ; le mandat-poste coûte 8,50 $, plafonne à 999,99 $ et se paie
comptant ou par carte de débit seulement ; un colis avisé est gardé 15 jours
civils au bureau de poste, un avis final part après 5 jours, puis le colis
retourne à l'expéditeur ; le réacheminement du courrier dure au maximum
12 mois et ne couvre ni les colis ni les enveloppes prépayées. Les personnes,
le quartier, les adresses et les heures sont inventés.
"""

MANIFESTE = {
    'slug': 'module-n3-poste',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Démarches à la poste',

    # Ambre : la couleur du niveau 3. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#B45309',
    'accent_doux': '#FBEEDC',

    'ia_oral': "L'élève parle à la préposée du bureau de poste : il salue, il "
               "dit en une phrase ce qu'il vient faire, il demande le prix et "
               "le délai avant de choisir, il dit ce qu'il y a dans son colis, "
               "puis il annonce son choix et répète le prix à voix haute.",

    'jr_cas': 'colis',
    'jr_role': 'client',
    'jr_scenario': 'poste',
    'ia_jeu_de_role': "L'élève est au comptoir d'un bureau de poste : il se "
                      "renseigne avant de choisir son envoi, il dit ce que "
                      "contient son colis, ou il vient chercher un colis avec "
                      "son avis de livraison, ou il demande à faire suivre son "
                      "courrier.",

    'bravo': "🎉 Bravo, tu as terminé le module « Le colis de Yassine » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
