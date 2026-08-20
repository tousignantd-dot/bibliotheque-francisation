# -*- coding: utf-8 -*-
"""C3 · y et là.
Bloc C · couleur ambre (écriture) · 75 min.
Source : mini-leçon `t2y`, exercice `t2y`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre='y et là',
        chapeau="« Je vais au centre communautaire. Je vais au centre "
                "communautaire chaque jeudi. » Deux petits mots évitent la "
                "répétition — et se placent chacun à sa façon.",
        duree='75 minutes')

    d.titre(notes="Écrire la phrase répétée du chapeau au tableau et demander au groupe ce "
                  "qui cloche. La plupart le sentent immédiatement.")

    d.objectifs([
        "remplacer un lieu par y, devant le verbe ;",
        "remplacer un lieu déjà nommé par là, après le verbe ;",
        "placer y devant l'auxiliaire au passé composé ;",
        "ne plus répéter le lieu après avoir employé y.",
    ])

    d.tableau('Analyse', "Les deux mots, côte à côte",
              ['', 'y', 'là'],
              [["Remplace", "à, au, dans, chez + lieu", "un lieu déjà nommé"],
               ["Sa place", "avant le verbe", "après le verbe"],
               ["Exemple", "J'y vais le jeudi.", "On mangeait là."],
               ["Verbe typique", "aller, retourner", "rester, manger, travailler"]],
              cle=1,
              note="La ligne de la place est celle qui demande le plus de pratique : y "
                   "précède le verbe, à l'inverse de plusieurs langues.",
              notes="Faire recopier. Cette diapo répond à 90 % des questions du groupe.")

    d.regle('y, collé devant le verbe',
            "y se place avant le verbe, jamais après.",
            precision="« J'y vais » et non « je vais y ». Au passé composé, y passe devant "
                      "l'auxiliaire : « j'y suis allée deux fois ». Avec deux verbes, y se "
                      "met devant celui qui porte le sens : « je vais y aller ».",
            notes="Les trois cas au tableau, l'un sous l'autre. Faire produire une phrase "
                  "de chaque type par trois élèves.")

    d.regle('là, après le verbe',
            "là montre un endroit dont on vient de parler.",
            precision="« Le balcon ? On mangeait là tous les soirs. » · « Je suis restée là "
                      "trois heures. » là est plus concret que y : il est proche du geste "
                      "de montrer du doigt.",
            notes="Les deux mots sont souvent interchangeables. Le dire : ne pas laisser un "
                  "élève bloquer sur ce choix.")

    d.piege('Répéter le lieu après y',
            "J'y vais au centre communautaire le jeudi.",
            "J'y vais le jeudi.",
            "Si vous dites y, le lieu est déjà dedans. Le répéter est une faute, et elle "
            "s'entend tout de suite — c'est comme dire deux fois le même mot. La phrase "
            "juste est plus courte, et c'est justement l'intérêt.",
            notes="Faire entendre la faute : lire la phrase de gauche à voix haute, "
                  "lentement. Le groupe réagit.")

    d.pratique('Pratique · 1 de 2', "y ou là ?",
               "Remplacez le lieu souligné.", [
        ("Je vais au centre communautaire. › J'___ vais le jeudi.", "y"),
        ("Elle joue dans cette équipe. › Elle ___ joue depuis six ans.", "y"),
        ("On mangeait sur le balcon. › On mangeait ___ tous les soirs.", "là"),
        ("Je suis allée à Québec. › J'___ suis allée le mois passé.", "y"),
        ("Elle est restée dans le vestiaire. › Elle est restée ___ trois heures.", "là"),
        ("Nous habitons chez ma sœur. › Nous ___ habitons depuis mars.", "y"),
    ], corrige=True,
       notes="Aux lignes 3 et 5, y serait aussi acceptable. Le dire, et expliquer pourquoi "
             "là sonne mieux : le lieu vient d'être nommé et on y fait quelque chose.")

    d.pratique('Pratique · 2 de 2', "Corrigez la phrase",
               "Chaque phrase contient une faute de place ou une répétition.", [
        ("Je vais y le jeudi soir.", "J'y vais le jeudi soir."),
        ("J'y suis allée à Québec le mois passé.", "J'y suis allée le mois passé."),
        ("Elle joue y depuis six ans.", "Elle y joue depuis six ans."),
        ("Nous y habitons chez ma sœur.", "Nous y habitons depuis mars."),
    ], corrige=True, cols=1,
       notes="Faire venir quatre élèves au tableau, un par phrase. Demander de nommer la "
             "faute avant de corriger.")

    d.cartes('Pour aller plus loin', "Trois emplois très courants", [
        ("« J'y vais »",
         "La phrase la plus employée du français parlé. Elle veut dire « je pars » autant "
         "que « je m'y rends »."),
        ("« On y va ? »",
         "Une invitation à partir. C'est la phrase de Chantal à la fin du premier dialogue "
         "du module."),
        ("« Il y a »",
         "Attention : ici, y ne remplace rien. « Il y a » est une expression figée qui "
         "annonce l'existence de quelque chose."),
    ], notes="La troisième carte évite une confusion fréquente. Ne pas s'y attarder plus "
             "de deux minutes.")

    d.billet(
        "Écrivez quatre phrases sur des lieux de votre semaine, deux avec y, deux avec là.",
        exemples=[
            "Nommez le lieu dans une première phrase, puis remplacez-le dans la suivante.",
            "Exemple : « Je vais au parc le dimanche. J'y vais avec mes enfants. »",
        ],
        notes="Corriger surtout la place du pronom et l'absence de répétition.")

    return d.save(dossier)
