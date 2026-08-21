# -*- coding: utf-8 -*-
"""B3 · Les pronoms au téléphone.
Bloc B « Défi 1 · Le camion » · couleur ambre · 75 min.
Source : exercice `t1pron` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Les pronoms au téléphone",
        chapeau="Ce qui sépare parler d'énumérer : ne pas répéter « le "
                "camion » à chaque phrase.",
        duree='75 minutes')

    d.titre(notes="Première séance de grammaire du défi 1. Au niveau 5, la difficulté "
                  "n'est plus de trouver les mots : c'est de faire tenir trois phrases "
                  "ensemble. Les pronoms sont l'outil de cela.")

    d.objectifs([
        "employer le, la, les après un verbe sans préposition ;",
        "employer lui et leur après un verbe avec « à » ;",
        "employer y pour un lieu, en pour une quantité ;",
        "placer le pronom devant le verbe, même à la négative.",
    ])

    d.tableau('Les quatre familles', "Quel pronom, et pourquoi",
              ['Le pronom', 'Il remplace', 'Exemple'],
              [["le · la · les", "une chose ou une personne, sans préposition",
                "Je réserve le camion. donne Je le réserve."],
               ["lui · leur", "une personne annoncée par « à »",
                "Je téléphone à la répartitrice. donne Je lui téléphone."],
               ["y", "un lieu, ou « à + une chose »",
                "Je vais à Limoilou. donne J'y vais."],
               ["en", "« de + quelque chose », ou une quantité",
                "J'ai quinze boîtes. donne J'en ai quinze."]],
              cle=0,
              note="Pour choisir : posez « quoi ? » après le verbe. Si la réponse vient "
                   "sans « à », c'est le, la ou les.",
              notes="Diapositive à photographier. C'est le tableau de référence de toute "
                    "la séance.")

    d.regle("Le pronom passe devant le verbe",
            "Je le réserve. Je vais le rappeler. Je lui ai téléphoné.",
            precision="C'est l'inverse de l'anglais et de bien d'autres langues, et c'est "
                      "la première chose à automatiser. Avec deux verbes, le pronom se "
                      "colle à celui qui porte le sens : « je vais le rappeler ».",
            notes="Faire dire la phrase fausse à voix haute — « je réserve le » — pour "
                  "entendre qu'elle ne tient pas. L'oreille apprend vite ici.")

    d.cartes("Deux pronoms qu'on n'ose pas employer", "Et qui font toute la différence", [
        ("y", "« J'y pense. » C'est une des phrases les plus fréquentes du français "
              "parlé. Elle ne s'analyse pas : elle s'apprend telle quelle."),
        ("en", "« J'en ai quinze. » Le nombre reste à la fin : le « en » ne le "
               "remplace pas, il l'annonce."),
        ("Pour une personne", "On garde la préposition : « je pense à elle », jamais "
                             "« j'y pense » pour quelqu'un."),
        ("Avec une quantité", "« — Combien de boîtes ? — J'en ai. » ne répond pas. Il "
                             "faut « j'en ai quinze »."),
    ], notes="Ces deux pronoms sont ceux que les élèves évitent le plus longtemps. Les "
             "faire employer dix fois de suite : c'est de la répétition, pas de "
             "l'explication.")

    d.piege("Dire « à lui », « à leur »",
            "Je téléphone à lui demain.",
            "Je lui téléphone demain.",
            "Après un verbe qui demande « à », on dit simplement « lui » ou « leur », "
            "devant le verbe. « À lui » ne s'emploie que pour insister : « c'est à lui "
            "que je parle, pas à vous ».",
            notes="Faire chercher trois autres verbes avec « à » : parler à, écrire à, "
                  "demander à, répondre à.")

    d.regle("À la négative, le « ne » passe avant le pronom",
            "Je ne lui ai pas téléphoné.",
            precision="L'ordre est : ne · pronom · auxiliaire · pas · participe. Jamais "
                      "« je lui ne pas ». Les quatre morceaux se placent toujours dans "
                      "le même ordre.",
            notes="Écrire l'ordre au tableau et le laisser pendant l'exercice suivant. "
                  "Beaucoup d'élèves n'y arrivent qu'en le voyant.")

    d.pratique('Transformation', "Remplacez par un pronom",
               "L'enseignante lit la phrase ; le groupe la redit avec un pronom.", [
        ("Je réserve le camion.", "Je le réserve."),
        ("Je téléphone à la répartitrice.", "Je lui téléphone."),
        ("Je vais à Limoilou.", "J'y vais."),
        ("J'ai besoin de couvertures.", "J'en ai besoin."),
        ("J'écris aux déménageurs.", "Je leur écris."),
        ("Je n'ai pas téléphoné à la compagnie.", "Je ne lui ai pas téléphoné."),
    ], corrige=True,
       notes="C'est le laboratoire de la mini-leçon t1pron. Aller vite : six phrases en "
             "cinq minutes, puis recommencer dans le désordre.")

    d.pratique('Dialogue', "Répondez sans répéter",
               "Par deux : l'un pose la question, l'autre répond avec un pronom.", [
        ("— Vous avez rappelé la répartitrice ?", "— Oui, je lui ai téléphoné hier."),
        ("— Et le camion, vous l'avez réservé ?", "— Je le réserve demain matin."),
        ("— Il vous faut des boîtes ?", "— Il m'en faut une vingtaine."),
        ("— Vous allez souvent à Limoilou ?", "— J'y vais deux fois par semaine."),
        ("— Vous leur avez parlé de l'escalier ?", "— Je leur en ai parlé au téléphone."),
        ("— Vous pensez au relevé de compteur ?", "— J'y pense, ne vous inquiétez pas."),
    ], corrige=True,
       notes="Ce sont les items de l'exercice t1pron. Les faire d'abord à l'oral, par "
             "deux : l'écran viendra ensuite confirmer.")

    d.billet(
        "Écrivez trois phrases sur votre semaine, chacune avec un pronom différent.",
        exemples=[
            "Une avec « le » ou « la », une avec « lui », une avec « y » ou « en ».",
            "Relisez-les à voix haute : le pronom doit être devant le verbe.",
        ],
        notes="La consigne force à sortir du vocabulaire du déménagement, ce qui est le "
              "but : le pronom doit servir partout.")

    return d.save(dossier)
