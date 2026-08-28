# -*- coding: utf-8 -*-
"""B1 · Mon quart commence à quelle heure ?
Bloc B « Défi 1 · Mon quart commence à quelle heure ? » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-horaire/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Mon quart commence à quelle heure ?",
        chapeau="« 6 h - 14 h » se comprend en une seconde quand on sait le "
                "lire, et fait manquer une journée quand on ne le sait pas. "
                "Fabiola, elle, a fini par demander.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Faire le lien avec le billet de A4 : chacun a "
                  "écrit sa semaine. Ce sont ces horaires-là qu'on lira, pas seulement "
                  "celui de Fabiola.")

    d.objectifs([
        "lire un quart écrit en chiffres sur un horaire ;",
        "comprendre l'heure de vingt-quatre heures ;",
        "relever la durée d'un quart et celle d'une pause ;",
        "poser une question sur son horaire à son chef d'équipe.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce que « 6 h - 14 h » veut dire ?",
        image=IMG + 'tableau-horaire.jpg',
        pistes=[
            "À quelle heure cette personne commence-t-elle ?",
            "À quelle heure finit-elle ?",
            "Combien d'heures cela fait-il ?",
            "Est-ce que la pause est comprise dedans ?",
        ],
        notes="La quatrième question surprend presque toujours : la pause est dans le "
              "quart, mais elle n'est pas payée partout. Ne pas trancher — dire que ça "
              "dépend du milieu, et que ça se demande.")

    d.dialogue('Dialogue · 1 de 3', "Je ne suis pas sûre", [
        ("FABIOLA", "Monsieur Roy, je regarde l'horaire et je ne suis pas sûre.", True),
        ("GAÉTAN", "Dites-moi. Quelle journée vous inquiète ?", True),
        ("FABIOLA", "Mercredi. C'est écrit « 6 h - 14 h ». Ça veut dire quoi ?", True),
        ("GAÉTAN", "Votre quart commence à six heures et finit à quatorze heures.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="La première réplique est la leçon entière du module : « je ne suis pas "
             "sûre » suffit à ouvrir la conversation. Aucune honte, aucune excuse — et "
             "le chef répond aussitôt.")

    d.dialogue('Dialogue · 2 de 3', "Huit heures, moins la pause", [
        ("FABIOLA", "Six heures du matin ? Il fait encore noir.", False),
        ("GAÉTAN", "Le déjeuner des résidents est à sept heures. On prépare avant.", True),
        ("FABIOLA", "Et ça dure combien de temps, huit heures ?", True),
        ("GAÉTAN", "Huit heures, moins la pause du midi. Trente minutes.", True),
    ], notes="Deux questions modèles de Fabiola : « ça veut dire quoi ? » et « ça dure "
             "combien de temps ? ». Les faire relever — elles reviennent à l'exercice "
             "de B3.")

    d.dialogue('Dialogue · 3 de 3', "Rien d'écrit, c'est congé", [
        ("MIGUEL", "Moi, je travaille de quatorze heures à vingt-deux heures.", True),
        ("FABIOLA", "Et le samedi ? Il n'y a rien d'écrit sur ma ligne.", True),
        ("GAÉTAN", "Rien d'écrit, c'est congé. Vous êtes en congé samedi et dimanche.", True),
        ("GAÉTAN", "De onze heures et demie à midi. Vous mangez avant les résidents.", True),
    ], notes="La règle de la case vide, vue en A4, est ici confirmée par le chef "
             "d'équipe. C'est exactement le geste qu'on veut enseigner : vérifier ce "
             "qu'on croit avoir compris.")

    d.tableau('Analyse', "Ce qu'on lit sur la ligne de Fabiola",
              ["Écrit sur le tableau", "Ce que ça veut dire"],
              [["6 h - 14 h", "de six heures du matin à deux heures de l'après-midi"],
               ["8 h", "la durée du quart, pause comprise"],
               ["11 h 30 - 12 h", "la pause, trente minutes"],
               ["(rien)", "congé — on ne vient pas"]],
              cle=1,
              note="L'heure de vingt-quatre heures s'écrit toujours sur un "
                   "horaire, et se dit rarement à voix haute : on dit "
                   "« deux heures », on écrit « 14 h ».",
              notes="Diapo à photographier. La note du bas est le pont vers B3 : "
                    "l'horaire écrit et l'heure parlée ne sont pas la même chose.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("« 6 h - 14 h » veut dire de six heures à quatorze heures.", "vrai"),
        ("Le déjeuner des résidents est à six heures.", "faux — à sept heures"),
        ("La pause du midi dure trente minutes.", "vrai"),
        ("Miguel travaille de quatorze heures à vingt-deux heures.", "vrai"),
        ("Fabiola et Miguel se croisent quinze minutes.", "vrai — à deux heures"),
        ("Fabiola travaille samedi et dimanche.", "faux — elle est en congé"),
    ], corrige=True,
       notes="C'est l'exercice `t1vf` du module interactif, mot pour mot. Faire justifier "
             "chaque « faux » par la réplique exacte.")

    d.billet(
        "Écrivez une question que vous n'avez jamais osé poser au travail.",
        exemples=[
            "Sur l'horaire, sur la pause, sur une tâche.",
            "« Est-ce que la pause est payée ? »",
        ],
        notes="Devoir court, anonyme si l'élève préfère. Ces questions serviront en B3, "
              "où on apprend à les poser. C'est le matériau le plus utile du module et "
              "il ne s'invente pas.")

    return d.save(dossier)
