# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots.
Bloc E « Je me lance » · couleur framboise · 60 min.
Source : banc `FC_CARDS`, cartes mémoire et autoévaluation du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre='Je retiens des mots',
        chapeau="Seize mots, quatre familles, et une question : qu'est-ce que "
                "je suis maintenant capable de faire au comptoir d'une "
                "pharmacie ?",
        duree='60 minutes')

    d.titre(notes="Dernière séance du module. Prévoir les cartes mémoire du module "
                  "interactif : la révision se fait à l'écran, en paires.")

    d.objectifs([
        "revoir les seize mots du module, par familles ;",
        "employer chaque mot dans une phrase ;",
        "évaluer ce qu'on est capable de faire ;",
        "nommer ce qui reste à travailler.",
    ])

    d.cartes("L'endroit et les papiers", "Quatre mots", [
        ("une ordonnance, le comptoir des ordonnances",
         "Le papier du médecin, et le comptoir du fond où on le dépose. Les deux mots "
         "vont ensemble : on ne dit pas « le comptoir » tout court, il y en a deux."),
        ("la carte d'assurance maladie",
         "À présenter chaque fois, même pour un simple renouvellement. Vérifiez sa date "
         "d'expiration : elle se renouvelle avant, pas après."),
        ("un médicament en vente libre",
         "Il s'achète sans ordonnance. Certains restent quand même derrière le "
         "comptoir : c'est le pharmacien qui décide de les donner."),
        ("le pharmacien",
         "Il prépare, il conseille, il peut prolonger une ordonnance. Le conseil est "
         "gratuit et ne demande pas de rendez-vous."),
    ], notes="Faire dire chaque mot avec son article, puis dans une phrase. Les quatre "
             "sont ceux du bloc A.")

    d.cartes("Le corps et les malaises", "Quatre mots", [
        ("tousser, avoir de la fièvre",
         "Les deux malaises les plus fréquents à la pharmacie. « Je tousse depuis "
         "quatre jours », « j'ai de la fièvre depuis hier soir »."),
        ("un rhume",
         "Le nez qui coule, la gorge irritée. Ça dure environ une semaine. Un rhume qui "
         "persiste plus de sept jours mérite une consultation."),
        ("un pansement",
         "Pour une coupure. La phrase qui va avec : « je me suis coupé le doigt », au "
         "passé composé, avec être."),
        ("j'ai mal à…",
         "La phrase de base, et ses quatre formes : au dos, à la tête, à l'oreille, aux "
         "dents. C'est le nom qui suit qui décide."),
    ], notes="Faire montrer la partie du corps en même temps que le mot. Les mots du "
             "corps s'apprennent avec le corps.")

    d.cartes("Le renouvellement", "Quatre mots", [
        ("un renouvellement",
         "Recevoir encore une fois le même médicament, sans nouveau papier. Le nombre "
         "restant est écrit sur l'étiquette."),
        ("le dossier",
         "La liste que la pharmacie garde de tous vos médicaments. C'est elle qui "
         "permet de repérer un mélange dangereux."),
        ("l'assurance médicaments",
         "Elle paie une partie du prix. Il reste presque toujours une somme à votre "
         "charge : c'est normal, ce n'est pas une erreur."),
        ("est-ce que je peux… ?",
         "La demande de base du module : « Est-ce que je peux faire renouveler mon "
         "ordonnance ? » Une phrase, apprise en bloc."),
    ], notes="Les quatre mots du bloc C. Faire redire la phrase de demande par tout le "
             "groupe : c'est celle qui servira le plus souvent.")

    d.cartes("L'étiquette", "Quatre mots", [
        ("la posologie",
         "Ce qui dit combien en prendre et quand. Un mot long, mais écrit partout : "
         "mieux vaut le reconnaître que l'éviter."),
        ("un comprimé",
         "Le petit rond dur qu'on avale avec de l'eau. « Un comprimé trois fois par "
         "jour » n'est pas « trois comprimés une fois par jour »."),
        ("une étiquette",
         "Le papier collé sur le flacon, avec votre nom et la posologie. Quatre lignes "
         "à lire lentement, une seule fois, mais bien."),
        ("un effet secondaire",
         "Ce qu'un médicament peut faire d'autre : mal au cœur, sommeil. Si ça vous "
         "inquiète, appelez la pharmacie — c'est gratuit."),
    ], notes="Les quatre mots du bloc D. Faire relire l'étiquette de Nadia une dernière "
             "fois, à voix haute, par un élève.")

    d.pratique('Emploi', "Une phrase avec chaque mot",
               "En paires : l'un dit le mot, l'autre fait la phrase.", [
        ("une ordonnance", "« Mon ordonnance est finie depuis samedi. »"),
        ("depuis", "« Je tousse depuis quatre jours. »"),
        ("un renouvellement", "« Est-ce qu'il me reste un renouvellement ? »"),
        ("la posologie", "« Est-ce que vous pouvez m'expliquer la posologie ? »"),
        ("pas plus de", "« Pas plus de quatre comprimés par jour. »"),
    ], corrige=True,
       notes="Changer de rôle à mi-parcours. Noter au tableau les trois plus belles "
             "phrases produites par le groupe.")

    d.tableau('Autoévaluation', "Qu'est-ce que je suis capable de faire ?",
              ["Je suis capable de…", "Pas encore · Un peu · Oui"],
              [["nommer les deux comptoirs", "— · — · —"],
               ["dire où j'ai mal et depuis quand", "— · — · —"],
               ["demander un renouvellement", "— · — · —"],
               ["lire une posologie et la répéter", "— · — · —"],
               ["comprendre « pas plus de »", "— · — · —"]],
              cle=0,
              note="La même grille est dans le module, avec neuf énoncés.",
              notes="Faire remplir l'autoévaluation à l'écran, dans le module. Relever "
                    "ce que le groupe évalue le plus bas : c'est là que la révision de "
                    "la semaine suivante commence.")

    d.billet(
        "Écrivez ce que vous irez demander à votre pharmacie cette semaine.",
        exemples=[
            "Une vraie question, pour une vraie visite.",
            "Écrivez la phrase entière, comme vous allez la dire.",
        ],
        notes="Dernier devoir du module. Demander un retour à la séance suivante : qui y "
              "est allé, ce qui s'est passé. C'est la seule évaluation qui compte "
              "vraiment.")

    return d.save(dossier)
