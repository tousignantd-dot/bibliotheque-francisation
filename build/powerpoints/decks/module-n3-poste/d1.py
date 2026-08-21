# -*- coding: utf-8 -*-
"""D1 · Ce carton-là était dans ma boîte aux lettres.
Bloc D « Défi 3 · Le carton dans la boîte aux lettres » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3avis`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-poste/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre='Ce carton-là était dans ma boîte aux lettres',
        chapeau="Un petit carton veut dire qu'un colis est arrivé pendant que "
                "vous étiez au travail. Il vous attend, mais pas "
                "éternellement : quinze jours, et il repart.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 3. Demander qui a déjà trouvé un carton comme "
                  "celui-là sans savoir ce que c'était. Il y a presque toujours "
                  "quelqu'un, et souvent un colis retourné.")

    d.objectifs([
        "reconnaître un avis de livraison ;",
        "lire les six renseignements qu'il contient ;",
        "savoir ce qu'il faut apporter pour ramasser un colis ;",
        "comprendre le délai de quinze jours.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce que ce carton-là veut dire ?",
        image=IMG + 'carton-avis.jpg',
        pistes=[
            "Est-ce que c'est de la publicité ?",
            "Qui l'a mis là, et pourquoi ?",
            "Est-ce qu'il faut faire quelque chose ?",
            "Est-ce qu'on peut attendre un mois ?",
        ],
        notes="Beaucoup d'élèves jettent ce carton en croyant que c'est une circulaire. "
              "C'est l'erreur la plus coûteuse du module, et c'est le sujet de toute "
              "la séance.")

    d.dialogue('Dialogue · 1 de 3', "Votre colis est ici", [
        ("YASSINE", "Bonjour. J'ai trouvé ce carton-là dans ma boîte aux lettres.", True),
        ("CAROLE", "C'est un avis de livraison. Votre colis est ici.", True),
        ("YASSINE", "Qu'est-ce qu'il faut apporter ?", True),
        ("CAROLE", "Le carton et une pièce d'identité avec photo. Les deux.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="La première réplique est la phrase à retenir : on montre le carton et on "
             "dit d'où il vient. Rien d'autre n'est nécessaire pour être servi.")

    d.dialogue('Dialogue · 2 de 3', "Quinze jours", [
        ("YASSINE", "Est-ce que vous le gardez longtemps, un colis ?", True),
        ("CAROLE", "Quinze jours. Après, il retourne à la personne qui l'a envoyé.", True),
        ("YASSINE", "Quinze jours seulement ? Je ne le savais pas.", False),
        ("CAROLE", "On envoie un deuxième carton après cinq jours, pour rappeler.", True),
    ], notes="Le délai est l'information la plus utile de la séance. Le faire écrire au "
             "tableau en gros : QUINZE JOURS. Beaucoup de colis repartent parce que "
             "personne ne connaît ce chiffre.")

    d.dialogue('Dialogue · 3 de 3', "Je déménage le premier juillet", [
        ("YASSINE", "J'ai une autre question. Je déménage le premier juillet.", True),
        ("CAROLE", "Vous pouvez faire suivre votre courrier à la nouvelle adresse.", True),
        ("YASSINE", "Pendant combien de temps ?", True),
        ("CAROLE", "Jusqu'à douze mois. Mais attention : les colis ne suivent pas.", True),
    ], notes="Faire remarquer la première réplique : « J'ai une autre question » ouvre "
             "un deuxième service pendant qu'on est au comptoir. C'est une stratégie, "
             "pas seulement une phrase.")

    d.tableau('Analyse', "Ce que dit le carton d'avis",
              ['La ligne', 'Ce qu\'elle dit'],
              [["Pour", "BERRADA, Yassine — 2145, 8e Avenue, app. 3"],
               ["Pourquoi", "Personne n'était là pour signer."],
               ["Où le ramasser", "Bureau de poste de la 3e Avenue, à partir du 5 juin, treize heures."],
               ["Quoi apporter", "Ce carton et une pièce d'identité avec photo."],
               ["Jusqu'à quand", "Gardé quinze jours. Après le 19 juin, retour à l'expéditeur."]],
              cle=0,
              note="Un avis final est envoyé après cinq jours, pour rappeler.",
              notes="Diapo à photographier. C'est le document de l'exercice `t3avis`. "
                    "Faire trouver chaque ligne par un élève différent : c'est un "
                    "exercice de lecture, pas de mémoire.")

    d.regle("Les deux choses à apporter",
            "le carton ET une pièce d'identité avec photo",
            precision="Les deux, jamais l'une sans l'autre. Un permis de conduire, "
                      "une carte d'assurance maladie avec photo, un passeport : "
                      "tout ce qui porte votre nom et votre visage. Sans les deux, "
                      "la préposée ne peut pas remettre le colis, même si elle "
                      "vous reconnaît.",
            notes="Diapo à photographier. Le mot « ET » est en majuscules exprès : "
                  "c'est l'erreur qui fait revenir les gens une deuxième fois.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue et le carton.", [
        ("Le carton trouvé dans la boîte aux lettres est un avis de livraison.", "vrai"),
        ("Il faut apporter le carton et une pièce d'identité avec photo.", "vrai"),
        ("Le colis est gardé au bureau de poste pendant deux mois.", "faux — quinze jours"),
        ("Un deuxième carton est envoyé après cinq jours.", "vrai"),
        ("Le courrier peut suivre jusqu'à douze mois à la nouvelle adresse.", "vrai"),
        ("Les colis suivent aussi à la nouvelle adresse.", "faux — seulement les lettres"),
    ], corrige=True,
       notes="C'est l'exercice `t3vf` du module. La dernière ligne annonce la séance D2, "
             "qui traite le déménagement en entier.")

    d.pratique('Compréhension', "Le carton d'avis de Yassine",
               "Relisez le tableau, puis répondez par vrai ou faux.", [
        ("Le colis attend Yassine au bureau de poste de la 3e Avenue.", "vrai"),
        ("Yassine peut le ramasser le 4 juin au matin.", "faux — à partir du 5 juin, treize heures"),
        ("Le carton seul suffit pour ramasser le colis.", "faux — le carton et une pièce d'identité"),
        ("Après le 19 juin, le colis retourne à la personne qui l'a envoyé.", "vrai"),
        ("Le colis a été avisé parce que personne ne pouvait signer.", "vrai"),
        ("Aucun rappel n'est envoyé avant le retour du colis.", "faux — un avis final après cinq jours"),
    ], corrige=True,
       notes="C'est l'exercice `t3avis`. Il demande de revenir au document, ligne par "
             "ligne : c'est de la compréhension écrite, et le programme la vise "
             "explicitement au niveau 3 sur ce genre de formulaire.")

    d.billet(
        "Écrivez la phrase que vous direz en arrivant au comptoir avec un carton.",
        exemples=[
            "Une seule phrase suffit.",
            "Qu'est-ce que vous apporterez avec vous ?",
        ],
        notes="Deux minutes. La phrase attendue est celle du dialogue : « J'ai trouvé "
              "ce carton-là dans ma boîte aux lettres. » Elle prépare la séance D2, qui "
              "travaille « ce », « cet », « cette ».")

    return d.save(dossier)
