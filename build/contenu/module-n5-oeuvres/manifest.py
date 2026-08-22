# -*- coding: utf-8 -*-
"""Identité de module-n5-oeuvres — « Le club du jeudi » (niveau 5).

La situation du programme est « Découverte d'œuvres littéraires, musicales,
cinématographiques ou télévisuelles », domaine général de formation « Culture
et médias ».
`build/cadre.py 5 "Découverte d’œuvres"` rend un cadre très étroit : **deux
intentions de communication seulement**, « Regarder un film » en compréhension
orale et « Lire une bande dessinée » en compréhension écrite. Aucune intention
de production, aucun lexique rattaché. Tout le reste du module se déduit des
savoirs du niveau 5 et des attentes de fin de cours.

Ce que le cadre a décidé, malgré son étroitesse :

· Les deux intentions sont des intentions de **réception** — regarder, lire.
  Or les critères d'évaluation du niveau 5 exigent aussi « une communication
  orale appropriée de discours se rapportant à des thèmes familiers : besoins
  courants, **loisirs ou centres d'intérêt** ». C'est la seule situation du
  programme où le loisir est la matière même de la conversation. Le module va
  donc de la réception vers la production : on regarde, on lit, puis on
  raconte et on juge.
· Le niveau 5 est le premier du **stade intermédiaire** : « des discours
  simples mais organisés ». Le module ne demande donc jamais une réponse à une
  question, mais un tour de parole entier — deux minutes debout devant le
  club, où personne n'interrompt.
· C'est le premier module du programme où l'élève donne une **appréciation et
  la justifie**. Dire « c'est bon » ne compte pas ; l'avis doit être annoncé
  comme un avis, porté par un adjectif précis, et suivi d'une raison.

Les savoirs exercés, pris dans les 78 du niveau :

· le présent de narration — distinguer les actions en cours des actions
  habituelles, employer le présent pour la simultanéité (Défi 1) ;
· les pronoms relatifs simples qui, que, où, et le GN à expansion (Défi 1) ;
· les pronoms démonstratifs complexes non déictiques — celui qui, celle que,
  ceux dont on parle (Défi 2) ;
· la reprise de l'information par substitution lexicale — synonymie et
  hyperonymie : l'album, la bande dessinée, l'histoire, l'œuvre (Défi 2) ;
· les phrases emphatiques par dislocation — « moi, ce qui m'a touchée,
  c'est… » (Défi 3) ;
· l'exclamative avec Quel…! et l'accord du déterminant exclamatif (Défi 3) ;
· les connecteurs de cause et de concession, et la subordonnée à verbe
  conjugué CD avec « que » (Défi 3).

Ce qui le distingue de son voisin de niveau 4 : au niveau 4, on nomme un
loisir et l'on dit qu'on l'aime ; ici, l'élève tient seul un discours suivi de
deux minutes sur une œuvre — il en raconte l'intrigue au présent sans dévoiler
le dénouement, il la reprend sans se répéter, puis il justifie son
appréciation devant quelqu'un qui n'est pas d'accord.

Les personnages et les lieux sont inventés, et le module n'attribue jamais un
titre, un auteur ni une date réels à une œuvre : les élèves parlent de leurs
propres lectures et de leurs propres films, et l'assistant a pour consigne
explicite, dans `server.py`, de n'inventer aucun titre. Les mots du métier —
une case, une bulle, une planche, une onomatopée, un album, un tome, une
intrigue, un dénouement — sont, eux, ceux que la bibliothèque emploie
réellement.
"""

MANIFESTE = {
    'slug': 'module-n5-oeuvres',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    # L'apostrophe est échappée : le thème est injecté dans une chaîne
    # JavaScript à guillemets simples, au moment du dépôt de la production
    # orale. Non échappée, elle ferme la chaîne et l'envoi meurt.
    'theme': "Découverte d\\'œuvres",

    # Sarcelle : la couleur du niveau 5. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#0D7A6F',
    'accent_doux': '#DCF2EF',

    'ia_oral': "L'élève présente en deux minutes, devant le club de lecture "
               "du jeudi, une œuvre qu'il a aimée : il dit d'abord de quoi il "
               "parle — le titre, le genre et le support —, il raconte "
               "l'intrigue au présent sans dévoiler le dénouement, il donne "
               "son appréciation avec un adjectif précis plutôt qu'avec "
               "« c'est bon », il la justifie par au moins une raison, et il "
               "dit à qui il conseille l'œuvre. Il vouvoie le groupe.",

    'jr_cas': 'club',
    'jr_role': 'interlocuteur',
    'jr_scenario': 'oeuvres',
    'ia_jeu_de_role': "L'élève parle d'une œuvre à quelqu'un qui ne la "
                      "connaît pas : il dit de quoi il s'agit, il en raconte "
                      "le début au présent sans révéler la fin, il donne son "
                      "avis avec un adjectif précis, il le justifie, et il "
                      "tient son avis quand son interlocuteur n'est pas "
                      "d'accord.",

    'bravo': "🎉 Bravo, vous avez terminé le module « Le club du jeudi » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
