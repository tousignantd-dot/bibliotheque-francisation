# -*- coding: utf-8 -*-
"""E2 · Le courriel, et les seize mots
Bloc E « Je me lance » · couleur framboise · 75 min.
Production écrite, puis bilan du module.
Source : bloc « Je me lance » (courriel d'invitation) et « Je retiens des
mots ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Le courriel, et les seize mots",
        chapeau="Dernière séance. Vous écrivez à quelqu'un pour l'inviter à "
                "venir avec vous : le voyage que vous ferez, du début à la "
                "fin, au futur simple. Puis on rassemble les seize mots du "
                "module et on fait le point.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Prévoir quarante minutes d'écriture en "
                  "silence, puis le bilan. Rendre au début les billets de E1 et les "
                  "rétroactions des productions orales : la comparaison est le vrai "
                  "moment d'apprentissage de la séance.")

    d.objectifs([
        "écrire un courriel qui raconte un projet du début à la fin ;",
        "employer le futur simple pour un projet décidé ;",
        "réunir ses phrases avec « qui », « que » et « où » ;",
        "faire le point sur ce qu'on est maintenant capable de faire.",
    ], notes="Le premier objectif est le critère du niveau 5 à l'écrit : un texte "
             "organisé, pas trois phrases détachées. C'est exactement l'équivalent "
             "écrit de la demande complète du défi 1.")

    d.regle("Un projet se raconte au futur simple",
            "Nous partirons le 28. Le trajet durera huit heures. Nous "
            "dormirons au gîte.",
            precision="Le futur proche — « on va partir » — se dit ; à l'écrit, "
                      "dans une invitation, le futur simple fait plus soigné.",
            notes="Diapositive à photographier. Ne pas interdire le futur proche : "
                  "signaler la différence de registre suffit, et les élèves choisissent "
                  "d'eux-mêmes une fois qu'ils la connaissent.")

    d.tableau('Le courriel', "Cinq parties, dans l\'ordre",
              ['La partie', "Ce qu'on y met"],
              [["L'objet", "Trois ou quatre mots : « Une semaine au Bic ? »"],
               ["La salutation", "Bonjour, puis le prénom"],
               ["L'invitation", "Où, quand, combien de nuits"],
               ["Le programme", "Ce qu'on fera, et ce qu'on verra"],
               ["La question finale", "Ce que vous attendez comme réponse"]],
              cle=1,
              notes="La dernière ligne est celle qu'on oublie : un courriel "
                    "d'invitation sans question ne reçoit pas de réponse. « Est-ce que "
                    "ça te tente ? » suffit, mais il faut la poser.")

    d.cartes("Ce que le correcteur regarde", "Quatre points, annoncés d'avance", [
        ("Le texte se tient",
         "On suit le projet du début à la fin, sans sauter."),
        ("Les temps sont justes",
         "Futur simple pour le projet, passé pour ce qui est déjà fait."),
        ("Les prépositions de lieu",
         "à Rimouski, en Gaspésie, au Bas-Saint-Laurent."),
        ("Les phrases sont reliées",
         "qui, que, où — au moins une fois chacun."),
    ], notes="Annoncer les critères avant l'écriture, jamais après. Un élève qui sait "
             "qu'on regarde les phrases reliées en écrit ; celui qui l'apprend à la "
             "correction se sent piégé.")

    d.piege("Écrire trois phrases détachées",
            "Je vais à Rimouski. C'est beau. Viens avec moi.",
            "J'irai à Rimouski fin septembre, dans une région que je ne connais pas encore.",
            "Trois phrases courtes côte à côte, c'est du niveau 4. Le niveau 5 "
            "demande qu'elles se tiennent : une seule phrase reliée en dit autant "
            "et se lit mieux.",
            notes="Reprendre l'exercice de C2 si le besoin s'en fait sentir : réunir "
                  "deux phrases courtes en une seule est la manipulation qui débloque "
                  "cette production.")

    d.vocabulaire('Bilan du vocabulaire', "Les seize mots, une dernière fois", [
        ("un attrait", "Ce qu'on va voir dans une région."),
        ("un horaire", "La liste des heures de départ et d'arrivée."),
        ("la soute", "L'espace à valises, sous le plancher de l'autocar."),
        ("un gîte", "Une maison où l'on loue une chambre, déjeuner compris."),
        ("un sentier", "Le petit chemin de terre où l'on marche."),
        ("la marée", "L'eau qui monte et qui descend deux fois par jour."),
        ("un belvédère", "L'endroit en hauteur d'où l'on regarde le paysage."),
        ("jaser", "Parler avec quelqu'un pour le plaisir de la conversation."),
    ], notes="Huit des seize, ceux que le relevé montre comme les moins sûrs. Faire "
             "dire chaque mot avec son article et une phrase. Les huit autres sont dans "
             "le banc de l'activité et se révisent avec les cartes mémoire.")

    d.pratique('Bilan', "Êtes-vous maintenant capable de… ?",
               "Répondez pour vous-même, honnêtement.", [
        ("Exposer une demande complète à un comptoir ?", "où, quand, combien de temps, combien de personnes"),
        ("Poser trois questions polies de suite ?", "trois formules différentes"),
        ("Lire une ligne d'horaire interurbain ?", "en ligne, pas en colonne"),
        ("Comparer deux possibilités et choisir ?", "avec la raison qui a fait pencher"),
        ("Raconter votre journée au passé ?", "l'action et le décor"),
        ("Tenir le vouvoiement avec un inconnu ?", "du début à la fin"),
    ], corrige=True,
       notes="Faire cocher individuellement, sans ramasser. Proposer à ceux qui hésitent "
             "sur deux points ou plus de refaire le défi correspondant dans l'activité "
             "interactive : elle reste ouverte après la fin du module.")

    d.billet(
        "En une phrase : où irez-vous, et quand ?",
        exemples=[
            "Une vraie destination, une vraie date, même approximative.",
            "Gardez ce billet : c'est le seul du module qui ne se corrige pas.",
        ],
        notes="Ne pas ramasser celui-ci. Le module a commencé par « tu t'en vas où ? » "
              "et il se termine par la même question, posée à chacun. C'est la seule "
              "chose qu'il cherchait vraiment.")

    return d.save(dossier)
