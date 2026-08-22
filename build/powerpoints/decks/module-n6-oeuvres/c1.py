# -*- coding: utf-8 -*-
"""C1 · La feuille verte
Bloc C « Défi 2 · La biographie de la réalisatrice » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`, quatre cartes de FC_CARDS de la
section t2.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="La feuille verte",
        chapeau="Dix lignes sur une demi-feuille, et tout ce qui arrête un "
                "lecteur : des verbes qu'on ne dit jamais, des dates dans le "
                "désordre, et six petits mots qui renvoient en arrière.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 2. Distribuer la feuille verte — la "
                  "biographie imprimée — avant de parler, et laisser lire trois "
                  "minutes en silence. Les réactions viennent seules.")

    d.objectifs([
        "comprendre une biographie lue à voix haute ;",
        "repérer les verbes d'un temps qu'on ne parle jamais ;",
        "ranger les dates d'un texte sur une ligne du temps ;",
        "employer les quatre mots de la fabrication d'un film.",
    ], notes="Le premier objectif est l'intention de compréhension écrite du "
             "programme, mot pour mot : lire une biographie.")

    d.declencheur(
        'Observation', "Qu'est-ce qui te ralentit dans ce texte ?",
        pistes=[
            "Est-ce le vocabulaire, ou autre chose ?",
            "Y a-t-il des verbes que tu n'as jamais entendus ?",
            "Les dates sont-elles dans l'ordre ?",
            "Combien de fois le texte dit-il « elle » sans nommer la personne ?",
        ],
        notes="Presque personne ne répond « le vocabulaire ». C'est la démonstration "
              "du niveau 6 : ce qui bloque n'est plus le lexique, c'est la cohésion.")

    d.dialogue('Dialogue · 1 de 3', "La lecture à voix haute", [
        ("BRUNO", "Avant qu'on se quitte, prends la feuille verte. Je la lis à voix haute pour ceux qui n'ont pas leurs lunettes.", True),
        ("LECTRICE", "Aurélie Pichette naquit à Rimouski en 1951, dans une famille où personne n'allait au cinéma.", True),
        ("LECTRICE", "Elle entra par hasard dans une salle de montage en 1972 et y resta onze ans. C'est là qu'elle apprit son métier, dit-elle, et non dans une école.", True),
        ("LECTRICE", "Elle attendit quinze ans avant de tourner un long métrage. « Les Marées de novembre » sortit en 1994, dans huit salles seulement.", True),
    ], consigne="Écouter d'abord, feuille retournée.",
       notes="Faire écouter sans le texte sous les yeux. Un texte au passé simple "
             "entendu se comprend souvent mieux que lu : l'oreille ne bute pas sur "
             "l'orthographe.")

    d.dialogue('Dialogue · 2 de 3', "Des verbes qu'on n'entend jamais", [
        ("THÉRÈSE", "Attends, Bruno. Il y a des verbes que je n'ai jamais entendus. « Elle naquit », « elle entra », « il fut ». Personne ne parle comme ça.", True),
        ("BRUNO", "Personne, non. C'est le passé simple. On ne le parle jamais, mais on le lit tout le temps : dans les biographies, dans les romans, dans les documentaires.", True),
        ("THÉRÈSE", "Et je dois apprendre à l'écrire ?", True),
        ("BRUNO", "Non, jamais. Tu dois seulement le reconnaître. « Elle naquit », c'est « elle est née ».", True),
    ], notes="La réponse de Bruno est la consigne du module : reconnaître, pas "
             "produire. La répéter chaque fois qu'un élève s'inquiète, et ils "
             "s'inquiètent tous.")

    d.dialogue('Dialogue · 3 de 3', "Deux travaux pour un seul mot", [
        ("THÉRÈSE", "« Le film tint l'affiche onze semaines à Sherbrooke, où il avait été présenté en premier. » Le « où », il parle de la ville ou du moment ?", True),
        ("BRUNO", "De la ville. Et c'est une vraie question, parce que le même petit mot sert aussi pour le temps.", True),
        ("BRUNO", "Regarde la dernière phrase : « Elle y vint, et elle refusa de parler. » Le « y », il remplace quoi ?", True),
        ("THÉRÈSE", "La rétrospective ? Non... la salle Beauchemin. Elle est venue ici.", True),
    ], notes="L'hésitation de Thérèse, puis sa correction, est exactement le geste "
             "qu'on enseigne en C4 : reculer d'une phrase. La nommer.")

    d.tableau('Analyse', "Trois obstacles, trois gestes",
              ['L\'obstacle', 'Le geste'],
              [["les verbes au passé simple", "les traduire dans sa tête : elle naquit, elle est née"],
               ["les dates en désordre", "une ligne du temps au crayon, dans la marge"],
               ["les petits mots", "reculer d'une phrase, jamais plus loin"],
               ["ce qu'on ne fait pas", "chercher chaque mot inconnu : on perd le fil"]],
              cle=0,
              note="Trois gestes, dans cet ordre. Le troisième est le plus rentable.",
              notes="Diapositive à photographier. C'est le tableau de référence du "
                    "Défi 2 ; C2, C3 et C4 en prennent chacune une ligne.")

    d.vocabulaire('Vocabulaire', "Quatre mots pour fabriquer un film", [
        ("une réalisatrice", "La personne qui dirige le tournage d'un film et qui décide de sa forme."),
        ("un tournage", "La période pendant laquelle on filme, avec l'équipe et les acteurs."),
        ("le montage", "Le travail de choisir les morceaux filmés et de les mettre dans l'ordre voulu."),
        ("une rétrospective", "Une série de projections qui reprend tous les films d'une même personne."),
    ], notes="« Le montage » est le mot clé du bloc : onze ans de montage expliquent "
             "pourquoi ce film-là est construit en quatre morceaux. Le dire.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la biographie lue à voix haute.", [
        ("Aurélie Pichette est née à Rimouski en 1951.", "vrai"),
        ("Elle est partie à Montréal pour étudier le cinéma.", "faux - la comptabilité"),
        ("Elle a travaillé onze ans dans une salle de montage.", "vrai"),
        ("Son premier court métrage a été projeté trois fois seulement.", "vrai"),
        ("La critique de l'époque a bien accueilli le film.", "faux - elle fut sévère"),
        ("Le film a tenu l'affiche onze semaines à Sherbrooke.", "vrai"),
    ], corrige=True,
       notes="Faire retrouver la phrase exacte pour chaque réponse, doigt sur la "
             "ligne. C'est l'exercice de lecture, pas l'exercice de mémoire.")

    d.billet(
        "Écris la phrase de la biographie qui t'a le plus arrêté.",
        exemples=[
            "Recopie-la telle quelle.",
            "Ajoute un mot pour dire ce qui t'a arrêté.",
        ],
        notes="Deux minutes. Ces billets décident de l'ordre de C2 à C4 : si tous "
              "citent des verbes, commencer par le passé simple ; s'ils citent des "
              "pronoms, commencer par C4.")

    return d.save(dossier)
