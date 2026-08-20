# -*- coding: utf-8 -*-
"""C4 · Je me suis trompée de direction.
Bloc C · couleur acier · 55 min.
Source : dialogue `t2b`, exercice `t2b`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='acier',
        titre='Je me suis trompée de direction',
        chapeau="Nour a pris l'autobus dans le mauvais sens. Elle s'en est "
                "aperçue en dix minutes et elle a perdu vingt minutes au lieu "
                "d'une heure. Comment ? En regardant les numéros des rues.",
        duree='55 minutes')

    d.titre(notes="Séance courte et pratique. Elle clôt le bloc C sur une compétence "
                  "concrète : se rattraper quand on s'est trompé.")

    d.objectifs([
        "reconnaître les signes qu'on va dans la mauvaise direction ;",
        "savoir quoi faire dès qu'on s'en aperçoit ;",
        "demander au chauffeur avant de monter ;",
        "raconter au passé composé un déplacement raté.",
    ])

    d.declencheur(
        'Mise en situation', "Vous êtes dans l'autobus depuis dix minutes et quelque chose cloche.",
        pistes=[
            "Qu'est-ce qui vous ferait douter ?",
            "Est-ce que vous descendez tout de suite, ou vous attendez ?",
            "Où prenez-vous l'autobus dans l'autre sens ?",
            "À qui pouvez-vous demander avant de monter ?",
        ],
        notes="Cinq minutes. Presque tout le groupe aura vécu la situation. Récolter les "
              "stratégies : plusieurs sont excellentes et méritent d'être partagées.")

    d.dialogue('Dialogue · 1 de 2', "Comment elle s'en est aperçue", [
        ("NOUR", "Je me suis trompée hier. J'ai pris l'autobus dans le mauvais sens.", True),
        ("PATRICE", "Comment tu t'en es aperçue ?", False),
        ("NOUR", "Les noms des rues montaient au lieu de descendre. Au bout de dix minutes, j'ai compris.", True),
        ("PATRICE", "Tu as fait quoi ?", False),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Le signe est dans la troisième réplique : les numéros ou les noms qui vont "
             "dans le mauvais sens. C'est la règle vue en A4, appliquée en mouvement.")

    d.dialogue('Dialogue · 2 de 2', "Ce qu'elle a fait", [
        ("NOUR", "Je suis descendue au premier arrêt et j'ai traversé la rue. L'arrêt d'en face allait dans l'autre sens.", True),
        ("PATRICE", "C'est le bon réflexe. Le même numéro d'autobus, mais de l'autre côté de la rue.", True),
        ("NOUR", "J'ai perdu vingt minutes, mais je suis arrivée.", False),
        ("PATRICE", "La prochaine fois, demande au chauffeur avant de monter. Ils répondent toujours.", True),
    ], notes="Trois choses à retenir : descendre tout de suite, traverser la rue, et "
             "demander au chauffeur la prochaine fois. Les écrire au tableau.")

    d.cartes('Les trois signes', "Qu'on va dans le mauvais sens", [
        ("Les numéros vont à l'envers",
         "Vous cherchez le 500 et les numéros descendent vers le 200. C'est le signe le "
         "plus rapide : il se voit en deux minutes."),
        ("Le paysage change de nature",
         "Vous vous éloignez du centre alors que vous devriez vous en approcher — moins "
         "d'immeubles, plus d'espace."),
        ("Le temps passe et rien ne ressemble à ce qu'on vous a décrit",
         "Aucun des repères annoncés n'apparaît. Au bout de dix minutes sans repère, "
         "il y a un problème."),
    ], notes="Le premier signe est le plus fiable. Faire le lien explicite avec la règle "
             "des numéros vue en A4.")

    d.regle("Ce qu'il faut faire",
            "Descendez au premier arrêt et traversez la rue.",
            precision="L'arrêt d'en face porte le même numéro de ligne et va dans l'autre "
                      "sens. Vous ne payez pas deux fois si votre titre est encore valide. "
                      "Descendre tout de suite coûte cinq minutes ; attendre le terminus en "
                      "coûte quarante.",
            notes="Diapo à photographier. C'est la compétence pratique de la séance.")

    d.piege('Attendre en espérant',
            "Je vais attendre encore un peu, ça va peut-être revenir.",
            "Je descends au prochain arrêt et je traverse.",
            "Un autobus ne fait jamais demi-tour. Chaque minute passée à espérer est une "
            "minute qu'il faudra refaire dans l'autre sens. Le doute est déjà une raison "
            "suffisante pour descendre : vérifier depuis le trottoir ne coûte rien.",
            notes="C'est une leçon de comportement autant que de langue. Elle est utile.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Elle s'en est aperçue tout de suite en montant.", "faux — au bout de dix minutes"),
        ("Les noms des rues montaient au lieu de descendre.", "vrai"),
        ("Elle est restée jusqu'au terminus.", "faux — elle est descendue au premier arrêt"),
        ("Elle a traversé la rue pour prendre l'arrêt d'en face.", "vrai"),
        ("Le bon autobus portait un autre numéro.", "faux — le même numéro"),
        ("Patrice lui conseille de demander au chauffeur avant de monter.", "vrai"),
    ], corrige=True,
       notes="La cinquième ligne est celle à retenir : le même numéro dans les deux sens. "
             "C'est le rappel de B4.")

    d.cartes('La phrase à savoir', "Demander au chauffeur", [
        ("La question",
         "« Est-ce que vous allez vers Saint-Hubert ? » — courte, claire, et le chauffeur "
         "répond par oui ou non."),
        ("Le bon moment",
         "Avant de monter, par la porte avant, en montrant votre titre. Pas en cours de "
         "route."),
        ("Ce qu'on fait si c'est non",
         "On remercie, on descend, et on va à l'arrêt d'en face. Personne ne s'en formalise."),
    ], notes="Faire répéter la question par tout le groupe, deux fois. C'est une phrase "
             "qu'ils emploieront la semaine même.")

    d.billet(
        "Racontez en cinq phrases une fois où vous vous êtes trompé de chemin.",
        exemples=[
            "Où alliez-vous ? Comment vous en êtes-vous aperçu ? Qu'avez-vous fait ?",
            "Employez le passé composé.",
        ],
        notes="Sujet léger et rassembleur : tout le monde a une histoire. Excellente "
              "préparation à la production orale de E1.")

    return d.save(dossier)
