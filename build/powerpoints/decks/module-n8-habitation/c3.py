# -*- coding: utf-8 -*-
"""C3 · Concéder pour être lu
Bloc C « Défi 2 · L'appel qui conteste » · couleur ambre · 75 min.
Source : exercice `t2conc` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Donner raison, puis avancer",
        chapeau="Une contestation qui nie tout se lit en dix secondes et se "
                "classe comme une plainte de plus. Trois lignes de "
                "concession font lire les quinze suivantes.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, mais le point de départ n'est pas grammatical : "
                  "c'est un calcul. Concéder est ce qui rend la suite crédible, et "
                  "c'est vrai bien au-delà d'une lettre d'assurance.")

    d.objectifs([
        "employer « bien que » et « quoique » avec le subjonctif ;",
        "employer « même si » avec l'indicatif, sans se tromper ;",
        "construire une concession écrite : certes… ; il n'en reste pas moins que…",
        "placer la concession avant les faits, jamais après.",
    ], notes="Les deux premiers objectifs vont ensemble et se commettent souvent en "
             "même temps, chacun à l'envers de l'autre.")

    d.declencheur(
        'Discussion', "Quelqu'un vous accuse de quelque chose que vous n'avez pas fait. Que dites-vous ?",
        pistes=[
            "Est-ce que vous niez tout, d'un bloc ?",
            "Y a-t-il une petite partie de ce qu'il dit qui est vraie ?",
            "Qu'est-ce que ça change de le reconnaître ?",
            "Qu'est-ce que ça change de ne pas le reconnaître ?",
        ],
        notes="Faire venir la réponse du groupe. Nier en bloc met l'autre en position "
              "de chercher ce qu'on cache ; concéder un point lui enlève cette "
              "position. C'est du calcul, pas de la morale.")

    d.regle("Ce qu'on met en second l'emporte",
            "« Le drain était vieux, mais il avait été nettoyé » plaide pour "
            "vous. « Le drain avait été nettoyé, mais il était vieux » "
            "plaide contre vous. Ce sont exactement les mêmes mots.",
            precision="Concédez donc en premier, sans exception, et gardez votre fait "
                      "le plus solide pour la fin de la phrase. C'est vrai de la "
                      "phrase, et c'est vrai de la lettre entière.",
            notes="Diapositive à photographier. Faire lire les deux versions par deux "
                  "personnes différentes, puis demander laquelle on croit.")

    d.tableau('Formes', "Quel marqueur, quel mode",
              ['Marqueur', 'Mode et exemple'],
              [["bien que · quoique", "subjonctif — bien que le rapport SOIT détaillé"],
               ["même si", "indicatif — même si l'obstruction EST ancienne"],
               ["certes…, mais…", "indicatif — le registre de l'écrit"],
               ["il n'en reste pas moins que", "indicatif — la formule qui conclut"],
               ["en revanche · toutefois", "indicatif — opposer sans concéder"]],
              cle=0,
              notes="Diapositive à photographier. Le repère qui sauve : « même si » "
                    "est un « si », et « si » n'a jamais de subjonctif.")

    d.piege(
        'Mode',
        "même si le rapport soit détaillé",
        "même si le rapport est détaillé",
        "« Même si » veut l'indicatif, toujours. C'est la faute qui trahit "
        "le plus vite un apprenant avancé, parce qu'elle vient d'une "
        "sur-correction : on a appris que la concession demande le "
        "subjonctif, et on l'applique partout. Retenez le couple : bien que, "
        "subjonctif ; même si, indicatif.",
        notes="Écrire le couple au tableau et l'y laisser toute la séance. Les deux "
              "fautes inverses se commettent souvent le même jour, chez la même "
              "personne.")

    d.pratique('Grammaire', "Le marqueur qui convient",
               "Attention au mode du verbe qui suit.", [
        ("___ le rapport soit détaillé, il ne s'appuie sur aucune caméra.", "Bien que / Quoique"),
        ("___ l'obstruction est ancienne, elle n'explique pas une seule soirée.", "Même si"),
        ("Ce n'est pas vous qui avez fermé le dossier ; il n'en ___ pas moins que c'est à vous que j'écris.", "reste"),
        ("Le contrat couvre le refoulement ; ___ revanche, il exclut le défaut d'entretien.", "en"),
        ("___ , la visite a été courte ; mais elle a donné lieu à des mesures.", "Certes"),
        ("La franchise reste due ; ___ , le reste des dommages est couvert.", "toutefois"),
    ], corrige=True,
       notes="Faire justifier le mode à chaque fois. Le troisième est une formule "
             "figée : la faire répéter à voix haute jusqu'à ce qu'elle vienne seule.")

    d.cartes('Modèles', "Concéder, puis retourner", [
        ("Sur un constat",
         "« Certes, un dépôt a bien été observé sur la grille ; il n'en "
         "reste pas moins qu'aucune mesure n'a été prise et qu'aucune "
         "inspection par caméra n'a été effectuée. »"),
        ("Sur une durée",
         "« Bien que la visite ait eu lieu deux jours après le sinistre, "
         "elle n'a duré que vingt-cinq minutes. »"),
        ("Sur l'âge de l'installation",
         "« Même si le drain a douze ans, il a été nettoyé cinq mois avant "
         "le sinistre, et la facture acquittée est jointe. »"),
        ("Sur la personne au téléphone",
         "« Certes, ce n'est pas vous qui avez rendu la décision ; il n'en "
         "reste pas moins que c'est à vous que je peux parler aujourd'hui. »"),
    ], notes="Faire remarquer ce qu'on concède : toujours un constat, jamais une "
             "déduction. On donne raison sur ce que l'expert a vu, et on discute ce "
             "qu'il en tire. C'est le lien direct avec le bloc B.")

    d.billet(
        "Écrivez une concession sur le dossier de Teodora, en deux temps.",
        exemples=[
            "Premier temps : ce que vous accordez, avec « certes ».",
            "Deuxième temps : ce que vous en faites, avec « il n'en reste pas moins que ».",
        ],
        notes="Une seule phrase, deux temps. Elle entrera telle quelle dans la lettre "
              "du bloc E : le paragraphe de concession est écrit ce matin.")

    return d.save(dossier)
