# -*- coding: utf-8 -*-
"""A1 · Je cherche un manteau d'hiver — mise en situation.
Bloc A « Je découvre » · couleur teal · 75 min.
Source du module : dialogue `prep`, exercices `prVocab`, `pr1` et `prChoisir`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-vetements/images/')


def build(dossier):
    d = Deck(
        code='A1', section='teal',
        titre="Je cherche un manteau d'hiver",
        chapeau="Kofi passe ses hivers en trois couches de vêtements depuis "
                "trois ans. Cette année, il achète un vrai manteau — et il "
                "découvre qu'un manteau d'hiver se choisit autrement.",
        duree='75 minutes')

    d.titre(notes="Ouverture du module. Question d'entrée : « comment vous êtes-vous "
                  "habillés votre premier hiver ? ». Les récits sortent tout de suite, et "
                  "ils sont souvent drôles.")

    d.objectifs([
        "dire ce que je cherche dans un magasin de vêtements ;",
        "donner ma taille et demander à essayer ;",
        "savoir ce qui compte sur un manteau d'hiver ;",
        "comprendre qu'une taille change d'une marque à l'autre.",
    ])

    d.declencheur(
        'Mise en situation', "Vous devez choisir un manteau ici. Par où commencez-vous ?",
        image=IMG + 'rayon-manteaux.jpg',
        pistes=[
            "Qu'est-ce qui distingue un manteau d'hiver d'une veste ?",
            "Comment savoir s'il sera assez chaud ?",
            "Quelle taille prenez-vous, d'habitude ?",
            "Est-ce que la taille est la même dans toutes les marques ?",
        ],
        notes="Cinq minutes. La deuxième piste amène la cote de température, que presque "
              "personne ne connaît. C'est le cœur de la séance.")

    d.cartes('La situation', "Ce qu'on sait de Kofi", [
        ("D'où il vient",
         "Du Ghana. Il est au Québec depuis trois ans."),
        ("Comment il s'habillait",
         "En trois couches de vêtements. Ça fonctionne à moins cinq ; à moins vingt-cinq, "
         "non."),
        ("Ce qu'il ne connaît pas",
         "La cote de température, sa taille dans les marques d'ici, et le fait qu'un "
         "manteau d'hiver se prend plus grand."),
        ("Ce qu'il fait de bien",
         "Il dit ce qu'il cherche précisément : « un manteau d'hiver, un vrai, pas une "
         "veste ». La conseillère sait tout de suite où le mener."),
    ], notes="La deuxième carte fait rire et rassemble : beaucoup d'élèves ont fait "
             "exactement ça.")

    d.dialogue('Dialogue · 1 de 3', "Dire ce qu'on cherche", [
        ("VALÉRIE", "Bonjour ! Je peux vous aider ?", False),
        ("KOFI", "Bonjour. Je cherche un manteau d'hiver. Un vrai, pas une veste.", True),
        ("VALÉRIE", "D'accord. Vous voulez quelque chose pour quelle température ?", True),
        ("KOFI", "Je ne sais pas. Pour l'hiver d'ici. Je m'habille en trois couches depuis trois ans.", True),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="« Pour quelle température ? » est la question du métier. Elle surprend, et "
             "c'est elle qui oriente tout le choix.")

    d.dialogue('Dialogue · 2 de 3', "La cote de température", [
        ("VALÉRIE", "Alors il vous faut un manteau coté moins trente. C'est écrit sur l'étiquette, en petit.", True),
        ("KOFI", "Moins trente ? Il fait vraiment moins trente ?", True),
        ("VALÉRIE", "Quelques jours par hiver, oui. Avec le vent, ça descend plus bas.", True),
        ("KOFI", "Bon. Vous en avez de quelle taille ?", False),
    ], notes="Écrire « coté moins trente » au tableau. C'est l'information la plus utile de "
             "la séance, et elle est écrite en tout petit sur les vraies étiquettes.")

    d.dialogue('Dialogue · 3 de 3', "La taille et l'essayage", [
        ("VALÉRIE", "Du petit au très grand. Vous faites quelle taille, d'habitude ?", True),
        ("KOFI", "Moyen, je pense. Mais je ne sais pas si c'est pareil ici.", True),
        ("VALÉRIE", "Ça change d'une marque à l'autre. Le mieux, c'est d'essayer. Les cabines sont au fond.", True),
        ("KOFI", "Je peux en essayer plusieurs ?", True),
    ], notes="« Ça change d'une marque à l'autre » : à dire et à redire. Aucune taille "
             "annoncée ne dispense d'essayer.")

    d.tableau('Analyse', "Ce qu'on regarde sur un manteau d'hiver",
              ['Ce qu\'on regarde', 'Pourquoi'],
              [["La cote de température", "moins vingt, moins trente — écrit en petit"],
               ["Le remplissage", "duvet ou fibre : chaleur et poids"],
               ["La longueur", "aux genoux pour attendre dehors"],
               ["Le capuchon", "une bordure qui coupe le vent"]],
              cle=0,
              note="Et la taille : une de plus que d'habitude, pour la place d'un chandail.",
              notes="Diapo à photographier. Faire recopier : c'est la liste de vérification "
                    "d'un achat de manteau.")

    d.vocabulaire('Vocabulaire · 1 de 2', "Dans le magasin", [
        ("un manteau", "Le vêtement d'extérieur long et chaud de l'hiver."),
        ("une veste", "Plus léger, pour l'automne et le printemps."),
        ("une cabine d'essayage", "Le petit espace fermé où on essaie."),
        ("la taille", "Petit, moyen, grand, très grand — pour les vêtements."),
        ("la pointure", "Un chiffre — pour les chaussures. On ne dit pas « taille »."),
    ], notes="La distinction taille / pointure est nette en français et se remarque quand "
             "on la manque.")

    d.vocabulaire('Vocabulaire · 2 de 2', "Ce qui tient chaud", [
        ("le duvet", "Les plumes légères qui remplissent un manteau chaud."),
        ("la fibre synthétique", "L'autre remplissage : moins chaud, mais il craint moins l'humidité."),
        ("un capuchon", "La partie qui couvre la tête."),
        ("la cote de température", "Jusqu'à combien de degrés le manteau protège."),
        ("une couche", "Un vêtement porté par-dessus un autre. « Trois couches »."),
    ], notes="Le duvet est plus chaud et plus léger, mais il perd tout s'il est mouillé. La "
             "fibre sèche vite. Les deux se défendent.")

    d.regle("Ce qu'il faut retenir",
            "Un manteau d'hiver se prend une taille plus grand.",
            precision="Il faut de la place pour un chandail dessous. Un manteau serré est "
                      "un manteau froid : l'air emprisonné entre les couches est ce qui "
                      "tient chaud. C'est contre-intuitif, et c'est la première chose "
                      "qu'on apprend en essayant.",
            notes="Faire répéter la phrase par deux élèves. C'est la diapo à photographier.")

    d.piege("Se fier à sa taille habituelle",
            "Je fais du moyen, je prends le moyen.",
            "Ça change d'une marque à l'autre. Le mieux, c'est d'essayer.",
            "Les tailles ne sont normalisées nulle part. Le même « moyen » varie de "
            "plusieurs centimètres d'une marque à l'autre — et un manteau d'hiver se prend "
            "en plus une taille au-dessus. Essayer n'est pas une politesse : c'est la seule "
            "façon de savoir.",
            notes="Point pratique universel, qui vaut aussi pour les achats en ligne.")

    d.billet(
        "Notez ce que vous portez l'hiver, et ce qui vous manque.",
        exemples=[
            "Manteau, bottes, tuque, gants, foulard.",
            "Pour chacun : est-il assez chaud ? Sinon, qu'est-ce qui manque ?",
        ],
        notes="Ramasser. Ces listes servent au jeu de rôle de E1, et elles révèlent parfois "
              "de vrais besoins.")

    return d.save(dossier)
