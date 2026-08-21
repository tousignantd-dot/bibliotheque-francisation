# -*- coding: utf-8 -*-
"""A1 · « Ça fait trois mois. »
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-rendezvous/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="« Ça fait trois mois. »",
        chapeau="Rachid a cinquante-deux ans et la tête lui tourne le matin "
                "depuis le mois de mars. Il appelle ça « rien ». Sa fille, "
                "elle, compte les mois — et c'est elle qui a raison.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : combien "
                  "de temps attendez-vous avant d'aller voir un médecin ? Les réponses "
                  "vont de « tout de suite » à « jamais », et l'écart dit à lui seul ce "
                  "que le module va travailler. Ne juger aucune réponse.")

    d.objectifs([
        "dire depuis combien de temps un problème de santé dure ;",
        "distinguer le médecin de famille, le sans-rendez-vous, le 8-1-1 et l'urgence ;",
        "savoir ce qu'est un GMF et ce qu'on y trouve ;",
        "préparer ce qu'il faut avoir sous la main avant de téléphoner.",
    ])

    d.declencheur(
        'Observation', "Cette personne se tient au mur en se levant. Depuis trois mois. "
                       "Qu'est-ce qu'elle devrait faire ?",
        image=IMG + 'salle-attente.jpg',
        pistes=[
            "Est-ce que c'est grave ? Qui peut le dire ?",
            "Où va-t-on avec un problème qui dure ?",
            "Combien de temps peut-on attendre ?",
            "Qu'est-ce qui empêche d'appeler ?",
        ],
        notes="La dernière piste est la vraie : ce n'est presque jamais l'ignorance qui "
              "retient, c'est la langue au téléphone. Le dire au groupe — c'est "
              "exactement ce que le module va enlever comme obstacle.")

    d.dialogue('Dialogue · 1 de 3', "Trois mois, et il appelle ça « rien »", [
        ("NADIA", "Papa, tu t'es tenu au comptoir en te levant, tantôt. Je t'ai vu.", True),
        ("RACHID", "C'est rien. Je me lève trop vite, c'est tout.", True),
        ("NADIA", "Ça fait combien de temps que ça t'arrive ?", True),
        ("RACHID", "Je ne sais pas. Depuis le mois de mars, peut-être. Ça passe en "
                   "dix secondes.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer les deux façons de dire la durée dans quatre répliques : "
             "« ça fait combien de temps que » et « depuis le mois de mars ». Elles "
             "reviendront toute la séance.")

    d.dialogue('Dialogue · 2 de 3', "Ce n'est pas à toi de décider", [
        ("NADIA", "Mars, on est en juin. Ça fait trois mois, papa.", True),
        ("RACHID", "Trois mois, et je travaille tous les jours. Ce n'est pas une "
                   "maladie, ça.", True),
        ("NADIA", "Ce n'est pas à toi de décider. Tu as un médecin de famille, "
                  "sers-t'en.", True),
        ("RACHID", "La docteure Fongang, oui. Mais prendre un rendez-vous, c'est "
                   "deux heures au téléphone.", True),
    ], notes="« Ce n'est pas à toi de décider » est la phrase pivot du module. Un problème "
             "qui dure ne s'évalue pas soi-même. Demander au groupe s'il est d'accord.")

    d.dialogue('Dialogue · 3 de 3', "Ce qu'il faut avoir à côté du téléphone", [
        ("NADIA", "Que tu as des étourdissements le matin depuis trois mois, et que "
                  "tu es fatigué. Deux phrases, pas plus. Garde ta carte "
                  "d'assurance maladie à côté de toi.", True),
        ("RACHID", "Pourquoi la carte ?", True),
        ("NADIA", "Ils demandent toujours le numéro. Et vérifie la date : si elle "
                  "est expirée, tu vas payer.", True),
        ("RACHID", "Elle est bonne jusqu'en février. J'appelle demain matin, alors.", False),
    ], notes="« Deux phrases, pas plus » surprend toujours : les élèves croient devoir "
             "tout raconter au téléphone. Ce sera le point du défi 1.")

    d.regle("Un problème qui dure demande son propre médecin",
            "Le sans-rendez-vous répare ce qui vient d'arriver ; le médecin de "
            "famille suit ce qui revient.",
            precision="Au sans-rendez-vous, la personne qui vous reçoit ne connaît pas "
                      "votre dossier et vous voit une seule fois. Pour trois mois de "
                      "symptômes qui changent, il faut quelqu'un qui puisse comparer avec "
                      "l'année dernière — et c'est votre médecin de famille.",
            notes="Diapositive à photographier. C'est la décision la plus utile de tout le "
                  "module, et beaucoup d'élèves ne l'ont jamais entendue formulée.")

    d.cartes("Quatre portes", "Laquelle pousser, et quand", [
        ("Son médecin de famille",
         "Ce qui dure, ce qui revient, ce qui demande un suivi dans le temps."),
        ("Le sans-rendez-vous",
         "Le jour même, sans réserver — mais pas forcément avec son médecin."),
        ("Info-Santé, au 8-1-1",
         "Une infirmière au téléphone, jour et nuit, gratuitement. Elle oriente."),
        ("L'urgence, au 9-1-1",
         "Ce qui menace tout de suite : la poitrine, la respiration, une perte de connaissance."),
    ], notes="Insister sur la troisième : beaucoup d'élèves ignorent le 8-1-1, qui est "
             "pourtant le bon premier appel quand on hésite entre les trois autres.")

    d.tableau('Où appeler ?', "Cinq situations, une décision",
              ['La situation', 'Où appeler'],
              [["Des étourdissements depuis trois mois", "son médecin de famille"],
               ["Une coupure au doigt, hier soir", "le sans-rendez-vous"],
               ["Une fièvre chez un enfant, la nuit", "le 8-1-1"],
               ["Une douleur à la poitrine, maintenant", "le 9-1-1"],
               ["Je ne sais pas si c'est grave", "le 8-1-1"]],
              cle=0,
              notes="Faire ajouter deux situations par le groupe et les faire classer. "
                    "C'est là que sortent les vraies hésitations.")

    d.piege("Décider soi-même que ce n'est pas grave",
            "Je travaille tous les jours, donc ce n'est pas une maladie.",
            "Ça dure depuis trois mois, donc j'en parle à quelqu'un.",
            "Tenir debout n'est pas un diagnostic. Ce qui décide, ce n'est pas si l'on "
            "peut continuer, c'est depuis quand ça dure et si ça change.",
            notes="Rachid dit cette phrase mot pour mot dans le dialogue. La faire "
                  "retrouver, puis demander qui l'a déjà dite lui-même.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Rachid a des étourdissements depuis le mois de mars.", "vrai"),
        ("Rachid trouve tout de suite que c'est grave.", "faux — il dit « c'est rien »"),
        ("Dans un GMF, plusieurs médecins travaillent ensemble.", "vrai"),
        ("Au sans-rendez-vous, on voit son propre médecin.", "faux — pas forcément"),
        ("Nadia conseille de tout raconter au téléphone.", "faux — deux phrases, pas plus"),
        ("Une carte d'assurance maladie expirée peut coûter cher.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte du dialogue.")

    d.billet(
        "Écrivez en une phrase depuis quand dure quelque chose chez vous.",
        exemples=[
            "Un mal de dos, une fatigue, un bruit dans l'oreille — ou quelque chose de banal.",
            "Employez « depuis » ou « ça fait… que ». Une phrase, pas plus.",
        ],
        notes="Personne n'est obligé d'écrire quelque chose de personnel : un mal de dos "
              "inventé fait le même travail de langue. Le dire avant de distribuer.")

    return d.save(dossier)
