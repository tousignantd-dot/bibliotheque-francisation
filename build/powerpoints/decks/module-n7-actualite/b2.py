# -*- coding: utf-8 -*-
"""B2 · Deuxième écoute : les chiffres exacts
Bloc B « Défi 1 · Le reportage » · couleur teal · 75 min.
Source : extrait `t1`, exercices `t1detail` et `t1source`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n7-actualite/images/')


def build(dossier):
    d = Deck(
        code='B2', section='teal',
        titre="Deuxième écoute : les chiffres exacts",
        chapeau="Cette fois, on a le droit d'arrêter et de revenir en "
                "arrière. Un chiffre mal entendu, ce n'est pas un détail : "
                "c'est ce qui change une nouvelle en rumeur.",
        duree='75 minutes')

    d.titre(notes="Deuxième séance du Défi 1. Le groupe a déjà le sujet en tête ; il "
                  "peut donc écouter pour autre chose. Rappeler la méthode des trois "
                  "écoutes, affichée en B1.")

    d.objectifs([
        "relever les chiffres et les dates d'un reportage long ;",
        "attribuer chaque parole à la personne qui l'a dite ;",
        "distinguer une source nommée d'une source anonyme ;",
        "citer un fait vérifié du dossier de la consigne.",
    ], notes="Le troisième objectif prépare tout le bloc C : « la Ville indique » n'est "
             "pas la même chose que « la conseillère Ferron déclare ».")

    d.declencheur(
        'Observation', "Que rapporte-t-on, et combien ça vaut ?",
        image=IMG + 'contenants-sac.jpg',
        pistes=[
            "Rapportez-vous vos contenants vides ?",
            "Savez-vous combien vous récupérez par contenant ?",
            "Où allez-vous les porter ?",
            "Est-ce que c'était pareil dans votre pays ?",
        ],
        notes="Beaucoup d'élèves paient la consigne sans savoir qu'ils peuvent la "
              "récupérer. La séance a donc une utilité immédiate, indépendamment de la "
              "langue.")

    d.tableau('Analyse', "La consigne au Québec : les faits vérifiés",
              ['La date', 'Ce qui change'],
              [["1er novembre 2023", "dix cents sur les contenants visés ; vingt-cinq cents sur le verre de 500 ml et plus"],
               ["1er mars 2025", "les contenants de plastique deviennent consignés"],
               ["mars 2027", "le verre et les contenants multicouches s'ajouteront"],
               ["14 octobre", "le conseil municipal doit se prononcer sur l'emplacement"]],
              cle=0,
              note="Les trois premières lignes sont vérifiées sur les sites officiels. La quatrième appartient au scénario du module.",
              notes="Distinction importante à dire au groupe : ce qui concerne la "
                    "consigne est réel et vérifiable ; le quartier du Ruisseau, lui, est "
                    "inventé pour les besoins du cours. Un élève doit savoir ce qu'il "
                    "peut répéter à l'extérieur.")

    d.regle("Écouter pour un chiffre",
            "On n'entend un chiffre que si on l'attend.",
            precision="À la deuxième écoute, on sait de quoi parle le reportage : on "
                      "peut donc décider d'avance ce qu'on cherche. Combien de cents ? "
                      "Quelle année ? Combien de places ? L'oreille trouve ce qu'elle "
                      "cherche et laisse passer le reste - et c'est très bien ainsi.",
            notes="Diapositive à photographier. Faire écrire les quatre questions avant "
                  "de lancer l'extrait.")

    d.pratique('Relevé', "Deuxième écoute : les chiffres",
               "Réécoutez, arrêtez, revenez en arrière si nécessaire.", [
        ("La consigne ordinaire est de combien de cents ?", "dix"),
        ("Et sur le verre de 500 ml et plus ?", "vingt-cinq"),
        ("Depuis quand le plastique est-il consigné ?", "mars 2025"),
        ("Quand le verre s'ajoutera-t-il ?", "mars 2027"),
        ("À quelle distance est le point de dépôt le plus proche ?", "trois kilomètres"),
        ("Combien de places devant le dépanneur ?", "huit"),
        ("Depuis combien d'années Marjolaine habite-t-elle l'immeuble ?", "vingt-six"),
        ("Quelle est la date de la séance du conseil ?", "le 14 octobre"),
    ], corrige=True,
       notes="Corrigé masqué au premier passage. Autoriser franchement les arrêts et "
             "les retours : c'est la consigne de la deuxième écoute, pas une triche.")

    d.tableau('Analyse', "Qui dit quoi, et à quel titre",
              ['La parole', 'Qui la dit'],
              [["« Le dossier est à l'étude. »", "Hélène Ferron, conseillère - une élue nommée"],
               ["« Ça fait onze ans que je reprends les canettes. »", "Benoît Sarrazin, dépanneur - un témoin nommé"],
               ["« Moi, je n'ai pas d'auto. »", "Marjolaine Cusson, résidente - un témoin nommé"],
               ["« Un dépôt de cette taille serait ouvert six jours sur sept. »", "la Ville - aucune personne nommée"]],
              cle=0,
              note="La dernière ligne est la seule sans visage. Retenez-la : elle revient au Défi 2.",
              notes="Diapositive à photographier. Demander pourquoi une institution "
                    "parle parfois sans nommer personne. Les réponses des élèves valent "
                    "mieux que l'explication.")

    d.piege("Confondre un témoin et un porte-parole",
            "Le dépanneur a dit que la Ville allait tout payer.",
            "Le dépanneur a dit qu'il craignait de perdre ses places.",
            "Un témoin parle de ce qu'il vit ; un porte-parole parle au nom d'un "
            "organisme, et engage cet organisme. Prêter à l'un l'autorité de l'autre "
            "est la façon la plus courante de transformer un reportage exact en rumeur "
            "fausse, sans que personne ait menti.",
            notes="Ce piège prépare directement le jeu de rôle de E1, où le voisin "
                  "sceptique fait exactement cette confusion.")

    d.billet(
        "Écrivez un chiffre du reportage et dites qui l'a donné.",
        exemples=[
            "Par exemple : dix cents - c'est le journaliste qui le rappelle.",
            "Si vous ne savez plus qui l'a dit, écrivez-le aussi.",
        ],
        notes="Deux minutes. Les « je ne sais plus » sont utiles : ils montrent quelles "
              "voix se confondent encore.")

    return d.save(dossier)
