# -*- coding: utf-8 -*-
"""A4 · « Ce qu'on voit dans un fait divers »
Bloc A « Je découvre » · couleur ambre · 75 min. Lecture d'images et sources.
Source : exercices `prImg`, `prMot`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-actualite/images/')


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Ce qu'on voit dans un fait divers",
        chapeau="Un fait divers arrive rarement seul : il y a une photo, "
                "et sous la photo une légende d'une ligne. La photo montre "
                "l'après — les fenêtres noircies, l'eau dans le sous-sol, "
                "la porte du cabanon restée ouverte.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. Elle referme la découverte : après la "
                  "forme du texte, les sons et les mots, on regarde ce que le journal "
                  "montre. Commencer par projeter une photo sans rien dire et laisser "
                  "le groupe raconter ce qu'il voit.")

    d.objectifs([
        "décrire en une phrase ce qu'une photo de fait divers montre ;",
        "distinguer ce qui est visible sur la photo de ce qu'on suppose ;",
        "repérer qui parle dans un fait divers, et au nom de qui ;",
        "employer les mots du module pour décrire une scène.",
    ], notes="Le deuxième objectif prépare tout le bloc D : ce qu'on voit est un fait, "
             "ce qu'on en conclut est une opinion. Le dire dès maintenant, en une "
             "phrase, sans y insister.")

    d.declencheur(
        'Observation', "Un immeuble aux fenêtres noircies. "
                       "Qu'est-ce qu'on sait, et qu'est-ce qu'on suppose ?",
        image=IMG + 'immeuble-incendie.jpg',
        pistes=[
            "Ce qu'on voit : les fenêtres, la façade, l'heure du jour.",
            "Ce qu'on suppose : la cause, le nombre de personnes, l'heure du feu.",
            "Qui pourrait parler dans l'article, à votre avis ?",
            "Quelle serait la légende de cette photo, en une ligne ?",
        ],
        notes="Faire tenir la distinction pendant tout l'exercice : on voit des "
              "fenêtres noircies, on ne voit pas un incendie. La photo est prise le "
              "lendemain, et c'est vrai de presque toutes les photos de fait divers.")

    d.cartes("Six photos, six phrases", "Ce que montre chaque image de l'activité", [
        ("Le journal sur la table",
         "Un journal de quartier ouvert sur une table de cafétéria."),
        ("L'immeuble le lendemain",
         "Un immeuble aux fenêtres noircies, le lendemain d'un feu."),
        ("Le sous-sol",
         "Un sous-sol où l'eau monte au-dessus des boîtes rangées."),
        ("Le cabanon",
         "Une petite bâtisse de cour, la porte grande ouverte."),
        ("Les pompiers",
         "Deux pompiers qui tiennent un boyau devant une façade."),
        ("La porte-parole",
         "Une femme qui parle devant plusieurs micros tendus."),
    ], cols=3,
       notes="Projeter, faire décrire à l'oral, puis ouvrir l'exercice prImg dans "
             "l'activité : les six photos s'y glissent sur leur phrase. La description "
             "orale doit venir avant la manipulation.")

    d.declencheur(
        'Observation', "Une femme parle devant des micros. "
                       "Qui est-elle, et au nom de qui parle-t-elle ?",
        image=IMG + 'porte-parole-micros.jpg',
        pistes=[
            "Un témoin parle en son nom : il raconte ce qu'il a vu.",
            "Une porte-parole parle au nom d'un service : la Ville, la police.",
            "Le journal écrit « la Ville dit que », pas « madame Untel pense que ».",
            "Un voisin qui répète ce qu'il a entendu ne parle au nom de personne.",
        ],
        notes="La deuxième piste est celle qui compte. Quand une porte-parole parle, "
              "ce n'est pas son avis à elle : c'est la position du service. La nuance "
              "a l'air petite ; elle est énorme, et le bloc C entier repose dessus.")

    d.regle("Une photo montre l'après, jamais l'évènement",
            "Le photographe arrive après les pompiers. Ce qu'on voit, "
            "c'est ce qui reste.",
            precision="Des fenêtres noircies, de l'eau dans un sous-sol, une porte "
                      "ouverte. La photo prouve qu'il y a eu quelque chose ; elle ne "
                      "dit ni quand, ni comment, ni pourquoi. Ces trois "
                      "renseignements-là ne sont que dans le texte.",
            notes="Diapositive à photographier. Elle justifie tout le module : si la "
                  "photo suffisait, personne n'aurait besoin de raconter.")

    d.tableau('Sur la photo', "Ce qui se voit, ce qui se lit",
              ['On le voit', 'On le lit seulement'],
              [["Des fenêtres noircies", "Le feu a éclaté vers quatre heures"],
               ["De l'eau dans un sous-sol", "La rivière montait depuis trois jours"],
               ["Une porte de cabanon ouverte", "Une trentaine de vélos ont disparu"],
               ["Des pompiers avec un boyau", "Ils sont arrivés huit minutes après"],
               ["Une femme devant des micros", "Elle parle au nom de la Ville"]],
              cle=1,
              notes="Faire cacher la colonne de droite et demander au groupe ce qui "
                    "manque à chaque photo. La réponse est toujours la même : l'heure, "
                    "la durée, le nombre, la source. C'est ce que la parole apporte.")

    d.pratique('Description', "Décrivez la scène en une phrase",
               "Employez les mots du module, et rien que ce que vous voyez.", [
        ("La photo de l'immeuble", "des fenêtres noircies après un incendie"),
        ("La photo du sous-sol", "de l'eau au-dessus des boîtes, après une inondation"),
        ("La photo du cabanon", "une porte de cabanon laissée grande ouverte"),
        ("La photo des pompiers", "deux pompiers qui tiennent un boyau devant une façade"),
        ("La photo de la femme", "une porte-parole qui fait une déclaration"),
        ("La photo du journal", "un hebdomadaire ouvert sur une table"),
    ], corrige=True,
       notes="Exercice prImg de l'activité. Exiger l'article et un mot du module dans "
             "chaque phrase : c'est le premier réinvestissement du vocabulaire de A3.")

    d.piege("Raconter ce que la photo laisse croire",
            "On voit que le feu est parti de la cuisine.",
            "On voit les fenêtres noircies du deuxième étage.",
            "Une photo ne dit jamais la cause. Quand vous racontez, séparez ce que "
            "vous avez vu de ce que vous avez lu, et ce que vous avez lu de ce que "
            "vous supposez.",
            notes="Piège central du module, posé ici sous sa forme la plus simple. Il "
                  "reviendra au bloc C sous la forme « qui l'a dit ? » et au bloc D "
                  "sous la forme « fait ou opinion ? ».")

    d.billet(
        "Décrivez en deux phrases une photo de journal que vous avez vue récemment.",
        exemples=[
            "Première phrase : ce qu'on voit. Deuxième phrase : ce que vous en avez conclu.",
            "Soulignez la deuxième : c'est la partie qui n'est pas dans la photo.",
        ],
        notes="Fin du bloc A. Ramasser et relire deux billets en ouverture de B1 : la "
              "séparation entre ce qu'on voit et ce qu'on conclut est exactement ce "
              "qui va manquer aux premiers récits du bloc B.")

    return d.save(dossier)
