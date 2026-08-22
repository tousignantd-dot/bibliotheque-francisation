# -*- coding: utf-8 -*-
"""C5 · Si, et les sept parties du courriel
Bloc C « Défi 2 · L'avis et la réponse » · couleur ambre · 90 min. Bilan du défi.
Source : exercices `t2si` (dialogue `t2b`) et `t2courriel`, leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C5', section='ambre',
        titre="Si, et les sept parties du courriel",
        chapeau="Toute la fin du dossier tient dans des hypothèses. Et tout "
                "ce qu'on en écrit tient dans sept parties, toujours les "
                "mêmes.",
        duree='90 minutes')

    d.titre(notes="Dernière séance avant le bloc E. Elle donne les deux outils de la "
                  "production : la phrase avec « si », qui permet de parler d'une "
                  "suite sans s'engager, et la forme du courriel.")

    d.objectifs([
        "employer « si » avec le présent, jamais avec le futur ;",
        "choisir entre présent, futur et impératif dans la suite ;",
        "distinguer le « si » de condition du « si » de question ;",
        "nommer les sept parties d'un courriel formel.",
    ], notes="Le premier objectif est la faute la plus visible du niveau, et la plus "
             "facile à corriger : une leçon suffit si elle est faite pour vrai.")

    d.dialogue('Dialogue', "La visite, un samedi de novembre", [
        ("FARIDA", "Avant de faire le tour, je veux être claire : ce n'est pas une location, c'est une sous-location.", True),
        ("NICOLAS", "C'est-à-dire ?", True),
        ("FARIDA", "Le bail reste à mon nom. Si vous ne payez pas, c'est moi que le propriétaire va poursuivre. Alors je vais demander des références, et je vais les appeler.", True),
        ("NICOLAS", "Et si monsieur Tardif ne répond pas ?", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Ce dialogue n'a pas de section à lui dans le module : il est porté par "
             "l'exercice interactif sur « si ». Le faire écouter en entier avant de "
             "projeter, il ne dure pas deux minutes.")

    d.tableau('Analyse', "Après « si », le présent. Ensuite, trois choix",
              ['La suite', 'Exemple'],
              [["présent", "s'il ne répond pas, il est réputé avoir consenti"],
               ["futur", "si vous donnez vos références, je les appellerai"],
               ["impératif", "si vous voulez une preuve, faites signer la copie"],
               ["jamais", "si vous ne paierez pas — le futur est interdit"]],
              cle=0,
              notes="Diapositive à photographier. Le choix de la suite change le ton, "
                    "pas le sens : le présent constate, le futur promet, l'impératif "
                    "conseille.")

    d.regle("Jamais de futur après le « si » de condition",
            "Le verbe qui suit « si » reste au présent, quoi qu'il arrive après.",
            precision="C'est la faute qui se remarque le plus vite, et elle se "
                      "corrige en une leçon. Attention à l'autre « si », celui qui "
                      "veut dire « oui ou non » : « je ne sais pas s'il répondra » "
                      "est correct, parce que ce n'est pas une condition. Le test : "
                      "peut-on remplacer par « dans le cas où » ?",
            notes="Diapositive à photographier. Faire le test à voix haute sur trois "
                  "phrases, dont une du second type. Le test tranche en une seconde et "
                  "il se retient.")

    d.pratique('Pratique', "Le verbe après « si »",
               "Écrivez la forme qui convient.", [
        ("Si monsieur Tardif ne … (répondre) pas, il a consenti.", "répond"),
        ("Si vous ne payez pas, c'est moi que le locateur … (poursuivre).", "poursuivra"),
        ("Si le refus … (être) motivé, la sous-location ne se fait pas.", "est"),
        ("Si vous … (vouloir) une preuve, faites signer la copie.", "voulez"),
        ("Si le locateur … (exiger) des frais, il doit dire lesquels.", "exige"),
        ("Je ne sais pas s'il … (répondre) avant mardi.", "répondra"),
    ], corrige=True,
       notes="La dernière ligne est le contre-exemple : ce « si » n'est pas une "
             "condition, et le futur y est permis. Ne pas la corriger comme une faute "
             "si un élève écrit « répond » — expliquer la différence.")

    d.tableau('Écriture', "Les sept parties, dans l'ordre",
              ['La partie', 'Ce qu\'on y met'],
              [["l'objet", "cinq ou six mots, sans verbe conjugué"],
               ["l'appel", "le nom de la personne, puis une virgule"],
               ["les trois paragraphes", "pourquoi j'écris, les faits, ma demande"],
               ["la signature", "nom, logement, moyen de vous joindre"]],
              cle=0,
              note="La salutation ferme le message, sans familiarité.",
              notes="Diapositive à photographier. Les trois paragraphes du milieu "
                    "comptent pour trois parties : les compter à voix haute pour "
                    "arriver à sept.")

    d.cartes('Ton', "Ferme et poli en même temps", [
        ("La demande au conditionnel", "« Pourriez-vous me confirmer par écrit… » Le conditionnel ne dit pas que vous doutez : il laisse à l'autre la place de répondre."),
        ("L'obligation impersonnelle", "« Il faut que votre réponse soit écrite » passe mieux que « vous devez me répondre », et dit exactement la même chose."),
        ("La source citée", "« Selon la page du Tribunal… » plutôt que « la loi dit ». Vous rapportez, vous ne tranchez pas."),
        ("L'avis annoncé", "« À mon avis, ce motif ne regarde pas monsieur Trudel. » Trois mots, et l'affirmation devient une opinion discutable."),
    ], notes="Ces quatre tournures sont exactement ce que la correction par l'IA "
             "cherchera dans le texte de E2. Le dire : ce n'est pas un caprice de "
             "style, c'est la grille.")

    d.piege('Attention',
            "trois sujets dans le même message",
            "un message, un sujet",
            "L'avis, les frais et la fenêtre du salon qui ferme mal : trois "
            "courriels. Un message à trois sujets reçoit une réponse à un "
            "seul, et c'est toujours celui qui vous intéresse le moins.",
            notes="Terminer là-dessus. C'est la consigne la plus concrète du bloc, et "
                  "elle vaut pour tous les écrits administratifs de leur vie.")

    d.billet(
        "Écrivez la dernière phrase de votre courriel : votre demande, au conditionnel, avec une date.",
        exemples=[
            "Une seule phrase.",
            "« Pourriez-vous… d'ici le… »",
        ],
        notes="Cinq minutes. Ces phrases se recopient directement dans le courriel de "
              "E2 : le dire aux élèves, ils écrivent mieux quand ils savent que ça "
              "servira.")

    return d.save(dossier)
