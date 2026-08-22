# -*- coding: utf-8 -*-
"""A1 · « Cinq paragraphes, jamais plus »
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-actualite/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="« Cinq paragraphes, jamais plus »",
        chapeau="Marisol Ferreira prépare les salades à la cafétéria d'un "
                "cégep de Sherbrooke. Tous les mardis, l'hebdomadaire du "
                "secteur traîne sur la table de la salle des employés. Elle "
                "a commencé à le lire pour pratiquer son français ; "
                "maintenant, c'est le cuisinier qui attend qu'elle lui "
                "raconte.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : qui "
                  "lit un journal, en quelle langue, et à quel moment de la journée ? "
                  "Beaucoup répondront qu'ils n'en lisent aucun, faute de temps ou de "
                  "mots. C'est exactement le point de départ : un fait divers de "
                  "quartier tient en cinq paragraphes et parle de la rue d'à côté.")

    d.objectifs([
        "reconnaître un fait divers parmi les autres textes d'un journal ;",
        "nommer les trois parties d'un fait divers : le titre, le chapeau, le texte ;",
        "retrouver en lisant ce qui est arrivé, où et quand ;",
        "comprendre pourquoi un fait divers fait toujours parler quelqu'un.",
    ], notes="Le deuxième objectif est celui qui rend la lecture possible : celui qui "
             "sait où est le chapeau connaît la nouvelle en dix secondes. Le montrer "
             "sur un vrai journal si on en a un sous la main.")

    d.declencheur(
        'Observation', "Un journal ouvert sur une table de cafétéria. "
                       "Qu'est-ce qu'on y lit en premier ?",
        image=IMG + 'journal-cafeteria.jpg',
        pistes=[
            "Est-ce qu'il y a un journal de quartier là où vous habitez ?",
            "Qu'est-ce que vous lisez en premier dans un journal ?",
            "Quand vous apprenez une nouvelle, à qui la racontez-vous ?",
            "Est-ce que quelqu'un vous a déjà raconté une nouvelle de travers ?",
        ],
        notes="La quatrième piste annonce tout le module : une nouvelle mal racontée "
              "est une nouvelle sans ordre et sans source. Laisser deux ou trois "
              "histoires se dire, elles serviront d'exemples jusqu'en D2.")

    d.dialogue('Dialogue · 1 de 5', "Il sort quand, celui-là ?", [
        ("SYLVAIN", "Marisol, tu lis encore ton petit journal. Il sort "
                    "quand, celui-là ?", True),
        ("MARISOL", "Le mardi. Une fois par semaine. C'est un hebdomadaire "
                    "de la région.", True),
        ("SYLVAIN", "Et il y a quoi dedans ? Des annonces de garage ?", True),
        ("MARISOL", "Il y a des annonces, oui. Mais moi, je lis les faits "
                    "divers.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer d'entrée le tutoiement : deux collègues de cuisine qui "
             "travaillent côte à côte depuis des mois. C'est le registre de tout le "
             "module, et c'est celui du jeu de rôle de E1.")

    d.dialogue('Dialogue · 2 de 5', "Les faits divers, c'est quoi au juste ?", [
        ("SYLVAIN", "Les faits divers, c'est quoi au juste ?", True),
        ("MARISOL", "Des petites nouvelles d'ici. Un feu, une inondation, "
                    "un vol de vélos.", True),
        ("SYLVAIN", "Ah, les affaires qui arrivent aux voisins.", True),
        ("MARISOL", "Exactement. C'est court : cinq paragraphes, jamais "
                    "plus.", True),
    ], notes="Écrire au tableau les trois exemples de Marisol : un feu, une "
             "inondation, un vol. Ce sont les trois nouvelles du module, et le groupe "
             "les retrouvera aux blocs B, C et D.")

    d.dialogue('Dialogue · 3 de 5', "Le titre, puis les lignes en gras", [
        ("SYLVAIN", "Tu lis tout, du début à la fin ?", True),
        ("MARISOL", "Non. Je lis le titre, puis les trois lignes en gras "
                    "en dessous.", True),
        ("SYLVAIN", "Les lignes en gras, ça s'appelle comment ?", True),
        ("MARISOL", "Le chapeau. Il dit toute la nouvelle en une phrase "
                    "ou deux.", True),
    ], notes="Le cœur de la séance tient dans ces quatre répliques. Faire répéter le "
             "mot « chapeau » avec son article. Beaucoup d'élèves lisent un article de "
             "journal en commençant par la première ligne du texte : leur montrer "
             "qu'on ne lit jamais comme ça.")

    d.dialogue('Dialogue · 4 de 5', "Et il fait parler du monde", [
        ("SYLVAIN", "Et après ?", True),
        ("MARISOL", "Après, le texte donne les détails, et il fait parler "
                    "du monde.", True),
        ("SYLVAIN", "Du monde comme qui ?", True),
        ("MARISOL", "Un témoin, un pompier, quelqu'un de la Ville. Ceux "
                    "qui étaient là.", True),
    ], notes="Cette page annonce tout le bloc C. Un fait divers n'est jamais une "
             "liste : il donne la parole, et chaque parole porte un nom. Poser la "
             "question au groupe : à quoi ça sert, de savoir qui l'a dit ?")

    d.dialogue('Dialogue · 5 de 5', "Assis-toi, j'en ai une bonne", [
        ("SYLVAIN", "Moi, je n'ai jamais le temps. Tu me raconteras.", True),
        ("MARISOL", "Ça me fait pratiquer mon français. Assis-toi, j'en "
                    "ai une bonne.", False),
    ], notes="La dernière réplique dit la situation du module en huit mots : quelqu'un "
             "n'a rien lu, quelqu'un d'autre raconte. Toute la suite consiste à "
             "apprendre à s'asseoir en face de Sylvain et à parler d'un seul tenant.")

    d.regle("Le chapeau dit tout, le texte ajoute les détails",
            "On lit le titre, puis les deux ou trois lignes en gras. On "
            "sait alors la nouvelle, et on décide si on lit la suite.",
            precision="Le titre annonce. Le chapeau résume l'évènement complet en "
                      "une ou deux phrases. Le texte, lui, ne fait qu'ajouter : "
                      "l'heure exacte, le nombre de logements, ce que les gens ont "
                      "déclaré. On peut s'arrêter après le chapeau sans rien manquer "
                      "d'essentiel.",
            notes="Diapositive à photographier. Elle servira encore en B1, quand on "
                  "demandera à l'élève de commencer son récit par la grosse nouvelle "
                  "plutôt que par l'heure.")

    d.tableau('La forme du texte', "Trois parties, trois usages",
              ['La partie', 'Ce qu\'elle contient'],
              [["Le titre", "Cinq ou six mots. Il annonce, il ne raconte pas."],
               ["Le chapeau", "Deux ou trois lignes en gras : toute la nouvelle d'un coup."],
               ["Le 1er paragraphe", "Ce qui est arrivé, où et quand, au passé composé."],
               ["Le milieu", "Le décor à l'imparfait, puis les paroles entre guillemets."],
               ["La fin", "Ce qui reste : les sinistrés, l'enquête qui se poursuit."]],
              cle=1,
              notes="Faire cacher la colonne de droite et deviner. La dernière ligne "
                    "surprend toujours : presque tous les faits divers se terminent par "
                    "« l'enquête se poursuit », et ce n'est pas une formule creuse.")

    d.cartes("Quatre mots du journal", "Le vocabulaire de la première séance", [
        ("un fait divers",
         "Un court article sur un évènement d'ici : un feu, un vol, une inondation."),
        ("un hebdomadaire",
         "Un journal qui paraît une fois par semaine, toujours le même jour."),
        ("le chapeau",
         "Les lignes en gras sous le titre, qui disent toute la nouvelle."),
        ("un témoin",
         "La personne qui était sur place et qui a vu ce qui s'est passé."),
    ], notes="Faire répéter chaque mot avec son article. « Le chapeau » fera rire : "
             "c'est le même mot que celui qu'on met sur la tête, et c'est justement "
             "l'image — le chapeau se pose sur le texte.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue de la salle des employés.", [
        ("L'Écho des Cantons paraît une fois par semaine.", "vrai"),
        ("Marisol lit d'abord les annonces de garage.", "faux — elle lit les faits divers"),
        ("Le chapeau, ce sont les lignes en gras sous le titre.", "vrai"),
        ("Un fait divers raconte des nouvelles du monde entier.", "faux — des nouvelles d'ici"),
        ("Marisol a commencé à lire le journal pour pratiquer son français.", "vrai"),
        ("Sylvain lit le journal tous les mardis, lui aussi.", "faux — il n'a jamais le temps"),
        ("Un fait divers fait parler des témoins et des pompiers.", "vrai"),
        ("Un fait divers occupe une page complète du journal.", "faux — cinq paragraphes"),
    ], corrige=True,
       notes="Exercice pr1 de l'activité interactive. Faire justifier chaque « faux » "
             "par la réplique exacte : c'est ce geste-là qu'on demandera pendant tout "
             "le module, retrouver dans le texte ce qu'on avance.")

    d.piege("Lire un article de journal comme un livre",
            "Je commence à la première ligne et je vais jusqu'au bout.",
            "Je lis le titre, puis le chapeau. Ensuite je décide.",
            "Un journal ne se lit pas dans l'ordre. Le chapeau existe précisément "
            "pour qu'on puisse s'arrêter là. Trois minutes par jour suffisent pour "
            "lire quatre faits divers de cette façon.",
            notes="Piège très concret : plusieurs élèves abandonnent la lecture d'un "
                  "journal parce qu'ils la vivent comme un examen. Leur donner la "
                  "permission de ne pas tout lire change tout.")

    d.billet(
        "Écrivez en une phrase une nouvelle arrivée près de chez vous cette semaine.",
        exemples=[
            "Dites d'abord ce qui est arrivé, puis où et quand.",
            "Si vous ne savez rien, écrivez la question que vous poserez à un voisin.",
        ],
        notes="Ramasser les billets. Ils fournissent la matière du bloc B : chacun "
              "aura une nouvelle à lui à raconter, en plus de celles du module.")

    return d.save(dossier)
