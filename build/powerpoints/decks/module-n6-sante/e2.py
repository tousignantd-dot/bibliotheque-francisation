# -*- coding: utf-8 -*-
"""E2 · Écrire à quelqu'un qui attend de vos nouvelles
Bloc E « Je me lance » · couleur framboise · 75 min. Production écrite et bilan.
Source : production écrite de custom.js et autoévaluation « Je retiens des mots ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Écrire à quelqu'un qui attend de vos nouvelles",
        chapeau="Une lettre personnelle, pas un courriel de bureau. Les mots "
                "du dossier servent au laboratoire ; ceux-ci servent à "
                "rassurer quelqu'un qui est loin.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Prévoir trente minutes d'écriture "
                  "réelle et quinze minutes de bilan. Commencer par cinq minutes sur "
                  "les billets de E1.")

    d.objectifs([
        "présenter une lettre personnelle : appel, trois paragraphes, salutation ;",
        "raconter un évènement dans l'ordre, avec ses repères de temps ;",
        "reprendre sans répéter et annoncer ses exemples ;",
        "terminer par ce qui arrive ensuite, avec une date.",
    ], notes="Ces objectifs viennent des attentes de fin de cours du niveau, la "
             "situation du programme n'ayant aucune intention de production écrite. "
             "C'est écrit dans le manifeste du module.")

    d.declencheur(
        'Observation', "À qui donnez-vous de vos nouvelles, et comment ?",
        pistes=[
            "Par téléphone, par message, par courriel ?",
            "Est-ce que vous racontez tout, ou est-ce que vous rassurez ?",
            "Qu'est-ce qui est le plus difficile à écrire : le début ou la fin ?",
        ],
        notes="Cinq minutes. La réponse la plus fréquente est « je rassure ». C'est "
              "précisément ce que la lettre doit faire sans mentir, et le tableau "
              "suivant montre comment.")

    d.tableau('Analyse', "Trois paragraphes, trois travaux",
              ['Le paragraphe', 'Ce qu\'il contient'],
              [["Le premier", "comment vous allez, et pourquoi vous écrivez aujourd'hui"],
               ["Le deuxième", "ce qui s'est passé, raconté dans l'ordre"],
               ["Le troisième", "ce qui arrive ensuite, et ce que vous demandez"]],
              cle=0,
              note="Un paragraphe porte une idée principale, et une seule. Le blanc entre deux est un changement d'idée.",
              notes="Diapositive à photographier. Rappeler D1 : la mise en page est "
                    "une information. On écrit comme on aimerait qu'on nous écrive.")

    d.tableau('Analyse', "Une lettre personnelle n'est pas un courriel de bureau",
              ['On écrit', 'Plutôt que'],
              [["Ma chère sœur,", "Madame,"],
               ["Je t'embrasse.", "Veuillez agréer mes salutations."],
               ["J'ai enfin vu la spécialiste.", "Je vous informe que j'ai été vue."],
               ["Je monte les escaliers moins vite.", "Réduction de la tolérance à l'effort."]],
              cle=0,
              note="Le savoir du programme est explicite : formules d'appel et de salutation d'une lettre personnelle.",
              notes="Diapositive à photographier. La quatrième ligne est celle qui "
                    "compte : plusieurs élèves seront tentés d'employer les mots du "
                    "compte rendu pour faire sérieux.")

    d.tableau('Analyse', "Ce que la lettre doit contenir",
              ['L\'élément', 'Un exemple'],
              [["Un plus-que-parfait", "mon médecin avait envoyé la demande en avril"],
               ["Un « le mois où »", "ça a commencé le mois où mon fils est parti"],
               ["Un exemple annoncé", "je monte moins bien, par exemple les douze marches"],
               ["Une reprise", "cette fatigue, ce rendez-vous, ces examens"],
               ["Une subordonnée infinitive", "elle m'a demandé de noter mes journées"]],
              cle=0,
              note="Et une date, au moins : ce qui arrive ensuite, et quand.",
              notes="Diapositive à photographier. C'est la liste exacte du module "
                    "interactif : les élèves la retrouveront cochable à l'écran.")

    d.piege('Écriture',
            "j'ai une réduction de la tolérance à l'effort",
            "je monte les escaliers moins vite qu'avant",
            "Les mots du compte rendu ne communiquent rien à quelqu'un qui "
            "n'est pas médecin. Ils ne font pas sérieux : ils font distant, et "
            "ils inquiètent davantage parce que le lecteur ne peut rien en "
            "faire. Un mot qu'on peut redire dans sa langue courante est un mot "
            "compris.",
            notes="C'est la leçon la plus transférable du module entier. La faire "
                  "reformuler par deux élèves avant de commencer l'écriture.")

    d.pratique('Préparation', "Votre premier paragraphe, en deux phrases",
               "Comment vous allez, et pourquoi vous écrivez aujourd'hui.", [
        ("Phrase 1 : comment vous allez, en évitant « ça va ».", ""),
        ("Phrase 2 : pourquoi vous écrivez aujourd'hui et pas hier.", ""),
    ],
       notes="Cinq minutes, en silence. Faire lire deux ou trois premiers "
             "paragraphes à voix haute et les améliorer ensemble : le reste de la "
             "lettre suit tout seul.")

    d.tableau('Bilan', "Ce que vous savez faire maintenant",
              ['Le défi', 'Ce que vous en gardez'],
              [["Je découvre", "ce qu'on apporte, et ce que l'hôpital n'a pas"],
               ["Défi 1", "entrer en conversation, raconter ce qui s'était passé avant"],
               ["Défi 2", "décrire un changement plutôt qu'un état, et poser ses questions"],
               ["Défi 3", "retrouver sa propre phrase sous les mots du dossier"]],
              cle=0,
              note="Quatre semaines pour une seule chose : nommer ce qu'on a, au lieu d'attendre que quelqu'un le devine.",
              notes="Diapositive à photographier. Enchaîner sur l'autoévaluation du "
                    "module interactif, dix-neuf énoncés, à faire en classe.")

    d.billet(
        "Écrivez votre lettre : huit à douze phrases, trois paragraphes.",
        exemples=[
            "Relisez la liste des éléments avant d'envoyer.",
            "Terminez par ce qui arrive ensuite, et par une date.",
        ],
        notes="Trente minutes. L'assistant du module vérifie le texte avant l'envoi à "
              "l'enseignant. Plusieurs élèves enverront leur lettre pour de vrai : "
              "c'est le meilleur usage possible de la séance, et il faut le dire.")

    return d.save(dossier)
