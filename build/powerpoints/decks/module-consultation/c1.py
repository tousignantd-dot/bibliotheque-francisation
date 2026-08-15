# -*- coding: utf-8 -*-
"""C1 · L'examen de la docteure Beaulieu.
Bloc C · couleur acier (compréhension orale) · 60 min.
Source : dialogue `t2` et exercice `t2vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="L'examen de la docteure Beaulieu",
        chapeau="Sept répliques, et tout y est : le diagnostic, l'arrêt de travail, la "
                "référence, les soins à la maison. Comprendre cette conversation, c'est "
                "savoir quoi faire en sortant.",
        duree='60 minutes')

    d.titre(notes="Ouverture du défi 2. Demander d'abord : que se passe-t-il après le "
                  "triage ? Beaucoup ne savent pas qu'on revoit une seconde personne.")

    d.objectifs([
        "comprendre un diagnostic dit en une phrase ;",
        "distinguer ce qui est grave de ce qui ne l'est pas ;",
        "retenir les consignes de soins données à l'oral ;",
        "savoir ce qu'est un billet de repos et une référence.",
    ])

    d.dialogue('Dialogue · 1 de 3', "Est-ce que ça fait mal quand j'appuie ici ?", [
        ("LA DOCTEURE", "Étendez la jambe, s'il vous plaît. Est-ce que ça fait mal quand "
                        "j'appuie ici ?", False),
        ("YANNICK", "Oui, juste là, sur le côté.", True),
        ("LA DOCTEURE", "Vous avez une inflammation du tendon. Ce n'est pas une "
                        "fracture, mais il ne faut pas forcer.", True),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="Passer l'audio du défi 2. Faire remarquer que la docteure dit d'abord ce "
             "que c'est, puis ce que ce n'est pas. C'est l'ordre habituel.")

    d.dialogue('Dialogue · 2 de 3', "Est-ce que je peux retourner travailler ?", [
        ("YANNICK", "Est-ce que je peux retourner travailler demain ?", True),
        ("LA DOCTEURE", "Pas tout de suite. Je vous donne un billet pour quatre jours de "
                        "repos et je vous réfère en physiothérapie.", True),
    ], notes="C'est la seule question que Yannick pose de tout le module. Faire remarquer "
             "au groupe qu'elle est excellente : c'est la question qui change sa semaine.")

    d.dialogue('Dialogue · 3 de 3', "Qu'est-ce que je fais en attendant ?", [
        ("YANNICK", "Qu'est-ce que je fais en attendant ?", True),
        ("LA DOCTEURE", "De la glace vingt minutes, trois fois par jour, et vous évitez "
                        "de soulever des charges.", True),
    ], notes="Deuxième question de Yannick, aussi bonne que la première. Faire compter "
             "les chiffres dans la réponse : vingt minutes, trois fois. Les chiffres "
             "sont ce qu'on oublie en premier.")

    d.tableau('Analyse', "Ce que la docteure dit, en quatre temps",
              ['Ce qu\'elle donne', 'Sa phrase'],
              [["Le diagnostic", "une inflammation du tendon"],
               ["Ce que ce n'est pas", "pas une fracture"],
               ["L'arrêt de travail", "un billet pour quatre jours"],
               ["La suite", "une référence en physiothérapie"],
               ["Les soins à la maison", "de la glace, et ne pas forcer"]],
              cle=0,
              note="Cinq informations en sept répliques. Un patient qui n'en retient que "
                   "trois sort avec la moitié de son traitement.",
              notes="Faire noter les cinq dans le cahier, en colonne. C'est la grille "
                    "d'écoute de toute consultation.")

    d.regle('La règle de la séance',
            "Un diagnostic tient en une phrase : ce que c'est, et ce que ce n'est pas.",
            precision="« Vous avez une inflammation du tendon. Ce n'est pas une "
                      "fracture. » La deuxième moitié est aussi importante que la "
                      "première : elle vous dit de quoi vous n'avez pas à vous inquiéter.",
            notes="Beaucoup d'élèves n'entendent que le mot difficile et manquent la "
                  "rassurance qui suit. Le dire explicitement.")

    d.vocabulaire('Vocabulaire', "Les mots de la consultation", [
        ("une inflammation", "Une réaction du corps qui cause douleur et enflure."),
        ("une fracture", "Un os cassé."),
        ("un billet de repos", "Un papier du médecin qui autorise à ne pas travailler."),
        ("référer", "Envoyer un patient vers un autre professionnel."),
        ("la physiothérapie", "Des soins avec des exercices pour retrouver ses mouvements."),
        ("forcer", "Faire un effort trop grand pour la partie du corps blessée."),
    ], notes="« Référer » est le verbe le plus utile et le moins connu. Le faire "
             "employer dans une phrase par chaque élève.")

    d.cartes('En apprendre plus', "Quatre choses à savoir sur le billet de repos", [
        ("À qui il sert",
         "À l'employeur. Il dit combien de jours vous ne pouvez pas travailler, sans "
         "dire pourquoi : votre diagnostic reste privé."),
        ("Il faut le demander",
         "Le médecin ne le propose pas toujours. Si vous en avez besoin, dites-le "
         "pendant la consultation, pas après."),
        ("Il peut être payant",
         "Certaines cliniques facturent le billet, parce que ce n'est pas un soin. "
         "Demandez le prix avant."),
        ("La référence est différente",
         "Une référence envoie vers un autre professionnel — physiothérapeute, "
         "spécialiste. Elle ne remplace pas le billet de repos."),
    ], notes="Ces quatre points sont du savoir pratique que personne n'enseigne. Prendre "
             "le temps de répondre aux questions : elles seront nombreuses.")

    d.pratique('Pratique · 1 de 3', "Vrai ou faux — l'examen",
               "Répondez sans relire le dialogue.", [
        ("La docteure demande à Yannick de plier la jambe.", "FAUX — de l'étendre"),
        ("Yannick a une fracture du genou.", "FAUX — une inflammation du tendon"),
        ("Il s'agit d'une inflammation du tendon.", "VRAI"),
        ("Yannick peut retourner travailler dès le lendemain.", "FAUX — quatre jours de repos"),
        ("Le billet de repos couvre quatre jours.", "VRAI"),
        ("La docteure le réfère en physiothérapie.", "VRAI"),
        ("Il doit appliquer de la glace trois fois par jour.", "VRAI"),
        ("Il peut continuer à soulever des charges lourdes.", "FAUX — il doit éviter"),
    ], corrige=True,
       notes="La première trompe presque tout le monde : « étendez » et « pliez » sont "
             "deux gestes opposés, et l'un des deux fait mal.")

    d.pratique('Pratique · 2 de 3', "Retrouvez la consigne exacte",
               "Les chiffres comptent : donnez-les.", [
        ("Combien de temps la glace, et combien de fois ?", "vingt minutes, trois fois par jour"),
        ("Combien de jours de repos ?", "quatre jours"),
        ("Vers qui la docteure le réfère-t-elle ?", "vers la physiothérapie"),
        ("Qu'est-ce qu'il doit éviter ?", "soulever des charges"),
    ], corrige=True,
       notes="Faire répondre sans regarder les notes. Les chiffres d'une consigne "
             "s'oublient en une heure si on ne les écrit pas — c'est le message.")

    d.piege("Le piège du mot difficile",
            "J'ai quelque chose au genou, je n'ai pas compris quoi.",
            "J'ai une inflammation du tendon, une tendinite.",
            "Quand un mot médical vous échappe, demandez-le tout de suite et écrivez-le. "
            "Vous en aurez besoin pour votre employeur, votre pharmacien et votre "
            "physiothérapeute. Un diagnostic qu'on ne sait pas nommer ne se transmet pas.",
            notes="Faire écrire le mot « tendinite » au tableau. Demander à chacun "
                  "d'écrire le nom d'un problème de santé qu'il a déjà eu — beaucoup ne "
                  "le savent qu'en langue maternelle.")

    d.pratique('Pratique · 3 de 3', "Qu'est-ce que vous demandez ?",
               "La docteure vient de parler. Quelle est votre question ?", [
        ("« Vous avez une inflammation du tendon. »",
         "Qu'est-ce que ça veut dire, exactement ?"),
        ("« Je vous donne un billet de repos. »",
         "Pour combien de jours ?"),
        ("« Je vous réfère en physiothérapie. »",
         "Est-ce que je dois prendre le rendez-vous moi-même ?"),
        ("« Évitez de forcer pendant quelques jours. »",
         "Est-ce que je peux marcher normalement ?"),
    ], corrige=True,
       notes="Ce sont les questions de B3 remises en situation. Faire remarquer au "
             "groupe qu'il les pose maintenant sans y penser.")

    d.billet(
        "Résumez la consultation de Yannick en quatre phrases.",
        exemples=[
            "Une pour le diagnostic, une pour l'arrêt de travail, une pour la suite, "
            "une pour les soins à la maison.",
            "Écrivez les chiffres : quatre jours, vingt minutes, trois fois.",
        ],
        notes="C'est l'exercice de compréhension le plus complet du module. Le ramasser "
              "et le corriger : il révèle exactement qui a suivi.")

    return d.save(dossier)
