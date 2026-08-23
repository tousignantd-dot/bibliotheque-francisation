# -*- coding: utf-8 -*-
"""C2 · Ce que dit la lettre de refus
Bloc C « Défi 2 · L'appel qui conteste » · couleur ambre · 75 min.
Source : exercice `t2lettre`, de type `texte`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Une page pour un dossier de quatre",
        chapeau="Une lettre de refus est un résumé. Tout ce qu'elle affirme "
                "s'appuie sur des documents qu'elle ne joint pas — et elle "
                "contient, en petit, la seule partie qui vous soit utile.",
        duree='75 minutes')

    d.titre(notes="Deuxième séance de compréhension écrite du module. Prévoir la "
                  "lettre projetée et une copie papier par équipe. Comme en B2 : "
                  "crayon en main.")

    d.objectifs([
        "repérer la disposition invoquée dans une lettre de refus ;",
        "trouver le mot qui décide, au milieu d'un paragraphe ;",
        "lire le paragraphe des recours, celui que personne ne lit ;",
        "distinguer l'absence de protection de l'application d'une exclusion.",
    ], notes="Le troisième objectif est celui qui a le plus d'effet hors de la classe : "
             "toute lettre de refus contient sa propre suite.")

    d.declencheur(
        'Lecture', "Lisez la lettre en entier. Quel paragraphe vous est utile ?",
        pistes=[
            "Lequel annonce la décision ?",
            "Lequel donne le motif ?",
            "Lequel vous dit quoi faire maintenant ?",
            "Lequel est écrit le plus petit ?",
        ],
        notes="Les deux dernières questions donnent la même réponse, et c'est tout "
              "l'intérêt de la séance. Laisser le groupe le découvrir.")

    d.regle("Cherchez d'abord la disposition invoquée",
            "Un numéro d'article, un titre de clause. C'est ce qui "
            "transforme un refus en décision motivée, et ce qui vous dit "
            "quel texte aller lire.",
            precision="Une lettre qui dit seulement « votre demande est refusée » "
                      "n'est pas une décision motivée, et vous pouvez exiger par "
                      "écrit qu'elle le devienne. C'est un premier gain, et il ne "
                      "coûte qu'un courriel.",
            notes="Diapositive à photographier. Faire souligner « article 7.3 » dans "
                  "la copie papier, puis aller lire ce que l'article dit.")

    d.pratique('Compréhension écrite', "Où est-ce écrit ?",
               "Pour chaque question, citez le passage exact de la lettre.", [
        ("Quel numéro et quelle date faut-il rappeler dans toute réponse ?",
         "réclamation 2026-41837, sinistre du 14 septembre 2026"),
        ("Quel est le motif retenu, et sur quel tuyau porte-t-il ?",
         "défaut d'entretien du drain de plancher"),
        ("Quelle disposition du contrat est invoquée ?",
         "l'exclusion prévue à l'article 7.3"),
        ("Depuis quand l'avenant est-il en vigueur, et avec quelle franchise ?",
         "depuis le 1er juin 2023, franchise de 1 000 $"),
        ("Comment demander que la décision soit réexaminée ?",
         "une demande de révision écrite au service du traitement des plaintes"),
        ("Dans quel délai la réponse finale doit-elle arriver ?",
         "soixante jours suivant la réception de la demande"),
    ], corrige=True,
       notes="Exiger la citation exacte, pas la reformulation. C'est l'entraînement "
             "direct à la lettre du bloc E, où le motif se cite entre guillemets.")

    d.piege(
        'Réponse',
        "Envoyer ses papiers pour prouver qu'on est bien assuré",
        "Discuter l'exclusion, et elle seule",
        "La lettre reconnaît elle-même que l'avenant est au contrat : « ce "
        "n'est pas l'absence de protection qui fonde la présente décision ». "
        "Répondre là-dessus, c'est défendre un point que personne n'attaque, "
        "et perdre trois semaines. Le sujet est l'exclusion, et rien "
        "d'autre.",
        notes="C'est le piège le plus coûteux du module et il ne se voit pas : la "
              "réaction est naturelle et parfaitement inutile. Demander au groupe "
              "qui aurait fait ça — beaucoup de mains se lèvent.")

    d.tableau('Analyse', "Ce que chaque paragraphe fait",
              ['Le paragraphe', 'Son travail'],
              [["Objet : réclamation, sinistre", "rattacher la lettre à un dossier"],
               ["Nous ne pouvons donner suite", "annoncer, sans motif"],
               ["L'expertise conclut que…", "donner le motif — le mot qui décide est ici"],
               ["Visée par l'exclusion de l'article 7.3", "motiver la décision"],
               ["Vous pouvez adresser une demande…", "ouvrir la suite"]],
              cle=0,
              notes="Diapositive à photographier. Le dernier paragraphe est le seul "
                    "utile, et il est toujours en bas, en petit. Le dire aux élèves "
                    "vaut pour toutes les lettres de leur vie, pas seulement celle-ci.")

    d.regle("Notez la date de réception, pas celle de la lettre",
            "Les délais se comptent à partir du jour où la lettre vous "
            "parvient — et c'est vous qui devrez en faire la preuve.",
            precision="Le geste tient en trois secondes : écrire au crayon, sur la "
                      "lettre elle-même, le jour où on l'a sortie de la boîte. "
                      "Gardez aussi l'enveloppe.",
            notes="Diapositive à photographier. Petit geste, grande conséquence : sans "
                  "cette date, on plaide sur sa parole.")

    d.pratique('Vocabulaire', "Les mots de la lettre",
               "Complétez avec le mot exact.", [
        ("Le cas nommé au contrat pour lequel on ne paie pas : une ___.", "exclusion"),
        ("Le reproche de ne pas avoir entretenu : le ___ d'entretien.", "défaut"),
        ("La dernière position écrite de l'entreprise : une ___ finale.", "réponse"),
        ("Une décision qui dit sur quoi elle s'appuie est une décision ___.", "motivée"),
        ("La demande qu'on adresse pour faire réexaminer : une demande de ___.", "révision"),
    ], corrige=True,
       notes="Cinq mots, tous dans la lettre. Les faire retrouver dans la copie papier "
             "plutôt que de mémoire.")

    d.billet(
        "Relisez une lettre officielle que vous avez chez vous. Trouvez son paragraphe des recours.",
        exemples=[
            "Assurance, immigration, banque, école, employeur : n'importe laquelle.",
            "S'il n'y en a pas, écrivez-le : c'est un renseignement aussi.",
        ],
        notes="Devoir qui sort du module. Plusieurs élèves reviennent en disant qu'ils "
              "ne l'avaient jamais lu — c'est le but.")

    return d.save(dossier)
