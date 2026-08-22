# -*- coding: utf-8 -*-
"""E2 · L'avis à la porte, et les seize mots
Bloc E « Je me lance » · couleur framboise · 75 min.
Production écrite, puis bilan du module.
Source : bloc « Je me lance » (l'avis affiché au Centre) et « Je retiens
des mots ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="L'avis à la porte, et les seize mots",
        chapeau="Dernière séance. Vous écrivez l'avis que les gens liront "
                "demain matin en entrant, debout, leur manteau sur le bras. "
                "Puis on rassemble les mots du module et on fait le point.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Prévoir quarante minutes d'écriture en "
                  "silence, puis le bilan. Rendre au début les billets de E1 et les "
                  "rétroactions des productions orales : la comparaison est le vrai "
                  "moment d'apprentissage de la séance.")

    d.objectifs([
        "écrire un avis qui annonce une décision et sa raison ;",
        "employer le futur simple pour la date, l'heure et le lieu ;",
        "donner deux consignes à l'impératif, dont une avec un gérondif ;",
        "faire le point sur ce qu'on est maintenant capable de faire.",
    ], notes="Le troisième objectif relie les deux moitiés du module : le Défi 2 "
             "donne la décision, le Défi 3 donne l'équipement. L'avis est le seul "
             "endroit où les deux se rencontrent.")

    d.regle("Un avis se lit debout, en trente secondes",
            "La décision d'abord. La météo ensuite, jamais l'inverse.",
            precision="Quelqu'un qui entre avec son manteau sur le bras ne lira pas "
                      "trois phrases de contexte avant de savoir si sa sortie a lieu. "
                      "De six à neuf phrases, avec « vous », et la nouvelle est dans "
                      "la première.",
            notes="Diapositive à photographier. Écrire au tableau deux premières "
                  "phrases — une qui commence par la météo, une qui commence par la "
                  "décision — et faire choisir. Le groupe choisit toujours la "
                  "seconde, et c'est l'argument.")

    d.tableau('L\'avis', "Six exigences, annoncées d'avance",
              ["La partie", "Ce qu'on y met"],
              [["La première phrase", "la décision — pas la météo"],
               ["La raison", "étant donné que, comme, ou parce que"],
               ["Le nom exact de l'avis", "veille ou avertissement, et de quoi"],
               ["Deux phrases au futur", "la nouvelle date, l'heure, le lieu"],
               ["Deux consignes", "à l'impératif, dont une avec un gérondif"],
               ["La fin", "quoi faire si la date ne convient pas, et votre nom"]],
              cle=1,
              notes="Annoncer les critères avant l'écriture, jamais après. Un élève "
                    "qui sait qu'on regarde le gérondif en écrit un ; celui qui "
                    "l'apprend à la correction se sent piégé. Ce sont les six points "
                    "de la liste en ligne.")

    d.piege("Commencer par la météo",
            "Environnement Canada a émis un avertissement…",
            "La marche du samedi 8 est reportée au samedi 22 février.",
            "Le premier avis se lit dans l'ordre où l'information est arrivée à "
            "celui qui l'écrit. Le second se lit dans l'ordre où elle intéresse "
            "celui qui la reçoit. Le contexte vient après la nouvelle, toujours.",
            notes="C'est la faute la plus fréquente de cette production, et elle "
                  "n'est pas une faute de langue : c'est une faute de destinataire. "
                  "La nommer ainsi aide les élèves à la voir.")

    d.cartes("Ce que le correcteur regarde", "Quatre points, et vous les connaissez", [
        ("La décision est complète",
         "Reportée à quelle date, à quelle heure, à quel endroit. Les trois."),
        ("Une raison, avec un connecteur",
         "Une seule, la plus forte, reliée à la décision dans la même phrase."),
        ("Les temps sont justes",
         "Futur simple pour ce qui est fixé ; présent pour la décision déjà prise."),
        ("Consigne et manière",
         "Un impératif pour ce qu'il faut apporter, un gérondif pour le comment."),
    ], notes="Quatre points seulement. Un avis d'élève qui les porte tous est "
             "publiable tel quel dans un vrai centre communautaire — le dire au "
             "groupe, parce que c'est vrai.")

    d.vocabulaire('Bilan du vocabulaire', "Huit des seize mots, une dernière fois", [
        ("une veille", "L'avis qui dit que le phénomène est possible, sans être certain."),
        ("un avertissement", "L'avis qui dit que le phénomène est imminent ou commencé."),
        ("la pluie verglaçante", "La pluie qui gèle en touchant le sol."),
        ("le refroidissement éolien", "Le froid que la peau ressent quand le vent s'ajoute."),
        ("la crue printanière", "La montée de l'eau quand la neige fond partout à la fois."),
        ("reporter", "Déplacer une activité à une autre date, sans y renoncer."),
        ("des crampons", "Les pointes qu'on attache sous ses bottes pour ne pas glisser."),
        ("un coup de chaleur", "Le malaise grave quand le corps n'arrive plus à se refroidir."),
    ], notes="Huit des seize, ceux que le relevé montre comme les moins sûrs. Faire "
             "dire chaque mot avec son article et une phrase. Les huit autres se "
             "révisent avec les cartes mémoire de l'activité.")

    d.pratique('Bilan', "Êtes-vous maintenant capable de… ?",
               "Répondez pour vous-même, honnêtement.", [
        ("Distinguer une veille d'un avertissement ?", "possible, ou imminent"),
        ("Tirer d'un bulletin le phénomène, la région et le moment ?", "les trois, au passage"),
        ("Dire si un avis touche votre activité ?", "la région, puis l'heure"),
        ("Choisir entre maintenir, reporter et annuler ?", "c'est le calendrier qui tranche"),
        ("Donner la raison avec le bon connecteur ?", "un seul, le plus fort"),
        ("Dire ce qu'il faut apporter, et comment ?", "impératif, puis gérondif"),
    ], corrige=True,
       notes="Faire cocher individuellement, sans ramasser. Proposer à ceux qui "
             "hésitent sur deux points ou plus de refaire le défi correspondant dans "
             "l'activité interactive : elle reste ouverte après la fin du module.")

    d.billet(
        "En une phrase : quelle décision météo avez-vous déjà eu à prendre, pour vous ou pour d'autres ?",
        exemples=[
            "Une vraie situation : un rendez-vous, un déplacement, un travail.",
            "Gardez ce billet : c'est le seul du module qui ne se corrige pas.",
        ],
        notes="Ne pas ramasser celui-ci. Le module a commencé par une femme qui "
              "devait décider pour trente personnes ; il se termine par la même "
              "question, posée à chacun.")

    return d.save(dossier)
