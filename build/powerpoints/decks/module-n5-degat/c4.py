# -*- coding: utf-8 -*-
"""C4 · Il faut que, pour que : le subjonctif présent.
Bloc C « Défi 2 · L'avis » · couleur ambre · 75 min. Grammaire et écriture.
Source : exercices `t2subj` et `t2fiche`, mini-leçon `t2subj`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="Il faut que, pour que : le subjonctif présent",
        chapeau="Le subjonctif ne s'emploie jamais tout seul : il vient après "
                "un mot qui l'appelle. Apprenez les déclencheurs, et il se met "
                "de lui-même.",
        duree='75 minutes')

    d.titre(notes="Le mot « subjonctif » fait peur ; le mode, non. Commencer en écrivant "
                  "« Il faut que vous soyez là » au tableau et en demandant si quelqu'un "
                  "dirait autre chose. Personne ne se trompe à l'oral — c'est un bon "
                  "départ.")

    d.objectifs([
        "former le subjonctif à partir de la forme « ils » du présent ;",
        "connaître les quatre irréguliers courants ;",
        "reconnaître les quatre déclencheurs du niveau 5 ;",
        "savoir quand l'infinitif suffit.",
    ])

    d.regle("Il vient après un mot qui l'appelle",
            "Ce sont les déclencheurs qu'il faut connaître, pas le mode.",
            precision="Le subjonctif n'apparaît jamais au début d'une phrase. Il suit "
                      "« il faut que », « il est nécessaire que », « pour que », « avant "
                      "que ». Quatre déclencheurs suffisent pour la vie courante au "
                      "niveau 5, et ils reviennent tous dans les avis et les lettres du "
                      "logement.",
            notes="Dire cette phrase avant toute conjugaison : elle transforme un mode "
                  "réputé difficile en une liste de quatre expressions.")

    d.cartes("Comment il se forme", "À partir de « ils »", [
        ("On prend la forme « ils » du présent",
         "ils libèrent · ils finissent · ils prennent"),
        ("On enlève -ent",
         "libèr- · finiss- · prenn-"),
        ("On ajoute -e, -es, -e, -ions, -iez, -ent",
         "que je libère · que tu finisses · qu'il prenne"),
        ("Le « que » fait partie du paquet",
         "On n'apprend jamais « libère » seul : on apprend « que je libère »."),
    ], notes="La dernière carte évite l'erreur la plus fréquente à l'écrit : oublier le "
             "« que ».")

    d.tableau('Les quatre irréguliers', "À savoir par cœur",
              ['Le verbe', 'Au subjonctif'],
              [["être", "que je sois · que vous soyez · que nous soyons"],
               ["avoir", "que j'aie · que nous ayons"],
               ["faire", "que je fasse · que nous fassions"],
               ["aller", "que j'aille · que nous allions"],
               ["pouvoir", "que je puisse · qu'ils puissent — le cinquième, très utile"]],
              cle=0,
              note="« Que les ouvriers puissent travailler » revient dans tous les avis.",
              notes="Faire répéter les quatre premiers en série, comme une liste. Le "
                    "cinquième s'ajoute naturellement à l'usage.")

    d.tableau('Les quatre déclencheurs', "Ce qui appelle le subjonctif",
              ['Le déclencheur', 'Un exemple du module'],
              [["il faut que", "Il faut que vous soyez présent mercredi matin."],
               ["il est nécessaire que",
                "Il est nécessaire que les occupants libèrent l'accès."],
               ["pour que / afin que",
                "Tassez la commode pour que les ouvriers puissent travailler."],
               ["avant que", "Prenez vos photos avant que la tache sèche."]],
              cle=0,
              note="Attention : « après que » ne demande pas le subjonctif.",
              notes="Expliquer la note : ce qui est fini est réel, donc indicatif. "
                    "Beaucoup de locuteurs natifs se trompent — le dire, ça dédramatise.")

    d.regle("Deux sujets, sinon l'infinitif",
            "S'il n'y a personne de précis, l'infinitif suffit.",
            precision="« Il faut libérer l'accès » — personne en particulier. « Il faut "
                      "que vous libériez l'accès » — vous. Même chose pour le but : "
                      "« pour libérer le mur » si c'est le même sujet, « pour que les "
                      "ouvriers puissent travailler » s'il change. Cette règle vous "
                      "évite la moitié des subjonctifs.",
            notes="C'est la diapositive la plus rassurante de la séance. La donner tôt "
                  "dans la pratique, pas seulement à la fin.")

    d.pratique('Pratique · exercice t2subj', "Mettez au subjonctif présent",
               "Le verbe entre parenthèses.",
               [("Il faut que vous (être) ___ présent mercredi matin.", "soyez"),
                ("Il est nécessaire que les occupants (libérer) ___ l'accès.",
                 "libèrent"),
                ("Tassez la commode pour que les ouvriers (pouvoir) ___ travailler.",
                 "puissent"),
                ("Prenez vos photos avant que la tache (sécher) ___ .", "sèche"),
                ("Il faut que j' (avoir) ___ une réponse écrite.", "aie"),
                ("Il est important que nous (faire) ___ constater les dommages.",
                 "fassions")],
               corrige=True, cols=1,
               notes="Faire nommer le déclencheur avant de conjuguer, à chaque phrase. "
                     "C'est l'habitude à installer.")

    d.pratique('Pratique · exercice t2fiche', "La fiche à remplir après avoir lu l'avis",
               "Six lignes, toujours les mêmes. D'après l'avis du dialogue.",
               [("Logements visés", "les logements 3 et 4"),
                ("Nature des travaux", "l'assèchement des murs et du plancher"),
                ("Du … au …", "du mercredi 12 au vendredi 14 novembre"),
                ("Plage horaire", "entre 8 h et 17 h"),
                ("Ce que je dois faire", "libérer l'accès au mur touché"),
                ("Ce que ça m'enlève", "trois nuits dans ma chambre")],
               corrige=True, cols=1,
               notes="La dernière ligne est celle que personne n'écrit spontanément, et "
                     "c'est la seule qui servira au défi 3. Insister.")

    d.piege("Mettre le subjonctif après « après que »",
            "Après qu'il soit parti, j'ai tout rangé.",
            "Après qu'il est parti, j'ai tout rangé.",
            "Ce qui est fini est réel, donc indicatif. L'erreur est très répandue, y "
            "compris chez les locuteurs natifs, parce que « avant que » est juste à côté "
            "et demande, lui, le subjonctif. La logique est pourtant nette : ce qui vient "
            "est incertain, ce qui est passé ne l'est plus.",
            notes="Ne pas en faire un cheval de bataille : signaler, expliquer la "
                  "logique, passer. L'essentiel de la séance est ailleurs.")

    d.billet(
        "Écrivez une phrase avec « il faut que » et une avec « pour que ».",
        exemples=[
            "« Il faut que je sois là mercredi matin. »",
            "« J'ai tassé le lit pour que les ouvriers puissent passer. »",
        ],
        notes="Trois minutes. Vérifier le « que » et la forme du verbe, rien d'autre.")

    return d.save(dossier)
