# -*- coding: utf-8 -*-
"""A1 · Le bureau de poste de la 3e Avenue.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-poste/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre='Le bureau de poste de la 3e Avenue',
        chapeau="Un bureau de poste n'est pas seulement un endroit où on "
                "achète des timbres. On y envoie une boîte, on y ramasse un "
                "colis, on y achète un papier qui vaut de l'argent.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Demander au groupe qui est déjà entré dans "
                  "un bureau de poste au Québec, et pour quoi faire. Les réponses "
                  "donnent des exemples réels pour toute la semaine.")

    d.objectifs([
        "nommer ce qu'on trouve dans un bureau de poste ;",
        "dire quatre choses qu'on peut y faire ;",
        "comprendre une conversation entre voisins ;",
        "savoir qu'on peut demander à la préposée de répéter.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'on peut faire à cet endroit-là ?",
        image=IMG + 'comptoir-poste.jpg',
        pistes=[
            "Qu'est-ce qu'il y a derrière le comptoir ?",
            "À quoi servent les petites cases dans le mur ?",
            "Est-ce qu'on peut y faire autre chose qu'envoyer une lettre ?",
            "Qu'est-ce que vous diriez en arrivant devant la personne ?",
        ],
        notes="Laisser venir les mots dans n'importe quelle langue, puis les traduire "
              "ensemble au tableau. Beaucoup d'élèves connaissent une poste très "
              "différente dans leur pays : c'est la comparaison qui fait entrer le "
              "vocabulaire.")

    d.dialogue('Dialogue · 1 de 3', "Il y a un bureau de poste près d'ici ?", [
        ("YASSINE", "Denise, il y a un bureau de poste près d'ici ?", True),
        ("DENISE", "Oui, sur la 3e Avenue, à dix minutes à pied. Pourquoi ?", True),
        ("YASSINE", "Je veux envoyer une boîte à mon frère, à Calgary.", True),
        ("DENISE", "Alors c'est là. On y envoie des lettres et des colis.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Présenter les deux personnages : Yassine Berrada, arrivé du Maroc il y a "
             "quatorze mois, et Denise Pelletier, sa voisine retraitée. Faire répéter la "
             "question de la première réplique : elle sert dans n'importe quel quartier.")

    d.dialogue('Dialogue · 2 de 3', "Beaucoup de choses", [
        ("YASSINE", "Et les timbres, on les achète où ?", True),
        ("DENISE", "Au même comptoir. En carnet, ça coûte moins cher qu'à l'unité.", True),
        ("YASSINE", "Est-ce qu'on peut faire autre chose là-bas ?", True),
        ("DENISE", "Beaucoup de choses. Un envoi recommandé, un mandat-poste, "
                   "un changement d'adresse.", True),
    ], notes="C'est la découverte centrale de la séance : un seul comptoir pour tout. "
             "Ne pas expliquer « recommandé » ni « mandat-poste » maintenant : la "
             "séance A3 leur est consacrée.")

    d.dialogue('Dialogue · 3 de 3', "Demande-lui de répéter", [
        ("YASSINE", "Et la boîte rouge, dans la rue ?", True),
        ("DENISE", "C'est pour les lettres déjà timbrées. Jamais pour un colis.", True),
        ("YASSINE", "Est-ce que la préposée parle vite ?", True),
        ("DENISE", "Un peu. Demande-lui de répéter, elle va le faire. C'est normal.", True),
    ], notes="La dernière réplique est la plus importante du module : faire répéter est "
             "permis, et personne ne s'en formalise. Le dire explicitement au groupe.")

    d.tableau('Analyse', "Quatre choses qu'on fait au bureau de poste",
              ["Ce qu'on vient faire", "Ce que ça veut dire"],
              [["Envoyer une lettre ou un colis", "on paie le voyage au comptoir"],
               ["Acheter des timbres", "en carnet, c'est moins cher qu'à l'unité"],
               ["Ramasser un colis qui attend", "on apporte le carton et une pièce d'identité"],
               ["Demander un service", "mandat-poste, recommandé, changement d'adresse"]],
              cle=0,
              note="Un seul comptoir sert à tout : on n'a pas à chercher la bonne file.",
              notes="Diapo à photographier. Faire nommer chaque ligne par un élève "
                    "différent. C'est le plan du module entier.")

    d.regle("L'endroit et sa règle la plus simple",
            "la boîte rouge, c'est pour les lettres déjà timbrées",
            precision="Jamais pour un colis, jamais pour une lettre sans timbre. "
                      "Une lettre sans timbre n'est pas affranchie : elle revient à "
                      "la personne qui l'a envoyée, parfois trois semaines plus tard.",
            notes="Diapo à photographier. Beaucoup d'élèves ont déjà mis une enveloppe "
                  "non affranchie dans une boîte rouge. Dédramatiser, puis expliquer ce "
                  "qui arrive ensuite.")

    d.cartes("Les mots de l'endroit", "Quatre mots", [
        ("un bureau de poste",
         "Le magasin du gouvernement où on envoie et où on ramasse le courrier. "
         "Ouvert le jour, avec un comptoir et une file d'attente."),
        ("un préposé, une préposée",
         "La personne qui travaille derrière le comptoir. C'est elle qui pèse, qui "
         "dit le prix et qui répond aux questions."),
        ("un envoi",
         "Tout ce qu'on confie à la poste : une lettre, une boîte, un papier qui "
         "vaut de l'argent. Le mot réunit tout."),
        ("affranchir",
         "Payer le voyage de l'envoi, avec un timbre collé ou au comptoir quand la "
         "préposée pèse la boîte."),
    ], notes="Faire dire chaque mot avec son article. Les quatre reviennent dans toutes "
             "les séances du module.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le bureau de poste est à dix minutes à pied de chez Yassine.", "vrai"),
        ("On achète les timbres à un autre comptoir que les colis.", "faux — au même comptoir"),
        ("Un carnet de timbres coûte moins cher qu'un timbre à l'unité.", "vrai"),
        ("On peut mettre un colis dans la boîte rouge de la rue.", "faux — seulement les lettres timbrées"),
        ("Demander à la préposée de répéter, c'est normal.", "vrai"),
        ("Le bureau de poste ouvre à neuf heures le jeudi.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte du dialogue. "
             "Cet exercice est le `pr1` du module interactif : les élèves le "
             "retrouveront à l'écran en A3.")

    d.billet(
        "Écrivez une chose que vous devez envoyer ou ramasser cette année.",
        exemples=[
            "Une lettre, une boîte, des papiers pour le gouvernement ?",
            "Est-ce que vous savez déjà où est le bureau de poste le plus proche ?",
        ],
        notes="Devoir court. Il donne des exemples personnels pour le défi 1 et il "
              "révèle qui a déjà une démarche réelle à faire.")

    return d.save(dossier)
