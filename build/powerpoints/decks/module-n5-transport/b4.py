# -*- coding: utf-8 -*-
"""B4 · Prévu ou imprévu
Bloc B « Défi 1 · Ce qui bloque la route » · couleur ambre · 75 min.
Source : exercices `t1inc` et `t1red`, mini-leçon `t1inc`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Prévu ou imprévu",
        chapeau="Devant une entrave, une seule question compte : est-ce que "
                "quelqu'un le savait d'avance ? Si oui, il y a une heure de "
                "fin. Si non, personne ne peut vous dire quand ce sera fini — "
                "pas même la personne au micro.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 1. Elle réunit tout le bloc : le vocabulaire "
                  "de A3, les repères de B2, les expressions de temps de B3, et elle "
                  "s'achève sur la première vraie production — redire une annonce en une "
                  "phrase organisée.")

    d.objectifs([
        "reconnaître si une entrave était prévue ou vient d'arriver ;",
        "savoir ce que les véhicules présents disent de la durée ;",
        "connaître Québec 511 et ce qu'on y trouve ;",
        "redire une annonce en une phrase, avec ses quatre informations.",
    ], notes="Le quatrième objectif est une production : y garder les vingt-cinq "
             "dernières minutes. C'est la répétition générale du jeu de rôle de E1.")

    d.regle("Deux familles, deux façons d'y répondre",
            "Le prévu se contourne la veille. L'imprévu se décide en trente "
            "secondes, avec ce qu'on vient d'entendre.",
            precision="Des travaux annoncés jusqu'à cinq heures finissent à cinq "
                      "heures. Un accident finit quand la remorqueuse a fini.",
            notes="Diapositive à photographier. C'est la synthèse du défi 1 et la "
                  "justification de tout le module : l'imprévu ne se lit nulle part, il "
                  "s'entend.")

    d.tableau('Deux familles', "Ce qui les distingue",
              ['Prévu', 'Imprévu'],
              [["des travaux", "un accident"],
               ["une fermeture annoncée", "une panne"],
               ["une heure de fin connue", "personne ne sait"],
               ["publié sur Québec 511", "d'abord à la radio"]],
              cle=1,
              notes="Québec 511 est le service d'information routière du ministère des "
                    "Transports : la ligne téléphonique 511 et le site quebec511.info. "
                    "Le montrer si la classe a un écran.")

    d.cartes("Les véhicules disent la durée", "Sans qu'on ait à la dire", [
        ("Une remorqueuse en route",
         "Elle n'est pas arrivée : ça va durer."),
        ("Une remorqueuse sur place",
         "Ça commence : il faut charger le véhicule."),
        ("Des véhicules d'urgence",
         "Ce sera long : on ne rouvre pas tant qu'ils y sont."),
        ("Les policiers dirigent",
         "Une voie passe, lentement, sous contrôle."),
    ], notes="C'est du raisonnement, pas du vocabulaire : le bulletin ne dit pas « ce "
             "sera long », il dit qui est sur place. Faire refaire le raisonnement "
             "d'Amine, vu en B1.")

    d.regle("Se ranger pour les véhicules d'urgence",
            "Gyrophares derrière vous : on se range à droite et on immobilise "
            "son véhicule.",
            precision="Près d'un véhicule d'urgence arrêté sur le bord de la route, "
                      "on ralentit et on se déplace dans la voie voisine.",
            notes="C'est la loi au Québec, et c'est aussi une information de sécurité "
                  "que beaucoup d'élèves n'ont jamais reçue. La donner simplement, sans "
                  "en faire une leçon de conduite.")

    d.piege("Croire qu'un accident finit à l'heure annoncée",
            "Il a dit vingt minutes, donc dans vingt minutes ça passe.",
            "Vingt minutes est une estimation faite pendant que ça se passe.",
            "Si les remorqueuses viennent d'arriver, ce sera plus long. Le chiffre "
            "est une indication, pas un horaire — sauf pour des travaux annoncés.",
            notes="Rappeler la réplique d'Amine en B1 : ce n'est pas la durée qui "
                  "décide, c'est l'incertitude sur la durée.")

    d.pratique('Classement', "Prévu ou imprévu ?",
               "Dites à quelle famille appartient chaque annonce.", [
        ("La bretelle sera fermée samedi et dimanche.", "prévu"),
        ("Un carambolage vient de se produire.", "imprévu"),
        ("Les travaux de nuit se prolongent.", "prévu, mais en retard"),
        ("Un véhicule lourd est immobilisé sur l'accotement.", "imprévu"),
        ("On signale un nid-de-poule dans la voie de droite.", "imprévu"),
        ("La voie de gauche est fermée toutes les nuits.", "prévu"),
    ], corrige=True,
       notes="Les six items viennent de l'exercice `t1inc`. Faire justifier le "
             "troisième : les travaux étaient prévus, mais l'heure de fin a bougé.")

    d.pratique('Production', "Redites l'annonce en une phrase",
               "Quatre informations, dans l'ordre, en une seule phrase.", [
        ("Accident · 40 · Côte-de-Liesse · ouest · 2 voies sur 3 · 20 min",
         "Il y a un accident sur la 40, à la hauteur de Côte-de-Liesse, en direction ouest ; deux voies sur trois sont bloquées pour au moins vingt minutes."),
        ("Travaux · pont Jacques-Cartier · vers Montréal · fermé · 9 h",
         "Le pont Jacques-Cartier est fermé en direction de Montréal jusqu'à neuf heures, à cause de travaux."),
        ("Panne · 40 · accotement · Pie-IX · ouest · remorqueuse en route",
         "Un camion est immobilisé sur l'accotement de la 40, à la hauteur de Pie-IX, en direction ouest ; une remorqueuse est en route."),
    ], corrige=True,
       notes="Faire produire à l'oral, à deux, avant d'afficher le corrigé. Accepter "
             "toutes les variantes qui contiennent les quatre informations : c'est "
             "l'ordre et la complétude qu'on évalue, pas le mot à mot.")

    d.billet(
        "Écrivez la phrase que vous diriez à quelqu'un qui vous attend, ce matin.",
        exemples=[
            "Ce qui bloque, où, dans quel sens, pour combien de temps.",
            "Une seule phrase, deux respirations au maximum.",
        ],
        notes="Ramasser les billets : ce sont les brouillons du jeu de rôle de E1. Les "
              "relire avant le bloc E pour savoir sur quoi insister.")

    return d.save(dossier)
