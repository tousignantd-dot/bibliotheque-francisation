# -*- coding: utf-8 -*-
"""B2 · Est-ce que vous engagez ?
Bloc B « Défi 1 » · couleur ambre · 75 min. Écriture et question.
Source du module : exercice `t1quest` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre='Est-ce que vous engagez ?',
        chapeau="Une question se pose de trois façons en français. Au "
                "comptoir d'un commerce, c'est toujours la même qui sert, et "
                "elle s'apprend par cœur.",
        duree='75 minutes')

    d.titre(notes="Séance de langue. Lire d'abord deux ou trois billets de B1, sans "
                  "nommer personne, et faire améliorer la formulation par le groupe.")

    d.objectifs([
        "poser une question avec « est-ce que » ;",
        "choisir la bonne question selon la situation ;",
        "demander à qui parler quand le patron est absent ;",
        "éviter les formulations qui ferment la porte.",
    ])

    d.tableau('Analyse', "Trois façons de poser la même question",
              ['La forme', "L'exemple", 'Quand'],
              [["La voix qui monte", "Vous engagez ?", "entre gens qui se connaissent"],
               ["Est-ce que devant", "Est-ce que vous engagez ?", "partout, et c'est celle-ci"],
               ["Le verbe retourné", "Engagez-vous ?", "à l'écrit, dans une lettre"],
               ["Jamais les deux", "Est-ce que engagez-vous ?", "cette forme n'existe pas"]],
              cle=1,
              note="« Est-ce que » se pose devant, et la phrase ne change pas d'ordre.",
              notes="Diapo à photographier. La dernière ligne est l'erreur la plus "
                    "fréquente : la faire entendre une fois, puis ne plus la répéter.")

    d.regle("Après « est-ce que », rien ne bouge",
            "Est-ce que vous engagez ?",
            precision="La phrase qui suit garde l'ordre normal : sujet, puis verbe. "
                      "On ne retourne rien. C'est ce qui rend cette forme si commode : "
                      "on prend n'importe quelle phrase et on pose « est-ce que » devant.",
            notes="Diapo à photographier. Faire fabriquer cinq questions au groupe à "
                  "partir de phrases ordinaires, en direct.")

    d.cartes("Quatre questions à savoir par cœur", "Selon ce qu'on trouve sur place", [
        ("Il y a une affiche",
         "« Est-ce que vous engagez encore ? » Le mot « encore » évite le malaise : "
         "une affiche reste souvent collée une semaine après l'embauche."),
        ("Il n'y a pas d'affiche",
         "« Est-ce que vous cherchez quelqu'un ? » La plus large. Elle sert dans "
         "n'importe quel commerce, même sans rien d'affiché."),
        ("Le poste est peut-être comblé",
         "« Est-ce que le poste est encore libre ? » Polie et prudente : elle laisse à "
         "l'autre une réponse facile s'il a déjà engagé."),
        ("Le patron n'est pas là",
         "« À qui est-ce que je peux parler ? » Repartir avec un nom et une heure vaut "
         "mieux qu'une visite perdue. On revient le lendemain en demandant la personne."),
    ], notes="Faire choisir à chacun les deux questions qu'il apprendra par cœur, et "
             "les faire écrire sur le papier commencé en A4.")

    d.piege("Dire « je veux du travail »",
            "Je veux du travail.",
            "Je cherche du travail. / Je viens offrir mes services.",
            "« Je veux » sonne exigeant en français, et l'effet est immédiat sur le "
            "visage de l'autre. « Je cherche » dit exactement la même chose sans "
            "l'exigence. « J'offre mes services » va encore plus loin : c'est vous qui "
            "apportez quelque chose.",
            notes="Nuance difficile à sentir. La faire entendre en jouant les deux "
                  "versions, avec le même ton, et demander laquelle donne envie.")

    d.pratique('Écriture', "Complétez la question",
               "Complétez avec : engagez, cherchez, poste, travail, embauche.", [
        ("Est-ce que vous ___ encore, madame ?", "engagez"),
        ("Est-ce que vous ___ quelqu'un pour le matin ?", "cherchez"),
        ("Est-ce que le ___ est encore libre ?", "poste"),
        ("Je cherche du ___ pour le matin seulement.", "travail"),
        ("Sur l'affiche, c'est écrit : « On ___ . »", "embauche"),
        ("C'est un ___ de commis au comptoir.", "poste"),
    ], corrige=True,
       notes="Même exercice que t1quest dans le module. Faire relire chaque question "
             "complétée à voix haute, avec l'intonation montante.")

    d.pratique('Transformation', "Posez la question avec « est-ce que »",
               "Transformez chaque phrase en question.", [
        ("Vous engagez.", "Est-ce que vous engagez ?"),
        ("Vous cherchez quelqu'un.", "Est-ce que vous cherchez quelqu'un ?"),
        ("Le poste est encore libre.", "Est-ce que le poste est encore libre ?"),
        ("Je peux laisser mon numéro.", "Est-ce que je peux laisser mon numéro ?"),
        ("Vous engagez pour le matin.", "Est-ce que vous engagez pour le matin ?"),
        ("Il faut de l'expérience.", "Est-ce qu'il faut de l'expérience ?"),
    ], corrige=True,
       notes="Insister sur la dernière : « est-ce qu'il » se dit d'une seule coulée. "
             "Le faire répéter séparément.")

    d.pratique('Oral', "Deux par deux, trois situations",
               "L'un entre, l'autre tient le commerce. On change après chaque situation.", [
        ("Une affiche dans la vitrine", "Est-ce que vous engagez encore ?"),
        ("Aucune affiche", "Est-ce que vous cherchez quelqu'un ?"),
        ("Le patron est absent", "À qui est-ce que je peux parler ?"),
    ], notes="Quinze minutes. Passer dans les rangées et n'écouter que la question "
             "d'ouverture : le reste vient en B3 et B4.")

    d.billet(
        "Écrivez la question que vous poserez, et à quel commerce.",
        exemples=[
            "La question, mot pour mot.",
            "Le nom du commerce, celui de votre billet de A3.",
        ],
        notes="Deux minutes. Garder les billets : ils servent de liste de départ en E1.")

    return d.save(dossier)
