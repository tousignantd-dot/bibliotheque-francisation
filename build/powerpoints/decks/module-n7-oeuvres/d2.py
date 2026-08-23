# -*- coding: utf-8 -*-
"""D2 · Accorder, supposer, annoncer
Bloc D « Défi 3 » · couleur ambre · écriture et grammaire · 75 min.
Source : exercices `t3conc`, `t3si`, `t3conn` et `t3crit` (type texte).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Accorder, supposer, annoncer",
        chapeau="Trois outils, et une réunion tient debout : la concession "
                "pour accorder, l'hypothèse pour déplacer sans attaquer, les "
                "connecteurs pour dire où l'on en est.",
        duree='75 minutes')

    d.titre(notes="Séance dense : trois points de langue et une lecture. Si le temps "
                  "manque, sacrifier la lecture de la critique, qui se fait très bien "
                  "à l'écran, et garder la concession et l'hypothèse.")

    d.objectifs([
        "employer « bien que » avec le subjonctif et « même si » avec l'indicatif ;",
        "transformer un adjectif en nom après « malgré » ;",
        "poser une hypothèse avec « si » plus imparfait, puis conditionnel ;",
        "employer quant à, autrement dit, en somme, par conséquent.",
    ], notes="Les quatre objectifs sont ceux de la lettre de E2. Le deuxième est le "
             "plus technique : la nominalisation est la marque de la langue écrite.")

    d.declencheur(
        'Préparation', "Comment dit-on non sans dire non ?",
        pistes=[
            "« Si le budget était plus grand, je proposerais l'humour. » Est-ce un non ?",
            "Qui est contredit dans cette phrase ?",
            "Pourquoi est-ce plus facile à entendre ?",
            "Avez-vous déjà employé cette tournure sans le savoir ?",
        ],
        notes="La deuxième piste est la clé : personne n'est contredit, et pourtant "
              "le refus est complet. C'est l'outil le plus courtois d'une réunion.")

    d.tableau('Analyse', "Trois marqueurs, trois constructions",
              ['Le marqueur', 'Ce qui suit'],
              [["bien que", "le subjonctif : bien que le film soit lent"],
               ["même si", "l'indicatif : même si le film est lent"],
               ["malgré", "un nom : malgré sa lenteur"]],
              cle=0,
              note="La concession se place avant votre position, jamais après.",
              notes="Diapositive à photographier. La note est la moitié de la leçon : "
                    "la deuxième moitié de la phrase est celle qu'on retient.")

    d.cartes('Analyse', "Transformer l'adjectif en nom", [
        ("lent", "la lenteur"),
        ("long", "la longueur"),
        ("cher", "le prix"),
        ("petit", "la petite taille"),
        ("court", "la brièveté"),
        ("difficile", "la difficulté"),
    ], cols=2,
       notes="Six transformations à faire par écrit. La nominalisation revient dans "
             "toute lettre formelle : c'est un investissement, pas un caprice.")

    d.regle("Après « si », l'imparfait. Jamais le conditionnel",
            "« Si j'avais le temps, je viendrais » — et non « si j'aurais ».",
            precision="Le conditionnel se tient de l'autre côté de la virgule. Il se "
                      "fabrique avec le radical du futur et les terminaisons de "
                      "l'imparfait : il y a toujours un r avant la terminaison. Le "
                      "même temps sert à demander poliment : pourriez-vous, je "
                      "voudrais, il faudrait.",
            notes="Diapositive à photographier. C'est la faute la plus reconnaissable "
                  "du français, et elle se corrige en une leçon si on la nomme.")

    d.tableau('Analyse', "Six mots qui tiennent une discussion",
              ['Le mot', 'Ce qu\'il annonce'],
              [["quant à", "je passe au point suivant"],
               ["en ce qui concerne", "je cadre l'aspect dont je vais parler"],
               ["autrement dit", "je redis la même chose plus simplement"],
               ["en somme", "je ramasse tout avant de conclure"],
               ["par conséquent", "je tire la suite logique"],
               ["cela dit", "je nuance ce que je viens d'affirmer"]],
              cle=0,
              notes="Diapositive à photographier. Six rangées sans note, c'est la "
                    "limite : les libellés de gauche restent courts pour que rien ne "
                    "se replie.")

    d.piege('Grammaire',
            "« Bien que le film est lent, il tient. »",
            "« Bien que le film soit lent, il tient. »",
            "Après « bien que », l'indicatif n'existe pas. Si le subjonctif ne "
            "vient pas au moment de parler, changez de marqueur : « même s'il "
            "est lent » dit exactement la même chose et ne fait jamais de "
            "faute de mode.",
            notes="La sortie de secours est aussi utile que la règle : un élève qui "
                  "hésite doit avoir une phrase de rechange, pas un blanc.")

    d.pratique('Grammaire', "Accordez, puis maintenez",
               "Employez le marqueur demandé et la bonne forme.", [
        ("(bien que + être) ___ le début ___ lent, la deuxième heure tient.", "Bien que le début soit lent"),
        ("(même si + coûter) ___ le billet ___ trente-quatre dollars, il entre au budget.", "Même si le billet coûte"),
        ("(malgré + nom) ___ sa ___, le film ne m'a jamais perdue.", "Malgré sa lenteur"),
        ("(bien que + pouvoir) ___ on ___ regarder un film chez soi, une salle change l'écoute.", "Bien qu'on puisse"),
        ("(si + imparfait) Si le budget ___ plus grand, je ___ l'humour.", "était, proposerais"),
        ("(politesse) ___ -vous nous réserver dix places ?", "Pourriez"),
    ], corrige=True,
       notes="Exercices `t3conc` et `t3si` du module, qui en comptent huit chacun. "
             "Les six d'ici couvrent les six formes ; le reste à l'écran.")

    d.pratique('Lecture', "La critique du Courrier",
               "Fait, opinion, ou nuance ?", [
        ("Le film dure une heure cinquante.", "un fait : on peut vérifier"),
        ("Le premier quart d'heure m'a paru interminable.", "une opinion, sans appui"),
        ("Aucune parole n'est échangée avant la douzième minute.", "un fait, qui appuie l'opinion"),
        ("Bien que le rythme demeure lent, la deuxième heure tient.", "une nuance : concession"),
        ("C'est la plus belle scène du film.", "une opinion, la plus forte du texte"),
        ("À voir, mais pas un soir de fatigue.", "la recommandation, et sa condition"),
    ], corrige=True,
       notes="Exercice `t3crit` du module, qui compte onze questions. Faire remarquer "
             "que la condition finale est la partie la plus utile de toute la "
             "critique.")

    d.billet(
        "Écrivez la phrase de concession que vous emploierez jeudi.",
        exemples=[
            "Avec « bien que » et un subjonctif, ou « malgré » et un nom.",
            "Suivie de votre position, dans la même phrase.",
        ],
        notes="Fin du bloc D. Ces phrases entrent telles quelles dans l'exposé de E1 "
              "et dans le compte rendu de E2 : les faire garder.")

    return d.save(dossier)
