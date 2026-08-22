# -*- coding: utf-8 -*-
"""B1 · Aux ressources humaines, bureau 12
Bloc B « Défi 1 · On m'explique la démarche » · couleur acier · 75 min.
Source : dialogue `t1`, exercices `t1vf` et `t1ordre`, cinq cartes de
FC_CARDS. Intention du programme : comprendre des explications sur les étapes
d'une démarche administrative.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Aux ressources humaines, bureau 12",
        chapeau="Marie-Soleil Grenon explique la démarche en cinq étapes, "
                "sans papier, en quinze minutes. Ce qui est difficile n'est "
                "pas le vocabulaire : c'est que tout se tient.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 1. C'est l'intention même du programme : "
                  "comprendre des explications sur les étapes d'une démarche "
                  "administrative. Tout le bloc B travaille cette écoute-là.")

    d.objectifs([
        "suivre une explication de cinq étapes du début à la fin ;",
        "noter pour chaque étape l'action, le document, le délai, la "
        "personne ;",
        "distinguer ce qui est exigé de ce qui est seulement possible ;",
        "employer les cinq mots des ressources humaines.",
    ], notes="Le deuxième objectif est celui qu'on évalue : quatre colonnes dans le "
             "cahier, et on remplit à l'écoute. C'est un geste, pas une notion.")

    d.declencheur(
        'Observation', "Qu'est-ce que tu fais quand quelqu'un t'explique trop vite ?",
        pistes=[
            "Tu demandes de répéter, ou tu attends la fin ?",
            "Est-ce que tu notes pendant, ou après ?",
            "Quelle question poses-tu quand une date n'a pas été dite ?",
        ],
        notes="La troisième question prépare la séance. La réponse attendue : « c'est "
              "pour quand ? ». Beaucoup d'élèves n'osent pas la poser, et c'est la "
              "seule qui compte vraiment dans une démarche.")

    d.dialogue('Dialogue · 1 de 3', "Les deux premières étapes", [
        ("YANETH", "Bonjour. Je viens pour l'affichage du poste de vérificatrice à la qualité.", True),
        ("MARIE-SOLEIL", "Je vais vous expliquer la démarche au complet. Il y a cinq étapes, et elles se font dans l'ordre.", True),
        ("MARIE-SOLEIL", "Premièrement, vous vérifiez que vous êtes admissible : six mois d'ancienneté et la formation sur les allergènes.", True),
        ("MARIE-SOLEIL", "Deuxièmement, vous remplissez le formulaire RH-04, la demande de mutation interne.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Faire relever les deux étapes au tableau, en quatre colonnes : action, "
             "document, délai, personne. La première n'a pas de délai — le faire "
             "remarquer, c'est normal.")

    d.dialogue('Dialogue · 2 de 3', "Le délai, et le chef d'équipe", [
        ("YANETH", "Et il faut que je le remette en personne ?", True),
        ("MARIE-SOLEIL", "Non, vous pouvez me l'envoyer par courriel. Ce qui compte, c'est la date : je dois l'avoir avant le vendredi vingt-cinq, seize heures.", True),
        ("YANETH", "Et mon chef d'équipe ? Ghislain m'a dit qu'il n'avait rien à signer.", True),
        ("MARIE-SOLEIL", "Il a raison. Je l'avise, c'est tout. Sa signature n'est pas requise et son avis n'entre pas dans la décision.", True),
    ], notes="« Ce qui compte, c'est la date » : la phrase pivot de la séance. La "
             "faire répéter. Beaucoup d'élèves retiennent le geste et perdent "
             "l'échéance.")

    d.dialogue('Dialogue · 3 de 3', "Le comité, et sur quoi on choisit", [
        ("YANETH", "Et le choix se fait comment ? Par ancienneté ?", True),
        ("MARIE-SOLEIL", "Non, et c'est important que vous le sachiez. Le choix se fait sur les compétences. L'ancienneté ne tranche qu'à égalité.", True),
        ("MARIE-SOLEIL", "Beaucoup de gens ne se présentent pas parce qu'ils pensent le contraire, et ils se privent pour rien.", True),
        ("YANETH", "Donc je ne perds pas ma place à l'expédition tant que les trente jours ne sont pas finis.", True),
    ], notes="La dernière réplique est une reformulation par l'élève du dialogue : "
             "c'est exactement ce qu'on demandera au groupe de faire. La signaler "
             "comme un modèle.")

    d.tableau('Analyse', "Les cinq étapes, avec leur délai",
              ['Étape', 'Ce qu\'elle demande'],
              [["1 · Admissibilité", "six mois d'ancienneté et la formation sur les allergènes"],
               ["2 · Formulaire", "remplir le RH-04, demande de mutation interne"],
               ["3 · Remise", "aux ressources humaines, avant le vendredi 25, 16 h"],
               ["4 · Comité", "trente minutes, la semaine du 28, deux personnes"],
               ["5 · Réponse", "par écrit, dans les cinq jours ouvrables, à tous"]],
              cle=0,
              note="La période d'essai vient après, et seulement si la candidature est retenue.",
              notes="Diapositive à photographier. C'est le tableau de tout le bloc B, "
                    "et c'est ce que l'élève devra redire à voix haute en E1.")

    d.regle("Ce qu'une étape porte toujours",
            "L'action, le document, le délai, la personne — quatre choses, pas une de moins.",
            precision="Une étape à laquelle il manque le délai est une étape qu'on "
                      "manquera. C'est la première chose à demander quand elle n'a "
                      "pas été dite : « c'est pour quand ? ». Personne ne trouvera "
                      "la question déplacée, et elle sauve des démarches entières.",
            notes="Diapositive à photographier. Faire poser la question à voix haute "
                  "par trois élèves, pour qu'elle sorte facilement le jour venu.")

    d.vocabulaire('Vocabulaire', "Cinq mots des ressources humaines", [
        ("les ressources humaines", "Le service qui s'occupe des employés : dossiers, formulaires, congés."),
        ("un formulaire", "La feuille toute faite qu'on remplit pour demander quelque chose."),
        ("un comité de sélection", "Le petit groupe qui rencontre les candidats et qui choisit."),
        ("l'ancienneté", "Le temps qu'une personne a passé au service du même employeur."),
        ("une période d'essai", "Le temps où l'on fait le nouveau travail pour voir si ça convient."),
    ], notes="« L'ancienneté » se compte dans l'entreprise, pas dans le poste : c'est "
             "la précision qui règle la moitié des questions du groupe.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'explication de Marie-Soleil.", [
        ("Il faut six mois d'ancienneté et la formation sur les allergènes.", "vrai"),
        ("Le formulaire doit obligatoirement être remis en personne.", "faux - le courriel est accepté"),
        ("La signature du chef d'équipe est nécessaire.", "faux - il est seulement avisé"),
        ("Le comité est formé de deux personnes et dure trente minutes.", "vrai"),
        ("Le choix se fait d'abord sur l'ancienneté.", "faux - sur les compétences"),
        ("Seules les personnes retenues reçoivent une réponse écrite.", "faux - tous les candidats internes"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le cinquième est "
             "celui qui change des vies : c'est la croyance qui empêche de se présenter.")

    d.billet(
        "Écris les cinq étapes, dans l'ordre, sans regarder le tableau.",
        exemples=[
            "Trois mots par étape suffisent.",
            "Ajoute un délai à celles qui en ont un.",
        ],
        notes="Cinq minutes. Ramasser : c'est la mesure de la séance, et le point de "
              "départ de B2. Ceux qui inversent 2 et 3 sont ceux qu'il faudra "
              "reprendre sur « avant de » et « une fois que ».")

    return d.save(dossier)
