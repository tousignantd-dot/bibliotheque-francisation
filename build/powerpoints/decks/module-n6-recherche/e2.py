# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots.
Bloc E « Je me lance » · couleur framboise · 60 min. Dernière séance.
Source : le banc de vocabulaire du module, autoévaluation.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre='Je retiens des mots',
        chapeau="Dix-sept mots, quatre familles : le poste, l'offre, la "
                "demande, l'entrevue. Et une question à se poser honnêtement — "
                "qu'est-ce que je suis maintenant capable de faire ?",
        duree='60 minutes')

    d.titre(notes="Dernière séance du module. Elle sert à consolider, pas à ajouter. "
                  "Aucun mot neuf ici.")

    d.objectifs([
        "revoir les mots du module par famille ;",
        "employer chaque mot dans une phrase à soi ;",
        "évaluer honnêtement ce qu'on sait faire ;",
        "nommer la prochaine étape de sa propre recherche.",
    ])

    d.vocabulaire('Famille 1', "Le poste et le secteur",
                  [("un poste", "L'emploi précis qu'une personne occupe, avec son titre."),
                   ("un secteur d'activité", "Le grand domaine : la construction, la santé, la logistique."),
                   ("un curriculum vitæ", "Le document qui résume la formation et l'expérience."),
                   ("le temps partiel", "Un horaire de moins de trente heures par semaine."),
                   ("un ordre professionnel", "L'organisme qui donne le droit d'exercer certains métiers.")],
                  notes="Faire dire à chacun son poste et son secteur, à voix haute. "
                        "C'est le retour à la séance A1, cinq semaines plus tard.")

    d.vocabulaire('Famille 2', "Lire l'offre",
                  [("une offre d'emploi", "L'annonce par laquelle une entreprise cherche quelqu'un."),
                   ("une tâche", "Ce qu'on doit faire dans son travail, jour après jour."),
                   ("une exigence", "Ce que l'employeur demande absolument."),
                   ("un atout", "Une compétence en plus, souhaitée mais pas obligatoire."),
                   ("un poste permanent", "Un emploi sans date de fin prévue.")],
                  notes="Redemander la différence entre exigence et atout. C'est le point "
                        "du module qui change le plus de comportements.")

    d.vocabulaire('Famille 3', "Écrire la demande",
                  [("une demande d'emploi", "Le formulaire détaillé qu'on remplit pour se présenter."),
                   ("une lettre de motivation", "La courte lettre qui accompagne le CV."),
                   ("une référence", "Une personne qui parlera de votre travail à un employeur."),
                   ("les disponibilités", "Les jours et les heures où on peut travailler.")],
                  notes="Demander qui a déjà choisi ses deux références. Beaucoup n'y "
                        "pensent qu'au moment de remplir le formulaire, et c'est trop tard.")

    d.vocabulaire('Famille 4', "Passer l'entrevue",
                  [("une entrevue", "La rencontre où l'employeur pose des questions."),
                   ("une compétence", "Ce qu'une personne sait faire, par la formation ou l'expérience."),
                   ("l'assurance collective", "La protection de santé offerte par l'employeur.")],
                  notes="« Assurance collective » est le mot que les élèves entendent en "
                        "entrevue sans oser demander ce qu'il veut dire.")

    d.tableau('Bilan', "Les quatre points de langue du module",
              ['Le point', 'La phrase qui le porte'],
              [["Les mots en -able", "Mon expérience est transférable."],
               ["Le relatif « où »", "C'est l'entreprise où j'ai appris le métier."],
               ["L'infinitif passé", "Après avoir vérifié les commandes, je préparais les bons."],
               ["Le subjonctif", "J'aimerais que vous sachiez que j'ai six ans d'expérience."]],
              cle=0,
              note="Quatre phrases. Apprises, elles portent la moitié d'une entrevue.",
              notes="Diapositive à photographier. Faire recopier les quatre phrases avec "
                    "le métier de chacun à la place de celui de Marisol.")

    d.pratique('Autoévaluation', "Qu'est-ce que je suis capable de faire ?",
               "Pour chaque énoncé : pas encore, un peu, ou oui.", [
        ("Je repère les quatre parties d'une offre d'emploi.", ""),
        ("Je fais la différence entre une exigence et un atout.", ""),
        ("Je décris mes tâches avec des verbes d'action et des chiffres.", ""),
        ("Je connais les formules d'une lettre de motivation.", ""),
        ("Je développe une réponse d'entrevue avec un exemple.", ""),
        ("Je pose au moins une question à l'employeur.", ""),
    ], cols=1,
       notes="L'autoévaluation complète est dans l'activité interactive, avec dix "
             "énoncés. Celle-ci en projette six pour lancer la discussion.")

    d.billet(
        "Nommez votre prochaine étape.",
        exemples=[
            "Une offre à laquelle postuler cette semaine ?",
            "Un curriculum vitæ à refaire ? Deux références à demander ?",
        ],
        notes="Terminer là-dessus. Le module ne vaut que s'il débouche sur une action "
              "réelle, et beaucoup ont besoin qu'on la leur fasse écrire.")

    return d.save(dossier)
