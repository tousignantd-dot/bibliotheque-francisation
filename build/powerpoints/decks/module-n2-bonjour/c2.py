# -*- coding: utf-8 -*-
"""C2 · Merci et bonne fête.
Bloc C « Défi 2 · Merci et bonne fête » · couleur ambre · 60 min.
Source : dialogue `t2b`, exercices `t2merci` et `t2carte`, mini-leçon `t2merci`.

La séance qui porte les deux intentions écrites du programme : comprendre
des souhaits ou des remerciements, choisir une carte de vœux, et en rédiger
de simples. Tout tient sur deux petits mots — « pour » après merci, et le
choix entre « bon » et « bonne ».
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-bonjour/images/')


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Merci et bonne fête",
        chapeau="On remercie pour ce qui est arrivé, on souhaite ce qui "
                "vient. Et une carte tient en trois lignes.",
        duree='60 minutes')

    d.titre(notes="Apporter de vraies cartes de vœux, plusieurs, achetées à la pharmacie. "
                  "Les faire circuler pendant toute la séance : c'est l'objet même de "
                  "l'intention du programme.")

    d.objectifs([
        "remercier avec « merci pour » ;",
        "choisir entre « bon » et « bonne » ;",
        "reconnaître à quelle occasion va une carte ;",
        "écrire trois lignes sur une carte.",
    ])

    d.declencheur(
        'Observation', "À qui donne-t-on ceci ?",
        image=IMG + 'carte-table.jpg',
        pistes=[
            "Qu'est-ce que c'est ?",
            "Quand est-ce qu'on en donne une ?",
            "Qu'est-ce qu'on écrit dedans ?",
            "En avez-vous déjà reçu une ici ?",
        ],
        notes="Faire circuler les vraies cartes apportées pendant que le groupe répond. "
              "Beaucoup n'en ont jamais tenu une et ne savent pas qu'on en donne pour un "
              "départ, une naissance, un examen réussi.")

    d.dialogue('Dialogue · 1 de 2', "Merci pour la soupe", [
        ("GILBERTE", "Nadia, j'ai de la soupe pour toi.", True),
        ("NADIA", "Oh ! Merci beaucoup, madame Roy. Merci pour la soupe.", True),
        ("GILBERTE", "Ça me fait plaisir.", True),
        ("NADIA", "Vous êtes gentille. Samedi, c'est votre fête ?", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Deux remerciements dans la même réplique : « merci beaucoup » tout court, "
             "puis « merci pour la soupe ». Faire entendre la différence.")

    d.dialogue('Dialogue · 2 de 2', "Soixante-dix ans samedi", [
        ("GILBERTE", "Oui. Samedi, j'ai soixante-dix ans.", True),
        ("NADIA", "Bonne fête à l'avance !", True),
        ("GILBERTE", "Merci, Nadia.", True),
    ], notes="« À l'avance » se comprend sans être expliqué. Le donner comme bloc, sans "
             "l'analyser : c'est un énoncé à mémoriser, pas une structure.")

    d.tableau('Analyse', "Bon ou bonne ?",
              ['On dit « bonne »', 'On dit « bon »'],
              [["bonne journée", "bon anniversaire"],
               ["bonne soirée", "bon voyage"],
               ["bonne fête", "bon cours"],
               ["bonne santé", "bon appétit"]],
              cle=2,
              note="Si on peut dire « une », c'est « bonne ». C'est le seul truc.",
              notes="Diapositive à photographier. Faire ajouter deux souhaits par le "
                    "groupe et les classer dans la bonne colonne.")

    d.regle("Merci pour…",
            "Après « merci », on met <b>pour</b> devant la chose.",
            precision="Merci <b>pour</b> la soupe. Merci <b>pour</b> votre aide. Merci "
                      "<b>pour</b> la carte. Sans « pour », la phrase n'est pas "
                      "française — et c'est le petit mot qu'on oublie le plus souvent.",
            notes="Diapositive à photographier. Faire dire à chaque élève un « merci "
                  "pour… » vrai, adressé à quelqu'un de la classe.")

    d.cartes("Quatre cartes", "Pour quelle occasion ?", [
        ("Bonne fête !", "le jour de l'anniversaire"),
        ("Merci pour tout", "quand quelqu'un nous a beaucoup aidés"),
        ("Félicitations !", "quand une personne réussit un examen"),
        ("Bienvenue !", "à une personne qui arrive dans l'immeuble"),
    ], cols=2, notes="Diapositive à photographier. Poser les vraies cartes apportées sur "
                     "une table et faire associer chacune à l'une des quatre lignes.")

    d.pratique('Compréhension', "Le petit mot qui manque",
               "Complétez chaque phrase.", [
        ("___ pour la soupe, madame Roy.", "Merci"),
        ("C'est sa fête : « ___ fête ! »", "Bonne"),
        ("Il part en avion : « ___ voyage ! »", "Bon"),
        ("Vous partez le matin : « ___ journée ! »", "Bonne"),
        ("Elle vous dit merci : « Ce n'est ___ . »", "rien"),
    ], corrige=True, cols=1,
       notes="Faire d'abord à l'oral. Les lignes 2 et 3 sont le cœur : les corriger en "
             "reprenant l'astuce du « une ».")

    d.pratique('Pratique · seul, puis à deux', "Trois lignes sur une carte",
               "Écrivez une vraie carte, à donner vraiment.", [
        ("Étape 1", "Ligne 1 : un souhait, avec le nom de la personne."),
        ("Étape 2", "Ligne 2 : un merci, avec le mot « pour »."),
        ("Étape 3", "Ligne 3 : votre prénom."),
        ("Étape 4", "Lisez votre carte à votre voisin."),
    ], cols=1,
       notes="Vingt minutes. Fournir du carton plié : une carte écrite sur une feuille "
             "lignée ne produit pas le même soin. Beaucoup voudront la donner pour vrai — "
             "les encourager.")

    d.billet(
        "Recopiez votre carte au propre, et donnez-la à quelqu'un.",
        exemples=[
            "Bonne fête, madame Roy !",
            "Merci pour votre aide.",
            "Nadia, votre voisine du 3",
        ],
        notes="Devoir. C'est le brouillon de la production écrite de E1 : le rappeler.")

    return d.save(dossier)
