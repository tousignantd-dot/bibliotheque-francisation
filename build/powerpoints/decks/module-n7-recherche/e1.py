# -*- coding: utf-8 -*-
"""E1 · L'appel, et l'exposé
Bloc E « Je me lance » · couleur teal · production orale · 75 min.
Source : section `appli` du module — jeu de rôle `recherche`, production orale.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="L'appel, et l'exposé",
        chapeau="Un appel sans question, c'est une candidature de plus. Un "
                "appel avec trois questions, c'est un nom qu'on retient. "
                "Ensuite, deux minutes debout pour comparer deux régions.",
        duree='75 minutes')

    d.titre(notes="Première séance de production. Les élèves arrivent avec leurs "
                  "trois questions de D1 et leur feuille à deux colonnes de C4. "
                  "Vérifier que chacun les a avant de commencer.")

    d.objectifs([
        "téléphoner à un employeur pour s'informer, avant de postuler ;",
        "poser des questions ouvertes et relier son parcours à l'entreprise ;",
        "exposer les avantages et les inconvénients de deux régions ;",
        "annoncer une décision et la justifier par un chiffre.",
    ], notes="Les deux dernières viennent des attentes de fin de cours du niveau 7, "
             "pas de la situation : « il expose les avantages et les inconvénients "
             "de deux situations pour prendre une décision ». Le dire au groupe.")

    d.declencheur(
        'Préparation', "Que dit-on dans les dix premières secondes d'un appel ?",
        pistes=[
            "Votre nom, d'où vous appelez, et pourquoi.",
            "Combien de secondes pour les trois ?",
            "Qu'est-ce que la personne au bout du fil est en train de faire ?",
            "Que se passe-t-il si vous n'avez pas préparé vos questions ?",
        ],
        notes="Faire chronométrer : dix secondes suffisent largement pour les trois. "
              "Le faire dire debout, à voix haute, deux fois par élève.")

    d.regle("Un appel se prépare, ou il ne sert à rien",
            "Trois questions écrites avant de composer le numéro. Trois "
            "questions que l'annonce ne permet pas de trancher.",
            precision="Le salaire, le supérieur immédiat, le nombre de postes, les "
                      "conditions d'un programme d'installation : les silences d'une "
                      "annonce sont vos questions. Et l'appel n'est pas une entrevue "
                      "— vous ne serez ni retenu ni écarté aujourd'hui.",
            notes="Diapositive à photographier. Rassurer : personne ne décide rien "
                  "au téléphone. C'est ce qui rend l'exercice possible.")

    d.tableau('Analyse', "Les trois situations du jeu de rôle",
              ['Le cas', 'Ce qu\'il faut obtenir'],
              [["Le poste au laboratoire",
                "les tâches réelles, l'horaire, à qui l'on se rapporte"],
               ["L'aide à l'installation",
                "le montant, les conditions, la durée"],
               ["Le diplôme obtenu ailleurs",
                "ce qui rend une expérience « vérifiable »"]],
              cle=0,
              note="L'assistant joue le chef du laboratoire. Il répond volontiers, mais il ne devine rien.",
              notes="Diapositive à photographier. Les trois cas sont ceux de la "
                    "section « Je me lance » du module interactif.")

    d.cartes('Analyse', "Les tournures à réutiliser", [
        ("Demander poliment", "Pourriez-vous me préciser la date d'entrée en fonction ?"),
        ("Dire son but", "Je vous appelle pour que vous ayez mon nom en tête."),
        ("Mettre en avant", "Ce que j'apporte, c'est neuf ans de contrôle de conformité."),
        ("Restreindre", "Je n'ai travaillé qu'en laboratoire industriel."),
        ("Changer de sujet", "Quant à l'installation dans la région, j'aurais une question."),
        ("Conclure", "En somme, à qui dois-je faire parvenir mon dossier ?"),
    ], cols=1,
       notes="Les six tournures viennent des cinq séances de grammaire du module. "
             "Les afficher pendant tout le jeu de rôle.")

    d.piege('Production orale',
            "« Bonjour, je vous appelle pour le poste. »",
            "« Bonjour, Hafida Zerouali, j'appelle de Longueuil au sujet du poste de technicienne de laboratoire affiché chez vous. »",
            "La première laisse tout le travail à l'interlocuteur : quel "
            "poste, qui parle, d'où. La seconde donne les trois "
            "renseignements en une phrase, et la conversation commence "
            "vraiment à la deuxième réplique.",
            notes="Faire répéter la phrase longue jusqu'à ce qu'elle sorte d'un "
                  "trait. C'est la seule qu'il faut savoir par cœur.")

    d.pratique('Production orale', "L'exposé : trois temps, deux minutes",
               "Debout, sans lire ses notes mot à mot.", [
        ("TEMPS 1", "les deux régions, et pourquoi celles-là"),
        ("TEMPS 2", "les avantages et les inconvénients, chiffres à l'appui"),
        ("TEMPS 3", "votre décision, et la raison qui a pesé le plus"),
        ("Un connecteur au moins", "quant à, par ailleurs, en somme"),
        ("Un comparatif au moins", "plus de, moins de, meilleur, le plus"),
        ("Une mise en avant", "ce qui a pesé le plus, c'est..."),
    ], notes="Deux minutes chacun, minutées. Le reste du groupe écoute avec une "
             "grille à trois cases : les trois temps y sont-ils ? Pas de note, une "
             "remarque par auditeur.")

    d.billet(
        "Quelle question avez-vous oublié de poser au téléphone ?",
        exemples=[
            "Il y en a toujours une.",
            "Écrivez-la : elle ira dans votre lettre.",
        ],
        notes="Transition vers E2 : ce qui n'a pas été demandé de vive voix se "
              "demande par écrit, dans le troisième paragraphe de la lettre.")

    return d.save(dossier)
