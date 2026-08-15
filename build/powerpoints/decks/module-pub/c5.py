# -*- coding: utf-8 -*-
"""C5 · Le Rendez-vous des mains habiles.
Bloc C · couleur teal (lire et répondre) · 60 min.
Source : exercice `aSalon` — analyser une publicité complète.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C5', section='teal',
        titre='Le Rendez-vous des mains habiles',
        chapeau="Une publicité de salon, plus longue que les affiches du quartier. Tout "
                "ce qu'on a appris s'y applique d'un coup : les quatre éléments, les "
                "valeurs, le slogan.",
        duree='60 minutes')

    d.titre(notes="Séance de synthèse du défi 2. Distribuer le texte et laisser lire cinq "
                  "minutes sans consigne : on veut d'abord une lecture ordinaire.")

    d.objectifs([
        "analyser une publicité avec les quatre éléments ;",
        "relever les informations pratiques ;",
        "choisir un slogan qui convient au message ;",
        "nommer les valeurs mises en avant.",
    ])

    d.cartes('Le texte', "Le Rendez-vous des mains habiles", [
        ("Quand et où",
         "Du 3 au 5 octobre, à l'aréna de Beauport."),
        ("Ce qu'on y trouve",
         "Trente artisans vous ouvrent leur atelier : ébénisterie, poterie, remise en "
         "état de meubles, couture."),
        ("Ce qu'on peut faire",
         "Essayez le tour de potier et repartez avec votre première pièce."),
        ("Les conditions",
         "Les ateliers pour débutants sont gratuits pour les moins de 16 ans. "
         "Information : mainshabiles.qc.ca"),
    ], notes="Faire remarquer la troisième carte : « repartez avec votre première "
             "pièce ». C'est une promesse concrète, comme dans La Nuit des ateliers.")

    d.pratique('Pratique · 1 de 4', "Les informations pratiques",
               "Répondez d'après le texte.", [
        ("Comment s'appelle l'événement ?", "Le Rendez-vous des mains habiles"),
        ("À quel endroit se tient-il ?", "à l'aréna de Beauport"),
        ("Combien d'artisans y participent ?", "trente"),
        ("Pendant quelles dates ?", "du 3 au 5 octobre"),
        ("Qu'est-ce qui est gratuit, et pour qui ?",
         "les ateliers pour débutants, pour les moins de 16 ans"),
        ("Où trouver plus d'information ?", "sur mainshabiles.qc.ca"),
    ], corrige=True,
       notes="Six questions, six réponses dans le texte. Faire pointer chaque fois la "
             "phrase exacte.")

    d.pratique('Pratique · 2 de 4', "Les quatre éléments",
               "Émetteur, récepteur, message, canal.", [
        ("L'émetteur", "les organisateurs du salon — le nom du site le confirme"),
        ("Le récepteur", "les gens curieux des métiers manuels, et les familles"),
        ("Le message", "un salon de trois jours où trente artisans ouvrent leur atelier"),
        ("Le canal", "une publicité écrite — affiche, journal ou site"),
    ], corrige=True,
       notes="Le récepteur demande une déduction : « gratuits pour les moins de 16 ans » "
             "indique que les jeunes sont visés.")

    d.pratique('Pratique · 3 de 4', "Quel slogan conviendrait ?",
               "Quatre propositions. Laquelle, et pourquoi ?", [
        ("« Le confort d'abord »", "non — rien à voir avec le sujet"),
        ("« Vos mains savent plus que vous croyez »", "oui — l'autonomie, les métiers manuels"),
        ("« Roulez plus loin »", "non — c'est un slogan de garage ou de vélo"),
        ("« Dormez sur vos deux oreilles »", "non — c'est la sécurité, pas le sujet"),
    ], corrige=True,
       notes="Faire justifier le rejet des trois autres autant que le choix du bon. C'est "
             "là que le raisonnement se voit.")

    d.pratique('Pratique · 4 de 4', "Les valeurs du salon",
               "Deux valeurs, avec ce qui vous les a fait deviner.", [
        ("Première valeur", "l'autonomie — on apprend à faire soi-même"),
        ("Deuxième valeur", "la découverte — on essaie le tour de potier"),
        ("Une troisième possible", "le partage — les artisans ouvrent leur atelier"),
        ("Ce qui n'est pas une valeur ici", "la sécurité, le confort, la rapidité"),
    ], corrige=True,
       notes="Le quatrième item est utile : nommer ce qui n'y est pas aide à préciser ce "
             "qui y est.")

    d.piege("Le piège du slogan qui sonne bien",
            "« Le confort d'abord » — ça sonne bien, je le prends.",
            "Un slogan doit correspondre au message et à la valeur.",
            "Un slogan bien tourné mais hors sujet ne sert à rien : il fait penser à "
            "autre chose. Vérifiez toujours qu'il porte la valeur de la publicité — "
            "ici, l'autonomie et la découverte, pas le confort.",
            notes="Faire relire les quatre propositions et demander à quoi chacune ferait "
                  "penser. L'exercice est rapide et parlant.")

    d.piege("Le piège de l'information incomplète",
            "C'est gratuit, j'emmène toute la famille.",
            "Gratuit pour les moins de 16 ans, et seulement les ateliers débutants.",
            "Deux limites dans une seule phrase : l'âge, et le type d'atelier. Une "
            "publicité place souvent le mot « gratuit » en évidence et les conditions "
            "juste après. Lisez la phrase entière.",
            notes="C'est le même piège qu'en C1. Le répéter volontairement : c'est une "
                  "habitude de lecture, et une habitude demande des répétitions.")

    d.regle('La règle du défi 2',
            "Une publicité se lit à trois niveaux : les faits, la promesse, la valeur.",
            precision="Les faits : trente artisans, du 3 au 5 octobre, à Beauport. La "
                      "promesse : repartez avec votre première pièce. La valeur : vos "
                      "mains savent plus que vous croyez. Les trois ensemble font une "
                      "publicité complète.",
            notes="C'est la synthèse du défi. L'écrire au tableau : elle servira "
                  "directement en E1.")

    d.billet(
        "Analysez une publicité de votre choix aux trois niveaux.",
        exemples=[
            "Les faits, la promesse, la valeur.",
            "N'importe quelle publicité vue cette semaine.",
        ],
        notes="Ramasser. Ces analyses montrent si les trois niveaux sont acquis, et elles "
              "préparent directement la production de E1.")

    return d.save(dossier)
