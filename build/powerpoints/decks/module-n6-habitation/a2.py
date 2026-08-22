# -*- coding: utf-8 -*-
"""A2 · Le chantier parle grec, anglais et allemand
Bloc A « Je découvre » · couleur indigo · 75 min. Graphie-phonie.
Source : exercice `prGraphie` et sa mini-leçon. Savoir du programme : associer
des phonèmes à des graphèmes inhabituels — /k/ écrit ch, /s/ écrit x, le son
de « chat » écrit sh ou sch.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Le chantier parle grec, anglais et allemand",
        chapeau="Trois groupes de lettres ne se lisent pas comme ils "
                "s'écrivent, et tous les trois reviennent dans une "
                "conversation de travaux.",
        duree='75 minutes')

    d.titre(notes="Séance d'oreille. Prévoir de faire écouter chaque mot deux fois "
                  "avant toute explication : la règle n'a de sens qu'après avoir "
                  "entendu l'écart entre ce qui est écrit et ce qui est dit.")

    d.objectifs([
        "entendre le k dans les mots savants écrits avec ch ;",
        "entendre le s dans les nombres écrits avec x ;",
        "entendre le son de « chat » dans sh et sch ;",
        "demander qu'on écrive un mot entendu pour la première fois.",
    ], notes="Le quatrième objectif n'est pas de la phonétique : c'est une stratégie "
             "de survie sur un chantier, et elle vaut d'être nommée.")

    d.declencheur(
        'Observation', "« Un technicien va passer. » Combien de sons différents dans « ch » ?",
        pistes=[
            "Comment dis-tu « chantier » ? Et « technicien » ?",
            "Est-ce le même son dans les deux mots ?",
            "Connais-tu un mot écrit avec ch qui se dit avec un k ?",
        ],
        notes="Laisser le groupe hésiter. Presque personne ne remarque l'écart avant "
              "qu'on le nomme, et une fois nommé, personne ne l'oublie.")

    d.tableau('Analyse', "Le grec : ch qui se dit k",
              ['On écrit', 'On entend'],
              [["un architecte", "ar-ki-tecte"],
               ["la technique", "tec-nique"],
               ["le chlore", "clore"],
               ["une orchidée", "or-ki-dée"]],
              cle=0,
              note="Des mots savants ou techniques, presque tous venus du grec.",
              notes="Diapositive à photographier. Préciser tout de suite que chantier, "
                    "chauffage, planche et marchandise gardent le son normal : le k "
                    "est l'exception, pas la règle.")

    d.tableau('Analyse', "Les nombres : x qui se dit s",
              ['On écrit', 'On entend'],
              [["six semaines", "si semaines"],
               ["six heures", "siz heures"],
               ["il y en a six", "sisse"],
               ["soixante", "soi-sante"]],
              cle=0,
              note="Un seul mot écrit, trois façons de le dire selon ce qui suit.",
              notes="Diapositive à photographier. Les trois formes de « six » se "
                    "comprennent toutes : rassurer le groupe là-dessus. Ce qu'on "
                    "travaille est la reconnaissance, pas la production parfaite.")

    d.tableau('Analyse', "L'emprunt : sh et sch qui se disent comme dans « chat »",
              ['On écrit', 'On entend'],
              [["un schéma", "ché-ma"],
               ["le schiste", "chiste"],
               ["le shampoing", "chan-poing"],
               ["un short", "chort"]],
              cle=0,
              note="Jamais « sk » en français, dans aucun de ces mots.",
              notes="Diapositive à photographier. « Un schéma » est le mot le plus "
                    "utile des quatre : il revient dans tous les documents "
                    "techniques du module.")

    d.regle("Trois familles, et tout le reste se lit normalement",
            "ch qui dit k, x qui dit s, sh et sch qui disent ch.",
            precision="Ces trois familles se comptent sur les doigts. Le reste du "
                      "français se lit comme il s'écrit sur ce point. Il ne s'agit "
                      "donc pas d'apprendre une exception de plus : il s'agit de "
                      "reconnaître une petite liste de mots, et de savoir que quand "
                      "un mot entendu ne se trouve nulle part, il faut essayer ch à "
                      "la place du k.",
            notes="Diapositive à photographier. C'est la règle du bloc.")

    d.pratique('Écoute', "Quel son porte le groupe de lettres ?",
               "Écoutez le mot, puis répondez : comme k, comme s, ou comme ch.", [
        ("un architecte", "comme k"),
        ("dix", "comme s"),
        ("un schéma", "comme ch"),
        ("la technique", "comme k"),
        ("soixante", "comme s"),
        ("le shampoing", "comme ch"),
        ("le chlore", "comme k"),
        ("le schiste", "comme ch"),
    ], corrige=True,
       notes="Le même exercice existe dans le module, à cartes écoutables. Ici, c'est "
             "l'enseignante qui dit les mots : deux fois chacun, sans montrer "
             "l'orthographe la première fois.")

    d.piege('Piège', "répéter le mot comme on l'a entendu",
            "demander qu'on l'écrive",
            "Vous entendez « tecnique » et personne ne vous comprend quand vous "
            "l'écrivez ainsi. Sur un chantier, demander qu'on vous écrive un mot "
            "n'étonne personne : tout le monde le fait, y compris entre gens de "
            "métier.",
            notes="Le moment de la séance à ne pas presser. Faire pratiquer la phrase "
                  "à voix haute : « Pouvez-vous me l'écrire ? » Elle servira toute "
                  "la session.")

    d.pratique('Production', "Lire à voix haute",
               "Chacun lit une ligne, puis la fait répéter à son voisin.", [
        ("L'architecte a signé le plan modifié.", "ar-ki-tecte"),
        ("Le permis prend dix jours ouvrables.", "di jours"),
        ("Le rapport était accompagné d'un schéma très clair.", "ché-ma"),
        ("La technique d'injection se fait sous pression.", "tec-nique"),
        ("La gouttière se vide à soixante centimètres du mur.", "soi-sante"),
        ("Le schiste est une pierre qui se fend en feuillets.", "chiste"),
    ], corrige=True,
       notes="Faire lire deux fois : une fois pour l'exactitude, une fois pour le "
             "rythme. C'est la phrase entière qu'on travaille, pas le mot isolé.")

    d.billet(
        "Écris un mot que tu as entendu au travail et que tu n'as pas su écrire.",
        exemples=[
            "Écris-le comme tu l'as entendu.",
            "On le cherchera ensemble à la prochaine séance.",
        ],
        notes="Trois minutes. Ces mots-là sont meilleurs que ceux du module parce "
              "qu'ils viennent de la vie des élèves. Les reprendre en A3.")

    return d.save(dossier)
