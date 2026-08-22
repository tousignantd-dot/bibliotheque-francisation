# -*- coding: utf-8 -*-
"""B2 · Poser sa question : trois façons.
Bloc B « Défi 1 · Quand, combien, quoi apporter ? » · teal · 75 min.
Source du module : exercice `t1quest`, mini-leçon `t1quest`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='teal',
        titre="Poser sa question : trois façons",
        chapeau="Beaucoup de gens n'osent pas téléphoner parce qu'ils "
                "cherchent la bonne façon de poser leur question. Il n'y en a "
                "pas une : il y en a trois, et les trois marchent. La plus "
                "courte est même la plus fréquente.",
        duree='75 minutes')

    d.titre(notes="Séance charnière du module. Le message à faire passer tient en une "
                  "phrase : aucune des trois formes n'est impolie, et la plus simple "
                  "est celle qu'on emploie le plus au téléphone.")

    d.objectifs([
        "poser une question avec le mot de question seul ;",
        "poser une question avec « est-ce que » ;",
        "reconnaître la question où le sujet passe après le verbe ;",
        "comprendre la particule -tu, qu'on entend partout au Québec.",
    ])

    d.tableau('Analyse', "La même question, trois façons",
              ["La façon", "Exemple", "Où on l'entend"],
              [["le mot de question seul", "C'est quand ?", "au téléphone, tout le temps"],
               ["avec est-ce que", "Est-ce que ça commence bientôt ?", "partout, à l'oral comme à l'écrit"],
               ["le sujet après le verbe", "Quand commence la session ?", "sur les feuillets, dans les services"],
               ["la particule -tu", "Ça commence-tu cette semaine ?", "au Québec, à l'oral seulement"]],
              cle=1,
              note="Aucune n'est impolie. Ce qui rend poli, c'est bonjour, s'il vous plaît et merci.",
              notes="Diapo à photographier. Insister sur la dernière colonne : c'est elle "
                    "qui règle la question « laquelle dois-je employer ? ». Réponse : "
                    "celle qui sort le plus facilement.")

    d.regle("La façon la plus simple",
            "« C'est quand ? » · « C'est combien ? » · « C'est où ? »",
            precision="Deux ou trois mots, et on comprend très bien. C'est la forme la "
                      "plus employée au téléphone, par tout le monde, y compris par les "
                      "gens dont le français est la langue maternelle. Ajoutez « s'il "
                      "vous plaît » si vous voulez l'adoucir.",
            notes="Diapo à photographier. La faire dire à voix haute par tout le groupe, "
                  "trois fois. C'est la phrase qui débloque l'appel téléphonique.")

    d.cartes("Les deux autres façons", "À reconnaître, puis à employer", [
        ("Est-ce que…",
         "Se pose devant une phrase normale, sans rien changer d'autre : « Il faut "
         "apporter quelque chose » devient « Est-ce qu'il faut apporter quelque chose ? ». "
         "Devant une voyelle, on écrit « est-ce qu' »."),
        ("Quand est-ce que…",
         "Le mot de question passe en avant, puis « est-ce que » : « Quand est-ce que ça "
         "commence ? », « Combien est-ce que ça coûte ? ». Plus long, tout aussi juste."),
        ("Combien coûte la session ?",
         "Le sujet passe après le verbe. On la lit sur les feuillets et on l'entend dans "
         "les services. À reconnaître d'abord ; à employer quand on se sentira prêt."),
        ("Ça commence-tu cette semaine ?",
         "Le « tu » collé au verbe ne veut pas dire « toi » : il transforme la phrase en "
         "question. C'est du français d'ici, très courant. À comprendre, pas à écrire."),
    ], notes="La quatrième carte surprend toujours. Prendre le temps : un élève qui ne "
             "l'a jamais entendue explicitement croit qu'on lui parle familièrement.")

    d.piege('Le piège', "C'est quand combien où quoi apporter ?",
            "C'est quand ? … C'est combien ? … Il faut apporter quoi ?",
            "Une question à la fois. Laissez la personne répondre avant de poser la "
            "suivante : c'est plus facile pour elle, et surtout pour vous — quatre "
            "réponses données d'un coup ne se retiennent pas.",
            notes="C'est l'erreur de celui qui a préparé son appel et veut tout dire avant "
                  "d'avoir peur. La nommer sans moquerie : elle vient du trac, pas de "
                  "l'ignorance.")

    d.pratique('Production · 1 de 2', "Écrivez la question",
               "Pour chaque renseignement cherché, écrivez une question. "
               "Plusieurs réponses sont possibles.", [
        ("Vous voulez savoir le jour et l'heure du badminton.",
         "C'est quand ? · Quand est-ce que c'est ? · C'est à quelle heure ?"),
        ("Vous voulez savoir le prix d'une séance.",
         "C'est combien ? · Combien est-ce que ça coûte ? · Ça coûte combien ?"),
        ("Vous voulez savoir dans quelle salle ça se passe.",
         "C'est où ? · Où est-ce que c'est ? · C'est dans quelle salle ?"),
        ("Vous voulez savoir ce qu'il faut apporter.",
         "Qu'est-ce qu'il faut apporter ? · Est-ce qu'il faut apporter quelque chose ?"),
        ("Vous voulez savoir quand la session commence.",
         "Quand est-ce que la session commence ? · Quand commence la session ?"),
        ("Vous voulez savoir si votre enfant de huit ans peut venir.",
         "Est-ce que ma fille peut venir ? · Est-ce que c'est pour les enfants aussi ?"),
    ], corrige=True,
       notes="C'est l'exercice t1quest du module. Accepter toute question qui va "
             "chercher le bon renseignement : le corrigé donne des exemples, pas une "
             "liste fermée.")

    d.pratique('Production · 2 de 2', "Deux par deux, au téléphone",
               "Dos à dos, sans se voir. L'un pose ses quatre questions, l'autre invente "
               "les réponses. Puis on échange.", [
        ("Celui qui appelle", "salue, dit ce qu'il cherche, pose une question à la fois"),
        ("Celui qui répond", "répond court, une information par réplique"),
        ("Celui qui appelle", "fait répéter au moins une fois : « Pardon ? »"),
        ("Celui qui appelle", "récapitule les quatre renseignements avant de raccrocher"),
        ("Celui qui répond", "confirme : « C'est exactement ça. »"),
    ], notes="Dos à dos, c'est le point de la consigne : sans le visage, on écoute "
             "vraiment. Circuler et noter les récapitulations réussies, pas les erreurs.")

    d.billet(
        "Écrivez la même question de trois façons différentes.",
        exemples=[
            "Prenez la question du prix, ou celle du matériel.",
            "Une ligne par façon, dans l'ordre du tableau de la séance.",
        ],
        notes="Devoir court. Il prépare B3, où la même question sera reprise à la forme "
              "polie — « je voudrais », « vous pourriez ».")

    return d.save(dossier)
