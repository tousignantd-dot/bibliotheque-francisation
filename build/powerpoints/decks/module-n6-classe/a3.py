# -*- coding: utf-8 -*-
"""A3 · L'annonce du lundi matin
Bloc A « Je découvre » · couleur acier · 75 min. Compréhension orale.
Source du module : dialogue `prep` et exercice `prVF`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='acier',
        titre="L'annonce du lundi matin",
        chapeau="Une enseignante annonce un travail de recherche. En trois "
                "minutes, elle donne le nombre de personnes, le nombre de "
                "sources, la durée de l'exposé et une échéance. Tout est dit "
                "une fois.",
        duree='75 minutes')

    d.titre(notes="Séance d'écoute. Le dialogue fait vingt et une répliques : "
                  "prévoir trois écoutes complètes et ne pas s'excuser de la "
                  "longueur — au niveau 6, le programme vise des discours "
                  "détaillés et structurés.")

    d.objectifs([
        "suivre une annonce longue sans en perdre le fil ;",
        "relever les chiffres qu'on ne dit qu'une fois ;",
        "reconnaître ce qui est une consigne et ce qui est un conseil ;",
        "comprendre pourquoi trois sources valent mieux qu'une.",
    ], notes="La distinction consigne / conseil est le point difficile : "
             "« prenez celui qui vous fâche » est un conseil, « trois sources "
             "au minimum » est une obligation.")

    d.declencheur(
        'Avant d\'écouter', "Que feriez-vous en premier, si on vous annonçait ça ce matin ?",
        pistes=[
            "Choisir le sujet ? Chercher tout de suite ?",
            "Avec qui vous mettriez-vous, et pourquoi ?",
            "Qu'est-ce que vous voudriez savoir avant de commencer ?",
        ],
        notes="Recueillir trois réponses, les noter au tableau, et y revenir "
              "à la fin de la séance. Presque toujours, personne ne propose "
              "de lire la consigne au complet.")

    d.dialogue('Écoute 1', "L'annonce, premières répliques", [
        ("MIREILLE", "Avant qu'on ouvre le cahier, j'ai quelque chose à vous annoncer, et j'aime autant vous le dire tout de suite : ça va durer trois semaines.", False),
        ("MARISOL", "Trois semaines de quoi, madame ?", False),
        ("MIREILLE", "D'un travail de recherche. En équipe de trois. Chaque équipe choisit un sujet dans une liste, cherche de l'information, écrit un court texte et vient présenter ce qu'elle a trouvé devant la classe.", True),
        ("YOUSSEF", "Un exposé ? Devant tout le monde ?", False),
    ], consigne="Première écoute : ne rien noter, seulement écouter.",
       notes="Quatre répliques par page : au-delà, le corps du texte descend "
             "au plancher et la diapositive ne se lit plus du fond de la "
             "classe.")

    d.dialogue('Écoute 2', "Ce qu'on attend vraiment", [
        ("MIREILLE", "Un compte rendu, plutôt. Cinq minutes par équipe. Ce n'est pas un concours : personne ne va vous demander d'être drôle. On veut savoir ce que vous avez trouvé et d'où ça vient.", True),
        ("MARISOL", "Et le sujet, on le choisit vraiment ? Ou bien il est déjà choisi et vous nous laissez croire qu'on choisit ?", False),
        ("MIREILLE", "Vous choisissez vraiment. Il y a huit sujets sur la feuille et ils touchent tous la ville : la collecte des matières organiques, le transport en commun, les bibliothèques de quartier, l'eau potable…", False),
        ("MIREILLE", "Prenez celui qui vous fâche ou celui qui vous intrigue, ça revient au même.", False),
    ], consigne="Deuxième écoute : notez les chiffres.",
       notes="Faire relever à l'oral : trois semaines, trois personnes, huit "
             "sujets, cinq minutes. Quatre chiffres, tous dits une seule "
             "fois.")

    d.dialogue('Écoute 3', "Les sources, et ce qu'on en fait", [
        ("MIREILLE", "Vous aurez trois sources au minimum, et pas trois fois la même. Madame Ouimet, à la bibliothèque du centre, vous montrera comment on juge une source.", True),
        ("YOUSSEF", "Et si les trois ne disent pas la même chose ?", False),
        ("MIREILLE", "Alors vous aurez enfin quelque chose à écrire. Un travail où tout le monde est d'accord n'apprend rien à personne.", True),
        ("MIREILLE", "Ce que je veux lire, c'est : voici ce que dit l'un, voici ce que dit l'autre, et voici pourquoi ils ne s'entendent pas.", False),
    ], consigne="Troisième écoute : qu'est-ce qui est demandé, exactement ?",
       notes="C'est le cœur du module. Les sources qui se contredisent ne "
             "sont pas un problème à résoudre : ce sont elles qui donnent au "
             "travail quelque chose à dire.")

    d.tableau('Analyse', "Consigne ou conseil ?",
              ['Ce qui est dit', 'Ce que ça vaut'],
              [["équipe de trois", "consigne : ce n'est pas négociable"],
               ["trois sources au moins", "consigne : c'est un minimum chiffré"],
               ["cinq minutes par équipe", "consigne : le temps est compté"],
               ["prenez ce qui vous fâche", "conseil : personne ne vérifiera"],
               ["lisez la feuille ce soir", "conseil, mais celui qui coûte le plus cher"]],
              cle=1,
              note="Un conseil n'oblige à rien — et c'est pourtant celui-là qui décide de la note.",
              notes="Diapositive à photographier. Demander pourquoi le dernier "
                    "conseil coûte cher : la réponse arrive à la séance B1.")

    d.pratique('Pratique', "Vrai ou faux",
               "Réécoutez au besoin, puis répondez.", [
        ("Le travail de recherche se fait seul.", "faux : en équipe de trois"),
        ("Chaque équipe choisit son sujet dans une liste de huit.", "vrai"),
        ("Il faut trois sources, et pas trois fois la même.", "vrai"),
        ("Si les sources se contredisent, il faut en enlever une.", "faux : il faut l'écrire"),
        ("La grille d'évaluation est donnée avec la consigne.", "vrai"),
        ("Le compte rendu dure vingt minutes.", "faux : cinq minutes"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `prVF` du module. La quatrième affirmation est "
             "celle qui divise : y revenir même si le groupe répond juste.")

    d.billet(
        "Écris la phrase de l'annonce qui te semble la plus importante.",
        exemples=[
            "Puis, en dessous : pourquoi celle-là ?",
            "Deux phrases en tout, pas plus.",
        ],
        notes="Trois minutes. Les réponses se partagent presque toujours "
              "entre l'échéance et les trois sources ; les deux sont bonnes, "
              "et la comparaison lance la séance suivante.")

    return d.save(dossier)
