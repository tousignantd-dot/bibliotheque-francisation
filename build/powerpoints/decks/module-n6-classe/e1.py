# -*- coding: utf-8 -*-
"""E1 · La rencontre d'équipe, et le compte rendu à voix haute
Bloc E « Je me lance » · couleur framboise · 75 min. Production orale.
Source du module : `ROLE_CAS` du jeu de rôle et le bloc « Production orale ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='framboise',
        titre="La rencontre d'équipe, et le compte rendu à voix haute",
        chapeau="D'abord se partager le travail — ce qui demande d'arriver "
                "avec une proposition. Ensuite dire à la classe ce qu'on a "
                "trouvé, en cinq minutes, sans lire sa feuille.",
        duree='75 minutes')

    d.titre(notes="La situation « Salle de classe » n'a aucune intention de "
                  "production au programme : les deux tâches viennent des "
                  "attentes de fin de cours du niveau 6, qui sont communes à "
                  "toutes ses situations.")

    d.objectifs([
        "proposer une répartition du travail et la justifier ;",
        "reprendre ce que l'autre vient de dire sans le répéter ;",
        "fixer une date pour chaque partie, et la faire redire ;",
        "présenter un compte rendu en trois temps.",
    ], notes="Le premier objectif est le plus difficile et le moins "
             "enseigné : arriver avec une proposition plutôt qu'avec une "
             "question ouverte.")

    d.declencheur(
        'Pour commencer', "Une rencontre d'équipe qui ne décide rien : pourquoi ?",
        pistes=[
            "Personne n'est arrivé avec une proposition ?",
            "Personne n'a donné de date ?",
            "Est-ce que ça vous est déjà arrivé ?",
        ],
        notes="Les deux premières pistes sont les deux causes réelles. "
              "Laisser le groupe les trouver : l'expérience est là, elle ne "
              "demande qu'à être nommée.")

    d.tableau('Analyse', "Ce qui fait avancer une rencontre",
              ['Ce qu\'on dit', 'Ce que ça produit'],
              [["« Je propose que… »", "une décision possible dès la première minute"],
               ["« J'ai déjà lu… »", "de la confiance, parce que c'est vérifiable"],
               ["« Toi, tu prendrais… »", "une part nommée, pas un vague partage"],
               ["« D'ici vendredi 14 »", "une date, donc un engagement"],
               ["« Donc, toi tu fais… »", "un récapitulatif : plus personne n'a d'excuse"]],
              cle=0,
              note="« On se partage ça » ne décide rien, et « bientôt » n'est pas une date.",
              notes="Diapositive à photographier. La note du bas est ce que "
                    "l'assistant du module refuse explicitement d'accepter "
                    "dans le jeu de rôle.")

    d.cartes('Jeu de rôle', "Trois situations, à choisir", [
        ("Qui fait quoi", "Onze jours, rien n'est partagé. Tu arrives avec une proposition."),
        ("La partie manquante", "Quatre jours, une partie n'est pas écrite, et ce n'est pas la tienne."),
        ("Les sources s'opposent", "Ton coéquipier veut n'en garder qu'une. Tu penses qu'il faut écrire les deux."),
    ], cols=3,
       notes="Ce sont les trois cas du jeu de rôle du module. L'assistant "
             "joue un coéquipier de bonne foi qui ne propose jamais rien de "
             "lui-même : sans proposition, la rencontre tourne en rond.")

    d.regle("Une part nommée, une date, un récapitulatif",
            "« Toi, tu prends la partie sur le traitement. Moi, la page de la ville. D'ici vendredi 14. »",
            precision="Sans nom de partie, personne ne sait quoi faire. Sans "
                      "date, personne ne sait quand. Sans récapitulatif, "
                      "chacun se rappellera autre chose.",
            notes="Diapositive à photographier. Faire jouer la rencontre en "
                  "vraies équipes après cette diapositive : quinze minutes, "
                  "puis on passe à l'oral.")

    d.tableau('Analyse', "Le compte rendu, en trois temps",
              ['Le temps', 'Ce qu\'on y dit'],
              [["Temps 1", "le sujet, et pourquoi l'équipe l'a choisi"],
               ["Temps 2", "ce que les sources disent, en nommant chacune"],
               ["Temps 3", "ce que l'équipe en conclut, annoncé comme un avis"]],
              cle=0,
              note="Environ 90 secondes chacun pour préparer sa part ; cinq minutes par équipe en classe.",
              notes="Diapositive à photographier. Le temps 2 est le seul où "
                    "l'on nomme ses sources, et c'est ce que la grille "
                    "regarde.")

    d.pratique('Pratique', "Les phrases qui servent",
               "Dites à quel moment de la rencontre chaque phrase sert.", [
        ("Je propose qu'on se partage comme ça.", "au début : la proposition"),
        ("J'ai déjà lu la page de la ville.", "pour dire ce qui est fait"),
        ("Tu disais que la lettre ne compte pas ; moi, je ne le pense pas.", "pour reprendre sans répéter"),
        ("Si tu finis lundi, je relis tout mardi.", "pour poser une condition"),
        ("Envoie-les-moi avant vendredi.", "pour demander une chose précise"),
        ("Donc, toi tu fais le traitement, moi la ville.", "à la fin : le récapitulatif"),
    ], corrige=True, cols=1,
       notes="Faire dire chaque phrase à voix haute avant de la classer. "
             "Ce sont exactement les tournures que l'élève réemploiera dans "
             "le jeu de rôle du module.")

    d.piege('Exposé',
            "lire sa feuille pendant le compte rendu",
            "répéter trois fois, chronomètre en main",
            "La consigne dit « sans lire son texte », et un texte lu perd son "
            "auditoire à la deuxième phrase. La seule solution est la "
            "répétition : la première dure toujours huit minutes, la "
            "troisième tient dans cinq.",
            notes="Prévoir dix minutes de répétition en équipe à la fin de la "
                  "séance, avec un chronomètre par équipe. Le faire en "
                  "classe : la plupart ne le feront pas à la maison.")

    d.billet(
        "Écris la première phrase de ton compte rendu.",
        exemples=[
            "Elle doit nommer le sujet et dire pourquoi vous l'avez choisi.",
            "Une phrase, apprise par cœur : c'est celle qui rassure au moment de commencer.",
        ],
        notes="Trois minutes. Faire dire quelques premières phrases à voix "
              "haute avant de sortir : entendre la sienne dans sa propre "
              "bouche change tout pour la séance suivante.")

    return d.save(dossier)
