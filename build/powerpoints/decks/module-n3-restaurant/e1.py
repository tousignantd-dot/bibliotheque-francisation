# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 75 min.
Source : jeu de rôle `comptoir`, production orale et production écrite du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='Je me lance',
        chapeau="Tout le module tient dans un échange d'une minute : dire ce "
                "qu'on veut, choisir un format, répondre au préposé, demander "
                "ce qui manque. Puis l'écrire.",
        duree='75 minutes')

    d.titre(notes="Séance d'évaluation formative. Prévoir les tablettes ou les portables "
                  "pour le jeu de rôle avec l'assistant, et un casque par élève si "
                  "possible.")

    d.objectifs([
        "tenir une commande complète au comptoir ;",
        "répondre aux cinq questions du préposé sans hésiter ;",
        "s'enregistrer, s'écouter et se corriger ;",
        "écrire une courte commande pour trois personnes.",
    ])

    d.regle("Le préposé répond, il n'annonce pas",
            "ce qu'on ne demande pas ne se dit pas",
            precision="Dans le jeu de rôle, l'assistant ne donne ni le contenu "
                      "du plat, ni les formats, ni le prix avant qu'on les "
                      "demande — et il ne rappelle jamais ce qu'on a oublié. "
                      "C'est exactement ce qui se passe au comptoir.",
            notes="Diapo à photographier. Prévenir le groupe avant de commencer : "
                  "l'élève qui attend que l'assistant parle n'obtiendra rien.")

    d.cartes("Les trois situations du jeu de rôle", "À choisir dans le module", [
        ("Le trio du midi",
         "Tu as une heure pour dîner et tu veux un trio. Tu ne sais pas ce qu'il y a "
         "dans les sandwichs, ni ce que le trio comprend."),
        ("La soupe du jour",
         "Tu veux une soupe et un café. Tu ne sais pas quelle est la soupe du jour, ni "
         "quels formats existent. Tu manges sur place."),
        ("Deux repas pour emporter",
         "Tu commandes pour toi et pour une camarade. Il te faut deux repas pour "
         "emporter, des ustensiles et des serviettes."),
    ], cols=3,
       notes="Faire choisir avant de commencer. Un élève qui hésite prend la première : "
             "c'est celle qui reprend le plus de choses du module.")

    d.tableau('Analyse', "Les sept sujets à couvrir",
              ["Dans l'ordre", "Ce qu'on dit"],
              [["1. Saluer", "Bonjour."],
               ["2. Dire ce qu'on veut", "Je voudrais un trio, s'il vous plaît."],
               ["3. Demander ce qu'il y a dedans", "Ce sandwich-là, c'est quoi ?"],
               ["4. Choisir un format", "Petit, s'il vous plaît."]],
              cle=1,
              note="Les trois derniers sujets sont sur la diapositive suivante.",
              notes="Diapo à photographier. Un tableau de sept lignes ne se lit pas de "
                    "loin : c'est pour ça qu'il est coupé en deux.")

    d.tableau('Analyse', "Les sept sujets à couvrir (suite)",
              ["Dans l'ordre", "Ce qu'on dit"],
              [["5. Répondre au préposé", "Pour ici. Débit, s'il vous plaît."],
               ["6. Demander ce qui manque", "Est-ce que je peux avoir du sel ?"],
               ["7. Retenir et remercier", "Le 42. Merci beaucoup."]],
              cle=1,
              note="Sept sujets, une minute. Ce n'est pas une conversation : "
                   "c'est une commande.",
              notes="Faire cocher les sept sujets par un observateur pendant que deux "
                    "élèves jouent la scène devant le groupe.")

    d.pratique('Production orale', "Ce qu'on écoute en vous corrigeant",
               "Quatre choses, et rien d'autre.", [
        ("La formule polie", "je voudrais, s'il vous plaît, merci"),
        ("Le format", "petit, moyen ou grand, accordé au plat"),
        ("Les réponses", "les cinq questions du préposé, répondues du premier coup"),
        ("La demande finale", "un condiment ou un ustensile demandé poliment"),
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

    d.pratique('Production écrite', "La commande du groupe",
               "Cinq à huit phrases, avec quatre choses obligatoires.", [
        ("Le plat de chacun", "avec au, à la ou aux : un sandwich au poulet"),
        ("Un format", "pour ce qui en a un : une petite soupe"),
        ("Un breuvage par personne", "jus, lait, café ou eau"),
        ("Ce qui manque souvent", "ustensiles, serviettes, condiments"),
    ], corrige=False,
       notes="Rappeler les deux tableaux de petits mots : celui de B3 pour le contenu du "
             "plat, celui de D2 pour les condiments.")

    d.piege("Écrire une commande trop vague",
            "trois repas, s'il vous plaît",
            "trois plats nommés, avec leur format et leur breuvage",
            "Une commande écrite sert à ne rien oublier au comptoir. Si elle ne dit pas "
            "quel plat, quel format et quel breuvage, elle ne sert à rien : il faudra "
            "rappeler les trois personnes. Court et complet vaut mieux que long et vague.",
            notes="Montrer un exemple trop vague et un exemple juste, côte à côte au "
                  "tableau. La différence se voit immédiatement.")

    d.billet(
        "Terminez votre commande et envoyez-la.",
        exemples=[
            "Relisez-la une fois avant d'envoyer.",
            "Vérifiez les petits mots : au, aux, du, des.",
        ],
        notes="Ce qui n'est pas fini en classe se termine à la maison. Les productions "
              "envoyées apparaissent dans le portail enseignant.")

    return d.save(dossier)
