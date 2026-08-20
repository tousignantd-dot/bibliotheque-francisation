# -*- coding: utf-8 -*-
"""A3 · Retard, absence ou abandon ?
Bloc A · couleur framboise (vocabulaire) · 60 min.
Source : exercices `t1situ` et `t1img`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/assets/'
       'interactive/module-travail/images/')


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre='Retard, absence ou abandon ?',
        chapeau="Trois mots, trois démarches complètement différentes. Se tromper de mot "
                "au téléphone, c'est laisser croire qu'on ne reviendra jamais — ou "
                "l'inverse.",
        duree='60 minutes')

    d.titre(notes="Séance de vocabulaire à conséquences pratiques. Commencer par écrire "
                  "les trois mots au tableau et demander la différence. Les définitions "
                  "seront approximatives : c'est normal.")

    d.objectifs([
        "distinguer un retard, une absence et un abandon ;",
        "choisir le bon mot selon la situation ;",
        "savoir quelle démarche va avec chacun ;",
        "nommer une raison acceptable pour chacun des trois.",
    ])

    d.tableau('Analyse', "Trois mots, trois définitions",
              ['Le mot', 'Ce que c\'est', 'Combien de temps'],
              [["un retard", "arriver après un moment fixé", "quelques minutes ou heures"],
               ["une absence", "ne pas être là où on est attendu", "une journée ou plus"],
               ["un abandon", "renoncer à un cours ou à un travail", "définitif"]],
              cle=0,
              note="La différence n'est pas la gravité : c'est la durée et le retour. On "
                   "revient d'un retard et d'une absence, pas d'un abandon.",
              notes="Écrire au tableau : RETARD, on revient aujourd'hui. ABSENCE, on "
                    "revient plus tard. ABANDON, on ne revient pas.")

    d.regle('Le critère qui tranche',
            "Est-ce que je reviens ? Et quand ?",
            precision="Aujourd'hui, plus tard : c'est un retard. Un autre jour : c'est "
                      "une absence. Jamais : c'est un abandon. La question ne porte pas "
                      "sur la raison, mais sur le retour.",
            notes="Diapo centrale de la séance. Faire appliquer la question à chacune "
                  "des situations de l'exercice qui suit.")

    d.declencheur(
        'Mise en situation', "Que se passe-t-il, et de quoi s'agit-il ?",
        image=IMG + 'autobus-manque.jpg',
        pistes=[
            "Qu'est-ce que vous voyez exactement ?",
            "Est-ce que cette personne reviendra aujourd'hui ?",
            "Retard, absence ou abandon ?",
            "Qu'est-ce qu'elle devrait faire tout de suite ?",
        ],
        notes="Trois minutes. La réponse est « un retard » : le prochain autobus passe "
              "dans vingt minutes. La bonne réaction est d'appeler tout de suite, pas "
              "d'attendre d'être arrivé.")

    d.cartes('Analyse', "Quatre situations, trois mots", [
        ("Elle regarde son autobus partir",
         "Le prochain passe dans vingt minutes. Elle sera là aujourd'hui, en retard. "
         "C'est un RETARD : elle appelle et donne une heure d'arrivée."),
        ("La famille charge ses boîtes dans un camion",
         "Elle s'installe dans une autre ville, loin du centre. C'est un ABANDON : il "
         "faut remplir un formulaire et prévenir la direction."),
        ("Les valises sont prêtes près de la porte",
         "Départ demain matin pour trois semaines. C'est une ABSENCE longue : elle se "
         "prévient à l'avance, par écrit."),
        ("Il se repose après son opération",
         "Sa conjointe reste auprès de lui. C'est une ABSENCE : elle prévient chaque "
         "jour ou donne une date de retour."),
    ], notes="Faire deviner le mot avant de lire la seconde moitié de chaque carte. Le "
             "groupe se trompera surtout entre absence et abandon.")

    d.tableau('Analyse', "Quelle démarche pour quel cas",
              ['Le cas', 'Ce qu\'on fait'],
              [["un retard", "appeler ou écrire, donner une heure d'arrivée"],
               ["une absence courte", "prévenir le matin même, avant l'heure du cours"],
               ["une absence longue", "prévenir à l'avance, par écrit, avec les dates"],
               ["un abandon", "prévenir la direction et remplir un formulaire"]],
              cle=0,
              note="Dans les quatre cas, on prévient. Ce qui change, c'est le moment et "
                   "la forme.",
              notes="La colonne de droite est ce que les élèves doivent retenir. La faire "
                    "copier dans le cahier.")

    d.pratique('Pratique · 1 de 3', "Retard, absence ou abandon ?",
               "Posez la question : est-ce que je reviens, et quand ?", [
        ("Une personne reste à la maison parce que son conjoint vient d'être opéré.",
         "une absence — elle reviendra plus tard"),
        ("Une famille obtient un logement dans une autre ville, loin du centre.",
         "un abandon — elle ne reviendra pas"),
        ("Une personne part trois semaines voir sa famille dans son pays.",
         "une absence — longue, mais elle revient"),
        ("Une personne a manqué son autobus et attend le suivant.",
         "un retard — elle arrive aujourd'hui"),
        ("Une personne commence un emploi à temps plein et ne peut plus suivre le cours.",
         "un abandon — elle ne reviendra pas"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la question du retour. Le cinquième item "
             "est nouveau et se discute : certains diront « absence ».")

    d.piege("Le piège du mot « absence » pour tout",
            "Je serai absent. (alors qu'on déménage définitivement)",
            "Je dois abandonner le cours, je déménage.",
            "Dire « absence » quand c'est un abandon fait garder votre place dans le "
            "groupe pendant des semaines — une place qui manque à quelqu'un d'autre. Et "
            "cela empêche de récupérer une attestation pour les cours déjà suivis.",
            notes="Conséquence pratique importante : un abandon déclaré permet parfois "
                  "d'obtenir une attestation partielle. Un silence, non.")

    d.piege("Le piège du retard non annoncé",
            "Je vais arriver dans vingt minutes, ce n'est pas la peine d'appeler.",
            "J'appelle tout de suite pour dire que j'arrive à neuf heures vingt.",
            "Vingt minutes de retard non annoncées inquiètent inutilement, et surtout "
            "elles se remarquent. Vingt minutes annoncées ne se remarquent presque pas. "
            "L'appel prend trente secondes.",
            notes="Faire le calcul avec le groupe : combien de temps prend l'appel ? "
                  "Combien de temps dure le retard ? Le rapport est frappant.")

    d.pratique('Pratique · 2 de 3', "Nommez la situation et la démarche",
               "Le mot juste, puis ce qu'on fait.", [
        ("Votre voiture est tombée en panne sur l'autoroute.",
         "un retard — appeler tout de suite avec une heure d'arrivée"),
        ("Vous partez un mois dans votre pays d'origine.",
         "une absence longue — prévenir par écrit, avec les dates"),
        ("Vous commencez un emploi qui vous empêche de suivre le cours.",
         "un abandon — prévenir la direction et remplir le formulaire"),
        ("Votre enfant est malade et vous restez à la maison aujourd'hui.",
         "une absence — prévenir le matin même"),
    ], corrige=True,
       notes="Faire produire la première phrase de l'appel pour chaque cas : « Bonjour, "
             "je vous appelle pour vous dire que… »")

    d.pratique('Pratique · 3 de 3', "Une raison acceptable",
               "Pour chaque cas, nommez une raison qui s'explique en une phrase.", [
        ("Un retard", "un autobus manqué, une panne de voiture, une panne d'électricité"),
        ("Une absence d'une journée", "un enfant malade, un rendez-vous médical"),
        ("Une absence longue", "un voyage, une convalescence, un décès dans la famille"),
        ("Un abandon", "un déménagement, un nouvel emploi, un horaire incompatible"),
    ], corrige=True,
       notes="Insister : une raison s'explique en une phrase. Si elle demande cinq "
             "minutes, c'est qu'on se justifie au lieu d'expliquer.")

    d.billet(
        "Écrivez trois phrases : une pour un retard, une pour une absence, une pour un abandon.",
        exemples=[
            "Chaque phrase commence par « Je vous appelle pour vous dire que… ».",
            "Employez le bon mot dans chacune.",
        ],
        notes="Ramasser. Le mot employé montre si la distinction est acquise ; la suite "
              "de la phrase montre si la démarche l'est aussi.")

    return d.save(dossier)
