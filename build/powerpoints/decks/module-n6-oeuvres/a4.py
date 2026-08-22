# -*- coding: utf-8 -*-
"""A4 · Ce que chaque texte donne, et ce qu'il ne donne pas
Bloc A « Je découvre » · couleur ambre · 75 min. Bilan du bloc.
Source : exercices `prGenres` et `prImg`, mini-leçon « Savoir d'avance ce
qu'un texte va donner ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Ce que chaque texte donne, et ce qu'il ne donne pas",
        chapeau="On perd beaucoup de temps à chercher dans un texte ce qu'il "
                "ne contient pas : une opinion dans une biographie, une fin "
                "dans un résumé, une histoire dans une bande-annonce.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. Elle referme le tableau ouvert en A1 et "
                  "prépare le Défi 1. Commencer par relire les billets de A1 : ils "
                  "disent quel texte intimide le groupe.")

    d.objectifs([
        "reconnaître un texte à sa forme, en trois secondes ;",
        "dire ce qu'on va y chercher avant de commencer à lire ;",
        "nommer ce qu'aucun de ces textes ne donne ;",
        "situer les lieux du dossier : la salle, le quai, la maison, le journal.",
    ], notes="Le troisième objectif est le plus important et le plus vite oublié : "
             "aucun texte ne remplace le film.")

    d.declencheur(
        'Observation', "D'où vient chacune de ces phrases ?",
        pistes=[
            "« Elle croyait n'avoir que des boîtes à faire. »",
            "« Elle entra dans une salle de montage en 1972. »",
            "« Mon vrai reproche est ailleurs. »",
            "« Montage : Aurélie Pichette. »",
        ],
        notes="Les quatre phrases se reconnaissent à leur forme seule, sans contexte. "
              "Faire justifier chaque réponse : c'est l'exercice réel de la séance.")

    d.tableau('Analyse', "Reconnaître un texte à sa forme",
              ['Ce que tu vois', 'Ce que c\'est'],
              [["une voix, pas de fin", "une bande-annonce"],
               ["des dates, du passé simple", "une biographie"],
               ["quelqu'un dit « je »", "une critique"],
               ["l'histoire, sans jugement", "un résumé"],
               ["une liste de noms", "un générique"]],
              cle=0,
              note="Trois secondes suffisent, et elles font gagner dix minutes de lecture.",
              notes="Diapositive à photographier. C'est le tableau de A1 retourné : "
                    "là-bas on partait du genre, ici on part de l'indice.")

    d.regle("Ce qu'aucun texte ne donne",
            "Le déroulement complet n'est nulle part ailleurs que dans le film.",
            precision="Le résumé s'arrête avant le dénouement. La critique le tait par "
                      "politesse. La bande-annonce ment un peu par le ton. Et aucun "
                      "des trois ne vous dira ce que vous, vous en penserez. C'est "
                      "pour cela qu'un ciné-club projette avant de discuter, et "
                      "jamais l'inverse.",
            notes="Diapositive à photographier. Faire le lien avec le Défi 1, qui "
                  "commence la semaine prochaine : on va enfin regarder le film.")

    d.pratique('Compréhension', "Quel texte, et pourquoi ?",
               "Nommez le texte, puis dites à quoi vous l'avez reconnu.", [
        ("Deux minutes, une voix hors champ, aucune fin.", "la bande-annonce"),
        ("Des dates, un parcours, aucune opinion.", "la biographie"),
        ("Un avis signé, publié après la sortie.", "la critique"),
        ("L'histoire en deux paragraphes, sans le dénouement.", "le résumé"),
        ("Qui a fait le montage, qui a fait la musique.", "le générique"),
        ("L'ordre exact de tout ce qui arrive.", "le film - et rien d'autre"),
    ], corrige=True,
       notes="Le dernier item est le seul dont la réponse n'est pas un texte. Le "
             "garder pour la fin et le laisser tomber sans commentaire : il se "
             "retient tout seul.")

    d.cartes("Les lieux du dossier", "Où se passe le module", [
        ("La salle Beauchemin",
         "une petite salle de projection de quartier, à Sherbrooke, le mercredi soir."),
        ("La maison au bord de l'eau",
         "celle qu'Estelle vient vider en trois jours, dans le film."),
        ("Le quai du village",
         "l'endroit des retours en arrière, en novembre 1978."),
        ("L'Écho de la Magog",
         "l'hebdomadaire local, où paraît la critique et où l'on écrira."),
    ], notes="Ces quatre lieux sont ceux des photos de l'exercice 5. Les nommer "
             "maintenant évite de perdre du temps à les situer dans les blocs "
             "suivants.")

    d.piege("Chercher dans un texte ce qu'il ne contient pas",
            "Je lis la biographie pour savoir ce que raconte le film.",
            "Je lis le résumé pour savoir ce que raconte le film.",
            "C'est la perte de temps la plus fréquente, et elle décourage : on lit dix "
            "lignes difficiles, on ne trouve rien, et on conclut qu'on n'a pas "
            "compris. Alors qu'on a très bien compris — simplement, la réponse "
            "n'était pas là.",
            notes="Faire raconter une expérience de ce genre. Presque tous les élèves "
                  "en ont une, avec un formulaire ou une lettre officielle.")

    d.billet(
        "Avant le film de la semaine prochaine, qu'est-ce que tu vas chercher ?",
        exemples=[
            "Une phrase suffit.",
            "Pense au tableau des trois secondes.",
        ],
        notes="Deux minutes. Ces billets se relisent en B1, juste avant la "
              "bande-annonce : ils montrent au groupe qu'il savait déjà quoi "
              "chercher.")

    return d.save(dossier)
