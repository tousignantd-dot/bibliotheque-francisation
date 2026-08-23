# -*- coding: utf-8 -*-
"""Identité de module-n8-actualite — « Deux versions, et la mienne »
(niveau 8, activité 122, numéro 5 du niveau).

Le slug porte le niveau et nomme la situation, comme les quatre autres
modules d'actualité du dépôt.

CE QUE LE PROGRAMME DEMANDE
---------------------------
`python3 build/cadre.py 8 "actualité"` rend **sept** intentions — le cadre le
plus fourni du niveau après « Emploi » :

  · Compréhension orale  — comprendre un point de vue sur l'actualité ;
                           comprendre des reportages ou des documentaires
                           reliés à des sujets d'intérêt général.
  · Production orale     — commenter l'actualité en justifiant son point de
                           vue.
  · Compréhension écrite — comprendre un article d'opinion, une chronique, un
                           éditorial ou un blogue ; comprendre des articles ou
                           des reportages liés à des sujets d'intérêt général.
  · Production écrite    — rédiger une lettre pour le courrier des lecteurs
                           pour donner son opinion ; résumer un texte
                           d'opinion.

Contrairement aux quatre autres modules de la situation, celui-ci n'a **rien
à emprunter aux attentes de fin de cours** : les deux productions écrites sont
demandées explicitement, et « Je me lance » les porte toutes les deux — le
résumé du texte d'opinion est intégré à la lettre, dont le premier paragraphe
doit résumer l'éditorial auquel elle répond. C'est le contraire de
`module-n8-recherche` (119), où le courriel devait être justifié.

Le lexique rattaché est vide pour cette situation, comme aux niveaux 5, 6
et 7. Les seize mots se composent à partir des trois savoirs qui la nomment :
« lecture d'une chronique, d'un éditorial ou d'un blogue », « lecture d'un
article d'opinion » et « discussion portant sur un sujet d'actualité ».

CE QUI LE DISTINGUE DE SES QUATRE VOISINS DE SITUATION
------------------------------------------------------
Écrit avant le scénario, en une phrase par voisin.

  · `module-nouvelles` (41, niveau 4) **repère** dans un bulletin : qui, quoi,
    où, quand.
  · `module-n5-actualite` (71) **raconte** un fait divers à quelqu'un qui ne
    l'a pas lu ; le silence de l'autre l'oblige à s'organiser.
  · `module-n6-actualite` (99) **suit un même sujet** à travers cinq genres et
    comprend pourquoi ils ne disent pas la même chose.
  · `module-n7-actualite` (60) **démêle le fait de l'opinion** dans un texte
    signé, et intervient dans un blogue.
  · Celui-ci : la nouvelle est connue de tout le monde et personne n'en
    conteste les faits. Ce qui se travaille est **le désaccord** — deux
    comptes rendus qui choisissent autrement sans qu'aucun ne mente, un
    éditorial dont on discute la thèse et non les chiffres, et un avis qu'il
    faut défendre en **tenant compte de l'objection** plutôt qu'en l'ignorant.

C'est aussi le module le plus **textuel** du dépôt : trois exercices de type
`texte`, un par défi. La situation les appelle — quatre de ses sept intentions
portent sur de l'écrit —, et le troisième suit la recommandation du
journal de l'activité 119 : faire lire à l'élève, découpé par fonctions, le
modèle du texte qu'on lui demandera d'écrire vingt minutes plus tard.

LE SCÉNARIO — TOUT EST INVENTÉ
-------------------------------
Mirela Petrescu, 43 ans, arrivée de Roumanie il y a six ans, technicienne en
documentation à la bibliothèque municipale de Rivière-aux-Cèdres, une ville de
vingt-quatre mille habitants à quarante minutes de Sherbrooke. Le conseil
municipal a voté la cession du boisé Sainte-Perpétue — onze hectares
appartenant à la Ville — à Habitations Verchères-Nord, qui veut y bâtir cent
quatre-vingts logements dont quarante-cinq à loyer abordable. Un registre
référendaire s'ouvre dans quinze jours.

  · Régine Sauvé, 68 ans, enseignante retraitée, porte-parole du comité de
    citoyens « Le boisé, c'est à nous ». Voix `enseignante`.
  · Grégoire Ferland, animateur de la tribune téléphonique « Le fil de la
    Rive » à la radio communautaire CIRC, et auteur d'un balado hebdomadaire.
    Voix `narrateur` — **non ralentie** : sa chronique du défi 2 est un
    monologue de douze répliques dont le débit rapide est justement ce que
    l'exercice fait travailler.
  · Wilfrid Chamberland, 52 ans, éditorialiste à l'hebdomadaire *Le Courant de
    la Rive*, favorable au projet. Voix `masculin_1`.

Quatre personnages, quatre voix, aucun partage. Compté avant d'écrire : le
dépôt n'a que **deux voix féminines**, donc aucun extrait ne réunit plus de
deux femmes — Mirela et Régine, jamais une troisième.

La ville, le boisé, le promoteur, les deux médias, les personnes, les chiffres
et l'événement sont **entièrement inventés**. Aucun fait d'actualité réel n'est
mentionné nulle part, et aucun journal, chroniqueur ou élu existant n'est
nommé : un module de francisation n'a pas à fabriquer de faux documents sur des
faits réels. Ce qui n'est pas inventé est vérifié et relève de la procédure
municipale québécoise, pas de l'actualité : une assemblée publique de
consultation, un registre référendaire ouvert aux personnes habiles à voter,
un règlement d'emprunt, un avis public, une séance du conseil municipal.

Le module **vouvoie** partout, sauf entre Mirela et Régine, qui se tutoient
après le premier extrait : elles se connaissent de la bibliothèque, et le
module travaille justement la variété de registre — la tribune et la lettre
sont, elles, au vouvoiement strict.
"""

MANIFESTE = {
    'slug': 'module-n8-actualite',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': "Suivi de l\\'actualité",

    # Pourpre : la couleur du niveau 8. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#7E3F98',
    'accent_doux': '#F3E8F7',

    'ia_oral': "L'élève intervient à une tribune téléphonique pour commenter "
               "un sujet d'actualité locale : il annonce sa position en une "
               "phrase, résume le fait en deux phrases sans le déformer, "
               "donne deux arguments dont un chiffré, concède ce que "
               "l'autre camp a de juste avec « certes… mais » ou « bien "
               "que » suivi du subjonctif, emploie au moins une hypothèse "
               "irréelle au conditionnel passé et une phrase emphatique, "
               "puis termine par une demande précise. Il vouvoie l'animateur "
               "et reste courtois même en désaccord.",

    'jr_cas': 'boise',
    'jr_role': 'auditeur',
    'jr_scenario': 'tribune',
    'ia_jeu_de_role': "L'élève appelle à une tribune téléphonique pour "
                      "commenter un projet municipal contesté : il annonce sa "
                      "position, la justifie par des faits, répond à "
                      "l'animateur qui le contredit sans se fâcher, concède "
                      "un point avant d'avancer le sien, distingue ce qu'il "
                      "sait de ce qu'il croit, et refuse de reprendre à son "
                      "compte une rumeur qu'on lui tend.",

    'bravo': "🎉 Bravo, vous avez terminé le module « Deux versions, et la "
             "mienne » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie',
                          'Beaulieu', 'tendinite',
                          'Consulter au bon endroit', 'physiothérapie'],
}
