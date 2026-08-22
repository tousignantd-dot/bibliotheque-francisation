# -*- coding: utf-8 -*-
"""B1 · Au téléphone avec Ousmane
Bloc B « Défi 1 · Le courriel d'Ousmane » · couleur acier · 75 min.
Source : dialogue `t1` (trois pages de quatre répliques), exercice `t1vf` et
son bandeau de savoir, mots du Défi 1 de FC_CARDS.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Au téléphone avec Ousmane",
        chapeau="Quand on n'est pas sûr d'avoir compris un texte long, une "
                "question au téléphone vaut trois relectures.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 1. Rappeler le tableau des cinq évènements de "
                  "A1 avant de commencer : c'est la carte du courriel, et toute la "
                  "séance consiste à remettre ces évènements dans l'ordre.")

    d.objectifs([
        "suivre une conversation téléphonique longue sans en perdre le fil ;",
        "vérifier une information en la redisant à sa façon ;",
        "reconnaître ce qui était déjà arrivé avant le reste ;",
        "employer les quatre mots du Défi 1 avec leur article.",
    ], notes="Le deuxième objectif se travaille à chaque écoute : « donc, si je "
             "comprends bien… » est la phrase la plus utile du module.")

    d.declencheur(
        'Observation', "Quand tu ne comprends pas un message, que fais-tu ?",
        pistes=[
            "Tu relis, tu demandes, tu laisses tomber ?",
            "À qui oses-tu demander, et à qui n'oses-tu pas ?",
            "As-tu déjà répondu à côté, faute d'avoir bien compris ?",
            "Qu'est-ce qui aurait aidé ?",
        ],
        notes="Beaucoup relisent trois fois plutôt que de demander. C'est le "
              "comportement que la séance vient corriger : demander coûte moins cher "
              "que relire.")

    d.dialogue('Dialogue · 1 de 3', "Deux ans, ça ne se raconte pas en trois lignes", [
        ("MARISOL", "Ousmane ! C'est Marisol, de Saint-Hyacinthe. J'ai reçu ton courriel ce matin.", True),
        ("OUSMANE", "Marisol ! Ça fait deux ans. Tu l'as lu au complet ? Je me suis relu et je me suis dit que c'était long.", True),
        ("MARISOL", "Je l'ai lu deux fois. Et j'ai des questions, parce que je mêle l'ordre. La petite est née quand, exactement ?", True),
        ("OUSMANE", "Assia est née le 14 mars. On était encore sur la rue Perreault. On a déménagé après, en juin.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Faire noter les deux dates au tableau dès la première écoute. Elles "
             "servent à tout le bloc B.")

    d.dialogue('Dialogue · 2 de 3', "Vendue, mais habitée encore", [
        ("MARISOL", "Donc quand tu m'as écrit la dernière fois, en avril, vous n'aviez pas encore déménagé.", True),
        ("OUSMANE", "Non, mais la maison était déjà vendue. Quand je t'ai écrit, on l'avait déjà vendue, mais on habitait encore dedans.", True),
        ("MARISOL", "Bon. Et l'accident, c'est l'accident de qui ? J'ai compris que c'était toi, puis j'ai eu un doute.", True),
        ("OUSMANE", "Ce n'est pas moi. C'est mon beau-frère, celui qui travaille au garage avec moi. Il est tombé d'une plateforme en novembre.", True),
    ], notes="La deuxième réplique porte le plus-que-parfait du bloc. La faire "
             "répéter, puis demander : la vente vient avant ou après le courriel ?")

    d.dialogue('Dialogue · 3 de 3', "Ce qui s'était passé avant", [
        ("MARISOL", "Tu écris aussi que ta sœur était arrivée depuis un mois. Kadiatou, c'est ça ?", True),
        ("OUSMANE", "Kadiatou, oui. Elle est arrivée de Conakry en octobre. Quand mon beau-frère est tombé, elle venait de s'installer chez nous.", True),
        ("MARISOL", "Et les funérailles dont tu parles à la fin ? J'ai relu trois fois et je n'étais pas certaine.", True),
        ("OUSMANE", "De mon oncle Mamadou, au pays, en février. Je n'ai pas pu y aller. C'est la partie triste du courriel.", True),
    ], notes="Le reste du dialogue s'écoute sans être projeté — vingt répliques ne "
             "tiennent pas à l'écran. Demander ensuite ce qui est dit à la fin : "
             "l'autobus de 14 h 40, vendredi.")

    d.vocabulaire('Vocabulaire', "Les quatre mots du Défi 1", [
        ("un accident de travail", "Un évènement qui blesse quelqu'un pendant qu'il fait son métier."),
        ("une réadaptation", "La période où l'on réapprend à se servir d'une partie du corps blessée."),
        ("des retrouvailles", "Le moment où des gens qui ne s'étaient pas vus depuis longtemps se revoient."),
        ("un imprévu", "Une chose qui arrive sans avoir été annoncée et qui change les plans."),
    ], notes="« Des retrouvailles » est toujours au pluriel. « Un accident de "
             "travail » n'est pas un accident de la route : il ouvre d'autres droits, "
             "et le mot compte au Québec.")

    d.tableau('Analyse', "Sept dates, deux ans",
              ['Le moment', 'Ce qui est arrivé'],
              [["Le 14 mars", "la naissance d'Assia, rue Perreault"],
               ["En juin", "le déménagement à l'autre bout de la ville"],
               ["En octobre", "l'arrivée de Kadiatou, venue de Conakry"],
               ["En novembre", "la chute du beau-frère au garage"],
               ["En février", "le décès de l'oncle Mamadou, au pays"],
               ["En avril", "le retour au travail à temps partiel"]],
              cle=0,
              notes="Diapositive à photographier. Le courriel ne donne pas cet ordre : "
                    "il faut le reconstruire. C'est le travail du bloc B.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la conversation téléphonique.", [
        ("Assia est née le 14 mars.", "vrai"),
        ("La famille avait déménagé avant la naissance d'Assia.", "faux - le déménagement est en juin"),
        ("La maison était déjà vendue en avril.", "vrai"),
        ("C'est Ousmane qui est tombé de la plateforme.", "faux - c'est son beau-frère"),
        ("Kadiatou est arrivée après l'accident.", "faux - elle est arrivée en octobre, un mois avant"),
        ("Ousmane et sa sœur arrivent au terminus à 14 h 40.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le cinquième "
             "énoncé est celui qui sépare le groupe : il demande le calcul du "
             "plus-que-parfait, qu'on verra en B4.")

    d.billet(
        "Quelle question poserais-tu à Ousmane, toi ?",
        exemples=[
            "Une phrase.",
            "Une vraie question, sur ce que tu n'aurais pas compris.",
        ],
        notes="Deux minutes. Les questions servent en B2 : on les compare à celles "
              "que l'exercice pose sur le texte du courriel.")

    return d.save(dossier)
