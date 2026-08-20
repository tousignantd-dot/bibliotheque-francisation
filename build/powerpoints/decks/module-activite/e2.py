# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots.
Bloc E « Je me lance » · couleur foret · 60 min.
Source : cartes mémoire, banc de vocabulaire et autoévaluation du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='foret',
        titre='Je retiens des mots',
        chapeau="Quinze mots, sept points de langue, six questions. Dernière "
                "séance : on rassemble, on révise, et chacun fait le point sur "
                "ce qu'il sait maintenant faire.",
        duree='60 minutes')

    d.titre(notes="Séance de bilan. Rendre tous les billets corrigés du module avant de "
                  "commencer.")

    d.objectifs([
        "rassembler le vocabulaire du module en quatre familles ;",
        "réviser avec les cartes mémoire, seul ou à deux ;",
        "reformuler les points de langue en une phrase chacun ;",
        "évaluer honnêtement ce que je suis maintenant capable de faire.",
    ])

    d.vocabulaire('Famille · 1 de 4', "S'inscrire", [
        ("une inscription", "L'action de s'enregistrer pour une activité."),
        ("un dépliant", "La brochure qui présente les activités de la ville."),
        ("le tarif", "Le prix demandé."),
        ("une preuve de résidence", "Un document récent à son nom, avec l'adresse."),
        ("une session", "La période pendant laquelle l'activité a lieu."),
    ], notes="Faire redire l'article avec chaque mot. Dernière occasion de le corriger.")

    d.vocabulaire('Famille · 2 de 4', "À la piscine", [
        ("un moniteur", "La personne qui dirige l'activité."),
        ("un maillot de bain", "Le vêtement pour se baigner."),
        ("un bonnet de bain", "Obligatoire dans plusieurs piscines d'ici."),
        ("un vestiaire", "La pièce où on se change."),
        ("une planche", "La mousse qu'on tient devant soi pour apprendre à nager."),
    ], notes="Ces cinq mots servent dès la première inscription. Les faire employer dans "
             "une phrase complète.")

    d.vocabulaire('Famille · 3 de 4', "Les consignes", [
        ("une consigne", "Une instruction donnée par la personne qui dirige."),
        ("obligatoire", "Sans cela, on ne peut pas participer."),
        ("recommandé", "C'est un conseil, pas une condition."),
        ("fourni", "C'est donné sur place : rien à acheter."),
        ("un bénévole", "Une personne qui aide sans être payée."),
    ], notes="Les trois adjectifs du milieu reviennent partout, bien au-delà des loisirs.")

    d.vocabulaire('Famille · 4 de 4', "Lire le dépliant", [
        ("la légende", "L'explication des symboles, en bas de la page."),
        ("une place disponible", "Une place encore libre."),
        ("une chorale", "Un groupe de personnes qui chantent ensemble."),
        ("un résident", "Une personne qui habite la ville ; elle paie moins cher."),
        ("une reprise", "Un cours refait plus tard pour remplacer un cours manqué."),
    ], notes="« Résident » et « légende » sont les deux mots administratifs du module. "
             "Dernier rappel.")

    d.tableau('Les points de langue', "Une phrase chacun",
              ['Le point', 'En une phrase'],
              [["les chiffres", "attends la fin du mot, puis fais répéter"],
               ["il faut, il est important de", "une condition arrive : note-la"],
               ["le superlatif", "le, la ou les devant plus ou moins"]],
              cle=1,
              note="Quatre autres au tableau suivant.",
              notes="Faire reformuler chaque ligne par un élève différent avant d'afficher "
                    "la colonne de droite.")

    d.tableau('Les points de langue', "Une phrase chacun (suite)",
              ['Le point', 'En une phrase'],
              [["l'impératif avec un pronom", "affirmatif : après. négatif : avant"],
               ["chaque, plusieurs, quelques", "seul chaque demande le singulier"],
               ["lire un dépliant", "commence par ce qui t'élimine"],
               ["le registre", "les deux sont du bon français"]],
              cle=0,
              notes="La dernière ligne est celle qui a le plus marqué le groupe. La faire "
                    "répéter.")

    d.regle("Ce qu'il faut retenir du module",
            "Savoir quoi demander vaut mieux que tout comprendre.",
            precision="Rosa n'a pas appris le français en une session. Elle a appris six "
                      "questions, et à répéter les réponses avant de partir. C'est ce qui "
                      "lui a permis d'inscrire son garçon et de se trouver une activité "
                      "à elle.",
            notes="Diapo à photographier. C'est la phrase de clôture du module.")

    d.cartes('Réviser seul', "Trois façons de le faire", [
        ("Les cartes mémoire",
         "Dans l'activité interactive, section « Je retiens des mots ». La traduction est "
         "masquée par défaut."),
        ("Les trois exercices de vocabulaire",
         "Le mot et sa définition, le mot et l'image, le mot à écrire. Les mêmes quinze "
         "mots."),
        ("Les sept mini-leçons",
         "Sept panneaux « En apprendre plus », avec de l'audio. Ils restent accessibles "
         "après la fin du module."),
    ], notes="Montrer les trois à l'écran, une minute chacun.")

    d.billet(
        "Autoévaluation : pour chaque énoncé, pas encore, un peu, ou oui.",
        exemples=[
            "Je peux m'informer sur une activité : horaire, tarif, matériel, documents.",
            "Je comprends les consignes d'un moniteur, même dites vite.",
            "Je peux lire un dépliant de ma ville et trouver ce que je cherche.",
        ],
        notes="L'autoévaluation complète est dans l'activité interactive. La faire remplir "
              "là : elle est conservée avec les traces de l'élève.")

    return d.save(dossier)
