# -*- coding: utf-8 -*-
"""B2 · Cinq façons de faire rire, et leurs noms
Bloc B « Défi 1 » · couleur acier · compréhension écrite · 75 min.
Source : exercices `t1trans` (type texte) et `t1proc`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='acier',
        titre="Cinq façons de faire rire, et leurs noms",
        chapeau="Écrit, un sketch ne fait plus rire. C'est exactement ce qu'on "
                "cherche : sans le ton ni la salle, on voit enfin où le "
                "procédé se trouve.",
        duree='75 minutes')

    d.titre(notes="Séance de lecture. Distribuer la transcription sur papier : les "
                  "élèves doivent pouvoir souligner. L'exercice à l'écran vient "
                  "après, pas avant.")

    d.objectifs([
        "lire la transcription d'un sketch et y repérer les procédés ;",
        "nommer l'ironie, le sarcasme, la caricature, le burlesque, l'absurde ;",
        "distinguer une ironie d'un sarcasme par sa cible ;",
        "repérer les paroles rapportées dans un texte suivi.",
    ], notes="Le troisième objectif évite un malentendu fréquent : un spectacle "
             "entier peut être ironique sans un seul sarcasme, et c'est le cas ici.")

    d.declencheur(
        'Préparation', "Pourquoi écrire une chose qui se dit ?",
        pistes=[
            "Qu'est-ce qu'on perd en transcrivant un sketch ?",
            "Qu'est-ce qu'on gagne ?",
            "Peut-on citer un passage précis sans transcription ?",
            "Est-ce qu'un texte drôle se relit plusieurs fois ?",
        ],
        notes="La troisième piste est la réponse : pour dire « le passage où il dit "
              "que la pièce est heureuse », il faut pouvoir y revenir. C'est ce que "
              "l'élève fera en E1.")

    d.tableau('Analyse', "Trois repères pour lire un sketch",
              ['Ce qu\'on cherche', 'Où ça se trouve'],
              [["Ce qui ne peut pas être vrai",
                "presque toujours le lieu du procédé"],
               ["Les changements de voix",
                "deux-points, guillemets, il dit, je lui réponds"],
               ["La chute",
                "la dernière phrase, courte, jamais expliquée"]],
              cle=0,
              note="Chercher dans cet ordre : le faux, les voix, puis la fin.",
              notes="Diapositive à photographier. Les trois repères valent pour tout "
                    "texte humoristique, pas seulement pour celui-ci.")

    d.cartes('Analyse', "Six procédés, six définitions", [
        ("l'ironie", "dire le contraire de ce qu'on pense, et être compris"),
        ("le sarcasme", "une ironie qui vise quelqu'un et qui veut faire mal"),
        ("la caricature", "garder deux ou trois traits, et exagérer ceux-là"),
        ("le burlesque", "faire rire par le corps, la chute, le geste maladroit"),
        ("l'absurde", "pousser une idée jusqu'où plus rien ne tient debout"),
        ("l'autodérision", "rire de soi avant que les autres n'en aient l'idée"),
    ], cols=2,
       notes="Exercice `t1proc` du module. Faire chercher dans l'extrait un exemple "
             "de chacun : cinq s'y trouvent, le sarcasme non. C'est la découverte "
             "de la séance.")

    d.regle("L'ironie vise une situation, le sarcasme vise une personne",
            "Les deux disent le contraire de ce qu'ils pensent. Seul le second "
            "cherche à blesser.",
            precision="Réjean Cadorette est ironique d'un bout à l'autre et il n'est "
                      "sarcastique nulle part : il ne s'en prend ni à la cliente, ni "
                      "au gérant, ni à lui-même. Confondre les deux fait dire d'un "
                      "humoriste doux qu'il est méchant.",
            notes="Diapositive à photographier. Le mot « sarcasme » est souvent "
                  "employé par les élèves pour toute moquerie : la distinction se "
                  "fait à la cible, pas au ton.")

    d.tableau('Analyse', "Quatre passages, quatre procédés",
              ['Le passage', 'Ce qu\'il fait'],
              [["J'adore ça, attendre",
                "dit le contraire de ce qu'il pense"],
               ["Une chemise bleue, un écran",
                "garde trois traits du gérant et jette le reste"],
               ["Elle est heureuse",
                "donne une vie à une pièce d'entrepôt"],
               ["Derrière la porte barrée",
                "pousse l'idée jusqu'à l'impossible"]],
              cle=0,
              notes="Diapositive à photographier. Le quatrième est le plus difficile "
                    "à faire sentir : rien n'est impossible dans la phrase prise "
                    "isolément, c'est le sérieux du ton qui la rend absurde.")

    d.piege('Lecture',
            "« Il vient de le dire, donc il le pense. »",
            "« Il vient de le dire, et rien ne peut être vrai là-dedans. »",
            "C'est l'erreur de Gaétan dans le dialogue, et elle est très "
            "commune chez qui apprend une langue : on s'accroche aux mots, "
            "parce que les mots sont ce qu'on a mis le plus d'efforts à "
            "comprendre. Le français écrit ne signale l'ironie par aucun signe.",
            notes="Point de compréhension, pas de grammaire. Rassurer : ce n'est pas "
                  "un manque de vocabulaire, c'est une habitude de lecture qui "
                  "s'acquiert.")

    d.pratique('Lecture', "Où est le procédé ?",
               "Retrouvez dans la transcription le passage qui répond.", [
        ("Quelle phrase dit le contraire de ce qu'il pense ?", "j'adore ça, attendre"),
        ("Où donne-t-il le nom officiel d'une situation pénible ?", "on appelle ça le service à la clientèle"),
        ("Quel passage caricature le gérant en trois traits ?", "un jeune homme très bien, très propre, une chemise bleue"),
        ("Où fait-il d'une pièce une personne heureuse ?", "elle est heureuse, dans le système"),
        ("Quelle exagération termine l'extrait ?", "il est au deuxième, derrière la porte barrée"),
        ("Quelle est la chute de la première histoire ?", "Madame, moi ça fait trente ans"),
    ], corrige=True,
       notes="Exercice `t1trans` du module, qui compte dix questions. Six suffisent "
             "en classe ; les quatre autres se font à l'écran.")

    d.billet(
        "Nommez un procédé que vous avez déjà vu dans une émission d'ici.",
        exemples=[
            "Le procédé, et l'émission ou le spectacle.",
            "Une phrase, si vous vous en souvenez.",
        ],
        notes="Beaucoup d'élèves regardent des émissions québécoises sans en saisir "
              "l'humour. Les réponses disent lesquelles, et ce sont de bonnes "
              "recommandations à faire circuler.")

    return d.save(dossier)
