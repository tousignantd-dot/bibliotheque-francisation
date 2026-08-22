# -*- coding: utf-8 -*-
"""B1 · Le voisin de banquette
Bloc B « Défi 1 · Deux heures dans la salle d'attente » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf`, quatre mots de FC_CARDS.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Le voisin de banquette",
        chapeau="Une salle d'attente est le seul endroit d'un hôpital où "
                "personne n'est obligé de vous parler. C'est aussi celui où "
                "l'on apprend le plus.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 1. Reprendre trente secondes le tableau des "
                  "quatre personnes de A1 avant de commencer : le module suit un "
                  "seul dossier, et le groupe doit s'en rappeler.")

    d.objectifs([
        "suivre une conversation longue entre deux inconnus ;",
        "reconnaître ce dont on parle et ce dont on ne parle pas ;",
        "entendre un récit qui recule dans le temps ;",
        "employer les quatre mots de l'attente avec leur article.",
    ], notes="Le deuxième objectif est culturel autant que linguistique. Il se "
             "travaille par l'exemple, jamais par la liste d'interdits.")

    d.declencheur(
        'Observation', "Est-ce que vous parlez aux gens dans une salle d'attente ?",
        pistes=[
            "Chez vous, est-ce qu'on se parle entre inconnus ?",
            "Qu'est-ce qu'on peut demander, et qu'est-ce qu'on ne demande pas ?",
            "Qui commence, d'habitude ?",
            "Est-ce que ça change quelque chose à l'attente ?",
        ],
        notes="Cinq minutes. La comparaison entre pays est très riche ici et il n'y "
              "a rien à trancher : on note les usages au tableau, on ne les classe pas.")

    d.dialogue('Dialogue · 1 de 3', "Vous êtes après attendre depuis longtemps ?", [
        ("GILLES", "Vous êtes après attendre depuis longtemps ?", True),
        ("LEYLA", "Depuis neuf heures et demie. Il est onze heures moins quart.", True),
        ("GILLES", "Bienvenue. Moi, ça fait deux heures et je ne suis même pas malade. C'est ma femme qui est là-dedans.", True),
        ("LEYLA", "Ah. Vous l'attendez tout ce temps-là ?", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Faire remarquer la réponse de Leyla : elle reprend un mot de Gilles au "
             "lieu de répondre par oui. C'est ce geste-là qui transforme deux phrases "
             "polies en conversation, et il revient en B4.")

    d.dialogue('Dialogue · 2 de 3', "Fatiguée comment ?", [
        ("GILLES", "On appelle ça un proche aidant, paraît-il. Moi, j'appelle ça être marié.", True),
        ("LEYLA", "C'est une job que j'aime. C'est juste que depuis huit mois, je la fais fatiguée.", True),
        ("GILLES", "Fatiguée comment ? Fatiguée de fin de semaine, ou fatiguée qui ne part pas ?", True),
        ("LEYLA", "Qui ne part pas. Au mois de mars, j'avais laissé faire, je pensais que c'était l'hiver.", True),
    ], notes="Arrêter sur la question de Gilles. Elle est plus précise que « comment "
             "ça va ? » et elle vient d'un homme sans formation : la précision n'est "
             "pas une affaire de vocabulaire savant.")

    d.dialogue('Dialogue · 3 de 3', "Ça valait la peine", [
        ("GILLES", "On avait passé proche d'annuler, au mois d'août. Je l'ai gardée dans l'auto de force.", True),
        ("LEYLA", "Et ça valait la peine ?", True),
        ("GILLES", "Ça valait la peine. Pas parce qu'ils ont trouvé un remède miracle. Parce qu'à partir de ce jour-là, quelqu'un s'occupait de son affaire.", True),
        ("GILLES", "Quand elle va vous demander comment vous allez, ne répondez pas « ça va ».", True),
    ], notes="Écrire au tableau : « Ne répondez pas ça va. » C'est la phrase qui "
             "ouvre tout le Défi 2. La laisser affichée jusqu'à la séance C2.")

    d.tableau('Analyse', "Ce dont on parle, et ce dont on ne parle pas",
              ['Le sujet', 'Est-ce qu\'on l\'aborde ?'],
              [["L'attente, l'heure", "oui : c'est à tout le monde"],
               ["Le stationnement", "oui : c'est à tout le monde"],
               ["Ce que l'autre a", "non : ça lui appartient"],
               ["Pourquoi il est là", "non : il le dira s'il veut"],
               ["Ce qu'on lui a dit", "non, jamais"]],
              cle=0,
              note="Une seule règle : on parle de ce qui est à tout le monde, jamais de ce qui est à l'autre.",
              notes="Diapositive à photographier. La frontière n'est pas propre au "
                    "Québec, mais elle y est nette. Une question sur la santé d'un "
                    "inconnu met mal à l'aise, même posée gentiment.")

    d.regle("Une bonne amorce laisse une porte de sortie",
            "Elle se répond en un mot par quelqu'un qui n'a pas envie de parler.",
            precision="« Vous attendez depuis longtemps ? » peut recevoir « oui » et "
                      "s'arrêter là. Si la réponse est courte et ne revient pas vers "
                      "vous, on s'arrête : ce n'est pas un refus de vous, c'est un "
                      "refus de parler, et il est légitime.",
            notes="Diapositive à photographier. Le dire explicitement évite qu'un "
                  "élève interprète un silence comme un rejet lié à son accent.")

    d.vocabulaire('Vocabulaire', "Les quatre mots de l'attente", [
        ("un malaise", "Un dérangement du corps qu'on sent sans pouvoir le montrer du doigt."),
        ("la fatigue chronique", "Une fatigue qui dure des mois et que le repos ne fait pas partir."),
        ("un proche aidant", "Celui qui accompagne quelqu'un de sa famille sans être payé pour ça."),
        ("les heures de visite", "Les moments où l'on a le droit d'entrer voir quelqu'un d'hospitalisé."),
    ], notes="Demander qui, dans le groupe, est un proche aidant sans le savoir. La "
             "question surprend et la réponse est souvent oui.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la conversation de Leyla et de Gilles.", [
        ("Gilles attend depuis deux heures sans être malade.", "vrai"),
        ("Sa femme ne conduit plus depuis son opération.", "vrai"),
        ("Leyla est arrivée au Québec il y a trois ans.", "faux - cinq ans"),
        ("Leyla dort neuf heures et se lève reposée.", "faux - comme si elle avait travaillé"),
        ("En mars, elle avait mis sa fatigue sur le compte de l'hiver.", "vrai"),
        ("Le rendez-vous a valu la peine parce qu'on a trouvé un remède.", "faux - parce que quelqu'un s'en occupe"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le dernier est "
             "le plus important : ce que Gilles décrit n'est pas une guérison, c'est "
             "la fin d'une solitude.")

    d.billet(
        "Écrivez une phrase pour entrer en conversation dans une salle d'attente.",
        exemples=[
            "Une seule phrase, qui ne demande rien de privé.",
            "Elle doit pouvoir se répondre en un mot.",
        ],
        notes="Deux minutes. Ramasser les billets et en lire trois ou quatre à voix "
              "haute sans nommer les auteurs : ils serviront de banc de départ en B4.")

    return d.save(dossier)
