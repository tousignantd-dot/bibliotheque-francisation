# -*- coding: utf-8 -*-
"""E2 · La demande écrite, et les seize mots
Bloc E « Je me lance » · couleur framboise · 75 min.
Production écrite, puis bilan du module.
Source du module : bloc « Je me lance » (la demande au conseiller) et
« Je retiens des mots ».
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-ecole/images/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="La demande écrite, et les seize mots",
        chapeau="Dernière séance. Vous écrivez à monsieur Gauthier pour "
                "demander un changement à votre dossier. Rien ne bouge tant "
                "que ce courriel n'est pas envoyé : c'est lui qui entre au "
                "dossier, pas la conversation d'hier.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Prévoir quarante minutes d'écriture en "
                  "silence, puis le bilan. Rendre au début les billets de E1 et les "
                  "rétroactions des productions orales : la comparaison est le vrai "
                  "moment d'apprentissage de la séance.")

    d.objectifs([
        "écrire une demande de sept à dix phrases ;",
        "dire ce qu'on demande avant de l'expliquer ;",
        "employer une phrase emphatique et une phrase au subjonctif ;",
        "faire le point sur ce qu'on est maintenant capable de faire.",
    ], notes="Le deuxième objectif est celui qui distingue une demande d'une "
             "plainte : la demande vient avant l'explication. C'est aussi ce que le "
             "correcteur regarde en premier.")

    d.declencheur(
        'Observation', "Pourquoi écrire, quand on a déjà parlé ?",
        image=img('babillard-avis.jpg'),
        pistes=[
            "Qu'est-ce qu'un dossier garde, et qu'est-ce qu'il ne garde pas ?",
            "Qui lira votre courriel, et combien en a-t-il devant lui ?",
            "Pourquoi garder une copie de ce qu'on envoie ?",
            "Combien de temps attend-on une réponse, d'habitude ?",
        ],
        notes="La première question est celle de tout le module : un dossier ne se "
              "souvient d'aucune conversation. La quatrième amène la question glissée "
              "sur le délai, qui doit se retrouver dans le courriel.")

    d.regle("On écrit à quelqu'un qui en a quarante autres devant lui",
            "Le motif de la lettre est dans la première phrase, pas dans la dernière.",
            precision="Sept à dix phrases, avec « vous ». Ce que vous demandez vient "
                      "avant l'explication ; une raison, pas trois — une lettre qui "
                      "accumule les explications se lit comme une excuse.",
            notes="Diapositive à photographier. Écrire au tableau deux premières "
                  "phrases, une qui commence par l'explication et une qui commence par "
                  "la demande, et faire choisir. Le groupe choisit la seconde.")

    d.tableau('Le courriel', "Sept exigences, annoncées d'avance",
              ["La partie", "Ce qu'on y met"],
              [["La première phrase", "salutation, votre nom, votre groupe"],
               ["La demande", "dite avant toute explication"],
               ["Une phrase emphatique", "ce qui me bloque, c'est…"],
               ["Une raison", "introduite par « Comme », en tête de phrase"],
               ["Une phrase au subjonctif", "il faut que… ou pour que…"],
               ["La fin", "une date d'effet, une question sur le délai, votre numéro"]],
              cle=1,
              notes="Six des sept points de la liste en ligne. Annoncer les critères "
                    "avant l'écriture, jamais après : un élève qui sait qu'on regarde "
                    "le subjonctif en écrit un ; celui qui l'apprend à la correction "
                    "se sent piégé.")

    d.cartes("Les trois défis, dans un seul courriel", "D'où vient chaque phrase", [
        ("Les dates avant le motif",
         "Défi 1 — à partir du 20 avril ; l'ordre du comptoir vaut aussi à l'écrit."),
        ("La question glissée",
         "Défi 1 — je voudrais savoir si… Elle ferme le courriel sans le durcir."),
        ("L'échéance et la reprise",
         "Défi 2 — une date d'effet, et « cette demande » plutôt que le mot répété."),
        ("L'emphase et le subjonctif",
         "Défi 3 — ce qui me bloque, c'est… ; pour que je puisse…"),
    ], notes="Diapositive à photographier. Le module entier tient dans ces quatre "
             "cartes, et la demande écrite est le seul endroit où les trois défis se "
             "rencontrent. Le dire au groupe avant l'écriture.")

    d.piege("Commencer par l'explication",
            "Depuis mon retour, ma vie a beaucoup changé et…",
            "Je vous écris pour demander un transfert au groupe du soir.",
            "Le premier courriel se lit dans l'ordre où les choses sont arrivées à "
            "celui qui l'écrit. Le second se lit dans l'ordre où elles intéressent "
            "celui qui le reçoit. L'explication vient après la demande, toujours.",
            notes="C'est la faute la plus fréquente de cette production, et elle n'est "
                  "pas une faute de langue : c'est une faute de destinataire. La "
                  "nommer ainsi aide les élèves à la voir.")

    d.vocabulaire('Bilan du vocabulaire', "Huit des seize mots, une dernière fois", [
        ("le secrétariat", "Le comptoir où l'on remet les papiers et où l'on s'inscrit."),
        ("une conseillère", "La personne qui décide des changements au dossier."),
        ("un motif", "La raison qu'on donne pour justifier une absence."),
        ("une pièce justificative", "Le papier qui prouve le motif : un billet, une lettre."),
        ("une échéance", "La date limite : après elle, la demande n'est plus reçue."),
        ("un transfert", "Le passage d'un groupe à un autre, sans changer de cours."),
        ("une attestation", "Le papier qui dit que vous êtes inscrit ici en ce moment."),
        ("un délai", "Le temps que prend une démarche avant d'aboutir."),
    ], notes="Huit des seize, ceux que le relevé montre comme les moins sûrs. Faire "
             "dire chaque mot avec son article et une phrase. Les huit autres se "
             "révisent avec les cartes mémoire de l'activité.")

    d.pratique('Bilan', "Êtes-vous maintenant capable de… ?",
               "Répondez pour vous-même, honnêtement.", [
        ("Savoir à quelle porte frapper dans un centre ?", "secrétariat ou conseiller"),
        ("Annoncer une absence prévue, dans l'ordre ?", "les dates avant le motif"),
        ("Glisser une question polie dans une phrase ?", "je voudrais savoir si…"),
        ("Trouver l'échéance d'un avis officiel ?", "une seule date sur trois"),
        ("Demander un changement sans vous plaindre ?", "nommer ce qui bloque"),
        ("Écrire une demande qui entre au dossier ?", "et en garder une copie"),
    ], corrige=True,
       notes="Faire cocher individuellement, sans ramasser. Proposer à ceux qui "
             "hésitent sur deux points ou plus de refaire le défi correspondant dans "
             "l'activité interactive : elle reste ouverte après la fin du module.")

    d.billet(
        "En une phrase : quelle démarche allez-vous faire cette semaine, et auprès de qui ?",
        exemples=[
            "Une vraie démarche, dans votre vraie vie.",
            "Gardez ce billet : c'est le seul du module qui ne se corrige pas.",
        ],
        notes="Ne pas ramasser celui-ci. Le module a commencé par une femme qui "
              "gardait sa nouvelle depuis trois jours sans oser demander ; il se "
              "termine par la même question, posée à chacun.")

    return d.save(dossier)
