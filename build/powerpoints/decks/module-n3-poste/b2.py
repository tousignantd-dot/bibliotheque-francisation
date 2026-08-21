# -*- coding: utf-8 -*-
"""B2 · Les cinq questions du comptoir.
Bloc B « Défi 1 · Demander avant de choisir » · couleur ambre (écriture) · 75 min.
Source : mini-leçon `t1quest`, exercice `t1quest`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre='Les cinq questions du comptoir',
        chapeau="Combien, combien de temps, est-ce que, où, qu'est-ce que. "
                "Cinq mots de question, et toute une démarche tient debout.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire et d'écriture. Elle donne les outils que la "
                  "séance B1 a fait entendre. Écrire les cinq mots au tableau avant "
                  "de commencer et les laisser toute la séance.")

    d.objectifs([
        "choisir le bon mot de question selon la réponse attendue ;",
        "écrire cinq questions correctes avec « est-ce que » ;",
        "poser ces questions à voix haute sans hésiter ;",
        "reconnaître qui parle : la préposée ou le client.",
    ])

    d.tableau('Analyse · 1 de 2', "Les deux questions qui décident",
              ['Le mot', 'Ce qu\'on demande', 'La question complète'],
              [["Combien", "un prix", "Combien est-ce que ça coûte ?"],
               ["Combien de temps", "un délai", "Combien de temps est-ce que ça prend ?"]],
              cle=0,
              note="Elles vont toujours ensemble : un prix seul ne dit rien.",
              notes="Diapo à photographier. Faire poser les deux questions à la suite "
                    "par un élève différent, à voix haute.")

    d.tableau('Analyse · 2 de 2', "Les trois autres",
              ['Le mot', 'Ce qu\'on demande', 'La question complète'],
              [["Est-ce que", "un oui ou un non", "Est-ce que je peux payer par carte ?"],
               ["Où", "un endroit", "Où est-ce que je mets mon adresse ?"],
               ["Qu'est-ce que", "une chose", "Qu'est-ce que je dois écrire ?"]],
              cle=0,
              note="La réponse attendue décide du mot : un oui, un endroit, une chose.",
              notes="Diapo à photographier. Faire chercher au groupe une autre question "
                    "du bureau de poste pour chacun des trois mots.")

    d.regle("Les deux questions à ne jamais oublier",
            "Combien est-ce que ça coûte ? Combien de temps est-ce que ça prend ?",
            precision="Elles vont toujours ensemble, parce qu'un prix seul ne veut "
                      "rien dire : vingt-deux dollars est cher pour un envoi qui "
                      "prend deux semaines, et bon marché pour un envoi qui prend "
                      "deux jours.",
            notes="Diapo à photographier. Faire répéter les deux questions à la suite, "
                  "comme une seule phrase : c'est ainsi qu'elles se disent au comptoir.")

    d.cartes("Trois façons de poser la même question", "Le prix", [
        ("Combien est-ce que ça coûte ?",
         "La forme complète, la plus claire. C'est celle qu'on apprend, et personne "
         "ne trouve jamais qu'elle fait trop scolaire."),
        ("Ça coûte combien ?",
         "La forme courante à l'oral, au Québec comme ailleurs. Le mot de question "
         "passe à la fin, et la voix monte."),
        ("C'est combien ?",
         "La plus courte. Elle marche partout, mais elle ne dit pas de quoi on "
         "parle : à employer quand on montre l'objet du doigt."),
        ("Et pour l'autre service ?",
         "La question de relance, quand la préposée a nommé un seul prix. "
         "Trois mots, et vous obtenez la comparaison."),
    ], notes="Les trois premières sont équivalentes. La quatrième est celle qui manque "
             "le plus souvent aux élèves : sans elle, on choisit sans comparer.")

    d.pratique('Écriture', "Quel mot de question ?",
               "Écrivez « combien », « combien de temps », « est-ce que », "
               "« où » ou « qu'est-ce que ».", [
        ("___ est-ce que ça coûte, pour Calgary ?", "combien"),
        ("___ est-ce que ça prend pour se rendre ?", "combien de temps"),
        ("___ je peux payer par carte de débit ?", "est-ce que"),
        ("___ est-ce que j'écris mon adresse sur la boîte ?", "où"),
        ("___ il faut apporter pour ramasser un colis ?", "qu'est-ce que"),
        ("___ vous pouvez répéter, s'il vous plaît ?", "est-ce que"),
    ], corrige=True,
       notes="C'est l'exercice `t1quest` du module interactif. Le faire d'abord sur la "
             "fiche, puis à l'écran. La dernière ligne reprend la formule de la "
             "séance A4 : la faire remarquer.")

    d.piege(
        "Ordre des mots",
        "Ça prend combien de temps ça ?",
        "Combien de temps est-ce que ça prend ?",
        "Le mot de question se met au début, et « est-ce que » vient tout de suite "
        "après. À l'oral rapide, on entend souvent la première forme, mais elle "
        "n'aide personne à se faire comprendre quand on débute.",
        notes="Ne pas condamner la forme orale : la nommer, dire qu'elle existe, et "
              "expliquer pourquoi on apprend l'autre d'abord.")

    d.pratique('À l\'oral', "Qui dit cette phrase ?",
               "La préposée derrière le comptoir, ou le client ?", [
        ("Il va où, votre colis ?", "la préposée"),
        ("Je voudrais envoyer ce colis, s'il vous plaît.", "le client"),
        ("Qu'est-ce qu'il y a dans la boîte ?", "la préposée"),
        ("Combien de temps est-ce que ça prend ?", "le client"),
        ("Le repérage est compris dans les deux services.", "la préposée"),
        ("Est-ce que vous pouvez répéter le prix ?", "le client"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice `t1qui` du module, où les phrases s'écoutent. Le faire "
             "ici à la voix : lire chaque phrase et laisser le groupe répondre à main "
             "levée, puis justifier.")

    d.billet(
        "Écrivez les deux questions que vous poserez la prochaine fois, avant de choisir.",
        exemples=[
            "Une pour le prix, une pour le délai.",
            "Écrivez-les en entier, avec « est-ce que ».",
        ],
        notes="Deux minutes. Corriger seulement l'ordre des mots : c'est le seul point "
              "de la séance qui doit être acquis avant B3.")

    return d.save(dossier)
