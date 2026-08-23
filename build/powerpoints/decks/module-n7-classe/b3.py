# -*- coding: utf-8 -*-
"""B3 · Le chiffre qu'on n'a pas vérifié
Bloc B « Défi 1 » · couleur ambre · grammaire · 75 min.
Source : exercice `t1cond`, mini-leçon `t1cond`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Le chiffre qu'on n'a pas vérifié",
        chapeau="« L'écart est de dix degrés » vous engage. « L'écart serait "
                "de dix degrés » vous protège. Une syllabe sépare les deux, "
                "et dans un travail de recherche, elle vaut cher.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, et la plus utile du Défi 1. Le conditionnel "
                  "est déjà connu comme forme de politesse ; l'emploi travaillé ici "
                  "est le second, et il surprend souvent.")

    d.objectifs([
        "former le conditionnel présent des verbes courants ;",
        "reconnaître les huit radicaux irréguliers, qui sont ceux du futur ;",
        "employer le conditionnel pour rapporter sans garantir ;",
        "distinguer cet emploi de celui de la politesse.",
    ], notes="Le troisième objectif est celui du défi ; les deux premiers sont l'outil "
             "et le quatrième évite la confusion la plus fréquente.")

    d.declencheur(
        'Observation', "Deux phrases, une syllabe de différence",
        pistes=[
            "« La canopée est de dix-sept pour cent. »",
            "« La canopée serait de dix-sept pour cent. »",
            "Laquelle diriez-vous si vous n'avez pas vu le document ?",
            "Que se passe-t-il si le chiffre est faux, dans un cas et dans l'autre ?",
        ],
        notes="La dernière piste est le cœur de la séance : la première phrase est "
              "fausse si le chiffre l'est ; la seconde reste exacte, parce qu'elle "
              "n'a rien affirmé.")

    d.regle("Radical du futur, terminaisons de l'imparfait",
            "Le conditionnel se fabrique avec le radical du futur et les "
            "terminaisons de l'imparfait. Il y a toujours un « r » juste "
            "avant la terminaison.",
            precision="Je parlerais, tu parlerais, elle parlerait, nous parlerions, "
                      "vous parleriez, elles parleraient. Rien de neuf à apprendre : "
                      "deux choses connues, assemblées.",
            notes="Diapositive à photographier. Le « r » est le repère à donner : "
                  "c'est lui qui distingue le conditionnel de l'imparfait.")

    d.tableau('Analyse', "Les huit radicaux irréguliers",
              ['Le verbe', 'Au conditionnel'],
              [["être", "je serais"],
               ["avoir", "j'aurais"],
               ["aller", "j'irais"],
               ["faire", "je ferais"],
               ["pouvoir", "je pourrais"],
               ["devoir", "je devrais"],
               ["venir", "je viendrais"]],
              cle=0,
              notes="Diapositive à photographier. Le huitième, falloir, n'existe qu'à "
                    "la troisième personne du singulier : il faudrait. Le dire à "
                    "l'oral plutôt que de charger le tableau.")

    d.tableau('Analyse', "Deux emplois, une seule forme",
              ['L\'emploi', 'Un exemple'],
              [["Rapporter sans garantir",
                "L'écart serait d'une dizaine de degrés, selon l'organisme."],
               ["Demander poliment",
                "Pourrais-tu reprendre plus lentement ?"],
               ["Proposer sans imposer",
                "On pourrait noter l'ombre à chaque coin de rue."]],
              cle=0,
              note="Même forme, trois usages. C'est le contexte qui tranche, jamais la forme.",
              notes="Diapositive à photographier. Les deux derniers emplois servent au "
                    "bloc D : ils sont l'outil de base de l'animation.")

    d.pratique('Grammaire', "Mettez au conditionnel présent",
               "Rapportez le renseignement au lieu de l'affirmer.", [
        ("Selon la fiche, la canopée ___ (être) de 17 %.", "serait"),
        ("D'après Perrine, l'écart ___ (atteindre) dix degrés.", "atteindrait"),
        ("Les jeunes arbres ___ (avoir) besoin d'eau trois ans.", "auraient"),
        ("Le programme ___ (viser) 400 arbres par année.", "viserait"),
        ("Il ___ (falloir) mesurer à la même heure.", "faudrait"),
        ("Cette méthode ___ (venir) d'une étude de l'an dernier.", "viendrait"),
    ], corrige=True,
       notes="Faire lire la phrase entière à voix haute après correction : "
             "l'oreille apprend le « r » plus vite que la règle.")

    d.piege('Grammaire',
            "« Je serai content de vous répondre. »",
            "« Je serais content de vous répondre. »",
            "Un « s » de différence, et deux sens. Le futur affirme ce qui "
            "va arriver ; le conditionnel présente la chose comme possible, "
            "ou l'exprime poliment. À l'oral, les deux se ressemblent "
            "beaucoup : c'est à l'écrit que l'erreur se voit.",
            notes="Piège classique et il vaut la peine d'y passer cinq minutes : il "
                  "reviendra dans les comptes rendus du bloc D, où le conditionnel "
                  "sert à rapporter un futur.")

    d.regle("Le conditionnel ne vient jamais seul",
            "Un chiffre au conditionnel s'accompagne toujours de sa source : "
            "selon la ville, d'après la fiche, si l'on en croit l'organisme.",
            precision="Le conditionnel dit que ce n'est pas de vous ; la source dit "
                      "de qui c'est. L'un sans l'autre laisse le lecteur devant un "
                      "chiffre qui flotte.",
            notes="Diapositive à photographier. C'est la règle que le travail écrit "
                  "du bloc C reprendra telle quelle.")

    d.pratique('Production', "Rapportez, puis nommez la source",
               "Une phrase complète, avec son conditionnel et sa source.", [
        ("Le pourcentage de canopée de la ville", "…serait de 17 %, selon la fiche de la ville."),
        ("La perte de jeunes arbres", "…serait d'un sur cinq, d'après le même document."),
        ("L'écart entre deux secteurs", "…atteindrait dix degrés, selon Perrine Auclair."),
        ("Le nombre d'arbres plantés par année", "…serait de 400, si l'on en croit le programme."),
    ], corrige=False,
       notes="Exercice écrit puis oral. Ramasser : ces quatre phrases se retrouveront "
             "presque telles quelles dans l'exposé du bloc E.")

    d.billet(
        "Écrivez un chiffre que vous avez trouvé, au conditionnel, avec sa source.",
        exemples=[
            "Un chiffre de votre propre sujet de recherche.",
            "Une seule phrase, et la source à la fin.",
        ],
        notes="Devoir concret. Vérifier deux choses en corrigeant : le « r » du "
              "conditionnel, et la présence de la source. L'un sans l'autre ne vaut "
              "rien.")

    return d.save(dossier)
