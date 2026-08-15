# -*- coding: utf-8 -*-
"""A1 · Le genou de Yannick — mise en situation.
Bloc A « Je découvre » · couleur teal · 75 min.
Source du module : dialogue `prep`, exercices `prVocab` et `pr1`, cartes mémoire.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='teal',
        titre='Le genou de Yannick',
        chapeau="Yannick finit son quart à l'entrepôt à minuit. Au réveil, son genou "
                "droit est enflé et chaud. L'urgence ou la clinique sans rendez-vous ? "
                "La réponse n'est pas la même selon ce qu'on a.",
        duree='75 minutes')

    d.titre(notes="Ouverture du module 1. Ne pas donner le vocabulaire tout de suite : "
                  "la séance part d'une situation, pas d'une liste de mots. Écrire au "
                  "tableau : entrepôt, quart de nuit, genou droit.")

    d.objectifs([
        "décrire une douleur avec le mot précis, pas seulement « j'ai mal » ;",
        "dire depuis quand la douleur dure et ce qui l'aggrave ;",
        "distinguer ce qui relève de l'urgence de ce qui relève de la clinique ;",
        "savoir ce qu'il faut apporter avant de partir consulter.",
    ], notes="Lire chaque objectif à voix haute et prévenir qu'on y revient au billet "
             "de sortie, à la fin de la séance.")

    d.declencheur(
        'Mise en situation', "Vous vous réveillez avec un genou enflé. Où allez-vous ?",
        pistes=[
            "Est-ce que vous iriez à l'urgence, à la clinique, ou nulle part ?",
            "Qu'est-ce qui vous ferait changer d'idée : la fièvre ? le sang ? la douleur ?",
            "Combien de temps attendriez-vous avant de consulter ?",
            "Qu'est-ce que vous apporteriez avec vous ?",
        ],
        notes="Cinq minutes en grand groupe, sans rien corriger. Noter au tableau les "
              "mots que le groupe emploie : on les comparera aux mots justes à la diapo "
              "du vocabulaire. Beaucoup diront « l'hôpital » pour tout — c'est justement "
              "ce que la séance va nuancer.")

    d.cartes('La situation', "Ce qu'on sait de Yannick", [
        ("Ce qu'il fait",
         "Manutentionnaire dans un entrepôt. Il soulève des boîtes toute la soirée et "
         "son quart de travail se termine à minuit."),
        ("Ce qui ne va pas",
         "Le genou droit est enflé et chaud au réveil. Il n'a rien senti sur le coup, "
         "pendant le travail."),
        ("Ce qu'il n'a pas",
         "Pas de fièvre, pas de rougeur, pas de coup précis dont il se souvienne. Ces "
         "trois absences comptent autant que les symptômes."),
        ("À qui il en parle",
         "À Rosalie, sa collègue, avant d'appeler qui que ce soit. Elle l'aide à choisir "
         "où aller."),
    ], notes="Insister sur la troisième carte. Ce qu'on n'a PAS oriente le choix du "
             "service autant que ce qu'on a : c'est le raisonnement de toute la séance.")

    # ── le dialogue, en trois temps ────────────────────────────────
    d.dialogue('Dialogue · 1 de 3', "Je me suis réveillé avec le genou enflé", [
        ("YANNICK", "Rosalie, je me suis réveillé ce matin avec le genou tout enflé. "
                    "J'ai fini mon quart à l'entrepôt à minuit et je n'avais rien senti "
                    "sur le coup.", True),
        ("ROSALIE", "Est-ce que tu peux marcher dessus ?", False),
        ("YANNICK", "Un peu, mais ça élance dès que je plie la jambe.", True),
        ("ROSALIE", "Tu n'as pas de fièvre ? La peau n'est pas rouge ?", False),
        ("YANNICK", "Non, seulement enflé et chaud.", False),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="Passer l'audio du module (section « Je découvre ») avant d'afficher le "
             "texte. Les deux répliques teintées portent la description : le moment, "
             "puis le geste qui déclenche la douleur.")

    d.dialogue('Dialogue · 2 de 3', "Ce n'est pas un cas pour l'urgence", [
        ("ROSALIE", "Alors ce n'est pas un cas pour l'urgence. Va plutôt à la clinique "
                    "sans rendez-vous du quartier : elle ouvre à sept heures et tu vas "
                    "passer plus vite.", True),
        ("YANNICK", "Je pensais appeler mon médecin de famille.", False),
        ("ROSALIE", "Tu aurais un rendez-vous dans trois semaines. Pour une blessure "
                    "comme celle-là, il faut voir quelqu'un aujourd'hui.", True),
    ], notes="Faire remarquer que Rosalie décide APRÈS avoir posé deux questions, pas "
             "avant. Demander au groupe : quelles étaient les deux questions ?")

    d.dialogue('Dialogue · 3 de 3', "Je prends ma carte et j'y vais", [
        ("YANNICK", "Tu as raison. Je prends ma carte d'assurance maladie et j'y vais "
                    "tout de suite.", True),
    ], notes="Une seule réplique, mais elle contient le geste pratique de la séance : "
             "la carte d'assurance maladie. Demander qui l'a sur soi en ce moment.")

    d.tableau('Analyse', "Ce que Yannick dit, et pourquoi c'est utile",
              ['Sa phrase', 'Ce que ça donne au soignant'],
              [["« réveillé avec le genou enflé »", "le moment d'apparition"],
               ["« j'ai fini mon quart à minuit »", "l'activité qui précède"],
               ["« rien senti sur le coup »", "pas de choc brutal"],
               ["« ça élance quand je plie »", "le geste qui déclenche"],
               ["« pas de fièvre, pas de rougeur »", "ce qui écarte l'infection"]],
              cle=1,
              note="Chaque phrase courte répond d'avance à une question du soignant.",
              notes="Faire chercher au groupe la question correspondant à chaque ligne. "
                    "C'est l'exercice de la séance B3, qu'on amorce ici sans le nommer.")

    d.regle('La règle de la séance',
            "On ne dit pas seulement où on a mal : on dit depuis quand et ce qui aggrave.",
            precision="Trois informations suffisent pour être compris d'une infirmière au "
                      "triage : l'endroit, le moment d'apparition, le geste qui fait mal. "
                      "Tout le reste, elle le demandera.",
            notes="Écrire les trois mots au tableau — ENDROIT · DEPUIS QUAND · QUEL GESTE — "
                  "et les y laisser jusqu'à la fin du module.")

    d.vocabulaire('Vocabulaire · 1 de 2', "Le corps qui fait mal", [
        ("enflé", "Qui a augmenté de volume à cause d'une blessure."),
        ("élancer", "Faire une douleur vive et répétée, par à-coups."),
        ("une inflammation", "Une réaction du corps qui cause douleur et enflure."),
        ("un tendon", "La partie qui attache un muscle à un os."),
        ("soulever une charge", "Lever un objet lourd."),
        ("un quart de travail", "La période de travail d'un employé."),
    ], notes="Faire prononcer chaque mot. « Élancer » est le plus utile et le moins connu : "
             "faire produire une phrase avec, en lien avec une douleur réelle.")

    d.vocabulaire('Vocabulaire · 2 de 2', "Où aller, quoi apporter", [
        ("une clinique sans rendez-vous", "Une clinique où on consulte sans avoir réservé."),
        ("le triage", "L'étape où une infirmière évalue la gravité des cas."),
        ("une carte d'assurance maladie", "La carte qui donne accès aux soins gratuits."),
        ("un billet de repos", "Un papier du médecin qui autorise à ne pas travailler."),
        ("la physiothérapie", "Des soins avec des exercices pour retrouver ses mouvements."),
        ("une ordonnance", "Le papier du médecin pour obtenir un médicament."),
    ], notes="Ces six mots reviennent dans les quinze séances suivantes. Vérifier que "
             "chacun sait où se trouve sa carte d'assurance maladie et si elle est valide.")

    d.pratique('Pratique', 'Vrai ou faux — le genou de Yannick',
               "Répondez sans relire le dialogue.", [
        ("Yannick s'est blessé pendant un match de soccer.", "FAUX — au travail, à l'entrepôt"),
        ("Il a fini son quart de travail à minuit.", "VRAI"),
        ("Son genou est enflé et chaud.", "VRAI"),
        ("Yannick fait de la fièvre.", "FAUX — il n'en a pas"),
        ("Rosalie lui conseille d'aller à l'urgence.", "FAUX — à la clinique sans rendez-vous"),
        ("La clinique sans rendez-vous ouvre à sept heures.", "VRAI"),
        ("Avec son médecin de famille, il attendrait trois semaines.", "VRAI"),
        ("La douleur augmente quand il plie la jambe.", "VRAI"),
    ], corrige=True, cols=1,
       notes="La cinquième est celle qui trompe le plus : beaucoup entendent « urgence » "
             "dans le dialogue sans entendre la négation qui la précède.")

    d.piege("Le piège du premier jour",
            "J'ai mal.",
            "J'ai le genou droit enflé depuis cette nuit.",
            "« J'ai mal » ne dit ni l'endroit, ni le côté, ni le moment. L'infirmière "
            "devra poser quatre questions pour arriver là où une seule phrase aurait "
            "suffi. Ce n'est pas une question de politesse : c'est du temps de "
            "consultation gagné.",
            notes="Faire reformuler oralement par trois ou quatre élèves : « j'ai mal » → "
                  "une phrase complète. Ne pas corriger la grammaire à cette étape, "
                  "seulement la précision.")

    d.billet(
        "Décrivez une douleur — la vôtre ou une douleur inventée — en une seule phrase.",
        exemples=[
            "Nommez l'endroit, dites depuis quand, dites quel geste fait mal.",
            "Exemple : « J'ai l'épaule gauche raide depuis trois jours, ça fait mal quand "
            "je lève le bras. »",
        ],
        notes="Ramasser les billets. Ils servent de point de départ à la séance B1, où "
              "la même phrase sera dite à l'infirmière du triage.")

    return d.save(dossier)
