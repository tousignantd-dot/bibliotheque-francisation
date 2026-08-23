# -*- coding: utf-8 -*-
"""A1 · Le camion est reparti, et il reste trois choses
Bloc A « Je découvre » · couleur framboise · 75 min. Vocabulaire.
Source du module : `FC_CARDS` (prep) et l'exercice `prVocab`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='framboise',
        titre="Le camion est reparti, et il reste trois choses",
        chapeau="Une rampe tordue, deux boîtes noyées, un meuble fendu. "
                "Avant de réclamer quoi que ce soit, il faut savoir "
                "comment ces choses-là s'appellent.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Demander d'entrée qui a déjà "
                  "déménagé au Québec, et qui avait une assurance habitation "
                  "ce jour-là. La deuxième main est toujours beaucoup plus "
                  "basse que la première : c'est tout le sujet du module.")

    d.objectifs([
        "nommer ce qui a été abîmé et par qui ;",
        "distinguer déclarer un sinistre et réclamer ;",
        "dire ce qu'un inventaire et un connaissement engagent ;",
        "reconnaître le point qu'on concède et celui qu'on défend.",
    ], notes="Le programme ne rattache aucun lexique à cette situation : le "
             "vocabulaire a été composé à partir des deux savoirs du cours "
             "sur l'assurance. Les seize mots du module en sortent.")

    d.declencheur(
        'Pour commencer', "Le jour d'un déménagement, qu'est-ce qui peut "
                          "s'abîmer, et qui est responsable ?",
        pistes=[
            "Qu'est-ce que vous avez vu s'abîmer, chez vous ou chez d'autres ?",
            "Qui répare : la personne qui déménage, le propriétaire, la compagnie ?",
            "Comment prouveriez-vous que ce n'était pas déjà cassé ?",
        ],
        notes="La troisième question est celle qui compte : elle amène l'idée "
              "de preuve datée, sur laquelle tout le module repose. Laisser "
              "venir « je le dirais » avant de parler de photos et de papiers.")

    d.vocabulaire('Vocabulaire', 'Les cinq mots du jour du déménagement', [
        ("un sinistre", "L'événement qui cause le dommage et qui déclenche le contrat."),
        ("un inventaire", "La liste écrite de tout ce qui est transporté ou abîmé."),
        ("un connaissement", "Le papier que le transporteur fait signer et qui dit ce qu'il prend en charge."),
        ("une déclaration de valeur", "Le fait d'annoncer d'avance ce que vaut un objet, pour qu'il soit couvert à ce prix-là."),
        ("un dégât d'eau", "Le dommage causé par l'eau qui entre là où elle ne devrait pas."),
    ], notes="Faire répéter chaque mot avec son article. « Connaissement » est "
             "difficile et rare : le dire trois fois, et préciser que c'est le "
             "papier qu'on signe dans le camion, souvent sans le lire.")

    d.regle("Ce qui n'est pas noté n'a pas eu lieu",
            "L'inventaire signé au départ est la seule photographie de l'état de vos meubles avant le transport.",
            precision="Un dommage absent de cette feuille est réputé ne pas "
                      "avoir existé — et, dans l'autre sens, un dommage qui "
                      "apparaît après elle devient très difficile à nier.",
            notes="Diapositive à photographier. Insister sur les deux sens : "
                  "la feuille protège le transporteur des dommages anciens, "
                  "et elle protège la personne des dommages nouveaux.")

    d.tableau('Analyse', "Les gestes du premier soir",
              ['Ce qu\'on fait', 'Ce que ça règle plus tard'],
              [["Réclamer la copie signée", "l'état des biens avant le transport"],
               ["Photographier avec la date", "le dommage situé à la minute"],
               ["Noter l'heure du camion", "la période où un autre avait la garde"],
               ["Ne rien jeter, ne rien réparer", "un bien jeté n'est plus indemnisable"]],
              cle=0,
              note="Vingt minutes le soir même valent six semaines de courriels.",
              notes="Diapositive à photographier. Demander lequel des cinq "
                    "gestes leur semble le plus difficile le jour même : la "
                    "réponse est presque toujours le premier, parce qu'on est "
                    "épuisé et que les hommes sont pressés de partir.")

    d.cartes('Attention', "Déclarer ou réclamer ?", [
        ("Déclarer un sinistre", "c'est dire qu'il s'est passé quelque chose. Ça n'engage à rien."),
        ("Réclamer", "c'est demander de l'argent. Ça vient après, avec un inventaire."),
        ("Ce qui se passe", "Beaucoup de gens attendent d'avoir tout chiffré pour appeler. Ils appellent trois semaines trop tard."),
        ("La règle", "On déclare le jour même. Plus la déclaration est proche des faits, moins elle se discute."),
    ], cols=2,
       notes="Confusion très fréquente, et coûteuse. Le délai de déclaration "
             "est une vraie date inscrite au contrat, souvent trente jours.")

    d.pratique('Pratique', "Le mot et sa définition",
               "Reliez chaque mot à ce qu'il veut dire.", [
        ("un sinistre", "l'événement qui déclenche le contrat"),
        ("un inventaire", "la liste écrite de ce qui est transporté"),
        ("un connaissement", "le papier que le transporteur fait signer"),
        ("une déclaration de valeur", "annoncer d'avance ce que vaut un objet"),
        ("un dégât d'eau", "le dommage causé par l'eau"),
    ], corrige=True, cols=1,
       notes="Faire à l'oral d'abord, puis à l'écrit. C'est l'exercice "
             "`prVocab` du module, dans sa version projetée.")

    d.billet(
        "Nomme un objet chez toi que tu déclarerais à sa valeur avant un déménagement, et dis pourquoi.",
        exemples=[
            "Une seule phrase, avec le nom de l'objet.",
            "La raison doit tenir en cinq mots : « parce qu'il vient de… ».",
        ],
        notes="Trois minutes. Ramasser et lire rapidement : les objets nommés "
              "sont presque toujours des objets de famille rapportés du pays "
              "d'origine, et c'est exactement la situation du module.")

    return d.save(dossier)
