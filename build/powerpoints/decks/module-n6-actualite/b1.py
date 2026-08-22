# -*- coding: utf-8 -*-
"""B1 · Ça vous regarde, mardi 8 h 10
Bloc B « Défi 1 · La chronique pratique » · couleur acier · 75 min.
Source : dialogue `t1`, exercices `t1vf` et `t1chiffres`, cartes FC_CARDS de
la tâche `t1`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Ça vous regarde, mardi 8 h 10",
        chapeau="Claudine Rousseau explique en huit minutes ce que la "
                "plupart des gens ignorent toute leur vie : quand la "
                "garantie du fabricant est finie, il en reste une autre, et "
                "personne ne te la vend.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 1. Annoncer la méthode des trois écoutes et "
                  "l'afficher : première écoute sans arrêter, pour le sujet ; deuxième "
                  "pour les chiffres ; troisième pour l'ordre des étapes. Elle sert aux "
                  "trois défis.")

    d.objectifs([
        "comprendre le sujet d'une chronique pratique dès la première "
        "écoute ;",
        "dire ce qu'est la garantie légale et à quel moment elle "
        "s'applique ;",
        "relever les chiffres exacts à la deuxième écoute ;",
        "employer les cinq mots de la garantie et des recours.",
    ], notes="Le deuxième objectif a une valeur qui dépasse le cours : plusieurs élèves "
             "ont déjà jeté un appareil réparable. Le dire sans dramatiser.")

    d.declencheur(
        'Observation', "Qu'est-ce que tu fais quand un appareil brise ?",
        pistes=[
            "As-tu déjà rapporté un appareil brisé au magasin ?",
            "Qu'est-ce qu'on t'a répondu ?",
            "Gardes-tu tes factures, et où ?",
            "Combien de temps une laveuse devrait-elle durer, selon toi ?",
        ],
        notes="La dernière question prépare toute la séance : le groupe donnera des "
              "chiffres très différents. C'est précisément ce que veut dire « durée "
              "raisonnable » : personne n'a le même chiffre, et la loi non plus.")

    d.dialogue('Chronique · 1 de 3', "Il vous en reste une autre", [
        ("THÉO", "Huit heures dix, c'est l'heure de Ça vous regarde. Claudine Rousseau, bonjour. Ce matin, vous voulez parler des appareils qui brisent trop vite.", True),
        ("CLAUDINE", "Bonjour Théo. Je veux surtout parler de ce que les gens ignorent : au Québec, quand la garantie du fabricant est expirée, il vous en reste une autre. Et celle-là, personne ne vous la vend, parce qu'elle est déjà dans la loi.", True),
        ("THÉO", "Vous parlez de la garantie légale.", True),
        ("CLAUDINE", "Exactement. La loi dit qu'un bien doit servir à l'usage normal auquel il est destiné, et qu'il doit y servir pendant une durée raisonnable.", True),
    ], consigne="Première écoute : ne rien noter, seulement écouter.",
       notes="Faire écouter diapositive masquée. Après l'écoute, une seule question : "
             "de quoi ça parle ? Ne rien demander de plus à la première écoute.")

    d.dialogue('Chronique · 2 de 3', "Raisonnable, ça veut dire combien ?", [
        ("THÉO", "Raisonnable, ça veut dire combien de temps ?", True),
        ("CLAUDINE", "Ça dépend, et c'est voulu. On regarde le prix payé, ce qui était écrit au contrat, et les conditions d'utilisation.", True),
        ("CLAUDINE", "Une laveuse à quatre cents dollars et une laveuse à quinze cents dollars n'ont pas la même durée raisonnable, même si elles lavent le même linge.", True),
        ("THÉO", "Donnez-nous un cas concret, parce que je sens que les gens ne le croient pas.", True),
    ], notes="« Ça dépend, et c'est voulu » : la faire répéter. Beaucoup d'élèves "
             "cherchent un nombre d'années et se découragent de ne pas le trouver. "
             "L'absence de chiffre est une protection, pas un flou.")

    d.dialogue('Chronique · 3 de 3', "Gardez vos factures", [
        ("CLAUDINE", "Prenons une laveuse de sept cent quatre-vingts dollars qui cesse de vidanger après trois ans. Le marchand vous dira que la garantie d'un an est finie.", True),
        ("CLAUDINE", "Il a raison sur la garantie du fabricant. Mais la garantie légale, elle, court encore, et c'est au marchand ou au fabricant de réparer.", True),
        ("THÉO", "Un dernier conseil avant la pause ?", True),
        ("CLAUDINE", "Gardez vos factures. Une photo de la facture dans votre téléphone, le jour de l'achat, c'est trente secondes qui peuvent valoir plusieurs centaines de dollars.", True),
    ], notes="Le conseil final est le plus applicable de tout le module. Proposer au "
             "groupe de le faire séance tenante avec une facture qu'ils ont sur eux.")

    d.regle("La garantie que personne ne te vend",
            "La garantie légale existe même quand celle du fabricant est expirée.",
            precision="Elle est écrite dans la Loi sur la protection du consommateur, "
                      "elle ne s'achète pas et elle ne se demande pas : elle est déjà "
                      "là. Un bien doit servir à son usage normal pendant une durée "
                      "raisonnable, compte tenu du prix payé, du contrat et des "
                      "conditions d'utilisation.",
            notes="Diapositive à photographier. C'est un fait vérifié auprès de l'Office "
                  "de la protection du consommateur, pas un élément du scénario. Le "
                  "distinguer clairement : un élève doit savoir ce qu'il peut répéter.")

    d.vocabulaire('Vocabulaire', "Les mots de la garantie et des recours", [
        ("la garantie légale", "La protection écrite dans la loi, qui existe même quand celle du fabricant est terminée."),
        ("une durée raisonnable", "Le temps pendant lequel un objet devrait fonctionner, compte tenu de son prix."),
        ("une pièce de rechange", "Le morceau qu'on commande pour remplacer celui qui a cassé."),
        ("une mise en demeure", "Une lettre où l'on raconte les faits, où l'on demande, et où l'on donne un délai."),
        ("un recours", "Le moyen prévu par la loi quand on n'obtient rien autrement."),
    ], notes="Cinq mots, avec l'article. « Une mise en demeure » fait peur : dire tout "
             "de suite que c'est une lettre ordinaire, pas un document d'avocat.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la chronique.", [
        ("La garantie légale s'achète en même temps que l'appareil.", "faux - elle est déjà dans la loi"),
        ("La loi fixe un nombre d'années précis pour la durée raisonnable.", "faux - et c'est voulu"),
        ("Le prix payé compte dans l'appréciation de la durée raisonnable.", "vrai"),
        ("Un délai de dix jours est habituellement considéré comme raisonnable.", "vrai"),
        ("Aux petites créances, il faut être représenté par un avocat.", "faux - on se représente seul"),
        ("Le dernier conseil de la chroniqueuse porte sur les factures.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la phrase entendue. Les deux premières "
             "sont les plus utiles hors du cours ; y revenir.")

    d.pratique('Relevé', "Deuxième écoute : les chiffres exacts",
               "Réécoutez et complétez. Vous pouvez arrêter et revenir en arrière.", [
        ("La chronique passe à ... heures dix.", "huit"),
        ("La laveuse de l'exemple a coûté sept cent ... dollars.", "quatre-vingts"),
        ("Elle a cessé de vidanger après ... ans.", "trois"),
        ("La garantie du fabricant durait ... an.", "un"),
        ("Un délai de ... jours est habituellement raisonnable.", "dix"),
        ("Les petites créances acceptent une réclamation de ... mille dollars ou moins.", "quinze"),
    ], corrige=True, cols=2,
       notes="Autoriser franchement les arrêts et les retours : c'est la consigne de la "
             "deuxième écoute, pas une triche. Faire écrire les nombres en lettres, "
             "c'est aussi de l'orthographe.")

    d.billet(
        "Nomme un appareil qui a brisé chez toi, et dis combien de temps il a duré.",
        exemples=[
            "Un appareil, un nombre d'années, c'est tout.",
            "On s'en servira en B2 pour discuter de la durée raisonnable.",
        ],
        notes="Deux minutes. Ramasser : les réponses donnent en B2 une série de cas "
              "réels, bien meilleurs que des exemples inventés.")

    return d.save(dossier)
