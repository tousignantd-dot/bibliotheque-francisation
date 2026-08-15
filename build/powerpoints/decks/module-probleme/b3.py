# -*- coding: utf-8 -*-
"""B3 · Depuis, depuis que, ça fait… que.
Bloc B · couleur ambre (écriture) · 90 min.
Source : mini-leçon `t1depuis`, exercices `t1depuis` et `t1duree`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre='Dire depuis quand un problème dure',
        chapeau="Dès que vous signalez un problème, la personne propriétaire va demander "
                "« depuis quand ? ». Cette réponse décide souvent de l'urgence de "
                "l'intervention. Le français offre trois façons de la donner.",
        duree='90 minutes')

    d.titre(notes="Séance longue et centrale. Trois marqueurs, un seul sens. Prévoir "
                  "beaucoup de production orale avant l'écrit.")

    d.objectifs([
        "répondre à la question « depuis quand ? » de trois façons différentes ;",
        "choisir entre depuis, depuis que et ça fait… que en regardant ce qui suit ;",
        "garder le verbe au présent quand la situation dure encore ;",
        "mettre la durée en valeur quand je trouve que ça traîne.",
    ])

    d.regle('Le point commun',
            "Dans les trois cas, le verbe reste au présent, parce que la situation dure encore.",
            precision="« Le robinet coule depuis deux jours » — et il coule toujours en ce "
                      "moment. C'est la différence la plus importante avec beaucoup d'autres "
                      "langues, où on emploierait un temps du passé.",
            notes="Point capital à installer avant les trois marqueurs. Le répéter à chaque "
                  "exemple de la séance.")

    d.tableau('Analyse · 1 de 3', "depuis + un nom ou une durée",
              ['Élément', 'Exemple', 'Remarque'],
              [["La situation", "Le calorifère est froid", "au présent"],
               ["Le marqueur", "depuis", "jamais de verbe après"],
               ["Un nom ou une durée", "avant-hier", "ou : deux jours, lundi"]],
              cle=1,
              note="Deux emplois dans un seul mot : depuis lundi donne le point de départ, "
                   "depuis deux jours donne la durée. La phrase complète : « Le calorifère "
                   "est froid depuis avant-hier. »",
              notes="Faire produire cinq phrases orales avec depuis avant de passer au "
                    "deuxième marqueur.")

    d.tableau('Analyse · 2 de 3', "depuis que + une phrase complète",
              ['Élément', 'Exemple', 'Remarque'],
              [["La situation", "La porte n'ouvre plus", "au présent"],
               ["Le marqueur", "depuis que", "le que change tout"],
               ["Sujet + verbe conjugué", "vous avez ajouté un vélo", "une phrase entière"]],
              cle=1,
              note="Depuis que relie deux actions : la deuxième dure depuis que la première "
                   "a eu lieu. C'est le marqueur qui explique une cause dans le temps.",
              notes="Insister : c'est le petit mot « que » qui autorise un verbe conjugué "
                    "après. Sans lui, pas de verbe.")

    d.tableau('Analyse · 3 de 3', "ça fait… que + une phrase complète",
              ['Élément', 'Exemple', 'Remarque'],
              [["L'ouverture", "Ça fait", "la durée passe en premier"],
               ["La durée", "deux semaines", "c'est elle qu'on met en valeur"],
               ["que + phrase", "que la tache est là", "le que est obligatoire"]],
              cle=1,
              note="C'est la forme la plus fréquente à l'oral au Québec. Elle sert souvent "
                   "à faire sentir que c'est long — donc à insister sans hausser le ton.",
              notes="Point pragmatique important : choisir « ça fait… que » est déjà une "
                    "façon polie de se plaindre. On y reviendra à la séance D2.")

    d.cartes('Comparer', "La même idée, trois formulations", [
        ("depuis + durée",
         "« La tache est là depuis deux semaines. » Neutre. On informe, on ne commente pas."),
        ("ça fait… que",
         "« Ça fait deux semaines que la tache est là. » Le contenu est identique, mais la "
         "durée ouvre la phrase : on insiste sur la longueur."),
        ("depuis que + phrase",
         "« La tache grossit depuis qu'il a plu dimanche. » Ce n'est plus une durée, c'est "
         "une cause : on relie le problème à un événement."),
        ("Laquelle choisir ?",
         "Depuis pour informer. Ça fait… que quand on commence à trouver le temps long. "
         "Depuis que quand on sait d'où vient le problème."),
    ], notes="La quatrième carte est le vrai apprentissage : les trois formes ne sont pas "
             "interchangeables au niveau du ton, même si elles le sont au niveau du sens.")

    d.regle('Comment choisir en deux secondes',
            "Regardez ce qui vient après.",
            precision="Un nom ou une durée seule — deux jours, hier, ce matin : depuis. "
                      "Un verbe conjugué : depuis que. Vous voulez commencer la phrase par "
                      "la durée : ça fait… que.",
            notes="Écrire ces trois lignes au tableau. C'est la diapo à photographier.")

    d.pratique('Pratique', 'Complétez',
               "Avec depuis, depuis que ou ça fait.", [
        ("Le calorifère ne chauffe plus ___ avant-hier.", "depuis"),
        ("___ deux semaines que cette tache est au plafond.", "Ça fait"),
        ("La porte n'ouvre plus au complet ___ Jean-Philippe a ajouté un vélo.", "depuis que"),
        ("Les voisins se plaignent ___ un mois.", "depuis"),
        ("___ trois jours qu'Oksana attend l'électricien.", "Ça fait"),
        ("L'escalier reste propre ___ le concierge a posé un tapis.", "depuis que"),
    ], corrige=True,
       notes="Faire justifier chaque réponse à voix haute : « après, il y a un nom » ou "
             "« après, il y a un sujet et un verbe ». C'est le raisonnement qu'il faut "
             "automatiser, pas la réponse.")

    d.piege('Le temps du verbe',
            "J'ai habité ici depuis deux ans.",
            "J'habite ici depuis deux ans.",
            "En français, une action qui dure encore reste au présent avec depuis. Le passé "
            "composé voudrait dire que vous n'y habitez plus. C'est une des différences les "
            "plus visibles avec l'anglais et avec plusieurs autres langues, où le temps du "
            "passé est obligatoire dans cette phrase.",
            notes="Erreur extrêmement fréquente et très durable. La signaler chaque fois "
                  "qu'elle apparaît, jusqu'à la fin du module.")

    d.piege('Le que oublié',
            "Ça fait deux semaines la tache est là.",
            "Ça fait deux semaines que la tache est là.",
            "Le que est obligatoire : c'est lui qui relie la durée à la phrase qui suit. "
            "C'est l'oubli le plus fréquent des trois. Attention aussi à l'inverse : "
            "« depuis que hier » est incorrect, parce que hier n'est pas une phrase — "
            "on dit simplement « depuis hier ».",
            notes="Deux pièges symétriques : le que manquant, et le que en trop. Les "
                  "présenter ensemble aide à les distinguer.")

    d.pratique('Pratique', 'Quelle est la durée ?',
               "Lisez la phrase et écrivez seulement la durée ou le moment de départ.", [
        ("Ça fait deux semaines que la tache est au plafond.", "deux semaines"),
        ("La serrure est brisée depuis samedi passé.", "samedi passé"),
        ("Le robinet de la cuisine coule depuis deux jours.", "deux jours"),
        ("Ça fait un mois que les voisins se plaignent.", "un mois"),
        ("Ça fait trois heures que nous attendons le plombier.", "trois heures"),
    ], corrige=True, cols=2,
       notes="Exercice de repérage. Il prépare la production : pour dire depuis quand, il "
             "faut d'abord savoir isoler la durée.")

    d.pratique('Vérification', 'Cinq questions rapides',
               "Répondez sans regarder vos notes.", [
        ("Le calorifère est froid ___ trois jours.", "depuis — une durée, pas une phrase"),
        ("Tout va mieux ___ le concierge est arrivé.", "depuis que — un sujet et un verbe"),
        ("___ un mois que j'attends la réparation.", "Ça fait"),
        ("Quel temps de verbe emploie-t-on avec depuis ?", "le présent"),
        ("Ça fait deux jours ___ il pleut.", "qu' — le que est obligatoire"),
    ], corrige=True)

    d.billet(
        "Dites depuis quand dure un problème de votre logement — de deux façons différentes.",
        exemples=[
            "Une phrase avec depuis, une phrase avec ça fait… que.",
            "Exemple : « Mon robinet coule depuis trois jours. » / « Ça fait trois jours que mon robinet coule. »",
        ],
        notes="Deux phrases, pas une. C'est la reformulation qui prouve la compréhension, "
              "pas la production d'une seule forme.")

    return d.save(dossier)
