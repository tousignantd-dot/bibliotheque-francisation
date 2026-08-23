# -*- coding: utf-8 -*-
"""A4 · Affirmé, ou seulement suggéré ?
Bloc A « Je découvre » · couleur ambre · 75 min.
Source : exercice `prDit`, mini-leçon `prDit`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Affirmé, ou seulement suggéré ?",
        chapeau="Une annonce contient deux sortes de phrases : celles qui "
                "engagent leur auteur devant la loi, et celles qui ne "
                "l'engagent à rien. Tout le module tient dans cette "
                "différence.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A, et la plus importante des quatre. Si le "
                  "groupe ne repart qu'avec une chose, que ce soit celle-ci.")

    d.objectifs([
        "séparer une affirmation vérifiable d'une simple suggestion ;",
        "poser à toute annonce la question qui tranche ;",
        "reconnaître les trois mots qui annoncent une suggestion ;",
        "comprendre pourquoi une suggestion n'est pas illégale, mais vide.",
    ], notes="Le quatrième objectif évite le contresens le plus fréquent : les élèves "
             "concluent volontiers que la publicité est illégale. Elle ne l'est pas.")

    d.declencheur(
        'Observation', "Qu'est-ce qu'on vous promet, au juste ?",
        pistes=[
            "« Notre matelas est garanti dix ans. » Que promet-on ?",
            "« Vos nuits valent mieux que ça. » Que promet-on ?",
            "Si la première phrase était fausse, que pourriez-vous reprocher ?",
            "Et si la seconde était fausse ?",
        ],
        notes="Laisser le groupe buter sur la quatrième question : on ne peut rien "
              "reprocher, parce que rien n'a été affirmé. C'est là que la séance "
              "commence vraiment.")

    d.regle("Le test tient en une question",
            "Qu'est-ce que je pourrais reprocher si ce n'était pas vrai ?",
            precision="Si vous trouvez quelque chose à reprocher — un prix, une "
                      "durée, une quantité, un rang —, l'annonceur s'est engagé. Si "
                      "vous ne trouvez rien, c'est que rien ne vous a été promis.",
            notes="Diapositive à photographier. La question se pose à voix haute et "
                  "elle se pose vite : c'est un réflexe, pas une analyse.")

    d.tableau('Analyse', "Deux sortes de phrases",
              ['Ce qu\'elle fait', 'Ce qui arrive si c\'est faux'],
              [["Elle affirme un fait", "représentation trompeuse, et un recours existe"],
               ["Elle donne une impression", "rien : il n'y a rien à contredire"],
               ["Elle chiffre", "on peut aller vérifier"],
               ["Elle compare sans dire à quoi", "on ne peut pas vérifier"]],
              cle=0,
              note="La deuxième n'est pas illégale. Elle est vide, ce qui est différent.",
              notes="Diapositive à photographier. Le mot « vide » est celui à retenir : "
                    "il évite l'indignation et permet l'analyse.")

    d.cartes('Analyse', "Les trois mots qui annoncent une suggestion", [
        ("pourrait, pourraient", "une possibilité, jamais une promesse"),
        ("jusqu'à", "la limite haute, donnée pour le cas ordinaire"),
        ("plus, sans deuxième terme", "un comparatif que vous complétez vous-même"),
    ], cols=1,
       notes="Trois mots seulement, et ils reviennent dans toutes les annonces du "
             "module. Les faire noter tels quels : ce sont des signaux d'alarme.")

    d.pratique('Pratique', "Affirmé, ou suggéré ?",
               "Classez chaque phrase d'annonce.", [
        ("Nos entraîneurs pourraient vous faire découvrir un corps que vous ne connaissez pas.", "suggéré - le conditionnel"),
        ("Le plus grand centre de la Rivière-du-Nord.", "affirmé - un rang se vérifie"),
        ("Un environnement plus chaleureux.", "suggéré - plus que quoi ?"),
        ("Frais d'adhésion de soixante dollars applicables.", "affirmé - un montant"),
        ("Jusqu'à quarante pour cent de rabais sur les matelas sélectionnés.", "suggéré - la limite haute"),
        ("Il ne reste que trois jours à notre vente d'entrepôt.", "affirmé - une durée"),
        ("Parce que vos nuits valent mieux que ça.", "suggéré - rien de vérifiable"),
        ("Plus de vingt appareils neufs.", "affirmé - une quantité chiffrée"),
    ], corrige=True,
       notes="Exercice `prDit` du module. Le huitième surprend : « plus de vingt » "
             "est un chiffre, pas un comparatif tronqué. Prendre le temps de le dire.")

    d.piege('Lecture',
            "« ils mentent »",
            "« ils me laissent conclure »",
            "Un annonceur qui écrit « prenez soin de vous » ne ment pas : il "
            "ne dit rien. Ce qu'on peut lui reprocher, c'est d'avoir placé "
            "cette phrase là où vous cherchiez un prix. La différence n'est "
            "pas morale, elle est pratique : on ne se plaint pas de la même "
            "façon d'un mensonge et d'un silence.",
            notes="Point de rigueur. Un élève qui dit « c'est de la fraude » se fera "
                  "répondre non, et perdra sa cause. Le module lui donne les mots "
                  "justes.")

    d.billet(
        "Reprenez l'annonce que vous avez notée en A1 : que promet-elle vraiment ?",
        exemples=[
            "Écrivez une phrase affirmée et une phrase suggérée.",
            "S'il n'y a aucune phrase affirmée, écrivez-le : c'est une réponse.",
        ],
        notes="Devoir de classement. La consigne « c'est une réponse » compte : "
              "beaucoup d'annonces n'affirment strictement rien, et le constater est "
              "l'apprentissage.")

    return d.save(dossier)
