# -*- coding: utf-8 -*-
"""C1 · Les cinq parties du chèque.
Bloc C « Défi 2 · Je fais un chèque » · couleur acier · 75 min.
Source : dialogue `t2`, exercices `t2vf`, `t2parties`, `t2ordre`,
mini-leçon `t2ordre`.

Première séance du Défi 2. Le chèque est un papier que beaucoup d'élèves ont
dans un tiroir sans jamais l'avoir rempli, et un chèque incomplet est refusé
au comptoir. La séance nomme les cinq parties, dans l'ordre où la main les
écrit.
"""
import os

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-guichet/images/')


def _photo(nom):
    """La photo si elle est sur le disque, sinon rien. Voir `a1.py`."""
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Les cinq parties du chèque",
        chapeau="Nommer chaque ligne d'un chèque, écrire la date et le nom "
                "de qui reçoit l'argent, et savoir où va la signature.",
        duree='75 minutes')

    d.titre(notes="Photocopier deux chèques vierges par élève — un modèle inventé, jamais "
                  "un vrai chèque de quelqu'un. Un pour l'essai, un pour la bonne copie. "
                  "Annoncer le contrat : à la fin de la séance, chacun a rempli un chèque "
                  "en entier.")

    d.objectifs([
        "nommer les cinq parties d'un chèque ;",
        "écrire la date au long ;",
        "écrire le nom de qui reçoit l'argent ;",
        "savoir où et quand signer.",
    ])

    d.declencheur(
        'Observation', "Comment payer quand le comptant est refusé ?",
        image=_photo('etape-comptoir.jpg'),
        pistes=[
            "Avez-vous déjà entendu « nous ne prenons pas le comptant » ?",
            "Où est-ce que ça arrive : à l'école, au sport, chez le propriétaire ?",
            "Avez-vous des chèques à la maison ?",
            "Qui a déjà rempli un chèque en français ?",
        ],
        notes="Beaucoup de centres et de propriétaires refusent le comptant : ce n'est pas "
              "une méfiance, c'est une trace écrite. Le dire simplement.")

    d.dialogue('Dialogue · 1 de 3', "Nous ne prenons pas le comptant", [
        ("MONIQUE", "Bonjour ! Le cours de natation, c'est quarante-cinq dollars.", True),
        ("AMADOU", "Bonjour. J'ai l'argent comptant.", True),
        ("MONIQUE", "Nous ne prenons pas le comptant. Un chèque ou la carte.", True),
        ("AMADOU", "J'ai des chèques. Mais je ne sais pas écrire un chèque.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire écouter deux fois, diapositive masquée. Insister sur la dernière "
             "réplique : dire « je ne sais pas » est exactement ce qu'il faut faire, et "
             "madame Lachance aide aussitôt.")

    d.dialogue('Dialogue · 2 de 3', "La date d'abord, en haut", [
        ("MONIQUE", "C'est facile. La date d'abord, en haut.", True),
        ("AMADOU", "Le 14 mars 2026.", True),
        ("MONIQUE", "Après, le nom : Centre sportif Sainte-Cécile.", True),
        ("AMADOU", "Et le montant ?", True),
    ], notes="Faire suivre du doigt sur le chèque photocopié pendant l'écoute : en haut à "
             "droite pour la date, la longue ligne du milieu pour le nom.")

    d.dialogue('Dialogue · 3 de 3', "Deux fois le montant, puis la signature", [
        ("MONIQUE", "Deux fois : 45,00 en chiffres, et en lettres en dessous.", True),
        ("AMADOU", "Et je signe en bas ?", True),
        ("MONIQUE", "Oui. Vous signez en bas, à droite.", True),
    ], notes="Le montant écrit deux fois étonne toujours. Ne pas expliquer encore "
             "pourquoi : c'est la séance C2 qui le fera, avec le trait au bout de la "
             "ligne.")

    d.tableau('Analyse', "Chaque ligne, et ce qu'on y met",
              ["La ligne", "Ce qu'on y écrit"],
              [["En haut, à droite", "la date : le 14 mars 2026"],
               ["« Payez à l'ordre de »", "le nom de la personne ou du commerce"],
               ["La petite case, à droite", "le montant en chiffres : 45,00"],
               ["La longue ligne", "le montant en lettres : quarante-cinq dollars"],
               ["En bas, à droite", "votre signature, écrite de votre main"],
               ["Le mémo, en bas à gauche", "pourquoi vous payez : cours de natation"]],
              cle=1,
              notes="Diapositive à photographier. C'est la page la plus utile du Défi 2 : "
                    "la faire recopier à la main, sous forme de dessin de chèque. Six "
                    "lignes, et le chèque est complet ; il en manque une, et le comptoir "
                    "le refuse.")

    d.regle("La date au long, et le nom au complet",
            "Le 14 mars 2026 — Centre sportif Sainte-Cécile.",
            precision="Le jour, puis le mois écrit en lettres, puis l'année. Seul le "
                      "premier jour du mois prend « er » : le 1er mars, mais le 2, le 3, "
                      "le 14 ne prennent rien. Et le nom s'écrit au complet : pas "
                      "« le centre », pas « eux ».",
            notes="Diapositive à photographier. Faire écrire la date d'aujourd'hui au "
                  "tableau par trois élèves différents. Corriger seulement le mois en "
                  "lettres et l'ordre.")

    d.regle("Ne signez jamais un chèque d'avance",
            "Un chèque signé, sans nom et sans montant, se remplit par n'importe qui.",
            precision="La signature est la dernière chose qu'on écrit, jamais la "
                      "première. Un carnet de chèques se range comme de l'argent : c'en "
                      "est.",
            notes="Diapositive à photographier. Le dire deux fois plutôt qu'une : avec le "
                  "NIP de la séance A1, c'est la seconde consigne du module qui protège "
                  "de l'argent perdu.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le cours de natation coûte quarante-cinq dollars.", "vrai"),
        ("Le centre accepte l'argent comptant.", "faux — chèque ou carte"),
        ("Amadou a des chèques.", "vrai"),
        ("On écrit le montant une seule fois.", "faux — deux fois"),
        ("La signature se met en bas, à droite.", "vrai"),
    ], corrige=True, cols=1,
       notes="Les cinq mêmes énoncés sont dans le module en ligne, exercice `t2vf`.")

    d.pratique('Écriture', "Le chèque d'Amadou, ligne par ligne",
               "Complétez le chèque du centre sportif.", [
        ("Date : le 14 ___ 2026", "mars"),
        ("Payez à l'___ de : Centre sportif Sainte-Cécile", "ordre"),
        ("Montant en chiffres : ___ ,00", "45"),
        ("Montant en lettres : quarante-cinq ___", "dollars"),
        ("Mémo : cours de ___", "natation"),
        ("En bas à droite, je mets ma ___.", "signature"),
    ], corrige=True, cols=2,
       notes="Les six mêmes phrases sont dans le module en ligne, exercice `t2ordre`, "
             "avec sa mini-leçon.")

    d.pratique('Pratique · seul', "Votre premier chèque",
               "Sur le chèque photocopié, quatre choses seulement.", [
        ("Étape 1", "En haut à droite : la date d'aujourd'hui, au long."),
        ("Étape 2", "Payez à l'ordre de : le nom complet de votre centre de francisation."),
        ("Étape 3", "Dans la petite case : 45,00"),
        ("Étape 4", "Le mémo : cours de français."),
    ], cols=1,
       notes="Vingt minutes. Ne pas faire écrire le montant en lettres aujourd'hui : "
             "c'est la séance C2. Ramasser les chèques et les redonner en C2 — ils "
             "serviront à finir le travail.")

    d.billet(
        "Écrivez la date d'aujourd'hui et celle de votre anniversaire, au long.",
        exemples=[
            "Le 22 août 2026",
            "Le 1er mars 1991",
            "Le 14 novembre 2003",
        ],
        notes="Devoir court. Vérifier deux choses : le mois en lettres, et le « er » du "
              "premier du mois — nulle part ailleurs.")

    return d.save(dossier)
