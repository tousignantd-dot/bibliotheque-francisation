# -*- coding: utf-8 -*-
"""A1 · Cinq façons de parler de la même affaire
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercices `prVF` et `prGenres`, cinq premières
cartes de FC_CARDS.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Cinq façons de parler de la même affaire",
        chapeau="La laveuse de Nadège ne vidange plus. Le même sujet va "
                "revenir cinq fois cette session, dans cinq genres "
                "différents, et jamais de la même manière.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : "
                  "qu'est-ce qui a brisé chez vous cette année, et qu'est-ce que vous "
                  "avez fait ? Presque tout le monde a une histoire d'appareil, et "
                  "presque personne n'a réclamé. C'est exactement le sujet du module.")

    d.objectifs([
        "nommer les cinq genres : la chronique pratique, l'entrevue, "
        "le documentaire, le fait divers, le courrier des lecteurs ;",
        "dire d'avance ce que chaque genre va donner, et ce qu'il ne "
        "donnera pas ;",
        "distinguer une chronique d'une nouvelle ;",
        "employer les cinq premiers mots du dossier avec leur article.",
    ], notes="Le deuxième objectif est celui du module entier : savoir d'avance ce "
             "qu'on va trouver, c'est déjà la moitié de la compréhension.")

    d.declencheur(
        'Observation', "Où prends-tu tes nouvelles, et sous quelle forme ?",
        pistes=[
            "À la radio le matin, à la télévision le soir, sur un téléphone ?",
            "As-tu déjà lu la page des lettres dans un journal ?",
            "Sais-tu qui écrit ces lettres, et si elles sont payées ?",
            "Qu'est-ce qui t'a le plus étonné dans les médias d'ici ?",
        ],
        notes="Question sans mauvaise réponse. Beaucoup d'élèves suivent surtout "
              "l'actualité de leur pays d'origine. Ne rien dévaloriser : s'en servir "
              "au contraire pour comparer les genres d'un pays à l'autre.")

    d.dialogue('Dialogue · 1 de 3', "Ma laveuse ne vidange plus", [
        ("NADÈGE", "Raphaël, tu écoutes CFTR le matin, toi ?", True),
        ("RAPHAËL", "Quand je conduis, oui. Pourquoi, il s'est passé quelque chose ?", True),
        ("NADÈGE", "Non. C'est moi qui ai un problème. Ma laveuse ne vidange plus. Trois ans et quatre mois, et le marchand me dit que la garantie est finie.", True),
        ("RAPHAËL", "Ah. Tu devrais écouter Claudine Rousseau, mardi matin. Elle fait une chronique là-dessus à peu près quatre fois par année.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Trois ans et quatre mois, 780 dollars : ces deux chiffres reviennent "
             "dans les quatre blocs. Les écrire au tableau dès maintenant et les y "
             "laisser toute la séance.")

    d.dialogue('Dialogue · 2 de 3', "Une chronique, c'est quoi exactement ?", [
        ("NADÈGE", "Une chronique, c'est quoi exactement ? J'entends le mot tout le temps et je ne suis jamais certaine.", True),
        ("RAPHAËL", "C'est un rendez-vous. La même personne revient chaque semaine, à la même heure, sur le même genre de sujet.", True),
        ("NADÈGE", "Donc ce n'est pas une nouvelle.", True),
        ("RAPHAËL", "Non. Une nouvelle, ça t'apprend qu'il est arrivé quelque chose. Une chronique pratique, ça t'apprend quoi faire.", True),
    ], notes="La dernière réplique est la définition du module. La faire répéter par "
             "deux élèves, puis demander un exemple de chronique dans leur langue.")

    d.dialogue('Dialogue · 3 de 3', "Des lettres signées par du monde ordinaire", [
        ("NADÈGE", "Le journal du quartier, il y a deux pages que je ne comprends pas. Des lettres, avec des noms de monde ordinaire en dessous.", True),
        ("RAPHAËL", "Le courrier des lecteurs. Ce sont des gens comme toi et moi qui écrivent au journal. Personne ne les paie.", True),
        ("NADÈGE", "Alors ce n'est pas de l'information.", True),
        ("RAPHAËL", "C'est de l'opinion, et ça se présente comme telle. Cinq façons de parler de la même affaire, finalement.", True),
    ], notes="Annoncer ici la production écrite de E2 : dans quatre semaines, chacun "
             "écrira sa propre lettre au Courrier de la Batture. Le dire tôt donne un "
             "but à tout le reste.")

    d.tableau('Analyse', "Les cinq genres, et ce que chacun te donne",
              ['Le genre', 'Ce que tu y trouves'],
              [["La chronique pratique", "une démarche à suivre, expliquée étape par étape"],
               ["L'entrevue", "ce qu'un invité accepte de dire, en réponse à des questions"],
               ["Le documentaire", "l'histoire longue d'un sujet, dite par une voix hors champ"],
               ["Le fait divers", "quinze lignes sur un accident, sans aucun avis"],
               ["Le courrier des lecteurs", "des opinions signées par des gens ordinaires"]],
              cle=0,
              note="Les cinq peuvent parler du même sujet la même semaine, sans dire la même chose.",
              notes="Diapositive à photographier. C'est le tableau de référence de tout "
                    "le module ; il revient en A4 sous forme d'exercice, puis à chaque "
                    "ouverture de défi.")

    d.regle("Savoir d'avance ce qu'on va trouver",
            "Reconnaître le genre, c'est déjà avoir compris la moitié du texte.",
            precision="Devant une chronique pratique, tu cherches des étapes. Devant "
                      "un fait divers, tu cherches ce qui est arrivé, où et quand. "
                      "Devant une lettre de lecteur, tu cherches une opinion et la "
                      "raison qui l'appuie. Ce n'est pas le même travail, et ce n'est "
                      "pas la même écoute.",
            notes="Diapositive à photographier. Insister : on ne demande pas de tout "
                  "comprendre, on demande de savoir quoi chercher.")

    d.vocabulaire('Vocabulaire', "Les cinq genres, avec leur article", [
        ("une chronique pratique", "Un rendez-vous où la même personne revient expliquer comment faire quelque chose."),
        ("une entrevue", "Un échange où quelqu'un pose les questions et où l'invité répond."),
        ("un documentaire", "Une longue émission racontée par une voix qu'on ne voit pas."),
        ("un fait divers", "Un texte très court sur un accident, un vol ou un incendie, sans avis."),
        ("le courrier des lecteurs", "La page où le journal publie les lettres signées de gens ordinaires."),
    ], notes="Faire répéter chaque mot avec son article. « Le courrier des lecteurs » "
             "prend le défini : il n'y en a qu'un par journal. Le faire remarquer.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la conversation de Nadège et de Raphaël.", [
        ("La laveuse a cessé de vidanger après trois ans et quatre mois.", "vrai"),
        ("Le marchand a répondu que la garantie était expirée.", "vrai"),
        ("Selon Raphaël, une chronique t'apprend qu'il est arrivé quelque chose.", "faux - elle t'apprend quoi faire"),
        ("Dans une entrevue, il faut écouter les questions autant que les réponses.", "vrai"),
        ("Les auteurs du courrier des lecteurs sont payés par le journal.", "faux - personne ne les paie"),
        ("Le fait divers donne l'avis du journaliste sur ce qui est arrivé.", "faux - aucun avis, jamais"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le cinquième "
             "surprend toujours : beaucoup croient que le journal paie ses lecteurs.")

    d.billet(
        "Quel genre voudrais-tu comprendre en premier, et pourquoi ?",
        exemples=[
            "Une phrase suffit.",
            "Pense à ce que tu écoutes ou lis déjà, même dans ta langue.",
        ],
        notes="Deux minutes. Les réponses servent en A4 : elles disent quel genre "
              "intimide le plus le groupe, et c'est celui-là qu'il faudra travailler "
              "le plus lentement.")

    return d.save(dossier)
