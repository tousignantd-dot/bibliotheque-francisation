# -*- coding: utf-8 -*-
"""C3 · L'article 4, ligne à ligne
Bloc C « Défi 2 · Ce que disent les documents » · couleur ambre · 75 min.
Source : exercice `t2polit` — le second exercice du type `texte` — et sa
mini-leçon. Savoir du programme : tenir compte de la présentation matérielle ;
comprendre un verbe pronominal à sens passif.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="L'article 4, ligne à ligne",
        chapeau="Une politique interne est un texte que l'entreprise écrit "
                "pour elle-même. Ce n'est pas une loi — et à l'intérieur de "
                "l'entreprise, c'est le texte le plus lourd.",
        duree='75 minutes')

    d.titre(notes="Séance de lecture d'un texte réglementaire. Dire d'entrée que les "
                  "règles du module sont celles d'une entreprise inventée : elles ne "
                  "décrivent aucune loi du Québec, et une autre usine en aurait "
                  "d'autres.")

    d.objectifs([
        "lire un article numéroté et le citer par son numéro ;",
        "reconnaître les trois marques de la langue d'une politique ;",
        "chercher dans un article : qui, quoi, quand, et sinon ;",
        "remettre une phrase passive à l'actif pour savoir qui agit.",
    ], notes="Le quatrième objectif est une stratégie de lecture : « une réponse est "
             "transmise » — par qui ? La réponse est presque toujours « l'employeur ».")

    d.declencheur(
        'Observation', "« Tout poste vacant est affiché. » Qui affiche ?",
        pistes=[
            "Est-ce écrit dans la phrase ?",
            "Pourquoi la politique ne le dit-elle pas ?",
            "Est-ce qu'on peut le savoir quand même ?",
        ],
        notes="Deux minutes. La conclusion — le passif sans auteur est la langue "
              "normale d'un règlement — évite au groupe de croire à une cachotterie.")

    d.tableau('Analyse', "L'article 4, paragraphe par paragraphe",
              ['Le numéro', 'Ce qu\'il règle'],
              [["4.1", "affichage à l'interne d'abord, dix jours ouvrables"],
               ["4.2", "qui peut se présenter : six mois de service continu"],
               ["4.3", "le choix : les compétences, puis l'ancienneté à égalité"],
               ["4.4", "réponse écrite à tous, dans les cinq jours ouvrables"],
               ["4.5", "période d'essai de trente jours et droit de retour"]],
              cle=0,
              note="« Selon 4.3 » suffit à mettre tout le monde devant le même texte.",
              notes="Diapositive à photographier. Faire apprendre un seul numéro par "
                    "cœur — 4.3 — parce que c'est celui qui décide qui obtient le "
                    "poste, et celui qu'on croit connaître de travers.")

    d.regle("La langue d'une politique, trois marques",
            "Elle dit « l'employé », elle emploie des noms, elle emploie le passif.",
            precision="« Le comblement des postes » plutôt que « quand on comble un "
                      "poste » ; « une réponse est transmise » plutôt que « nous "
                      "transmettons une réponse » ; « l'employé qui compte six mois » "
                      "plutôt que « vous ». Ces trois marques la rendent sèche — et "
                      "elles disent qu'elle vaut pour tout le monde, pas pour vous en "
                      "particulier.",
            notes="Diapositive à photographier. Rappeler la séance A3 : les noms en "
                  "-tion, -ment, -age. C'est exactement ce vocabulaire-là qui revient "
                  "ici, et le groupe l'a déjà travaillé.")

    d.pratique('Lecture', "Dans quel article est la réponse ?",
               "Nommez le numéro, puis lisez le passage exact.", [
        ("Où un poste vacant est-il offert en premier ?", "4.1 - à l'interne, avant l'externe"),
        ("Combien de temps de service faut-il ?", "4.2 - six mois de service continu"),
        ("Sur quoi le comité fonde-t-il son choix ?", "4.3 - les compétences"),
        ("Qu'est-ce qui décide quand deux personnes se valent ?", "4.3 - l'ancienneté départage"),
        ("Que reçoit une personne non retenue ?", "4.4 - une réponse écrite"),
        ("Que garde l'employé pendant l'essai ?", "4.5 - le droit de revenir à son poste"),
    ], corrige=True,
       notes="Exiger le numéro avant la phrase. C'est le geste que la séance installe, "
             "et c'est ce que l'exercice interactif fait faire en cliquant dans le "
             "texte.")

    d.piege('Piège', "lire « à compétences égales » comme « selon l'ancienneté »",
            "lire la phrase en entier, dans l'ordre",
            "L'article 4.3 dit deux choses : d'abord les compétences, ensuite — et "
            "seulement à égalité — l'ancienneté. Beaucoup de gens ne retiennent que "
            "la seconde moitié et ne se présentent jamais. C'est la lecture partielle "
            "la plus coûteuse de tout le module.",
            notes="Y consacrer du temps : c'est la croyance qui décide qui dépose un "
                  "formulaire et qui n'en dépose pas. Faire relire 4.3 à voix haute "
                  "par trois élèves.")

    d.pratique('Écriture', "Remettre à l'actif",
               "Récrivez la phrase en disant qui fait l'action.", [
        ("Tout poste vacant est affiché à l'interne.", "l'employeur affiche tout poste vacant"),
        ("Une réponse écrite est transmise à chaque candidat.", "les ressources humaines transmettent une réponse"),
        ("L'employé muté est soumis à une période d'essai.", "l'entreprise soumet l'employé muté à un essai"),
        ("La candidature est retenue par le comité.", "le comité retient la candidature"),
    ], corrige=True,
       notes="Accepter « l'employeur » ou « l'entreprise » partout : le point n'est "
             "pas de deviner le service exact, c'est de savoir qu'il y a quelqu'un "
             "derrière la phrase.")

    d.billet(
        "Quel article citerais-tu si on te disait que l'ancienneté décide ?",
        exemples=[
            "Donne le numéro.",
            "Écris la phrase que tu dirais, en une ligne.",
        ],
        notes="Trois minutes. C'est la répétition du jeu de rôle d'E1, où l'assistant "
              "affirme précisément cela. Ramasser et relire deux ou trois réponses à "
              "voix haute.")

    return d.save(dossier)
