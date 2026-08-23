# -*- coding: utf-8 -*-
"""B3 · Devoir, il faut, il faudrait
Bloc B « Défi 1 · Le répondeur du centre » · couleur ambre · 75 min.
Source du module : exercice `t1devoir` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Devoir, il faut, il faudrait",
        chapeau="Trois façons de dire qu'une chose doit se faire, et elles "
                "ne sont pas interchangeables. Le personnel d'un centre "
                "emploie surtout les deux dernières ; vous emploierez la "
                "première pour dire ce que vous vous engagez à faire.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Commencer par faire écouter les trois formes "
                  "dites l'une après l'autre — « vous devez », « il faut », « il "
                  "faudrait » — et demander laquelle est la plus douce. Le groupe "
                  "l'entend sans qu'on l'explique.")

    d.objectifs([
        "conjuguer devoir au présent, sans faute d'orthographe ;",
        "employer « il faut » pour une règle qui vaut pour tout le monde ;",
        "adoucir avec « il faudrait » ;",
        "garder l'infinitif après ces trois formes.",
    ], notes="Le quatrième objectif est la faute numéro un du niveau : « je dois je "
             "téléphone ». La corriger dès la première apparition, sans attendre "
             "l'exercice.")

    d.regle("Après devoir et après falloir, l'infinitif",
            "Je dois téléphoner. Il faut remettre. Il faudrait signer.",
            precision="Le second verbe ne se conjugue jamais. « Je dois "
                      "j'appelle » ne se dit pas.",
            notes="Diapositive à photographier. C'est la règle la plus rentable de la "
                  "séance : elle vaut aussi après pouvoir, vouloir, aller et savoir.")

    d.tableau('Devoir au présent', "Six formes, deux pièges",
              ['La personne', 'La forme'],
              [["je", "dois — un seul s, jamais de t"],
               ["tu", "dois — la même chose"],
               ["il, elle", "doit — avec un t"],
               ["nous", "devons"],
               ["vous", "devez"],
               ["ils, elles", "doivent"]],
              cle=1,
              notes="Faire écrire « je dois » et « il doit » au tableau côte à côte. Le "
                    "t de la troisième personne est la seule difficulté, et elle ne "
                    "s'entend pas.")

    d.cartes("Trois degrés", "Du plus ferme au plus doux", [
        ("Vous devez",
         "Ferme, et cela nomme la personne. Le centre l'emploie quand rien n'est négociable."),
        ("Il faut",
         "La règle, sans personne. « Il » ne désigne rien : c'est un sujet vide."),
        ("Il faudrait",
         "Le conditionnel de politesse. Une suggestion posée sur la table."),
        ("Est-ce que je peux",
         "Ce n'est plus une obligation, c'est une permission. On commence presque toujours par là."),
    ], notes="La quatrième carte est celle que les élèves emporteront : au téléphone "
             "comme au comptoir, la première phrase après le bonjour est presque "
             "toujours « est-ce que je peux ».")

    d.regle("Falloir n'existe qu'à une forme",
            "Il faut, il faudra, il faudrait. Jamais « je faut », jamais "
            "« nous fallons ».",
            precision="Pour parler de soi, on emploie devoir : je dois.",
            notes="Cette règle-là paraît évidente et ne l'est pas : « je faut » se dit "
                  "régulièrement au niveau 4, par analogie avec « je peux » et « je "
                  "veux ».")

    d.pratique('Complétez', "Dois, doit, devez, faut, faudrait",
               "Une seule forme convient.", [
        ("Je ___ signaler mon absence avant le cours.", "dois"),
        ("Vous ___ nous remettre une note écrite et signée.", "devez"),
        ("Il ___ téléphoner avant huit heures.", "faut"),
        ("Elle ___ apporter le papier de la clinique jeudi.", "doit"),
        ("Il ___ nous prévenir un peu plus tôt, si c'est possible.", "faudrait"),
        ("Un élève à temps plein ___ justifier ses absences.", "doit"),
    ], corrige=True,
       notes="La cinquième est la seule où deux réponses se défendent : « il faut » "
             "n'est pas faux, mais « il faudrait » est ce que le personnel dirait, à "
             "cause de « si c'est possible ». Le faire remarquer.")

    d.pratique('Du ferme au doux', "Dites la même chose trois fois",
               "Avec vous devez, il faut, puis il faudrait.", [
        ("remettre une note",
         "Vous devez remettre une note. Il faut remettre une note. Il faudrait la remettre avant vendredi."),
        ("téléphoner avant huit heures",
         "Vous devez téléphoner avant huit heures. Il faut téléphoner tôt. Il faudrait appeler un peu plus tôt."),
        ("signer le papier",
         "Vous devez signer le papier. Il faut le signer à la main. Il faudrait le signer avant de le remettre."),
        ("annoncer un abandon",
         "Vous devez l'annoncer par écrit. Il faut le faire avant la fin du mois. Il faudrait le faire cette semaine."),
    ], corrige=True,
       notes="Exercice à faire à trois voix : un élève dit la forme ferme, un autre la "
             "forme générale, un troisième la forme douce. Le ton change plus que les "
             "mots, et c'est ce ton-là qu'il faut reconnaître au téléphone.")

    d.piege("Conjuguer le second verbe",
            "Je dois je téléphone au centre avant huit heures.",
            "Je dois téléphoner au centre avant huit heures.",
            "Après devoir et après falloir, le verbe qui suit reste à "
            "l'infinitif. C'est la faute la plus fréquente du niveau, et elle "
            "s'entend tout de suite.",
            notes="La corriger par reformulation plutôt que par explication : répéter "
                  "la phrase juste, une fois, et continuer. L'explication a déjà été "
                  "donnée en début de séance.")

    d.tableau('Ce que vous direz au téléphone', "Six phrases toutes faites",
              ['La situation', 'La phrase'],
              [["Vous vous engagez", "Je dois vous remettre une note."],
               ["Vous demandez", "Est-ce que je peux vous rappeler demain ?"],
               ["On vous explique", "Il faut téléphoner avant huit heures."],
               ["On vous suggère", "Il faudrait nous apporter le papier."],
               ["On vous rappelle", "Vous devez nous remettre une note signée."],
               ["On vous rassure", "Il ne faut pas attendre la fin du mois."]],
              cle=1,
              notes="Les trois premières sont dans votre bouche, les trois dernières "
                    "dans celle du secrétariat. Faire jouer les six par paires, debout, "
                    "dos à dos : au téléphone, on ne se voit pas.")

    d.billet(
        "Écrivez une phrase avec « je dois » et une avec « il faut », à "
        "propos de votre cours.",
        exemples=[
            "Le second verbe à l'infinitif dans les deux.",
            "Des choses vraies : ce que vous devez faire cette semaine.",
        ],
        notes="Ramasser. La faute de l'infinitif se voit d'un coup d'œil sur les "
              "billets ; ceux qui la font se revoient individuellement au début de B4.")

    return d.save(dossier)
