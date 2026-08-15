# -*- coding: utf-8 -*-
"""E1 · À toi : la clinique et le courriel.
Bloc E · couleur teal (je me lance) · 90 min.
Source : section `appli`, exercice `aFiche` (l'entorse), production orale et écrite.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='À toi : la clinique et le courriel',
        chapeau="Tout le module en une séance. Lire une fiche, décrire une douleur à "
                "voix haute, puis écrire à une clinique pour demander un rendez-vous.",
        duree='90 minutes')

    d.titre(notes="Séance d'application. Aucun contenu nouveau : c'est une séance de "
                  "production. Prévoir un tiers de lecture, un tiers d'oral, un tiers "
                  "d'écrit, et tenir l'horaire.")

    d.objectifs([
        "lire une fiche-conseil qu'on n'a jamais vue et en tirer les gestes à faire ;",
        "décrire une douleur à voix haute, sans notes, en trente secondes ;",
        "écrire un courriel de demande de rendez-vous ;",
        "employer les formules d'ouverture et de clôture d'un courriel.",
    ])

    # ── premier temps · la lecture ─────────────────────────────────
    d.tableau('Lire', "La fiche-conseil sur l'entorse à la cheville",
              ['La rubrique', 'Ce qu\'elle dit'],
              [["Ce que c'est", "les ligaments de la cheville sont étirés"],
               ["Les premiers gestes", "repos, glace, compression, élever la jambe"],
               ["À éviter", "la chaleur, les massages, la marche prolongée"],
               ["Quand consulter", "si on ne peut pas mettre de poids sur le pied"]],
              cle=0,
              note="Ce sont les mêmes rubriques que la fiche sur la tendinite, en D1. "
                   "Un contenu nouveau dans une structure connue.",
              notes="Ne pas expliquer la fiche avant l'exercice : c'est une lecture "
                    "autonome. Laisser cinq minutes de lecture silencieuse.")

    d.pratique('Pratique · 1 de 4', "Vrai ou faux — l'entorse",
               "D'après la fiche que vous venez de lire.", [
        ("Une entorse touche les ligaments.", "VRAI"),
        ("Il faut appliquer de la chaleur le premier jour.", "FAUX — de la glace"),
        ("Élever la jambe fait partie des premiers gestes.", "VRAI"),
        ("On peut masser la cheville dès le premier jour.", "FAUX — à éviter"),
        ("Il faut consulter si on ne peut pas mettre de poids sur le pied.", "VRAI"),
    ], corrige=True,
       notes="Corriger vite, en renvoyant chaque fois à la rubrique de la fiche. "
             "L'important n'est pas la réponse mais l'endroit où on l'a trouvée.")

    # ── deuxième temps · la production orale ───────────────────────
    d.regle("À l'oral · la phrase de trente secondes",
            "L'endroit avec le côté · depuis quand · ce qui aggrave · le chiffre sur dix.",
            precision="C'est la structure travaillée en B4. Elle ne change pas, quelle "
                      "que soit la douleur ni la personne à qui on parle : infirmière, "
                      "médecin, pharmacienne, ou le 811 au téléphone.",
            notes="Écrire les quatre éléments au tableau avant de lancer l'exercice oral. "
                  "Les élèves les regarderont ; c'est voulu.")

    d.pratique('Pratique · 2 de 4', "À deux · l'appel au 811",
               "L'un est l'infirmière d'Info-Santé, l'autre appelle. Puis on échange.", [
        ("L'infirmière ouvre", "Info-Santé, bonjour. Qu'est-ce que je peux faire pour vous ?"),
        ("Vous décrivez", "les quatre éléments, en trente secondes"),
        ("L'infirmière questionne", "Est-ce que vous pouvez mettre du poids dessus ?"),
        ("L'infirmière conclut", "Allez à la clinique sans rendez-vous demain matin."),
    ], corrige=False,
       notes="Dix minutes par personne. Circuler avec une feuille et noter les quatre "
             "éléments manquants les plus fréquents. Ne corriger personne pendant le jeu.")

    d.cartes('Écrire', "Le courriel de demande de rendez-vous", [
        ("L'objet",
         "Court et précis : « Demande de rendez-vous — douleur au genou ». La personne "
         "qui trie les courriels décide avec l'objet seul."),
        ("L'ouverture",
         "« Bonjour, » suivi d'une virgule et d'un retour à la ligne. Jamais « Salut », "
         "jamais rien du tout."),
        ("Le corps",
         "Trois phrases : qui vous êtes, ce que vous avez, ce que vous demandez. C'est "
         "la phrase de trente secondes, mise par écrit."),
        ("La clôture",
         "« Merci de votre réponse. » puis votre nom complet et votre numéro de "
         "téléphone. Sans le numéro, personne ne peut vous rappeler."),
    ], notes="Faire remarquer que le corps du courriel est exactement la production orale "
             "de B4. Rien de nouveau n'est demandé : seule la forme change.")

    d.tableau('Analyse', "Les formules à connaître",
              ['Pour', 'On écrit'],
              [["ouvrir", "Bonjour,"],
               ["se présenter", "Je m'appelle… et je suis patient chez vous."],
               ["demander", "J'aimerais obtenir un rendez-vous."],
               ["remercier", "Merci de votre réponse."],
               ["signer", "votre nom complet et votre numéro"]],
              cle=1,
              note="Cinq formules qui servent pour tout courriel officiel, pas seulement "
                   "en santé.",
              notes="Les faire copier dans le cahier. Elles réapparaissent au module 3, "
                    "où l'on écrit à un employeur.")

    d.pratique('Pratique · 3 de 4', "Écrivez le courriel",
               "Cinq à huit lignes. Objet, ouverture, corps, clôture, signature.", [
        ("La situation",
         "Vous avez la cheville droite enflée depuis deux jours et vous ne pouvez pas "
         "marcher normalement."),
        ("Ce que vous demandez",
         "Un rendez-vous à la clinique cette semaine, de préférence le matin."),
        ("À ne pas oublier",
         "Votre nom complet, votre numéro de téléphone, et depuis quand ça dure."),
    ], corrige=False,
       notes="Vingt minutes d'écriture individuelle. Circuler et aider sur la forme, pas "
             "sur le contenu. Ramasser les copies : elles sont l'évaluation du module.")

    d.piege('Le piège du courriel trop court',
            "Bonjour, j'ai mal. Merci.",
            "Bonjour, je m'appelle… J'ai la cheville droite enflée depuis deux jours…",
            "Un courriel sans nom, sans numéro et sans description oblige la clinique à "
            "rappeler pour tout demander — ou à ne pas répondre du tout. Les trois "
            "phrases du corps ne sont pas de la politesse : ce sont les informations "
            "sans lesquelles on ne peut pas vous donner de rendez-vous.",
            notes="Montrer les deux versions côte à côte. Demander laquelle obtiendrait "
                  "une réponse le jour même.")

    d.pratique('Pratique · 4 de 4', "Relisez avant d'envoyer",
               "Cinq vérifications, dans l'ordre.", [
        ("L'objet dit-il de quoi il s'agit ?", "Demande de rendez-vous — douleur au genou"),
        ("Ai-je écrit mon nom complet ?", "prénom et nom de famille"),
        ("Ai-je donné mon numéro de téléphone ?", "avec l'indicatif régional"),
        ("Ai-je dit depuis quand ça dure ?", "une date ou un nombre de jours"),
        ("Les verbes sont-ils au bon temps ?", "présent pour l'état, passé pour l'accident"),
    ], corrige=True,
       notes="Faire faire cette relecture par le voisin, pas par l'auteur. Une relecture "
             "croisée trouve deux fois plus d'oublis.")

    d.billet(
        "En une phrase : qu'est-ce que vous savez faire aujourd'hui que vous ne saviez pas faire au début du module ?",
        exemples=[
            "Pensez à la première séance : « Où iriez-vous avec un genou enflé ? »",
            "Une seule phrase, honnête. Elle n'est pas notée.",
        ],
        notes="Lire quelques billets à voix haute, sans nommer les auteurs. C'est la "
              "meilleure préparation à la séance de bilan qui suit.")

    return d.save(dossier)
