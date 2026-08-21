# -*- coding: utf-8 -*-
"""E2 · La demande écrite, et le bilan.
Bloc E « Je me lance » · couleur framboise · 60 min. Dernière séance.
Source : la production écrite du module, `FC_CARDS`, autoévaluation.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="La demande écrite, et le bilan",
        chapeau="Seize mots, quatre familles, et une dernière production : "
                "demander un congé de formation en arrivant avec le problème "
                "réglé plutôt qu'avec un souhait.",
        duree='60 minutes')

    d.titre(notes="Dernière séance du module. Elle consolide et elle produit ; aucun mot "
                  "neuf, aucun point de grammaire neuf.")

    d.objectifs([
        "revoir les seize mots du module par famille ;",
        "écrire une demande de congé de formation chiffrée ;",
        "réemployer le subjonctif et l'hypothèse au passé dans un texte utile ;",
        "évaluer honnêtement ce qu'on est maintenant capable de faire.",
    ])

    d.vocabulaire('Famille 1', "Le poste et les tâches",
                  [("une description de tâches", "Le document qui énumère tout ce qu'on doit faire."),
                   ("un supérieur immédiat", "La personne à qui on rend des comptes directement."),
                   ("faire le suivi", "Reprendre un dossier commencé pour le faire avancer."),
                   ("un imprévu", "Ce qui arrive sans avoir été planifié.")],
                  notes="Retour à A4, quatre semaines plus tard. Faire employer chaque "
                        "mot dans une phrase sur son propre travail.")

    d.vocabulaire('Famille 2', "La paie et la réclamation",
                  [("un relevé de paie", "Le document qui détaille les heures, le taux et les retenues."),
                   ("les heures supplémentaires", "Les heures travaillées au-delà de la semaine normale."),
                   ("une réclamation", "La démarche pour faire corriger une somme due."),
                   ("un accusé de réception", "Le message qui confirme qu'un document a été reçu.")],
                  notes="Demander au groupe le seuil et la majoration. La réponse doit "
                        "venir sans hésitation : quarante heures, cinquante pour cent.")

    d.vocabulaire('Famille 3', "La réunion",
                  [("un ordre du jour", "La liste des points traités pendant une réunion."),
                   ("un compte rendu", "Le texte qui rapporte les décisions, les responsables et les dates."),
                   ("un compromis", "La solution que deux parties acceptent quand aucune n'obtient tout."),
                   ("une échéance", "La date limite à laquelle une chose doit être faite.")],
                  notes="Faire redire la formule d'une ligne de compte rendu : quoi, qui, "
                        "quand.")

    d.vocabulaire('Famille 4', "La formation",
                  [("le perfectionnement", "Améliorer des compétences qu'on possède déjà."),
                   ("une attestation", "Le document officiel qui prouve une formation réussie."),
                   ("un congé de formation", "Le temps libéré par l'employeur pour suivre un cours."),
                   ("la reconnaissance des acquis", "La démarche qui fait créditer ce qu'on sait déjà faire.")],
                  notes="Rappeler où s'adresser pour la reconnaissance des acquis : le "
                        "centre de services scolaire.")

    d.tableau('Production écrite', "Ce que la demande doit contenir",
              ['L\'élément', 'Pourquoi'],
              [["Un objet qui se lit seul", "la décision se prend souvent à l'objet"],
               ["Le nom exact de la formation et sa durée", "sans cela, la demande n'est pas traitable"],
               ["Un chiffre : ce que la lacune coûte", "c'est l'argument, pas l'envie d'apprendre"],
               ["Comment le travail se fait pendant l'absence", "c'est la seule vraie objection de l'employeur"]],
              cle=0,
              note="Une hypothèse au passé, une phrase au subjonctif, une demande unique, une date de réponse.",
              notes="Diapositive à photographier. C'est la grille de correction du "
                    "travail remis.")

    d.regle("La phrase à placer",
            "Si j'avais su utiliser ce module l'an dernier, j'aurais économisé quarante heures.",
            precision="Elle fait tout le travail à elle seule : elle nomme la lacune, "
                      "elle la chiffre, et elle montre que vous avez réfléchi avant "
                      "d'écrire. Sans elle, la demande dit « j'aimerais » ; avec elle, "
                      "elle dit « voici ce que ça vous rapporte ».",
            notes="Diapositive à photographier. Chacun adapte la phrase à son propre "
                  "travail avant de rédiger.")

    d.pratique('Bilan', "Qu'est-ce que je suis capable de faire ?",
               "Répondez honnêtement : pas encore, un peu, ou oui.", [
        ("Je comprends une description de tâches détaillée.", ""),
        ("Je découpe une phrase longue en groupes de souffle.", ""),
        ("Je distingue le registre du corridor de celui d'un courriel.", ""),
        ("Je peux exposer un problème de paie avec ses dates et ses chiffres.", ""),
        ("Je connais le seuil de 40 heures et la majoration de 50 %.", ""),
        ("Je nomme un écart à la voix passive, sans accuser personne.", ""),
        ("Je résume les propos d'un collègue avant de donner mon avis.", ""),
        ("Je rédige un compte rendu : décision, responsable, échéance.", ""),
    ], notes="Reprendre l'autoévaluation du module, section « Je retiens des mots ». "
             "Faire nommer à chacun le point qu'il travaillera encore.")

    d.billet(
        "Écrivez votre demande de congé de formation et déposez-la.",
        exemples=[
            "De huit à douze phrases, un objet qui se lit seul.",
            "Un chiffre, une hypothèse au passé, une date de réponse.",
        ],
        notes="Troisième et dernière production écrite du module. Elle se dépose dans "
              "la section « Je me lance ».")

    return d.save(dossier)
