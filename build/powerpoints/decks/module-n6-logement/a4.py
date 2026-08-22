# -*- coding: utf-8 -*-
"""A4 · Le verbe caché sous le nom
Bloc A « Je découvre » · couleur ambre · 75 min. Grammaire et vocabulaire.
Source : exercices `prMots` et `prImg`, mini-leçon `prMots`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Le verbe caché sous le nom",
        chapeau="« La reconduction du bail s'effectue de plein droit » veut "
                "dire « le bail continue tout seul ». Même chose, deux "
                "habits.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. Elle prépare directement le Défi 1 : "
                  "la page qu'on lira lundi est écrite en noms, et sans ce travail "
                  "elle paraîtra trois fois plus difficile qu'elle n'est.")

    d.objectifs([
        "retrouver le verbe sous un nom en -tion et en -ment ;",
        "connaître les deux noms irréguliers du dossier : cession, "
        "indemnité ;",
        "employer le bon article selon le suffixe ;",
        "traduire une phrase administrative en phrase parlée.",
    ], notes="Le quatrième objectif est le vrai. Les trois premiers ne sont que des "
             "moyens : ce qu'on veut, c'est qu'une phrase de texte officiel cesse "
             "d'être un mur.")

    d.declencheur(
        'Observation', "Pourquoi les textes officiels sont-ils écrits comme ça ?",
        pistes=[
            "« Le paiement du loyer » ou « vous payez votre loyer » : lequel est plus clair ?",
            "Pourquoi un texte de loi préfère-t-il le premier ?",
            "Avez-vous déjà renoncé à lire un papier à cause de sa langue ?",
        ],
        notes="Répondre honnêtement à la question : un nom se numérote, se cite et se "
              "met en titre ; un verbe demande un sujet, donc quelqu'un de précis. Un "
              "texte qui vaut pour tout le monde ne peut pas nommer quelqu'un.")

    d.tableau('Analyse', "Le suffixe fabrique le nom",
              ['Le suffixe', 'Les mots du dossier'],
              [["-tion (féminin)", "la location, la sous-location, la résiliation"],
               ["-ment (masculin)", "le renouvellement, le consentement, le paiement"],
               ["irréguliers", "céder donne la cession · indemniser donne une indemnité"]],
              cle=0,
              note="Le genre suit le suffixe, presque sans exception.",
              notes="Diapositive à photographier. La règle du genre vaut la peine "
                    "d'être dite : elle règle à elle seule la moitié des fautes "
                    "d'accord dans les productions du bloc E.")

    d.cartes('Détail', "Deux préfixes, et ce qu'ils changent", [
        ("sous-", "Il veut dire « en dessous », donc « qui dépend de ». Un sous-locataire dépend du locataire, jamais directement du locateur."),
        ("re-", "Il refait : louer donne relouer, conduire donne reconduire. La reconduction du bail, c'est le bail qu'on reconduit — qu'on refait rouler."),
        ("Le mot qui trompe", "« Cession » se prononce comme « session » et n'a aucun rapport. Dans un écrit, seul le contexte les distingue."),
        ("Le mot qui manque", "« Un sous-louage » n'existe pas, « une cédation » non plus. Devant un doute, écrivez le verbe : personne ne vous reprochera une phrase simple."),
    ], notes="La dernière carte est un conseil de survie, pas une facilité. Un élève "
             "qui écrit « je veux sous-louer » est parfaitement clair ; un élève qui "
             "invente un nom savant ne l'est plus.")

    d.pratique('Pratique', "Le nom de la même famille",
               "Complétez avec le nom qui correspond au verbe.", [
        ("Elle veut sous-louer : elle prépare une…", "sous-location"),
        ("Il faut céder le bail : on parle d'une…", "cession de bail"),
        ("Le bail se renouvelle tout seul : c'est le…", "renouvellement"),
        ("Le locateur consent : elle obtient son…", "consentement"),
        ("On met fin au bail : la loi encadre la…", "résiliation"),
        ("Elle paie le premier du mois : le… du loyer", "paiement"),
    ], corrige=True,
       notes="Faire dire l'article à chaque fois. Un nom sans article n'est pas su : "
             "c'est au moment de l'employer dans une phrase que la faute se voit.")

    d.regle("Retrouver le verbe, c'est comprendre la phrase",
            "Sous chaque nom d'un texte officiel, il y a un verbe.",
            precision="« La reconduction du bail » veut dire que le bail continue. "
                      "« Le consentement du locateur » veut dire que le locateur "
                      "accepte. « Le remboursement des dépenses » veut dire qu'on "
                      "rembourse les dépenses. "
                      "Faites l'opération à voix basse pendant que vous lisez : la "
                      "phrase se dégonfle d'elle-même.",
            notes="Diapositive à photographier. Faire l'exercice en direct sur une "
                  "phrase que l'enseignante écrit au tableau, tirée de la page qui "
                  "sera lue en B2.")

    d.tableau('Traduction', "Ce qu'on dit, ce qu'on lit",
              ['On dirait', 'Le document écrit'],
              [["le bail continue tout seul", "la reconduction du bail"],
               ["il accepte", "son consentement"],
               ["elle prête son logement", "la sous-location"],
               ["on met fin au bail", "la résiliation du bail"]],
              cle=0,
              notes="Lire la colonne de droite à voix haute, puis demander la gauche. "
                    "L'exercice est plus difficile dans ce sens-là, et c'est celui "
                    "dont l'élève aura besoin lundi.")

    d.billet(
        "Traduisez en langage parlé : « Le paiement du loyer demeure à la charge du locataire. »",
        exemples=[
            "Une phrase avec un verbe et un sujet.",
            "Qui paie, et quoi ?",
        ],
        notes="Deux minutes. La bonne réponse est « le locataire continue de payer le "
              "loyer ». Ceux qui n'y arrivent pas encore auront besoin d'aide en B2 : "
              "les repérer maintenant.")

    return d.save(dossier)
