# -*- coding: utf-8 -*-
"""B2 · Le même indice, deux lectures
Bloc B « Défi 1 · La dernière scène » · couleur teal · 75 min.
Source : exercices `t1deux` et `t1img`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n8-oeuvres' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='B2', section='teal',
        titre="Le même indice, deux lectures",
        chapeau="Six indices, deux histoires. Chacune en explique trois ou "
                "quatre, aucune ne les explique tous — et deux d'entre eux "
                "servent aux deux à la fois.",
        duree='75 minutes')

    d.titre(notes="Séance de méthode, la plus importante du bloc B. On y apprend à "
                  "mesurer une lecture au lieu de la défendre plus fort.")

    d.objectifs([
        "compter les indices dont une lecture rend compte ;",
        "retourner un indice au lieu de le passer sous silence ;",
        "accepter qu'un détail appuie deux lectures à la fois ;",
        "céder devant une lecture qui explique davantage.",
    ], notes="Le quatrième objectif est le plus étranger au groupe : céder n'est pas "
             "perdre. Le formuler ainsi — on ne perd rien, on gagne une scène.")

    d.declencheur(
        'Observation', "Cette chaloupe est-elle prête à partir ?",
        image=IMG + 'chaloupe-retournee.jpg',
        pistes=[
            "Que faudrait-il faire avant de l'utiliser ?",
            "Combien de gestes, exactement ?",
            "Lequel de ces gestes Estelle a-t-elle faits ?",
            "Lequel n'a-t-elle pas fait ?",
        ],
        notes="La quatrième piste amène la corde sans qu'on la nomme. Ne pas la donner "
              "vous-même : le groupe la trouve en trente secondes et s'en souvient "
              "beaucoup mieux.")

    d.tableau('Analyse', "Deux lectures, et ce qu'elles expliquent",
              ['L\'indice', 'Ce qu\'il appuie'],
              [["Le téléphone laissé sonner", "elle choisit"],
               ["Les bottes de ville enlevées", "elle choisit"],
               ["La chaloupe remise à l'eau", "elle choisit"],
               ["La corde restée attachée", "elle est prise"],
               ["Six épisodes de promesses", "elle est prise"],
               ["Les bottes de la mère", "les deux"]],
              cle=1,
              notes="Diapositive à photographier. Trois contre deux, et un partagé : "
                    "aucune lecture ne prend tout. Faire remarquer la dernière "
                    "ligne — c'est elle qui rend la scène intéressante, pas les cinq "
                    "autres.")

    d.regle("Une lecture se mesure",
            "Mettez les indices en colonne et cochez ceux dont votre lecture "
            "rend compte. Le résultat est un nombre.",
            precision="Une lecture qui couvre huit indices sur dix bat une lecture qui "
                      "en couvre quatre, même dite plus fort et même défendue plus "
                      "longtemps. C'est le seul critère mesurable de la discussion, "
                      "et il met tout le monde à égalité.",
            notes="Diapositive à photographier. Le mot « mesure » compte : on quitte "
                  "l'impression pour le décompte, et c'est ce qui rend un cercle de "
                  "lecture praticable avec dix-huit adultes.")

    d.cartes('Analyse', "Un indice, deux façons de le lire", [
        ("Le téléphone : lecture A", "elle le porte au quai pour pouvoir le laisser"),
        ("Le téléphone : lecture B", "elle le laisse sonner : plus rien à dire"),
        ("La corde : lecture A", "ce n'est pas ce qui la retient, c'est ce qu'elle laisse"),
        ("La corde : lecture B", "une chaloupe attachée n'emmène personne"),
        ("Les bottes : lecture A", "elle enlève celles de ville : elle s'installe"),
        ("Les bottes : lecture B", "elle finit dans celles de sa mère, comme sa mère"),
    ], notes="Six cases, trois indices. Aucune des six n'est fausse : c'est ce qui "
             "déroute au début, et ce qu'il faut installer. Faire lire les six à voix "
             "haute par six personnes différentes.")

    d.piege('Piège', "passer sous silence l'indice qui gêne",
            "le sortir soi-même, et le retourner",
            "Un indice évité se voit toujours : votre interlocuteur l'a remarqué "
            "avant vous, et votre silence le lui confirme. Le sortir soi-même "
            "coûte dix secondes et change tout — on le garde intégralement comme "
            "fait, et on discute seulement de ce qu'il veut dire. C'est ce que "
            "fait Fatoumata avec la corde en D1, et c'est le geste le plus fort "
            "d'une discussion.",
            notes="Exemple à donner tel quel : « la corde n'est pas ce qui la retient, "
                  "c'est ce qu'elle laisse en place ». Le faire répéter.")

    d.pratique('Pratique', "Quelle lecture cet indice appuie-t-il ?",
               "Elle choisit, elle est prise, ou les deux ?", [
        ("Elle laisse le téléphone sonner sur le quai.", "elle choisit"),
        ("La corde reste attachée au taquet.", "elle est prise"),
        ("C'est elle qui remet la chaloupe à l'eau.", "elle choisit"),
        ("Elle enfile les bottes de sa mère.", "les deux"),
        ("Elle promet de partir depuis six épisodes.", "elle est prise"),
        ("La lampe du quai s'allume toute seule.", "les deux"),
    ], corrige=True,
       notes="Exercice `t1deux` du module. Accepter la discussion sur les deux "
             "dernières : elles sont volontairement ambiguës, et c'est le sujet.")

    d.pratique('Pratique', "Les objets de la scène",
               "Reliez la photo à la phrase qui la décrit.", [
        ("Un quai de bois, la nuit, une lampe allumée au bout.", "le quai"),
        ("Une chaloupe retournée sur la berge, la coque en l'air.", "la chaloupe"),
        ("Des bottes de caoutchouc à côté de bottes de ville.", "les bottes"),
        ("Une corde enroulée en huit autour d'un taquet.", "la corde"),
        ("Une cuisine de chalet, une lampe allumée, personne.", "le chalet"),
        ("Un chemin de terre, l'auto stationnée au bout.", "le chemin"),
    ], corrige=True,
       notes="Exercice `t1img` du module. À faire à l'écran plutôt qu'ici si la "
              "classe a des postes : le glisser-déposer vaut mieux que la lecture.")

    d.billet(
        "Reprenez l'œuvre de votre billet d'A1. Écrivez deux indices qui "
        "appuient votre lecture, et un qui la gêne.",
        exemples=[
            "Un indice est un détail qu'on peut montrer, pas une impression.",
            "Le troisième est le plus important : ne le choisissez pas trop facile.",
        ],
        notes="Ce billet prépare directement D1 et E1. Les copies qui ne trouvent "
              "aucun indice gênant sont celles dont la lecture n'est pas encore une "
              "lecture ; leur redemander une fois.")

    return d.save(dossier)
