# -*- coding: utf-8 -*-
"""E2 · La demande de révision
Bloc E « Je me lance » · couleur framboise · 75 min.
Production écrite et bilan. Source du module : l'exercice `t2lettre` (type
texte) et la production écrite de « Je me lance ».

La situation du programme n'a **aucune intention de production écrite** : elle
est purement orale. Cette lettre vient des attentes de fin de cours du
niveau 8, qui demandent que l'adulte « rédige des lettres ou des courriels
d'affaires ayant des objectifs particuliers » et « négocie la solution d'un
problème, propose des compromis et donne son opinion en la justifiant à l'aide
d'arguments ». C'est écrit ici pour qu'un relecteur ne retire pas la tâche.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="La demande de révision",
        chapeau="Sept fonctions, dans cet ordre. Et un seul point contesté "
                "par lettre — c'est la contrainte la plus utile et la plus "
                "difficile à tenir.",
        duree='75 minutes')

    d.titre(notes="Dernière séance. Les élèves ont lu le modèle à l'exercice 6 "
                  "du défi 2 ; ils écrivent maintenant le leur. Prévoir "
                  "quarante minutes d'écriture réelle, montre en main.")

    d.objectifs([
        "écrire une demande de révision en sept fonctions ordonnées ;",
        "n'y contester qu'un seul point ;",
        "citer deux pièces datées et numérotées ;",
        "terminer par un chiffre, une contrepartie et une demande écrite.",
    ], notes="Le deuxième objectif sera le plus transgressé. Le répéter avant "
             "de lâcher la classe sur le clavier.")

    d.declencheur(
        'Pour commencer', "Vous avez trois désaccords. Combien en mettez-vous "
                          "dans une lettre ?",
        pistes=[
            "Trois, pour ne rien oublier ?",
            "Que fait un lecteur pressé devant trois contestations ?",
            "Lequel des trois choisiriez-vous : le plus grave, ou le mieux appuyé ?",
        ],
        notes="Réponse : un seul, et c'est le mieux appuyé, pas le plus "
              "fâchant. Ce ne sont presque jamais les mêmes, et c'est la "
              "difficulté de l'exercice.")

    d.tableau('Analyse', "Les cinq premières fonctions",
              ['La fonction', 'Comment on l\'écrit'],
              [["1. Identifier", "Objet : demande de révision — dossier 8-4-1-7-2-6"],
               ["2. Accepter", "Je vous confirme d'abord mon accord sur…"],
               ["3. Contester", "Je conteste en revanche le troisième élément…"],
               ["4. Concéder, retourner", "Certes, la clause existe… Or elle exclut…"],
               ["5. Appuyer", "…l'inventaire de huit heures (pièce 1)…"]],
              cle=0,
              note="Les deux dernières — proposer et clore — sont sur la diapositive suivante.",
              notes="Diapositive à photographier. Cinq lignes seulement : le "
                    "garde-fou du gabarit refuse un tableau plus long avec "
                    "une note, et sept fonctions ne se lisent pas de loin.")

    d.cartes('Analyse', "Les deux dernières fonctions", [
        ("6. Proposer", "Je propose en conséquence un règlement de huit cent cinquante dollars…"),
        ("La contrepartie", "…contre ma renonciation à toute autre réclamation dans ce dossier."),
        ("7. Clore", "Je vous saurais gré de me communiquer votre décision par écrit, en indiquant la clause."),
        ("La formule", "Veuillez agréer, Madame, l'expression de mes salutations distinguées."),
    ], cols=2,
       notes="Faire remarquer que la contrepartie ne coûte rien : on renonce "
             "à des réclamations qu'on n'a plus. C'est ce qui transforme une "
             "demande en échange.")

    d.regle("Ce que vous acceptez vient en premier",
            "Le lecteur voit en dix secondes qu'il n'a pas affaire à un refus de principe — et il lit la suite autrement.",
            precision="Le même mécanisme qu'au téléphone, et il fonctionne "
                      "encore mieux à l'écrit, parce que rien ne vient "
                      "adoucir un texte hostile.",
            notes="Diapositive à photographier. C'est la règle du module, "
                  "posée en A3, jouée en C1, écrite ici. Troisième et "
                  "dernière rencontre.")

    d.piege('Attention',
            "un ton indigné, même une seule phrase",
            "les faits, une concession, et un chiffre",
            "L'indignation est légitime et elle ne se transmet pas par écrit : "
            "elle se lit comme du bruit, et elle donne une raison de refuser "
            "sans examiner. Relisez votre lettre en cherchant les adjectifs — "
            "« inacceptable », « scandaleux », « ridicule » — et remplacez "
            "chacun par une date ou un montant.",
            notes="Excellent exercice de relecture, et rapide : faire "
                  "surligner les adjectifs avant de rendre. Il y en a "
                  "presque toujours deux ou trois.")

    d.pratique('Pratique', "Bilan du module — qu'est-ce que je sais faire ?",
               "Cochez ce que vous êtes maintenant capable de faire seul.", [
        ("Poser les trois gestes du premier jour", "copie signée, photos datées, rien d'accepté de vive voix"),
        ("Calculer ce que je toucherai", "dommage retenu, moins la franchise, une fois par sinistre"),
        ("Exiger la clause exacte d'un refus", "et la faire relire mot pour mot"),
        ("Concéder d'abord ce qui est juste", "à voix haute, avant de contester le reste"),
        ("Proposer un chiffre justifié", "avec une contrepartie et une pièce extérieure"),
        ("Écrire une demande de révision", "sept fonctions, un seul point contesté"),
    ], cols=1,
       notes="Version projetée de l'autoévaluation du module, qui en compte "
             "vingt. Ces six-là sont celles que l'enseignante doit voir "
             "cochées avant de clore le module.")

    d.billet(
        "Écris la première phrase de ton paragraphe 2 : ce que tu acceptes.",
        exemples=[
            "Commence par « Je vous confirme d'abord mon accord sur… ».",
            "Nomme précisément les éléments, avec leur numéro.",
        ],
        notes="Cinq minutes avant l'écriture complète. Ceux qui commencent "
              "par contester se repèrent d'un coup d'œil, et c'est le moment "
              "de les reprendre — pas une fois la lettre écrite.")

    return d.save(dossier)
