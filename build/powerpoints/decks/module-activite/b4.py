# -*- coding: utf-8 -*-
"""B4 · Les conditions d'admission.
Bloc B · couleur acier · 60 min.
Source : exercice `t1cond`, cartes mémoire.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='acier',
        titre="Les conditions d'admission",
        chapeau="« Il reste trois places. » « Il n'y a pas de reprise. » « Les "
                "partitions sont fournies. » Chaque phrase cache une "
                "conséquence concrète — encore faut-il la voir.",
        duree='60 minutes')

    d.titre(notes="Séance de compréhension fine. Elle clôt le bloc B en reliant les formes "
                  "vues en B2 à ce qu'elles impliquent vraiment.")

    d.objectifs([
        "traduire une condition en conséquence concrète ;",
        "savoir ce qui m'empêche de participer et ce qui ne m'empêche pas ;",
        "reconnaître ce qu'une phrase ne dit pas ;",
        "nommer les cinq documents demandés le plus souvent.",
    ])

    d.tableau('Analyse', "Ce que la phrase implique vraiment",
              ['La phrase', 'Ce que ça veut dire pour moi'],
              [["Il faut une preuve de résidence.", "sans elle, je paie 25 $ de plus"],
               ["Le bonnet est obligatoire.", "sans lui, mon enfant n'entre pas"],
               ["Il n'y a pas de reprise.", "un cours manqué est perdu"],
               ["Il reste trois places.", "je m'inscris cette semaine"]],
              cle=1,
              note="La deuxième ligne est la seule qui empêche de participer le jour même.",
              notes="Diapo centrale. Faire trouver la conséquence par le groupe avant "
                    "d'afficher la colonne de droite.")

    d.cartes('Les cinq documents', "Ceux qu'on demande le plus souvent", [
        ("Une preuve de résidence",
         "Facture d'électricité, bail, relevé bancaire — n'importe quel document récent à "
         "son nom, avec l'adresse."),
        ("La carte d'assurance maladie",
         "Souvent demandée pour les activités sportives des enfants, en cas d'accident."),
        ("Un certificat de naissance",
         "Parfois demandé pour prouver l'âge d'un enfant dans une catégorie."),
        ("Une carte de citoyen",
         "Plusieurs villes en émettent une : elle remplace la preuve de résidence et donne "
         "accès aux tarifs réduits."),
    ], notes="La quatrième carte est très utile : beaucoup d'élèves ignorent que leur ville "
             "émet une carte de citoyen. Vérifier avant le cours et donner l'information.")

    d.regle("Ce qu'une phrase ne dit pas",
            "« Il n'y a pas de reprise » ne veut pas dire que le cours est perdu.",
            precision="Louise ajoute : « chaque cours reprend ce qui a été vu ». Une "
                      "information négative est souvent suivie d'une information "
                      "rassurante. Écoutez la suite avant de vous inquiéter.",
            notes="C'est une leçon d'écoute autant que de langue : ne pas s'arrêter à la "
                  "première moitié de la réponse.")

    d.piege("S'arrêter à la mauvaise nouvelle",
            "— Il n'y a pas de reprise. — Ah, alors ce n'est pas pour nous.",
            "— Il n'y a pas de reprise. — …mais chaque cours reprend ce qui a été vu.",
            "Beaucoup de réponses administratives commencent par une restriction et se "
            "terminent par une nuance. Couper après la restriction fait renoncer à des "
            "activités parfaitement accessibles.",
            notes="Faire jouer la paire à deux élèves. La différence d'issue est frappante.")

    d.pratique('Pratique', "Quelle conséquence ?",
               "Dites ce que la phrase change pour vous.", [
        ("« Il faut une preuve de résidence. »", "sans elle, je paie le tarif élevé"),
        ("« Le bonnet est obligatoire. »", "sans bonnet, pas d'entrée dans l'eau"),
        ("« Il est préférable que les parents restent dans la salle. »", "je peux entrer, mais on préfère que non"),
        ("« Il reste trois places. »", "je dois m'inscrire tout de suite"),
        ("« Les partitions sont fournies. »", "je n'ai rien à acheter"),
        ("« Il n'est pas nécessaire de venir en personne. »", "je peux m'inscrire en ligne"),
    ], corrige=True, cols=1,
       notes="Faire répondre à voix haute avant d'afficher. Les élèves trouvent presque "
             "toujours, mais lentement : c'est la vitesse qu'on travaille ici.")

    d.vocabulaire('Vocabulaire', "Les mots des conditions", [
        ("obligatoire", "Sans cela, on ne peut pas participer."),
        ("recommandé", "C'est un conseil, pas une condition."),
        ("fourni", "C'est donné sur place : rien à acheter."),
        ("une reprise", "Un cours refait plus tard, pour remplacer un cours manqué."),
        ("une place disponible", "Une place encore libre dans le groupe."),
    ], notes="Ces cinq mots reviennent dans tous les dépliants municipaux. Les élèves les "
             "reverront dans le banc de vocabulaire.")

    d.billet(
        "Trouvez une activité de votre ville et notez ses conditions d'admission.",
        exemples=[
            "L'âge, le niveau, les documents, le matériel obligatoire.",
            "Pour chacune, écrivez ce que ça change pour vous.",
        ],
        notes="Bilan du bloc B. Le travail se fait sur un dépliant réel ou sur le site de "
              "la ville — c'est le meilleur devoir du module.")

    return d.save(dossier)
