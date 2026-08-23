# -*- coding: utf-8 -*-
"""A1 · Trois propositions, quatorze cents dollars
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercices `pr1` et `prVocab`.
"""
from theme import Deck

import pathlib

# Chemin déduit du fichier, jamais écrit en dur : le dépôt est aussi construit
# depuis un worktree git, où un chemin absolu vers la copie principale
# pointerait sur des images qui n'y sont pas encore.
IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-oeuvres' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Trois propositions, et un avis à préparer pour jeudi",
        chapeau="Un comité doit choisir une sortie pour trente-huit personnes. "
                "Ce n'est pas le choix qui est difficile : c'est de dire "
                "pourquoi, devant quelqu'un qui pense autrement.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : "
                  "qui a déjà eu à choisir une sortie pour un groupe ? Les histoires "
                  "sortent vite, et elles finissent presque toujours par « personne "
                  "n'était content ». C'est la matière du module.")

    d.objectifs([
        "nommer les pièces d'une œuvre et d'une soirée de spectacle ;",
        "distinguer un goût d'un avis, et un avis d'un argument ;",
        "choisir le registre de langue que la situation demande ;",
        "employer les premiers mots du dossier : une œuvre, une appréciation, "
        "une concession.",
    ], notes="Le deuxième objectif est le cœur du module et il ne sera pas atteint "
             "aujourd'hui. Le poser quand même : les quinze séances y reviennent.")

    d.declencheur(
        'Observation', "Où avez-vous rencontré une œuvre cette semaine ?",
        image=IMG + 'salle-vue-de-scene.jpg',
        pistes=[
            "Un film, une série, une chanson, un livre, un spectacle ?",
            "Seul, ou avec quelqu'un ?",
            "En avez-vous parlé à quelqu'un après ?",
            "Avez-vous dit pourquoi vous aviez aimé, ou seulement que vous aviez aimé ?",
        ],
        notes="Question sans mauvaise réponse. La quatrième piste est celle qui porte "
              "le module : presque personne ne dit pourquoi. Ne pas le reprocher, le "
              "faire remarquer.")

    d.dialogue('Dialogue · 1 de 3', "Le mandat du comité", [
        ("GHYSLAINE", "Le comité social se réunit jeudi et il faut choisir la sortie de fin d'année. On a trente-huit personnes et quatorze cents dollars.", True),
        ("MARILOU", "Quatorze cents pour trente-huit ? Ça fait à peu près trente-six dollars par personne. C'est serré.", True),
        ("GHYSLAINE", "C'est serré, oui. J'ai reçu trois propositions et je te les envoie ce soir.", True),
        ("MARILOU", "Et toi, tu penses quoi ?", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Laisser le groupe faire le calcul au tableau. Trente-six dollars par "
             "personne, transport compris : c'est ce chiffre qui décidera de tout en D1.")

    d.dialogue('Dialogue · 2 de 3', "Pourquoi elle ne répond pas", [
        ("GHYSLAINE", "Je ne dois surtout pas te le dire avant que tu les aies vus. Sinon tu vas voter comme moi et le comité ne sert plus à rien.", True),
        ("MARILOU", "Un avis, ce n'est pas difficile. J'aime ou je n'aime pas.", True),
        ("GHYSLAINE", "C'est là que tu te trompes. Un avis, ça ne sert à rien tout seul.", True),
        ("GHYSLAINE", "Si tu arrives avec « j'ai aimé ça », Gaétan va te répondre « moi j'ai pas aimé ça » et on ne sera pas plus avancés.", True),
    ], notes="Le point de départ du module, dit par un personnage. L'écrire au tableau "
             "et l'y laisser jusqu'à E2 : un avis seul ne se discute pas.")

    d.dialogue('Dialogue · 3 de 3', "Ce qu'on attend d'elle jeudi", [
        ("GHYSLAINE", "Il faut que tu expliques pourquoi, et que tu l'appuies sur un moment précis.", True),
        ("GHYSLAINE", "Pas « c'était drôle », mais « le passage du comptoir m'a fait rire, parce qu'il joue le gérant sans jamais l'imiter ».", True),
        ("MARILOU", "Et si Gaétan n'est pas d'accord ?", True),
        ("GHYSLAINE", "Tu commences par lui accorder quelque chose. Une personne à qui on a donné raison sur un point écoute le reste.", True),
    ], notes="Les trois consignes de tout le module tiennent ici : le pourquoi, le "
             "moment précis, la concession. Les écrire au tableau en trois lignes.")

    d.tableau('Analyse', "Trois propositions sur la table",
              ['La proposition', 'Ce que ça suppose'],
              [["Le spectacle",
                "trente-quatre dollars, une grande salle, et il faut suivre l'ironie"],
               ["Le tour de chant",
                "vingt-deux dollars, cent vingt chaises, un sous-sol d'église"],
               ["Le long métrage",
                "quinze dollars, une heure cinquante, presque aucune parole au début"]],
              cle=0,
              note="Aucune n'est meilleure : chacune coûte quelque chose au groupe.",
              notes="Diapositive à photographier. Ne pas laisser le groupe choisir "
                    "aujourd'hui : la classe n'a encore rien vu ni rien entendu.")

    d.regle("Un avis n'est pas un goût",
            "Un goût parle de vous. Un avis parle de l'œuvre, et on peut en "
            "discuter.",
            precision="« J'aime pas ça » est vrai et il n'y a rien à répondre. « Le "
                      "début est lent parce qu'aucune parole n'est échangée avant la "
                      "douzième minute » se vérifie, s'approuve ou se conteste. C'est "
                      "la seule des deux phrases qui fait avancer une réunion.",
            notes="Diapositive à photographier. Question fréquente : « mais mon goût "
                  "compte, non ? » Oui, et il ne se discute pas. C'est exactement le "
                  "point.")

    d.vocabulaire('Vocabulaire', "Six mots pour commencer", [
        ("une œuvre", "Ce qu'une personne a écrit, filmé, composé ou joué, et qui existe maintenant tout seul."),
        ("une appréciation", "Ce qu'une personne pense d'une œuvre, une fois qu'elle l'a vue ou entendue."),
        ("une concession", "Le fait d'accorder un point à celui qui n'est pas d'accord, avant de lui répondre."),
        ("un long métrage", "Un film de cinéma qui dure plus d'une heure."),
        ("un tour de chant", "Un spectacle où une personne chante ses chansons, souvent avec peu de musiciens."),
        ("une salle de spectacle", "Le lieu où l'on présente un spectacle devant un public assis."),
    ], notes="Faire répéter avec l'article. « Concession » est le mot du module : le "
             "faire dire trois fois, il reviendra à chaque séance.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le comité a quatorze cents dollars pour trente-huit personnes.", "vrai"),
        ("Ghyslaine dit tout de suite laquelle elle préfère.", "faux - elle refuse"),
        ("Réjean Cadorette a travaillé trente ans dans un entrepôt.", "vrai"),
        ("Le tour de chant a lieu dans une salle de mille places.", "faux - cent vingt chaises"),
        ("Selon Ghyslaine, un avis vaut autant sans raison.", "faux - il ne sert à rien"),
        ("C'est Marilou qui rédigera le compte rendu.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le deuxième "
             "surprend toujours : pourquoi une présidente refuserait-elle de dire son "
             "avis ? Parce qu'elle veut huit avis, pas huit fois le sien.")

    d.billet(
        "Nommez une œuvre que vous avez vue ou entendue cette semaine, et dites "
        "une chose que vous en pensez.",
        exemples=[
            "Le titre, et où vous l'avez vue.",
            "Une phrase qui commence par « j'ai trouvé que ».",
        ],
        notes="Devoir concret. Les réponses servent de matière première tout le "
              "module : chaque élève arrive avec une œuvre à défendre, et c'est "
              "celle qu'il présentera en E1.")

    return d.save(dossier)
