# -*- coding: utf-8 -*-
"""Identité de module-n7-oeuvres — « Ce que j'en pense, et pourquoi ».

Niveau 7, situation « Découverte d'œuvres littéraires, musicales,
cinématographiques et télévisuelles », domaine général de formation « Culture
et médias ». Activité 116, `numero` 9 du niveau. Slug et numéro réservés dans
`docs/vagues-suivantes.md`, vague 7.

Ce que `python3 build/cadre.py 7 "Découverte" --savoirs` donne, et rien
d'autre : **quatre intentions, toutes orales**.

  · CO — comprendre une œuvre ou un évènement culturel et faire un commentaire
    à ce sujet ;
  · CO — écouter un sketch humoristique ;
  · CO — comprendre une chanson ;
  · PO — comprendre une œuvre ou un évènement culturel et faire un commentaire
    à ce sujet, et résumer un film.

Les trois défis *sont* les trois genres que ces intentions nomment : le sketch,
la chanson, l'œuvre commentée devant d'autres. C'est le cas de figure que
l'activité 110 a décrit — au niveau 7, la situation peut être plus nette que le
niveau, et il n'y a alors rien à choisir parmi les cinquante-sept savoirs avant
d'avoir posé les intentions. `GRILLE_3_DEFIS` sans hésiter : trois entrées
distinctes, trois dialogues, trois grammaires.

**La production écrite ne vient pas de la situation**, qui n'en porte aucune :
elle se tire des attentes de fin de cours du niveau 7, communes à tout le
cours et, elles, productives — « en classe, il fait un exposé informel sur un
thème concret en fonction de ses centres d'intérêts » (la production orale) et
« il rédige un court texte d'opinion en appuyant son point de vue sur des
arguments » (la production écrite, ici le compte rendu envoyé aux membres du
comité). C'est écrit ici pour que le relecteur suivant ne prenne pas ces tâches
pour une invention hors programme.

**Ce qui le distingue de ses deux voisins de situation**, en une phrase, écrite
avant le scénario : `module-n5-oeuvres` (73) **raconte** une œuvre aimée devant
un club qui écoute, `module-n6-oeuvres` (103) **résume** un film et nuance son
avis par écrit — et ici, on ne raconte plus rien : on **défend un avis devant
quelqu'un qui ne le partage pas**, sur des œuvres qui ne disent pas ce
qu'elles veulent dire. Un sketch dit le contraire de sa pensée, une chanson
parle par images, une critique mêle le fait et l'opinion. C'est le seul module
du dépôt où comprendre l'œuvre et se faire entendre sont **deux difficultés
distinctes**, et où la seconde se joue contre un interlocuteur.

Les dix savoirs retenus sur les cinquante-sept du niveau, choisis par la
question : « est-ce que ça sert à comprendre l'implicite ou à défendre un
avis ? »

  · les variétés de langue — populaire, familière, standard, soutenue — et le
    ton choisi en fonction de la situation (Je découvre) ;
  · le vocabulaire des formes d'humour : ironie, sarcasme, burlesque,
    caricatural — savoir lexical que le programme nomme pour cette
    situation-là (Défi 1) ;
  · la phrase incise et le sujet qui suit le prédicat — « dit-il », « répond
    la vieille dame » : le sketch est fait de paroles rapportées (Défi 1) ;
  · les guillemets précédés d'un deux-points qui introduisent un discours
    direct (Défi 1) ;
  · les phrases emphatiques par clivage et pseudoclivage — « c'est lui qui »,
    « ce qui m'a fait rire, c'est » : la forme même du commentaire (Défi 1) ;
  · la reprise de l'information — le référent implicite du pronom « ils », la
    substitution lexicale pour ne pas se répéter (Défi 2) ;
  · les subordonnées corrélatives d'intensité — si / tellement… que, trop /
    assez… pour que : une chanson est faite de degrés (Défi 2) ;
  · le sens générique et le sens spécifique du GN sujet — « La musique, ça me
    calme » contre « La musique de ce film est trop forte » : l'exemple du
    programme est lui-même musical (Défi 2) ;
  · la concession — bien que + subjonctif, malgré que, même si + indicatif :
    accorder quelque chose avant de répondre (Défi 3) ;
  · l'hypothèse irréelle avec si + imparfait / conditionnel présent, et le
    conditionnel de politesse (Défi 3) ;
  · les connecteurs de topicalisation et de reformulation — quant à, en ce qui
    concerne, autrement dit, en somme (Défi 3).

**Aucune œuvre réelle n'est nommée nulle part.** Le spectacle « Tout est
correct » et son auteur Réjean Cadorette, la chanson « Le troisième étage » et
Nadia Ferron, le long métrage « Onze heures moins quart » et Marie-Soleil
Brouillette, la salle Aubry-Lanthier, l'hebdomadaire « Le Courrier de la
Rivière-Blanche » et le critique Damase Ouellet sont **inventés de toutes
pièces**. C'est un choix, et il est pédagogique autant que prudent : attribuer
une fausse réplique, une fausse date de sortie ou une fausse critique à une
œuvre qui existe serait fabriquer un faux document. Les mots du métier — un
tour de chant, une première partie, un rappel, une chute, un long métrage, une
critique, un compte rendu — sont, eux, ceux qu'on emploie réellement au Québec.

Le seul fait vérifié du module est le cadre de l'aide financière aux sorties
culturelles ; il n'est pas nommé et rien n'en dépend. Tout le reste est
inventé, y compris les montants du budget du comité.
"""

