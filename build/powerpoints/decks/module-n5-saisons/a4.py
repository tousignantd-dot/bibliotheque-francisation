# -*- coding: utf-8 -*-
"""A4 · La langue des avis
Bloc A « Je découvre » · couleur ambre · 75 min. Écriture et registre.
Source : exercice `prAvis` et sa mini-leçon du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="La langue des avis",
        chapeau="« Un avertissement a été émis. » « L'avis est en vigueur "
                "jusqu'à samedi matin. » « L'avertissement a été levé. » Six "
                "mots reviennent tous les jours dans la bouche du service — "
                "et le dernier est celui qu'on oublie d'attendre.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. Elle referme le vocabulaire de l'avis en "
                  "passant à la langue elle-même : les verbes, le passif, les formules "
                  "figées. Ouvrir en projetant un vrai avis d'Environnement Canada et en "
                  "faisant souligner les six mots au fur et à mesure.")

    d.objectifs([
        "employer « émettre » et « lever » au passif, comme le fait le service ;",
        "comprendre « en vigueur » et savoir ce qu'il commande ;",
        "reconnaître les formules figées, qui s'apprennent d'un bloc ;",
        "savoir que les prévisions changent, et pourquoi ce n'est pas une erreur.",
    ], notes="Le quatrième objectif désamorce une méfiance très répandue : « ils se "
             "trompent tout le temps ». Non — ils réévaluent. Ce qui en découle est la "
             "méthode du module : décider le plus tard possible, mais dire d'avance "
             "quand on décidera.")

    d.declencheur(
        'Lecture', "« Un avertissement de pluie verglaçante a été émis. » "
                   "Qui l'a émis ?",
        pistes=[
            "Le nom de la personne est-il dans la phrase ?",
            "Pourquoi le service ne dit-il jamais qui a décidé ?",
            "Quelle différence avec « Environnement Canada a émis un avertissement » ?",
            "Laquelle des deux formes met l'avertissement en avant ?",
        ],
        notes="Le passif est ici au service du sens, pas de la grammaire : l'avis compte, "
              "pas la personne qui l'a signé. Le faire découvrir par les pistes plutôt "
              "que l'annoncer.")

    d.regle("Émettre, être en vigueur, être levé",
            "Un avis est émis, il reste en vigueur un certain temps, puis il "
            "est levé.",
            precision="Tant qu'il est en vigueur, il compte. Quand il est levé, "
                      "c'est fini — et c'est le mot que presque personne n'attend.",
            notes="Diapositive à photographier. Faire remarquer que les trois verbes sont "
                  "au passif : c'est la langue du service, et l'élève n'a qu'à la "
                  "reconnaître, pas à la produire — sauf pour « en vigueur », qui sert "
                  "dans le message au groupe.")

    d.cartes("Quatre formules", "Ce qui s'apprend d'un bloc", [
        ("Un avertissement a été émis",
         "L'avis vient de sortir. Personne n'est nommé, et c'est normal."),
        ("L'avis est en vigueur jusqu'à…",
         "Il compte encore. Notez l'heure de fin : c'est ce qui vous sert."),
        ("L'avertissement a été levé",
         "C'est terminé. On peut maintenir ce qu'on avait reporté."),
        ("Je vous confirme vendredi à midi",
         "Ce qu'on dit quand on ne peut pas encore décider."),
    ], notes="Les quatre se répètent en chœur, puis individuellement. Ce sont des "
             "formules : on ne les construit pas mot à mot, on les prend entières. "
             "Insister sur la quatrième — c'est la seule que l'élève dira lui-même.")

    d.tableau('Trois avis', "Ce qu'on fait devant chacun",
              ['Avis', "Ce qu'il dit", "Ce qu'on fait"],
              [["Bulletin spécial", "Un temps inhabituel s'en vient", "On lit et on attend"],
               ["Veille", "C'est possible", "On surveille, on annonce quand on répondra"],
               ["Avertissement", "C'est imminent ou commencé", "On décide et on prévient"],
               ["Avis levé", "C'est terminé", "On peut maintenir"]],
              note="Le quatrième n'est pas un avis : c'est la fin des trois autres.",
              notes="Reprendre la règle de A1 en y ajoutant la ligne « avis levé ». C'est "
                    "la seule nouveauté du tableau, et c'est celle qui manque le plus aux "
                    "gens : beaucoup annulent pour un avis retiré la veille au soir.")

    d.piege("Croire qu'un changement de prévision est une erreur",
            "Ils ont dit trente centimètres, il en est tombé dix. Ils se trompent tout le temps.",
            "Ils ont réévalué. C'est pour ça qu'on décide le plus tard possible.",
            "Une prévision se refait plusieurs fois par jour à mesure que les "
            "données arrivent. Ce n'est pas de l'incompétence : c'est le métier.",
            notes="Ce piège n'est pas linguistique, mais il empêche d'employer la "
                  "méthode : quelqu'un qui ne fait pas confiance aux prévisions décide "
                  "trop tôt, ou pas du tout.")

    d.pratique('Écriture', "Complétez l'avis",
               "Un mot par trou : veille, avertissement, prévisions, "
               "éclaircies, en vigueur, émis.", [
        ("Une ___ de tempête hivernale a été émise : le phénomène est possible.", "veille"),
        ("Un ___ de pluie verglaçante a été émis : c'est imminent.", "avertissement"),
        ("L'avis est ___ jusqu'à samedi matin.", "en vigueur"),
        ("Les ___ de vendredi ont changé trois fois dans la journée.", "prévisions"),
        ("On annonce quelques ___ en fin d'après-midi.", "éclaircies"),
        ("L'avertissement a été ___ par Environnement Canada cet après-midi.", "émis"),
    ], corrige=True,
       notes="Ce sont les six items de l'exercice prAvis du module. Les faire ici sur "
             "papier, puis renvoyer au module pour la correction automatique et la "
             "mini-leçon. Faire relire chaque phrase complétée à voix haute.")

    d.billet(
        "Écrivez en trois lignes l'avis que vous enverriez à un groupe, jeudi soir.",
        exemples=[
            "Dites quel avis est en vigueur, et jusqu'à quand.",
            "Terminez par : « Je vous confirme vendredi à midi. »",
        ],
        notes="C'est la première production écrite du module, et elle est courte exprès. "
              "Ramasser les billets : ils montrent qui a compris que « je ne sais pas "
              "encore » se dit avec une heure.")

    return d.save(dossier)
