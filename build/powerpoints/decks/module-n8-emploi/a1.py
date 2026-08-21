# -*- coding: utf-8 -*-
"""A1 · Ta description de tâches, au complet.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercices `pr1` et `prTaches`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n8-emploi/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Ta description de tâches, au complet",
        chapeau="Un poste, ce n'est pas un titre : c'est une liste de gestes, "
                "avec des heures et des montants. Comprendre cette liste en "
                "détail, c'est la première compétence d'un employé.",
        duree='75 minutes')

    d.titre(notes="Première séance du module et du niveau 8. Demander d'abord qui, "
                  "dans le groupe, travaille en ce moment, et qui a déjà reçu une "
                  "description de tâches écrite. La réponse est presque toujours non : "
                  "c'est le point de départ.")

    d.objectifs([
        "suivre une explication détaillée sur des tâches professionnelles ;",
        "repérer les chiffres qui commandent une consigne ;",
        "poser une question de précision au bon moment ;",
        "distinguer ce qui est écrit de ce qui se transmet autrement.",
    ], notes="Le quatrième objectif est celui du niveau 8. Un poste s'apprend par deux "
             "canaux : le document, et la culture du lieu. Le module montre les deux.")

    d.declencheur(
        'Observation', "Qui vous a expliqué votre travail ?",
        image=IMG + 'bons-commande.jpg',
        pistes=[
            "Aviez-vous un document écrit ?",
            "Combien de temps a duré l'explication ?",
            "Qu'est-ce que vous avez compris seulement après des mois ?",
            "À qui posiez-vous vos questions ?",
        ],
        notes="Laisser venir les récits. Beaucoup diront « personne ne m'a rien "
              "expliqué ». C'est fréquent, et ce n'est pas une fatalité : le module "
              "donne les mots pour demander.")

    d.dialogue('Dialogue · 1 de 3', "Quatre blocs, et des chiffres", [
        ("MANON", "Ça fait huit mois que tu es avec nous, et on ne t'a jamais expliqué ta description de tâches au complet.", True),
        ("NADIA", "Je l'ai lue le premier jour, mais je ne comprenais pas encore la moitié des mots.", True),
        ("MANON", "Le premier bloc, c'est la réception des commandes : tu les entres dans le système avant midi.", True),
        ("NADIA", "Et quand un bon arrive à deux heures de l'après-midi ?", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Nadia pose une question de cas particulier tout de suite. C'est exactement "
             "ce qu'on attend d'un employé : la règle générale ne suffit jamais.")

    d.dialogue('Dialogue · 2 de 3', "Les montants décident", [
        ("MANON", "Tu compares les factures avec les bons de commande. Si l'écart est en bas de vingt-cinq dollars, tu approuves.", True),
        ("NADIA", "Vingt-cinq dollars, d'accord. Et si c'est un fournisseur qui se trompe chaque fois ?", True),
        ("MANON", "Tu le notes dans le tableau partagé, et on en parle à la réunion du mois.", True),
        ("NADIA", "Le compte rendu, c'est la partie qui m'inquiète le plus, honnêtement.", True),
    ], notes="Faire remarquer que Nadia répète le chiffre à voix haute : « vingt-cinq "
             "dollars, d'accord ». C'est une stratégie d'écoute, pas un tic.")

    d.dialogue('Dialogue · 3 de 3', "Ce qui n'est écrit nulle part", [
        ("YVES", "Puis, elle t'a passé le grand portrait ?", True),
        ("NADIA", "Le grand portrait au complet, oui. Quatre blocs, avec les heures et les montants.", True),
        ("YVES", "Le gars de la découpe part à une heure. Si le bon n'est pas entré, la commande attend à demain.", True),
        ("NADIA", "Ça, ce n'est écrit nulle part dans ma description de tâches.", True),
    ], notes="La bascule de registre est ici. Yves ne dit pas les mêmes mots que Manon, "
             "et il donne l'information la plus utile de la séance. Y revenir en A3.")

    d.tableau('Analyse', "Quatre blocs, quatre règles chiffrées",
              ['Le bloc', 'La règle qui va avec'],
              [["La réception des commandes", "entrées avant midi ; après midi, on avertit Yves"],
               ["Le suivi des livraisons", "appel au transporteur le mardi et le jeudi"],
               ["Les factures des fournisseurs", "écart de moins de 25 $ : on approuve seul"],
               ["La réunion de production", "compte rendu rédigé dans les deux jours"]],
              cle=0,
              note="Une description de tâches utile tient dans un tableau de deux colonnes.",
              notes="Diapositive à photographier. Proposer à chacun de faire le sien pour "
                    "son propre emploi, en devoir à long terme du module.")

    d.regle("Le détail qui commande",
            "Dans une consigne de travail, le chiffre est la consigne.",
            precision="« Entre les bons rapidement » ne veut rien dire ; « avant midi » "
                      "se vérifie. « Un petit écart » ne veut rien dire ; « moins de "
                      "vingt-cinq dollars » se décide seul. Quand une consigne n'a pas "
                      "de chiffre, il faut le demander — c'est le geste professionnel le "
                      "plus rentable qu'un employé puisse faire.",
            notes="Diapositive à photographier. Elle fonde tout le module : la paie, la "
                  "réunion et la demande de formation se gagnent avec des chiffres.")

    d.piege("Dire oui sans avoir compris",
            "Oui oui, ça va, j'ai compris.",
            "Pour être certaine : avant midi, ça vaut aussi le vendredi ?",
            "Personne ne pense du mal d'un employé qui demande une précision le premier "
            "jour. Tout le monde pense du mal de celui qui se trompe six mois plus tard "
            "sur une consigne qu'il n'avait jamais comprise. La question de précision "
            "coûte dix secondes ; l'erreur coûte une journée de production.",
            notes="Faire répéter la formule « pour être certaine… ». Elle revient en C4, "
                  "quand Nadia vérifie une échéance en pleine réunion.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Nadia travaille chez Valmont depuis huit mois.", "vrai"),
        ("Les bons doivent être entrés avant midi.", "vrai"),
        ("Un bon reçu en après-midi n'est pas entré du tout.", "faux — il est entré, et on avertit Yves"),
        ("Elle approuve seule les écarts jusqu'à cent dollars.", "faux — vingt-cinq dollars"),
        ("Le compte rendu se rédige dans les deux jours.", "vrai"),
        ("Un compte rendu rapporte ce que chaque personne a dit.", "faux — les décisions, les responsables, les dates"),
        ("La raison de la règle de midi est écrite dans le document.", "faux — Yves l'explique à la pause"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le dialogue est "
             "long : accepter deux écoutes.")

    d.billet(
        "Écrivez les quatre gestes que vous faites le plus souvent au travail.",
        exemples=[
            "Pour chacun, y a-t-il une heure ou un montant à respecter ?",
            "Lequel n'est écrit dans aucun document ?",
        ],
        notes="Devoir concret. Ces quatre lignes reviennent en A4 pour le vocabulaire, "
              "et en E1 comme matière du jeu de rôle.")

    return d.save(dossier)
