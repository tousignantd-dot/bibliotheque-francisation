# -*- coding: utf-8 -*-
"""B1 · Je voudrais des renseignements.
Bloc B « Défi 1 · Quand, combien, quoi apporter ? » · acier · 75 min.
Source du module : dialogue `t1`, exercice `t1vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Je voudrais des renseignements",
        chapeau="Marisol n'osait pas téléphoner. Elle prend le téléphone "
                "quand même, et la préposée répond à chacune de ses quatre "
                "questions. Quatre minutes, et l'activité est choisie.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 1. Demander d'abord qui a déjà téléphoné à un "
                  "service en français, et ce qui a été difficile. La réponse est presque "
                  "toujours la même : on ne voit pas la personne, et ça va vite.")

    d.objectifs([
        "comprendre un appel de renseignements du début à la fin ;",
        "repérer les quatre renseignements dans ce qu'on me répond ;",
        "comprendre le mot « session » et ce qu'il recouvre ;",
        "répéter ce que j'ai compris avant de raccrocher.",
    ])

    d.dialogue('Dialogue · 1 de 3', "Le jour et l'heure", [
        ("ROXANE", "Centre communautaire Pointe-Verte, bonjour.", True),
        ("MARISOL", "Bonjour. Je voudrais des renseignements sur le badminton, s'il vous plaît.", True),
        ("ROXANE", "Bien sûr. Le badminton libre, c'est le mardi soir, de sept heures à neuf heures.", True),
        ("MARISOL", "Le mardi soir. Toutes les semaines ?", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Deux choses à faire remarquer : la préposée annonce le nom du centre en "
             "décrochant, ce qui laisse le temps de se préparer ; et Marisol répète « le "
             "mardi soir » avant de poser sa question suivante. C'est la technique du "
             "module entier.")

    d.dialogue('Dialogue · 2 de 3', "Pardon, la session ?", [
        ("ROXANE", "Toutes les semaines, oui, jusqu'à la fin de la session.", False),
        ("MARISOL", "Pardon, la session ?", True),
        ("ROXANE", "La session d'automne : de septembre à décembre. Après, il y a la session d'hiver.", True),
        ("MARISOL", "D'accord. Et c'est combien ?", False),
    ], notes="« Pardon, la session ? » est la réplique la plus importante de la séance : "
             "un seul mot, et l'explication arrive. Le faire répéter par tout le groupe. "
             "C'est plus facile que « pouvez-vous répéter » et ça marche mieux, parce que "
             "ça dit exactement ce qu'on n'a pas compris.")

    d.dialogue('Dialogue · 3 de 3', "Le prix et le matériel", [
        ("ROXANE", "Trois dollars par séance. Vous payez à l'entrée du gymnase.", True),
        ("MARISOL", "Trois dollars. Est-ce qu'il faut apporter quelque chose ?", True),
        ("ROXANE", "Des espadrilles propres, obligatoirement. Le gymnase est un plancher de bois.", True),
        ("MARISOL", "Merci beaucoup. Alors mardi, sept heures, trois dollars, des espadrilles.", True),
    ], notes="La dernière réplique récapitule les quatre renseignements dans l'ordre où "
             "ils ont été demandés. C'est le geste à installer cette semaine : on répète, "
             "et la personne au bout du fil confirme ou corrige.")

    d.tableau('Analyse', "Les quatre renseignements de l'appel",
              ["La question de Marisol", "Ce que Roxane répond"],
              [["C'est quel jour ?", "le mardi soir, toutes les semaines"],
               ["C'est à quelle heure ?", "de sept heures à neuf heures"],
               ["C'est combien ?", "trois dollars par séance, payés à l'entrée"],
               ["Il faut apporter quoi ?", "des espadrilles propres et de l'eau"]],
              cle=0,
              note="Quatre questions, quatre réponses, et l'appel est fini.",
              notes="Diapo à photographier. Faire remarquer qu'aucune question n'est "
                    "longue : trois ou quatre mots suffisent, et c'est la réponse qui "
                    "porte l'information.")

    d.regle("Le geste à installer",
            "On répète ce qu'on a compris avant de raccrocher.",
            precision="« Alors mardi, sept heures, trois dollars, des espadrilles. » "
                      "Dix secondes, et l'erreur de soir est évitée. La personne au bout "
                      "du fil confirme — « c'est exactement ça » — ou corrige. Personne "
                      "n'a jamais trouvé ça impoli.",
            notes="Diapo à photographier. C'est le critère d'évaluation du bloc E : la "
                  "production orale demande explicitement cette récapitulation.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Marisol téléphone au centre pour s'inscrire tout de suite.",
         "faux — elle se renseigne avant de décider"),
        ("Le badminton libre a lieu de sept heures à neuf heures.", "vrai"),
        ("La session d'automne va de septembre à décembre.", "vrai"),
        ("Il faut payer trois dollars chaque fois qu'on vient.", "vrai — par séance"),
        ("Marisol doit apporter sa propre raquette.",
         "faux — on en prête sur place"),
        ("Les espadrilles doivent être propres à cause du plancher de bois.", "vrai"),
        ("À la fin, Marisol répète les quatre renseignements.", "vrai"),
    ], corrige=True,
       notes="C'est l'exercice t1vf du module. Faire justifier chaque « faux » par la "
             "réplique exacte : la première affirmation est celle qui distingue ce "
             "module du module 13 du niveau 4, où l'on s'inscrit pour de bon.")

    d.billet(
        "Écrivez les quatre questions que vous poseriez au téléphone.",
        exemples=[
            "Choisissez l'activité que vous avez notée à la séance A1.",
            "Une question par ligne, dans l'ordre où vous les poseriez.",
        ],
        notes="Devoir court. Les quatre questions écrites ce soir sont celles qu'on "
              "travaillera en B2 : chacun arrive avec les siennes.")

    return d.save(dossier)
