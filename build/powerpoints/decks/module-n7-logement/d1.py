# -*- coding: utf-8 -*-
"""D1 · À la caisse, puis la promesse d'achat
Bloc D « Défi 3 · La promesse d'achat » · couleur acier · compréhension orale
et écrite · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3prom` (type `texte`, treize
passages cliquables).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="À la caisse, puis la promesse d'achat",
        chapeau="Une promesse d'achat acceptée n'est pas une intention : "
                "c'est un contrat. Ce qui la rend supportable, ce sont ses "
                "conditions — et chacune porte un nombre de jours.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 3, et séance la plus dense du module : un "
                  "dialogue de vingt-cinq répliques et un document. Prévoir de couper "
                  "l'écoute en trois, et de garder le document pour la seconde heure.")

    d.objectifs([
        "comprendre ce qu'est une mise de fonds et à quel seuil elle se calcule ;",
        "distinguer ce qui engage de ce qui protège dans une promesse d'achat ;",
        "relever le délai de chaque condition ;",
        "nommer ce que le notaire fait et ce que la municipalité facture.",
    ], notes="Le deuxième objectif est le fil du bloc D. Le poser dès l'ouverture : la "
             "première moitié du document engage, la seconde protège.")

    d.dialogue('Dialogue · 1 de 3', "Cinq pour cent de deux cent soixante-quinze mille", [
        ("FARAH", "Commençons par la question que tout le monde pose en dernier : combien avez-vous de côté ?", True),
        ("SOKHNA", "Dix-neuf mille huit cents.", False),
        ("FARAH", "Pour une propriété de deux cent soixante-quinze mille, la mise de fonds minimale est de cinq pour cent, parce qu'on est sous cinq cent mille. Ça fait treize mille sept cent cinquante.", True),
        ("SOKHNA", "Donc j'ai assez ?", False),
        ("FARAH", "Pour le minimum, oui. Mais sous vingt pour cent de mise de fonds, votre prêt doit être assuré, et la prime s'ajoute à votre prêt.", True),
    ], consigne="Écouter deux fois, diapositive masquée.",
       notes="Refaire le calcul au tableau : 5 % de 275 000 = 13 750. Les élèves qui "
             "décrochent au moment des pourcentages raccrochent dès qu'on écrit les "
             "chiffres.")

    d.dialogue('Dialogue · 2 de 3', "Les frais dont personne ne parle", [
        ("SOKHNA", "Les droits de mutation, c'est la taxe de bienvenue ?", True),
        ("FARAH", "C'est le même impôt. C'est la municipalité qui le perçoit, et c'est le nouveau propriétaire qui le paie, quelques mois après l'achat.", True),
        ("SOKHNA", "Et le notaire, il est obligatoire ?", True),
        ("FARAH", "Pour l'acte hypothécaire, oui. C'est lui aussi qui fait l'examen des titres, c'est-à-dire qu'il vérifie que la personne qui vous vend a bien le droit de vous vendre.", True),
    ], notes="« Examen des titres » est le mot le plus opaque du module. Le reformuler "
             "une fois de plus au tableau, avec un exemple : une maison vendue deux "
             "fois, ça existe.")

    d.dialogue('Dialogue · 3 de 3', "À ma place, vous achèteriez ?", [
        ("SOKHNA", "Madame Zaoui, à ma place, vous achèteriez ?", True),
        ("FARAH", "Je ne peux pas répondre à ça, et personne ne devrait répondre à ça à votre place. Ce que je peux faire, c'est vous donner les deux chiffres.", True),
        ("FARAH", "Locataire, à mille vingt-quatre par mois, vous n'avez rien d'autre à payer et rien qui vous appartienne. Propriétaire, tout compris, vous seriez autour de mille six cents.", True),
        ("SOKHNA", "Six cents dollars de plus par mois.", True),
    ], notes="Retenir les deux chiffres : ils sont la matière de la production orale de "
             "E1. Et retenir la réponse de la conseillère : refuser de décider à la "
             "place de quelqu'un est un comportement professionnel, pas une dérobade.")

    d.tableau('Analyse', "Ce qui engage, ce qui protège",
              ['Dans la promesse', 'Ce que ça fait'],
              [["le prix et la date d'occupation", "ça vous engage"],
               ["les inclusions", "ça vous engage : ce qui n'est pas écrit n'est pas vendu"],
               ["la condition de financement", "ça vous protège : vingt et un jours"],
               ["la condition d'inspection", "ça vous protège : une dizaine de jours"],
               ["les déclarations du vendeur", "ça vous protège : ce qu'il affirme savoir"]],
              cle=0,
              notes="Diapositive à photographier. C'est le plan de lecture de "
                    "l'exercice `t3prom` : les treize questions suivent cet ordre.")

    d.regle("Les jours se comptent en jours de calendrier",
            "Samedis, dimanches et jours fériés compris.",
            precision="Dix jours pour l'inspection, ce n'est pas deux semaines de "
                      "travail : c'est une semaine et demie, fins de semaine comprises. "
                      "L'inspecteur doit donc être appelé le jour même de l'acceptation. "
                      "Vingt et un jours pour le financement, c'est trois semaines "
                      "pleines, et c'est un minimum raisonnable.",
            notes="Diapositive à photographier. Faire compter les dix jours sur le "
                  "calendrier du mois en cours, au tableau : la surprise est utile.")

    d.pratique('Compréhension écrite', "Où est la réponse dans la promesse ?",
               "Pour chaque question, retrouvez le passage exact.", [
        ("Quel prix l'acheteuse offre-t-elle ?", "268 000 $, payable à la signature"),
        ("Qu'est-ce qui est exclu de la vente ?", "le cabanon extérieur"),
        ("Combien de jours pour confirmer le financement ?", "vingt et un jours de calendrier"),
        ("Qui paie l'inspection du bâtiment ?", "l'acheteur"),
        ("Que peut-elle faire si l'inspection révèle un problème majeur ?", "baisse de prix, réparations, ou se retirer"),
        ("À partir de quand les deux parties sont-elles liées ?", "dès l'acceptation par le vendeur"),
    ], corrige=True,
       notes="Six des treize questions de `t3prom`. Les sept autres se font à l'écran, "
             "en autonomie, pendant la dernière demi-heure.")

    d.billet(
        "Quelle condition écrirais-tu, toi, dans une promesse d'achat ?",
        exemples=[
            "Le financement et l'inspection sont les deux habituelles.",
            "Y en a-t-il une troisième que tu voudrais ?",
        ],
        notes="Deux minutes. Les réponses ouvrent D2 : une condition s'écrit au "
              "subjonctif, et c'est exactement le point de grammaire suivant.")

    return d.save(dossier)
