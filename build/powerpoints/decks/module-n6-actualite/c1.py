# -*- coding: utf-8 -*-
"""C1 · Vingt minutes avec l'Office
Bloc C « Défi 2 · L'entrevue et le documentaire » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`, cartes FC_CARDS de la tâche `t2`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Vingt minutes avec l'Office",
        chapeau="Une entrevue n'explique pas : elle fait parler quelqu'un. "
                "Ce qu'on y apprend dépend autant des questions posées que "
                "des réponses données - et de ce que l'invitée choisit de "
                "ne pas dire.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 2. Le sujet est le même qu'au Défi 1, mais "
                  "le genre a changé. Le demander au groupe avant l'écoute : qu'est-ce "
                  "qui va être différent ? Les réponses préparent l'écoute mieux "
                  "qu'une consigne.")

    d.objectifs([
        "suivre une entrevue longue sans perdre le fil ;",
        "distinguer ce que dit l'animateur de ce que dit l'invitée ;",
        "comprendre les trois causes différentes qu'une même expression "
        "recouvre ;",
        "employer les quatre mots de l'enquête.",
    ], notes="Le troisième objectif est le contenu le plus dense du module. Ne pas le "
             "traiter comme du vocabulaire : c'est une distinction de raisonnement, et "
             "elle revient à l'écrit en E2.")

    d.declencheur(
        'Observation', "Pourquoi un appareil brise-t-il ?",
        pistes=[
            "Est-ce qu'on t'a déjà dit qu'un appareil était « fait pour briser » ?",
            "Est-ce que c'est toujours vrai, selon toi ?",
            "As-tu déjà attendu une pièce de rechange ? Combien de temps ?",
            "As-tu déjà renoncé à réparer parce que c'était trop cher ?",
        ],
        notes="Les trois dernières questions correspondent aux trois causes que Myriam "
              "Vaugeois va distinguer. Les poser d'avance rend son explication "
              "évidente : le groupe l'a déjà vécue, il lui manque les mots.")

    d.dialogue('Entrevue · 1 de 3', "Ils avaient renoncé avant d'essayer", [
        ("THÉO", "Nous recevons Myriam Vaugeois, conseillère à l'Office de la protection du consommateur. Depuis mardi, notre boîte de courriels déborde.", True),
        ("MYRIAM", "Ça ne me surprend pas. Chaque fois qu'une chronique parle de la garantie légale, nos lignes sonnent pendant trois jours. Les gens avaient renoncé avant même d'essayer.", True),
        ("THÉO", "Renoncé à quoi, exactement ?", True),
        ("MYRIAM", "À se plaindre. Beaucoup nous racontent qu'ils avaient jeté l'appareil avant de nous appeler. Ils l'avaient remplacé, ils avaient payé deux fois.", True),
    ], consigne="Première écoute, diapositive masquée.",
       notes="Quatre plus-que-parfaits dans cette seule page : avaient renoncé, avaient "
             "jeté, avaient remplacé, avaient payé. Ne rien en dire aujourd'hui, mais "
             "les repérer soi-même : c'est la matière de C2.")

    d.dialogue('Entrevue · 2 de 3', "Trois choses derrière le même mot", [
        ("THÉO", "Mille heures décidées d'avance. C'est de l'obsolescence programmée ?", True),
        ("MYRIAM", "C'en est l'exemple le plus ancien et le plus documenté. Mais je vous demande d'être prudent avec cette expression, parce qu'elle sert aujourd'hui à tout expliquer.", True),
        ("MYRIAM", "Un appareil peut briser parce qu'il a été mal conçu ; parce qu'aucune pièce de rechange n'est disponible ; ou parce que la réparation coûte plus cher qu'un appareil neuf.", True),
        ("THÉO", "Laquelle des trois vous préoccupe le plus ?", True),
    ], notes="La question de Théo est la plus courte de l'entrevue, et c'est elle qui "
             "amène l'idée principale. Le faire remarquer maintenant : c'est le repère "
             "travaillé en C4.")

    d.dialogue('Entrevue · 3 de 3', "Appelez avant de jeter", [
        ("MYRIAM", "La deuxième. Il faut que les pièces existent et qu'on puisse les commander. Un appareil qu'on ne peut pas réparer est jetable, même s'il a été bien fait.", True),
        ("MYRIAM", "Je souhaite qu'ils appellent avant de jeter. Et qu'ils écrivent. Une mise en demeure écrite change complètement le ton d'une discussion, parce qu'elle laisse une trace.", True),
        ("THÉO", "On entend souvent dire que les petites créances, c'est long.", True),
        ("MYRIAM", "C'est vrai que c'est long. Je ne le nierai pas. Mais beaucoup de dossiers se règlent avant l'audience, dès que le commerçant reçoit l'avis.", True),
    ], notes="« C'est vrai que c'est long, je ne le nierai pas » : une invitée qui "
             "concède gagne en crédibilité. Le montrer au groupe, ça servira au "
             "courrier des lecteurs du Défi 3.")

    d.tableau('Analyse', "Trois causes derrière une seule expression",
              ['La cause', 'Ce qu\'elle exige'],
              [["L'appareil est mal conçu", "un recours contre le fabricant"],
               ["Il n'y a pas de pièce", "que les pièces existent et se commandent"],
               ["Réparer coûte plus cher", "un choix économique, pas un défaut"]],
              cle=0,
              note="Madame Vaugeois se préoccupe surtout de la deuxième : un appareil irréparable est jetable, même bien fait.",
              notes="Diapositive à photographier. Faire classer dans ces trois cases les "
                    "cas racontés par le groupe au déclencheur. L'exercice prend dix "
                    "minutes et vaut toute l'explication.")

    d.regle("Ce qu'un organisme public fait, et ne fait pas",
            "Nous ne prenons pas votre dossier en main : nous vous disons ce que vous pouvez faire.",
            precision="L'Office informe, il ne représente personne et il ne poursuit "
                      "personne à votre place. L'appel ne coûte rien, on y trouve les "
                      "modèles de lettre, et on repart en sachant si on a un recours ou "
                      "non. Pour beaucoup de gens, c'est justement ce qui manquait : "
                      "savoir que quelque chose était possible.",
            notes="Diapositive à photographier. Fait vérifié, pas élément du scénario. "
                  "Le distinguer clairement du reste : le nom de l'organisme et son "
                  "rôle sont réels.")

    d.vocabulaire('Vocabulaire', "Les mots de l'enquête", [
        ("un témoignage", "Le récit de ce qu'une personne a vécu elle-même et qu'elle raconte publiquement."),
        ("une enquête", "Un travail long qui cherche à établir ce qui s'est vraiment passé."),
        ("l'obsolescence programmée", "Le fait de décider d'avance qu'un objet cessera de fonctionner."),
        ("un organisme public", "Un service payé par l'État, où l'on peut s'informer sans rien débourser."),
    ], notes="Quatre mots seulement, mais « obsolescence programmée » est long et "
             "difficile à prononcer. Le découper en syllabes au tableau et le faire "
             "répéter lentement, trois fois.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'entrevue.", [
        ("Beaucoup de gens avaient jeté l'appareil avant d'appeler l'Office.", "vrai"),
        ("L'extrait du documentaire parle d'une entente sur les ampoules.", "vrai"),
        ("L'entente fixait une durée de vie maximale de dix mille heures.", "faux - mille heures"),
        ("C'est le manque de pièces de rechange qui la préoccupe le plus.", "vrai"),
        ("Elle nie que les petites créances soient longues.", "faux - elle le reconnaît"),
        ("L'Office prend le dossier de la personne en main à sa place.", "faux - il informe seulement"),
    ], corrige=True,
       notes="Le cinquième est le plus mal réussi : « je ne le nierai pas » est compris "
             "à l'envers par la moitié du groupe. Le reprendre en le reformulant "
             "positivement.")

    d.billet(
        "Laquelle des trois causes as-tu déjà rencontrée toi-même ?",
        exemples=[
            "Mal conçu, pas de pièce, ou trop cher à réparer ?",
            "Une phrase, avec l'appareil dont il s'agit.",
        ],
        notes="Deux minutes. Ces billets alimentent le jeu de rôle de E1 : chaque élève "
              "y arrive avec un cas réel, ce qui rend la discussion beaucoup plus "
              "vivante qu'avec le seul cas de Nadège.")

    return d.save(dossier)
