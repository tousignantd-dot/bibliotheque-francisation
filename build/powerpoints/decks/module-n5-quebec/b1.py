# -*- coding: utf-8 -*-
"""B1 · Rue Berri, au comptoir
Bloc B « Défi 1 · Au comptoir de la gare d'autocars » · acier · 75 min.
Source : dialogue `t1`, exercice `t1a`.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-quebec/images/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Rue Berri, au comptoir",
        chapeau="La Gare d'autocars de Montréal est au 1717, rue Berri, "
                "au-dessus de la station Berri-UQAM. Près de trois cents "
                "autocars en partent chaque jour, vers des endroits dont "
                "Thuy n'a jamais entendu le nom.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 1. Le changement de registre est le point "
                  "de la séance : Thuy tutoyait Camille, elle vouvoie Serge. Le faire "
                  "remarquer dès la première réplique et y revenir à chaque exercice.")

    d.objectifs([
        "exposer une demande complète d'un seul tenant, sans attendre les questions ;",
        "comprendre une réponse qui donne trois heures de départ et une durée ;",
        "vouvoyer un inconnu du début à la fin d'un échange ;",
        "répéter à voix haute l'information reçue pour la vérifier.",
    ], notes="Le premier objectif est le critère du niveau 5 et celui de tout le "
             "module : un discours organisé, pas une suite de questions-réponses. "
             "L'écrire au tableau et le laisser toute la séance.")

    d.declencheur(
        'Observation', "Vous arrivez au comptoir. Qu'est-ce que vous dites "
                       "en premier ?",
        image=img('gare-autocars.jpg'),
        pistes=[
            "Combien de phrases avant qu'on sache où vous allez ?",
            "Qu'est-ce que le préposé a besoin de savoir, exactement ?",
            "Est-ce qu'on le tutoie ou est-ce qu'on le vouvoie ?",
            "Qu'est-ce qui se passe si vous ne dites que « Rimouski » ?",
        ],
        notes="Laisser quelqu'un jouer la scène en donnant un mot à la fois : le groupe "
              "voit tout de suite que l'échange dure trois fois plus longtemps et que "
              "c'est le préposé qui travaille. C'est l'argument de toute la séance.")

    d.dialogue('Dialogue · 1 de 3', "Tout dire en une fois", [
        ("SERGE", "Bonjour ! Je peux vous aider ?", True),
        ("THUY", "Bonjour. Je voudrais aller à Rimouski, dans le "
                 "Bas-Saint-Laurent. Je partirais le lundi 28 septembre et "
                 "je reviendrais le dimanche suivant. Une personne.", True),
        ("SERGE", "Parfait, c'est clair. Rimouski, aller-retour, une "
                  "personne, du 28 septembre au 4 octobre.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Compter avec le groupe ce que Thuy donne en une réplique : la "
             "destination, la région, la date de départ, la date de retour, le nombre "
             "de personnes. Cinq informations, une phrase et demie. Et la réponse de "
             "Serge le dit : « c'est clair ».")

    d.dialogue('Dialogue · 2 de 3', "Combien de temps ça prend", [
        ("THUY", "Pourriez-vous me dire combien de temps ça prend ?", True),
        ("SERGE", "Le départ de sept heures arrive à quinze heures dix. "
                  "Huit heures dix, avec les arrêts. Trois-Rivières, "
                  "Québec, La Pocatière, Rivière-du-Loup, et Rimouski.", True),
        ("THUY", "Est-ce qu'il faut changer d'autocar ?", True),
    ], notes="« Pourriez-vous me dire » est la formule à retenir de la séance. Elle "
             "sera travaillée à fond en B2. Faire aussi remarquer que Serge nomme les "
             "arrêts : c'est ainsi qu'on apprend la géographie d'un trajet.")

    d.dialogue('Dialogue · 3 de 3', "Vingt minutes avant, quai 12", [
        ("SERGE", "Ça vous fait un aller-retour, départ lundi sept heures, "
                  "quai 12. Présentez-vous vingt minutes avant : les valises "
                  "se chargent avant le départ, pas après.", True),
        ("THUY", "Vingt minutes avant, quai 12. Merci beaucoup.", True),
        ("SERGE", "Bon voyage, madame. Vous allez aimer ça.", False),
    ], notes="La réplique de Thuy est un modèle : elle répète les deux informations "
             "critiques au lieu de dire « d'accord ». Le faire pratiquer tout de suite, "
             "deux par deux, avec des heures et des quais inventés.")

    d.regle("Une demande complète tient en une phrase",
            "Où · quand · combien de temps · combien de personnes.",
            precision="Le préposé n'a alors qu'à répondre. Sans ces quatre "
                      "informations, il doit poser quatre questions, et l'échange "
                      "devient un interrogatoire.",
            notes="Diapositive à photographier. C'est la grille du jeu de rôle de E1 et "
                  "celle de la correction. Elle reprend la règle de A1 en la "
                  "spécialisant au comptoir.")

    d.tableau('Deux façons de commencer', "La même demande, deux échanges",
              ['Par morceaux', "D'un seul tenant"],
              [["« Rimouski. »", "« Je voudrais aller à Rimouski. »"],
               ["« C'est quand ? » — « Lundi. »", "« Je partirais le lundi 28. »"],
               ["« Retour ? » — « Euh… »", "« Je reviendrais le dimanche. »"],
               ["Huit répliques", "Une réplique et demie"]],
              cle=1,
              notes="Faire jouer les deux versions par deux binômes, l'une après "
                    "l'autre. La différence de durée frappe plus qu'une explication.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Thuy part le lundi 28 septembre.", "vrai"),
        ("Il y a deux départs le lundi.", "faux — trois : 7 h, 12 h 30, 18 h 15"),
        ("Le départ de sept heures est direct.", "vrai"),
        ("Celui de midi trente a une correspondance à Québec.", "vrai — quarante minutes d'attente"),
        ("Thuy prend le tarif économique.", "faux — celui qui se change"),
        ("Il faut arriver cinq minutes avant le départ.", "faux — vingt minutes"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la réplique exacte. La dernière est "
             "d'utilité immédiate : les valises se chargent avant le départ, et un "
             "élève qui arrive à l'heure pile voit partir son autocar.")

    d.billet(
        "Écrivez votre demande complète, en une phrase : où, quand, combien de temps, combien de personnes.",
        exemples=[
            "Choisissez une vraie destination, celle que vous aviez notée en A1.",
            "Relisez-la à voix haute : elle doit tenir sans reprendre votre souffle deux fois.",
        ],
        notes="Ramasser les billets et les rendre en B4, où la même phrase sera reprise "
              "et complétée. Les garder : ils servent aussi de point de départ au jeu "
              "de rôle de E1.")

    return d.save(dossier)
