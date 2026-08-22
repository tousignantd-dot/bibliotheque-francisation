# -*- coding: utf-8 -*-
"""B4 · C'était déjà là, et ce n'est pas moi qui le fais
Bloc B « Défi 1 · Le diagnostic » · couleur ambre · 75 min.
Source : exercices `t1pqp` et `t1faire`, et leurs mini-leçons. Savoirs du
programme : comprendre que le plus-que-parfait désigne une action précédant
une autre action passée ; employer faire + infinitif avec par, et laisser +
infinitif.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="C'était déjà là, et ce n'est pas moi qui le fais",
        chapeau="Deux tournures que l'entrepreneur emploie sans arrêt : "
                "l'une place un fait avant l'achat de la maison, l'autre dit "
                "qui pose les mains sur l'ouvrage.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc B, et elle en porte deux points. Prévoir "
                  "quarante minutes pour le plus-que-parfait, trente pour le faire "
                  "causatif : le second va plus vite parce que le titre du module "
                  "l'a déjà installé.")

    d.objectifs([
        "former le plus-que-parfait avec l'auxiliaire à l'imparfait ;",
        "dire lequel de deux faits passés est arrivé en premier ;",
        "employer « faire » + infinitif, et dire par qui avec « par » ;",
        "distinguer « faire sécher » de « laisser sécher ».",
    ], notes="Le quatrième objectif a une conséquence concrète : « faire sécher » se "
             "facture, « laisser sécher » ne se facture pas. Le dire ainsi.")

    d.declencheur(
        'Observation', "« Quand vous avez acheté, la fissure s'était déjà ouverte. » Que dit cette phrase ?",
        pistes=[
            "Quels sont les deux moments de la phrase ?",
            "Lequel est arrivé en premier ?",
            "Est-ce que ça change quelque chose pour Doïna et Marius ?",
        ],
        notes="La troisième question est la plus intéressante : oui, ça change tout. "
              "Un défaut antérieur à l'achat n'engage pas les mêmes personnes. Ne "
              "pas aller plus loin sur le plan juridique : le module ne le fait pas.")

    d.tableau('Analyse', "Le plus-que-parfait : le passé du passé",
              ['Sa forme', 'Un exemple'],
              [["avoir à l'imparfait", "l'inspectrice l'avait noté"],
               ["être à l'imparfait", "elle était venue en septembre"],
               ["verbe pronominal", "la terre s'était tassée"],
               ["à la forme négative", "le plan n'était pas parti"]],
              cle=0,
              note="Le mot « déjà » l'accompagne presque toujours : c'est le meilleur repère à l'écoute.",
              notes="Diapositive à photographier. Le choix de l'auxiliaire est le même "
                    "qu'au passé composé, et les accords aussi : le dire, ça évite "
                    "vingt minutes de questions.")

    d.tableau('Analyse', "Deux moments dans la même phrase",
              ['Le second', 'Le premier'],
              [["ils ont acheté", "la fissure s'était ouverte"],
               ["il a trouvé vite", "l'inspectrice l'avait noté"],
               ["on a ouvert", "quelqu'un avait condamné le puisard"],
               ["elle a compris", "elle avait relu le rapport"]],
              cle=1,
              note="Le plus-que-parfait occupe toujours le moment le plus ancien.",
              notes="Diapositive à photographier. C'est l'exercice réel du bloc : "
                    "refaire la ligne du temps à partir de la phrase.")

    d.regle("L'ordre des mots n'est pas l'ordre des choses",
            "Ce qui est écrit en second est souvent arrivé en premier.",
            precision="Un diagnostic remonte le temps. Il part d'aujourd'hui — « le "
                      "mur est fendu » —, puis recule d'un cran — « elle était déjà "
                      "là quand vous avez acheté » —, puis d'un autre — « quelqu'un "
                      "avait condamné le puisard avant vous ». Chaque recul demande "
                      "un temps de verbe différent.",
            notes="Diapositive à photographier. Faire le lien avec B2 : le diagnostic "
                  "remonte à la cause, et la grammaire suit ce mouvement.")

    d.pratique('Pratique', "Mettre au plus-que-parfait",
               "Complétez avec le verbe entre parenthèses.", [
        ("Quand ils ont acheté, la fissure ___ (s'ouvrir) depuis des années.", "s'était ouverte"),
        ("Le sol poussait parce que la terre ___ (se tasser).", "s'était tassée"),
        ("Quand on a ouvert, quelqu'un ___ (condamner) le puisard.", "avait condamné"),
        ("En 1961, personne ___ (ne pas poser) de membrane.", "n'avait posé"),
        ("Elle a compris, parce qu'elle ___ (relire) le rapport.", "avait relu"),
        ("Léandre savait : lui aussi ___ (faire) aménager son sous-sol.", "avait fait"),
    ], corrige=True,
       notes="La dernière contient déjà un « avait fait » causatif : l'employer comme "
             "transition vers la seconde moitié de la séance.")

    d.tableau('Analyse', "Faire faire, ou laisser faire",
              ['La tournure', 'Ce qu\'elle dit'],
              [["faire + infinitif", "un autre exécute : je fais injecter la fissure"],
               ["avec « par »", "on dit qui : injecter par un sous-traitant"],
               ["laisser + infinitif", "personne n'agit : on laisse sécher"],
               ["le participe « fait »", "invariable devant un infinitif"]],
              cle=0,
              note="« Faire sécher » se facture, « laisser sécher » ne se facture pas.",
              notes="Diapositive à photographier. La note est la raison pour laquelle "
                    "ce point de grammaire est dans le module et non ailleurs : sur "
                    "une soumission, les deux phrases n'ont pas le même prix.")

    d.pratique('Pratique', "Fais faire, ou laisse faire ?",
               "Complétez avec « fais », « fait », « laisse » ou « laissé ».", [
        ("Je ne pose pas le béton : je ___ injecter la fissure par un spécialiste.", "fais"),
        ("Après l'injection, on ___ sécher trois ou quatre semaines.", "laisse"),
        ("Fernand a ___ refaire la pente par son sous-traitant.", "fait"),
        ("Doïna n'a pas ___ Marius toucher au panneau électrique.", "laissé"),
        ("Ne ___ pas la gouttière se vider au pied du mur.", "laissez"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la question « qui pose les mains "
             "dessus ? ». Le quatrième fait sourire, et il est juste : elle a "
             "empêché, donc « laisser » à la forme négative.")

    d.billet(
        "Écris une chose que tu fais faire, et une chose que tu laisses faire.",
        exemples=[
            "Chez toi, au travail, ou dans ta famille.",
            "Emploie « par » pour dire qui.",
        ],
        notes="Trois minutes. Fin du bloc B. Annoncer le bloc C : à partir de la "
              "prochaine séance, on quitte la parole et on entre dans les papiers — "
              "un rapport de onze pages et une soumission de deux.")

    return d.save(dossier)
