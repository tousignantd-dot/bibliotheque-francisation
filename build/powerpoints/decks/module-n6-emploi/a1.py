# -*- coding: utf-8 -*-
"""A1 · Un papier neuf sur le babillard
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercices `prVF` et `prEcrits`, quatre premières
cartes de FC_CARDS.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Un papier neuf sur le babillard",
        chapeau="Un poste se libère chez Emballages Bocage. Le même dossier "
                "va revenir quatre fois cette session, dans quatre écrits "
                "différents, et jamais de la même manière.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : "
                  "y a-t-il un babillard à votre travail, et qui le lit ? Presque "
                  "tout le monde en a vu un, presque personne ne s'arrête devant. "
                  "C'est exactement le sujet du module.")

    d.objectifs([
        "nommer les quatre écrits du travail : l'affichage, la note de "
        "service, la politique, le compte rendu ;",
        "dire d'avance ce que chaque écrit va donner, et ce qu'il ne "
        "donnera pas ;",
        "distinguer une mutation d'une promotion ;",
        "employer les quatre premiers mots du dossier avec leur article.",
    ], notes="Le deuxième objectif est celui du module entier : savoir d'avance ce "
             "qu'on va trouver dans un papier, c'est déjà la moitié de la lecture.")

    d.declencheur(
        'Observation', "Comment apprend-on qu'un poste se libère, là où tu travailles ?",
        pistes=[
            "Par un papier au mur, par un courriel, ou par la rumeur ?",
            "As-tu déjà vu quelqu'un changer de poste dans la même entreprise ?",
            "Faut-il demander la permission à son chef d'équipe, selon toi ?",
            "Qu'est-ce qui t'a le plus étonné du monde du travail d'ici ?",
        ],
        notes="Question sans mauvaise réponse. Beaucoup d'élèves ont connu un marché "
              "du travail où tout passe par la relation personnelle. Ne rien "
              "dévaloriser : s'en servir pour comparer, et pour faire sentir ce "
              "qu'une procédure écrite change — elle est lente, mais elle est la "
              "même pour tout le monde.")

    d.dialogue('Dialogue · 1 de 3', "Un affichage interne, c'est quoi ?", [
        ("YANETH", "Ghislain, il y a un papier neuf sur le babillard, à côté de la porte du vestiaire.", True),
        ("GHISLAIN", "Ça, c'est un affichage interne. Quand un poste se libère, l'entreprise le montre d'abord à ceux qui travaillent déjà ici.", True),
        ("YANETH", "Alors ce n'est pas une annonce comme celles qu'on voit sur Internet.", True),
        ("GHISLAIN", "Non. Un affichage interne, c'est pour nous autres. Et il y a un délai : dix jours ouvrables, puis il descend.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="« Dix jours ouvrables » et « vendredi 25 septembre, 16 h » : ces deux "
             "repères reviennent dans les quatre blocs. Les écrire au tableau dès "
             "maintenant et les y laisser toute la séance.")

    d.dialogue('Dialogue · 2 de 3', "Le poste, et qui peut se présenter", [
        ("YANETH", "Et le poste, c'est lequel ?", True),
        ("GHISLAIN", "Vérificatrice à la qualité, à l'atelier de conditionnement. Quart de jour. C'est la personne qui prend les échantillons et qui remplit les feuilles de contrôle.", True),
        ("YANETH", "Ça m'intéresse. J'ai fait deux ans à l'expédition et je connais le plancher par cœur.", True),
        ("GHISLAIN", "Tu as le droit de te présenter. Ce n'est pas une promotion, c'est une mutation : tu changes de poste, tu restes dans la même entreprise.", True),
    ], notes="La dernière réplique porte la distinction du bloc. La faire répéter par "
             "deux élèves, puis demander si le mot « mutation » existe dans leur "
             "langue et ce qu'il y recouvre.")

    d.dialogue('Dialogue · 3 de 3', "Quatre papiers pour un seul poste", [
        ("YANETH", "Et il faut que je te demande la permission ?", True),
        ("GHISLAIN", "Non, et c'est là que bien du monde se trompe. Ton chef d'équipe est avisé, il n'a rien à signer.", True),
        ("YANETH", "Une note de service, une politique, un affichage… Ça fait bien des papiers pour un seul poste.", True),
        ("GHISLAIN", "Il y en aura un quatrième : le compte rendu. Chacun a son travail. L'affichage annonce, la note explique, la politique fixe les règles, le compte rendu raconte.", True),
    ], notes="Annoncer ici les deux productions de E1 et E2 : dans quatre semaines, "
             "chacun décrira la démarche à voix haute et écrira son courriel aux "
             "ressources humaines. Le dire tôt donne un but à tout le reste.")

    d.tableau('Analyse', "Les quatre écrits, et ce que chacun te donne",
              ["L'écrit", 'Ce que tu y trouves'],
              [["L'affichage", "le poste, le quart, les exigences, la date limite"],
               ["La note de service", "une explication au personnel, avec la marche à suivre"],
               ["La politique", "les règles écrites, numérotées article par article"],
               ["Le compte rendu", "ce qui a été dit et décidé à une rencontre"]],
              cle=0,
              note="Les quatre peuvent parler du même poste la même semaine, sans dire la même chose.",
              notes="Diapositive à photographier. C'est le tableau de référence de tout "
                    "le module ; il revient en A4 sous forme d'exercice, puis à chaque "
                    "ouverture de défi.")

    d.regle("Savoir d'avance ce qu'on va trouver",
            "Reconnaître la sorte de papier, c'est déjà avoir compris la moitié du texte.",
            precision="Devant un affichage, tu cherches une date limite. Devant une "
                      "note de service, tu cherches des gestes à poser. Devant une "
                      "politique, tu cherches une règle et son numéro. Devant un "
                      "compte rendu, tu cherches une décision. Ce n'est pas le même "
                      "travail, et ce n'est pas la même lecture.",
            notes="Diapositive à photographier. Insister : on ne demande pas de tout "
                  "comprendre, on demande de savoir quoi chercher.")

    d.vocabulaire('Vocabulaire', "Les quatre premiers mots, avec leur article", [
        ("un babillard", "Le tableau du mur où l'employeur pose les papiers que tout le personnel doit voir."),
        ("un affichage interne", "L'annonce d'un poste libre, montrée d'abord aux personnes déjà employées."),
        ("une mutation", "Le passage d'un poste à un autre sans changer d'employeur."),
        ("une candidature interne", "La demande écrite d'une personne déjà employée qui veut un autre poste."),
    ], notes="Faire répéter chaque mot avec son article. « Un babillard » est un mot "
             "du Québec : ailleurs on dit « un tableau d'affichage ». Le signaler, "
             "c'est utile.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la conversation de Yaneth et de Ghislain.", [
        ("L'affichage interne s'adresse d'abord à ceux qui travaillent déjà là.", "vrai"),
        ("Dix jours ouvrables, ce sont dix jours de calendrier.", "faux - les fins de semaine ne comptent pas"),
        ("Le poste affiché est celui de vérificatrice à la qualité.", "vrai"),
        ("Yaneth doit obtenir la permission de son chef d'équipe.", "faux - il est avisé, rien de plus"),
        ("Les formulaires se déposent aux ressources humaines, au bureau douze.", "vrai"),
        ("Selon Ghislain, l'affichage dit la démarche au complet.", "faux - il dit le poste et la date, pas la démarche"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le quatrième "
             "surprend toujours : beaucoup croient qu'il faut la permission du chef, "
             "et c'est la croyance qui empêche le plus de gens de se présenter.")

    d.billet(
        "Quel papier voudrais-tu savoir lire en premier, et pourquoi ?",
        exemples=[
            "Une phrase suffit.",
            "Pense à un papier que tu as déjà reçu au travail et que tu n'as pas lu.",
        ],
        notes="Deux minutes. Les réponses servent en A4 : elles disent quel écrit "
              "intimide le plus le groupe, et c'est celui-là qu'il faudra travailler "
              "le plus lentement.")

    return d.save(dossier)
