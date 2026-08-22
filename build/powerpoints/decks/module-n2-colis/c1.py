# -*- coding: utf-8 -*-
"""C1 · Le formulaire du colis.
Bloc C « Défi 2 · Je remplis le formulaire » · couleur acier · 75 min.
Source : dialogue `t2`, exercices `t2vf`, `t2form`, mini-leçon `t2form`.

« Lire et remplir un formulaire » est la seconde intention du programme pour
cette situation, et la seule qui y soit inscrite deux fois — en
compréhension écrite et en production écrite. Le formulaire du colis est
donc le défi central de la seconde moitié du module.

Les mots de ce formulaire — nom, prénom, adresse, signature — se retrouvent
sur tous les autres : la banque, la clinique, l'école. C'est la séance qui
sert le plus loin du bureau de poste.
"""
import os

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-colis/images/')


def _photo(nom):
    """La photo si elle est sur le disque, sinon rien. Voir `a1.py`."""
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Le formulaire du colis",
        chapeau="Lire un formulaire case par case, y écrire son nom, son "
                "prénom et son adresse, et signer au bon endroit.",
        duree='75 minutes')

    d.titre(notes="Photocopier un formulaire vierge, deux par élève : un pour l'essai, un "
                  "pour la bonne copie. Le modèle du module est inventé et volontairement "
                  "simple — six cases, une signature.")

    d.objectifs([
        "reconnaître les mots nom, prénom, adresse, signature ;",
        "remplir les six cases d'un formulaire ;",
        "distinguer la case de l'expéditeur de celle du destinataire ;",
        "savoir ce qu'on fait du reçu.",
    ])

    d.declencheur(
        'Observation', "Que fait le préposé avec cette boîte ?",
        image=_photo('poste-balance.jpg'),
        pistes=[
            "Pourquoi la boîte va-t-elle sur la balance ?",
            "Qu'est-ce qu'on écrit sur un formulaire de colis ?",
            "Avez-vous déjà rempli un formulaire en français ?",
            "Quel mot vous a arrêté ?",
        ],
        notes="La quatrième question fait sortir les vraies difficultés : « nom » et "
              "« prénom » inversés, « signature » écrite en lettres détachées. Les noter "
              "au tableau, elles reviennent dans la pratique.")

    d.dialogue('Dialogue · 1 de 2', "Posez la boîte ici", [
        ("LUC", "Bonjour. Posez la boîte ici.", True),
        ("AMARA", "Voilà. C'est pour Sherbrooke.", True),
        ("LUC", "Deux kilos. Remplissez ce formulaire.", True),
        ("AMARA", "Qu'est-ce que j'écris ici ?", True),
        ("LUC", "Votre nom, votre prénom, votre adresse.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire répéter la question d'Amara par tout le groupe : « Qu'est-ce que "
             "j'écris ici ? ». C'est la phrase à emporter, et elle vaut devant n'importe "
             "quel guichet.")

    d.dialogue('Dialogue · 2 de 2', "Signez en bas, à droite", [
        ("AMARA", "Et cette case ?", True),
        ("LUC", "Le nom de la personne. Et son adresse.", True),
        ("AMARA", "D'accord. Et après ?", True),
        ("LUC", "Signez en bas. Ici, à droite.", True),
        ("AMARA", "Voilà. C'est fini ?", True),
        ("LUC", "Oui. Voici votre reçu. Gardez-le.", True),
    ], notes="Faire remarquer que le préposé ne remplit rien : il montre. Amara écrit "
             "elle-même, comme au comptoir réel.")

    d.tableau('Analyse', "Les mots de tous les formulaires",
              ['Le mot de la case', 'Ce qu\'on y écrit'],
              [["Nom", "le nom de famille : Diallo"],
               ["Prénom", "le petit nom, celui qu'on dit d'abord : Amara"],
               ["Adresse", "le numéro, la rue et l'appartement"],
               ["Signature", "son nom écrit à la main, jamais en lettres détachées"]],
              cle=2,
              note="En haut, l'expéditeur : c'est vous. En bas, le destinataire : c'est la "
                   "personne qui reçoit.",
              notes="Diapositive à photographier. Ces quatre mots sont sur le formulaire "
                    "de la banque, de la clinique et de l'école. Le dire au groupe : la "
                    "séance sert bien au-delà de la poste.")

    d.regle("Signer, ce n'est pas écrire son nom",
            "La signature se fait à la main, et toujours de la même façon.",
            precision="On peut écrire son nom en lettres détachées dans la case « Nom ». "
                      "Dans la case « Signature », on signe : c'est le tracé qu'on refait "
                      "pareil chaque fois, à la banque comme à la poste. Personne ne "
                      "signe à votre place.",
            notes="Diapositive à photographier. Faire signer trois fois de suite sur un "
                  "brouillon, et comparer : c'est la ressemblance entre les trois qui "
                  "compte, pas la beauté.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le colis pèse deux kilos.", "vrai"),
        ("Le préposé remplit le formulaire pour Amara.", "faux — elle écrit elle-même"),
        ("Amara écrit son nom et son adresse.", "vrai"),
        ("Elle signe en bas, à droite.", "vrai"),
        ("Le préposé jette le reçu.", "faux — il le donne, et il faut le garder"),
    ], corrige=True, cols=1,
       notes="Les cinq mêmes énoncés sont dans le module en ligne, exercice `t2vf`.")

    d.pratique('Écriture', "Je remplis mes cases",
               "Avec les renseignements d'Amara Diallo, 4520, rue Bélanger, "
               "app. 3, Montréal (Québec) H1T 1C5.", [
        ("Nom : ___", "Diallo"),
        ("Prénom : ___", "Amara"),
        ("Numéro et rue : 4520, ___ Bélanger", "rue"),
        ("Appartement : ___", "3"),
        ("Ville : ___", "Montréal"),
        ("Code postal : ___", "H1T 1C5"),
    ], corrige=True, cols=2,
       notes="Les six mêmes cases sont dans le module en ligne, exercice `t2form`, avec sa "
             "mini-leçon. Faire d'abord celle d'Amara au tableau, puis passer à la sienne "
             "dans la pratique à deux.")

    d.pratique('Pratique · à deux', "Mon colis, mon formulaire",
               "Deux par deux, avec le formulaire photocopié.", [
        ("Étape 1", "Remplissez la partie du haut avec vos propres renseignements."),
        ("Étape 2", "Remplissez la partie du bas avec ceux de votre voisin."),
        ("Étape 3", "Signez en bas, à droite."),
        ("Étape 4", "Échangez et vérifiez : est-ce qu'il manque une case ?"),
    ], cols=1,
       notes="Vingt minutes. À l'étape 4, faire chercher le code postal en premier : c'est "
             "la case le plus souvent oubliée, et la seule qui fasse revenir le colis.")

    d.billet(
        "Écrivez les quatre mots d'un formulaire et ce qu'on met dedans.",
        exemples=[
            "Nom : mon nom de famille.",
            "Prénom : mon petit nom.",
            "Signature : je signe à la main.",
        ],
        notes="Devoir court. Demander de repérer ces mêmes mots sur un vrai papier reçu à "
              "la maison, et de l'apporter s'ils le veulent.")

    return d.save(dossier)
