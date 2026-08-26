# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots.
Bloc E « Je me lance » · couleur framboise · 60 min.
Source : cartes mémoire, banc de vocabulaire et autoévaluation du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre='Je retiens des mots',
        chapeau="Seize mots, sept points de langue, huit questions. Dernière "
                "séance : on rassemble, on révise, et chacun fait le point.",
        duree='60 minutes')

    d.titre(notes="Séance de bilan. Rendre tous les billets corrigés du module avant de "
                  "commencer.")

    d.objectifs([
        "rassembler le vocabulaire du module en quatre familles ;",
        "réviser avec les cartes mémoire, seul ou à deux ;",
        "reformuler les points de langue en une phrase chacun ;",
        "évaluer honnêtement ce que je suis maintenant capable de faire.",
    ])

    d.vocabulaire('Famille · 1 de 4', "Les vêtements", [
        ("un manteau", "Le grand vêtement du dessus, pour sortir dehors."),
        ("une tuque", "Le chapeau de laine qui couvre les oreilles."),
        ("un chandail", "Le vêtement du haut du corps."),
        ("des bottes", "Les chaussures hautes qui protègent de la neige."),
    ], notes="« Tuque » est un mot d'ici : ailleurs on dirait « bonnet ». Le faire "
             "remarquer, sans en faire une leçon.")

    d.vocabulaire('Famille · 2 de 4', "La couleur et le motif", [
        ("rayé", "Se dit d'un tissu à lignes. Le contraire est « uni »."),
        ("foncé", "Se dit d'une couleur proche du noir. Le contraire est « pâle »."),
        ("uni", "D'une seule couleur, sans dessin."),
        ("à pois", "Avec des petits ronds répétés sur le tissu."),
    ], notes="Faire donner un exemple de chacun à partir de ce que porte le groupe.")

    d.vocabulaire('Famille · 3 de 4', "La taille et l'essayage", [
        ("la taille", "La grandeur du vêtement : petit, moyen ou grand."),
        ("la pointure", "La grandeur de la chaussure — jamais « la taille »."),
        ("une cabine d'essayage", "La petite pièce fermée où on essaie."),
        ("un cintre", "Le crochet qui tient le vêtement suspendu."),
        ("serré", "Trop petit, qui presse le corps."),
    ], notes="« Linge » est le mot courant ici pour l'ensemble des vêtements : « acheter "
             "du linge », « laver son linge ».")

    d.vocabulaire('Famille · 4 de 4', "Le prix et l'entretien", [
        ("un rabais", "L'argent qu'on enlève du prix, quelques jours."),
        ("une étiquette de prix", "Le carton attaché au vêtement."),
        ("la liquidation", "La vente des derniers articles, à très bas prix."),
        ("une étiquette d'entretien", "L'étiquette du col, qui dit comment laver."),
        ("la sécheuse", "La machine chaude qui sèche le linge."),
        ("la facture", "Le papier qui prouve le prix payé."),
    ], notes="Ces six mots reviennent à chaque achat. Les faire répéter avec l'article.")

    d.tableau('Les points de langue', "Une phrase chacun",
              ['Le point', 'En une phrase'],
              [["le u et le ou", "la langue en avant, ou au fond"],
               ["un ou une", "le genre s'apprend avec le mot"],
               ["la couleur", "après le vêtement, et elle s'accorde"],
               ["taille ou pointure", "le corps ou le pied"]],
              cle=0,
              note="Trois autres au tableau suivant.",
              notes="Faire reformuler chaque ligne par un élève différent avant d'afficher "
                    "la colonne de droite.")

    d.tableau('Les points de langue', "Une phrase chacun (suite)",
              ['Le point', 'En une phrase'],
              [["comparer", "plus, moins ou aussi… et toujours « que »"],
               ["celui-ci, celui-là", "montrer sans répéter le nom"],
               ["l'étiquette d'entretien", "un dessin barré veut dire « ne pas faire »"]],
              cle=2,
              notes="La dernière ligne est celle que les élèves rapportent le plus souvent "
                    "comme utile à la maison.")

    d.regle("Ce qu'il faut retenir du module",
            "Nommer, demander, comparer. Rien de plus.",
            precision="Farida n'a pas appris le nom de tous les vêtements d'un magasin. "
                      "Elle a appris à dire ce qu'elle cherche avec sa couleur, à donner "
                      "sa taille ou à dire qu'elle ne la connaît pas, et à comparer deux "
                      "prix avant de choisir. C'est ce qui lui permet d'acheter seule, "
                      "dans n'importe quel magasin.",
            notes="Diapo à photographier. C'est la phrase de clôture du module.")

    d.cartes('Réviser seul', "Trois façons de le faire", [
        ("Les cartes mémoire",
         "Dans l'activité interactive, section « Je retiens des mots ». La traduction est "
         "masquée par défaut."),
        ("Les trois exercices de vocabulaire",
         "Le mot et sa définition, le mot et l'image, le mot à écrire. Les mêmes seize "
         "mots."),
        ("Les sept mini-leçons",
         "Sept panneaux « Ouvrir la mini-leçon », avec de l'audio. Ils restent accessibles "
         "après la fin du module."),
    ], notes="Montrer les trois à l'écran, une minute chacun.")

    d.billet(
        "Autoévaluation : pour chaque énoncé, pas encore, un peu, ou oui.",
        exemples=[
            "Je peux nommer les vêtements de l'hiver et dire leur couleur.",
            "Je peux dire ma taille, ou dire que je ne la connais pas.",
            "Je peux comparer deux prix : plus cher que, moins cher que.",
            "Je comprends les dessins de l'étiquette d'entretien.",
        ],
        notes="L'autoévaluation complète est dans l'activité interactive. La faire remplir "
              "là : elle est conservée avec les traces de l'élève.")

    return d.save(dossier)