MANIFESTE = {
    'slug': 'module-n7-oeuvres',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    # L'apostrophe est échappée : le thème est injecté dans une chaîne
    # JavaScript à guillemets simples au moment du dépôt de la production.
    'theme': "Découverte d\\'œuvres",

    # Indigo : la couleur du niveau 7. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#3B49A0',
    'accent_doux': '#E8EAFA',

    'ia_oral': "L'élève fait un exposé informel de deux minutes devant sa "
               "classe : il présente une œuvre qu'il a vue, lue ou entendue, "
               "il la résume brièvement sans en dévoiler la fin, puis il "
               "donne son avis et le justifie — une chose qui l'a convaincu, "
               "une chose qui l'a moins convaincu, chacune appuyée sur un "
               "moment précis de l'œuvre. Il annonce son avis comme un avis, "
               "il emploie une phrase emphatique pour mettre en relief ce qui "
               "compte le plus, et une concession pour accorder quelque chose "
               "à ceux qui pensent autrement. Il vouvoie son auditoire.",

    'jr_cas': 'humour',
    'jr_role': 'marilou',
    # Le scénario s'appelle « avisoeuvre » et non « oeuvres » : cette clé-là
    # est déjà prise par module-n5-oeuvres (activité 73), et une clé en
    # double dans JEU_DE_ROLE_SCENARIOS ne lève AUCUNE erreur — Python garde
    # silencieusement la dernière définition, et le module aurait joué le
    # scénario du niveau 5.
    'jr_scenario': 'avisoeuvre',
    'ia_jeu_de_role': "L'élève discute d'une œuvre avec un collègue qui n'est "
                      "pas du tout du même avis : il dit ce qu'il a compris "
                      "de l'œuvre avant de dire ce qu'il en pense, il accorde "
                      "quelque chose à l'objection avant d'y répondre, il "
                      "appuie chaque jugement sur un moment précis, il emploie "
                      "« bien que » avec le subjonctif et « même si » avec "
                      "l'indicatif, et il pose une hypothèse avec « si » suivi "
                      "de l'imparfait.",

    # L'apostrophe s'échappe : les deux valeurs sont injectées dans la même
    # chaîne JavaScript à guillemets simples.
    'bravo': "🎉 Bravo, vous avez terminé le module "
             "« Ce que j\\'en pense, et pourquoi » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
