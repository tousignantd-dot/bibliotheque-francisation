# -*- coding: utf-8 -*-
"""B4 · Les mots du loisir et du sport.
Bloc B · couleur acier · 60 min.
Source : exercices `t1sport` et `t1relGN`, cartes mémoire, dialogue `appli`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-relations/images/')


def build(dossier):
    d = Deck(
        code='B4', section='acier',
        titre='Les mots du loisir et du sport',
        chapeau="S'entraîner, disputer un match, marquer, battre : six verbes "
                "suffisent pour parler de n'importe quel sport d'équipe. Et "
                "trois mots pour se rendre à l'activité.",
        duree='60 minutes')

    d.titre(notes="Séance de vocabulaire qui clôt le bloc B. Prévoir dix minutes à la fin "
                  "pour le dialogue du tournoi, qui sert de transition vers la suite.")

    d.objectifs([
        "employer six verbes du sport avec le bon complément ;",
        "nommer les lieux et les personnes d'une activité de quartier ;",
        "parler d'un loisir que je pratique ou que je voudrais pratiquer ;",
        "comprendre une conversation entre deux personnes qui ne se connaissent pas.",
    ])

    d.declencheur(
        'Observation', "Que se passe-t-il ici ? Quels mots connaissez-vous déjà ?",
        image=IMG + 'gymnase.jpg',
        pistes=[
            "Comment s'appelle cet endroit ? Et le filet ?",
            "Quel jour de la semaine y va-t-on, d'habitude ?",
            "Faut-il payer ? Faut-il s'inscrire ?",
            "Y a-t-il un endroit comme celui-là près de chez vous ?",
        ],
        notes="La dernière piste est la plus importante : plusieurs élèves ignorent qu'il "
              "existe un centre communautaire dans leur quartier. Avoir l'adresse du "
              "centre local sous la main.")

    d.vocabulaire('Vocabulaire · 1 de 2', "Six verbes du sport", [
        ("s'entraîner", "Pratiquer souvent pour devenir meilleur."),
        ("disputer un match", "Jouer une partie contre une autre équipe."),
        ("battre une équipe", "Gagner contre elle."),
        ("marquer", "Faire un point."),
        ("servir", "Lancer le ballon pour commencer l'échange."),
        ("participer", "Prendre part à l'activité avec les autres."),
    ], notes="« Disputer un match » surprend souvent : le verbe n'a rien d'agressif ici. "
             "Donner aussi la forme courante « jouer un match ».")

    d.vocabulaire('Vocabulaire · 2 de 2', "Les lieux et les gens", [
        ("un centre communautaire", "Un endroit du quartier pour le sport et les activités."),
        ("une ligue", "Un groupe d'équipes qui jouent les unes contre les autres."),
        ("une coéquipière", "Une personne de la même équipe que soi."),
        ("un tournoi", "Une compétition sur une ou deux journées."),
        ("le covoiturage", "Voyager à plusieurs dans la même voiture."),
    ], notes="Ces cinq mots sont dans le banc de vocabulaire du module. Les élèves peuvent "
             "les réviser avec les cartes mémoire, en autonomie.")

    d.tableau('Analyse', "Le verbe et son complément",
              ['On dit', 'On ne dit pas'],
              [["s'entraîner le dimanche", "entraîner le dimanche"],
               ["disputer un match", "disputer un jeu"],
               ["marquer un point", "marquer un but au volleyball"],
               ["participer à une activité", "participer une activité"]],
              cle=0,
              note="La quatrième ligne est la plus coûteuse : participer demande toujours à.",
              notes="Faire produire une phrase complète pour chaque ligne de gauche.")

    d.piege('Le verbe pronominal, encore',
            "Je entraîne le dimanche matin.",
            "Je m'entraîne le dimanche matin.",
            "Comme « se lever » vu en A4, « s'entraîner » a besoin de son petit mot. "
            "« Entraîner » sans le pronom veut dire autre chose : entraîner une équipe, "
            "c'est en être l'entraîneur.",
            notes="Rappeler A4. Cette famille de verbes reviendra au passé composé en C2, "
                  "avec l'auxiliaire être — l'annoncer.")

    d.dialogue('Dialogue', 'Au tournoi de Drummondville', [
        ("MARIAMA", "Excuse-moi, c'est bien ici, le vestiaire des équipes de Longueuil ?", False),
        ("OLIVIER", "Oui, entre. Moi, c'est Olivier, je joue pour Saint-Hubert. Toi, tu es avec Chantal ?", True),
        ("MARIAMA", "Mariama. Oui, c'est elle qui m'a amenée. Je joue avec elles depuis l'automne.", True),
        ("OLIVIER", "Depuis l'automne seulement ? Tu as l'air de jouer depuis dix ans.", False),
    ], consigne="Écoutez le début du dialogue. La suite sera travaillée en E1.",
       notes="Ne présenter que ce début : le dialogue complet sert de modèle au jeu de rôle "
             "de E1. Faire remarquer la présentation en trois mots — le prénom, l'équipe, "
             "depuis quand.")

    d.pratique('Pratique', "Le mot juste",
               "Complétez avec le mot du vocabulaire.", [
        ("On fait du ___ : Chantal passe me chercher le jeudi.", "covoiturage"),
        ("Mes ___ m'ont appelée quand j'ai manqué deux jeudis.", "coéquipières"),
        ("Le ___ dure deux jours, à Drummondville.", "tournoi"),
        ("Je m'___ toute seule le dimanche, au parc.", "entraîne"),
        ("Le volleyball a lieu au ___ communautaire.", "centre"),
        ("Notre équipe a ___ celle de Saint-Hubert.", "battu"),
    ], corrige=True,
       notes="La dernière ligne demande un participe passé : c'est une amorce du bloc C. "
             "L'accepter sans l'expliquer.")

    d.billet(
        "Décrivez en quatre phrases un loisir que vous pratiquez ou aimeriez pratiquer.",
        exemples=[
            "Où ? Quand ? Avec qui ? Depuis quand ?",
            "Employez au moins deux verbes de la première diapositive de vocabulaire.",
        ],
        notes="Bilan du bloc B. Garder les billets : ils alimentent le jeu de rôle de E1.")

    return d.save(dossier)
