# -*- coding: utf-8 -*-
"""Identité de module-n2-colis — « J'envoie une lettre et un colis ».

Dixième module court du dépôt, neuvième du niveau 2. La situation du
programme est « Démarches à la poste ». Son cadre est étroit et il décide de
tout : `build/cadre.py 2 "Démarches à la poste"` ne rend que **deux**
intentions, et elles sont toutes les deux écrites — « lire et remplir un
formulaire » (compréhension écrite et production écrite) et « adresser une
enveloppe » (production écrite). Défi 1 est donc l'enveloppe, Défi 2 est le
formulaire. Rien n'a été ajouté autour.

Distinct de `module-n3-poste` (niveau 3, activité 80), qui porte la même
situation un niveau plus haut : là-bas, l'unique intention est orale — on
s'informe au comptoir, on compare deux vitesses d'envoi, on demande un
mandat-poste, et le préposé répond par des phrases entières. Ici, la parole
tient en trois mots (« Un timbre, s'il vous plaît. », « Combien ça coûte ? »)
et tout le module se joue sur le papier : les cinq lignes d'une adresse, les
abréviations, le code postal, les cases d'un formulaire et l'endroit où on
signe.
"""

MANIFESTE = {
    'slug': 'module-n2-colis',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Démarches à la poste',

    # Couleur du niveau 2, posée par `build/couleurs_niveau.py`.
    'accent': '#A83A22',
    'accent_doux': '#FBEAE4',

    'ia_oral': "L'élève est au comptoir postal. Il salue, il demande ce "
               "qu'il veut en une phrase très courte (« Un timbre, s'il vous "
               "plaît. », « Je veux envoyer ce colis. »), il demande le prix "
               "avec « Combien ça coûte ? », il redit le montant qu'il a "
               "entendu pour vérifier, et il remercie. Phrases très courtes, "
               "au présent, sans subordonnée. Le vouvoiement doit être tenu "
               "du début à la fin.",

    'jr_cas': 'timbre',
    'jr_role': 'moi',
    'jr_scenario': 'colis',
    'ia_jeu_de_role': "L'élève fait une démarche au comptoir postal : il "
                      "demande un timbre ou l'envoi d'un colis, il demande "
                      "le prix, il répète le montant pour vérifier, il "
                      "demande de répéter quand ça va trop vite, et il "
                      "remercie avant de partir.",

    'bravo': "🎉 Bravo, tu as terminé le module « J\\'envoie une lettre et un colis » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
