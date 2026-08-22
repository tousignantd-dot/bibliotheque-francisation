# -*- coding: utf-8 -*-
"""Identité de module-n3-recherche-emploi — « On embauche » (niveau 3).

La situation du programme est « Recherche d'emploi », et c'est
`build/cadre.py 3 "Recherche d’emploi"` qui a décidé de la forme du module.
Son verdict est court et net : **quatre intentions de communication
seulement**, et elles se répartissent de façon très inégale.

  · Compréhension et production orales — une seule, la même des deux côtés :
    « Offrir ses services en personne et comprendre l'information donnée par
    son interlocuteur ». Pas d'entrevue, pas de téléphone, pas de relance :
    on entre quelque part et on demande si ça engage.
  · Compréhension écrite — deux : « Lire des offres d'emploi simples » et
    « Lire et remplir un formulaire simple de demande d'emploi ».
  · Production écrite — deux : le même formulaire, et « Rédiger une courte
    annonce pour offrir ses services ».

Le module est donc bâti à trois défis qui suivent exactement ce découpage :
on offre ses services de vive voix (Défi 1), on lit ce qui est affiché
(Défi 2), on écrit son nom sur le papier et on rédige sa propre annonce
(Défi 3). Aucun document n'a été inventé en dehors de ceux que le programme
nomme : une affiche d'embauche, deux offres simples, un formulaire de demande
d'emploi et une petite annonce de services.

Le lexique du CSS de Laval **ne rattache aucune entrée** à « Recherche
d'emploi ». Il en rattache trois à « Emploi », au même niveau, et elles ont
servi de socle plutôt que d'être réinventées : les *noms de tâches*, le
*parcours*, et les *noms de quelques métiers courants* rattachés à l'entrée
voisine. Le reste du vocabulaire est composé à partir des quatre intentions
ci-dessus, comme `build/cadre.py` le prescrit quand la situation n'a pas de
lexique.

**Deux voisins sur la même situation, et rien qui se recoupe.** Au niveau 6,
`module-n6-recherche` fait passer une entrevue d'embauche : on raconte son
parcours, on argumente, on pose ses questions au recruteur. Ici, au niveau 3,
rien de tout cela n'est demandé par le programme et rien de tout cela n'est
fait. Le geste du module est plus petit et plus concret : lire une affiche
collée dans une vitrine, pousser la porte, demander si ça engage, dire en
deux phrases ce qu'on sait faire et quand on est libre, laisser son nom et
son numéro de téléphone. Le scénario `entrevue` de `server.py` est calibré
pour le niveau 6 et serait ingérable ici ; le module ajoute son propre
scénario `embauche`, bref, où la personne à qui on parle est occupée et ne
donne que ce qu'on lui demande.

*Ce qui le distingue de son voisin du 4* : au niveau 4, `module-travail`
(activité 25) part d'un emploi déjà obtenu — l'horaire, les tâches, le
remplacement à demander. Ici, l'emploi n'existe pas encore : tout le module
tient dans les quatre gestes qui précèdent l'embauche, et il s'arrête au
moment où le formulaire est remis.

Le quartier, la boulangerie, le centre communautaire, les personnes, les
horaires, les salaires et les numéros de téléphone sont inventés.
"""

MANIFESTE = {
    'slug': 'module-n3-recherche-emploi',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Recherche d\'emploi',

    # Ambre : la couleur du niveau 3. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#B45309',
    'accent_doux': '#FBEEDC',

    'ia_oral': "L'élève entre dans un commerce pour offrir ses services : il "
               "salue, il dit en une phrase pourquoi il vient, il nomme ce "
               "qu'il sait faire et depuis quand, il donne ses "
               "disponibilités avec des jours et des heures, il demande à "
               "qui laisser son nom, puis il épelle son nom et donne son "
               "numéro de téléphone chiffre par chiffre avant de remercier.",

    'jr_cas': 'affiche',
    # `jr_role` est le rôle de l'ÉLÈVE, pas celui de l'assistant : server.py
    # le reçoit sous le nom `role_eleve` et donne à l'assistant l'autre rôle
    # du scénario. L'élève vient offrir ses services, donc « candidat » ;
    # l'assistant joue le gérant. Écrire « gerant » ici inverserait les deux
    # et l'assistant se mettrait à chercher du travail.
    'jr_role': 'candidat',
    'jr_scenario': 'embauche',
    'ia_jeu_de_role': "L'élève entre quelque part pour offrir ses services : "
                      "à la boulangerie où une affiche « On embauche » est "
                      "collée dans la vitrine, au centre communautaire qui "
                      "cherche quelqu'un pour l'entretien, ou à l'épicerie "
                      "où une petite annonce est punaisée au babillard. Il "
                      "doit demander si ça engage, dire ce qu'il sait faire, "
                      "donner ses disponibilités et laisser ses "
                      "coordonnées.",

    'bravo': "🎉 Bravo, tu as terminé le module « On embauche » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
