# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 75 min.
Source : jeu de rôle `electro`, production orale et production écrite du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='Je me lance',
        chapeau="Tout le module tient dans un échange de deux minutes : "
                "trouver le rayon, demander le prix et le format, conclure, "
                "faire livrer. Puis l'écrire.",
        duree='75 minutes')

    d.titre(notes="Séance d'évaluation formative. Prévoir les tablettes ou les portables "
                  "pour le jeu de rôle avec l'assistant, et un casque par élève si "
                  "possible.")

    d.objectifs([
        "tenir un échange court avec un vendeur ;",
        "poser quatre questions dans l'ordre utile ;",
        "s'enregistrer, s'écouter et se corriger ;",
        "écrire un court message de demande de livraison.",
    ])

    d.regle("Le vendeur répond, il n'annonce pas",
            "ce qu'on ne demande pas ne se dit pas",
            precision="Dans le jeu de rôle, l'assistant ne donne ni le prix, "
                      "ni le format, ni la livraison avant qu'on les demande — "
                      "et il ne rappelle jamais ce qu'on a oublié. C'est "
                      "exactement ce qui se passe au magasin.",
            notes="Diapo à photographier. Prévenir le groupe avant de commencer : "
                  "l'élève qui attend que l'assistant parle n'obtiendra rien.")

    d.cartes("Les trois situations du jeu de rôle", "À choisir dans le module", [
        ("La laveuse de la circulaire",
         "Ta laveuse est brisée. La Norlac LT 4200 est à 849 $ jusqu'à dimanche. Tu veux "
         "la voir, connaître sa largeur et la faire livrer."),
        ("Le micro-ondes du deuxième rayon",
         "Tu cherches un micro-ondes pour une petite cuisine. Tu ne sais pas où il est, "
         "ni s'il entre entre le mur et le réfrigérateur."),
        ("Le camion de samedi",
         "Tu as payé ton appareil. Il reste à demander la livraison : un jour, une "
         "heure, ton adresse, et le sort du vieil appareil."),
    ], cols=3,
       notes="Faire choisir avant de commencer. Un élève qui hésite prend la première : "
             "c'est celle qui reprend le plus de choses du module.")

    d.tableau('Analyse', "Les sept sujets à couvrir",
              ['Dans l\'ordre', 'Ce qu\'on dit'],
              [["1. Saluer", "Bonjour. Excusez-moi."],
               ["2. Dire ce qu'on cherche", "Je cherche une laveuse."],
               ["3. Demander le rayon", "Où est le rayon des laveuses ?"],
               ["4. Montrer et demander le prix", "Cette laveuse-là coûte combien ?"]],
              cle=1,
              note="Les trois derniers sujets sont sur la diapositive suivante.",
              notes="Diapo à photographier. Un tableau de sept lignes ne se lit pas de "
                    "loin : c'est pour ça qu'il est coupé en deux.")

    d.tableau('Analyse', "Les sept sujets à couvrir (suite)",
              ['Dans l\'ordre', 'Ce qu\'on dit'],
              [["5. Demander le format", "Elle fait combien de large ?"],
               ["6. Conclure et faire livrer", "Je la prends. Vous livrez samedi ?"],
               ["7. Remercier", "Merci beaucoup. À samedi."]],
              cle=1,
              note="Sept sujets, deux minutes. Ce n'est pas une conversation : "
                   "c'est un achat.",
              notes="Faire cocher les sept sujets par un observateur pendant que deux "
                    "élèves jouent la scène devant le groupe.")

    d.pratique('Production orale', "Ce qu'on écoute en vous corrigeant",
               "Quatre choses, et rien d'autre.", [
        ("Les questions", "quatre questions posées, dans un ordre utile"),
        ("Les nombres", "le prix et la mesure dits sans hésiter"),
        ("Les petits mots", "cette laveuse-là, je la prends"),
        ("La politesse", "bonjour au début, merci à la fin"),
    ], corrige=False,
       notes="Donner ces quatre critères avant l'enregistrement, pas après. L'élève "
             "s'écoute une première fois seul, puis envoie.")

    d.regle("S'écouter avant d'envoyer",
            "je m'enregistre, je m'écoute, je recommence",
            precision="La première prise sert à entendre ce qui manque. On "
                      "peut recommencer autant de fois qu'on veut : c'est le "
                      "seul endroit du module où c'est possible.",
            notes="Insister : les élèves ont tendance à envoyer la première prise. La "
                  "deuxième est presque toujours meilleure d'un cran.")

    d.pratique('Production écrite', "Le message de livraison",
               "Cinq à huit phrases, avec quatre choses obligatoires.", [
        ("L'appareil", "le nom et la marque de ce que vous avez acheté"),
        ("Le moment", "le jour et le moment qui vous conviennent"),
        ("Vos coordonnées", "votre adresse et votre numéro de téléphone"),
        ("Le futur proche", "une phrase avec « je vais » : Je vais être là."),
    ], corrige=False,
       notes="Rappeler l'écriture des dates : le 8 novembre, jamais « novembre 8 », et "
             "pas de majuscule aux jours.")

    d.piege("Écrire un message trop long",
            "raconter toute l'histoire de la laveuse brisée",
            "l'appareil, le jour, l'adresse, une phrase de plus",
            "Le comptoir de la livraison a besoin de quatre renseignements. Un message "
            "de huit lignes se lit mal et retarde la réponse. Court et complet vaut "
            "mieux que long et vague.",
            notes="Montrer un exemple trop long et un exemple juste, côte à côte au "
                  "tableau. La différence se voit immédiatement.")

    d.billet(
        "Terminez votre message et envoyez-le.",
        exemples=[
            "Relisez-le une fois avant d'envoyer.",
            "Vérifiez la date et les deux nombres.",
        ],
        notes="Ce qui n'est pas fini en classe se termine à la maison. Les productions "
              "envoyées apparaissent dans le portail enseignant.")

    return d.save(dossier)
