# -*- coding: utf-8 -*-
"""A4 · La décision de dix secondes.
Bloc A « Je découvre » · couleur ambre · 75 min. Écriture et décision.
Source : exercice `prNum` et sa mini-leçon.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-urgence/images/')


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="La décision de dix secondes",
        chapeau="Devant quelqu'un qui ne va pas bien, on n'hésite pas entre "
                "dix possibilités : on hésite entre appeler tout de suite "
                "et attendre demain. Une seule question tranche.",
        duree='75 minutes')

    d.titre(notes="Fin du bloc A. Commencer par relire deux billets de A1 — la liste des "
                  "signes — et annoncer qu'on va la compléter, puis la mettre à l'épreuve "
                  "sur des situations réelles.")

    d.objectifs([
        "poser la question qui tranche entre le 8-1-1 et le 9-1-1 ;",
        "connaître les cinq signes qui ne se discutent pas ;",
        "savoir ce que coûte un transport en ambulance, et quand il est payé ;",
        "écrire les deux phrases d'ouverture d'un appel au 8-1-1.",
    ])

    d.declencheur(
        'Décision', "Il est minuit. Votre voisine de soixante-dix ans est tombée et "
                    "elle ne peut pas se relever. Vous faites quoi ?",
        image=IMG + 'ambulance.jpg',
        pistes=[
            "Est-ce qu'on l'aide à se relever d'abord ?",
            "Est-ce qu'on l'amène en voiture ?",
            "Combien coûte une ambulance, et est-ce que ça doit compter ?",
            "Que dit-on en premier quand on compose ?",
        ],
        notes="La deuxième piste est un vrai danger : relever quelqu'un qui a une "
              "fracture de la hanche aggrave la blessure. Le dire, sans effrayer.")

    d.regle("Est-ce que ça peut attendre dix minutes ?",
            "Si non, c'est le 9-1-1. Si vous hésitez sur ce qu'il faut faire, c'est le 8-1-1.",
            precision="Dans le doute entre les deux, on compose le 9-1-1 : le service "
                      "existe pour des gens qui ne sont pas soignants, et personne ne "
                      "reprochera un appel de trop.",
            notes="Diapositive à photographier. Elle remplace toutes les listes : c'est "
                  "une question, pas un tableau à mémoriser.")

    d.cartes("Les cinq signes qui ne se discutent pas", "On raccroche et on compose le 9-1-1", [
        ("Une douleur à la poitrine",
         "Surtout avec des sueurs, un bras lourd ou une difficulté à respirer."),
        ("Une difficulté à respirer",
         "La personne cherche son air ou ne peut plus finir une phrase."),
        ("Une perte de connaissance",
         "Même brève, même si la personne se réveille ensuite."),
        ("Un saignement qu'on n'arrête pas",
         "Malgré une compresse et une pression maintenue."),
        ("Une chute d'où la personne ne se relève pas",
         "On ne la déplace pas et on ne la fait pas asseoir."),
        ("Et un sixième, moins connu",
         "Une confusion soudaine, des mots qui ne viennent plus, un visage qui tombe "
         "d'un côté."),
    ], cols=3,
       notes="Le sixième vaut à lui seul la séance : il est mal connu et c'est celui où "
             "chaque minute compte le plus.")

    d.tableau('Ce que coûte le transport', "Les chiffres, pour qu'ils cessent de faire peur",
              ['La question', 'La réponse'],
              [["Le tarif de base", "environ 125 $"],
               ["Le kilométrage", "environ 1,75 $ le kilomètre"],
               ["65 ans et plus", "payé, si le médecin le confirme après coup"],
               ["Couvert par la carte d'assurance maladie ?", "non — c'est "
                "l'établissement qui l'assume"],
               ["Faut-il hésiter pour cette raison ?", "jamais, devant l'un des "
                "cinq signes"]],
              cle=0,
              notes="Beaucoup d'élèves hésitent à cause du coût et n'osent pas le dire. "
                    "Donner les chiffres enlève la gêne et remet la décision au bon "
                    "endroit.")

    d.piege("Prendre sa voiture pour aller plus vite",
            "On va y aller en auto, ça coûte moins cher et c'est à dix minutes.",
            "On appelle : les ambulanciers commencent les soins dans le salon.",
            "L'ambulance n'est pas un taxi : les soins commencent chez vous, et l'hôpital "
            "sait qu'elle arrive. Pour une douleur à la poitrine, c'est la différence "
            "qui compte le plus.",
            notes="Le dire une fois, calmement, sans faire peur. Puis passer : la peur "
                  "n'apprend rien.")

    d.pratique('Décision', "8-1-1 ou 9-1-1 ?",
               "Pour chaque situation, décidez à voix haute, puis justifiez.", [
        ("Une personne tombée qui ne peut pas se relever.", "9-1-1"),
        ("Un enfant qui fait de la fièvre depuis deux jours.", "8-1-1"),
        ("Une forte douleur à la poitrine depuis dix minutes.", "9-1-1"),
        ("Un comprimé pris deux fois ce matin.", "8-1-1"),
        ("Un saignement qui ne s'arrête pas.", "9-1-1"),
        ("Une plaie rouge depuis trois jours.", "8-1-1"),
        ("Une personne effondrée dans l'autobus, qui ne répond pas.", "9-1-1"),
        ("Une éruption sur les bras, et un doute.", "8-1-1"),
    ], corrige=True,
       notes="Faire justifier avec la question de la règle, pas avec la liste : « est-ce "
             "que ça peut attendre dix minutes ? ». C'est le réflexe à installer.")

    d.regle("Au 8-1-1 on décrit ; au 9-1-1 on annonce",
            "Deux phrases contre une. La longueur de l'appel n'est pas la même.",
            precision="Au 8-1-1, l'infirmière a besoin du détail : depuis quand, quelle "
                      "température, prise comment, qui boit, qui mange. Au 9-1-1, elle "
                      "n'a besoin que de l'endroit et d'une phrase.",
            notes="Cette diapositive fait le pont vers le bloc B, qui portera entièrement "
                  "sur la phrase unique du 9-1-1.")

    d.billet(
        "Écrivez les deux premières phrases d'un appel au 8-1-1.",
        exemples=[
            "Première phrase : pour qui vous appelez, et son âge.",
            "Deuxième phrase : ce qu'elle a, et depuis quand.",
        ],
        notes="Ramasser. Les meilleures serviront d'ouverture à la séance B1, où l'on "
              "verra qu'au 9-1-1, ces deux phrases-là arrivent trop tôt.")

    return d.save(dossier)
