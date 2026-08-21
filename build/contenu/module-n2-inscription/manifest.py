# -*- coding: utf-8 -*-
"""Identité de module-n2-inscription — « Je m'inscris au cours de français ».

Septième module court du dépôt, sixième du niveau 2 : huit séances, deux
défis. La situation du programme est « Inscription ». Elle n'a que **deux**
intentions, et elles décident du module à elles seules : repérer des
renseignements sur un cours dans une petite annonce et les prendre en note
(compréhension écrite, puis production écrite), et remplir un formulaire
d'inscription (production écrite). Défi 1 est l'annonce, Défi 2 est le
formulaire. Rien n'a été inventé autour.

Distinct de `module-n2-couloirs` (90) et de `module-n2-classe` (89), qui se
passent dans le même établissement : là, l'élève cherche une porte ou écoute
une consigne ; ici, il fait une **démarche** — un papier affiché à lire, une
date à recopier, un nom à épeler, seize cases à remplir et une signature au
bas de la page. L'épellation existe déjà au niveau 1, dans
`module-n1-presenter` : elle y sert à se présenter, elle sert ici à faire
écrire son nom correctement par quelqu'un d'autre.
"""

MANIFESTE = {
    'slug': 'module-n2-inscription',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Inscription',

    # Couleur du niveau 2, posée par `build/couleurs_niveau.py`.
    'accent': '#A83A22',
    'accent_doux': '#FBEAE4',

    'ia_oral': "L'élève s'inscrit au cours de français au secrétariat du "
               "centre : il dit ce qu'il veut, il donne son nom de famille et "
               "son prénom, il épelle son nom lettre par lettre, il donne sa "
               "date de naissance, son adresse et son numéro de téléphone. "
               "Phrases très courtes, au présent. Le vouvoiement doit être "
               "tenu du début à la fin.",

    'jr_cas': 'annonce',
    'jr_role': 'moi',
    'jr_scenario': 'inscription',
    'ia_jeu_de_role': "L'élève s'inscrit à un cours de français : il demande "
                      "la date, l'heure et le lieu, il redit les "
                      "renseignements pour vérifier, il donne les "
                      "renseignements de son formulaire une case à la fois, "
                      "et il épelle son nom quand on le lui demande.",

    'bravo': "🎉 Bravo, tu as terminé le module « Je m\\'inscris au cours de "
             "français » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
