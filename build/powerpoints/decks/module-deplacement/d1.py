# -*- coding: utf-8 -*-
"""D1 · Les annonces qu'on entend.
Bloc D « Défi 3 · Les messages qu'on entend » · couleur acier · 60 min.
Source : dialogue `t3`, exercices `t3vf` et `t3annonce`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Les annonces qu'on entend",
        chapeau="Trois secondes, un haut-parleur, du bruit de foule. Les "
                "annonces du transport sont courtes et souvent mal audibles — "
                "mais elles suivent toujours la même forme.",
        duree='60 minutes')

    d.titre(notes="Séance d'écoute. Prévoir le son. Faire le lien avec A2 : les consonnes "
                  "qui tombent expliquent la moitié de ce que le groupe n'entend pas.")

    d.objectifs([
        "reconnaître les quatre types d'annonce du transport ;",
        "distinguer une annonce qui informe d'une annonce qui demande ;",
        "repérer les deux mots qui annoncent un problème ;",
        "savoir quoi faire quand on n'a pas tout entendu.",
    ])

    d.declencheur(
        'Écoute', "Qu'avez-vous compris ?",
        pistes=[
            "« En raison de travaux, l'autobus 45 ne dessert pas l'arrêt Sainte-Foy. »",
            "Quels mots avez-vous saisis ?",
            "Est-ce une bonne ou une mauvaise nouvelle pour vous ?",
            "Que faites-vous maintenant ?",
        ],
        notes="Faire écouter une seule fois, puis demander ce qui a été compris. Le mot "
              "« dessert » sera rarement saisi : c'est justement le mot clé.")

    d.tableau('Analyse', "Les quatre types d'annonce",
              ['Le type', 'Exemple'],
              [["Le prochain arrêt", "Prochain arrêt : Curé-Poirier."],
               ["Une consigne", "Laissez descendre avant de monter."],
               ["Un problème de service", "Le service est interrompu."],
               ["Un départ", "Dernier appel, quai 12."]],
              cle=2,
              note="Le troisième type est le seul qui vous oblige à changer vos plans.",
              notes="Diapo centrale. Faire recopier. Les élèves n'ont pas à tout comprendre : "
                    "ils doivent reconnaître le type.")

    d.cartes('Les deux mots à reconnaître', "Ceux qui annoncent un problème", [
        ("« ne dessert pas »",
         "L'autobus passe sans s'arrêter à cet arrêt. Il faut descendre avant, ou après. "
         "Le verbe « desservir » n'existe presque que dans ce contexte."),
        ("« interruption de service »",
         "La ligne est coupée entre deux points. Un service de remplacement est presque "
         "toujours annoncé juste après : écoutez la suite."),
        ("Les deux se ressemblent, mais…",
         "« Ne dessert pas » ne touche qu'un arrêt. « Interruption » touche tout un "
         "tronçon. La deuxième est plus grave."),
    ], notes="Ces deux expressions valent à elles seules la séance. Les écrire au tableau "
             "et les faire répéter.")

    d.regle('Informer ou demander',
            "Une annonce vous donne une information, ou vous demande de faire quelque chose.",
            precision="« Prochain arrêt : Curé-Poirier » informe. « Laissez descendre avant "
                      "de monter » demande. Reconnaître lequel des deux, c'est déjà savoir "
                      "s'il faut bouger ou non — même sans avoir tout compris.",
            notes="Les annonces qui demandent sont presque toujours à l'impératif. Faire le "
                  "lien avec B2 : c'est le même temps.")

    d.piege("Faire semblant d'avoir compris",
            "Je n'ai pas compris, mais tout le monde reste assis, alors je reste.",
            "« Excusez-moi, qu'est-ce qu'ils ont dit ? »",
            "Demander à son voisin est parfaitement normal, y compris entre gens d'ici — "
            "les annonces sont souvent inaudibles pour tout le monde. La phrase tient en "
            "cinq mots et évite de rater son arrêt.",
            notes="Faire répéter la phrase par le groupe. C'est une phrase de survie "
                  "urbaine, pas un aveu de faiblesse.")

    d.pratique('Pratique', "On m'informe, ou on me demande ?",
               "Écoutez chaque annonce.", [
        ("Prochain arrêt : boulevard Curé-Poirier.", "on m'informe"),
        ("Laissez descendre avant de monter.", "on me demande"),
        ("En raison de travaux, l'autobus ne dessert pas cet arrêt.", "on m'informe"),
        ("Attention à l'espace entre le quai et la voiture.", "on me demande"),
        ("Tous les passagers doivent descendre.", "on me demande"),
        ("Un service d'autobus est offert à la sortie.", "on m'informe"),
    ], corrige=True,
       notes="Utiliser l'exercice 2 du Défi 3 pour l'écoute. Deux passages avant de donner "
             "la réponse.")

    d.cartes('Quand on n\'a pas tout entendu', "Trois recours", [
        ("Regarder l'afficheur",
         "La plupart des véhicules affichent le prochain arrêt à l'écran. L'annonce "
         "sonore n'est qu'un doublon."),
        ("Demander à son voisin",
         "« Excusez-moi, qu'est-ce qu'ils ont dit ? » Personne ne s'en offusque."),
        ("Descendre et vérifier",
         "En cas de doute sérieux, descendre au prochain arrêt coûte cinq minutes. Rester "
         "dans le doute peut en coûter quarante."),
    ], notes="La troisième carte reprend la leçon de C4. La cohérence entre les séances "
             "aide les élèves à retenir.")

    d.billet(
        "Notez une annonce entendue cette semaine dans un lieu public.",
        exemples=[
            "Dans l'autobus, au métro, à l'épicerie, à l'hôpital.",
            "De quel type était-elle ? Vous informait-elle, ou vous demandait-elle quelque chose ?",
        ],
        notes="Les relevés font une excellente entrée en matière pour D2. En lire deux ou "
              "trois à voix haute.")

    return d.save(dossier)
