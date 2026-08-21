# -*- coding: utf-8 -*-
"""Identité de module-n3-loyer — « Trois questions avant de louer » (niveau 3).

La situation du programme est « Location d'un logement », et
`build/cadre.py 3 "Location d’un logement"` est catégorique : **deux
intentions de communication, pas une de plus**.

    Compréhension orale · Demander et comprendre des renseignements sur le
                          logement pendant une visite
    Production orale    · la même, mot pour mot
    Compréhension écrite· Lire des petites annonces simples

Aucune intention de production écrite n'est rattachée à cette situation au
niveau 3. La production écrite du module s'appuie donc sur les attentes de fin
de cours du niveau, qui demandent « un message compréhensible d'une ou de
quelques phrases simples se rapportant à des situations personnelles ou
familières » — d'où un court message à un proche, cinq à huit phrases, et
rien de plus ambitieux.

Le cadre a décidé de la forme, et il l'a resserrée : le module ne parle ni de
bail à lire, ni de comparaison entre deux logements, ni de recours. Il tient
en trois gestes, qui sont les trois défis — **on lit une annonce, on
téléphone, on pose trois questions**.

Deux voisins dans le dépôt, et aucun recoupement :

- `module-logement` (niveau 4, module 9) visite deux logements et les compare
  pour choisir : il argumente, il pèse ce qui compte pour soi. Ici, l'élève ne
  compare rien — il y a un seul logement, et tout le travail est d'aller
  chercher six renseignements qu'on ne lui donnera pas spontanément.
- `module-n5-logement` fait la démarche entière : l'appel avec prise de notes,
  la visite, puis le bail, l'annexe et l'avis de renouvellement. Ici, aucun
  papier ne se lit sauf six lignes d'annonce, et personne ne signe.

Le lexique que le programme rattache à la situation est court et il a servi
tel quel, comme le voulait la consigne : les pièces (cuisine, salon, chambre à
coucher, salle de bain, balcon), les caractéristiques (3 ½, 4 ½, meublé, non
meublé, chauffé, éclairé, électricité comprise), le bail, et les verbes
« louer », « pouvoir », « falloir », « se renseigner », « loger », « chauffer »,
« éclairer ».

Les faits québécois sont vérifiés, pas inventés :

- le **bail** est le formulaire obligatoire du Tribunal administratif du
  logement (l'ancienne Régie du logement, renommée en 2020) ; il dure
  habituellement douze mois et se **reconduit tout seul** si personne n'envoie
  d'avis ;
- le **1er juillet** est la date de déménagement usuelle au Québec, et la
  plupart des baux courent du 1er juillet au 30 juin ;
- un propriétaire **ne peut pas exiger de dépôt de garantie**, ni le dernier
  mois de loyer, ni plus d'un mois de loyer d'avance : le Code civil ne lui
  permet de demander que le premier mois, et encore, à l'avance seulement ;
- il **ne peut pas refuser un logement à une famille avec des enfants** : la
  Charte des droits et libertés de la personne interdit la discrimination
  fondée sur l'état civil ;
- un **3 ½** a une chambre fermée, un **4 ½** en a deux ; le demi désigne la
  salle de bain, pas une pièce.

Les personnes, l'immeuble, l'annonce, l'adresse et le numéro de téléphone sont
inventés. Le numéro appartient à la plage 555-01xx, réservée à la fiction.

**Les médias sont en attente.** Ce module a été produit dans un environnement
distant qui ne porte ni la clé d'ElevenLabs ni celle de fal.ai : aucun appel
n'a été tenté. Le contenu n'a **pas** été amputé pour autant — les treize
cartes à photo gardent leur champ `img`, les deux exercices `imgmatch` gardent
leurs treize images, et les bandeaux `savoir` gardent leurs pastilles. Les
deux générateurs sont écrits, complets et relançables tels quels sur le poste
de l'utilisateur ; les deux commandes sont dans le journal de
`docs/vagues-suivantes.md`, à l'entrée de l'activité 81.
"""

MANIFESTE = {
    'slug': 'module-n3-loyer',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    # L'apostrophe s'échappe : le gabarit place ce thème dans une chaîne
    # JavaScript à guillemets simples.
    'theme': "Location d\\'un logement",

    # Ambre : la couleur du niveau 3. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#B45309',
    'accent_doux': '#FBEEDC',

    'ia_oral': "L'élève téléphone au sujet d'une petite annonce de logement : "
               "il salue, il dit qu'il appelle pour l'annonce, il pose trois "
               "questions simples — le loyer et ce qui est compris dedans, le "
               "nombre de chambres, la date à laquelle le logement est libre — "
               "puis il demande un rendez-vous pour visiter et répète le jour "
               "et l'heure pour vérifier.",

    'jr_cas': 'chabot',
    'jr_role': 'locataire',
    'jr_scenario': 'visite',
    'ia_jeu_de_role': "L'élève visite un logement à louer dont il a lu "
                      "l'annonce : il se présente, il demande le loyer et ce "
                      "qui est compris, il se renseigne sur les pièces, la "
                      "buanderie, le stationnement et la date, et il vérifie "
                      "ce qu'il a compris avant de partir.",

    'bravo': "🎉 Bravo, tu as terminé le module « Trois questions avant de "
             "louer » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
