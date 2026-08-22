# -*- coding: utf-8 -*-
"""E1 · Décris les étapes à voix haute
Bloc E « Je me lance » · couleur teal · 75 min. Production orale.
Source : bloc « Je me lance » du module — jeu de rôle `demarcheinterne` et
production orale. Intention du programme : décrire les étapes d'une démarche
administrative, en donnant les détails nécessaires.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Décris les étapes à voix haute",
        chapeau="C'est l'intention même du programme : décrire les étapes "
                "d'une démarche administrative, avec les détails "
                "nécessaires. Quatre semaines de module tiennent dans ces "
                "quatre-vingt-dix secondes.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Tout le module a préparé celle-ci : les cinq "
                  "étapes de B1, l'ordre de B2, les pronoms de B3, le subjonctif de "
                  "B4, les documents du bloc C, l'hypothèse en « si » de D2.")

    d.objectifs([
        "décrire les cinq étapes dans l'ordre, sans en sauter ;",
        "donner un délai précis pour au moins deux étapes ;",
        "illustrer un point par un exemple annoncé ;",
        "répondre à une objection sans se fâcher.",
    ], notes="Le deuxième objectif est celui qui distingue une bonne production d'une "
             "production moyenne : « avant vendredi » ne compte pas, « vendredi 25, "
             "seize heures » compte.")

    d.declencheur(
        'Retour', "Explique la démarche à ton voisin, sans notes. Deux minutes.",
        pistes=[
            "Commence par dire de quoi il s'agit et où tu l'as lu.",
            "Nomme les cinq étapes dans l'ordre.",
            "Donne au moins un délai exact.",
        ],
        notes="Faire circuler et noter qui saute une étape. Ne rien corriger pendant : "
              "on relève, on reprendra après le tableau du plan.")

    d.tableau('Le plan', "Trois temps, quatre-vingt-dix secondes",
              ['Le temps', 'Ce qu\'on y dit'],
              [["Temps 1", "de quoi il s'agit, et où tu l'as appris"],
               ["Temps 2", "les cinq étapes dans l'ordre, avec les délais"],
               ["Temps 3", "un exemple, puis ce que tu ferais à sa place"]],
              cle=0,
              note="Le plan est le même dans le module : l'élève le retrouve à l'écran, mot pour mot.",
              notes="Diapositive à photographier. Le faire recopier au dos du cahier : "
                    "c'est le seul papier autorisé pendant l'enregistrement.")

    d.cartes('Modèles', "Une phrase pour ouvrir chaque temps", [
        ("Temps 1",
         "« Chez nous, un poste de vérificatrice a été affiché au babillard le 14 septembre. C'est écrit dans la note de service. »"),
        ("Temps 2",
         "« D'abord, tu vérifies que tu as six mois d'ancienneté. Avant de rencontrer le comité, tu dois avoir remis le RH-04, au plus tard le vendredi 25 à seize heures. »"),
        ("Temps 3",
         "« Prenons la période d'essai : trente jours, et si ça ne convient pas, tu reviens à ton poste. À ta place, je me présenterais. »"),
        ("Ce qu'on évite",
         "Réciter le tableau sans le comprendre, sauter les délais, dire « il faut aller voir les ressources humaines » et s'arrêter là."),
    ], notes="Diapositive à photographier. Les trois modèles sont ceux du module : "
             "l'élève les retrouvera à l'écran, ce qui rassure ceux qui bloquent au "
             "moment d'enregistrer.")

    d.regle("Un exemple s'annonce",
            "Par exemple · notamment · ainsi · prenons · c'est le cas de.",
            precision="À l'oral, le connecteur avertit celui qui écoute qu'un exemple "
                      "arrive : il peut alors cesser de chercher une information "
                      "nouvelle. Sans lui, l'exemple se confond avec une étape de "
                      "plus, et l'explication paraît en compter six.",
            notes="Diapositive à photographier. Faire produire une phrase avec chacun "
                  "des cinq connecteurs, à l'oral, avant l'enregistrement.")

    d.pratique('Jeu de rôle', "Le collègue qui doute",
               "Avec l'assistant du module. Voici ce qu'il va dire — préparez vos réponses.", [
        ("« Où c'est écrit, ça ? »", "dans la note de service, et l'article 4 de la politique"),
        ("« C'est l'ancienneté qui décide, tout le monde le sait. »", "non : les compétences d'abord, article 4.3"),
        ("« Il faut la permission du chef d'équipe. »", "non : il est avisé, sa signature n'est pas requise"),
        ("« Tu vas perdre ta place à l'expédition. »", "non : droit de retour pendant trente jours"),
        ("« C'est quand la date limite, au juste ? »", "vendredi 25 septembre, seize heures"),
    ], corrige=True,
       notes="L'assistant joue Ghislain, bourru et pressé. Il redemande un délai "
             "chaque fois que l'élève reste vague, et il affirme une fois que "
             "l'ancienneté décide — pour être corrigé. Prévenir le groupe : c'est "
             "voulu.")

    d.piege('Piège', "réciter les cinq étapes comme une liste",
            "les relier par des mots d'ordre",
            "Une liste récitée s'oublie à la troisième étape et ne se comprend pas. "
            "Reliez : « d'abord », « une fois que c'est fait », « avant de », « dès "
            "que ». Ce sont les mots du bloc B, et c'est ce qui transforme une "
            "énumération en explication.",
            notes="Faire entendre les deux versions par la même personne : la liste "
                  "plate, puis la version reliée. La différence s'entend "
                  "immédiatement, et elle convainc mieux qu'une consigne.")

    d.pratique('Enregistrement', "Ce que l'IA regardera",
               "Relisez avant d'appuyer sur le micro.", [
        ("De quoi il s'agit, et où tu l'as appris", "dit avant tout détail"),
        ("Les cinq étapes, dans l'ordre", "sans en sauter ni les mélanger"),
        ("Au moins deux délais précis", "jour, date et heure"),
        ("Un exemple annoncé", "par exemple, notamment, ainsi, prenons"),
        ("Une reprise sans répétition", "ce poste, cette formation, je le sais"),
        ("Ce que tu ferais à sa place", "annoncé comme un avis"),
    ], corrige=True,
       notes="Ces six points sont exactement ceux de la consigne de correction du "
             "module. Les projeter pendant que le groupe enregistre : personne ne "
             "doit deviner sur quoi il est évalué.")

    d.billet(
        "Après ton enregistrement : quelle étape as-tu failli oublier ?",
        exemples=[
            "Une phrase.",
            "Dis ce que tu ferais pour ne pas l'oublier la prochaine fois.",
        ],
        notes="Trois minutes, après les enregistrements. C'est la préparation d'E2 : "
              "ce qu'on oublie à l'oral, on l'oublie aussi dans un courriel.")

    return d.save(dossier)
