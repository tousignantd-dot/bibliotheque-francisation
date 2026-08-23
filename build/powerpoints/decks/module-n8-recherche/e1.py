# -*- coding: utf-8 -*-
"""E1 · Le jeu de rôle et la production orale
Bloc E « Je me lance » · couleur teal · 75 min.
Source : bloc `custom` du module — jeu de rôle `selection` et production
orale. Intention du programme : participer à une entrevue de sélection
comportant plusieurs étapes, en production comme en compréhension.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="C'est à vous : quarante-cinq minutes devant le comité",
        chapeau="Tout ce qui a été appris depuis quatre séances se joue ici, "
                "d'un coup et sans filet. Le jeu de rôle sert de répétition ; "
                "l'enregistrement, de preuve.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Ouvrir en faisant relire à voix haute la "
                  "phrase préparée en D2 — celle de la question interdite. Chacun la "
                  "dit une fois, debout.")

    d.objectifs([
        "tenir une entrevue de sélection avec l'assistant, du début à la fin ;",
        "répondre à chaque question par un exemple daté et chiffré ;",
        "raconter à voix haute une décision prise seul, en trois temps ;",
        "négocier une condition en offrant une contrepartie.",
    ], notes="Séance de production, pas d'enseignement. Le temps de parole de "
             "l'enseignante doit rester sous dix minutes.")

    d.declencheur(
        'Préparation', "Trois choses à avoir en tête avant de commencer",
        pistes=[
            "Votre exemple daté : lequel, avec quel chiffre ?",
            "L'objection que votre dossier pose : laquelle, et votre réponse ?",
            "La condition que vous demanderez, et ce que vous offrez en échange.",
            "Votre phrase pour la question interdite.",
        ],
        notes="Cinq minutes en silence, au crayon. Personne ne commence l'entrevue "
              "sans avoir les quatre écrites devant soi.")

    d.tableau('Jeu de rôle', "Trois situations, un même comité",
              ['Situation', 'Ce qui s\'y joue'],
              [["Le poste de superviseure",
                "expliquer un choix, donner un exemple daté et chiffré"],
               ["Onze ans qui ne comptent pas",
                "faire valoir une expérience acquise ailleurs, concéder puis avancer"],
               ["L'échelon qui n'est pas affiché",
                "proposer une contrepartie datée plutôt que demander"]],
              cle=0,
              note="L'assistant joue le directeur de la production. Il ne se contente jamais d'une qualité annoncée.",
              notes="Diapositive à photographier. Prévenir le groupe : le directeur "
                    "laissera passer, une fois, une question qu'il n'a pas le droit "
                    "de poser. C'est voulu, et c'est là que la phrase de D2 sert.")

    d.cartes('Jeu de rôle', "Les huit sujets à couvrir", [
        ("Se présenter, puis laisser mener",
         "Une phrase, pas trois. C'est le comité qui conduit l'entrevue, et "
         "l'occuper d'entrée se paie tout de suite."),
        ("Répondre par un exemple",
         "Jamais par une qualité. « Je suis rigoureuse » ne prouve rien ; "
         "« quatre cents caisses, onze jours de production » prouve."),
        ("Nommer l'objection",
         "Ce qui gêne dans votre dossier, dites-le vous-même, en une phrase, "
         "sans vous excuser, et donnez la vraie raison."),
        ("Négocier en offrant",
         "Un échelon tout de suite, le suivant lié à un résultat daté et "
         "mesurable. Et acceptez que le refus soit écrit aussi."),
    ], notes="Les huit sujets complets sont dans le module. Ces quatre-là sont ceux "
             "qu'on rate, et ce sont ceux qu'il faut nommer avant de commencer.")

    d.regle("Réutilisez ce que vous venez d'apprendre",
            "Certes cette expérience a été acquise ailleurs, mais elle porte "
            "sur vingt-deux personnes. Si j'avais eu les données, j'aurais "
            "arrêté la ligne plus tôt. Ce que j'apporte, c'est seize ans "
            "d'usine.",
            precision="Concession, hypothèse irréelle, mise en relief : les trois "
                      "points de langue du bloc, chacun dans une phrase. Un candidat "
                      "qui les emploie une fois chacun se distingue sans avoir à "
                      "hausser le ton.",
            notes="Diapositive à photographier et à garder affichée pendant tout le "
                  "jeu de rôle.")

    d.tableau('Production orale', "Raconter une décision, en trois temps",
              ['Temps', 'Ce qu\'on dit'],
              [["1. Annoncer",
                "Je vais vous parler d'un soir où j'ai dû arrêter une ligne seule."],
               ["2. Situation, geste, résultat",
                "Trois problèmes, quinze personnes qui attendent, quarante minutes perdues, aucune caisse fausse."],
               ["3. Autrement, puis la règle",
                "Si j'avais eu les données, j'aurais arrêté plus tôt. Depuis, je note l'heure avant tout."]],
              cle=0,
              notes="Diapositive à photographier. Deux minutes environ, debout, sans "
                    "lire ses notes mot à mot. C'est le récit préparé en devoir de D1.")

    d.pratique('Production orale', "Ce qu'on écoute chez l'autre",
               "Pendant que quelqu'un parle, cochez ce que vous entendez.", [
        ("Une date précise", "année, mois ou jour"),
        ("Un chiffre vérifiable", "un nombre de personnes, d'heures, de caisses"),
        ("Une hypothèse irréelle", "si j'avais..., j'aurais..."),
        ("Une règle appliquée depuis", "depuis, je..."),
        ("Une mise en relief", "ce que j'apporte, c'est..."),
    ], corrige=False,
       notes="Grille d'écoute mutuelle. Elle vaut mieux qu'une correction de "
             "l'enseignante : entendre ce qui manque chez l'autre fait entendre ce "
             "qui manque chez soi.")

    d.piege('Piège', "répondre par une qualité",
            "répondre par un exemple",
            "« Je suis rigoureuse », « j'aime le travail d'équipe », « je "
            "m'adapte vite » : trois phrases qu'un comité entend vingt fois "
            "par jour et qui ne laissent aucune trace. Une date et un chiffre "
            "en laissent une, même six semaines plus tard.",
            notes="C'est la faute la plus fréquente, et elle vient d'un bon réflexe : "
                  "on veut se décrire. Le comité, lui, veut savoir ce qu'on a fait.")

    d.billet(
        "Enregistrez votre récit et déposez-le dans le module.",
        exemples=[
            "Réécoutez-vous avant d'envoyer : entendez-vous une date et un chiffre ?",
            "Si non, refaites-le. Personne ne le fait du premier coup.",
        ],
        notes="Le dépôt se fait dans « Je me lance ». Rappeler que la correction de "
              "l'IA reste privée : seul ce que l'élève envoie parvient à "
              "l'enseignante.")

    return d.save(dossier)
