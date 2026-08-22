# -*- coding: utf-8 -*-
"""B3 · À quoi renvoie le petit mot
Bloc B « Défi 1 · Le diagnostic » · couleur ambre · 75 min.
Source : exercice `t1repr` et sa mini-leçon. Savoirs du programme : associer
le pronom « le » à son référent, « en » à un GPrép inanimé, « y » à son
complément ; reprendre des référents par une variété de pronoms.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="À quoi renvoie le petit mot",
        chapeau="« Je la répare », « on en a parlé », « il faut y penser ». "
                "Perdre le fil d'une explication, ce n'est pas manquer un "
                "mot : c'est perdre ce à quoi il renvoie.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire du texte, et c'est ce qui distingue vraiment le "
                  "niveau 6 des niveaux 3 et 5. Prévenir le groupe : les exercices "
                  "sont en deux phrases, parce qu'un pronom n'a de sens qu'après la "
                  "phrase qu'il reprend.")

    d.objectifs([
        "choisir le pronom sur le verbe, et non au son ;",
        "employer le, la, les quand le verbe n'a pas de préposition ;",
        "employer en après un verbe qui demande « de » ;",
        "employer y après un verbe qui demande « à », ou pour un lieu.",
    ], notes="Le premier objectif est la clé de tous les autres. Le répéter à chaque "
             "correction : on cherche la préposition du verbe, jamais l'oreille.")

    d.declencheur(
        'Observation', "« On en a parlé hier. » De quoi ?",
        pistes=[
            "Sans la phrase d'avant, peux-tu répondre ?",
            "Combien de mots faut-il remonter, d'habitude ?",
            "Que fais-tu quand tu as perdu le fil : tu demandes, ou tu continues ?",
        ],
        notes="La question n'a volontairement pas de réponse : c'est ce qui fait "
              "comprendre qu'un pronom ne vit jamais seul.")

    d.tableau('Analyse', "Le pronom se choisit sur le verbe",
              ['Le verbe demande', 'Le pronom'],
              [["rien du tout", "réparer quelque chose : le, la, les"],
               ["la préposition de", "parler de quelque chose : en"],
               ["la préposition à", "penser à quelque chose : y"],
               ["un lieu", "descendre au sous-sol : y"]],
              cle=0,
              note="« J'en pense » n'existe pas : on pense à. « J'y parle » non plus : on parle de.",
              notes="Diapositive à photographier. C'est le tableau de la séance. Les "
                    "deux erreurs de la note sont les plus fréquentes, et elles "
                    "viennent toujours de l'oreille.")

    d.tableau('Analyse', "Un « le » à part : celui qui reprend une idée",
              ['La phrase', 'Ce que « le » reprend'],
              [["Doïna le sait.", "que le sous-sol n'est pas sec"],
               ["Il me l'a dit deux fois.", "qu'il faut attendre quatre semaines"],
               ["Personne ne le sait.", "si le permis sortira à temps"],
               ["Léandre le lui a déconseillé.", "de faire les travaux lui-même"]],
              cle=0,
              note="Ce « le »-là ne s'accorde jamais : « elle l'a su », pas « elle l'a sue ».",
              notes="Diapositive à photographier. C'est l'emploi que le niveau 6 "
                    "ajoute, et le plus difficile. Le test : remplacer par « cela ».")

    d.regle("Reprendre au lieu de répéter",
            "Répéter le même nom six fois se lit comme un texte d'enfant.",
            precision="Le niveau 6 demande l'inverse : reprendre un référent par une "
                      "variété de pronoms et de déterminants. « La fissure » devient "
                      "« la », puis « cette fente », puis « le problème du mur nord ». "
                      "C'est ce qui fait tenir un texte long — et ce qui le rend "
                      "difficile à suivre quand on ne le sait pas.",
            notes="Diapositive à photographier. Faire le lien avec le bloc C : un "
                  "rapport d'inspection est bâti là-dessus.")

    d.pratique('Pratique', "Quel pronom ?",
               "Lisez les deux phrases, puis complétez.", [
        ("Fernand a examiné la fissure. Il ___ répare après les travaux du terrain.", "la"),
        ("Doïna a lu le rapport hier soir. Elle ___ a relu deux fois.", "l'"),
        ("Il faut penser au permis. Il faut ___ penser tout de suite.", "y"),
        ("On a parlé du taux d'humidité. Kettly ___ a reparlé dans son rapport.", "en"),
        ("Le sous-sol n'est pas sec. Doïna ___ sait.", "le"),
        ("La maison repose sur cette fondation. On ne peut pas ___ toucher.", "y"),
    ], corrige=True,
       notes="Faire dire à voix haute quel verbe commande le pronom, avant de donner "
             "la réponse. C'est ce raisonnement-là qu'on installe, pas la réponse.")

    d.piege('Piège', "choisir le pronom au son",
            "chercher la préposition du verbe",
            "« J'en pense » et « j'y parle » sonnent bien à l'oreille de qui apprend "
            "le français, et les deux sont impossibles. On pense À, donc « j'y "
            "pense ». On parle DE, donc « j'en parle ». Le verbe décide, jamais le "
            "son.",
            notes="Écrire les quatre formes au tableau, les deux fausses barrées. Les "
                  "laisser jusqu'à la fin de la séance.")

    d.pratique('Écriture', "Reprendre sans répéter",
               "Réécrivez la deuxième phrase en remplaçant le groupe souligné.", [
        ("On a fait injecter la fissure. On a payé la fissure 2 600 $.", "On l'a payée 2 600 $."),
        ("Il y a deux solutions. Fernand a proposé une des deux solutions.", "Fernand en a proposé une."),
        ("Le permis prend dix jours. Doïna pense au permis tous les jours.", "Doïna y pense tous les jours."),
        ("Le mur n'est pas sec. Kettly a parlé de l'humidité du mur.", "Kettly en a parlé."),
    ], corrige=True,
       notes="Exercice central de la séance. Accepter toute reprise correcte, y "
             "compris « cette solution » ou « ce problème » : la substitution "
             "lexicale est aussi au programme.")

    d.billet(
        "Écris deux phrases sur ton logement : la seconde reprend un mot de la première.",
        exemples=[
            "Emploie le, la, en ou y.",
            "Souligne le mot repris.",
        ],
        notes="Trois minutes. Ramasser : la moitié des billets emploieront « le » là "
              "où « en » ou « y » s'imposent, et ça donne la révision de B4.")

    return d.save(dossier)
