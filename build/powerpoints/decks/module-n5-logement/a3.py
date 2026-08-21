# -*- coding: utf-8 -*-
"""A3 · Les mots du logement.
Bloc A « Je découvre » · couleur framboise · 75 min.
Source : `FC_CARDS`, exercices `prVocab` et `prImg`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-logement/images/')


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Les mots du logement",
        chapeau="Seize mots à installer avant de téléphoner. Sans eux, un "
                "appel de quatre minutes devient une suite de « pardon ? ».",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Elle vient avant le défi 1 parce que les mots "
                  "d'ici — buanderie, bois franc, case de stationnement — ne se devinent "
                  "pas, même pour un élève qui parle bien.")

    d.objectifs([
        "nommer les parties et les services d'un logement ;",
        "distinguer ce qui est fourni de ce qui est inclus ;",
        "employer les mots du bail : loyer, avis, renouvellement ;",
        "reconnaître les mots propres au Québec.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce que vous voyez, et comment ça s'appelle ?",
        image=IMG + 'buanderie-sous-sol.jpg',
        pistes=[
            "Où est cette pièce, dans un immeuble ?",
            "Qui a le droit de s'en servir ?",
            "Est-ce que c'est gratuit ?",
            "Comment ça s'appelle dans votre langue ?",
        ],
        notes="Le mot « buanderie » est presque toujours inconnu, et c'est un des huit "
              "renseignements qu'on demande au téléphone. Le faire répéter à voix haute.")

    d.vocabulaire('Famille · 1 de 4', "Le logement lui-même", [
        ("un quatre et demie", "Quatre pièces plus la salle de bain : deux chambres, "
                               "un salon, une cuisine."),
        ("un plancher de bois franc", "Un plancher fait de vraies planches de bois dur."),
        ("une remise", "Un petit espace fermé pour ranger les vélos, les pneus."),
        ("ensoleillé", "Se dit d'une pièce où le soleil entre une bonne partie du jour."),
        ("insonorisé", "Se dit d'un logement construit pour qu'on n'entende pas les voisins."),
    ], notes="Le demi, c'est toujours la salle de bain. Faire compter les pièces du "
             "logement de chacun : plusieurs découvriront comment nommer le leur.")

    d.vocabulaire('Famille · 2 de 4', "Les services de l'immeuble", [
        ("une buanderie", "Le local commun où les locataires lavent leur linge."),
        ("une case de stationnement", "L'espace réservé où un locataire gare son auto."),
        ("les électroménagers", "Poêle, réfrigérateur, laveuse, sécheuse."),
        ("chauffé et éclairé", "Se dit d'un loyer qui comprend déjà le chauffage "
                               "et l'électricité."),
    ], notes="« Chauffé et éclairé » s'écrit C/E dans les annonces. C'est la mention qui "
             "change le prix réel de cent dollars par mois.")

    d.vocabulaire('Famille · 3 de 4', "L'argent et les dates", [
        ("le loyer", "La somme payée chaque mois pour habiter le logement."),
        ("la date d'occupation", "Le jour où le logement devient disponible."),
        ("un avis de modification", "Le papier annonçant ce que le propriétaire "
                                    "veut changer."),
    ], notes="Rappeler la grande date du Québec : le 1er juillet. Presque tous les baux "
             "vont du 1er juillet au 30 juin, et c'est pourquoi le choix est large en "
             "avril et presque nul en septembre.")

    d.vocabulaire('Famille · 4 de 4', "Le bail et les droits", [
        ("un bail", "Le contrat écrit entre le propriétaire et le locataire."),
        ("le renouvellement", "Le fait qu'un bail recommence sans qu'on le resigne."),
        ("sous-louer", "Laisser quelqu'un habiter son logement en gardant son bail."),
        ("le Tribunal administratif du logement",
         "L'organisme qui tranche entre un locataire et un propriétaire."),
    ], notes="Le Tribunal s'appelait la Régie du logement jusqu'en 2020. Beaucoup de gens "
             "disent encore « la Régie » : le préciser, les élèves l'entendront.")

    d.tableau('Les mots d\'ici', "Ce qui ne se dit pas ailleurs",
              ['Au Québec', 'Ailleurs en français'],
              [["un quatre et demie", "un trois-pièces"],
               ["une buanderie", "une laverie, une blanchisserie"],
               ["un poêle", "une cuisinière"],
               ["une case de stationnement", "une place de parking"],
               ["chauffé et éclairé", "charges comprises"]],
              cle=0,
              note="Les annonces d'ici n'emploient que la colonne de gauche.",
              notes="Diapositive à photographier. Utile aux élèves venus de France, "
                    "d'Afrique francophone ou du Maghreb, qui connaissent la colonne de "
                    "droite et cherchent en vain les mots dans les annonces.")

    d.pratique('Vocabulaire', "Le mot juste",
               "Complétez avec un mot de la séance.", [
        ("Le local du sous-sol où on lave son linge : une …", "buanderie"),
        ("La somme payée chaque mois : le …", "loyer"),
        ("Le contrat signé pour un an : le …", "bail"),
        ("Une pièce où le soleil entre longtemps : elle est …", "ensoleillée"),
        ("On n'entend pas les voisins : l'immeuble est …", "insonorisé"),
        ("Le jour où le bail commence : la … d'occupation", "date"),
        ("Laisser quelqu'un habiter chez soi en gardant son bail : …", "sous-louer"),
        ("Le poêle et le réfrigérateur sont des …", "électroménagers"),
    ], corrige=True,
       notes="Faire employer chaque mot dans une phrase complète après la correction : le "
             "mot seul ne se retient pas.")

    d.piege("Confondre « meublé » et « équipé »",
            "Meublé, donc le poêle est là.",
            "Meublé parle des meubles ; les électroménagers se demandent à part.",
            "« Meublé » veut dire qu'il y a un lit, une table, une commode. Le poêle et le "
            "réfrigérateur ne sont pas des meubles : ils se demandent séparément, et c'est "
            "une des huit questions du téléphone.",
            notes="Erreur coûteuse : arriver dans un logement sans réfrigérateur le 1er "
                  "juillet, c'est une dépense de plusieurs centaines de dollars imprévue.")

    d.billet(
        "Décrivez votre logement actuel en quatre phrases.",
        exemples=[
            "Combien de pièces ? Est-il chauffé et éclairé ?",
            "Y a-t-il une buanderie, une remise, un stationnement ?",
        ],
        notes="Devoir d'écriture courte. Il réemploie le vocabulaire et fournit des cas "
              "réels pour la séance A4 et pour le défi 2.")

    return d.save(dossier)
