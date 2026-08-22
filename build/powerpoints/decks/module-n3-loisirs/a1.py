# -*- coding: utf-8 -*-
"""A1 · Le babillard de l'entrée.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source du module : dialogue `prep`, exercice `pr1`.
"""
import os

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-loisirs/images/')


def img(nom):
    """Le chemin de la photo, ou None tant qu'elle n'existe pas.

    Les 29 images du module sont produites par
    `build/contenu/module-n3-loisirs/gen_images.py`, qui n'a pas encore
    tourné. `theme.image()` ouvre le fichier avec Pillow : sans cette garde,
    la séance ne se construirait pas du tout. Elle se construit donc sans
    photo, et la reprend telle quelle dès que le fichier est là.
    """
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Le babillard de l'entrée",
        chapeau="Dans l'entrée de son immeuble, Marisol regarde son voisin "
                "lire le babillard. Le centre communautaire vient d'afficher "
                "son feuillet d'automne. Il y a des activités à trois rues de "
                "chez elle, et elle ne le savait pas.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Demander au groupe qui connaît le centre "
                  "communautaire de son quartier, et ce qu'on y fait. Beaucoup d'élèves "
                  "passent devant depuis des mois sans y être jamais entrés : c'est "
                  "exactement la situation de Marisol.")

    d.objectifs([
        "reconnaître un centre communautaire et dire ce qu'on y trouve ;",
        "lire un babillard et savoir ce qu'un feuillet de loisirs annonce ;",
        "comprendre une conversation entre deux voisins ;",
        "nommer les quatre renseignements qu'il faut avant de choisir.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'on trouve sur ce panneau ?",
        image=img('babillard-entree.jpg'),
        pistes=[
            "Où voit-on des panneaux comme celui-là dans votre quartier ?",
            "Qui met les feuilles dessus ? Qui les lit ?",
            "Qu'est-ce qui est écrit sur une feuille d'activité ?",
            "Est-ce que vous vous êtes déjà arrêté pour en lire une ?",
        ],
        notes="Laisser venir les mots dans n'importe quelle langue, puis les écrire au "
              "tableau en français. Le mot « babillard » est propre au Québec — ailleurs "
              "on dit « tableau d'affichage ». Le signaler, sans en faire une leçon.")

    d.dialogue('Dialogue · 1 de 3', "Le centre communautaire, c'est quoi ?", [
        ("MARISOL", "Thierry ! Qu'est-ce que tu regardes ?", True),
        ("THIERRY", "Le babillard. Le centre communautaire a mis son feuillet d'automne.", True),
        ("MARISOL", "Le centre communautaire… c'est quoi, exactement ?", True),
        ("THIERRY", "C'est une grande maison de quartier, sur la rue Galt. Il y a un gymnase, une cuisine et deux salles.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="La quatrième réplique donne la définition du module. La faire répéter, puis "
             "la faire redire par un élève sans regarder l'écran. Demander ensuite ce "
             "qu'on peut faire dans un gymnase, dans une cuisine, dans une salle.")

    d.dialogue('Dialogue · 2 de 3', "Trois activités, trois soirs", [
        ("MARISOL", "Et on fait quoi, là-dedans ?", False),
        ("THIERRY", "Des activités. Regarde : badminton le mardi soir, danse en ligne le jeudi, ciné-club le vendredi.", True),
        ("MARISOL", "Le samedi, je reste toujours à la maison avec Camila. Ça coûte cher ?", False),
        ("THIERRY", "Pas beaucoup. Certaines activités sont gratuites.", True),
    ], notes="Trois activités, trois soirs différents : c'est la première rencontre avec "
             "la forme « le mardi soir », qui reviendra en A4. Ne pas l'expliquer ici ; "
             "seulement la faire entendre.")

    d.dialogue('Dialogue · 3 de 3', "Quatre questions suffisent", [
        ("MARISOL", "Et il faut apporter quelque chose ?", False),
        ("THIERRY", "Ça, je ne sais pas. Appelle et demande : c'est écrit en bas, le numéro.", True),
        ("MARISOL", "Je n'ose pas téléphoner. Je parle encore mal.", True),
        ("THIERRY", "Tu parles très bien. Et au téléphone, quatre questions suffisent : quand, combien, où, quoi apporter.", True),
    ], notes="La dernière réplique est le plan du module entier. L'écrire au tableau et "
             "l'y laisser toute la semaine. Prendre au sérieux « je n'ose pas téléphoner » : "
             "c'est le vrai obstacle, pas le vocabulaire.")

    d.tableau('Analyse', "Les quatre renseignements avant de choisir",
              ["La question", "Ce qu'elle va chercher"],
              [["Quand ?", "le jour, l'heure, et si c'est toutes les semaines"],
               ["Combien ?", "le tarif, à la séance ou pour la session"],
               ["Où ?", "la salle, dans le centre"],
               ["Quoi apporter ?", "le matériel, et ce qui est prêté sur place"]],
              cle=0,
              note="Avec ces quatre-là, aucune activité de quartier ne reste mystérieuse.",
              notes="Diapo à photographier. Faire lire chaque ligne par un élève différent, "
                    "puis effacer le tableau et faire redire les quatre questions de mémoire.")

    d.regle("Le lieu et son nom",
            "« un centre communautaire »",
            precision="C'est la maison du quartier : un bâtiment public où l'on entre "
                      "sans rendez-vous. On y trouve souvent un gymnase, une cuisine et "
                      "des salles prêtées aux groupes. Les activités y sont annoncées "
                      "trois fois par année, dans un feuillet.",
            notes="Diapo à photographier. Faire répéter le mot à voix haute : il est long "
                  "et il fait peur à lire, mais il se dit en deux morceaux — centre, "
                  "communautaire.")

    d.cartes("Les mots de l'entrée", "Quatre mots", [
        ("un babillard",
         "Le grand panneau de liège où l'on affiche les papiers. Les feuilles y sont "
         "tenues par des punaises, et n'importe qui peut s'arrêter pour les lire."),
        ("un feuillet",
         "Le petit journal plié qui annonce les activités. Il arrive trois fois par "
         "année et se rapporte chez soi : c'est lui qu'on relit à la maison."),
        ("une session",
         "La période de plusieurs semaines pendant laquelle une activité a lieu. "
         "Automne, hiver, printemps : trois sessions par année."),
        ("le tarif",
         "Le prix demandé pour participer. Il se paie à la séance ou pour la session "
         "entière, et il est souvent plus bas pour le monde du quartier."),
    ], notes="Faire dire chaque mot avec son article. Les quatre reviennent dans toutes "
             "les séances du module.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Thierry lit le babillard dans l'entrée de l'immeuble.", "vrai"),
        ("Le centre communautaire est sur la rue Galt.", "vrai"),
        ("Il n'y a qu'une seule salle dans le centre.", "faux — un gymnase, une cuisine et deux salles"),
        ("Le badminton a lieu le jeudi soir.", "faux — le mardi soir"),
        ("Toutes les activités du centre sont gratuites.", "faux — certaines seulement"),
        ("Thierry ne sait pas s'il faut apporter quelque chose.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte du dialogue. C'est "
             "l'exercice pr1 du module : les élèves le retrouveront à l'écran.")

    d.billet(
        "Écrivez le nom d'une activité que vous aimeriez essayer près de chez vous.",
        exemples=[
            "Est-ce que vous savez quel jour elle a lieu ?",
            "Est-ce que vous savez combien elle coûte ?",
        ],
        notes="Devoir court. Les réponses servent de matière au défi 1 : chacun aura sa "
              "propre activité à se renseigner, plutôt que celle du manuel.")

    return d.save(dossier)
