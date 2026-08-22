# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 60 min. Dernière séance du module.
Source : dialogue `appli`, jeu de rôle `colis`, productions orale et écrite.

Séance de production. Tout ce que le module a montré revient ici, et rien de
neuf n'y est introduit — sauf un renversement : dans le dernier dialogue,
c'est Amara qui explique la poste à Karim. L'élève qui demandait devient
celui qui renseigne, et c'est la mesure du chemin parcouru.
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
        code='E1', section='teal',
        titre="Je me lance",
        chapeau="Faire sa démarche au comptoir de vive voix, puis écrire une "
                "adresse complète sur une enveloppe.",
        duree='60 minutes')

    d.titre(notes="Dernière séance. Rendre les enveloppes de la séance B2 au début : les "
                  "élèves voient ce qu'ils écrivaient il y a deux semaines. La moitié du "
                  "temps se passe en production réelle ; les diapositives ne sont qu'un "
                  "cadre.")

    d.objectifs([
        "faire une démarche complète au comptoir postal ;",
        "demander un prix et le redire pour vérifier ;",
        "s'enregistrer et s'écouter ;",
        "écrire une adresse complète sur une enveloppe.",
    ])

    d.declencheur(
        'Observation', "Sauriez-vous expliquer la poste à quelqu'un ?",
        image=_photo('poste-comptoir.jpg'),
        pistes=[
            "Où achète-t-on un timbre, près d'ici ?",
            "Qu'est-ce qu'on écrit sur une enveloppe, et dans quel ordre ?",
            "Que faire quand on trouve un carton dans sa boîte aux lettres ?",
            "Quelle phrase employez-vous si le prix va trop vite ?",
        ],
        notes="Quatre questions, quatre séances. Laisser répondre sans reprendre : le but "
              "est que le groupe entende qu'il sait déjà tout cela.")

    d.dialogue('Dialogue', "Cette fois, c'est Amara qui explique", [
        ("KARIM", "Amara, ma cousine arrive demain.", True),
        ("AMARA", "Elle veut envoyer une lettre ?", True),
        ("KARIM", "Oui. Elle ne sait pas comment.", True),
        ("AMARA", "C'est facile. Elle achète un timbre.", True),
        ("KARIM", "Où ?", True),
        ("AMARA", "Au comptoir postal, dans la pharmacie.", True),
        ("KARIM", "Et l'adresse ?", True),
        ("AMARA", "Le nom au milieu. La rue en dessous.", True),
    ], consigne="Écoutez, puis dites qui explique et qui demande.",
       notes="Faire remarquer le renversement : à la séance A1, c'est Amara qui ne savait "
             "rien. Le dire au groupe en toutes lettres — c'est le moment de la séance qui "
             "reste.")

    d.tableau('Analyse', "Ce qui revient de tout le module",
              ['Ce qu\'on dit', 'Vu en'],
              [["Un timbre, s'il vous plaît. Combien ça coûte ?", "A1 et A3"],
               ["Le nom au milieu, la rue en dessous.", "B1 — les cinq lignes"],
               ["Sherbrooke (Québec) J1H 1P4", "B2 — le code postal"],
               ["Écrivez votre nom. Signez ici. Gardez votre reçu.", "C1 et C2"]],
              cle=2,
              note="Rien de neuf dans cette colonne : le module entier tient dans ces "
                   "quatre lignes.",
              notes="Diapositive à photographier. Elle sert de révision de tout le module "
                    "en une seule page ; la laisser affichée pendant la production orale.")

    d.regle("Redire, et faire répéter",
            "Un dollar quarante-quatre ? … Pouvez-vous répéter, s'il vous plaît ?",
            precision="Ce sont les deux phrases qui servent le plus longtemps, bien "
                      "au-delà du comptoir postal. Elles ne sont ni une faiblesse ni une "
                      "faute : elles montrent qu'on écoute pour de bon.",
            notes="Diapositive à photographier. Le rappeler une dernière fois : personne "
                  "ne s'impatiente devant quelqu'un qui vérifie. C'est le contraire qui "
                  "fait perdre du temps à tout le monde.")

    d.cartes("Trois situations pour le jeu de rôle", "Choisissez la vôtre", [
        ("J'achète un timbre",
         "Vous avez une lettre à envoyer à Sherbrooke. Vous ne savez pas combien coûte "
         "un timbre."),
        ("J'envoie un colis",
         "Vous avez une boîte de deux kilos à envoyer. Vous voulez le prix, et savoir "
         "quoi écrire sur le formulaire."),
        ("Je viens chercher mon colis",
         "Vous avez trouvé un avis de livraison dans votre boîte aux lettres. Vous venez "
         "chercher votre colis."),
    ], cols=3, notes="Ce sont les trois situations du jeu de rôle en ligne. L'assistant y "
                     "joue Luc Tremblay, le préposé : il répond en deux ou trois mots, "
                     "lentement, une information à la fois.")

    d.pratique('Production orale', "Faites votre démarche au comptoir",
               "Trois temps. Enregistrez-vous, écoutez-vous, recommencez.", [
        ("TEMPS 1", "Bonjour. Je veux envoyer ce colis à Sherbrooke."),
        ("TEMPS 2", "Combien ça coûte ? … Pouvez-vous répéter, s'il vous plaît ?"),
        ("TEMPS 3", "Treize dollars quinze ? Merci beaucoup. Bonne journée."),
    ], cols=1,
       notes="Vingt minutes. Laisser recommencer autant de fois qu'il le faut : c'est "
             "l'écoute de soi qui fait progresser, pas la première prise. Les sept sujets "
             "à couvrir sont listés dans le module en ligne.")

    d.pratique('Production écrite', "Écrivez une adresse complète",
               "Sur l'enveloppe distribuée, les quatre lignes et le coin de "
               "l'expéditeur.", [
        ("À écrire", "Au milieu : le nom d'une personne que vous connaissez."),
        ("À écrire", "En dessous : le numéro, la rue et l'appartement."),
        ("À écrire", "La ville, la province entre parenthèses, le code postal."),
        ("À écrire", "En haut à gauche, en petit : votre nom et votre adresse."),
    ], cols=1,
       notes="Vingt minutes. Rappeler les deux choses qui seront regardées : la province "
             "entre parenthèses, et les six caractères du code postal. Les enveloppes "
             "réussies partent vraiment, si l'élève le veut.")

    d.billet(
        "Allez au comptoir postal cette semaine, et dites une phrase en français.",
        exemples=[
            "Un timbre, s'il vous plaît.",
            "Combien ça coûte ?",
            "Merci beaucoup. Bonne journée.",
        ],
        notes="Dernier devoir du module. Demander de raconter à la séance suivante ce qui "
              "s'est passé — ce qui a marché, et ce qui a été trop vite. C'est le retour "
              "qui compte, pas la réussite.")

    return d.save(dossier)
