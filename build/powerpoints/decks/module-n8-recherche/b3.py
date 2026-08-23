# -*- coding: utf-8 -*-
"""B3 · La question qui se pose à l'envers
Bloc B « Défi 1 » · couleur teal · 75 min.
Source : exercice `t1inter` et sa mini-leçon. Savoirs du niveau 8 :
l'interrogation par inversion avec reprise du GN sujet, et la variété de
langue dont il faut tenir compte.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='teal',
        titre="Trois hauteurs pour une même question",
        chapeau="« L'équipe existe déjà ? » « Est-ce que l'équipe existe "
                "déjà ? » « L'équipe existe-t-elle déjà ? » Les trois sont "
                "correctes. Ce qui les sépare est la distance.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire de la phrase, mais le vrai sujet est le "
                  "registre. Annoncer d'emblée qu'aucune des trois formes n'est "
                  "fautive : on choisit la distance qui convient à la personne.")

    d.objectifs([
        "poser une question aux trois hauteurs de langue ;",
        "laisser le nom sujet devant et le reprendre par un pronom ;",
        "placer le « t » de liaison entre deux traits d'union ;",
        "choisir la forme selon l'interlocuteur, pas selon la difficulté.",
    ], notes="Le quatrième objectif est celui qu'on rate : un élève qui vient "
             "d'apprendre l'inversion l'emploie partout, y compris avec un "
             "contremaître, où elle sonne raide.")

    d.declencheur(
        'Observation', "À qui diriez-vous laquelle ?",
        pistes=[
            "« La formation est payée ? »",
            "« Est-ce que la formation est payée ? »",
            "« La formation est-elle payée ? »",
            "Un collègue sur le plancher, une conseillère au téléphone, une lettre.",
        ],
        notes="Faire répartir les trois formes entre les trois destinataires. Le "
              "groupe y arrive seul, et c'est plus solide que de le lui dire.")

    d.regle("Le nom sujet reste devant",
            "Quand le sujet est un nom, on ne le déplace pas : on le laisse "
            "en tête et on le reprend derrière le verbe par un pronom de la "
            "troisième personne.",
            precision="Le poste comporte-t-il une part de recrutement ? L'échelle "
                      "est-elle communiquée ? On ne dit jamais « comporte le poste ». "
                      "Le pronom s'accorde avec le nom : le poste donne il, l'échelle "
                      "donne elle, les documents donnent ils.",
            notes="Diapositive à photographier. C'est la règle centrale et elle tient "
                  "en une ligne : le nom devant, le pronom derrière.")

    d.cartes('Analyse', "Trois choses à ne pas rater", [
        ("Le « t » de liaison",
         "Si le verbe finit par une voyelle, on insère un -t- entre deux "
         "traits d'union : existe-t-elle, décidera-t-il, a-t-elle. Deux "
         "traits d'union, jamais un seul, et aucune apostrophe."),
        ("Aux temps composés",
         "L'inversion porte sur l'auxiliaire, jamais sur le participe. "
         "L'usine a-t-elle été rachetée ? Les postes ont-ils été affichés ? "
         "Le participe reste après le pronom, à sa place."),
        ("Avec un mot interrogatif",
         "Il passe devant tout, et l'inversion suit. Combien de personnes "
         "l'équipe compte-t-elle ? Pourquoi ce poste a-t-il été créé ?"),
    ], notes="Les trois se vérifient à l'écrit, pas à l'oreille. Faire écrire les "
             "exemples au tableau plutôt que de les dicter.")

    d.pratique('Pratique 1 de 2', "Passez à l'inversion",
               "Réécrivez la question sans « est-ce que ».", [
        ("Est-ce que l'équipe existe déjà ?", "L'équipe existe-t-elle déjà ?"),
        ("Est-ce que le poste comporte du recrutement ?", "Le poste comporte-t-il du recrutement ?"),
        ("Est-ce que l'échelle est communiquée ?", "L'échelle est-elle communiquée ?"),
        ("Est-ce que l'usine a été rachetée en janvier ?", "L'usine a-t-elle été rachetée en janvier ?"),
        ("Est-ce que le comité décidera cette semaine ?", "Le comité décidera-t-il cette semaine ?"),
        ("Pourquoi est-ce que ce poste a été créé ?", "Pourquoi ce poste a-t-il été créé ?"),
    ], corrige=True,
       notes="La troisième ne prend pas de -t- : « est » finit par une consonne. C'est "
             "l'erreur la plus fréquente de l'exercice, et elle vient de l'excès de "
             "zèle, pas de l'ignorance.")

    d.piege('Piège', "« Est-ce que le poste comporte-t-il... »",
            "choisir une seule des deux formes",
            "Cumuler « est-ce que » et l'inversion double la question. C'est "
            "la faute qui trahit le plus sûrement quelqu'un qui vise la forme "
            "soutenue sans la maîtriser — et elle se produit précisément quand "
            "on veut bien faire. Une forme, pas deux.",
            notes="Écrire la phrase fautive au tableau et la faire corriger de deux "
                  "façons différentes. Les deux sont bonnes.")

    d.tableau('Application', "Huit questions prêtes pour un appel",
              ['La question', 'Ce qu\'elle vous apprend'],
              [["L'équipe existe-t-elle, ou faut-il la constituer ?",
                "poste neuf ou remplacement"],
               ["Pourquoi ce poste a-t-il été créé ?",
                "celle qui rapporte le plus"],
               ["À qui la personne rendra-t-elle compte ?",
                "le supérieur immédiat"],
               ["Le processus comporte-t-il d'autres étapes ?",
                "de quoi se préparer"],
               ["Quand la décision sera-t-elle prise ?",
                "quand relancer, sans harceler"]],
              cle=0,
              notes="Diapositive à photographier, et à recopier dans le cahier. Ces "
                    "cinq questions se posent telles quelles dans n'importe quel "
                    "appel de présélection, quel que soit le métier.")

    d.pratique('Pratique 2 de 2', "Vos questions, à la troisième hauteur",
               "Reprenez vos trois questions de B2 et posez-les à l'inversion.", [
        ("Question 1", "nom sujet devant, pronom derrière"),
        ("Question 2", "attention au -t- de liaison"),
        ("Question 3", "aux temps composés, on inverse l'auxiliaire"),
    ], corrige=False,
       notes="Troisième passage sur les mêmes phrases : familier en B1, conditionnel "
             "en B2, inversion ici. Faire lire deux ou trois productions à voix "
             "haute, debout, avec la mélodie de A2.")

    d.billet(
        "Trouvez une vraie offre d'emploi et écrivez trois questions à l'inversion.",
        exemples=[
            "Une sur ce que l'annonce ne dit pas.",
            "Une avec un mot interrogatif en tête.",
        ],
        notes="Devoir. Ce sont ces questions-là qui serviront au bloc C, quand on "
              "lira un profil d'entreprise et une offre complète.")

    return d.save(dossier)
