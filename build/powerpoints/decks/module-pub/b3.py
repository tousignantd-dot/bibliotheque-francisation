# -*- coding: utf-8 -*-
"""B3 · Le slogan.
Bloc B · couleur foret (vocabulaire) · 60 min.
Source : exercices `t1slogan` et `t1deviner`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='foret',
        titre='Le slogan',
        chapeau="« Rien ne se jette, tout se répare. » Cinq mots, et l'atelier tout "
                "entier tient dedans. Un bon slogan ne décrit pas un service : il "
                "donne une raison d'y croire.",
        duree='60 minutes')

    d.titre(notes="Écrire au tableau trois slogans connus du groupe, dans n'importe "
                  "quelle langue. Demander pourquoi on s'en souvient. Les réponses "
                  "donneront la leçon.")

    d.objectifs([
        "reconnaître un slogan et sa place dans une publicité ;",
        "associer un slogan à un produit ou à un service ;",
        "repérer la valeur portée par un slogan ;",
        "écrire un slogan court et facile à retenir.",
    ])

    d.regle('La définition',
            "Une phrase courte, facile à retenir, placée le plus souvent à la fin.",
            precision="Le slogan ne nomme pas toujours le produit. Il met en avant une "
                      "idée ou une valeur : c'est ce qui le rend mémorable. « Rien ne se "
                      "jette, tout se répare » ne dit ni l'atelier, ni la date, ni "
                      "l'adresse.",
            notes="Écrire la définition au tableau. Faire vérifier sur les slogans donnés "
                  "par le groupe : combien nomment le produit ?")

    d.cartes('Analyse', "Quatre qualités d'un bon slogan", [
        ("Il est court",
         "Cinq à huit mots. Assez court pour être dit d'une traite et retenu après une "
         "seule écoute."),
        ("Il a un rythme",
         "« Rien ne se jette, tout se répare. » Deux moitiés de même longueur, qui se "
         "répondent. C'est ce qui le fixe dans la mémoire."),
        ("Il porte une idée",
         "Pas une description. « Réparez aujourd'hui, gardez pour longtemps » propose "
         "une façon de voir, pas une liste de services."),
        ("Il se dit à voix haute",
         "Un slogan qu'on n'arrive pas à prononcer d'un trait est trop long ou mal "
         "construit. Le test se fait toujours à voix haute."),
    ], notes="La quatrième carte est le test pratique. Faire dire à voix haute chaque "
             "slogan de la séance : ceux qui accrochent se sentent tout de suite.")

    d.pratique('Pratique · 1 de 4', "Associez le slogan et le service",
               "Huit slogans, huit services.", [
        ("Réparez aujourd'hui, gardez pour longtemps.", "un atelier de réparation"),
        ("On s'occupe de vos pneus, occupez-vous de la route.", "un garage"),
        ("Le pain d'ici, chaque matin.", "une boulangerie"),
        ("Une deuxième vie pour vos vêtements.", "une friperie"),
        ("Vos plantes vous diront merci.", "un terreau de jardinage"),
        ("Dormez, nous veillons sur la maison.", "un système d'alarme"),
    ], corrige=True,
       notes="Faire chercher, dans chaque slogan, le mot qui met sur la piste. Il y en a "
             "toujours un : pneus, pain, vêtements, plantes.")

    d.pratique('Pratique · 2 de 4', "Deux slogans de plus",
               "Le service n'est jamais nommé.", [
        ("Deux mille livres vous attendent, sans un sou.", "une bibliothèque"),
        ("Sortez du froid, entrez au chaud.", "un café de quartier"),
        ("Rien ne se jette, tout se répare.", "un atelier de réparation de quartier"),
        ("Vos vieux outils ont encore du travail.", "un service de prêt d'outils"),
    ], corrige=True,
       notes="Aucun de ces quatre ne nomme le service. C'est ce qui les rend "
             "intéressants : ils demandent un petit effort, et l'effort fait retenir.")

    d.tableau('Analyse', "Le slogan et la valeur qu'il porte",
              ['Le slogan', 'La valeur'],
              [["Rien ne se jette, tout se répare.", "l'écologie"],
               ["Vos vieux outils ont encore du travail.", "la simplicité"],
               ["Sortez du froid, entrez au chaud.", "l'ouverture à l'autre"],
               ["Vos mains savent plus que vous croyez.", "l'autonomie"],
               ["Dormez, nous veillons sur la maison.", "la sécurité"]],
              cle=0, props=[0.62, 0.38],
              notes="Relier à la séance A4 : le slogan est l'endroit où la valeur se "
                    "condense en une phrase.")

    d.piege("Le piège du slogan qui décrit",
            "Atelier de réparation gratuit ouvert le samedi de 9 h à 16 h.",
            "Rien ne se jette, tout se répare.",
            "Une description n'est pas un slogan : elle donne des faits, que l'affiche "
            "porte déjà. Le slogan doit ajouter quelque chose — une idée, une image, une "
            "raison. Sinon, il est inutile.",
            notes="Faire transformer trois descriptions en slogans. C'est difficile, et "
                  "c'est justement l'exercice.")

    d.piege("Le piège du slogan trop long",
            "Venez réparer vos objets brisés avec nos bénévoles au centre du quartier.",
            "Rien ne se jette, tout se répare.",
            "Au-delà de huit ou dix mots, un slogan cesse d'être retenu : il devient une "
            "phrase ordinaire. Comptez les mots. Si vous ne pouvez pas le dire d'un seul "
            "souffle, il est trop long.",
            notes="Faire compter les mots de chaque slogan de la séance. Aucun ne dépasse "
                  "huit.")

    d.pratique('Pratique · 3 de 4', "Devinez le service",
               "Le slogan ne le nomme pas.", [
        ("« Rien ne se jette, tout se répare. »", "un atelier de réparation"),
        ("« Vos vieux outils ont encore du travail. »", "un prêt d'outils"),
        ("« Le froid dehors, la chaleur dedans. »", "un manteau d'hiver"),
        ("« Vos mains savent plus que vous croyez. »", "un salon des métiers manuels"),
    ], corrige=True,
       notes="Plusieurs réponses se défendent. Accepter toute proposition justifiée : "
             "c'est le raisonnement qu'on évalue.")

    d.pratique('Pratique · 4 de 4', "Écrivez un slogan",
               "Cinq à huit mots. Un rythme, une idée.", [
        ("Un atelier de couture de quartier", "Ce qui est déchiré peut être recousu."),
        ("Une bibliothèque d'outils", "Empruntez la scie, gardez le savoir-faire."),
        ("Un café communautaire", "Un café, une place, tout le monde."),
        ("Votre propre événement", "celui de votre billet de A1"),
    ], corrige=True,
       notes="Les corrigés sont des exemples, pas des modèles à copier. Les slogans du "
             "groupe seront souvent meilleurs.")

    d.billet(
        "Écrivez deux slogans pour votre événement.",
        exemples=[
            "Cinq à huit mots chacun.",
            "Dites-les à voix haute avant de les écrire. Gardez celui qui se dit le "
            "mieux.",
        ],
        notes="Ramasser. Les slogans seront repris en E1, dans la capsule complète. "
              "Demander de garder le brouillon.")

    return d.save(dossier)
