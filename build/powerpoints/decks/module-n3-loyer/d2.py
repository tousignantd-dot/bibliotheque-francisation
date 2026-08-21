# -*- coding: utf-8 -*-
"""D2 · Il n'y a pas de stationnement.
Bloc D « Défi 3 · Poser mes questions sur place » · couleur ambre · 75 min.
Source : exercices `t3neg`, `t3quest` et `t3rec`, mini-leçons `t3neg` et `t3rec`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Il n'y a pas de stationnement",
        chapeau="Comprendre un non pendant la visite, et savoir trois choses "
                "avant de dire oui : le bail, sa durée, et l'argent qu'on ne "
                "donne jamais.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc D, et la seule du module qui porte sur les "
                  "droits. Ouvrir avec la dernière ligne du vrai ou faux de la séance "
                  "D1 : « Dilnoza doit donner de l'argent le jour de la visite » était "
                  "faux, et le groupe voudra savoir pourquoi.")

    d.objectifs([
        "comprendre et employer il n'y a pas de, il n'y a pas d' ;",
        "distinguer pas de devant un nom et ne… pas devant un adjectif ;",
        "savoir ce qu'est un bail et combien de temps il dure ;",
        "savoir qu'un dépôt de garantie est interdit au Québec.",
    ])

    d.regle("Après « pas », l'article devient « de »",
            "Il y a un stationnement — il n'y a pas de stationnement",
            precision="Un, une, des, du : tous deviennent « de » après « pas ». "
                      "Une seule forme, quel que soit le genre et le nombre. "
                      "Devant une voyelle, le e tombe : il n'y a pas "
                      "d'ascenseur.",
            notes="Diapositive à photographier. C'est l'une des rares règles vraiment "
                  "simples du français : le dire, ça motive. Faire transformer cinq "
                  "phrases positives à l'oral avant tout écrit.")

    d.tableau('Analyse', "Répondre non, quatre cas",
              ["On dit", "Pourquoi"],
              [["il n'y a pas de stationnement", "devant un nom masculin"],
               ["il n'y a pas de buanderie", "devant un nom féminin"],
               ["il n'y a pas de meubles", "devant un pluriel"],
               ["il n'y a pas d'ascenseur", "devant une voyelle"]],
              cle=0,
              note="Les trois premiers sont identiques : de, toujours de.",
              notes="Diapositive à photographier. Faire remarquer que le genre et le "
                    "nombre ne changent rien ici : c'est la seule fois du module où l'on "
                    "n'a pas à y penser.")

    d.tableau('Analyse', "Devant un adjectif, pas de « de »",
              ["On dit", "Ce qui suit"],
              [["ce n'est pas compris", "un adjectif"],
               ["le logement n'est pas meublé", "un adjectif"],
               ["il n'y a pas de meubles", "un nom"],
               ["nous n'avons pas d'auto", "un nom, avec une voyelle"]],
              cle=0,
              note="Une seule question : est-ce qu'il y a un nom après ?",
              notes="Diapositive à photographier. Donner la méthode en une question, "
                    "comme au tableau : nom ou adjectif ? Le reste suit tout seul.")

    d.tableau('Analyse', "Le bail, en quatre lignes",
              ["Ce qu'on demande", "La réponse"],
              [["Qu'est-ce que c'est ?", "un formulaire officiel, le même partout"],
               ["Qui le fait ?", "le Tribunal administratif du logement"],
               ["Combien de temps ?", "douze mois, du 1er juillet au 30 juin"],
               ["Et après ?", "il se renouvelle tout seul"]],
              cle=0,
              note="Le renouvellement automatique protège le locataire.",
              notes="Diapositive à photographier. Préciser que le Tribunal s'appelait la "
                    "Régie du logement jusqu'en 2020 : les deux noms se disent encore, "
                    "et les élèves entendront les deux.")

    d.tableau('Analyse', "L'argent qu'on donne, et celui qu'on ne donne pas",
              ["La demande", "Ce que dit la loi"],
              [["le premier mois de loyer", "permis, à partir du premier jour"],
               ["un dépôt de garantie", "interdit au Québec"],
               ["le dernier mois d'avance", "interdit aussi"],
               ["une preuve de revenus", "permis de la demander"]],
              cle=0,
              note="Un propriétaire ne peut demander que le premier mois de loyer.",
              notes="Diapositive à photographier. C'est le renseignement le plus utile "
                    "de tout le module. Beaucoup d'élèves ont déjà payé un dépôt sans le "
                    "savoir : le dire sans accuser personne, et sans promettre qu'on "
                    "peut le récupérer facilement.")

    d.piege('Grammaire',
            "« il n'y a pas des meubles »",
            "« il n'y a pas de meubles »",
            "Au pluriel aussi, l'article devient « de ». C'est le piège le "
            "plus fréquent, parce que beaucoup de langues gardent le pluriel "
            "à la forme négative.",
            notes="Faire produire cinq phrases négatives au pluriel à l'oral : pas de "
                  "meubles, pas de rideaux, pas de voisins bruyants. Trois passages "
                  "suffisent d'habitude.")

    d.piege('Démarche',
            "signer le jour de la visite",
            "« Je vais y penser et je vous rappelle demain. »",
            "Personne n'est obligé de signer sur place. Un logement qu'on ne "
            "vous laisse pas le temps de considérer mérite qu'on se méfie.",
            notes="Faire répéter la phrase de sortie par tout le groupe, deux fois. "
                  "C'est une phrase de protection, et elle doit sortir sans hésiter.")

    d.pratique('Grammaire', "De, d' ou pas ?",
               "Complétez chaque réponse négative.", [
        ("Il n'y a pas ___ stationnement dans la cour.", "de"),
        ("Il n'y a pas ___ ascenseur : c'est un vieil immeuble.", "d'"),
        ("Le logement est vide : il n'y a pas ___ meubles.", "de"),
        ("Internet n'est ___ compris dans le loyer.", "pas"),
        ("Nous n'avons pas ___ auto, alors ça ne fait rien.", "d'"),
        ("Il n'y a pas ___ buanderie dans cet immeuble-là.", "de"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice 3 du Défi 3. Faire dire à chaque fois si le mot qui suit "
             "est un nom ou un adjectif : c'est la seule chose à vérifier.")

    d.pratique('Compréhension', "La question et la réponse",
               "Qu'est-ce qu'on vous répond ?", [
        ("Est-ce qu'il y a un stationnement ?", "Non. On se gare dans la rue."),
        ("Est-ce que les fenêtres sont neuves ?", "Elles ont été changées l'an dernier."),
        ("Où sont les chambres ?", "Au fond du couloir."),
        ("La buanderie est ouverte le soir ?", "De sept heures à dix heures."),
        ("L'école est loin ?", "Cinq minutes à pied."),
        ("Est-ce que je dois donner de l'argent ?", "Non. Le premier loyer le premier juillet."),
    ], corrige=True,
       notes="C'est l'exercice 5 du Défi 3. Faire jouer les six échanges à deux, debout, "
             "en se déplaçant dans la classe : une visite ne se fait pas assis.")

    d.billet(
        "Écrivez trois choses qu'il n'y a pas dans votre logement.",
        exemples=[
            "Il n'y a pas de ___ .",
            "Il n'y a pas d'___ . Il n'y a pas de ___ .",
        ],
        notes="Devoir court, et dernier du bloc D. Vérifier surtout le choix entre « de » "
              "et « d' ». Le bloc E commence par la production orale : rappeler aux "
              "élèves d'apporter leur papier de trois questions.")

    return d.save(dossier)
