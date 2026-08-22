# -*- coding: utf-8 -*-
"""C2 · « que, si, ce que »
Bloc C « Défi 2 · Ce que les gens ont dit » · couleur ambre · 75 min.
Source : exercice `t2que`, mini-leçon `t2que`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="« que, si, ce que »",
        chapeau="Trois mots de liaison, et rien d'autre. Une affirmation "
                "entre par « que ». Une question par oui ou non entre par "
                "« si ». Une question en « quoi » entre par « ce que » ou "
                "« ce qui ». Tout le discours rapporté du niveau 5 tient "
                "là-dedans.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire courte et rentable. Ouvrir en écrivant au "
                  "tableau trois phrases directes — une affirmation, une question "
                  "fermée, une question en « quoi » — et demander au groupe de les "
                  "rapporter. Les trois mots de liaison sortent tout seuls, ou "
                  "manquent visiblement.")

    d.objectifs([
        "choisir entre que, si, ce que et ce qui ;",
        "conserver les mots interrogatifs où, quand, comment, pourquoi ;",
        "supprimer le point d'interrogation et le « est-ce que » ;",
        "élider « que » devant une voyelle.",
    ], notes="Le troisième objectif est le plus visible à la correction : un point "
             "d'interrogation qui survit à la transformation signale que l'élève a "
             "recopié au lieu de rapporter.")

    d.regle("Une affirmation entre par « que »",
            "« L'enquête se poursuit. » devient : le porte-parole dit que "
            "l'enquête se poursuit.",
            precision="Devant une voyelle, que devient qu' : il dit qu'on ne sait "
                      "pas encore. C'est la liaison la plus fréquente des trois, et "
                      "celle qui sert dans neuf phrases sur dix.",
            notes="Diapositive à photographier. Faire produire cinq phrases en "
                  "« dit que » à partir des déclarations du dialogue de C1 avant de "
                  "passer à la suivante.")

    d.regle("Une question par oui ou non entre par « si »",
            "« Est-ce que la rue rouvrira demain ? » devient : la "
            "résidente demande si la rue rouvrira demain.",
            precision="Attention : si ne devient jamais s' devant elle, seulement "
                      "devant il et ils. On écrit « demande si elle va venir », et "
                      "« demande s'il va venir ».",
            notes="La précision sur l'élision est un point d'écrit pur. La donner, la "
                  "faire écrire, ne pas s'y attarder : elle se règle par l'exercice, "
                  "pas par l'explication.")

    d.tableau('Les trois portes', "La phrase de départ décide du mot de liaison",
              ['La phrase directe', 'Ce qu\'elle devient'],
              [["« Nous avons distribué des sacs. »", "La Ville dit qu'elle a distribué des sacs."],
               ["« Allez-vous refaire le fossé ? »", "Elle demande si la Ville va refaire le fossé."],
               ["« Que faites-vous ? »", "On demande ce que la Ville fait."],
               ["« Qu'est-ce qui a causé le feu ? »", "On demande ce qui a causé le feu."],
               ["« Quand refera-t-on le fossé ? »", "Elle demande quand on refera le fossé."]],
              cle=1,
              notes="Faire cacher la colonne de droite et transformer oralement. La "
                    "cinquième ligne montre que les mots interrogatifs se recopient "
                    "tels quels : rien à traduire.")

    d.cartes("ce qui, ou ce que ?", "La différence tient au sujet", [
        ("ce qui",
         "Quand la suite n'a pas de sujet à elle : on demande ce qui a causé le feu."),
        ("ce que",
         "Quand la suite a déjà son sujet : on demande ce que la Ville fait."),
        ("Le test",
         "Après « ce qui », un verbe. Après « ce que », un sujet, puis un verbe."),
        ("Les mots qui restent",
         "où, quand, comment, pourquoi, combien : on les recopie sans rien changer."),
    ], notes="Le test de la troisième carte règle presque tous les cas. Le faire "
             "appliquer à voix haute sur les deux premières lignes du tableau "
             "précédent avant l'exercice.")

    d.pratique('Écriture', "Le bon mot de liaison",
               "Complétez avec que, qu', si, ce que ou ce qui.", [
        ("Le porte-parole dit ___ l'enquête se poursuit.", "que"),
        ("La résidente demande ___ la Ville va refaire le fossé.", "si"),
        ("Sylvain demande ___ les pompiers ont trouvé dans le sous-sol.", "ce que"),
        ("Le journal écrit ___ on ne connaît pas encore la cause.", "qu'"),
        ("Teresa demande ___ a causé l'inondation.", "ce qui"),
        ("Marisol explique ___ la Croix-Rouge héberge les sinistrés.", "que"),
    ], corrige=True,
       notes="Exercice t2que de l'activité interactive. La quatrième vérifie "
             "l'élision, la cinquième le test « ce qui / ce que ». Les corriger en "
             "faisant redire la phrase directe de départ.")

    d.piege("Garder le point d'interrogation",
            "Elle demande si la Ville va refaire le fossé ?",
            "Elle demande si la Ville va refaire le fossé.",
            "Une parole rapportée n'est plus une question : c'est un récit. Le point "
            "d'interrogation, l'inversion et le « est-ce que » disparaissent tous les "
            "trois en même temps.",
            notes="Faute d'écrit très fréquente, et facile à repérer à la relecture. "
                  "Donner la consigne de relecture : chercher les points "
                  "d'interrogation et vérifier qu'il y a bien une vraie question.")

    d.piege("Employer « si » pour une affirmation",
            "Il dit si l'enquête se poursuit.",
            "Il dit que l'enquête se poursuit.",
            "« Si » n'entre que par une question à laquelle on répond par oui ou par "
            "non. Devant une affirmation, c'est toujours « que ». Le verbe "
            "d'introduction aide : on ne « dit » pas si, on « demande » si.",
            notes="Faire remarquer l'indice pratique : « demander » appelle « si », "
                  "« dire », « expliquer », « raconter » appellent « que ». Ce n'est "
                  "pas une règle absolue, mais c'est un bon réflexe.")

    d.billet(
        "Rapportez trois paroles : une affirmation, une question fermée, une question en « quoi ».",
        exemples=[
            "Trois phrases, chacune avec son mot de liaison.",
            "Vérifiez qu'aucune ne finit par un point d'interrogation.",
        ],
        notes="Ramasser. La troisième phrase est celle qui manque le plus souvent : "
              "prévoir d'en reprendre deux ou trois en ouverture de C3.")

    return d.save(dossier)
