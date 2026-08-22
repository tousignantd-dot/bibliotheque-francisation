# -*- coding: utf-8 -*-
"""B1 · Fanta pousse la porte.
Bloc B « Défi 1 · Est-ce que vous engagez ? » · couleur acier · 75 min.
Source du module : dialogue `t1`, exercice `t1vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Fanta pousse la porte',
        chapeau="La conversation entière tient en seize répliques : elle "
                "entre, elle demande, elle dit ce qu'elle sait faire, elle "
                "laisse son numéro. C'est le modèle du défi.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Commencer par vérifier le devoir de A4 : qui a "
                  "dit ses quatre phrases à voix haute, et devant qui ?")

    d.objectifs([
        "suivre une conversation d'embauche du début à la fin ;",
        "repérer les quatre renseignements dans le dialogue ;",
        "comprendre les questions que pose un patron ;",
        "reconnaître ce qui se demande et ce qui se donne.",
    ])

    d.declencheur(
        'Anticipation', "Le patron va poser trois questions. Lesquelles ?",
        pistes=[
            "Qu'est-ce qu'il a besoin de savoir avant tout ?",
            "Est-ce qu'il va demander votre âge ? votre pays ?",
            "Qu'est-ce qu'il ne demandera pas ?",
            "Qu'est-ce qu'il ne dira pas si vous ne le demandez pas ?",
        ],
        notes="Noter les hypothèses au tableau avant d'écouter, puis les cocher pendant "
              "le dialogue. Elles sont presque toujours plus longues que la réalité.")

    d.dialogue('Dialogue · 1 de 3', "Est-ce que vous engagez encore ?", [
        ("FANTA", "Bonjour, monsieur. Excusez-moi de vous déranger.", True),
        ("GILLES", "Bonjour. Je peux vous aider ?", True),
        ("FANTA", "J'ai vu votre affiche dans la vitrine. Est-ce que vous engagez encore ?", True),
        ("GILLES", "Oui, on cherche quelqu'un. Vous avez déjà travaillé en boulangerie ?", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Trois répliques, et la conversation est ouverte. Faire compter : combien "
             "de mots a-t-il fallu à Fanta pour poser sa question ?")

    d.dialogue('Dialogue · 2 de 3', "Ce que je sais faire", [
        ("FANTA", "Non, jamais. Mais j'ai de l'expérience en ménage et en garde d'enfants.", True),
        ("GILLES", "Le poste, c'est commis au comptoir. Servir les clients, remplir les tablettes, nettoyer à la fermeture.", True),
        ("FANTA", "Le ménage, je sais faire. Servir les clients, je peux apprendre vite.", True),
        ("GILLES", "Vous êtes disponible quels jours ?", True),
    ], notes="Le « non, jamais » de Fanta est suivi d'un « mais ». C'est ce « mais » "
             "qui garde la porte ouverte : le faire remarquer et le faire répéter.")

    d.dialogue('Dialogue · 3 de 3', "Écrivez-le ici", [
        ("FANTA", "Du lundi au vendredi, le matin. Je suis à l'école de français l'après-midi.", True),
        ("GILLES", "Le matin, ça m'arrange. On ouvre à six heures et demie.", True),
        ("FANTA", "Fanta Traoré. F-A-N-T-A. Traoré : T-R-A-O-R-É.", True),
        ("GILLES", "Écrivez-le ici, sur le carnet. Je vous rappelle cette semaine.", True),
    ], notes="Elle épelle sans qu'on le lui demande, et elle demande à écrire son "
             "numéro. Ce sont deux gestes appris en A4 : les nommer.")

    d.tableau('Analyse', "Qui dit quoi, et dans quel ordre",
              ['Fanta donne', 'Gilles demande'],
              [["Pourquoi elle vient", "Si elle a de l'expérience"],
               ["Ce qu'elle sait faire", "Quels jours elle est libre"],
               ["Ses disponibilités", "Comment elle s'appelle"],
               ["Son nom, épelé", "Où la joindre"],
               ["Son numéro, écrit", "Rien de sa vie privée"]],
              cle=0,
              note="Cinq échanges. Personne ne parle de son pays, de son âge ni de sa famille.",
              notes="Diapo à photographier. La dernière ligne rassure : beaucoup "
                    "craignent des questions personnelles qui ne viendront pas.")

    d.regle("Le poste ne se décrit pas tout seul",
            "Le patron ne dit l'horaire et le salaire que si on les demande.",
            precision="Gilles ne parle de six heures et demie qu'au moment où Fanta "
                      "parle de disponibilités. Il ne dit jamais le salaire : personne "
                      "ne le lui a demandé. Ce qu'on ne demande pas, on l'apprendra "
                      "trop tard.",
            notes="Diapo à photographier. Elle prépare B4 et le jeu de rôle de E1, où "
                  "l'assistant est fait pour ne rien donner d'avance.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Gilles cherche encore quelqu'un.", "vrai"),
        ("Fanta a déjà travaillé en boulangerie.", "faux — jamais"),
        ("Le poste, c'est commis au comptoir.", "vrai"),
        ("Fanta est disponible l'après-midi.", "faux — elle est à l'école"),
        ("La boulangerie ouvre à six heures et demie.", "vrai"),
        ("Fanta laisse son numéro par écrit.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la réplique exacte. Les six énoncés "
             "sont ceux de l'exercice t1vf du module.")

    d.pratique('Reconstitution', "Remettez la conversation dans l'ordre",
               "Six répliques mêlées. Quel est leur ordre ?", [
        ("Bonjour, monsieur. Excusez-moi de vous déranger.", "1"),
        ("J'ai vu votre affiche. Est-ce que vous engagez encore ?", "2"),
        ("J'ai de l'expérience en ménage et en garde d'enfants.", "3"),
        ("Du lundi au vendredi, le matin.", "4"),
        ("Fanta Traoré. T-R-A-O-R-É.", "5"),
        ("Vous pouvez me joindre au 438 555-0192.", "6"),
    ], corrige=True,
       notes="Faire jouer la suite à deux, debout, une fois l'ordre trouvé. C'est la "
             "première répétition du jeu de rôle de E1.")

    d.billet(
        "Écrivez la première phrase que vous direz en entrant.",
        exemples=[
            "Une seule phrase, celle qui dit pourquoi vous venez.",
            "Relisez-la à voix haute avant de la remettre.",
        ],
        notes="Deux minutes. Les phrases ramassées servent d'exemples en B2, sans "
              "nommer personne.")

    return d.save(dossier)
