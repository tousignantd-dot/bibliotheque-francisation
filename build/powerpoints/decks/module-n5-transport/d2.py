# -*- coding: utf-8 -*-
"""D2 · En passant par le boulevard
Bloc D « Défi 3 · Le trajet refait » · couleur ambre · 75 min.
Source : exercices `t3ger` et `t3fut`, mini-leçons du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="En passant par le boulevard",
        chapeau="« En sortant à Marcel-Laurin et en prenant le boulevard, on "
                "arrive à huit heures quinze. » Une phrase, deux gérondifs, "
                "un chemin complet et une heure. C'est le français du niveau "
                "5 : des idées qui s'emboîtent au lieu de se suivre.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, la dernière du module. Deux points : le gérondif "
                  "pour dire le chemin, les futurs pour dire l'heure. Ouvrir en écrivant "
                  "les trois phrases séparées au tableau, puis la phrase unique : la "
                  "différence se voit avant d'être expliquée.")

    d.objectifs([
        "former le gérondif à partir du verbe à « nous » ;",
        "employer le gérondif pour dire par quel chemin on passe ;",
        "employer le futur proche à l'oral et le futur simple à l'écrit ;",
        "annoncer une heure d'arrivée en chiffres.",
    ], notes="Le programme du niveau 5 nomme le gérondif explicitement : l'adulte "
             "l'emploie pour marquer la simultanéité ou la manière. C'est une des marques "
             "du passage au stade intermédiaire, et cela vaut d'être dit au groupe.")

    d.regle("Le gérondif se forme sur « nous »",
            "Nous passons, en passant. Nous prenons, en prenant. Nous "
            "sortons, en sortant.",
            precision="Trois exceptions seulement : être donne « en étant », avoir "
                      "« en ayant », savoir « en sachant ».",
            notes="Diapositive à photographier. Passer par la forme « nous » évite "
                  "toutes les erreurs : formé sur l'infinitif, le gérondif donne des "
                  "monstres comme « en prendant ».")

    d.tableau('Deux emplois', "La manière, et la simultanéité",
              ['On veut dire', 'On dit'],
              [["Par quel chemin", "En passant par le boulevard"],
               ["Comment gagner du temps", "En partant à six heures"],
               ["Deux choses à la fois", "Il écoute la radio en conduisant"],
               ["Pendant qu'on écoutait", "En écoutant, nous avons appris"]],
              cle=1,
              notes="L'emploi central du module est le premier : dire le chemin. Les "
                    "deux derniers sont de la simultanéité et servent surtout à "
                    "comprendre, moins à produire.")

    d.piege("Changer de sujet en cours de route",
            "En écoutant la radio, l'accident a été annoncé.",
            "En écoutant la radio, nous avons appris l'accident.",
            "Ce n'est pas l'accident qui écoute. Le sujet du gérondif est toujours "
            "celui de la phrase. Quand les deux actions n'ont pas le même sujet, on "
            "emploie « pendant que ».",
            notes="Erreur invisible pour celui qui la fait, très visible pour celui qui "
                  "écoute. Faire relire à voix haute en demandant chaque fois : qui fait "
                  "l'action ?")

    d.regle("Deux futurs, deux distances",
            "Au téléphone : je vais être en retard. Par écrit : nous "
            "partirons plus tôt lundi.",
            precision="Le présent convient aussi, à une condition : que l'heure "
                      "soit dite. « J'arrive » tout seul veut dire « je suis "
                      "presque là ».",
            notes="Diapositive à photographier. La condition sur le présent est celle "
                  "qui crée le plus de malentendus réels, au travail comme ailleurs.")

    d.cartes("Cinq futurs irréguliers", "Exactement ceux dont on a besoin", [
        ("être", "je serai là vers huit heures et quart"),
        ("avoir", "j'aurai vingt minutes de retard"),
        ("aller", "j'irai directement à l'atelier"),
        ("faire", "nous ferons le détour demain aussi"),
        ("pouvoir", "Farida pourra ouvrir à sept heures et demie"),
    ], notes="Faire entendre le « r » dans chacun : serai, aurai, irai, ferai, pourrai. "
             "C'est lui qui marque le futur à l'oreille, bien plus que la terminaison.")

    d.pratique('Gérondif', "Récrivez avec « en » + le verbe en -ant",
               "Une seule phrase à la place de deux.", [
        ("Nous prenons le boulevard et nous évitons le bouchon.", "En prenant le boulevard, nous évitons le bouchon."),
        ("Vous partez à six heures, vous éviterez le bouchon.", "En partant à six heures, vous éviterez le bouchon."),
        ("Il sort à Marcel-Laurin et il gagne dix minutes.", "En sortant à Marcel-Laurin, il gagne dix minutes."),
        ("Nous suivons le détour et nous arrivons à huit heures.", "En suivant le détour, nous arrivons à huit heures."),
        ("Elle écoutait le bulletin, elle a appris l'accident.", "En écoutant le bulletin, elle a appris l'accident."),
    ], corrige=True,
       notes="Les cinq mêmes phrases sont dans l'exercice `t3ger`. Faire dire chaque "
             "phrase complète à voix haute : le gérondif se fixe par le rythme, pas par "
             "la règle.")

    d.pratique('Futurs', "Mettez le verbe au temps demandé",
               "Futur proche à l'oral, futur simple à l'écrit.", [
        ("Futur proche : je (être) ___ en retard.", "je vais être"),
        ("Futur simple : j'(arriver) ___ vers huit heures quinze.", "j'arriverai"),
        ("Futur proche : on (sortir) ___ à la prochaine.", "on va sortir"),
        ("Futur simple : la bretelle (être) ___ fermée deux jours.", "sera"),
        ("Futur simple : Farida (pouvoir) ___ ouvrir l'atelier.", "pourra"),
        ("Futur simple : nous (faire) ___ le détour demain aussi.", "ferons"),
    ], corrige=True,
       notes="Les six mêmes items sont dans l'exercice `t3fut`. Faire choisir au groupe, "
             "pour chacun, s'il conviendrait au téléphone ou dans un courriel : c'est la "
             "vraie question.")

    d.billet(
        "Écrivez votre chemin de rechange en une phrase, avec deux gérondifs et une heure.",
        exemples=[
            "En sortant à …, et en prenant …, j'arriverai vers …",
            "Si vous prenez le transport en commun, dites la correspondance.",
        ],
        notes="Ramasser les billets : c'est la phrase centrale du jeu de rôle de E1, "
              "celle que le collègue attend et que personne ne donne du premier coup.")

    return d.save(dossier)
