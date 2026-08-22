# -*- coding: utf-8 -*-
"""D2 · Les petits mots qui tiennent les idées ensemble
Bloc D « Défi 3 » · couleur teal · écoute et réponds · 75 min.
Source : exercices `t3conn` (cols:1), `t3ponct` et `t3plan` et leurs
mini-leçons — les connecteurs, le tiret et les guillemets, et le plan d'un
courriel qui informe du contenu d'un article.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='teal',
        titre="Les petits mots qui tiennent les idées ensemble",
        chapeau="Un connecteur annonce ce qui s'en vient avant que ça "
                "arrive. Celui qui les lit avance plus vite et se trompe "
                "moins.",
        duree='75 minutes')

    d.titre(notes="Dernière séance avant les productions. Elle rassemble les trois "
                  "derniers savoirs du module : les connecteurs, la ponctuation, et le "
                  "plan du courriel qu'on écrira en E2.")

    d.objectifs([
        "reconnaître les quatre familles de connecteurs ;",
        "deviner la suite d'une phrase à partir du connecteur qui l'annonce ;",
        "lire le tiret et les guillemets sans se tromper de sens ;",
        "connaître le plan d'un courriel qui informe du contenu d'un article.",
    ], notes="Le quatrième objectif prépare directement E2. Le dire : ce qu'on voit "
             "aujourd'hui sera la grille de correction de la production écrite.")

    d.declencheur(
        'Observation', "Que va dire la phrase suivante ?",
        pistes=[
            "Le programme est gratuit. Pourtant…",
            "Marisol travaille vendredi. C'est pourquoi…",
            "Elle n'est pas venue, car…",
            "Comment le sais-tu avant même de lire ?",
        ],
        notes="Faire compléter les trois phrases à l'oral. Le groupe y arrive presque "
              "toujours : c'est la démonstration que le connecteur annonce la suite.")

    d.tableau('Analyse', "Quatre familles de connecteurs",
              ['La famille', 'Les mots, et ce qu\'ils annoncent'],
              [["Ajouter", "de plus, d'ailleurs : la suite va dans le même sens"],
               ["Opposer", "pourtant, cependant : la suite va contre"],
               ["Expliquer", "car, parce que, en effet : la suite dit pourquoi"],
               ["Conclure", "donc, c'est pourquoi : la suite est le résultat"],
               ["Situer", "d'abord, ensuite, depuis, au bout de : la suite se place"]],
              cle=0,
              note="Ainsi appartient à deux familles : il conclut et il illustre.",
              notes="Diapositive à photographier. Faire donner un exemple par famille, "
                    "tiré de la vie du groupe plutôt que du module.")

    d.pratique('Grammaire', "Quel connecteur ?",
               "Complétez chaque paire de phrases.", [
        ("Le programme est gratuit. ..., il reste des places.", "Pourtant"),
        ("Marisol travaille vendredi. ... Ghislain ira au terminus.", "C'est pourquoi"),
        ("Elle n'est pas venue, ... elle travaillait de nuit.", "car"),
        ("Les activités sont libres : une marche, un souper, ... une visite au marché.", "par exemple"),
        ("..., on remplit une fiche ; ensuite, on rencontre la coordonnatrice.", "D'abord"),
        ("L'organisme existe ... 1998 et n'a jamais changé de sous-sol.", "depuis"),
    ], corrige=True,
       notes="Faire dire quelle famille avant de donner le mot. C'est la famille qui "
             "compte ; le mot exact peut varier.")

    d.piege('Connecteur', "Il habite ici depuis six mois, donc c'est fini",
            "Il habite ici depuis six mois, donc il y habite encore",
            "Depuis dit qu'une durée continue jusqu'à maintenant. Il y a six mois dit "
            "qu'un fait est terminé. Confondre les deux fait comprendre l'inverse — "
            "et c'est une erreur qui coûte cher dans un formulaire.",
            notes="Faire construire deux phrases avec le même fait, une avec depuis, "
                  "une avec il y a. La différence se voit tout de suite.")

    d.tableau('Ponctuation', "Trois signes qui portent du sens",
              ['Le signe', 'Ce qu\'il apporte'],
              [["Un tiret seul", "il ouvre une liste après une phrase complète"],
               ["Un tiret en tête", "quelqu'un d'autre prend la parole"],
               ["Deux tirets", "ils encadrent une précision qu'on pourrait retirer"],
               ["Guillemets, phrase", "ce sont les mots exacts de quelqu'un"],
               ["Guillemets, un mot", "l'auteur ne prend pas ce mot à son compte"],
               ["Deux virgules", "elles encadrent un groupe qui explique un nom"]],
              cle=0,
              notes="Diapositive à photographier. Six rangées, pas de note. Le "
                    "cinquième emploi est celui qui change le sens d'un article "
                    "entier : le faire chercher dans le texte du Défi 3.")

    d.cartes('Plan', "Le courriel qui informe, en quatre paragraphes", [
        ("1. D'où ça vient",
         "J'ai lu ça dans L'Écho de la Yamaska de cette semaine. Deux phrases, pas plus."),
        ("2. Les faits",
         "Ce que c'est, pour qui, combien de temps, à quel rythme. Trois ou quatre faits choisis, pas dix."),
        ("3. Ton avis, annoncé",
         "À mon avis, pour ma part, je trouve que. Trois mots qui séparent le fait de l'opinion."),
        ("4. Ce qu'on peut faire",
         "Les inscriptions se prennent jusqu'au 30 septembre. Sans cela, le courriel se lit et s'oublie."),
    ], notes="C'est le plan exact de la production écrite de E2. Le faire recopier "
             "dans le cahier ; il servira de grille de vérification.")

    d.regle("Informer n'est pas donner son avis",
            "Celui qui te lit n'a pas lu l'article : tout ce qu'il en saura vient de toi.",
            precision="S'il ne peut plus distinguer ce que le journal a écrit de ce "
                      "que tu en penses, tu ne l'as pas informé : tu lui as donné une "
                      "opinion en la faisant passer pour une nouvelle. Trois mots "
                      "suffisent à séparer les deux.",
            notes="Diapositive à photographier. C'est l'exigence centrale de la "
                  "production écrite, et la seule qui ne se rattrape pas à la "
                  "correction.")

    d.billet(
        "Écris la première phrase de ton courriel à Ousmane.",
        exemples=[
            "Elle doit dire d'où vient l'article.",
            "Une seule phrase.",
        ],
        notes="Deux minutes. Fin du Défi 3 : annoncer les deux séances de production. "
              "Chacun garde son billet, il ouvrira son courriel en E2.")

    return d.save(dossier)
