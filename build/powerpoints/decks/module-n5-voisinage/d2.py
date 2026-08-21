# -*- coding: utf-8 -*-
"""D2 · « Ce qui est arrivé, ce qui était là »
Bloc D « Défi 3 · Les nouvelles et les félicitations » · couleur ambre · 75 min.
Source : exercices `t3pc` et `t3cour`, mini-leçon `t3pc`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="« Ce qui est arrivé, ce qui était là »",
        chapeau="Le passé composé fait avancer le récit ; l'imparfait plante "
                "le décor autour. Une nouvelle racontée entièrement au passé "
                "composé est une liste ; racontée entièrement à l'imparfait, "
                "elle ne commence jamais.",
        duree='75 minutes')

    d.titre(notes="Beaucoup d'élèves croient que l'imparfait est « plus difficile » ou "
                  "qu'il vient « après ». Démentir tout de suite : les deux temps "
                  "racontent la même histoire, mais ils n'y font pas le même travail.")

    d.objectifs([
        "employer le passé composé pour les événements ;",
        "employer l'imparfait pour le décor et les habitudes ;",
        "combiner les deux dans une même phrase ;",
        "écrire un bref courriel qui donne des nouvelles.",
    ], notes="Le quatrième objectif est une intention du programme prise mot pour mot : "
             "clavarder ou rédiger un bref courriel pour donner des nouvelles.")

    d.regle("Deux questions, deux temps",
            "« Et ensuite ? » annonce le passé composé. « C'était "
            "comment ? » annonce l'imparfait.",
            precision="J'ai eu ma citoyenneté mercredi — et ensuite ? On était "
                      "deux cents dans la salle — c'était comment ? Le test se fait "
                      "en une seconde, à voix basse, pendant qu'on écrit.",
            notes="Diapositive à photographier. Ce test remplace avantageusement les "
                  "listes de marqueurs, que les élèves apprennent et n'appliquent pas.")

    d.tableau('Deux colonnes', "Ce qui avance, ce qui décrit",
              ['Passé composé', 'Imparfait'],
              [["J'ai eu ma citoyenneté mercredi.", "On était deux cents."],
               ["J'ai pris trois jours de congé.", "Il y avait des drapeaux."],
               ["On a chanté à la fin.", "Mon fils portait sa chemise."],
               ["Elle a pleuré un peu.", "Je ne m'y attendais pas."],
               ["Elle a changé d'horaire.", "Avant, elle travaillait de nuit."]],
              cle=1,
              notes="Faire remarquer la dernière ligne : la même personne, la même "
                    "période, deux temps différents selon qu'on raconte le changement ou "
                    "l'habitude d'avant.")

    d.cartes("Les deux ensemble", "Le cas le plus fréquent, et le plus utile", [
        ("Décor, puis événement",
         "Je ne m'y attendais pas quand ils ont commencé à chanter."),
        ("Météo, puis décision",
         "Il pleuvait, donc on a reporté la fête au dimanche."),
        ("Situation, puis rupture",
         "Elle travaillait de nuit depuis six ans quand elle a changé d'horaire."),
        ("La recette d'une nouvelle",
         "Un événement, un décor, un détail. Trois phrases suffisent."),
    ], notes="La quatrième carte est la consigne d'écriture du courriel. « Il y avait "
             "vingt-deux personnes dans la ruelle » en dit plus long que « c'était le "
             "fun ».")

    d.pratique('Grammaire', "Passé composé ou imparfait ?",
               "Mettez le verbe au temps qui convient.", [
        ("J' ___ (avoir) ma citoyenneté mercredi dernier.", "ai eu"),
        ("On ___ (être) deux cents dans la grande salle.", "était"),
        ("Il y ___ (avoir) des drapeaux sur tous les murs.", "avait"),
        ("Elle ___ (prendre) trois jours de congé.", "a pris"),
        ("Son fils ___ (porter) sa chemise blanche.", "portait"),
        ("À la fin, tout le monde ___ (chanter) ensemble.", "a chanté"),
        ("Avant, elle ___ (travailler) toujours de nuit.", "travaillait"),
    ], corrige=True,
       notes="Exercice t3pc de l'activité. Pour chaque item, faire poser la question du "
             "test avant de répondre : « et ensuite ? » ou « c'était comment ? ».")

    d.regle("L'accord du participe, en deux lignes",
            "Avec être, le participe s'accorde avec le sujet. Avec avoir, "
            "il ne s'accorde pas avec le sujet.",
            precision="Je suis allée à la fête. · J'ai apporté un plat. Au "
                      "féminin, l'accord avec être ne s'entend pas — « allé » et "
                      "« allée » se disent pareil — mais il se voit dans un "
                      "courriel. C'est là qu'il compte.",
            notes="Ne pas ouvrir le dossier de l'accord du COD antéposé : hors programme "
                  "ici. Les deux lignes de la règle suffisent pour écrire un courriel de "
                  "nouvelles sans faute visible.")

    d.pratique('Écriture', "Le courriel, dans l'ordre",
               "Complétez le courriel de Marisol à une amie de son cours.", [
        ("___ : Des nouvelles de la ruelle", "Objet"),
        ("Bonjour Amina, j' ___ que tout va bien de ton côté.", "espère"),
        ("Samedi, je ___ allée à la fête de la ruelle.", "suis"),
        ("Il y ___ vingt-deux personnes dans la ruelle.", "avait"),
        ("J'ai ___ des empanadas, et il n'en est pas resté un seul.", "apporté"),
        ("Et toi, ___ se passe ton nouvel emploi ?", "comment"),
    ], corrige=True,
       notes="Exercice t3cour de l'activité. Faire remarquer les cinq mouvements du "
             "courriel : l'objet, la salutation, les nouvelles au passé, ce qui vient "
             "ensuite au futur, la question ouverte. C'est le plan de la production écrite "
             "de E2.")

    d.piege("Tout raconter au passé composé",
            "J'ai eu ma citoyenneté. On a été deux cents. Il y a eu des drapeaux.",
            "J'ai eu ma citoyenneté. On était deux cents, et il y avait des drapeaux.",
            "La phrase est compréhensible, mais elle sonne comme une liste. Le décor "
            "se décrit à l'imparfait, et c'est lui qui fait voir la scène.",
            notes="Lire les deux versions à voix haute, l'une après l'autre. La différence "
                  "s'entend immédiatement, bien mieux qu'elle ne s'explique.")

    d.billet(
        "Racontez en trois phrases une bonne nouvelle de votre année.",
        exemples=[
            "Une phrase au passé composé, une à l'imparfait, une au futur simple.",
            "Vérifiez l'accord du participe si vous employez « être ».",
        ],
        notes="Fin du bloc D. Ces trois phrases sont le brouillon direct du courriel de "
              "E2 : le dire aux élèves, ils y mettront plus de soin.")

    return d.save(dossier)
