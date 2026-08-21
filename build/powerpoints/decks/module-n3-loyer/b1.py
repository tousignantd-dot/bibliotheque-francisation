# -*- coding: utf-8 -*-
"""B1 · Chauffé, éclairé, non meublé.
Bloc B « Défi 1 · Lire la petite annonce » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Chauffé, éclairé, non meublé',
        chapeau="Six lignes d'annonce, et tout y est : les pièces, ce qui est "
                "compris, la date, le prix. Encore faut-il savoir ce que les "
                "mots veulent dire ici.",
        duree='75 minutes')

    d.titre(notes="Première séance du bloc B. Ouvrir avec les billets de la séance A1 : "
                  "chacun sait maintenant combien de pièces il lui faut. La question du "
                  "jour est de savoir reconnaître ce chiffre dans une annonce.")

    d.objectifs([
        "comprendre ce que veut dire « chauffé » dans une annonce ;",
        "comprendre ce que veut dire « éclairé » ;",
        "comprendre ce que veut dire « non meublé » ;",
        "repérer le loyer et la date dans une annonce.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qui est compris dans votre loyer ?",
        pistes=[
            "Est-ce que vous payez le chauffage en plus, l'hiver ?",
            "Est-ce que vous recevez un compte d'électricité ?",
            "Est-ce qu'il y avait des meubles quand vous êtes arrivé ?",
            "Est-ce que vous le saviez avant de signer ?",
        ],
        notes="Plusieurs élèves découvriront qu'ils paient des choses qu'ils croyaient "
              "comprises. Ne pas en faire un drame : c'est précisément ce que la séance "
              "sert à éviter la prochaine fois.")

    d.dialogue('Dialogue · 1 de 3', "Voilà, rue Chabot, Villeray", [
        ("RACHID", "Voilà. « Quatre et demie à louer, rue Chabot, Villeray. »", True),
        ("DILNOZA", "Villeray, c'est loin d'ici ?", True),
        ("RACHID", "Vingt minutes en autobus. Continue : « deuxième étage, deux chambres fermées ».", True),
        ("DILNOZA", "Deux chambres. C'est ce que je cherche. Et après ?", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer que Dilnoza lit à voix haute et s'arrête à chaque mot "
             "qu'elle ne comprend pas. C'est la bonne méthode et il faut le dire : "
             "personne ne lit une annonce d'un trait la première fois.")

    d.dialogue('Dialogue · 2 de 3', "Chauffé, ça veut dire quoi ?", [
        ("RACHID", "« Cuisine avec balcon arrière. Chauffé, éclairé. Non meublé. »", True),
        ("DILNOZA", "Chauffé, ça veut dire quoi ?", True),
        ("RACHID", "Que le chauffage est payé par la propriétaire. Tu ne paies pas l'hiver.", True),
        ("DILNOZA", "Et éclairé ?", True),
        ("RACHID", "L'électricité est comprise aussi. C'est rare. C'est une bonne annonce.", True),
    ], notes="C'est le cœur de la séance. « Éclairé » ne parle pas de la lumière du "
             "jour : c'est le mot que tout le monde comprend de travers. Le répéter "
             "deux fois, puis le faire reformuler par un élève.")

    d.dialogue('Dialogue · 3 de 3', "Le premier juillet", [
        ("DILNOZA", "Et ici, en bas ? « Libre le 1er juillet. Onze cent cinquante dollars. »", True),
        ("RACHID", "Le loyer, c'est mille cent cinquante dollars par mois. Chauffage compris.", True),
        ("DILNOZA", "Le premier juillet… C'est dans deux mois.", True),
        ("RACHID", "C'est la date de déménagement au Québec. Presque tout le monde bouge ce jour-là.", True),
    ], notes="Le 1er juillet est un fait local qui surprend toujours : la plupart des "
             "baux vont du 1er juillet au 30 juin, et les camions de déménagement sont "
             "réservés des mois d'avance. Le dire.")

    d.tableau('Analyse', "Trois mots d'annonce, et ce qu'ils coûtent",
              ["Le mot", "Ce que ça veut dire"],
              [["chauffé", "le chauffage est payé par le propriétaire"],
               ["éclairé", "l'électricité est comprise dans le loyer"],
               ["non meublé", "aucun meuble : on apporte tout"],
               ["non chauffé", "le chauffage est à votre charge, l'hiver"]],
              cle=1,
              note="Éclairé ne parle pas de la lumière du soleil.",
              notes="Diapositive à photographier. Ces quatre lignes suffisent à calculer "
                    "le vrai prix d'un logement. Faire recopier telles quelles.")

    d.regle("Le nombre écrit en gros n'est pas le prix",
            "Le prix, c'est le loyer plus ce qui n'est pas compris",
            precision="Deux logements affichés à 1 150 $ peuvent coûter cent "
                      "trente dollars de différence par mois. Avant de "
                      "comparer, il faut ramener les deux au même point : le "
                      "loyer, plus le chauffage et l'électricité s'ils ne sont "
                      "pas compris.",
            notes="Diapositive à photographier. Faire le calcul au tableau avec deux "
                  "annonces au même prix affiché : c'est la démonstration la plus utile "
                  "de tout le bloc B.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le logement est dans le quartier Villeray.", "vrai"),
        ("« Chauffé » veut dire que le chauffage est payé par la propriétaire.", "vrai"),
        ("« Éclairé » veut dire qu'il y a beaucoup de fenêtres.", "faux — l'électricité est comprise"),
        ("Le logement est meublé.", "faux — non meublé"),
        ("Le loyer est de mille cent cinquante dollars.", "vrai"),
        ("Le logement est libre le premier juillet.", "vrai"),
    ], corrige=True,
       notes="C'est l'exercice 1 du Défi 1. Faire justifier chaque « faux » par la "
             "réplique exacte du dialogue.")

    d.billet(
        "Écrivez ce qui est compris dans votre loyer et ce que vous payez en plus.",
        exemples=[
            "Dans mon loyer, ___ est compris.",
            "Je paie ___ en plus.",
        ],
        notes="Devoir court. Plusieurs élèves ne le sauront pas : leur dire de regarder "
              "leur bail ou de demander à leur propriétaire. Les réponses servent à la "
              "séance B3.")

    return d.save(dossier)
