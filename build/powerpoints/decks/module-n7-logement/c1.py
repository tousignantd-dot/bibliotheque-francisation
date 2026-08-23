# -*- coding: utf-8 -*-
"""C1 · La visite du samedi matin
Bloc C « Défi 2 · La visite avec la courtière » · couleur acier · compréhension
orale · 75 min.
Source : dialogue `t2`, exercice `t2vf` et son bandeau de cinq mots.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="La visite du samedi matin",
        chapeau="Quarante minutes de visite pour un engagement de "
                "vingt-cinq ans. Ce qui fait la différence, ce n'est pas de "
                "savoir juger un plancher : c'est de savoir à qui l'on parle.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2. On change de monde : le bloc B était la "
                  "location, les blocs C et D sont l'achat. Le dire explicitement, en "
                  "reprenant le tableau de A4.")

    d.objectifs([
        "suivre une visite de vingt-quatre répliques et en retenir les chiffres ;",
        "comprendre pour qui travaille la courtière, et ce que ça change ;",
        "relever les questions que pose Sokhna et ce qu'elles obtiennent ;",
        "employer cinq mots de la visite.",
    ], notes="Le deuxième objectif est le cœur du défi. Ce n'est pas une leçon de "
             "méfiance : c'est une information vérifiable, que la courtière donne "
             "elle-même dès la troisième réplique.")

    d.declencheur(
        'Avant d\'écouter', "Vous visitez un logement à vendre : à qui parlez-vous ?",
        pistes=[
            "La personne qui ouvre la porte, pour qui travaille-t-elle ?",
            "Est-ce que vous pouvez lui demander ce qu'elle pense du prix ?",
            "Qui la paie, à votre avis ?",
            "Qu'est-ce que vous lui demanderiez en premier ?",
        ],
        notes="Recueillir les réponses sans corriger. Le dialogue répond aux quatre "
              "questions, dans cet ordre, et c'est plus efficace que l'explication.")

    d.dialogue('Dialogue · 1 de 3', "Je suis la courtière du vendeur", [
        ("JOSIANE", "Avant qu'on monte, il y a une chose que je dois vous dire, et je la dis à tout le monde : je suis la courtière du vendeur. J'ai un contrat de courtage avec lui.", True),
        ("SOKHNA", "C'est-à-dire ?", False),
        ("JOSIANE", "C'est-à-dire que je travaille pour lui. Je ne vous représente pas. Je dois vous traiter équitablement et vous donner l'information de façon objective.", True),
        ("SOKHNA", "Et ça me coûterait combien, mon propre courtier ?", True),
        ("JOSIANE", "Dans la plupart des transactions résidentielles, la rétribution est payée par le vendeur. Ce que je ne peux pas faire, moi, c'est vous réclamer quoi que ce soit.", True),
    ], consigne="Écouter deux fois, diapositive masquée.",
       notes="Insister : une courtière qui annonce cela d'elle-même fait exactement son "
             "travail. C'est un bon signe, pas un aveu. Le groupe l'entend souvent à "
             "l'envers la première fois.")

    d.dialogue('Dialogue · 2 de 3', "Les chiffres de la fiche", [
        ("JOSIANE", "Quatre pièces et demie, deuxième étage, construit en mil neuf cent quatre-vingt-douze. Deux cent soixante-quinze mille, et les frais de copropriété sont de cent quatre-vingt-dix dollars par mois.", True),
        ("SOKHNA", "Cent quatre-vingt-dix par mois. Ça comprend quoi, exactement ?", True),
        ("JOSIANE", "L'assurance de l'immeuble, l'entretien des parties communes, le déneigement, et une part qui va au fonds de prévoyance.", True),
        ("SOKHNA", "Alors je la pose : combien il y a dans le fonds, et depuis quand ?", True),
    ], notes="Faire noter les trois chiffres au fil de l'écoute : 275 000, 190, 1992. "
             "Ils reviennent en C2, en D1 et dans la production orale de E1.")

    d.dialogue('Dialogue · 3 de 3', "Je ne le sais pas, et je ne vais pas l'inventer", [
        ("SOKHNA", "Le voisin du dessus, celui qu'on entend marcher, il est là depuis longtemps ?", True),
        ("JOSIANE", "Ça, je ne le sais pas, et je ne vais pas l'inventer. Je vais me renseigner et je vous rappelle.", True),
        ("SOKHNA", "J'apprécie que vous disiez « je ne sais pas ». Duquel des deux stationnements est-ce qu'on parle, sur la fiche ?", True),
        ("JOSIANE", "Du numéro huit, celui de gauche. Il est inclus. Le cabanon, lui, ne l'est pas.", True),
    ], notes="« Je ne sais pas, je vérifie » est la meilleure réponse possible, et le "
             "groupe croit souvent le contraire. Y consacrer deux minutes : une personne "
             "qui répond à tout n'est pas mieux informée, elle est plus rapide.")

    d.vocabulaire('Vocabulaire', "Cinq mots de la visite", [
        ("un courtier immobilier", "Un métier encadré. La question n'est pas s'il est honnête, mais pour qui il travaille."),
        ("un contrat de courtage", "Le contrat qui lie le courtier à une seule partie et qui fixe sa rétribution."),
        ("les frais de copropriété", "Ce qu'on paie chaque mois en plus du prêt, pour l'assurance, l'entretien commun et le fonds."),
        ("le fonds de prévoyance", "L'argent mis de côté ensemble pour les gros travaux : le toit, les balcons, les fenêtres."),
        ("une fiche descriptive", "Le papier qui donne l'année, la superficie, les frais et ce qui est inclus."),
    ], notes="Faire remarquer que trois de ces cinq mots n'existent pas en location. "
             "C'est la preuve concrète du tableau de A4.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la visite du condo de la rue Sainte-Anne.", [
        ("La courtière annonce d'elle-même qu'elle représente le vendeur.", "vrai"),
        ("Elle explique qu'elle défend aussi les intérêts de Sokhna.", "faux - elle dit le contraire"),
        ("Elle ne peut réclamer aucune rétribution à l'acheteur.", "vrai"),
        ("Les frais de copropriété sont de 190 $ par année.", "faux - par mois"),
        ("Elle invente une réponse au sujet du voisin du dessus.", "faux - elle dit qu'elle vérifie"),
        ("Le stationnement numéro huit est inclus, mais pas le cabanon.", "vrai"),
    ], corrige=True,
       notes="Six des huit items de `t2vf`. Le quatrième item se corrige en refaisant "
             "le calcul : 190 $ par année serait 16 $ par mois, ce qui n'existe pas.")

    d.billet(
        "Écris la première question que tu poserais en entrant.",
        exemples=[
            "Une question à laquelle on ne peut pas répondre « ça dépend ».",
            "Une seule question.",
        ],
        notes="Deux minutes. Les billets servent de matière première en C2, où l'on "
              "trie les questions précises et les questions vagues du groupe lui-même.")

    return d.save(dossier)
