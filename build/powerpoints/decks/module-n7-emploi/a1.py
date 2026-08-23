# -*- coding: utf-8 -*-
"""A1 · Se plaindre, ou présenter un projet ?
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source du module : dialogue `prep`, exercice `prCinq`.
"""
import pathlib

from theme import Deck

# La racine se déduit de `__file__`, jamais d'un chemin absolu écrit à la
# main : les decks des modules plus anciens portent le chemin en dur et
# `Slide.image()` lève alors une FileNotFoundError dès qu'on travaille dans un
# worktree — ce qui arrête le build des seize séances d'un coup.
IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-emploi' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Se plaindre, ou présenter un projet ?",
        chapeau="Tout le monde sait dire ce qui ne va pas au travail. Beaucoup "
                "moins de gens savent en faire un projet qu'on écoute jusqu'au "
                "bout. La différence n'est pas dans le ton : elle est dans ce "
                "qu'on met dans sa phrase.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : "
                  "y a-t-il quelque chose, à votre travail ou dans votre immeuble, que "
                  "vous trouvez mal fait ? Laisser trois ou quatre réponses venir. "
                  "Elles seront presque toutes des plaintes, et c'est exactement le "
                  "point de départ dont la séance a besoin.")

    d.objectifs([
        "distinguer une plainte d'un projet, et dire ce qui les sépare ;",
        "nommer les cinq parties d'un projet : constat, cause, conséquence, "
        "correctif, échéance ;",
        "employer les premiers mots du dossier : un projet, une évaluation "
        "sommaire, un ordre du jour ;",
        "situer le scénario du module : Aïcha Traoré et le poste 4.",
    ], notes="Le deuxième objectif est la colonne vertébrale des quatre blocs. Il "
             "revient à chaque séance, et l'élève devra pouvoir citer les cinq "
             "parties de mémoire à la fin du module.")

    d.declencheur(
        'Observation', "Qu'est-ce qui est mal fait, là où vous travaillez ?",
        image=IMG + 'poste-emballage.jpg',
        pistes=[
            "Qu'est-ce que vous avez déjà remarqué, sans jamais le dire ?",
            "À qui l'auriez-vous dit, si vous l'aviez dit ?",
            "Qu'est-ce qui vous a retenu ?",
            "Est-ce que quelqu'un a déjà changé quelque chose grâce à vous ?",
        ],
        notes="Question sans mauvaise réponse. Plusieurs élèves travaillent en usine, "
              "en entretien ménager ou en cuisine, et ont déjà vu un poste mal conçu. "
              "Ne pas commenter : recueillir. On y revient à la fin de la séance pour "
              "montrer que ces réponses sont des constats, donc la première des cinq "
              "parties. L'image montre le poste 4 : les caisses attendent au sol.")

    d.dialogue('Dialogue · 1 de 4', "Une feuille remplie à la maison", [
        ("AÏCHA", "Thérèse, tu as deux minutes ? Je voudrais te montrer quelque chose avant que tu partes.", False),
        ("THÉRÈSE", "Vas-y, mon dîner attendra. Qu'est-ce que tu as là ?", False),
        ("AÏCHA", "Une feuille que j'ai remplie toute seule, hier soir, à la maison. J'ai compté ce qui se passe au poste 4 depuis le mois de mars.", True),
        ("THÉRÈSE", "Le poste d'emballage. Celui où les caisses se ramassent à terre.", False),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer qu'Aïcha a compté. C'est le geste qui rend tout le reste "
             "possible, et c'est celui que personne ne fait spontanément.")

    d.dialogue('Dialogue · 2 de 4', "Ce n'est pas encore un projet", [
        ("AÏCHA", "Si je vais voir monsieur Cormier et que je lui dis que le poste 4 est mal fait, il va m'écouter deux minutes et passer à autre chose.", True),
        ("THÉRÈSE", "Il va t'écouter deux minutes, oui. Parce que ce que tu viens de me décrire, ce n'est pas encore un projet. C'est une plainte.", True),
        ("AÏCHA", "Une plainte. Le mot est dur.", False),
        ("THÉRÈSE", "Il n'est pas dur, il est exact, et ce n'est pas une critique.", False),
    ], notes="Le mot « plainte » va faire réagir. Le désamorcer tout de suite comme "
             "Thérèse le fait : ce n'est pas un jugement sur la personne, c'est le nom "
             "d'un genre de discours.")

    d.dialogue('Dialogue · 3 de 4', "Cinq choses, pas une", [
        ("THÉRÈSE", "Une plainte, ça dit ce qui ne va pas et ça s'arrête là. Un projet, ça dit ce qui ne va pas, ce que ça coûte, ce qu'on fait à la place, combien ça coûte et quand.", True),
        ("AÏCHA", "Cinq choses. Redis-les-moi lentement, je les écris.", False),
        ("THÉRÈSE", "Le constat. La cause. La conséquence, en chiffres si tu en as. Le correctif que tu proposes. Et l'échéance.", True),
        ("AÏCHA", "J'ai le constat et j'ai les chiffres. La cause aussi, je pense.", False),
    ], notes="Diapositive centrale de la séance. Faire écrire les cinq mots au cahier "
             "avant de passer à la suite, puis les faire répéter dans l'ordre, "
             "diapositive masquée.")

    d.dialogue('Dialogue · 4 de 4', "Écoute-le comme si tu prenais des notes", [
        ("THÉRÈSE", "Lundi matin, il y a la réunion de production. Monsieur Cormier présente son projet de quai. Écoute-le comme si tu prenais des notes pour l'école.", True),
        ("AÏCHA", "Pourquoi ? Son quai ne me concerne pas.", False),
        ("THÉRÈSE", "Son quai, non. Sa façon de le présenter, oui. Tu feras pareil pour le tien, deux semaines plus tard.", True),
        ("AÏCHA", "Donc j'apprends en écoutant quelqu'un d'autre.", False),
    ], notes="C'est le plan du module en trois répliques : on écoute une présentation "
             "(bloc B), on en fait une (bloc C), on l'écrit (bloc D). Le dire "
             "explicitement au groupe.")

    d.tableau('Analyse', "Les cinq parties d'un projet",
              ['La partie', "Ce qu'elle contient"],
              [["Le constat", "ce que vous avez vu et compté, avec la période"],
               ["La cause", "pourquoi ça arrive, sans désigner un coupable"],
               ["La conséquence", "ce que le problème coûte en jours ou en argent"],
               ["Le correctif", "ce que vous proposez, le gratuit avant le payant"],
               ["L'échéance", "une date précise, jamais « bientôt »"]],
              cle=0,
              note="Une plainte contient la première partie, parfois la deuxième. Un projet contient les cinq.",
              notes="Diapositive à photographier. C'est le tableau de référence de tout "
                    "le module ; il revient en B2 appliqué à la présentation de "
                    "monsieur Cormier, et en C2 appliqué à celle d'Aïcha.")

    d.regle("Un projet sans date n'est pas refusé : il est oublié",
            "Cinq parties, et la cinquième est une date.",
            precision="C'est la partie qu'on omet le plus souvent, parce qu'elle "
                      "engage. Sans elle, personne n'a à répondre, et le dossier "
                      "s'enfonce dans la pile. Une date force une réponse, même "
                      "négative - et une réponse négative se travaille, alors qu'un "
                      "silence ne se travaille pas.",
            notes="Diapositive à photographier. Insister : on n'écrit pas une date pour "
                  "faire pression, on l'écrit pour rendre une réponse possible.")

    d.vocabulaire('Vocabulaire', "Quatre mots pour commencer", [
        ("un projet", "Ce qu'on veut faire, avec les étapes, le coût et la date qui vont avec."),
        ("une évaluation sommaire", "Un premier examen rapide, qui donne des ordres de grandeur et non des chiffres définitifs."),
        ("un ordre du jour", "La liste écrite des points dont une réunion va traiter, dans l'ordre."),
        ("une réunion de production", "La rencontre régulière où l'équipe fait le point sur le travail de l'usine."),
    ], notes="Faire répéter avec l'article. « Sommaire » sera compris comme "
             "« bâclée » : corriger tout de suite - un premier examen sérieux, mais "
             "en ordres de grandeur.")

    d.pratique('Pratique', "Une plainte, ou un projet ?",
               "Pour chaque phrase, dites de quoi il s'agit.", [
        ("Le poste 4 est mal fait, tout le monde le sait.", "plainte"),
        ("Depuis mars, trois personnes sur cinq ont consulté pour le dos.", "projet - c'est un constat chiffré"),
        ("C'est toujours nous qui écopons, à l'expédition.", "plainte"),
        ("Une table élévatrice garderait la palette à hauteur de coude.", "projet - c'est un correctif"),
        ("Ça fait des années que ça dure et personne ne fait rien.", "plainte"),
        ("La rotation pourrait commencer le lundi 22 septembre.", "projet - c'est une échéance"),
    ], corrige=True,
       notes="Faire dire, pour chaque « projet », de quelle partie il s'agit. C'est "
             "l'exercice qui prépare tout le bloc B.")

    d.billet(
        "Écrivez le constat de quelque chose que vous voudriez voir changer.",
        exemples=[
            "Depuis quand est-ce que ça dure ?",
            "Combien de fois par jour ou par semaine ?",
            "Combien de personnes est-ce que ça touche ?",
        ],
        notes="Devoir concret. Exiger au moins un chiffre. Les billets servent de "
              "matière première en C2, quand chacun bâtit son évaluation sommaire.")

    return d.save(dossier)
