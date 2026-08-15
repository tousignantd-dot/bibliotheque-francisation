# -*- coding: utf-8 -*-
"""A3 · 911, 811 ou clinique ?
Bloc A · couleur acier (compréhension) · 60 min.
Source : exercice `prOu` — choisir le bon service selon la gravité.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='acier',
        titre='911, 811 ou clinique ?',
        chapeau="Trois numéros, trois usages, et une seule question pour choisir : "
                "est-ce que la vie est en danger maintenant ? Tout le reste en découle.",
        duree='60 minutes')

    d.titre(notes="Séance de repérage dans les services d'urgence. Demander d'entrée qui "
                  "a déjà composé le 911, et pourquoi. Les réponses orientent la séance.")

    d.objectifs([
        "savoir quand composer le 911 et quand ne pas le faire ;",
        "savoir ce que fait le 811 et à quoi il sert ;",
        "reconnaître les signes qui ne peuvent pas attendre ;",
        "dire au téléphone les informations qu'on va vous demander.",
    ])

    d.regle('La question qui décide',
            "Est-ce que la vie est en danger maintenant ?",
            precision="Si oui : le 911, sans hésiter et sans se demander si on dérange. "
                      "Si non, mais qu'on ne sait pas quoi faire : le 811. Si non, et "
                      "qu'il faut voir quelqu'un aujourd'hui : la clinique ou l'urgence.",
            notes="Écrire la question au tableau et l'y laisser toute la séance. C'est "
                  "elle qu'on appliquera à chacune des situations de l'exercice.")

    d.cartes('Analyse', "Trois numéros, trois usages", [
        ("Le 911 · la vie en danger",
         "Une personne ne respire plus, a perdu connaissance, saigne abondamment, ou a "
         "une douleur à la poitrine. On répond en quelques secondes et une ambulance "
         "part si nécessaire."),
        ("Le 811 · Info-Santé",
         "Une infirmière répond jour et nuit, gratuitement, dans plusieurs langues. Elle "
         "dit quoi faire et vers quel service aller. C'est le numéro du doute."),
        ("La clinique sans rendez-vous",
         "Pour ce qui doit être vu aujourd'hui sans être dangereux : une coupure, une "
         "brûlure légère, une fièvre qui dure."),
        ("L'urgence de l'hôpital",
         "Pour ce qui est sérieux sans mettre la vie en danger immédiatement : une "
         "brûlure avec cloques, une plaie profonde, une fracture possible."),
    ], notes="Insister sur la deuxième carte : « dans plusieurs langues » est une "
             "information que peu de gens connaissent et qui change tout pour un "
             "nouvel arrivant.")

    d.tableau('Analyse', "Cinq signes qui appellent le 911",
              ['Le signe', 'Pourquoi'],
              [["la personne ne respire plus", "quelques minutes suffisent"],
               ["elle a perdu connaissance", "la cause est inconnue"],
               ["douleur à la poitrine et au bras", "le cœur peut être en cause"],
               ["saignement qu'on n'arrête pas", "la perte de sang s'accélère"],
               ["brûlure blanche ou très étendue", "les tissus sont détruits"]],
              cle=0,
              note="Ces cinq signes ne se discutent pas. On compose le 911, même en "
                   "pleine nuit, même si on n'est pas certain.",
              notes="Faire apprendre ces cinq par cœur. C'est la seule liste du module "
                    "qui doit être sue sans hésitation.")

    d.tableau('Analyse', "Ce qu'on vous demandera au téléphone",
              ['La question', 'Votre réponse'],
              [["Où êtes-vous ?", "l'adresse, l'étage, comment entrer"],
               ["Qu'est-ce qui s'est passé ?", "en une phrase, au passé"],
               ["La personne est-elle consciente ?", "oui ou non"],
               ["Respire-t-elle ?", "oui ou non"],
               ["Quel est votre numéro ?", "pour qu'on vous rappelle"]],
              cle=0,
              notes="L'adresse en premier : c'est la seule information qui permet "
                    "d'envoyer les secours même si l'appel se coupe. Le dire "
                    "explicitement.")

    d.regle("La règle du téléphone",
            "L'adresse d'abord. Ne raccrochez jamais avant qu'on vous le dise.",
            precision="La personne au bout du fil vous guidera : elle peut vous dire "
                      "comment comprimer une plaie ou comment placer quelqu'un qui a "
                      "perdu connaissance. Rester en ligne fait partie des premiers "
                      "soins.",
            notes="Beaucoup de gens raccrochent dès qu'ils ont donné l'information, "
                  "croyant libérer la ligne. Corriger cette idée clairement.")

    d.pratique('Pratique · 1 de 3', "911 ou 811 ?",
               "Le 911 est réservé aux cas où la vie est en danger.", [
        ("Une personne ne respire plus.", "911"),
        ("Un enfant a une petite coupure au doigt et vous hésitez sur les soins.", "811"),
        ("Un homme a une douleur forte à la poitrine et au bras gauche.", "911"),
        ("Vous vous demandez si une fièvre de 38 degrés est inquiétante.", "811"),
        ("Une personne a perdu connaissance et ne répond pas.", "911"),
        ("Vous voulez savoir quoi faire pour une brûlure avec des cloques.", "811"),
    ], corrige=True,
       notes="Corriger en revenant chaque fois à la question du début : est-ce que la vie "
             "est en danger maintenant ? Ne jamais corriger par l'habitude.")

    d.piege("Le piège de la peur de déranger",
            "Je ne veux pas appeler le 911 pour rien.",
            "Si la vie peut être en danger, on appelle.",
            "Les répartiteurs préfèrent cent appels inutiles à un appel qui n'a pas été "
            "fait. Personne ne vous reprochera d'avoir appelé, et le service est "
            "gratuit. Hésiter coûte des minutes qui ne se rattrapent pas.",
            notes="Point culturel important pour un groupe de nouveaux arrivants, qui "
                  "viennent parfois de pays où les secours se font payer ou ne viennent "
                  "pas. Le dire explicitement.")

    d.piege("Le piège de l'ambulance payante",
            "L'ambulance coûte cher, on va y aller en auto.",
            "Si c'est un cas de 911, on appelle l'ambulance.",
            "Le transport en ambulance est facturé au Québec, c'est vrai. Mais les soins "
            "commencent dans le véhicule, et une personne qui perd connaissance en auto "
            "n'a personne pour l'aider. Le coût ne doit jamais entrer dans la décision "
            "quand la vie est en jeu.",
            notes="Question fréquente et légitime. Répondre honnêtement — oui, c'est "
                  "facturé — puis expliquer pourquoi cela ne change pas la décision.")

    d.pratique('Pratique · 2 de 3', "Quel service, et pourquoi ?",
               "Nommez le service et donnez la raison en une phrase.", [
        ("Votre collègue s'est brûlé le bras, il y a des cloques.",
         "l'urgence — des cloques veulent dire deuxième degré"),
        ("Vous ne savez pas si votre enfant doit voir un médecin.",
         "le 811 — c'est le numéro du doute"),
        ("Une personne est tombée et ne se réveille pas.",
         "le 911 — perte de connaissance"),
        ("Vous avez une coupure qui a saigné dix minutes puis s'est arrêtée.",
         "la clinique sans rendez-vous — aujourd'hui, sans danger"),
    ], corrige=True,
       notes="Faire donner la raison avant le numéro. C'est le raisonnement qu'on "
             "évalue, pas la mémoire.")

    d.pratique('Pratique · 3 de 3', "L'appel au 911, en cinq réponses",
               "Un accident vient d'arriver au travail. Répondez au répartiteur.", [
        ("Où êtes-vous ?", "Au 1250, rue Principale, dans la cuisine du restaurant."),
        ("Qu'est-ce qui s'est passé ?", "Un collègue est tombé et s'est cogné la tête."),
        ("Est-il conscient ?", "Non, il ne répond pas."),
        ("Est-ce qu'il respire ?", "Oui, je vois sa poitrine bouger."),
        ("Votre numéro ?", "C'est le 514 555-0142."),
    ], corrige=True,
       notes="Faire jouer la scène à deux, debout, avec un téléphone dans la main. "
             "La position debout change la voix et le rythme : c'est voulu.")

    d.billet(
        "Écrivez les deux numéros et, pour chacun, une situation où vous l'utiliseriez.",
        exemples=[
            "Le numéro, puis la situation en une phrase.",
            "Notez aussi votre adresse complète : c'est la première chose qu'on vous "
            "demandera.",
        ],
        notes="Vérifier que chacun sait dire son adresse complète en français, avec le "
              "numéro d'appartement. Beaucoup ne l'ont jamais dit à voix haute.")

    return d.save(dossier)
