# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 60 min. Dernière séance du module.
Source : dialogue `appli`, jeu de rôle `guichet`, exercices `aQui`, `aMoi`,
productions orale et écrite.

Séance de production. Rien de neuf n'y est introduit — sauf un renversement :
dans le dernier dialogue, c'est Amadou qui explique le guichet à Leïla. Celui
qui disait « c'est ma première fois » à la séance A1 est maintenant celui qui
renseigne. C'est la mesure du chemin parcouru, et il faut la dire au groupe.

La séance ferme aussi le module sur les mots : le bloc « Je retiens des mots »
n'a pas de séance à lui dans le format court, il se révise ici.
"""
import os

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-guichet/images/')


def _photo(nom):
    """La photo si elle est sur le disque, sinon rien. Voir `a1.py`."""
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Je me lance",
        chapeau="Expliquer un retrait de vive voix, une étape à la fois, "
                "puis écrire un court message sur ce qu'on a fait à la "
                "caisse.",
        duree='60 minutes')

    d.titre(notes="Dernière séance du module. Rendre les chèques de la séance C2 au "
                  "début : les élèves voient ce qu'ils ne savaient pas faire il y a deux "
                  "semaines. La moitié du temps se passe en production réelle ; les "
                  "diapositives ne sont qu'un cadre.")

    d.objectifs([
        "expliquer un retrait à quelqu'un, étape par étape ;",
        "demander de l'aide au guichet sans gêne ;",
        "s'enregistrer et s'écouter ;",
        "écrire un court message sur ce qu'on a fait à la caisse.",
    ])

    d.declencheur(
        'Observation', "Sauriez-vous expliquer le guichet à quelqu'un ?",
        image=_photo('etape-releve.jpg'),
        pistes=[
            "Qu'est-ce qu'on met dans la machine, et dans quel ordre ?",
            "Qu'est-ce qu'on reprend avant de partir ?",
            "Que dire quand l'écran écrit « des frais » ?",
            "Que faire si la carte reste dans la machine ?",
        ],
        notes="Quatre questions, quatre séances. Laisser répondre sans reprendre : le but "
              "est que le groupe s'entende savoir tout cela.")

    d.dialogue('Dialogue · 1 de 3', "Cette fois, c'est Amadou qui explique", [
        ("LEÏLA", "Amadou, tu m'aides ? Je n'ai jamais fait de retrait.", True),
        ("AMADOU", "Oui. Regarde : tu mets ta carte ici.", True),
        ("LEÏLA", "Après ?", True),
        ("AMADOU", "Tu tapes ton NIP. Quatre chiffres. Tu ne dis rien.", True),
    ], consigne="Écoutez, puis dites qui explique et qui demande.",
       notes="Faire remarquer le renversement : à la séance A1, c'est Amadou qui disait "
             "« c'est ma première fois ». Le dire au groupe en toutes lettres — c'est le "
             "moment de la séance qui reste.")

    d.dialogue('Dialogue · 2 de 3', "Tu choisis le montant", [
        ("LEÏLA", "Et pour l'argent ?", True),
        ("AMADOU", "Tu choisis « retrait », puis un montant. Vingt, quarante, soixante.", True),
        ("LEÏLA", "Moi, je veux soixante dollars.", True),
        ("AMADOU", "Alors tu appuies sur soixante. Trois billets de vingt.", True),
    ], notes="« Trois billets de vingt » : faire calculer à voix haute par le groupe. Le "
             "calcul dit en français vaut autant que le mot.")

    d.dialogue('Dialogue · 3 de 3', "Non ! Il reste trois choses", [
        ("LEÏLA", "Et c'est fini ?", True),
        ("AMADOU", "Non ! Tu prends ta carte, ton argent et ton relevé.", True),
    ], notes="La dernière réplique du module est celle qui évite la perte la plus "
             "fréquente : la carte oubliée dans la machine. La faire répéter par tout le "
             "groupe avant la production orale.")

    d.tableau('Analyse', "Ce qui revient de tout le module",
              ["Ce qu'on dit", "Vu en"],
              [["Bonjour. C'est ma première fois.", "A1"],
               ["Quarante dollars. C'est ça ?", "A2 et A3"],
               ["J'entre mon NIP. Je choisis le retrait.", "B1"],
               ["Je peux dire non aux frais.", "B2"],
               ["Quarante-cinq dollars, et je signe en bas.", "C1 et C2"]],
              cle=1,
              notes="Diapositive à photographier. Elle sert de révision de tout le module "
                    "en une page ; la laisser affichée pendant la production orale. Rien "
                    "de neuf : le module entier tient dans ces cinq lignes.")

    d.regle("Demander de l'aide n'est pas une faiblesse",
            "Plus lentement, s'il vous plaît. Sur quel bouton est-ce que j'appuie ?",
            precision="Ce sont les deux phrases qui servent le plus longtemps, bien "
                      "au-delà du hall des guichets. Une seule chose ne se demande "
                      "jamais et ne se dit jamais : le NIP.",
            notes="Diapositive à photographier. Le rappeler une dernière fois : personne "
                  "ne s'impatiente devant quelqu'un qui vérifie.")

    d.cartes("Trois situations pour le jeu de rôle", "Choisissez la vôtre", [
        ("Devant le guichet",
         "Vous voulez retirer quarante dollars. C'est votre première fois et vous "
         "n'êtes pas sûr de l'ordre des étapes."),
        ("L'écran parle de frais",
         "L'écran écrit « des frais de 3 $ ». Vous ne comprenez pas pourquoi, et vous "
         "voulez savoir si vous pouvez dire non."),
        ("La carte ne sort pas",
         "Vous avez votre argent, mais votre carte est restée dans la machine. Vous "
         "demandez de l'aide à l'employé du hall."),
    ], cols=3, notes="Ce sont les trois situations du jeu de rôle en ligne. L'assistant y "
                     "joue l'employé du hall : il répond lentement, une information à la "
                     "fois. Il ne demande jamais le NIP, et il ne faut jamais le donner.")

    d.pratique('Production orale', "Expliquez votre retrait",
               "Trois temps. Enregistrez-vous, écoutez-vous, recommencez.", [
        ("TEMPS 1", "Je mets ma carte dans le guichet. Je tape mon NIP. Je cache le clavier."),
        ("TEMPS 2", "Je choisis le retrait. J'appuie sur quarante dollars."),
        ("TEMPS 3", "Je prends ma carte, mon argent et mon relevé."),
    ], cols=1,
       notes="Vingt minutes. Laisser recommencer autant de fois qu'il le faut : c'est "
             "l'écoute de soi qui fait progresser, pas la première prise. Les sept sujets "
             "à couvrir sont listés dans le module en ligne.")

    d.pratique('Production écrite', "Écrivez ce que vous avez fait à la caisse",
               "Un court message à un ami, de quatre à six phrases.", [
        ("À écrire", "Le jour où vous êtes allé au guichet."),
        ("À écrire", "Le montant retiré, en dollars."),
        ("À écrire", "Ce que vous avez pris avant de partir."),
        ("À écrire", "Comment vous avez payé : chèque, carte ou comptant."),
    ], cols=1,
       notes="Vingt minutes. Rappeler les deux choses qui seront regardées : le montant "
             "écrit à la façon d'ici, et le verbe entier après « je peux » et « je "
             "dois ». Le reste se corrige plus tard.")

    d.vocabulaire('Je retiens des mots', "Les cinq mots du guichet", [
        ("un NIP", "Les quatre chiffres secrets de ta carte."),
        ("un retrait", "Quand tu prends de l'argent dans ton compte."),
        ("un dépôt", "Quand tu mets de l'argent dans ton compte."),
        ("un relevé", "Le petit papier qui dit ce qui reste dans ton compte."),
        ("des frais", "L'argent en plus qu'on paie pour une opération."),
    ], notes="Dernière révision du module. Les seize mots complets sont dans les cartes "
             "mémoire en ligne, section « Je retiens des mots ».")

    d.billet(
        "Allez au guichet cette semaine, et expliquez une étape en français à quelqu'un.",
        exemples=[
            "Je mets ma carte, et je tape mon NIP.",
            "Je choisis le retrait.",
            "Je prends ma carte avant mon argent.",
        ],
        notes="Dernier devoir du module. Demander de raconter à la séance suivante ce qui "
              "s'est passé — ce qui a marché, et ce qui a été trop vite. C'est le retour "
              "qui compte, pas la réussite.")

    return d.save(dossier)
