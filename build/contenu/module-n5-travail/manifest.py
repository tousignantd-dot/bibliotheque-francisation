# -*- coding: utf-8 -*-
"""Identité de module-n5-travail — « Le travail par écrit » (niveau 5,
activité 67).

Ce que le programme demande ici, et qui surprend : la situation « Emploi » du
niveau 5 ne parle pas de relations d'équipe. Ses sept intentions sont des
**écrits et des procédures de travail** — comprendre puis nommer les
principales étapes d'une démarche administrative simple, enregistrer un message
téléphonique, lire un mode d'emploi, rédiger des notes pratiques sur
l'utilisation du matériel courant, rédiger un court message à partir de notes
détaillées, et rédiger un courriel de réponse automatique en cas d'absence.
Les savoirs lexicaux du niveau les répètent mot pour mot : « photocopieur,
imprimante, boîte vocale », « appuyer, insérer, verrouiller, confirmer »,
« autorisation d'absence, registre des heures », « abréviations », « raison de
l'absence, moment du retour, personne à joindre en cas d'urgence ».

Aucun lexique n'est fourni pour cette situation : les seize mots de FC_CARDS
s'inventent à partir des savoirs ci-dessus.

Ce que ce module N'EST PAS, et pourquoi :

- ce n'est pas `module-travail` (39), au niveau 4, où l'on **annonce une
  absence ou un retard** par téléphone, à voix chaude, dans l'urgence du
  matin. Ici l'absence se prépare des semaines d'avance, par écrit, en six
  étapes, et le téléphone ne sert qu'à laisser un message que personne
  n'écoute en direct ;
- ce n'est pas `module-n8-emploi` (61), « Tenir son bout au travail », qui
  fait défendre un point de vue et négocier avec un supérieur. Ici on ne
  négocie rien : on suit une procédure et on réclame une trace écrite ;
- ce n'est pas `module-n6-recherche` (59), qui **cherche** un emploi — offre,
  demande, entrevue. Ici l'emploi est déjà obtenu, et c'est la paperasse du
  poste qu'il faut apprendre.

Le niveau 5 demande des **discours simples mais organisés**. D'où les six
étapes nommées dans l'ordre au défi 3, la note d'appel reconstruite à partir
d'un message entendu au défi 1, et le mode d'emploi en cinq temps au défi 2 —
plutôt qu'une suite de questions-réponses.

Les faits québécois employés ont été vérifiés le 21 août 2026 auprès de la
CNESST et de Légis Québec, et non inventés : deux journées d'absence payées par
année pour maladie ou obligations familiales après trois mois de service
continu, jusqu'à dix journées d'absence par année à ce titre ; deux semaines de
vacances après un an de service continu et trois semaines après trois ans ;
l'employeur doit faire connaître les dates de vacances au moins quatre semaines
à l'avance ; le bulletin de paie doit contenir assez de renseignements pour que
la personne puisse vérifier le calcul de son salaire (art. 46 de la Loi sur les
normes du travail). La coopérative, les personnes, les numéros de poste, les
dates et les politiques internes sont inventés — et le module dit quand une
règle vient de l'employeur plutôt que de la loi.
"""

MANIFESTE = {
    'slug': 'module-n5-travail',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Emploi',

    # Sarcelle : la couleur du niveau 5. Posée par build/couleurs_niveau.py,
    # qui la relit dans colors.css — ne pas la choisir à la main.
    'accent': '#0D7A6F',
    'accent_doux': '#DCF2EF',

    'ia_oral': "L'élève enregistre le message d'accueil de sa boîte vocale au "
               "travail. Vérifier qu'il se nomme et nomme son service dès la "
               "première phrase, qu'il dit qu'il n'est pas disponible sans "
               "raconter pourquoi, qu'il demande le nom, le numéro et la "
               "raison de l'appel, qu'il annonce au futur simple quand il "
               "rappellera, qu'il donne une autre ressource pour ce qui ne "
               "peut pas attendre, et qu'il termine par une formule de "
               "politesse. Vérifier aussi le registre : vouvoiement tenu du "
               "début à la fin, pas de « salut », pas de « bye ». Le message "
               "doit tenir en vingt à trente secondes : signaler ce qui est "
               "de trop plutôt que d'exiger un vocabulaire savant.",

    'jr_cas': 'vacances',
    'jr_role': 'employe',
    'jr_scenario': 'conge',
    'ia_jeu_de_role': "L'élève demande un congé à son chef d'équipe. Il "
                      "annonce sa demande en une phrase avec les deux dates, "
                      "celle du départ et celle du retour ; il propose "
                      "lui-même une solution pour son remplacement à "
                      "l'accueil ; il demande ce qu'il faut remplir, à qui "
                      "l'envoyer et dans quel délai ; il demande ce qui est "
                      "payé et ce qui ne l'est pas ; et il ne sort pas du "
                      "bureau sans avoir demandé une confirmation écrite. Le "
                      "vouvoiement se tient du début à la fin.",

    'bravo': "🎉 Bravo, vous avez terminé le module « Le travail par "
             "écrit » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
