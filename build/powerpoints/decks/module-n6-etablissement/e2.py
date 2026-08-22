# -*- coding: utf-8 -*-
"""E2 · Écrire au secrétariat
Bloc E « Je me lance » · couleur framboise · 75 min. Production écrite et bilan.
Source : production écrite de custom.js et autoévaluation « Je retiens des mots ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Écrire au secrétariat",
        chapeau="Un courriel qui demande une exception reçoit un non poli. "
                "Un courriel qui annonce ce qu'on va faire et quand reçoit "
                "un « c'est noté » — et c'est ce qu'on cherche.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Prévoir trente minutes d'écriture "
                  "réelle et quinze minutes de bilan. Le reste est de la préparation.")

    d.objectifs([
        "présenter un courriel formel : appel, trois paragraphes, salutation ;",
        "dire qui l'on est et de quel dossier il s'agit dès la première ligne ;",
        "poser une question indirecte et une condition avec « si » ;",
        "terminer par un engagement daté plutôt que par une demande de faveur.",
    ], notes="Le quatrième objectif est celui qui change le ton d'un courriel et sa "
             "réponse. Il vient des attentes de fin de cours du niveau, pas de la "
             "situation : c'est écrit dans le manifeste du module.")

    d.declencheur(
        'Observation', "Avez-vous déjà écrit à une école, à un bureau ?",
        pistes=[
            "En français ? Dans une autre langue ?",
            "Avez-vous reçu une réponse ? Combien de temps après ?",
            "Qu'est-ce qui était difficile : commencer, ou finir ?",
        ],
        notes="La réponse la plus fréquente est « commencer ». Le premier paragraphe "
              "est effectivement le plus dur, et c'est exactement celui que le "
              "tableau suivant règle.")

    d.tableau('Analyse', "Trois paragraphes, trois travaux",
              ['Le paragraphe', 'Ce qu\'il contient'],
              [["Le premier", "qui vous êtes, votre numéro de dossier, de quoi vous parlez"],
               ["Le deuxième", "votre situation et votre question, précisément"],
               ["Le troisième", "ce que vous vous engagez à faire, avec une date"]],
              cle=0,
              note="Un paragraphe porte une idée principale, et une seule. Le blanc entre deux paragraphes est un changement d'idée, pas de la décoration.",
              notes="Diapositive à photographier. Rappeler C2 : la mise en page est "
                    "une information. On écrit comme on nous écrit.")

    d.tableau('Analyse', "Ce que le courriel doit contenir",
              ['L\'élément', 'Un exemple'],
              [["Une formule d'appel", "Madame, · Monsieur,"],
               ["Le numéro de dossier", "au sujet du dossier 6-24-0187"],
               ["Une question indirecte", "je voudrais savoir si la preuve peut arriver en janvier"],
               ["Une condition avec si", "si je réussis le test le 28 novembre, …"],
               ["Un subjonctif", "j'aimerais que la date soit inscrite au dossier"],
               ["Un engagement daté", "je déposerai la preuve la semaine du 12 janvier"]],
              cle=0,
              notes="Diapositive à photographier. C'est la liste exacte du module "
                    "interactif : les élèves la retrouveront cochable à l'écran.")

    d.regle("N'écrivez pas au futur d'ordre",
            "Vous n'avez pas à imiter le style de l'avis que vous avez reçu.",
            precision="« La soussignée déposera » n'est pas de votre côté de la "
                      "lettre. Écrivez simplement : « Je déposerai la preuve la "
                      "semaine où je la recevrai. » Un futur normal, et une date. "
                      "C'est plus clair, et c'est mieux reçu.",
            notes="Diapositive à photographier. Plusieurs élèves croient qu'il faut "
                  "écrire compliqué pour être pris au sérieux. C'est le contraire, et "
                  "il faut le dire explicitement.")

    d.piege('Écriture',
            "je vous demande de faire une exception pour moi",
            "je vous informe que je déposerai la preuve la semaine du 12 janvier",
            "Une demande d'exception oblige la personne à refuser : elle n'a "
            "souvent pas le pouvoir d'accorder, et elle répond non poliment. "
            "Un engagement daté, lui, ne demande rien : il informe. La réponse "
            "est alors « c'est noté » — c'est-à-dire une ligne dans votre "
            "dossier.",
            notes="C'est la leçon la plus transférable du module entier. La faire "
                  "reformuler par deux élèves avant de commencer l'écriture.")

    d.pratique('Préparation', "Votre premier paragraphe, en deux phrases",
               "Qui vous êtes, votre dossier, de quoi vous parlez.", [
        ("Phrase 1 : votre nom, votre programme, votre numéro de dossier.", ""),
        ("Phrase 2 : le document dont vous parlez et sa date.", ""),
    ],
       notes="Cinq minutes, en silence. Faire lire deux ou trois premiers "
             "paragraphes à voix haute et les améliorer ensemble : le reste du "
             "courriel suit tout seul.")

    d.tableau('Bilan', "Ce que vous savez faire maintenant",
              ['Le défi', 'Ce que vous en gardez'],
              [["Je découvre", "à qui poser quelle question, et pourquoi tout finit en papier"],
               ["Défi 1", "suivre un entretien, poser une question indirecte, ne pas perdre le fil"],
               ["Défi 2", "trouver la condition et la date d'un avis, en trois minutes"],
               ["Défi 3", "prendre sa place, poser une condition, annoncer son avis"]],
              cle=0,
              note="Quatre semaines pour une seule compétence : décider, au lieu d'attendre qu'on décide pour vous.",
              notes="Diapositive à photographier. Enchaîner sur l'autoévaluation du "
                    "module interactif, dix-huit énoncés, à faire en classe.")

    d.billet(
        "Écris ton courriel, huit à douze phrases, trois paragraphes.",
        exemples=[
            "Relis la liste des six éléments avant d'envoyer.",
            "Termine par un engagement daté, jamais par une demande de faveur.",
        ],
        notes="Trente minutes. L'assistant du module vérifie le texte avant l'envoi à "
              "l'enseignant. Les élèves qui le souhaitent peuvent envoyer leur "
              "courriel pour de vrai, à leur propre centre : plusieurs le feront.")

    return d.save(dossier)
