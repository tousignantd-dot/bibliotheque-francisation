# -*- coding: utf-8 -*-
"""A1 · Un papier rouge dans la vitrine.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source du module : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre='Un papier rouge dans la vitrine',
        chapeau="Une affiche « On embauche » ne se répond pas par courriel. "
                "Elle se répond en poussant la porte. Encore faut-il savoir "
                "ce qu'elle dit, et ce qu'on va dire en entrant.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Demander d'abord au groupe qui a déjà "
                  "cherché du travail ici, et comment ça s'est passé. Les réponses "
                  "ouvrent la séance et donnent des exemples réels pour la semaine.")

    d.objectifs([
        "comprendre une affiche d'embauche ;",
        "nommer les mots du travail : un emploi, un métier, un patron ;",
        "savoir ce qu'on dit en entrant dans un commerce ;",
        "reconnaître le bon moment pour se présenter.",
    ])

    d.declencheur(
        'Observation', "Où avez-vous vu du travail affiché ?",
        pistes=[
            "Dans une vitrine ? Sur un babillard ?",
            "Est-ce que quelqu'un vous en a parlé ?",
            "Qu'est-ce qui était écrit sur le papier ?",
            "Est-ce que vous êtes entré ?",
        ],
        notes="Laisser venir les réponses dans n'importe quelle langue, puis les "
              "traduire ensemble au tableau. Beaucoup diront qu'ils ont vu et qu'ils "
              "ne sont pas entrés : c'est exactement ce que le module vient corriger.")

    d.dialogue('Dialogue · 1 de 3', "On embauche", [
        ("FANTA", "Sylvie, regardez. Il y a un papier dans la vitrine de la boulangerie.", True),
        ("SYLVIE", "« On embauche. » C'est écrit gros, en rouge. Vous savez ce que ça veut dire ?", True),
        ("FANTA", "Ça veut dire qu'ils cherchent quelqu'un ?", True),
        ("SYLVIE", "Exactement. Embaucher, c'est engager quelqu'un pour travailler.", False),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Fanta lit l'affiche et demande ce qu'elle veut dire. Souligner la "
             "question : « Qu'est-ce que ça veut dire ? » sert tout le module.")

    d.dialogue('Dialogue · 2 de 3', "Sans curriculum vitæ ?", [
        ("FANTA", "Mais moi, je n'ai pas de curriculum vitæ. Je n'ai jamais travaillé ici.", True),
        ("SYLVIE", "Pour une affiche comme celle-là, on n'en demande pas toujours. Vous entrez, et vous offrez vos services.", True),
        ("FANTA", "J'entre comme ça ? Sans rendez-vous ?", True),
        ("SYLVIE", "Sans rendez-vous. Vous saluez, vous dites pourquoi vous venez, et vous laissez votre nom.", True),
    ], notes="C'est le blocage le plus fréquent de la classe : croire qu'il faut un "
             "CV pour tout. Beaucoup de petits commerces n'en demandent pas.")

    d.dialogue('Dialogue · 3 de 3', "Pas à l'heure du dîner", [
        ("FANTA", "Je dis quoi, exactement ?", True),
        ("SYLVIE", "Trois choses. Ce que vous savez faire. Quand vous êtes libre. Où on peut vous joindre.", True),
        ("FANTA", "D'accord. Je vais essayer demain matin.", True),
        ("SYLVIE", "Le matin, c'est bien. Mais pas entre onze heures et deux heures : c'est l'heure du dîner, ils sont débordés.", True),
    ], notes="Le conseil sur l'heure est concret et sera réutilisé en E1. Demander au "
             "groupe à quelle heure sont calmes les commerces qu'ils connaissent.")

    d.tableau('Analyse', "Ce que dit l'affiche, et ce qu'elle ne dit pas",
              ["L'affiche dit", "Elle ne dit pas"],
              [["Qu'on cherche quelqu'un", "Quel poste exactement"],
               ["Que c'est encore ouvert", "Quel horaire"],
               ["Où se présenter : ici", "Combien de l'heure"],
               ["Souvent : demandez telle personne", "Si ça engage encore aujourd'hui"]],
              cle=0,
              note="Tout ce qui manque, c'est ce qu'on va demander en entrant.",
              notes="Diapo à photographier. Elle justifie tout le défi 1 : l'affiche "
                    "est un début de conversation, pas une description de poste.")

    d.regle("Ce qu'on dit en poussant la porte",
            "Bonjour. J'ai vu votre affiche. Est-ce que vous engagez ?",
            precision="Deux phrases, et la conversation est ouverte. La personne à qui "
                      "on parle est en train de travailler : elle n'a pas trois "
                      "minutes, mais elle a bien trente secondes.",
            notes="Diapo à photographier. Faire répéter les deux phrases à voix haute "
                  "par tout le groupe, deux fois, debout si le local le permet.")

    d.cartes("Les mots de l'affiche", "Quatre familles", [
        ("Le travail lui-même",
         "un emploi, un métier, un poste. « Emploi » est le mot général ; « métier » "
         "dit ce qu'on sait faire ; « poste » désigne la place à combler."),
        ("Les gens",
         "un patron, un gérant, un commis, un employé. Le patron décide ; le gérant "
         "s'occupe de la journée ; le commis sert les clients."),
        ("Les papiers",
         "une affiche, une offre d'emploi, un formulaire, un curriculum vitæ. Les "
         "trois premiers sont fréquents ; le dernier ne l'est pas toujours."),
        ("Les gestes",
         "embaucher, engager, offrir ses services, se présenter. Les deux premiers "
         "veulent dire la même chose et s'entendent tous les deux ici."),
    ], notes="Faire nommer chaque famille par un élève différent, avec l'article.")

    d.piege("Croire qu'il faut toujours un curriculum vitæ",
            "Je n'ai pas de CV, alors je n'entre pas.",
            "J'entre, et je dis ce que je sais faire.",
            "Un petit commerce qui affiche « On embauche » veut surtout savoir si vous "
            "êtes disponible et si vous pouvez faire le travail. Le CV vient plus tard, "
            "quand il vient. Ne pas entrer, c'est se refuser le poste soi-même.",
            notes="Ne pas moraliser. Beaucoup ont entendu le contraire dans un cours "
                  "d'employabilité : préciser que les deux sont vrais, selon le milieu.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Fanta est arrivée de Conakry il y a un an.", "vrai"),
        ("Elle a déjà travaillé au Québec.", "faux — jamais"),
        ("L'affiche de la boulangerie dit « On embauche ».", "vrai"),
        ("Sylvie dit qu'il faut un curriculum vitæ.", "faux — pas toujours"),
        ("Fanta a gardé des enfants pendant six ans.", "vrai"),
        ("Il faut y aller entre onze heures et deux heures.", "faux — c'est l'heure du dîner"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte du dialogue.")

    d.billet(
        "Écrivez trois choses que vous savez faire.",
        exemples=[
            "Avec un verbe : je sais faire le ménage, je sais cuisiner…",
            "Une seule ligne par chose. On les relira à la séance B3.",
        ],
        notes="Devoir court. Il prépare le défi 1 et donne à chacun des exemples "
              "personnels au lieu de ceux du dialogue.")

    return d.save(dossier)
