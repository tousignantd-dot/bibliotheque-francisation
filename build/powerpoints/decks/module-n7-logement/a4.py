# -*- coding: utf-8 -*-
"""A4 · Deux mondes, deux vocabulaires
Bloc A « Je découvre » · couleur teal · écoute et réponds · 75 min.
Source : exercices `prDeux` et `prImg`, les seize cartes de FC_CARDS, la
mini-leçon `prDeux`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre="Deux mondes, deux vocabulaires",
        chapeau="Louer et acheter sont deux systèmes complets : deux "
                "papiers, deux tribunaux, deux façons d'être protégé. "
                "Employer un mot de l'un dans l'autre se remarque tout de "
                "suite.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. Elle ferme « Je découvre » et ouvre les "
                  "trois défis : le bloc B est du côté location, les blocs C et D du "
                  "côté achat. Le dire au groupe, c'est donner la carte du module.")

    d.objectifs([
        "classer un mot du côté de la location ou du côté de l'achat ;",
        "nommer les personnes de chaque monde et ce qu'elles font ;",
        "dire qui protège le locataire et qui protège l'acheteur ;",
        "décrire une image en une phrase complète.",
    ], notes="Le troisième objectif est le renversement du module : en location, la "
             "loi protège d'office ; en achat, on se protège par ce qu'on écrit.")

    d.declencheur(
        'Mise en situation', "Sa sœur lui répète qu'elle paie pour rien",
        pistes=[
            "Sept ans de loyer : est-ce de l'argent perdu ?",
            "Qu'est-ce qu'on obtient en louant, qu'on n'obtient pas en achetant ?",
            "Connaissez-vous quelqu'un qui a acheté ici ? Comment ça s'est passé ?",
            "Qu'est-ce qui vous fait peur, dans l'idée d'acheter ?",
        ],
        notes="Ne pas trancher. La question revient en D2 et en E1, avec des chiffres. "
              "Ici, on ne fait que recueillir ce que le groupe croit savoir.")

    d.tableau('Analyse', "La même chose n'a pas le même nom",
              ['En location', 'En achat'],
              [["un bail", "une promesse d'achat, puis un acte de vente"],
               ["un locateur", "un courtier, un inspecteur, un notaire"],
               ["un loyer", "une hypothèque, des taxes, des frais de copropriété"],
               ["un avis de modification", "des conditions écrites dans la promesse"],
               ["le Tribunal administratif du logement", "ce que tu as écrit toi-même"]],
              cle=0,
              notes="Diapositive à photographier. La dernière rangée est la plus "
                    "importante et la moins évidente : y revenir en D1.")

    d.pratique('Vocabulaire', "Location ou achat ?",
               "Dites à quel monde appartient chaque mot.", [
        ("le bail", "location"),
        ("la mise de fonds", "achat"),
        ("l'avis de modification des conditions", "location"),
        ("les droits de mutation", "achat"),
        ("la reconduction au premier juillet", "location"),
        ("le fonds de prévoyance de l'immeuble", "achat"),
    ], corrige=True,
       notes="Six des huit items de prDeux. Pour chaque réponse, demander « comment le "
             "sais-tu ? » : c'est la justification qui installe le mot, pas le classement.")

    d.vocabulaire('Vocabulaire', "Quatre mots de la négociation", [
        ("une contre-proposition", "Une offre différente qu'on présente à la place de celle qu'on vient de recevoir."),
        ("une contrepartie", "Ce qu'une personne donne en échange de ce qu'elle obtient dans une entente."),
        ("une entente écrite", "Un accord noté sur papier, avec la date, pour que personne n'ait à se fier à sa mémoire."),
        ("un compromis", "Une solution où chacune des deux personnes accepte de reculer un peu."),
    ], notes="Ces quatre mots sont ceux du bloc B tout entier. Les faire écrire dans "
             "le carnet avec un exemple personnel : une entente déjà conclue, même hors "
             "du logement.")

    d.pratique('Écoute et réponds', "Décrivez l'image en une phrase",
               "Une phrase complète, avec un verbe conjugué et un lieu.", [
        ("Une enveloppe blanche coincée entre une porte de logement et son cadre.", "l'avis remis en main propre"),
        ("Une table de cuisine où deux tasses refroidissent à côté d'un papier plié.", "la discussion du défi 1"),
        ("Une pancarte plantée devant un immeuble de brique, un samedi matin.", "la propriété affichée"),
        ("Un salon vide et clair, avec une porte-fenêtre qui donne sur un balcon.", "la visite du défi 2"),
        ("Un bureau d'institution financière, deux chaises et un écran tourné vers le client.", "le rendez-vous du défi 3"),
    ], corrige=True,
       notes="Les cinq images de l'exercice prImg, projetées à l'écran du module. "
             "Faire produire la phrase à l'oral avant de montrer la colonne de droite.")

    d.billet(
        "Lequel des trois défis t'intéresse le plus, et pourquoi ?",
        exemples=[
            "L'avis du propriétaire, la visite avec la courtière, ou la promesse d'achat ?",
            "Une phrase suffit.",
        ],
        notes="Deux minutes. Les réponses disent quel bloc le groupe attend, et lequel "
              "l'intimide : c'est celui-là qu'il faudra travailler le plus lentement.")

    return d.save(dossier)
