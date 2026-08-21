# -*- coding: utf-8 -*-
"""Identité de module-n5-rendezvous — « Consultation d'un professionnel de la
santé » (niveau 5, activité 65).

Le programme est avare ici : **une seule intention**, portée à la fois par la
compréhension et par la production orales — « prendre, annuler ou modifier un
rendezvous par téléphone ». Aucun lexique n'est fourni pour cette situation ;
la liste FC_CARDS s'invente donc entièrement à partir des savoirs du niveau et
de la situation.

Ce que ce module N'EST PAS, et pourquoi :

- ce n'est pas `module-consultation` (35), le module 1 du niveau 4, qui fait
  **choisir le bon service** — clinique, urgence, Info-Santé — et décrire une
  douleur au triage. Là-bas, l'élève arrive quelque part et se fait orienter.
  Ici, l'élève tient le rendez-vous d'un bout à l'autre : il l'obtient au
  téléphone, il raconte trois mois de symptômes dans le bureau, il pose ses
  questions, puis il le déplace et l'annule dans les règles ;
- ce n'est pas `module-sante` (34) du niveau 4, qui reste au corps et aux
  symptômes ;
- ce n'est pas `module-n5-urgence` (66), qui viendra ensuite : l'urgence ne se
  prend pas en rendez-vous, et c'est justement ce qui les sépare.

Le niveau 5 demande des **discours simples mais organisés** : un échange suivi,
pas une suite de questions-réponses. D'où le récit de trois mois au défi 2 —
imparfait pour le décor, passé composé pour ce qui est arrivé, gérondif pour
dire quand ça se produit — et non une liste de symptômes.

Les faits québécois employés (GMF, carte d'assurance maladie, sans-rendez-vous,
Info-Santé, prélèvement à jeun, règle d'annulation de 24 heures affichée par
les cliniques) sont des usages courants et généraux ; la clinique, les
personnes, les numéros et les dates sont inventés.
"""

MANIFESTE = {
    'slug': 'module-n5-rendezvous',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': "Consultation d\\'un professionnel de la santé",

    # Sarcelle : la couleur du niveau 5. Posée par build/couleurs_niveau.py,
    # qui la relit dans colors.css — ne pas la choisir à la main.
    'accent': '#0D7A6F',
    'accent_doux': '#DCF2EF',

    'ia_oral': "L'élève raconte à un médecin un problème de santé qui dure "
               "depuis plusieurs mois. Vérifier qu'il situe le début du "
               "problème avec une expression de durée, qu'il plante le décor "
               "à l'imparfait et raconte ce qui est arrivé au passé composé, "
               "qu'il dit à quel moment le malaise se produit avec un "
               "gérondif (« en me levant », « en montant l'escalier »), qu'il "
               "distingue ce qui est constant de ce qui est occasionnel, et "
               "qu'il termine par au moins deux questions au médecin. "
               "Un récit organisé compte plus qu'un vocabulaire médical "
               "savant : ne pas exiger de termes techniques.",

    'jr_cas': 'premier',
    'jr_role': 'patient',
    'jr_scenario': 'rendezvous',
    'ia_jeu_de_role': "L'élève téléphone à une clinique au sujet d'un "
                      "rendez-vous : il dit en une phrase pourquoi il "
                      "appelle, donne son nom et son numéro de carte "
                      "d'assurance maladie, décrit brièvement son problème et "
                      "depuis quand il dure, propose ou accepte des "
                      "disponibilités, puis note la date, l'heure, l'heure "
                      "d'arrivée, ce qu'il doit apporter et le délai "
                      "d'annulation — et il répète l'essentiel pour le "
                      "confirmer avant de raccrocher.",

    'bravo': "🎉 Bravo, vous avez terminé le module « Prendre rendez-vous "
             "chez le médecin » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
