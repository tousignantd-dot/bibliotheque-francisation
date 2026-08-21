# -*- coding: utf-8 -*-
"""D1 · L'étiquette d'entretien.
Bloc D « Défi 3 · L'étiquette et le paiement » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3entretien`, mini-leçon `t3entretien`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-vetements/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="L'étiquette d'entretien",
        chapeau="Dans le col, une petite étiquette de tissu porte quatre ou "
                "cinq dessins. Une seule règle suffit pour les lire tous : un "
                "dessin barré veut dire « ne pas faire ».",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 3. Faire chercher l'étiquette d'entretien dans "
                  "le vêtement que chacun porte : elle est presque toujours là.")

    d.objectifs([
        "trouver l'étiquette d'entretien sur un vêtement ;",
        "reconnaître cinq dessins et la règle du dessin barré ;",
        "comprendre la forme « ne pas + infinitif » ;",
        "savoir ce qui abîme la laine.",
    ])

    d.declencheur(
        'Observation', "Que disent ces dessins ?",
        image=IMG + 'pictogrammes-entretien.jpg',
        pistes=[
            "Combien y en a-t-il ?",
            "Lesquels sont barrés ?",
            "Que veut dire une croix sur un dessin ?",
            "Où trouve-t-on cette étiquette ?",
        ],
        notes="Laisser deviner. La règle du dessin barré se trouve toujours par le groupe "
              "lui-même : elle est visuelle, pas linguistique.")

    d.dialogue('Dialogue · 1 de 3', "Le bassin", [
        ("FARIDA", "Il y a une petite étiquette dans le col. Avec des dessins.", True),
        ("JOCELYNE", "C'est l'étiquette d'entretien. Elle dit comment laver le vêtement.", True),
        ("FARIDA", "Le premier dessin, c'est un petit bassin avec de l'eau.", True),
        ("JOCELYNE", "Ça veut dire : laver à la machine. Le chiffre dedans, c'est la température.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Le chiffre dans le bassin est pris pour un prix par beaucoup d'élèves. Le "
             "corriger tout de suite.")

    d.dialogue('Dialogue · 2 de 3', "Le carré et le triangle", [
        ("FARIDA", "Et le carré avec un rond dedans, barré ?", True),
        ("JOCELYNE", "Ne pas mettre à la sécheuse. Ce vêtement sèche à l'air.", True),
        ("FARIDA", "Et le triangle barré ?", True),
        ("JOCELYNE", "Ne pas javelliser. Le javellisant ferait des taches jaunes.", True),
    ], notes="Deux fois la même structure : dessin barré, « ne pas + infinitif ». Faire "
             "remarquer la répétition.")

    d.dialogue('Dialogue · 3 de 3', "La règle", [
        ("FARIDA", "C'est compliqué…", True),
        ("JOCELYNE", "Non : un dessin barré, c'est toujours « ne pas faire ». Gardez ça et vous comprendrez tout.", True),
    ], notes="La séance tient dans cette réplique. La faire répéter, et l'écrire au "
             "tableau avant de passer au tableau d'analyse.")

    d.tableau('Analyse', "Cinq dessins",
              ['Le dessin', 'Ce qu\'il dit'],
              [["un bassin d'eau", "laver — le chiffre donne la température"],
               ["un carré avec un rond", "la sécheuse"],
               ["un triangle", "le javellisant"],
               ["un fer", "le repassage"],
               ["un rond", "le nettoyage à sec, chez le nettoyeur"]],
              cle=0,
              note="Barré, chacun veut dire « ne pas faire ». C'est toute la règle.",
              notes="Diapo à photographier. Faire dessiner les cinq symboles dans le "
                    "carnet, avec et sans la croix.")

    d.regle("Ne pas + infinitif",
            "« Ne pas javelliser. » « Ne pas mettre à la sécheuse. »",
            precision="C'est la forme courte des consignes écrites : plus brève que « ne "
                      "javellisez pas », donc elle tient sur une étiquette. On la retrouve "
                      "partout — sur les portes, sur les machines, sur les médicaments. "
                      "La reconnaître sert bien au-delà du linge.",
            notes="Diapo à photographier. Faire chercher d'autres exemples affichés dans le "
                  "centre : « ne pas stationner », « ne pas déranger ».")

    d.cartes("Ce qui abîme le linge d'hiver", "Trois accidents fréquents", [
        ("La laine à l'eau chaude",
         "Le chandail rapetisse et ne revient jamais. Eau froide — trente degrés — et "
         "séchage à plat."),
        ("La sécheuse",
         "C'est ce qui abîme le plus. Un carré barré dans le col veut dire que le vêtement "
         "sèche à l'air, sur un séchoir ou à plat sur une serviette."),
        ("Le javellisant sur la couleur",
         "Il ne nettoie pas : il décolore. Des taches jaunes apparaissent, et elles ne "
         "partent plus."),
    ], notes="Ces trois accidents coûtent chaque année des vêtements neufs. Le dire "
             "concrètement, avec des prix.")

    d.piege("Couper l'étiquette",
            "Elle pique, je l'enlève.",
            "Prenez-la en photo avant de la couper.",
            "Six mois plus tard, plus personne ne sait comment laver le vêtement. La "
            "photo dans le téléphone règle le problème sans le désagrément — et elle se "
            "retrouve plus vite qu'une étiquette froissée dans un col.",
            notes="Conseil très pratique. Beaucoup d'élèves coupent l'étiquette dès le "
                  "premier jour.")

    d.pratique('Pratique · 1 de 2', "Vrai ou faux ?",
               "D'après le dialogue.", [
        ("L'étiquette d'entretien est dans le col.", "vrai"),
        ("Le bassin d'eau veut dire « laver à la machine ».", "vrai"),
        ("Le chiffre dans le bassin est le prix.", "faux — la température"),
        ("À l'eau chaude, la laine rapetisse.", "vrai"),
        ("Le carré barré veut dire « mettre à la sécheuse ».", "faux — ne pas mettre"),
        ("Un dessin barré veut toujours dire « ne pas faire ».", "vrai"),
    ], corrige=True,
       notes="Utiliser l'exercice 1 du défi 3.")

    d.pratique('Pratique · 2 de 2', "Complétez",
               "Que dit ce dessin ?", [
        ("Un dessin barré veut dire : ___ pas faire.", "ne"),
        ("Le chiffre 30 dans le bassin veut dire 30 ___ .", "degrés"),
        ("Le carré avec un rond parle de la ___ .", "sécheuse"),
        ("Le triangle barré veut dire : ne pas ___ .", "javelliser"),
        ("À l'eau chaude, la laine ___ .", "rapetisse"),
    ], corrige=True,
       notes="Utiliser l'exercice 2 du défi 3.")

    d.billet(
        "Photographiez l'étiquette d'entretien de deux vêtements.",
        exemples=[
            "Comptez les dessins et repérez ceux qui sont barrés.",
            "Écrivez ce que chacun veut dire.",
        ],
        notes="Devoir concret, faisable par tout le monde le soir même. Il donne des cas "
              "réels pour la séance suivante.")

    return d.save(dossier)
