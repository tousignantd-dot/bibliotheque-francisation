# -*- coding: utf-8 -*-
"""Identité de module-n5-actualite — « Raconter une nouvelle » (niveau 5).

La situation du programme est « Suivi de l'actualité », domaine général de
formation « Culture et médias ». `build/cadre.py 5 "Suivi de l'actualité"`
rend le cadre le plus étroit de tout le niveau : **une seule intention de
communication**, en compréhension écrite — « Comprendre un fait divers dans un
journal ». Ni compréhension orale, ni production, ni lexique rattaché.

C'est donc le reste du cadre qui a décidé de la forme du module. Les attentes
de fin de cours du niveau 5 disent que l'adulte « rapporte le sens général des
propos de quelqu'un au présent en employant les pronoms et les déterminants
appropriés » et qu'il emploie « le passé composé et l'imparfait pour relater
des évènements ». Le savoir de lexique rattaché à la lecture d'un fait divers
donne les deux champs à couvrir : les actes criminels et les catastrophes
naturelles. De là les trois défis : ce qui est arrivé, ce que les gens ont
dit, ce que j'en pense. La lecture n'est qu'un point de départ ; tout le
travail du module est de **restituer** ce qu'on a lu à quelqu'un qui ne l'a
pas lu, et de dire ce qu'on en pense.

Les voisins, et ce qui l'en sépare :

· `module-nouvelles` (activité 41, niveau 4) écoute le bulletin de nouvelles
  et répond à des questions de repérage — qui, quoi, où. Ici, personne ne pose
  de questions : l'élève parle d'un seul tenant à quelqu'un qui n'a rien lu, et
  c'est le silence de l'autre qui l'oblige à s'organiser.
· `module-n7-actualite` (activité 60, niveau 7) porte la même situation trois
  niveaux plus haut : il démêle le reportage, la chronique et l'éditorial, il
  distingue le fait de l'opinion dans un texte signé et il intervient dans un
  blogue. Ici il n'y a qu'un genre — le fait divers, cinq paragraphes dans un
  hebdomadaire de quartier — et l'opinion n'est pas à débusquer chez l'autre :
  elle est à formuler soi-même, à la fin, et à justifier.
· `module-n5-transport` (activité 69, même niveau) écoute un bulletin de
  circulation pour refaire son trajet du matin même. Là, l'information sert à
  décider tout de suite ; ici elle ne sert à rien d'autre qu'à être racontée.

Les faits du Québec sont vérifiés, jamais devinés : le Service de sécurité
incendie et le Service de police de Sherbrooke sont les services municipaux de
cette ville ; la Sûreté du Québec dessert les municipalités qui n'ont pas de
corps de police à elles ; la Croix-Rouge canadienne héberge et vêt les
sinistrés à la demande des municipalités ; Environnement Canada émet les
avertissements de pluie abondante et de verglas ; la rivière Magog et la
rivière Saint-François traversent Sherbrooke et se rejoignent au centre-ville ;
Info-Crime Québec reçoit les signalements anonymes. Les personnes, les rues,
les évènements et l'hebdomadaire « L'Écho des Cantons » sont inventés — un
fait divers attribué à un vrai journal serait une fausse nouvelle.
"""

MANIFESTE = {
    'slug': 'module-n5-actualite',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    # L'apostrophe est échappée : le thème est injecté dans une chaîne
    # JavaScript à guillemets simples, au moment du dépôt de la production
    # orale. Non échappée, elle ferme la chaîne et l'envoi meurt.
    'theme': "Suivi de l\\'actualité",

    # Sarcelle : la couleur du niveau 5. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#0D7A6F',
    'accent_doux': '#DCF2EF',

    'ia_oral': "L'élève raconte à quelqu'un qui ne l'a pas lu un fait divers "
               "paru dans son journal local : il dit d'abord ce qui est "
               "arrivé, puis où et quand, il place le déroulement au passé "
               "composé et le décor à l'imparfait, il rapporte au présent au "
               "moins une parole en disant de qui elle vient, et il termine "
               "par ce qu'il en pense, présenté comme une opinion et justifié. "
               "Il tutoie son interlocuteur.",

    'jr_cas': 'incendie',
    'jr_role': 'sylvain',
    'jr_scenario': 'faitdivers',
    'ia_jeu_de_role': "L'élève raconte un fait divers à quelqu'un qui ne l'a "
                      "pas lu : il dit ce qui est arrivé, où et quand, il "
                      "rapporte ce que les gens ont déclaré en nommant qui "
                      "parle, puis il donne son avis et le défend quand son "
                      "interlocuteur n'est pas d'accord.",

    'bravo': "🎉 Bravo, tu as terminé le module « Raconter une nouvelle » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
