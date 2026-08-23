# -*- coding: utf-8 -*-
"""A2 · Demander, exiger, se renseigner
Bloc A « Je découvre » · couleur indigo · graphie-phonie et prosodie · 75 min.
Source : exercice `prTon` (douze cartes écoutables) et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Demander, exiger, se renseigner",
        chapeau="La même suite de mots peut demander, exiger ou "
                "s'informer. C'est la voix qui tranche, et c'est ce que "
                "l'autre entend en premier.",
        duree='75 minutes')

    d.titre(notes="Séance de prosodie. Elle passe souvent pour un supplément ; elle "
                  "est au contraire ce qui décide de la réponse qu'on obtiendra au "
                  "bloc B. Prévoir beaucoup d'écoute et peu d'explication.")

    d.objectifs([
        "entendre si une phrase demande, exige ou cherche une information ;",
        "faire monter la voix à la fin d'une demande ;",
        "reconnaître les cinq blocs du conditionnel à l'oreille ;",
        "poser une question de renseignement en appuyant le mot interrogatif.",
    ], notes="Le deuxième objectif est le seul qui se travaille physiquement : "
             "ralentir sur les trois derniers mots suffit à faire remonter la voix.")

    d.declencheur(
        'Écoute', "Deux phrases, les mêmes mots, deux effets",
        pistes=[
            "« Vous allez me l'écrire. » — qu'est-ce que vous entendez ?",
            "« Est-ce que vous accepteriez de me l'écrire ? » — et ici ?",
            "Laquelle des deux donne le choix à l'autre ?",
            "Dans votre langue, comment fait-on la différence ?",
        ],
        notes="Dire les deux phrases soi-même, deux fois chacune, sans les écrire au "
              "tableau. L'écrit efface justement ce qu'on veut faire entendre.")

    d.cartes('Analyse', "Trois intentions, trois mélodies", [
        ("On demande", "La voix monte à la fin et le débit ralentit sur les derniers mots. Le conditionnel aide : accepteriez, pourriez, aimeriez."),
        ("On exige", "La voix descend nettement et le débit se raidit. Rien n'est offert, et l'autre le sait avant la fin de la phrase."),
        ("On se renseigne", "La voix appuie sur le mot interrogatif — combien, quel jour, duquel — puis remonte à la fin."),
        ("Ce que ça change", "Une demande dite avec la voix d'une exigence devient un ordre. C'est le malentendu le plus fréquent, et il ne se voit pas à l'écrit."),
    ], notes="Une carte à la fois, en disant chaque exemple à voix haute. Faire "
             "répéter par le groupe entier avant de passer à la suivante.")

    d.pratique('Écoute', "Demande, exigence ou renseignement ?",
               "Écoutez chaque phrase et dites ce que la voix fait entendre.", [
        ("Est-ce que vous accepteriez de me le mettre par écrit ?", "on demande"),
        ("Vous allez me le mettre par écrit.", "on exige"),
        ("À partir de quel jour est-ce que le délai commence à courir ?", "on se renseigne"),
        ("Je veux un vitrier avant vendredi.", "on exige"),
        ("Pourriez-vous m'accorder une semaine avant de répondre ?", "on demande"),
        ("Combien y a-t-il exactement dans le fonds de prévoyance ?", "on se renseigne"),
    ], corrige=True,
       notes="Les six premières cartes de l'exercice prTon. Les dire soi-même plutôt "
             "que de faire jouer l'audio : on peut alors exagérer, puis atténuer.")

    d.regle("La voix monte, la porte reste ouverte",
            "Une demande se termine plus haut qu'elle n'a commencé.",
            precision="Le geste est physique et il n'a rien à voir avec la politesse "
                      "des mots : ralentir sur les trois derniers mots fait remonter la "
                      "voix toute seule. Un débit rapide, au contraire, fait tomber la "
                      "fin de la phrase — et une demande dont la fin tombe s'entend "
                      "comme un ordre, même avec « s'il vous plaît ».",
            notes="Diapositive à photographier. Faire l'expérience : la même phrase "
                  "dite vite, puis dite lentement. Le groupe entend la différence sans "
                  "qu'on ait à l'expliquer.")

    d.pratique('Prononciation', "Les cinq blocs à connaître par cœur",
               "Répétez chaque bloc trois fois, puis finissez la phrase.", [
        ("je pourrais", "Je pourrais repasser demain."),
        ("je voudrais", "Je voudrais une réponse écrite."),
        ("j'aimerais", "J'aimerais qu'on en discute."),
        ("ce serait", "Ce serait plus simple pour nous deux."),
        ("il faudrait", "Il faudrait fixer une date."),
    ], corrige=True,
       notes="Ces cinq blocs ouvrent la moitié des phrases du bloc B. Les faire "
             "apprendre comme des mots, sans analyse grammaticale : le conditionnel "
             "sera expliqué en B3, pas ici.")

    d.piege('Prononciation',
            "Je veux une réponse écrite.",
            "Je voudrais une réponse écrite.",
            "Les deux demandent exactement la même chose. La première ne laisse rien "
            "à l'autre ; la seconde lui laisse le geste d'accepter. Dans une "
            "négociation, cette différence-là vaut plus que n'importe quel argument.",
            notes="Demander au groupe laquelle des deux ils emploieraient avec un "
                  "propriétaire, puis laquelle avec un ami. La réponse est la même, et "
                  "c'est le point.")

    d.billet(
        "Écris une demande que tu as vraiment à faire, au conditionnel.",
        exemples=[
            "À ton propriétaire, à ton employeur, à l'école.",
            "Une phrase, avec « pourriez-vous » ou « j'aimerais ».",
        ],
        notes="Deux minutes. Ramasser les billets : ils servent en B3, où le "
              "conditionnel sera repris avec leurs propres phrases.")

    return d.save(dossier)
