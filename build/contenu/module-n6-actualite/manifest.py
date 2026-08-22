# -*- coding: utf-8 -*-
"""Identité de module-n6-actualite — « Suivre un sujet dans les médias ».

Niveau 6, situation « Suivi de l'actualité », domaine « Culture et médias ».
Activité 99. **Module pilote du niveau 6** : premier module de ce niveau
produit avec le gabarit, et modèle des neuf suivants. La note qui explique
les choix est dans `docs/vagues-suivantes.md`, section « Vague 5 ».

Ce que `python3 build/cadre.py 6 "Suivi de l'actualité"` donne, et rien
d'autre : **quatre intentions, toutes en compréhension**.

  · CO — comprendre des chroniques pratiques, des entrevues ou des
    documentaires sur des thèmes pratiques ou courants ;
  · CE — comprendre des chroniques pratiques, des entrevues ou des articles
    informatifs sur des thèmes courants ;
  · CE — comprendre un fait divers dans un journal ;
  · CE — lire le courrier des lecteurs.

Aucune production n'est demandée par la situation. C'est donc les **attentes
de fin de cours** du niveau qui portent « Je me lance » : l'adulte « rédige un
courriel [...] pour informer son destinataire du contenu d'un article
d'intérêt général », il « rédige un court texte en organisant ses idées à
l'aide de paragraphes », et il « décrit les étapes d'une démarche
administrative en donnant les détails nécessaires ». La production écrite est
donc un **courriel formel au courrier des lecteurs** qui informe d'abord et
donne son avis ensuite ; la production orale est le compte rendu détaillé de
la démarche à suivre. Le savoir de grammaire du texte « Découper, disposer,
formuler et présenter le contenu d'un courriel formel » vient confirmer la
forme.

Le lexique est vide pour cette situation. Les seize mots s'inventent à partir
des deux savoirs qui la nomment : « vocabulaire lié à l'univers médiatique, à
l'actualité, à l'opinion : documentaire, reportage, fait divers, courrier des
lecteurs » et « verbes et locutions exprimant l'opinion ».

Les voisins, et ce qui l'en sépare :

· `module-n5-actualite` (71, niveau 5) n'a qu'un genre — le fait divers — et
  qu'un travail : **raconter** à quelqu'un ce qu'on a lu. Ici, le fait divers
  n'est que le point d'entrée du dossier : il ouvre le Défi 3 et il est le
  genre le plus court des cinq. Le travail n'est plus de restituer un récit
  mais de **suivre un même sujet à travers plusieurs genres** — une chronique,
  une entrevue, un documentaire, un fait divers, une page de courrier — et de
  comprendre pourquoi ils ne disent pas la même chose.
· `module-n7-actualite` (60, niveau 7) démêle le **fait de l'opinion** chez
  celui qui écrit, dans un texte signé, et fait intervenir dans un blogue.
  Ici, personne ne cache son opinion : la chroniqueuse annonce la sienne, le
  courrier des lecteurs est fait pour ça. Ce qui est difficile au niveau 6,
  c'est plus modeste et plus fondamental : **tenir le fil d'un texte suivi**
  — savoir ce que reprend « le », « en », « où » ; reconnaître qu'un
  plus-que-parfait recule d'un cran ; entendre un passé simple de
  documentaire ; suivre une hypothèse en « si ».
· `module-n3-electro` (76, niveau 3) achète un électroménager au magasin.
  Ici on n'achète rien : la laveuse est déjà là, elle est brisée, et tout le
  module se passe dans les médias qui en parlent.

Les faits du Québec sont vérifiés, jamais devinés — auprès de l'Office de la
protection du consommateur, le 22 août 2026. La garantie légale veut qu'un
bien serve à l'usage normal auquel il est destiné, qu'il serve à cet usage
**pendant une durée raisonnable** compte tenu du prix payé, du contrat et des
conditions d'utilisation, qu'il soit exempt de vice caché et conforme à la
description qu'on en a faite. Elle s'applique même quand la garantie du
fabricant est expirée et même sans garantie prolongée achetée. Le recours
passe d'abord par une **mise en demeure** écrite, où un délai de dix jours est
le plus souvent tenu pour raisonnable, puis par la **Division des petites
créances** de la Cour du Québec pour une réclamation de 15 000 $ ou moins, où
l'on se représente soi-même, sans avocat.

Tout le reste est inventé : Nadège Beauplan, Raphaël Choquette, Claudine
Rousseau, Théo Marchesseault, Myriam Vaugeois, la radio « CFTR », le journal
« Le Courrier de la Batture », les marques, les prix et les dates. Une
chronique attribuée à une vraie station serait une fausse nouvelle.
"""

MANIFESTE = {
    'slug': 'module-n6-actualite',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    # L'apostrophe est échappée : le thème est injecté dans une chaîne
    # JavaScript à guillemets simples au moment du dépôt de la production
    # orale. Non échappée, elle ferme la chaîne et l'envoi meurt.
    'theme': "Suivi de l\\'actualité",

    # Acier : la couleur du niveau 6. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#1D6B8F',
    'accent_doux': '#E7F0F6',

    'ia_oral': "L'élève explique à un collègue ce qu'il a compris d'une "
               "chronique pratique entendue à la radio sur la garantie "
               "légale : il dit d'abord de quoi il s'agit et où il l'a "
               "entendu, il énumère ensuite les étapes de la démarche dans "
               "l'ordre en donnant les détails nécessaires, il emploie des "
               "connecteurs d'exemplification pour illustrer au moins un "
               "point, puis il termine par son point de vue en l'annonçant "
               "comme un point de vue. Il tutoie son interlocuteur.",

    'jr_cas': 'laveuse',
    'jr_role': 'nadege',
    'jr_scenario': 'chroniquepratique',
    'ia_jeu_de_role': "L'élève explique à quelqu'un qui n'a pas écouté la "
                      "chronique ce qu'il en a retenu : il résume, il "
                      "reprend les étapes dans l'ordre, il répond aux "
                      "objections de son interlocuteur en distinguant ce que "
                      "la chronique disait de ce qu'il en pense, et il "
                      "emploie « si » pour poser une hypothèse réaliste.",

    'bravo': "🎉 Bravo, tu as terminé le module « Suivre un sujet dans les "
             "médias » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
