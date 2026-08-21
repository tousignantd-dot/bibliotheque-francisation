# -*- coding: utf-8 -*-
"""C2 · Le sentier qui, la région que, le village où
Bloc C « Défi 2 » · couleur ambre · 75 min. Écriture et grammaire.
Source : exercice `t2rel` et sa mini-leçon (qui, que, où, dont).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Le sentier qui, la région que, le village où",
        chapeau="Les fiches touristiques sont écrites en longues phrases : "
                "« le sentier qui longe le fleuve », « la région que nous "
                "visitons », « le village où le gîte se trouve ». Sans les "
                "pronoms relatifs, on lit les mots sans lire la phrase.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Le pronom relatif est ce qui sépare une phrase "
                  "de niveau 4 d'une phrase de niveau 5 : c'est lui qui permet le "
                  "discours organisé plutôt que la suite de phrases courtes.")

    d.objectifs([
        "distinguer « qui » et « que » par leur fonction dans la phrase ;",
        "employer « où » pour un lieu et pour un moment ;",
        "comprendre « dont » dans une phrase lue ;",
        "réunir deux phrases courtes en une seule phrase claire.",
    ], notes="Le quatrième objectif est le vrai but : la production. Les trois premiers "
             "sont des moyens. Consacrer la seconde moitié de la séance à réunir des "
             "phrases, pas à identifier des pronoms.")

    d.regle("« Qui » fait l'action, « que » la subit",
            "« Qui » est suivi d'un verbe. « Que » est suivi d'un sujet, "
            "puis d'un verbe.",
            precision="Le sentier qui longe le fleuve — c'est le sentier qui longe. "
                      "Le sentier que j'ai pris — c'est moi qui ai pris.",
            notes="Diapositive à photographier. Le test « qu'est-ce qui vient juste "
                  "après ? » est le plus fiable et le plus rapide : un verbe, c'est "
                  "« qui » ; un sujet, c'est « que ».")

    d.tableau('Quatre pronoms', "Chacun a son emploi",
              ['Le pronom', "Ce qu'il remplace"],
              [["qui", "le sujet du verbe qui suit"],
               ["que", "le complément du verbe qui suit"],
               ["où", "un lieu, ou un moment"],
               ["dont", "un complément introduit par « de »"]],
              cle=1,
              notes="« Dont » est le seul des quatre à ne pas être exigé en production "
                    "au niveau 5 : il suffit de le comprendre en lecture. Le dire au "
                    "groupe, ça soulage.")

    d.cartes("Quatre phrases du module", "Toutes tirées de la fiche du parc", [
        ("Le sentier qui longe le fleuve",
         "C'est le sentier qui longe : « qui » puis un verbe."),
        ("Le sentier que Thuy a pris",
         "C'est Thuy qui a pris : « que » puis un sujet."),
        ("Le village où le gîte se trouve",
         "Un lieu : « où »."),
        ("Le matin où la marée descend",
         "Un moment : « où » aussi."),
    ], notes="La quatrième carte surprend toujours : « où » pour un moment. Donner "
             "d'autres exemples — « l'année où je suis arrivée », « le jour où il a "
             "neigé ». C'est très fréquent et jamais enseigné.")

    d.pratique('Choix', "Complétez avec qui, que ou où",
               "À l'oral, puis à l'écrit.", [
        ("C'est un parc … compte quatre secteurs de camping.", "qui"),
        ("Le gîte … Camille a recommandé est au village.", "que"),
        ("Rimouski est la ville … sa tante travaille.", "où"),
        ("Le sentier … monte à la montagne fait sept kilomètres.", "qui"),
        ("Les phoques … on voit à marée basse sont sur les roches.", "que"),
        ("C'était l'automne … elle a pris son premier autocar.", "où"),
    ], corrige=True,
       notes="Faire appliquer le test à voix haute à chaque ligne : « qu'est-ce qui "
             "vient après ? ». La cinquième est la plus difficile parce que le sujet "
             "« on » est court et passe inaperçu.")

    d.piege("Choisir « qui » parce que ça parle d'une personne",
            "Les gens qu'on rencontre… non, les gens qui on rencontre.",
            "Les gens qu'on rencontre — « on » est le sujet, donc « que ».",
            "« Qui » et « que » ne dépendent pas du tout de ce dont on parle : une "
            "personne ou une chose, c'est pareil. Ils dépendent uniquement de ce "
            "qui suit dans la phrase.",
            notes="C'est l'erreur de raisonnement la plus tenace, parce qu'elle vient "
                  "d'une analogie avec « qui » interrogatif, qui, lui, désigne bien une "
                  "personne. Le dire explicitement : ce sont deux mots différents.")

    d.pratique('Production', "Réunissez les deux phrases en une seule",
               "À l'écrit, puis lecture à voix haute.", [
        ("C'est un sentier. Il longe le fleuve.", "C'est un sentier qui longe le fleuve."),
        ("J'ai pris un dépliant. Il présente le parc.", "J'ai pris un dépliant qui présente le parc."),
        ("Voici le gîte. Camille l'a recommandé.", "Voici le gîte que Camille a recommandé."),
        ("C'est le village. Le phare s'y trouve.", "C'est le village où le phare se trouve."),
        ("J'ai visité le phare. Il pleuvait ce jour-là.", "J'ai visité le phare le jour où il pleuvait."),
    ], corrige=True,
       notes="C'est l'exercice qui compte. Faire lire les phrases réunies à voix haute : "
             "on entend immédiatement qu'elles sonnent plus adultes que les deux phrases "
             "courtes. C'est un argument efficace auprès du groupe.")

    d.billet(
        "Écrivez deux phrases sur la région que vous aimeriez visiter, avec « qui » et « que ».",
        exemples=[
            "Une phrase avec « qui », une avec « que ».",
            "Vérifiez : après « qui », un verbe ; après « que », un sujet.",
        ],
        notes="Ramasser les billets. Les phrases réutilisables reviennent en C4, dans la "
              "fiche de voyage, et en E2 dans le courriel.")

    return d.save(dossier)
