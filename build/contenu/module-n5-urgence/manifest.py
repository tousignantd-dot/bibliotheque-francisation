# -*- coding: utf-8 -*-
"""Identité de module-n5-urgence — « Urgence et hospitalisation » (niveau 5,
activité 66).

Le programme est avare ici comme ailleurs au niveau 5 : **une seule intention**,
portée à la fois par la compréhension et par la production orales — « téléphoner
au 9-1-1 et au 8-1-1 ». Aucun lexique n'est fourni pour cette situation ; les
seize mots de FC_CARDS s'inventent à partir des savoirs du niveau et de ce que
la situation exige réellement.

Ce que ce module N'EST PAS, et pourquoi :

- ce n'est pas `module-urgence` (36), le module 2 du niveau 4, où une
  travailleuse se brûle l'avant-bras et **raconte après coup** ce qui est
  arrivé, à l'urgence puis à l'accueil. Ici l'élève n'est pas le blessé : il
  est celui qui accompagne. Il compose le 9-1-1 **pendant** que ça se passe et
  doit tenir l'appel sans perdre le fil, puis il traverse le triage, l'attente,
  une hospitalisation de trois jours et un congé — tout ce que le niveau 4 ne
  fait pas ;
- ce n'est pas `module-n5-rendezvous` (65) : un rendez-vous se prend, une
  urgence ne se prend pas. Là-bas on choisit son moment ; ici c'est la nuit
  qui décide ;
- ce n'est pas `module-consultation` (35), qui fait choisir le bon service et
  décrire une douleur au triage sans jamais quitter la salle d'attente.

Le niveau 5 demande des **discours simples mais organisés**. D'où le récit de
la chute au défi 2 — imparfait pour le décor, passé composé pour ce qui est
arrivé, rapporté ensuite en discours indirect (« Elle m'a demandé si elle avait
perdu connaissance ») — et non une liste de symptômes.

Les faits québécois employés — 8-1-1 Info-Santé gratuit et ouvert jour et nuit,
9-1-1 pour ce qui menace tout de suite, échelle canadienne de triage et de
gravité à cinq niveaux, carte d'assurance maladie, facturation du transport
ambulancier (125 $ plus 1,75 $ le kilomètre, gratuité pour les 65 ans et plus
lorsque le médecin de l'établissement confirme que le transport était
nécessaire) — ont été vérifiés le 21 août 2026 auprès de Québec.ca, du MSSS et
d'Urgences-santé. L'hôpital, les personnes, les numéros, les dates et les
heures d'attente sont inventés.
"""

MANIFESTE = {
    'slug': 'module-n5-urgence',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Urgence et hospitalisation',

    # Sarcelle : la couleur du niveau 5. Posée par build/couleurs_niveau.py,
    # qui la relit dans colors.css — ne pas la choisir à la main.
    'accent': '#0D7A6F',
    'accent_doux': '#DCF2EF',

    'ia_oral': "L'élève raconte au téléphone, à un proche, ce qui est arrivé "
               "pendant la nuit et où en est la personne hospitalisée. "
               "Vérifier qu'il commence par rassurer en une phrase, qu'il "
               "plante le décor à l'imparfait et raconte les évènements au "
               "passé composé, qu'il rapporte au discours indirect ce que le "
               "personnel a dit ou demandé (« la docteure a dit que… », "
               "« l'infirmière m'a demandé si… »), qu'il annonce la suite au "
               "futur simple, et qu'il termine par les renseignements "
               "pratiques : l'étage, les heures de visite, ce qu'il faut "
               "apporter. Un récit organisé compte plus qu'un vocabulaire "
               "médical savant : ne pas exiger de termes techniques.",

    'jr_cas': 'chute',
    'jr_role': 'appelant',
    'jr_scenario': 'urgence911',
    'ia_jeu_de_role': "L'élève téléphone au 9-1-1 pour une autre personne : "
                      "il donne d'abord l'adresse complète et l'endroit "
                      "exact, il dit en une phrase ce qui se passe, il répond "
                      "aux questions du répartiteur sans raconter toute "
                      "l'histoire, il dit si la personne est consciente et si "
                      "elle respire, il applique les consignes reçues à "
                      "l'impératif, il donne son nom et son numéro de "
                      "téléphone, et il ne raccroche que lorsque le "
                      "répartiteur le lui dit.",

    'bravo': "🎉 Bravo, vous avez terminé le module « Une nuit à "
             "l\\'urgence » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
