# -*- coding: utf-8 -*-
"""Identité de module-n6-oeuvres — « Un film, et ce qu'on en écrit ».

Niveau 6, situation « Découverte d'œuvres littéraires, musicales,
cinématographiques et télévisuelles », domaine « Culture et médias ».
Activité 103, `numero` 6 du niveau. Slug et numéro réservés dans
`docs/vagues-suivantes.md`, vague 6.

Ce que `python3 build/cadre.py 6 "Découverte d’œuvres" --savoirs` donne, et
rien d'autre : **trois intentions, une par compétence**.

  · CO — regarder un film pour en repérer le déroulement ;
  · CE — lire une biographie ;
  · PE — résumer un film.

Elles se rangent une par défi, et c'est ce qui a donné la forme du module :
le Défi 1 est le film lui-même, le Défi 2 est la biographie de celle qui l'a
fait, le Défi 3 est ce qu'on écrit après. **Un seul dossier, trois genres** —
la règle que le pilote du niveau 6 (activité 99) a formulée : le niveau 6
n'est pas un niveau 7 facile, c'est le niveau de la cohésion. Le 5 raconte,
le 7 démasque, le 6 suit un fil.

Aucune intention de production **orale** n'est demandée par la situation. Le
compte rendu oral de « Je me lance » se tire donc des **attentes de fin de
cours** du niveau, qui sont productives et communes à tout le cours :
l'adulte « décrit de façon détaillée » au cours d'un exposé, il « demande
l'avis de quelqu'un dans une conversation », et — pour l'écrit — il « rédige
un texte d'un ou deux paragraphes pour raconter un film de façon sommaire ».
Cette dernière attente nomme mot pour mot la production écrite du module : un
résumé de film en deux paragraphes, l'un pour l'histoire, l'autre pour l'avis.

Le lexique de la situation est vide. Les seize mots s'inventent à partir du
seul savoir lexical qui la nomme — « vocabulaire lié aux œuvres
cinématographiques et littéraires : réalisation, conte, nouvelle,
personnages, lieux, actions » — et du savoir de relations sémantiques qui
donne l'exemple du champ lexical « cinéma : documentaire, film, reportage,
court métrage ».

Les dix savoirs retenus sur les cinquante-quatre du niveau, choisis par la
question du pilote — « est-ce que ça sert à suivre un texte ? » :

  · graphie-phonie : ch qui dit [k], x qui dit [s], sh et sch qui disent [ʃ]
    — savoir commun à tout le niveau, et le cinéma en est plein
    (chronologie, orchestre, dix, soixante, un flash-back, un schéma) ;
  · exploiter des champs lexicaux pour exprimer le détail ou la nuance ;
  · le plus-que-parfait, qui dit l'antériorité quand le point de référence
    est décalé — c'est exactement ce que fait un retour en arrière ;
  · l'imparfait qui renvoie à une action en cours dans le passé, avec ou
    sans « être en train de » ;
  · comprendre l'ordre des étapes à partir d'indices autres que les
    connecteurs de temps ;
  · le passé simple : reconnaître les verbes courants à la 3e personne et
    l'associer au passé composé — en `match`, jamais en `write` ;
  · le pronom relatif « où », complément de lieu ou de temps ;
  · la reprise de l'information : « le » pour une subordonnée complétive,
    « en » pour un GPrép inanimé, et la substitution lexicale ;
  · le sens de certains adjectifs selon leur place : grand, ancien, propre,
    drôle, nouveau — le savoir qui fait la nuance d'une critique ;
  · le subjonctif après un verbe introducteur usuel + que, et l'hypothèse
    réaliste avec « si » ;
  · les guillemets qui encadrent un mot qu'on nuance, et le découpage en
    paragraphes du texte écrit.

Les voisins, et ce qui l'en sépare :

· `module-n5-oeuvres` (73, niveau 5) est son voisin immédiat, même situation
  un cran plus bas. Là-bas, l'élève **présente au club une œuvre qu'il a
  aimée** : il en raconte l'intrigue au présent, il dit ce qu'il a aimé et
  pourquoi, il la recommande. Le travail est de tenir seul un tour de parole
  de deux minutes, et l'avis peut être entier. **Ici, l'avis doit être
  nuancé** : le film a un défaut et une qualité, il faut accorder quelque
  chose à celui qui n'est pas d'accord avant de lui répondre, et l'élève doit
  distinguer ce que le film raconte de ce qu'il en pense. Ce qui change n'est
  donc pas le sujet mais le travail — et, avec lui, la matière : au 5 c'est
  le présent de narration et la dislocation, ici c'est la chronologie
  (plus-que-parfait, imparfait, passé simple) et la nuance (place de
  l'adjectif, guillemets, concession).
· `module-n6-actualite` (99, même niveau) suit un sujet d'actualité dans cinq
  genres médiatiques. Ici il n'y a **aucune actualité** : le film a trente ans
  dans le Défi 2, et les trois écrits ne s'adressent pas au même besoin — on
  ne cherche pas quoi faire, on cherche à comprendre puis à juger.
· `module-n4-…` : aucun module du niveau 4 ne porte cette situation.

**Rien de réel n'est nommé.** Le film « Les Marées de novembre », sa
réalisatrice Aurélie Pichette, le ciné-club de la salle Beauchemin à
Sherbrooke, l'hebdomadaire « L'Écho de la Magog » et le critique Léo
Charbonneau sont **inventés de toutes pièces**. C'est un choix, et il est
pédagogique autant que prudent : attribuer une fausse citation, une fausse
date de tournage ou un faux prix à une œuvre qui existe serait fabriquer un
faux document, et un module de francisation n'a pas à en produire. Les mots
du métier — un long métrage, une bande-annonce, le générique, un tournage,
une rétrospective, un premier rôle, un retour en arrière — sont, eux, ceux
qu'on emploie réellement au Québec.
"""

MANIFESTE = {
    'slug': 'module-n6-oeuvres',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    # L'apostrophe est échappée : le thème est injecté dans une chaîne
    # JavaScript à guillemets simples au moment du dépôt de la production
    # orale. Non échappée, elle ferme la chaîne et l'envoi meurt.
    'theme': "Découverte d\\'œuvres",

    # Acier : la couleur du niveau 6. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#1D6B8F',
    'accent_doux': '#E7F0F6',

    'ia_oral': "L'élève fait le compte rendu détaillé d'un film devant un "
               "petit groupe : il dit d'abord de quel film il s'agit et où "
               "il l'a vu, il raconte ensuite le déroulement dans l'ordre "
               "sans dévoiler le dénouement, en plaçant les retours en "
               "arrière au bon endroit, puis il donne un avis nuancé — une "
               "chose qui l'a convaincu, une chose qui l'a moins convaincu, "
               "chacune appuyée sur un moment précis du film. Il annonce son "
               "avis comme un avis. Il tutoie ses interlocuteurs.",

    'jr_cas': 'marees',
    'jr_role': 'therese',
    'jr_scenario': 'cineclub',
    'ia_jeu_de_role': "L'élève discute d'un film avec quelqu'un qui ne l'a "
                      "pas aimé : il résume le déroulement sans raconter la "
                      "fin, il accorde quelque chose à l'objection avant d'y "
                      "répondre, il appuie chaque jugement sur un moment "
                      "précis, et il emploie « si » pour poser une hypothèse "
                      "réaliste.",

    'bravo': "🎉 Bravo, tu as terminé le module « Un film, et ce qu\\'on en "
             "écrit » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
