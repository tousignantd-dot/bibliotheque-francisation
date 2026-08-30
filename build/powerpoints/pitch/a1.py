# -*- coding: utf-8 -*-
"""A1 · Les écrans, cas par cas — ce que voit l'enseignant, selon la décision.

Section acier · l'annexe qu'on ouvre quand une direction demande « oui, mais
concrètement, ça donne quoi ? ». Ce sont de **vraies captures** du portail avec
une classe de démonstration, jamais des maquettes : c'est tout l'argument.

Source : `assets/presentations/captures-cas-de-figure.html`.
"""
from theme import Deck
from vues import ecran, poser


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Les écrans, cas par cas",
        chapeau="Quatre décisions d'établissement, et ce qu'elles changent à l'écran. "
                "Chaque image est une capture du portail en marche, avec une classe de "
                "démonstration — rien n'est dessiné pour la circonstance.",
        duree='6 minutes')

    d.titre(surtitre="ANNEXE  ·  LES ÉCRANS",
            notes="Annexe. On ne la projette pas d'office : on l'ouvre quand la salle "
                  "demande à voir. Si personne ne demande, c'est que la démonstration "
                  "en direct a suffi.")

    d.regle("Ce que cette annexe prouve",
            "Tout ce qui suit existe et tourne aujourd'hui.",
            precision="Les captures sont prises sur le portail en marche, avec des "
                      "élèves fictifs. Une maquette montre ce qu'on aimerait livrer ; "
                      "une capture montre ce qui est livré.",
            notes="Le dire une fois, au début. Ensuite les images parlent seules.")

    # ── Suivre une classe : deux façons, un seul écran ────────────────
    ecran(d, "Suivre une classe", "Avec des comptes",
          poser('cas', '01-suivi-comptes'),
          "Chaque élève a un pseudonyme et un code. L'enseignant voit qui a fait "
          "quoi, et retrouve un dossier individuel.",
          notes="Le mode ordinaire. Insister sur un mot : pseudonyme, jamais le vrai "
                "nom — le champ s'appelle « pseudo » dans l'interface, et c'est voulu.")

    ecran(d, "Suivre une classe", "Le même tableau, projeté",
          poser('cas', '02-suivi-anonyme'),
          "Un interrupteur remplace les pseudonymes par des rangs stables : on "
          "projette le travail de la classe sans exposer personne.",
          notes="C'est un réglage d'affichage, pas une permission — l'enseignant a "
                "déjà accès aux dossiers. Le bouton sert à montrer un texte au tableau "
                "sans nommer son auteur.")

    ecran(d, "Suivre une classe", "Sans aucun compte",
          poser('cas', '04-suivi-seance'),
          "Même tableau, mêmes chiffres. Les élèves s'appellent « Participant 3 » : "
          "il n'existe aucune donnée pour les nommer.",
          notes="La diapositive qui répond à la Loi 25 sans en parler. Le suivi n'est "
                "pas dégradé pour autant : c'est le même écran.")

    ecran(d, "Sans aucun compte", "Ce qu'on photocopie",
          poser('cas', '05-feuille-seance'),
          "Un code à six caractères, un code QR, l'adresse en toutes lettres. Noir "
          "et blanc : c'est la photocopieuse de l'école qui la tire.",
          notes="Le code QR est fabriqué par le serveur, pas par un service en ligne. "
                "Personne d'extérieur ne voit l'adresse de la classe.")

    # ── Le même module, selon que l'assistance est ouverte ────────────
    ecran(d, "Un module", "Assistance ouverte",
          poser('cas', '07-module-avec-ia'),
          "L'élève peut faire traduire un mot, simplifier une consigne, poser une "
          "question. Sept outils dans le rail de droite.",
          notes="Ne pas s'attarder : c'est la diapositive suivante qui porte "
                "l'argument.")

    ecran(d, "Un module", "Assistance fermée",
          poser('cas', '08-module-sans-ia'),
          "Le même fichier. Ce qui dépend d'un modèle disparaît ; l'écoute, la "
          "prononciation, le carnet et la révision restent.",
          notes="Le point à faire passer : ce n'est pas une version amputée qu'on "
                "installe ailleurs, c'est le même fichier qui se replie. Un centre qui "
                "change d'avis n'a rien à redéployer.")

    ecran(d, "Assistance fermée", "Ce qu'on perd, ce qu'on garde",
          poser('cas', '10-production-sans-ia'),
          "Plus de relecture avant l'envoi : l'enseignant reçoit le texte tel quel. "
          "La tâche, elle, ne bouge pas.",
          notes="Répondre ici à « qu'est-ce qu'on perd ? ». On perd la relecture "
                "immédiate, pas l'exercice — une réponse honnête rassure plus qu'un "
                "« rien du tout ».")

    # ── Où la décision se pose ───────────────────────────────────────
    ecran(d, "La décision", "Elle se pose sur l'arbre",
          poser('cas', '12-arbre-refus'),
          "Sur un centre, ou sur une commission scolaire entière. Le premier "
          "réglage explicite tranche, et il s'hérite vers le bas.",
          notes="Montrer que le badge dit d'où vient la décision — « hérité de "
                "CSS X ». Un centre qui a négocié une exception la porte écrite sur "
                "lui-même.")

    d.billet("Un dernier écran, si la question vient : l'espace direction, où l'on "
             "ouvre les comptes et où l'on regarde la dépense.",
             exemples=["Les treize captures sont dans le document papier.",
                       "Il se laisse sur la table à la fin de la rencontre."],
             notes="Fermer ici. Le document papier « Les écrans, cas par cas » reprend "
                   "les treize captures, celles-ci comprises.")

    return d.save(dossier)
