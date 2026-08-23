# -*- coding: utf-8 -*-
"""A2 · Le même avis, trois façons de le dire
Bloc A « Je découvre » · couleur indigo · registres de langue · 75 min.
Source : exercice `prReg` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Le même avis, trois façons de le dire",
        chapeau="« C'est plate » et « le rythme m'a paru lent » disent la même "
                "chose. Ce qui change n'est pas l'avis : c'est à qui l'on "
                "parle, et où.",
        duree='75 minutes')

    d.titre(notes="Séance de langue, pas de contenu. Prévenir le groupe : on ne "
                  "parlera d'aucune œuvre aujourd'hui, on travaille la façon de "
                  "dire. Les trois registres reviendront à chaque production.")

    d.objectifs([
        "reconnaître le familier, le standard et le soutenu à l'oreille ;",
        "dire le même avis dans les trois registres ;",
        "choisir le registre que la situation demande ;",
        "comprendre le familier même sans l'employer soi-même.",
    ], notes="Le quatrième objectif est le plus utile hors de la classe : la moitié de "
             "ce qui se dit au travail est du familier, et beaucoup d'élèves le "
             "prennent pour du français qu'ils n'ont pas appris.")

    d.declencheur(
        'Observation', "À qui parlez-vous autrement qu'à votre voisin de classe ?",
        pistes=[
            "À votre patron, à votre médecin, à un fonctionnaire ?",
            "Est-ce que vous changez de mots, ou seulement de ton ?",
            "Dans votre langue première, est-ce que ça existe aussi ?",
            "Est-ce qu'on vous a déjà repris sur la façon de dire ?",
        ],
        notes="La troisième piste ouvre la porte : tous les groupes répondent oui, et "
              "beaucoup ont dans leur langue des marques bien plus nettes qu'en "
              "français. Le phénomène n'est donc pas à apprendre, seulement à "
              "transposer.")

    d.tableau('Analyse', "Trois registres, trois situations",
              ['Le registre', 'Où il vit'],
              [["Familier",
                "à la maison, à la pause, entre collègues du même rang"],
               ["Standard",
                "au travail, au comptoir, dans une réunion ordinaire"],
               ["Soutenu",
                "dans un écrit, une critique, un exposé devant un auditoire"]],
              cle=0,
              note="Aucun n'est meilleur : chacun est faux ailleurs qu'à sa place.",
              notes="Diapositive à photographier. Insister : le soutenu n'est pas la "
                    "récompense du bon élève. Employé à la pause, il fait rire.")

    d.tableau('Analyse', "Les signes qui trahissent le familier",
              ['Le signe', 'Ce qu\'on entend'],
              [["Le « ne » tombe", "j'ai pas aimé, ça marche pas"],
               ["« il y a » se coupe", "y a des bouts où j'ai décroché"],
               ["Le mot se raccourcit", "un ordi, une job, le cinéma du coin"],
               ["Les mots d'ici", "en masse, capoter, c'est plate"]],
              cle=0,
              notes="Les quatre signes se repèrent à l'oreille en une seconde. Faire "
                    "chercher au groupe d'autres exemples entendus au travail cette "
                    "semaine : la liste s'allonge toute seule.")

    d.cartes('Analyse', "Le même avis, trois fois", [
        ("Familier", "C'était vraiment plate."),
        ("Standard", "Je n'ai pas trouvé le temps long."),
        ("Soutenu", "Le rythme m'a paru lent par moments."),
        ("Familier", "Le monde a ri en masse."),
        ("Standard", "La salle a beaucoup ri."),
        ("Soutenu", "L'auditoire a répondu avec chaleur."),
    ], cols=2,
       notes="Faire dire les six à voix haute, dans l'ordre. Le passage du premier au "
             "troisième doit s'entendre dans la voix autant que dans les mots.")

    d.regle("Le registre se choisit, il ne se subit pas",
            "Ce n'est pas de la politesse : c'est le registre que la situation "
            "demande, et l'avis reste exactement le même.",
            precision="Une personne qui dit « c'est plate » dans le corridor et « le "
                      "rythme m'a paru lent » au procès-verbal n'a pas changé d'idée. "
                      "Elle a changé de destinataire.",
            notes="Diapositive à photographier. C'est la phrase qui rassure : "
                  "personne n'est obligé de renoncer à sa façon de parler, il faut "
                  "seulement en avoir deux.")

    d.piege('Registre',
            "« L'auditoire a répondu avec chaleur, c'était vraiment le fun. »",
            "« L'auditoire a répondu avec chaleur. » ou « Le monde a triplé le fun. »",
            "La deuxième moitié de la première phrase détruit la première. Un "
            "registre se tient du début à la fin de la phrase, et de préférence "
            "du début à la fin du texte. Le mélange s'entend plus que la faute.",
            notes="Erreur très fréquente à l'écrit chez les élèves de niveau 7, qui "
                  "connaissent maintenant assez de mots pour piocher dans les deux "
                  "registres sans s'en rendre compte.")

    d.pratique('Écoute', "Familier, standard ou soutenu ?",
               "Écoutez chaque phrase et classez-la.", [
        ("Y a des bouts où j'ai décroché.", "familier"),
        ("J'ai perdu le fil deux ou trois fois.", "standard"),
        ("Mon attention a fléchi dans le premier quart d'heure.", "soutenu"),
        ("Franchement, ça m'a fait capoter.", "familier"),
        ("J'ai été très touchée par la dernière scène.", "standard"),
        ("Cette dernière scène m'a profondément émue.", "soutenu"),
    ], corrige=True,
       notes="Exercice `prReg` du module, à faire d'abord à l'oral en classe puis à "
             "l'écran. Douze phrases dans le module ; six suffisent ici.")

    d.billet(
        "Écrivez une phrase de votre billet d'hier dans un autre registre.",
        exemples=[
            "Si vous aviez écrit du standard, montez au soutenu.",
            "Si vous aviez écrit du soutenu, descendez au familier.",
        ],
        notes="Reprend le billet de A1, ce qui économise l'invention et montre que "
              "le registre se change sans changer l'idée.")

    return d.save(dossier)
