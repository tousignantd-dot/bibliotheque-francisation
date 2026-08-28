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
                "est maintenant capable de faire pendant son quart.",
        duree='60 minutes')

    d.titre(notes="Séance de bilan. Rendre tous les billets corrigés du module avant de "
                  "commencer : la progression d'un billet à l'autre se voit, et elle vaut "
                  "plus qu'un commentaire.")

    d.objectifs([
        "rassembler le vocabulaire du module en quatre familles ;",
        "réviser avec les cartes mémoire, seul ou à deux ;",
        "reformuler les points de langue en une phrase chacun ;",
        "évaluer honnêtement ce que je suis maintenant capable de faire.",
    ])

    d.vocabulaire('Famille · 1 de 4', "Le temps de travail", [
        ("un quart de travail", "Le bloc d'heures qu'on fait dans une journée."),
        ("un horaire", "Le tableau qui dit qui travaille, quel jour et à quelle heure."),
        ("une pause", "Le moment court où on arrête pour manger ou se reposer."),
        ("un congé", "Une journée sans travail — rien n'est écrit sur l'horaire."),
    ], notes="« Quart » est le mot que les élèves comprennent le plus mal : il n'a rien "
             "à voir avec le quart d'une heure. Le redire une dernière fois.")

    d.vocabulaire('Famille · 2 de 4', "Les gens et les lieux", [
        ("un chef d'équipe", "La personne qui donne les tâches et répond aux questions."),
        ("le vestiaire", "La pièce avec des casiers, où on se change avant de commencer."),
        ("un uniforme", "Les vêtements pareils que tous les employés portent."),
        ("poinçonner", "Marquer l'heure de son arrivée et de son départ sur une machine."),
    ], notes="« Poinçonner » est un mot d'ici. Ailleurs on dit « pointer » — les deux se "
             "comprennent, mais c'est le premier qui est affiché sur les machines.")

    d.vocabulaire('Famille · 3 de 4', "Demander et s'organiser", [
        ("aviser", "Prévenir quelqu'un à l'avance, pour qu'il ne soit pas surpris."),
        ("remplacer", "Faire le travail de quelqu'un qui n'est pas là."),
        ("échanger", "Donner une chose et prendre celle de l'autre à la place."),
        ("prêter", "Donner une chose pour un moment, en sachant qu'elle revient."),
    ], notes="« Aviser » est le verbe de la règle des trois jours. C'est celui qu'un "
             "employé doit connaître avant tous les autres.")

    d.vocabulaire('Famille · 4 de 4', "Les tâches", [
        ("une tâche", "Un travail précis, qui a un début et une fin."),
        ("une livraison", "Les boîtes de marchandise qu'un camion apporte au travail."),
        ("ranger", "Mettre chaque chose à la place où elle doit être."),
        ("éteindre", "Arrêter un appareil pour qu'il cesse de fonctionner."),
    ], notes="Ces quatre mots reviennent dans les consignes du défi 3 : les faire relire "
             "en même temps que les consignes notées au billet de D1.")

    d.tableau('Les points de langue', "Une phrase chacun",
              ['Le point', 'En une phrase'],
              [["les moments de la journée", "le matin, c'est chaque matin ; ce matin, c'est aujourd'hui"],
               ["de… à, jusqu'à, à partir de", "les deux bouts, la fin seule, le début seul"],
               ["l'heure écrite et l'heure dite", "on écrit 14 h, on dit deux heures"],
               ["les cinq mots de la question", "à quelle heure, quand, combien de temps, qui, où"]],
              cle=0,
              note="Cinq autres au tableau suivant.",
              notes="Faire reformuler chaque ligne par un élève différent avant "
                    "d'afficher la colonne de droite.")

    d.tableau('Les points de langue', "Une phrase chacun (suite)",
              ['Le point', 'En une phrase'],
              [["pouvoir, devoir, falloir", "la permission, mon obligation, la règle de la place"],
               ["permission ou aide", "qui va faire la chose : moi, ou vous"],
               ["répondre à une demande", "oui, non avec sa raison, ou « une minute »"],
               ["l'impératif", "le sujet disparaît, le verbe passe en premier"],
               ["où on en est", "c'est fait, je suis en train de, je vais le faire"]],
              cle=1,
              notes="La dernière ligne est celle que les élèves rapportent le plus "
                    "souvent comme utile dès la semaine suivante.")

    d.regle("Ce qu'il faut retenir du module",
            "Au début, je n'osais pas. Maintenant, je demande tout de suite.",
            precision="C'est Fabiola qui le dit, à la fin. Elle n'a pas "
                      "appris tout le vocabulaire d'une cuisine : elle a "
                      "appris à lire son horaire, à demander, et à redire "
                      "ce qu'elle a compris. C'est ce qui fait tenir un "
                      "emploi.",
            notes="Diapo à photographier. C'est la phrase de clôture du module. La lire, "
                  "laisser un silence, et enchaîner sur l'autoévaluation sans "
                  "commentaire.")

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
            "Je peux nommer les lieux et les objets de mon travail.",
            "Je peux lire mon quart sur l'horaire et le dire à voix haute.",
            "Je peux demander une permission ou de l'aide, et donner ma raison.",
            "Je peux comprendre une consigne, la noter et dire où j'en suis.",
        ],
        notes="L'autoévaluation complète est dans l'activité interactive. La faire "
              "remplir là : elle est conservée avec les traces de l'élève, et "
              "l'enseignante la retrouve sur la fiche.")

    return d.save(dossier)
