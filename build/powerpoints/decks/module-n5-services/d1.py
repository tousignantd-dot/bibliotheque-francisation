# -*- coding: utf-8 -*-
"""D1 · Au guichet, billet B-47.
Bloc D « Défi 3 · Le guichet » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3etapes`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-services/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Au guichet, billet B-47",
        chapeau="On arrive rarement les mains vides : on a déjà essayé en "
                "ligne, déjà téléphoné, déjà attendu. Il faut raconter ce "
                "qui s'est passé avant, comprendre ce qui manque, et "
                "repartir avec la réponse.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 3. Ramasser le devoir C4 : combien de champs "
                  "obligatoires chacun a-t-il comptés ? Quels mots inconnus ? Cinq minutes "
                  "qui font le pont avec la séance d'aujourd'hui.")

    d.objectifs([
        "expliquer au comptoir une démarche déjà commencée ;",
        "répondre exactement à une question fermée ;",
        "écouter ce qui manque au dossier ;",
        "connaître les six étapes d'une démarche administrative.",
    ])

    d.declencheur(
        'Observation', "Vous avez le billet B-47. Que direz-vous en vous assoyant ?",
        image=IMG + 'billet-file-attente.jpg',
        pistes=[
            "Par quoi commencez-vous ?",
            "Racontez-vous vos trois soirées devant le formulaire ?",
            "Que doit savoir le préposé en dix secondes ?",
            "Qu'avez-vous apporté ?",
        ],
        notes="Beaucoup d'élèves commencent par raconter leur frustration. C'est humain, "
              "et c'est ce qui allonge l'échange. Laisser dire, sans corriger : le "
              "dialogue s'en charge.")

    d.dialogue('Dialogue · 1 de 3', "Dire d'où on part", [
        ("VOIX", "Numéro B quarante-sept, au comptoir trois.", True),
        ("GAÉTAN", "Bonjour ! Vous pouvez vous asseoir. Qu'est-ce qui vous amène ?", True),
        ("LEÏLA", "Bonjour. Je viens pour ma carte de citoyenne. J'ai commencé la "
                  "demande en ligne, mais elle n'a pas fonctionné.", True),
        ("GAÉTAN", "Elle n'a pas fonctionné comment ? Elle a été refusée, ou elle "
                   "est restée bloquée ?", False),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Deux phrases de Leïla, et Gaétan sait où reprendre. Faire compter les mots : "
             "vingt-quatre. C'est tout ce qu'il fallait.")

    d.dialogue('Dialogue · 2 de 3', "Ce n'était pas votre faute", [
        ("LEÏLA", "Elle est restée bloquée à la dernière page. J'avais rempli tout "
                  "le formulaire et il me redemandait mon adresse.", True),
        ("GAÉTAN", "Ah, ça arrive quand l'adresse est écrite autrement que dans "
                   "notre système. Vous aviez mis « appartement » au long ?", True),
        ("LEÏLA", "Oui, j'avais écrit « appartement 3 ».", True),
        ("GAÉTAN", "C'est ça. Le système veut « app. 3 ». Ce n'est pas votre "
                   "faute, c'est une vraie faiblesse du formulaire.", True),
    ], notes="Le lien avec la séance C4 est direct : les élèves l'ont appris avant Leïla. "
             "Le faire remarquer, c'est valorisant et ça montre que le module tient "
             "ensemble.")

    d.dialogue('Dialogue · 3 de 3', "Ce qu'il faut, et ce qui manque parfois", [
        ("GAÉTAN", "Il faut que vous me montriez deux pièces : une avec votre "
                   "photo, et une avec votre adresse.", True),
        ("LEÏLA", "J'ai mon permis de conduire, et j'ai apporté mon bail.", True),
        ("GAÉTAN", "Alors il fait la job. Ce qui manque parfois, c'est une facture "
                   "trop vieille — il faut qu'elle date de moins de trois mois.", True),
        ("LEÏLA", "Dix minutes ! J'ai passé trois soirées sur le site Web.", True),
    ], notes="« Il faut que vous me montriez » et « il faut qu'elle date » : deux "
             "subjonctifs, travaillés en D2. Les souligner au passage sans les expliquer.")

    d.regle("Deux pièces, jamais une",
            "Une avec votre photo, une avec votre adresse — ce sont deux papiers différents.",
            precision="Une pièce d'identité dit qui vous êtes ; une preuve de résidence "
                      "dit où vous habitez. Un permis de conduire fait souvent les deux, "
                      "mais pas toujours. Et une facture doit dater de moins de trois mois.",
            notes="Diapositive à photographier. La confusion entre ces deux papiers est la "
                  "cause la plus fréquente d'un deuxième déplacement.")

    d.tableau('Les six étapes · 1 de 2', "Avant et pendant",
              ['Étape', 'Ce qu\'on y fait'],
              [["1. Avant de commencer", "lire la page et son encadré"],
               ["2. Réunir ce qu'il faut", "les pièces, et vérifier leur date"],
               ["3. Faire la demande", "en ligne, par téléphone ou au comptoir"]],
              cle=0,
              note="L'étape 1 est celle qu'on saute, et elle décide des cinq autres.",
              notes="Diapositive à photographier. Faire remarquer que le module a suivi "
                    "cet ordre : le défi 2 lisait la page, le défi 1 téléphonait.")

    d.tableau('Les six étapes · 2 de 2', "Après",
              ['Étape', 'Ce qu\'on y fait'],
              [["4. Garder une trace", "le numéro de requête et la date"],
               ["5. Attendre le délai", "en jours ouvrables, pas en jours de calendrier"],
               ["6. Relancer", "rappeler ou écrire, avec le numéro de requête"]],
              cle=0,
              note="Les trois dernières sont celles que « Je me lance » fait travailler.",
              notes="Diapositive à photographier. C'est la synthèse du module ; la garder "
                    "affichée jusqu'à la fin du bloc E.")

    d.cartes("Répondre à un guichet", "Quatre gestes", [
        ("Dire d'où vous partez",
         "« J'ai commencé la demande en ligne, mais elle n'a pas fonctionné. »"),
        ("Décrire la panne, pas la raconter",
         "« Elle est restée bloquée à la dernière page. » Le lieu, pas la chronologie."),
        ("Répondre exactement à la question",
         "« Refusée, ou bloquée ? » — « Bloquée. » Un guichet fonctionne par tri."),
        ("Repartir avec une suite claire",
         "Réglé, ou bien vous savez quoi apporter et quand revenir. Jamais entre les deux."),
    ], notes="La troisième carte est difficile : répondre en un mot semble impoli à "
             "beaucoup d'élèves. Expliquer que c'est au contraire ce qui aide.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Sa demande en ligne avait été refusée.", "faux — elle était bloquée"),
        ("Le formulaire buttait sur « appartement » écrit au long.", "vrai"),
        ("Gaétan dit que c'est une faiblesse du formulaire.", "vrai"),
        ("Il faut deux pièces : une avec photo, une avec l'adresse.", "vrai"),
        ("Le bail de Leïla est refusé parce qu'il porte deux noms.", "faux — il convient"),
        ("Une facture doit dater de moins de trois mois.", "vrai"),
        ("Leïla doit revenir la semaine suivante.", "faux — la carte s'imprime sur place"),
    ], corrige=True,
       notes="Faire justifier chaque « faux ». La dernière est celle qui frappe : trois "
             "soirées en ligne contre dix minutes au comptoir.")

    # `capture` n'existe que dans theme.Deck : les présentations la portent, les
    # fiches imprimées non (build/powerpoints/fiche.py n'a pas la méthode). Une
    # fiche noir et blanc n'a de toute façon rien à faire d'une capture d'écran.
    if hasattr(d, 'capture'):
        d.capture('t3etapes', "L'exercice à l'écran",
                  consigne="Reliez chaque étape à ce qu'on y fait.",
                  notes="Dix minutes de travail individuel, en clôture de séance. "
                        "L'exercice reprend le tableau des six étapes dans le désordre.")

    d.billet(
        "Préparez la première phrase que vous diriez à un guichet.",
        exemples=[
            "Une démarche vraie, en cours ou passée. Deux phrases au maximum.",
            "Notez aussi les deux pièces que vous apporteriez.",
        ],
        notes="Devoir court qui prépare le jeu de rôle de E1. Insister sur la limite de "
              "deux phrases : c'est la contrainte qui fait travailler.")

    return d.save(dossier)
