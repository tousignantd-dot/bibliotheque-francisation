# -*- coding: utf-8 -*-
"""C3 · Décrire avec qui, que, où.
Bloc C « Défi 2 · La visite » · couleur ambre · 75 min.
Source : exercice `t2relatifs` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Décrire avec qui, que, où",
        chapeau="« C'est une chambre. Elle donne sur la cour. Elle est "
                "tranquille. » Trois petites phrases sèches — ou une seule "
                "phrase d'adulte.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Les relatifs sont le savoir qui fait le plus "
                  "monter le niveau apparent d'une production orale : trois mots, et une "
                  "description change de registre.")

    d.objectifs([
        "employer « qui » quand le verbe suit directement ;",
        "employer « que » quand un sujet suit ;",
        "employer « où » pour un lieu et pour un moment ;",
        "savoir que « qui » ne s'élide jamais.",
    ])

    d.declencheur(
        'Observation', "Comment dire ces trois phrases en une seule ?",
        pistes=[
            "« C'est une chambre. Elle donne sur la cour. »",
            "« C'est la pièce. Tout le monde l'aime. »",
            "« C'est la chambre. Ma fille y dormira. »",
            "Quel petit mot faut-il, chaque fois ?",
        ],
        notes="Écrire les trois paires au tableau. Le groupe trouvera souvent « qui » "
              "partout. Ne pas corriger : le tableau suivant montre pourquoi ce n'est pas "
              "le même mot dans les trois cas.")

    d.tableau('Les trois relatifs', "Regardez ce qui suit le petit mot",
              ['Ce qui suit', 'Le relatif'],
              [["un verbe, sans autre sujet", "QUI — les fenêtres qui donnent au sud"],
               ["un sujet, puis un verbe", "QUE — la pièce que tout le monde aime"],
               ["un lieu", "OÙ — l'immeuble où elle habite"],
               ["un moment", "OÙ — l'année où le loyer a monté"]],
              cle=0,
              note="Ce qui décide, c'est la place dans la phrase — jamais le sens du mot d'avant.",
              notes="Diapositive à photographier. La note du bas est capitale : les élèves "
                    "croient presque tous que « qui » sert pour les personnes.")

    d.regle("« qui » ne veut pas dire « une personne »",
            "On dit « les fenêtres qui donnent au sud ».",
            precision="« qui » remplace le sujet du verbe qui suit, que ce sujet soit une "
                      "personne, une fenêtre ou une remise. C'est la place dans la phrase "
                      "qui décide, pas ce qu'on désigne.",
            notes="Diapositive à photographier. C'est l'erreur de raisonnement la plus "
                  "répandue, et elle vient souvent d'une comparaison avec l'anglais "
                  "who / which.")

    d.cartes("Deux astuces de vérification", "À faire dans sa tête", [
        ("Remplacez par « elle » ou « il »",
         "« Les fenêtres — ELLES donnent au sud. » Ça marche ? C'est QUI."),
        ("Remplacez par « la » ou « le »",
         "« La pièce — tout le monde L'aime. » Ça marche ? C'est QUE."),
        ("Cherchez un sujet",
         "Entre le relatif et le verbe : s'il y a quelqu'un, c'est QUE."),
        ("Pour « où », demandez : un lieu ou un moment ?",
         "L'immeuble où… · l'année où… · le jour où…"),
    ], notes="Faire appliquer les deux premières astuces sur les phrases du déclencheur. "
             "Elles fonctionnent à tous les coups et se font en une seconde.")

    d.piege("Élider « qui »",
            "le logement qui'est libre",
            "le logement qui est libre",
            "« que » s'élide en « qu' » devant une voyelle : le logement qu'elle visite. "
            "« qui » ne s'élide jamais, dans aucun cas. Si vous voyez « qu' », c'était "
            "forcément « que ».",
            notes="Cette règle donne aussi un outil de correction : en relisant, tout "
                  "« qu' » doit pouvoir se remplacer par « que ».")

    d.pratique('Application', "qui, que ou où ?",
               "Complétez chaque phrase.", [
        ("C'est la pièce … tout le monde aime.", "que — « tout le monde » est sujet"),
        ("Les fenêtres … donnent au sud gardent le salon clair.", "qui — le verbe suit"),
        ("C'est la chambre … ma fille dormira.", "où — un lieu"),
        ("Le logement … elle a visité jeudi est plus grand.", "qu' — élision de « que »"),
        ("Un immeuble … n'est pas insonorisé se remarque le soir.", "qui"),
        ("La remise … se trouve derrière la porte prend deux vélos.", "qui"),
        ("C'est l'année … le loyer n'a pas augmenté.", "où — un moment"),
        ("Le prix … elle paie comprend le stationnement.", "qu' / que"),
    ], corrige=True,
       notes="Faire dire l'astuce employée à chaque fois, à voix haute. Le raisonnement "
             "compte plus que la réponse.")

    d.pratique('Production', "Décrivez une pièce avec chacun des trois",
               "Trois phrases sur le logement de votre choix.", [
        ("Avec « qui »", "C'est la chambre qui donne sur la cour."),
        ("Avec « que »", "C'est la pièce que ma fille a choisie."),
        ("Avec « où »", "C'est la cuisine où la hotte fonctionne mal."),
    ], corrige=False,
       notes="Circuler et corriger à la volée. Faire lire trois productions à voix haute "
             "en fin de séance : entendre la différence avec les petites phrases sèches du "
             "déclencheur est ce qui installe la règle.")

    d.billet(
        "Décrivez votre logement en cinq phrases, avec au moins trois relatifs.",
        exemples=[
            "Un « qui », un « que », un « où ».",
            "Soulignez-les. Nous les vérifierons ensemble.",
        ],
        notes="Devoir d'écriture. Le soulignement force la conscience du choix, et rend la "
              "correction rapide.")

    return d.save(dossier)
