# -*- coding: utf-8 -*-
"""A1 · Trois minutes au comptoir
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `prVF`, cinq premiers mots de FC_CARDS.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Trois minutes au comptoir",
        chapeau="Leyla a attendu sept mois ce rendez-vous. En trois minutes, "
                "l'agente de l'accueil lui apprend ce que sept mois "
                "d'attente ne lui avaient pas appris.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : "
                  "qui a déjà attendu un rendez-vous avec un spécialiste, et combien "
                  "de temps ? Les chiffres qui sortiront seront élevés, et personne "
                  "n'aura besoin qu'on dramatise.")

    d.objectifs([
        "nommer les lieux et les papiers d'un rendez-vous en spécialité ;",
        "comprendre ce qu'une demande de consultation déclenche ;",
        "savoir ce qu'il faut avoir apporté, et ce que l'hôpital n'a pas ;",
        "employer les cinq premiers mots du dossier avec leur article.",
    ], notes="Le troisième objectif est le plus utile tout de suite : plusieurs "
             "élèves ont déjà perdu un rendez-vous faute d'un papier resté à la "
             "maison.")

    d.declencheur(
        'Observation', "Qu'est-ce que vous apportez à un rendez-vous médical ?",
        pistes=[
            "Votre carte, et quoi d'autre ?",
            "Est-ce qu'on vous a déjà demandé un papier que vous n'aviez pas ?",
            "Est-ce que vous notez quelque chose pendant le rendez-vous ?",
            "Combien de temps avez-vous attendu, la dernière fois ?",
        ],
        notes="Question sans mauvaise réponse. Noter au tableau ce que le groupe "
              "nomme : la liste sera presque toujours réduite à la carte, et c'est "
              "ce manque qui rend le tableau d'analyse utile tout à l'heure.")

    d.dialogue('Dialogue · 1 de 3', "Vous êtes à la bonne place", [
        ("LEYLA", "Bonjour. J'ai un rendez-vous à neuf heures quarante. Demirci, Leyla.", True),
        ("MARIETTE", "Bonjour. Votre carte d'assurance maladie, s'il vous plaît. Vous venez pour la médecine interne ?", True),
        ("LEYLA", "Je pense. C'est écrit sur le papier, mais je ne sais pas lequel des deux mots est le nom du docteur.", True),
        ("MARIETTE", "Montrez-moi. Charest, Sylvine. Sylvine, c'est son prénom ; Charest, c'est son nom de famille.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="S'arrêter sur la confusion du prénom et du nom : elle est très "
             "fréquente, et elle est la première chose qu'un adulte ose rarement "
             "demander. Faire lire trois convocations imaginaires au tableau.")

    d.dialogue('Dialogue · 2 de 3', "Notez-les quand même", [
        ("MARIETTE", "Votre médecin de famille avait envoyé une demande de consultation, c'est ça ?", True),
        ("LEYLA", "Oui. En avril. Elle m'avait dit d'attendre l'appel et de ne pas rappeler avant l'automne.", True),
        ("MARIETTE", "Vous avez apporté la liste de vos médicaments ?", True),
        ("LEYLA", "Je n'en prends pas. À part des vitamines, l'hiver.", True),
    ], notes="Poser la question au groupe avant d'écouter la suite : est-ce que les "
             "vitamines comptent ? La plupart répondront non. La réponse est oui, et "
             "c'est la découverte la plus utile de la séance.")

    d.dialogue('Dialogue · 3 de 3', "Ouvrez-la ici, pas chez vous", [
        ("MARIETTE", "Tout ce qui se prend compte, même ce qui s'achète sans papier.", True),
        ("LEYLA", "Et les prises de sang que j'ai faites au mois de mars, est-ce qu'elle les a ?", True),
        ("MARIETTE", "Si elles ont été faites ici, oui. Si c'est un laboratoire privé, apportez le papier.", True),
        ("MARIETTE", "Et quand vous sortirez de son bureau, on vous remettra une enveloppe. Ouvrez-la ici, pas chez vous.", True),
    ], notes="Écrire au tableau : « Ouvrez-la ici, pas chez vous. » et la laisser "
             "toute la session. Annoncer le Défi 3 : dans trois semaines, on ouvrira "
             "cette enveloppe ensemble.")

    d.tableau('Analyse', "Quatre personnes, quatre pouvoirs",
              ['La personne', 'Ce qu\'elle peut faire pour vous'],
              [["À l'accueil", "inscrire, expliquer où aller, dire combien de temps ça dure"],
               ["Le médecin de famille", "envoyer la demande, décider d'un arrêt de travail ensuite"],
               ["La spécialiste", "chercher la cause, demander des examens, écrire au médecin"],
               ["La liaison", "traduire ce qui est écrit et répondre au téléphone"]],
              cle=0,
              note="Aucune ne peut faire le travail d'une autre. Poser sa question au mauvais endroit fait perdre une semaine.",
              notes="Diapositive à photographier. C'est le tableau de référence du "
                    "module ; il revient à chaque ouverture de bloc.")

    d.regle("Ce qui a été fait ailleurs n'est pas au dossier",
            "L'hôpital ne voit que ce qui a été fait chez lui.",
            precision="Un laboratoire privé, une clinique d'une autre ville, un "
                      "examen d'un autre pays : ces papiers voyagent avec vous ou "
                      "n'existent pas. C'est l'oubli le plus fréquent, et il coûte "
                      "un rendez-vous attendu des mois.",
            notes="Diapositive à photographier. Donner la phrase à réutiliser : "
                  "« Est-ce que vous avez déjà mes résultats de mars ? » Elle est "
                  "polie, normale, et elle règle la question en dix secondes.")

    d.vocabulaire('Vocabulaire', "Les cinq premiers mots, avec leur article", [
        ("une clinique externe", "Le service d'un hôpital où l'on est reçu à une heure donnée, sans y être hospitalisé."),
        ("une demande de consultation", "Le papier par lequel un médecin en fait voir un autre à la même personne."),
        ("la médecine interne", "La spécialité de ceux qui cherchent la cause d'un problème qui touche tout le corps."),
        ("un délai d'attente", "Le temps qui sépare la demande du rendez-vous, et sur lequel l'accueil n'a aucun pouvoir."),
        ("un dossier médical", "Tout ce qui a été écrit sur vous par ceux qui vous ont vu, et qui vous suit."),
    ], notes="Faire répéter chaque mot avec son article. « Une demande de "
             "consultation » est long : le découper en trois temps et le faire dire "
             "deux fois. C'est le mot qui explique les sept mois d'attente.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la conversation de Leyla et de Mariette.", [
        ("Le rendez-vous de Leyla est à neuf heures quarante.", "vrai"),
        ("Sylvine est le nom de famille de la médecin.", "faux - c'est son prénom"),
        ("La demande de consultation a été envoyée en avril.", "vrai"),
        ("Un délai de sept mois est exceptionnel.", "faux - ce n'est pas rare"),
        ("Il faut noter les vitamines même sans ordonnance.", "vrai"),
        ("Les résultats d'un laboratoire privé sont au dossier.", "faux - il faut les apporter"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le dernier "
             "surprend le plus : beaucoup d'élèves croient que tout se retrouve "
             "automatiquement dans un système informatique.")

    d.billet(
        "Quelle question voudriez-vous poser, et à qui la poseriez-vous ?",
        exemples=[
            "Une phrase suffit, et elle peut commencer par « je me demande ».",
            "Nommez la personne : l'accueil, votre médecin, la spécialiste.",
        ],
        notes="Deux minutes. Ramasser les billets : ils donnent la matière du jeu de "
              "rôle de E1, et ils disent quelles questions le groupe n'ose pas poser.")

    return d.save(dossier)
