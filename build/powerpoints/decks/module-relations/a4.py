# -*- coding: utf-8 -*-
"""A4 · Les gestes de la semaine.
Bloc A « Je découvre » · couleur teal · 50 min.
Source : exercices `prImg`, `prJour` et `prVocab`, cartes mémoire.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-relations/images/')


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre='Les gestes de la semaine',
        chapeau="Huit photos, huit gestes qu'on fait toutes les semaines. "
                "Mettre le mot juste sur chacun, c'est pouvoir en parler à "
                "quelqu'un sans chercher ses mots.",
        duree='50 minutes')

    d.titre(notes="Séance courte, très visuelle. Elle clôt le bloc A : à la fin, chaque "
                  "élève doit pouvoir décrire sa semaine en six phrases.")

    d.objectifs([
        "nommer huit gestes de la vie quotidienne avec le mot exact ;",
        "situer chaque geste dans la semaine : quel jour, quel moment ;",
        "employer l'article juste : une brassée, la balayeuse, les ordures ;",
        "décrire ma propre semaine en six phrases enchaînées.",
    ])

    d.declencheur(
        'Observation', "Que fait cette personne ? En un mot précis.",
        image=IMG + 'brassee.jpg',
        pistes=[
            "Quel est le mot pour cette quantité de linge ?",
            "Quel jour faites-vous cela, chez vous ?",
            "Combien de fois par semaine ?",
            "Est-ce que quelqu'un d'autre le fait avec vous ?",
        ],
        notes="Attendre le mot « brassée ». S'il ne vient pas, ne pas le donner tout de "
              "suite : demander d'abord « une quoi de linge ? ». Le mot se retient mieux "
              "après un moment de recherche.")

    d.cartes('Les quatre gestes du ménage', "Le mot et le moment", [
        ("mettre une brassée",
         "Faire fonctionner la laveuse une fois. On dit aussi « partir une brassée ». "
         "Beaucoup de gens en font une le soir, en semaine."),
        ("passer la balayeuse",
         "Aspirer la poussière. « Balayeuse » est le mot québécois ; « aspirateur » se "
         "comprend partout."),
        ("sortir les ordures",
         "Mettre les déchets au bord de la rue. Chaque quartier a son jour — souvent le "
         "même que le bac de recyclage."),
        ("laver le plancher",
         "Se dit « laver », pas « nettoyer », quand on parle du plancher. « Faire le "
         "ménage » désigne l'ensemble."),
    ], notes="Insister sur les articles. Faire répéter « une brassée », « la balayeuse », "
             "« les ordures » — l'article fait partie du mot.")

    d.cartes('Les quatre autres gestes', "Le mot et le moment", [
        ("cuisiner pour la semaine",
         "Faire un grand chaudron le dimanche et congéler. C'est ce que fait Mariama, et "
         "c'est très courant chez les gens qui travaillent tôt."),
        ("se lever tôt",
         "« Je me lève à cinq heures et quart. » Verbe pronominal : le petit mot « me » "
         "n'est pas facultatif."),
        ("prendre l'autobus",
         "On dit « prendre » l'autobus, jamais « aller » l'autobus. L'arrêt peut être à "
         "« trois coins de rue »."),
        ("aller à l'entraînement",
         "La séance où on pratique un sport. Le tournoi, lui, arrive une fois par année."),
    ], notes="La deuxième carte annonce les verbes pronominaux, qui reviendront au bloc C "
             "avec l'auxiliaire être. Ne pas développer maintenant.")

    d.tableau('Situer dans la semaine', "Quand Mariama fait quoi",
              ['Moment', 'Ce qu\'elle fait'],
              [["Le matin, à 5 h 15", "elle se lève pour son quart de 7 heures"],
               ["Le jeudi après 16 h", "elle va jouer au volleyball"],
               ["Le samedi matin", "elle fait le ménage et sort les ordures"],
               ["Le dimanche", "elle cuisine pour toute la semaine"],
               ["Le soir, après le souper", "elle met une brassée"]],
              cle=1,
              notes="Cacher la colonne de droite et faire reconstituer de mémoire. Le "
                    "dialogue de A1 contient tout.")

    d.regle("L'article devant le jour",
            "« Le jeudi » veut dire tous les jeudis. « Jeudi », sans article, veut dire "
            "celui qui vient.",
            precision="« Je joue le jeudi » décrit une habitude. « Je joue jeudi » annonce "
                      "un seul soir. La différence tient à un mot de deux lettres, et elle "
                      "change complètement le sens d'une invitation.",
            notes="Faire produire les deux phrases par le groupe, avec un vrai exemple de "
                  "leur vie. C'est la diapo à photographier.")

    d.piege('Le verbe pronominal',
            "Je lève à cinq heures et quart.",
            "Je me lève à cinq heures et quart.",
            "« Lever » et « se lever » sont deux verbes différents : on lève un objet, on "
            "se lève de son lit. Le petit mot « me » n'est pas une politesse, c'est une "
            "partie du verbe. Sans lui, la phrase veut dire autre chose.",
            notes="Beaucoup de langues n'ont pas cette construction. Annoncer qu'elle "
                  "reviendra au passé composé, avec l'auxiliaire être.")

    d.pratique('Pratique', "Le mot juste",
               "Complétez avec le mot exact.", [
        ("Je pars une ___ de lavage avant de souper.", "brassée"),
        ("Le samedi, je passe la ___ dans tout le logement.", "balayeuse"),
        ("On sort le ___ de recyclage le mardi soir.", "bac"),
        ("Mon ___ de travail commence à sept heures.", "quart"),
        ("J'ai pris un ___ pour aller au tournoi.", "congé"),
        ("Le volleyball a lieu au ___ communautaire.", "centre"),
    ], corrige=True,
       notes="Ces six mots sont ceux du banc de vocabulaire du module. Les élèves peuvent "
             "les réviser seuls avec les cartes mémoire.")

    d.billet(
        "Décrivez votre semaine en six phrases, une par jour ou par moment.",
        exemples=[
            "Employez au moins trois mots vus aujourd'hui.",
            "Employez au moins un adverbe de fréquence de la séance A2.",
        ],
        notes="C'est le bilan du bloc A. Garder ces billets : ils serviront de brouillon à "
              "la production orale de E1.")

    return d.save(dossier)
