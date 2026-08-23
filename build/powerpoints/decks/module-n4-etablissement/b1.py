# -*- coding: utf-8 -*-
"""B1 · Le menu, puis le message
Bloc B « Défi 1 · Le répondeur du centre » · couleur acier · 75 min.
Source du module : dialogue `t1`, exercice `t1a`.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n4-etablissement/images/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Le menu, puis le message",
        chapeau="Sept heures dix. Nourhane compose le numéro du centre et "
                "tombe sur une voix enregistrée qui donne cinq consignes. "
                "Puis c'est à elle : une minute, personne en face, aucune "
                "question possible.",
        duree='75 minutes')

    d.titre(notes="Première séance du bloc B. Faire écouter le dialogue en entier, sans "
                  "rien montrer, avant toute explication : le groupe doit d'abord "
                  "éprouver ce que c'est que d'entendre un menu sans pouvoir le "
                  "relire. Puis seulement, ouvrir le texte.")

    d.objectifs([
        "comprendre un menu téléphonique et choisir la bonne touche ;",
        "reconnaître les cinq morceaux d'un message et leur ordre ;",
        "commencer par son nom et son groupe, jamais par la raison ;",
        "dire un numéro de téléphone par groupes de chiffres, deux fois.",
    ], notes="Le troisième objectif est le seul qui demande un vrai changement "
             "d'habitude. Tout le monde commence spontanément par la raison : c'est "
             "l'ordre de la pensée, ce n'est pas l'ordre du message.")

    d.declencheur(
        'Observation', "Un réveille-matin dans une chambre encore sombre. "
                       "Il est quelle heure ?",
        image=img('reveil-avant-aube.jpg'),
        pistes=[
            "À quelle heure décide-t-on qu'on ne pourra pas aller au cours ?",
            "Le bureau ouvre à huit heures : que faites-vous entre-temps ?",
            "Est-ce mieux d'appeler tôt ou d'attendre l'ouverture ?",
            "Qu'est-ce qui prouve que vous avez prévenu avant l'heure du cours ?",
        ],
        notes="La quatrième piste est la réponse à la troisième : le message est "
              "horodaté. Un message laissé à sept heures dix prouve ce qu'aucun appel "
              "de huit heures cinq ne prouvera.")

    d.dialogue('Dialogue · 1 de 4', "Vous avez rejoint le centre", [
        ("VOIX", "Bonjour. Vous avez rejoint le Centre d'éducation des "
                 "adultes de la Pointe-aux-Ormes.", True),
        ("VOIX", "Nos bureaux sont ouverts de huit heures à seize heures, du "
                 "lundi au vendredi.", True),
        ("VOIX", "Pour signaler une absence ou un retard, appuyez sur le 1.", True),
        ("VOIX", "Pour parler au secrétariat, appuyez sur le 2.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer que les heures d'ouverture arrivent avant les choix : "
             "c'est toujours le cas, et c'est le moment où l'attention retombe. Or "
             "c'est le seul renseignement qu'on ne pourra pas redemander.")

    d.dialogue('Dialogue · 2 de 4', "Ne faites rien", [
        ("VOIX", "Pour connaître le numéro d'un poste, appuyez sur le 3.", True),
        ("VOIX", "Pour réentendre ce menu, ne faites rien.", True),
        ("NOURHANE", "Le 1. C'est bien le 1, pour une absence.", True),
        ("VOIX", "Laissez votre message après le signal sonore. Pour "
                 "terminer, raccrochez.", True),
    ], notes="« Pour réentendre ce menu, ne faites rien » est la phrase la plus utile du "
             "dialogue : elle dit qu'on a le droit d'écouter deux fois. Beaucoup "
             "d'élèves appuient au hasard plutôt que d'attendre.")

    d.dialogue('Dialogue · 3 de 4', "Ici Nourhane Ouazzani, groupe 6", [
        ("NOURHANE", "Bonjour. Ici Nourhane Ouazzani, groupe 6, francisation "
                     "de jour.", True),
        ("NOURHANE", "Je vous appelle pour signaler mon absence "
                     "aujourd'hui, lundi le 14.", True),
        ("NOURHANE", "Je ne serai pas au cours parce que mon fils a une "
                     "otite et j'ai un rendez-vous à la clinique.", True),
    ], notes="Trois phrases, trois morceaux. Les faire compter par le groupe. Faire "
             "remarquer que la raison arrive en troisième position, jamais avant.")

    d.dialogue('Dialogue · 4 de 4', "Je répète : 450 555-0147", [
        ("NOURHANE", "Je serai en classe demain matin et je remettrai le "
                     "papier de la clinique jeudi.", True),
        ("NOURHANE", "Mon nom s'épelle O, U, A, deux Z, A, N, I. Ouazzani.", True),
        ("NOURHANE", "Vous pouvez me rappeler au 450 555-0147. Je répète : "
                     "450 555-0147.", True),
        ("NOURHANE", "Merci beaucoup. Bonne journée.", False),
    ], notes="L'épellation arrive tard, et c'est voulu : on se nomme d'abord "
             "normalement, on épelle ensuite. Faire épeler à chacun son nom de famille, "
             "puis le faire écrire par le voisin.")

    d.regle("Cinq morceaux, toujours dans cet ordre",
            "Qui vous êtes. Pourquoi vous appelez, avec la date. Le motif. "
            "Ce que vous ferez. Votre numéro, deux fois.",
            precision="Cinquante secondes suffisent. Ce qui fait déborder un "
                      "message, ce n'est jamais l'information : c'est "
                      "l'explication.",
            notes="Diapositive à photographier. Elle reste affichée jusqu'à E1, où elle "
                  "devient la grille d'évaluation de la production orale.")

    d.tableau('Le menu du centre', "Cinq consignes, cinq touches",
              ['La touche', 'Ce qu\'elle donne'],
              [["Le 1", "Signaler une absence ou un retard."],
               ["Le 2", "Parler au secrétariat, aux heures d'ouverture."],
               ["Le 3", "Connaître le numéro d'un poste."],
               ["Rien", "Réentendre le menu depuis le début."]],
              cle=1,
              notes="Faire écouter le menu une seconde fois en demandant au groupe de "
                    "lever un, deux ou trois doigts au bon moment. C'est un exercice "
                    "d'écoute rapide, et il fait rire.")

    d.piege("Commencer par la raison",
            "Bonjour, mon fils est malade, il a une otite depuis hier soir, "
            "alors...",
            "Bonjour. Ici Nourhane Ouazzani, groupe 6, francisation de jour.",
            "La personne écoute trente secondes sans savoir de qui il s'agit, "
            "puis doit tout réécouter. Votre nom d'abord : c'est ce qu'elle écrit "
            "en premier sur son papier.",
            notes="Faire l'expérience : l'enseignant lit un message qui commence par la "
                  "raison, et demande au groupe d'écrire le nom de la personne. "
                  "Personne n'y arrive. La démonstration vaut mieux que la règle.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Il faut appuyer sur le 1 pour signaler une absence.", "vrai"),
        ("Le menu dit que les bureaux ouvrent à sept heures.", "faux — à huit heures"),
        ("Pour réentendre le menu, il ne faut rien faire.", "vrai"),
        ("Nourhane commence par la raison de son absence.", "faux — par son nom"),
        ("Elle laisse son numéro une seule fois.", "faux — deux fois"),
        ("Elle épelle son nom de famille.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la réplique exacte. La cinquième est "
             "celle qu'on manque : on entend le numéro et on ne compte pas les fois.")

    d.billet(
        "Reprenez la phrase que vous avez écrite en A4 et ajoutez devant "
        "votre nom, votre groupe et la date.",
        exemples=[
            "Trois morceaux sur cinq : c'est déjà l'essentiel.",
            "Écrivez-les dans l'ordre, comme au téléphone.",
        ],
        notes="Ramasser les billets. Ils reviennent en B4, où l'on ajoutera les deux "
              "derniers morceaux et où l'on chronométrera le tout.")

    return d.save(dossier)
