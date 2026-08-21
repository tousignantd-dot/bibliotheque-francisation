# -*- coding: utf-8 -*-
"""A4 · À Rimouski, en Gaspésie, au Saguenay
Bloc A « Je découvre » · couleur ambre · 75 min. Écriture.
Source : exercice `prPrep` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="À Rimouski, en Gaspésie, au Saguenay",
        chapeau="Dire où l'on va demande de choisir une préposition, et le "
                "choix ne s'entend pas : il dépend du genre du lieu et de sa "
                "nature. Une ville, une région, une province, un pays — "
                "chacun a la sienne, et elle ne change jamais.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, la première du module. Elle est courte à "
                  "expliquer et longue à automatiser : prévoir beaucoup de répétition "
                  "orale plutôt qu'un long exposé. Le tableau de la règle reste projeté "
                  "toute la séance.")

    d.objectifs([
        "choisir entre « à », « en » et « au » selon le lieu ;",
        "dire où l'on va et d'où l'on vient dans la même phrase ;",
        "nommer cinq régions du Québec avec leur préposition ;",
        "écrire trois phrases justes sur un voyage qu'on aimerait faire.",
    ], notes="Le deuxième objectif est celui qui sert au comptoir : « Je pars de "
             "Montréal et je vais à Rimouski » est la phrase que Thuy dit en B1.")

    d.regle("Trois prépositions, trois sortes de lieux",
            "« À » devant une ville. « En » devant une région ou un pays "
            "féminin. « Au » devant un lieu masculin.",
            precision="Rien ne s'entend : il faut savoir si le nom est masculin ou "
                      "féminin. On l'apprend avec le nom, une fois pour toutes.",
            notes="Diapositive à photographier. Ne pas chercher de truc pour deviner le "
                  "genre des régions : il n'y en a pas de fiable. Le tableau suivant "
                  "donne les cinq qui servent vraiment.")

    d.tableau('Les lieux du module', "Où va-t-on ?",
              ['Le lieu', 'On dit'],
              [["Rimouski, Québec, Montréal", "à Rimouski, à Québec"],
               ["la Gaspésie, la Mauricie", "en Gaspésie, en Mauricie"],
               ["le Bas-Saint-Laurent", "au Bas-Saint-Laurent"],
               ["le Saguenay, le Québec", "au Saguenay, au Québec"],
               ["les Laurentides", "dans les Laurentides"]],
              cle=1,
              notes="La dernière ligne est la seule irrégulière : un nom de région au "
                    "pluriel prend « dans les ». C'est le cas des Laurentides et des "
                    "Cantons-de-l'Est, deux régions que les élèves nomment souvent.")

    d.cartes("Le piège des deux « Québec »", "Le même mot, deux lieux", [
        ("à Québec",
         "La ville de Québec. Sans article, donc « à »."),
        ("au Québec",
         "La province. Avec l'article « le », donc « au »."),
        ("Je vais à Québec",
         "Je vais dans la ville, en haut du fleuve."),
        ("Je vis au Québec",
         "J'habite la province, où que ce soit."),
    ], notes="Cette distinction fait rire et se retient bien. Elle est aussi utile "
             "administrativement : les formulaires demandent l'un ou l'autre, et les "
             "élèves les confondent.")

    d.tableau("D'où l'on vient", "La même logique, à l'envers",
              ["On va", "On vient"],
              [["à Rimouski", "de Rimouski"],
               ["en Gaspésie", "de Gaspésie"],
               ["au Bas-Saint-Laurent", "du Bas-Saint-Laurent"],
               ["au Viêt Nam", "du Viêt Nam"]],
              cle=1,
              notes="Faire compléter la colonne de droite. La symétrie « au / du » et "
                    "« en / de » est ce qui rend la règle mémorisable : ce n'est pas une "
                    "liste, c'est un système.")

    d.pratique('Application', "Complétez, puis lisez à voix haute",
               "Une phrase chacun, debout.", [
        ("Je pars … Montréal et je vais … Rimouski.", "de … à"),
        ("Ma collègue est née … Bas-Saint-Laurent.", "au"),
        ("Nous passons une semaine … Gaspésie.", "en"),
        ("Le train arrive … Halifax le lendemain matin.", "à"),
        ("Ils ont un chalet … Laurentides.", "dans les"),
        ("Elle est arrivée … Viêt Nam il y a trois ans.", "du"),
    ], corrige=True,
       notes="Faire lire la phrase entière, pas seulement la préposition. La cinquième "
             "et la sixième sont celles que le groupe manque.")

    d.piege("Choisir la préposition d'après le son",
            "Ça sonne mieux avec « en », je mets « en ».",
            "Je regarde si le nom est masculin, féminin, ou au pluriel.",
            "Les deux se prononcent souvent presque pareil dans une phrase rapide, "
            "et l'oreille ne tranche pas. C'est une règle qui se sait, pas une "
            "règle qui s'entend — et c'est une bonne nouvelle : elle ne varie pas.",
            notes="Rassurer : contrairement à beaucoup de points de grammaire française, "
                  "celui-ci n'a presque pas d'exceptions. Ce qui s'apprend une fois "
                  "reste juste.")

    d.billet(
        "Écrivez trois phrases : d'où vous venez, où vous habitez, où vous aimeriez aller.",
        exemples=[
            "Chaque phrase doit contenir une préposition de lieu.",
            "Reprenez la région que vous aviez notée au billet de la séance A1.",
        ],
        notes="Ramasser les billets et les garder : ils reviennent en E2, où le courriel "
              "d'invitation demande exactement ces trois informations.")

    return d.save(dossier)
