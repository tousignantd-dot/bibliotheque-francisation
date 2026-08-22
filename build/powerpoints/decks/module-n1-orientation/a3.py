# -*- coding: utf-8 -*-
"""A3 · MAJUSCULES et minuscules.
Bloc A « Je découvre » · couleur teal · 60 min. Dernière séance du bloc A.
Source : exercices `prMaj` et `prVocab`, mini-leçon `prMaj`, cartes mémoire.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre='MAJUSCULES et minuscules',
        chapeau="Les panneaux écrivent en grandes lettres, les cahiers en "
                "petites. C'est le même mot — encore faut-il le savoir.",
        duree='60 minutes')

    d.titre(notes="Séance charnière du bloc A. Sans elle, un élève qui connaît "
                  "« sortie » ne reconnaît pas « SORTIE » et croit avoir affaire à un "
                  "mot nouveau. C'est une cause d'échec très fréquente et très "
                  "silencieuse.")

    d.objectifs([
        "reconnaître le même mot en grandes et en petites lettres ;",
        "recopier en minuscules un mot lu en majuscules ;",
        "nommer quatre lieux du centre ;",
        "comprendre les mots « majuscule » et « minuscule ».",
    ])

    d.declencheur(
        'Observation', "Est-ce le même mot ?",
        pistes=[
            "SORTIE — sortie",
            "TOILETTES — toilettes",
            "ACCUEIL — accueil",
            "Qu'est-ce qui change ? Qu'est-ce qui ne change pas ?",
        ],
        notes="Écrire les trois paires au tableau avant la séance. Laisser chercher "
              "deux ou trois minutes : plusieurs répondront que ce sont des mots "
              "différents. C'est exactement le point de la séance.")

    d.regle("C'est le même mot",
            "La lettre change de taille, pas de son.",
            precision="La grande s'appelle une <b>majuscule</b>, la petite une "
                      "<b>minuscule</b>. Les panneaux prennent les grandes, pour "
                      "qu'on les voie de loin. Les cahiers et les livres prennent "
                      "les petites.",
            notes="Diapositive à photographier. C'est la règle de la séance.")

    d.tableau('Analyse', "Des paires plus ou moins faciles",
              ['La difficulté', 'Les lettres'],
              [["presque pareilles", "C et c · S et s · O et o"],
               ["un peu différentes", "E et e · A et a"],
               ["très différentes", "G et g · R et r · D et d"]],
              cle=1,
              note="Les trois dernières demandent du temps. Ce n'est pas vous.",
              notes="Diapositive à photographier. Faire écrire les trois paires "
                    "difficiles au cahier, grande puis petite, cinq fois chacune.")

    d.pratique('Pratique', "Écrivez le mot en minuscules",
               "Le mot est écrit en majuscules. Recopiez-le en petites lettres.", [
        ("SORTIE", "sortie"),
        ("ENTRÉE", "entrée"),
        ("TOILETTES", "toilettes"),
        ("ACCUEIL", "accueil"),
        ("POUSSEZ", "poussez"),
        ("CAFÉTÉRIA", "cafétéria"),
    ], corrige=True, cols=2,
       notes="Vingt minutes, au cahier, en lettres détachées. Circuler et regarder la "
             "tenue du crayon autant que le résultat.")

    d.vocabulaire('Vocabulaire', "Les quatre premiers lieux",
                  [("les toilettes", "un dessin d'homme ou de femme sur la porte"),
                   ("la cafétéria", "un dessin de fourchette ; des tables, pour le dîner"),
                   ("l'accueil", "après la porte, quelqu'un répond aux questions"),
                   ("la sortie", "un dessin vert : quelqu'un qui court")],
                  notes="Faire répéter chaque mot avec son petit mot — le, la, les. "
                        "L'article fait partie du mot, on ne l'apprend jamais après.")

    d.piege("Chercher l'accent sur la grande lettre",
            "ENTREE, sans accent, sur le panneau.",
            "entrée, avec l'accent, dans le cahier.",
            "Beaucoup de panneaux au Québec n'accentuent pas les majuscules. Le mot "
            "reste le même et se dit pareil ; l'accent revient dès qu'on écrit en "
            "petites lettres. Ne pas laisser croire à une faute de leur part.",
            notes="Le signaler en passant, sans en faire une règle : ils le "
                  "rencontreront le jour même dans le corridor.")

    d.pratique('Pratique · à deux', "Le mot et le lieu",
               "Deux par deux. Un montre un mot, l'autre montre l'endroit.", [
        ("Étape 1", "Écrivez les quatre mots en grandes lettres sur une feuille."),
        ("Étape 2", "Allez les poser sur les bonnes portes, avec l'enseignante."),
        ("Étape 3", "Revenez, effacez, recommencez en petites lettres."),
    ], cols=1,
       notes="Quinze minutes. L'aller-retour entre le papier et la vraie porte est "
             "ce qui fait tenir le mot.")

    d.billet(
        "Recopiez en petites lettres : TOILETTES, SORTIE, ACCUEIL.",
        exemples=[
            "En lettres détachées, bien lisibles.",
            "Ajoutez le petit mot devant : les, la, l'.",
        ],
        notes="Deux minutes. Ce billet sert de brouillon à la production écrite de E1.")

    return d.save(dossier)
