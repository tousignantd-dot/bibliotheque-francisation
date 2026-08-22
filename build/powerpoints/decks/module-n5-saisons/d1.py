# -*- coding: utf-8 -*-
"""D1 · Qu'est-ce qu'on apporte ?
Bloc D « Défi 3 · Ce qu'il faut apporter » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3a` et `t3equip`.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-saisons/images/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Qu'est-ce qu'on apporte ?",
        chapeau="Madame Bérubé a soixante-quinze ans, des crampons jamais "
                "sortis de leur boîte, et une seule question. La réponse "
                "n'est pas la même en février qu'en juillet — mais elle se "
                "construit de la même façon.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 3, et elle est d'écoute. Faire entendre "
                  "l'appel de Florence Bérubé deux fois avant d'ouvrir quoi que ce "
                  "soit : la première pour la situation, la seconde pour la liste. "
                  "Beaucoup d'élèves n'ont jamais vu de crampons — en apporter une "
                  "paire si l'école en a, l'objet vaut dix minutes d'explication.")

    d.objectifs([
        "suivre un appel où quelqu'un demande quoi apporter ;",
        "nommer l'équipement du grand froid et celui de la chaleur ;",
        "lire les deux chiffres du froid : le thermomètre et le vent ;",
        "reconnaître à quel avertissement répond une consigne.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qui manque à cette personne ?",
        image=img('crampons-botte.jpg'),
        pistes=[
            "Qu'est-ce qui est attaché sous cette botte ?",
            "À quoi ça sert, exactement ?",
            "Est-ce que vous en avez déjà vu ? Déjà porté ?",
            "Qu'est-ce que vous mettez, vous, sur un trottoir gelé ?",
        ],
        notes="Laisser parler dix minutes. Les réponses viennent de partout — sable, "
              "petits pas, éviter de sortir — et elles sont toutes bonnes. Le mot "
              "« crampons » s'installe ensuite tout seul.")

    d.dialogue('Dialogue · 1 de 4', "J'appelle pour la sortie du vingt-deux", [
        ("FLORENCE", "Bonjour Marisol, c'est Florence Bérubé. Qu'est-ce que je dois apporter ?", True),
        ("MARISOL", "Bonjour madame Bérubé. Des bottes avec une bonne semelle, et si vous en avez, des crampons.", True),
        ("FLORENCE", "Des crampons ? Comme les grimpeurs de montagne ?", True),
        ("MARISOL", "Des petits, ceux qui s'attachent par-dessus la botte. Ça change tout sur un trottoir gelé.", True),
    ], consigne="Écoutez deux fois avant de lire le texte.",
       notes="Faire remarquer la question de Florence : elle ne fait pas semblant de "
             "comprendre. C'est exactement ce que le module demande aux élèves de "
             "savoir faire, et c'est une personne âgée qui le montre.")

    d.dialogue('Dialogue · 2 de 4', "Trois couches, et pourquoi", [
        ("MARISOL", "Habillez-vous en trois couches plutôt qu'avec un gros manteau.", True),
        ("FLORENCE", "Pourquoi trois ?", True),
        ("MARISOL", "Parce qu'on marche une heure et qu'on entre au café ensuite.", True),
        ("MARISOL", "En enlevant une couche à l'intérieur, vous ne transpirez pas ; en la remettant dehors, vous n'attrapez pas froid.", True),
    ], notes="La dernière réplique porte les deux gérondifs du Défi 3. Ne pas les "
             "nommer aujourd'hui : les faire seulement entendre. Ils seront le sujet "
             "de la séance D2.")

    d.dialogue('Dialogue · 3 de 4', "C'est le vent qui décide", [
        ("FLORENCE", "Et le vent ? À la promenade de la mer, il y a toujours du vent.", True),
        ("MARISOL", "Le bulletin annonce moins douze avec un refroidissement éolien de moins vingt-deux.", True),
        ("MARISOL", "C'est le vent qui décide, pas le thermomètre. Couvrez-vous le visage.", True),
        ("FLORENCE", "Moins vingt-deux. Et l'été, en juillet, vous nous aviez dit le contraire.", True),
    ], notes="Écrire les deux chiffres au tableau, l'un sous l'autre : moins 12, moins "
             "22. Demander lequel gèle les doigts. La réponse est le second, toujours.")

    d.dialogue('Dialogue · 4 de 4', "En juillet, c'était l'inverse", [
        ("MARISOL", "En juillet, il y avait un avertissement de chaleur extrême et un indice UV de neuf.", True),
        ("MARISOL", "Ce jour-là, on est partis à neuf heures du matin en apportant deux litres d'eau chacun.", True),
        ("FLORENCE", "Deux litres, j'avais trouvé ça exagéré. J'ai tout bu.", True),
        ("MARISOL", "Tout le monde a tout bu. On boit avant d'avoir soif, on marche à l'ombre, on s'arrête vingt minutes au milieu.", True),
    ], notes="La réplique de Florence est celle qui reste : elle avait trouvé la "
             "consigne exagérée, et elle a tout bu. Le faire dire au groupe — c'est "
             "l'argument qui convainc mieux que n'importe quelle explication.")

    d.regle("La soif arrive trop tard",
            "On boit toutes les vingt minutes, même sans avoir soif.",
            precision="La soif se déclenche après le début de la déshydratation, pas "
                      "avant. C'est pour cela que la consigne n'est jamais « buvez "
                      "quand vous avez soif ». C'est ainsi qu'on évite un coup de "
                      "chaleur.",
            notes="Diapositive à photographier. Le rappeler chaque fois qu'une sortie "
                  "d'été est planifiée, y compris hors de ce module.")

    d.tableau('Analyse', "Deux avertissements, deux listes",
              ["Ce qu'on apporte", "Contre quoi"],
              [["Bottes, crampons, trois couches", "le froid extrême"],
               ["Tuque, foulard, mitaines, de quoi couvrir le visage", "le vent"],
               ["Deux litres d'eau, chapeau, crème solaire", "la chaleur extrême"],
               ["Des vêtements légers et pâles", "l'indice UV"]],
              cle=1,
              note="Dans les deux cas, on change l'heure de la sortie plutôt que de "
                   "l'annuler.",
              notes="Diapositive à photographier. La note du bas est la vraie leçon du "
                    "Défi 3 : l'équipement et l'heure permettent de maintenir presque "
                    "toutes les activités.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Réécoutez l'appel de madame Bérubé, puis répondez.", [
        ("Marisol conseille des crampons qui s'attachent par-dessus la botte.", "vrai"),
        ("Elle recommande un seul gros manteau plutôt que plusieurs couches.", "faux — trois couches"),
        ("Le refroidissement éolien annoncé est de moins vingt-deux.", "vrai"),
        ("En juillet, le groupe était parti à quatorze heures.", "faux — à neuf heures"),
        ("L'indice UV était de neuf lors de la sortie de juillet.", "vrai"),
        ("On évite un coup de chaleur en buvant seulement quand on a soif.", "faux — avant d'avoir soif"),
    ], corrige=True,
       notes="Six des huit énoncés de l'exercice `t3a`. Les faire d'abord sans le "
             "texte du dialogue sous les yeux : c'est de la compréhension orale, pas "
             "de la lecture.")

    d.pratique('Écoute et réponds', "Froid ou chaleur ?",
               "Pour chaque consigne, dites à quel avertissement elle répond.", [
        ("Attachez vos crampons avant de sortir du Centre.", "froid"),
        ("Apportez deux litres d'eau par personne.", "chaleur"),
        ("Habillez-vous en trois couches plutôt qu'avec un gros manteau.", "froid"),
        ("Nous partirons à neuf heures et nous serons rentrés avant midi.", "chaleur"),
        ("Couvrez-vous le visage : le vent est plus mordant que le thermomètre.", "froid"),
        ("Mettez de la crème solaire et un chapeau à large bord.", "chaleur"),
    ], corrige=True, cols=2,
       notes="Six des huit items de `t3equip`. Les deux qui restent — rentrer se "
             "réchauffer toutes les vingt minutes, marcher du côté ombragé — sont "
             "ceux qui se ressemblent le plus : les garder pour l'activité en ligne.")

    d.billet(
        "Écrivez trois choses que vous apporteriez à une marche d'une heure, en février, à Rimouski.",
        exemples=[
            "Trois objets, et pour chacun une raison en trois mots.",
            "Si vous n'avez jamais marché par moins vingt, écrivez ce que vous croyez : on comparera.",
        ],
        notes="Devoir court. Le comparer en D2 avec la liste du dialogue : l'écart est "
              "presque toujours les crampons et la couverture du visage.")

    return d.save(dossier)
