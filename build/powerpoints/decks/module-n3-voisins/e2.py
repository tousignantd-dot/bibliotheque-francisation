# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots.
Bloc E « Je me lance » · couleur framboise · 60 min.
Source : cartes mémoire, mini-leçons et autoévaluation du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre='Je retiens des mots',
        chapeau="Seize mots, neuf points de langue. Dernière séance : on "
                "rassemble, on révise, et chacun fait le point sur ce qu'il "
                "est maintenant capable de faire dans son immeuble.",
        duree='60 minutes')

    d.titre(notes="Séance de bilan. Rendre tous les billets corrigés du module avant de "
                  "commencer : la progression d'un billet à l'autre est visible, et elle "
                  "vaut plus qu'un commentaire.")

    d.objectifs([
        "rassembler le vocabulaire du module en quatre familles ;",
        "réviser avec les cartes mémoire, seul ou à deux ;",
        "reformuler les points de langue en une phrase chacun ;",
        "évaluer honnêtement ce que je suis maintenant capable de faire.",
    ])

    d.vocabulaire('Famille · 1 de 4', "L'immeuble et les gens", [
        ("un voisin", "La personne qui habite à côté, ou dans le même immeuble."),
        ("un immeuble", "Un bâtiment à plusieurs logements, les uns sur les autres."),
        ("le palier", "Le petit espace plat devant les portes, entre deux escaliers."),
        ("le concierge", "Celui qui s'occupe de l'immeuble et qui a les clés."),
        ("faire connaissance", "Se parler pour la première fois."),
    ], notes="« Palier » et « concierge » sont les deux mots que les élèves n'ont jamais "
             "eu besoin de dire avant, et qu'ils emploieront toutes les semaines.")

    d.vocabulaire('Famille · 2 de 4', "Demander la permission", [
        ("la permission", "Le droit de faire quelque chose, donné par quelqu'un."),
        ("une remise", "Une petite construction fermée, dans la cour, où on range."),
        ("une corde à linge", "La corde tendue dehors pour sécher le linge."),
        ("déranger", "Gêner quelqu'un, l'empêcher de faire ce qu'il fait."),
    ], notes="« Déranger » est le mot d'ouverture de toute demande : « excusez-moi de "
             "vous déranger ». Le faire répéter dans la formule complète.")

    d.vocabulaire('Famille · 3 de 4', "Inviter", [
        ("une invitation", "Ce qu'on dit ou ce qu'on écrit pour demander à quelqu'un de venir."),
        ("fêter", "Marquer un jour heureux en se réunissant."),
        ("apporter", "Prendre une chose avec soi et l'amener où on va."),
        ("un compliment", "Une phrase gentille sur ce que quelqu'un a fait."),
    ], notes="« Apporter » et « amener » se confondent souvent : on apporte une chose, on "
             "amène une personne. Le dire sans en faire un exercice.")

    d.vocabulaire('Famille · 4 de 4', "Décrire ce qui se perd", [
        ("un trousseau de clés", "Plusieurs clés tenues ensemble sur un même anneau."),
        ("un collier", "La bande qu'un animal porte autour du cou."),
        ("une affiche", "Une feuille posée sur un mur pour que tout le monde la lise."),
    ], notes="Ces trois mots servent bien au-delà de l'immeuble : au poste de police, à "
             "l'école, au bureau des objets perdus.")

    d.tableau('Les points de langue', "Une phrase chacun",
              ['Le point', 'En une phrase'],
              [["se présenter", "le nom, puis l'étage"],
               ["demander la permission", "la raison d'abord, la demande ensuite"],
               ["le, la, les, lui", "un petit mot avant le verbe, pour ne rien répéter"],
               ["les trois renseignements", "le jour, l'heure, l'endroit"]],
              cle=0,
              note="Cinq autres au tableau suivant.",
              notes="Faire reformuler chaque ligne par un élève différent avant "
                    "d'afficher la colonne de droite.")

    d.tableau('Les points de langue', "Une phrase chacun (suite)",
              ['Le point', 'En une phrase'],
              [["les deux futurs", "on dit « je vais », on écrit « il y aura »"],
               ["accepter ou refuser", "un refus se donne avec sa raison"],
               ["le compliment", "il porte sur ce qu'on a fait, pas sur ce qu'on est"],
               ["l'adjectif", "il s'accorde, et il se place après — sauf sept"],
               ["très, assez, un peu, trop", "devant l'adjectif, et « trop » signale un problème"]],
              cle=1,
              notes="La ligne du compliment est celle que les élèves rapportent le plus "
                    "souvent comme utile hors de la classe.")

    d.regle("Ce qu'il faut retenir du module",
            "Onze ans dans le même escalier, et jamais plus de dix secondes.",
            precision="Rachid et Manon se croisaient tous les jours sans se "
                      "parler. Ce qui a changé n'est pas leur français : "
                      "c'est qu'un des deux a posé une question. Demander "
                      "une permission, c'est aussi ouvrir une porte.",
            notes="Diapo à photographier. C'est la phrase de clôture du module. La lire, "
                  "laisser un silence, et enchaîner sur l'autoévaluation sans commentaire.")

    d.cartes('Réviser seul', "Trois façons de le faire", [
        ("Les cartes mémoire",
         "Dans l'activité interactive, section « Je retiens des mots ». La traduction est "
         "masquée par défaut."),
        ("Les trois exercices de vocabulaire",
         "Le mot et sa définition, le mot et l'image, le mot à écrire. Les mêmes seize "
         "mots."),
        ("Les neuf mini-leçons",
         "Neuf panneaux « Ouvrir la mini-leçon », avec de l'audio. Ils restent accessibles "
         "après la fin du module."),
    ], notes="Montrer les trois à l'écran, une minute chacun. Beaucoup d'élèves ignorent "
             "que le module reste ouvert après la dernière séance.")

    d.billet(
        "Autoévaluation : pour chaque énoncé, pas encore, un peu, ou oui.",
        exemples=[
            "Je peux me présenter à un voisin et présenter quelqu'un.",
            "Je peux demander une permission poliment et comprendre la réponse.",
            "Je peux inviter en donnant le jour, l'heure et l'endroit.",
            "Je peux décrire une personne, un animal ou un objet perdu.",
        ],
        notes="L'autoévaluation complète est dans l'activité interactive. La faire "
              "remplir là : elle est conservée avec les traces de l'élève, et "
              "l'enseignante la retrouve sur la fiche.")

    return d.save(dossier)
