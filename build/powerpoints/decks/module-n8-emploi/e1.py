# -*- coding: utf-8 -*-
"""E1 · Je me lance : l'appel et la réunion.
Bloc E « Je me lance » · couleur teal · 60 min.
Source : le jeu de rôle `emploi` et la production orale du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="L'appel et la réunion",
        chapeau="Tout ce qui a été appris se joue ici, à voix haute : régler "
                "un problème au téléphone, puis faire valoir son point de vue "
                "dans une réunion de décision.",
        duree='60 minutes')

    d.titre(notes="Séance de production orale. Le jeu de rôle avec l'assistant sert de "
                  "répétition ; la prise de parole enregistrée est ce qui sera remis.")

    d.objectifs([
        "régler un problème administratif au téléphone, du début à la fin ;",
        "tenir son bout après une objection de procédure ;",
        "intervenir dans une réunion en résumant, nuançant et proposant ;",
        "s'enregistrer, s'écouter, corriger, puis remettre.",
    ], notes="L'objectif 4 est un objectif de méthode. Insister : personne ne réussit "
             "au premier essai, et c'est l'intérêt de l'enregistrement.")

    d.cartes("Le jeu de rôle", "Trois situations, deux rôles", [
        ("Des heures supplémentaires non majorées",
         "44 heures travaillées, 4 au-delà de 40, payées au taux simple. Les heures avaient été demandées par courriel."),
        ("Un horaire changé sans avis",
         "Trois soirs au lieu de deux, sans que personne ait prévenu. Un cours est suivi le mercredi soir."),
        ("Une facture réglée deux fois",
         "1 840 $ payés en double, crédit promis il y a trois semaines et toujours absent."),
    ], cols=1,
       notes="L'assistant joue le service administratif. Il n'est pas de mauvaise foi, "
             "mais il objectera au moins une fois : c'est là que se joue la séance.")

    d.tableau('Plan', "Les sept temps de l'appel",
              ['Le temps', 'Ce qu\'on dit'],
              [["1. Se présenter et situer", "qui appelle, et de quel dossier il s'agit"],
               ["2. Exposer", "les faits, avec leurs dates et leurs chiffres"],
               ["3. Nommer l'écart", "à la voix passive, sans accuser personne"],
               ["4. Répondre à l'objection", "reconnaître la contrainte, puis maintenir"]],
              cle=0,
              note="Les trois derniers temps : citer la règle, demander quoi et de qui, obtenir une confirmation écrite.",
              notes="Diapositive à photographier. C'est la liste à cocher du module, "
                    "reprise de B1.")

    d.regle("La phrase qui sauve un appel",
            "Qu'est-ce qu'il vous faut, exactement, et de qui ?",
            precision="Quand l'autre oppose une procédure, ne discutez pas la procédure : "
                      "demandez ce dont elle a besoin pour avancer. Vous passez d'un "
                      "désaccord à une marche à suivre, et vous raccrochez avec une "
                      "action et une date au lieu d'une promesse vague.",
            notes="Diapositive à photographier. À afficher pendant tout le jeu de rôle.")

    d.pratique('Préparation', "Bonne idée, mauvaise idée ?",
               "Avant de composer le numéro.", [
        ("Écrire les dates et les chiffres sur un papier.", "bonne idée"),
        ("Commencer en disant que c'est inacceptable.", "mauvaise idée"),
        ("Nommer la norme sans accuser la personne.", "bonne idée"),
        ("Accepter « on va regarder ça » sans date.", "mauvaise idée"),
        ("Demander une confirmation écrite en expliquant pourquoi.", "bonne idée"),
        ("Menacer de porter plainte dès la première phrase.", "mauvaise idée"),
        ("Vérifier si d'autres périodes sont touchées.", "bonne idée"),
    ], corrige=True,
       notes="Cinq minutes, en groupe entier, avant d'ouvrir les postes.")

    d.tableau('Production orale', "Intervenir dans la réunion",
              ['Le temps', 'Ce qu\'on dit'],
              [["Temps 1 · Résumer", "Si je résume, l'écart de prix est réel : environ 40 000 $."],
               ["Temps 2 · Objecter avec un chiffre", "Cependant, le délai passerait à dix jours."],
               ["Temps 3 · Proposer au conditionnel", "Je proposerais un partage entre les deux fournisseurs."]],
              cle=0,
              note="Environ 90 secondes. On s'enregistre, on s'écoute, on recommence.",
              notes="C'est la production qui sera déposée. Rappeler la mélodie de A2 : "
                    "la voix descend au dernier groupe de chaque phrase.")

    d.piege("Parler plus fort quand on n'est pas écouté",
            "Non mais écoutez, c'est dix jours, dix jours !",
            "C'est écrit à la page quatre ; j'ai vérifié deux fois.",
            "En réunion, le volume ne convainc personne et coûte la crédibilité. Ce qui "
            "convainc, c'est la source et le chiffre. Nadia fait changer une décision de "
            "quarante mille dollars sans élever la voix une seule fois — parce qu'elle "
            "avait lu la page quatre.",
            notes="Rappeler que Nadia nomme aussi son propre intérêt : « c'est moi qui "
                  "écoperais de ce travail ». C'est ce qui désarme le soupçon.")

    d.billet(
        "Enregistrez votre intervention de 90 secondes et déposez-la.",
        exemples=[
            "Réécoutez-vous avant d'envoyer : les trois temps y sont-ils ?",
            "Avez-vous employé au moins un conditionnel de proposition ?",
        ],
        notes="Dépôt dans le module, section « Je me lance ». La rétroaction de l'IA "
              "reste privée ; seul l'envoi arrive à l'enseignante.")

    return d.save(dossier)
