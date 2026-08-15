# -*- coding: utf-8 -*-
"""A4 · Qui soigne quoi, et où aller.
Bloc A · couleur acier (compréhension) · 60 min.
Source : exercices `prPro`, `prImg`, `prQuel`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/assets/'
       'interactive/module-consultation/images/')


def build(dossier):
    d = Deck(
        code='A4', section='acier',
        titre='Qui soigne quoi, et où aller',
        chapeau="Six professionnels, trois portes d'entrée. Se tromper de porte coûte "
                "une demi-journée d'attente — ou, dans l'autre sens, retarde des soins "
                "qui n'attendent pas.",
        duree='60 minutes')

    d.titre(notes="Séance de repérage dans le réseau. Beaucoup d'élèves ne connaissent "
                  "qu'une porte : l'urgence. C'est la séance qui en ouvre trois autres.")

    d.objectifs([
        "nommer six professionnels de la santé et dire ce que chacun soigne ;",
        "distinguer l'urgence, la clinique sans rendez-vous et le médecin de famille ;",
        "reconnaître les signes qui obligent à aller à l'urgence ;",
        "savoir qui appeler quand on ne sait pas quoi faire.",
    ])

    d.declencheur(
        'Mise en situation', "Où iriez-vous, et pourquoi ?",
        image=IMG + 'pharmacien.jpg',
        pistes=[
            "Une éruption sur le bras depuis deux jours : où allez-vous ?",
            "Un enfant qui tousse depuis trois jours avec un peu de fièvre ?",
            "Une douleur à la poitrine avec difficulté à respirer ?",
            "Et quand vous ne savez pas du tout : qui pouvez-vous appeler ?",
        ],
        notes="Laisser répondre sans corriger. Noter les réponses au tableau ; on y "
              "reviendra à la diapo de la règle. La quatrième question amène Info-Santé, "
              "que peu d'élèves connaissent.")

    d.tableau('Analyse', "Six professionnels et leur domaine",
              ['Le professionnel', 'Ce qu\'il soigne'],
              [["l'optométriste", "la vision et les lunettes"],
               ["le dentiste", "les dents et les gencives"],
               ["la physiothérapeute", "les muscles et les articulations"],
               ["la dermatologue", "la peau"],
               ["le pédiatre", "la santé des enfants"],
               ["la pharmacienne", "les médicaments"]],
              cle=0, props=[0.42, 0.58],
              notes="On retient la partie du corps, pas la maladie : c'est ce qui permet "
                    "de choisir sans connaître le nom du problème. "
                    "Faire deviner le domaine à partir du nom quand c'est possible : "
                    "« dent-iste », « pédia-tre » (les enfants), « derma » (la peau).")

    d.cartes('Analyse', "Trois portes d'entrée, trois usages", [
        ("L'urgence",
         "Pour ce qui met la vie ou un membre en danger : saignement qu'on n'arrête pas, "
         "difficulté à respirer, douleur à la poitrine, perte de connaissance. Ouverte "
         "jour et nuit, mais l'attente est longue si le cas n'est pas grave."),
        ("La clinique sans rendez-vous",
         "Pour ce qui doit être vu aujourd'hui sans être dangereux : une blessure, une "
         "toux qui dure, une éruption, une douleur nouvelle. On y va tôt le matin."),
        ("Le médecin de famille",
         "Pour le suivi : renouveler une ordonnance, un examen annuel, un problème qui "
         "revient. Le rendez-vous peut prendre des semaines."),
        ("Info-Santé, le 811",
         "Quand on ne sait pas quoi faire. Une infirmière répond jour et nuit, "
         "gratuitement, et dit vers quelle porte aller."),
    ], notes="La quatrième carte est la plus utile de tout le module. S'assurer que "
             "chacun note le 811 dans son téléphone avant de sortir.")

    d.regle('La règle qui tranche',
            "Ce n'est pas la douleur qui décide, c'est le danger.",
            precision="Une douleur très forte peut relever de la clinique ; une "
                      "difficulté à respirer sans douleur relève de l'urgence. La "
                      "question à se poser n'est pas « est-ce que ça fait mal ? » mais "
                      "« est-ce que ça peut s'aggraver vite ? »",
            notes="Revenir aux réponses notées au tableau au début de la séance et les "
                  "relire à la lumière de cette règle. Certaines vont changer.")

    d.tableau('Analyse', "Quatre signes qui envoient à l'urgence",
              ['Le signe', 'Pourquoi'],
              [["difficulté à respirer", "l'oxygène manque en quelques minutes"],
               ["douleur à la poitrine", "le cœur peut être en cause"],
               ["saignement qui ne s'arrête pas", "la perte de sang s'accélère"],
               ["perte de connaissance", "la cause est inconnue et peut être grave"]],
              cle=0,
              note="Ces quatre signes ne se discutent pas : on appelle le 911 ou on va "
                   "à l'urgence, sans passer par la clinique.",
              notes="Faire apprendre ces quatre par cœur. C'est la seule liste du module "
                    "qui doit être sue sans hésitation.")

    d.pratique('Pratique · 1 de 3', 'Chaque professionnel et son domaine',
               "Reliez le professionnel à ce qu'il soigne.", [
        ("l'optométriste", "la vision et les lunettes"),
        ("le dentiste", "les dents et les gencives"),
        ("la physiothérapeute", "les muscles et les articulations"),
        ("la dermatologue", "la peau"),
        ("le pédiatre", "la santé des enfants"),
        ("la pharmacienne", "les médicaments"),
    ], corrige=True, cols=2,
       notes="Exercice de reconnaissance. Enchaîner tout de suite sur le suivant, qui "
             "demande le même savoir dans l'autre sens.")

    d.pratique('Pratique · 2 de 3', 'Qui iriez-vous voir ?',
               "Nommez le professionnel qui convient à la situation.", [
        ("Votre enfant de trois ans a de la fièvre depuis deux jours.", "le pédiatre"),
        ("Vous avez des taches rouges qui démangent sur le bras.", "la dermatologue"),
        ("Vous lisez de moins en moins bien de loin.", "l'optométriste"),
        ("Vous ne savez pas si votre médicament se prend avec de la nourriture.",
         "la pharmacienne"),
        ("Le médecin vous a référé pour retrouver l'usage de votre genou.",
         "la physiothérapeute"),
    ], corrige=True,
       notes="La quatrième surprend : beaucoup pensent qu'il faut rappeler le médecin. "
             "La pharmacienne répond gratuitement et sans rendez-vous.")

    d.pratique('Pratique · 3 de 3', 'Urgence ou clinique sans rendez-vous ?',
               "Pour chaque situation, dites où la personne devrait aller.", [
        ("Une personne saigne beaucoup et n'arrive pas à arrêter le saignement.",
         "URGENCE — le saignement ne s'arrête pas"),
        ("Un enfant tousse depuis trois jours et fait un peu de fièvre.",
         "CLINIQUE — ça dure, mais ce n'est pas dangereux"),
        ("Un homme a de la difficulté à respirer et mal à la poitrine.",
         "URGENCE — deux signes graves à la fois"),
        ("Une femme a une douleur au poignet depuis hier soir.",
         "CLINIQUE — nouvelle, mais sans danger"),
        ("Une personne a perdu connaissance dans la rue.",
         "URGENCE — appeler le 911"),
        ("Un étudiant a une éruption sur le bras depuis deux jours.",
         "CLINIQUE — la peau peut attendre quelques heures"),
    ], corrige=True,
       notes="Corriger en revenant chaque fois à la règle : « est-ce que ça peut "
             "s'aggraver vite ? » Ne jamais corriger par « parce que c'est comme ça ».")

    d.piege("Le piège de l'urgence",
            "Dans le doute, je vais à l'urgence.",
            "Dans le doute, j'appelle le 811.",
            "Aller à l'urgence pour un cas léger, c'est huit heures d'attente pour soi "
            "et un peu de retard pour les autres. Le 811 est gratuit, répond en quelques "
            "minutes, et dit exactement vers quelle porte aller. C'est la bonne réponse "
            "au doute.",
            notes="Beaucoup d'élèves nouvellement arrivés ne savent pas que ce service "
                  "existe ni qu'il est offert dans plusieurs langues. Le dire "
                  "explicitement.")

    d.billet(
        "Vous avez mal quelque part depuis deux jours. Où allez-vous, et pourquoi ?",
        exemples=[
            "Nommez la porte : urgence, clinique sans rendez-vous, médecin de famille "
            "ou 811.",
            "Donnez la raison en une phrase, avec « parce que ».",
        ],
        notes="Le « parce que » du billet prépare la séance B2, où la cause devient le "
              "sujet de la leçon.")

    return d.save(dossier)
