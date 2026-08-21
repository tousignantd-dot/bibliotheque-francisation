# -*- coding: utf-8 -*-
"""C2 · La route qui, la sortie que, l'endroit où
Bloc C « Défi 2 · Le bulletin de 6 h 50 » · couleur ambre · 75 min.
Source : exercice `t2rel` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="La route qui, la sortie que, l'endroit où",
        chapeau="Le bulletin ne dit pas : « La bretelle est fermée. Elle mène "
                "à la 40. » Il dit : « La bretelle qui mène à la 40 est "
                "fermée. » Une phrase au lieu de deux — et c'est cela que le "
                "niveau 5 appelle un discours organisé.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, mais entièrement au service de l'écoute : ces "
                  "quatre petits mots passent vite et emboîtent deux informations dans "
                  "une seule phrase. Ouvrir en écrivant les deux versions au tableau — "
                  "deux phrases, puis une — et laisser le groupe voir la différence.")

    d.objectifs([
        "employer « qui » quand un verbe suit tout de suite ;",
        "employer « que » quand un sujet suit ;",
        "employer « où » pour un lieu et pour un moment ;",
        "employer « dont » quand la phrase de départ contient « de ».",
    ], notes="Quatre pronoms en une séance, c'est beaucoup. « Qui » et « que » sont les "
             "deux à maîtriser aujourd'hui ; « où » et « dont » peuvent n'être que "
             "reconnus, ils reviendront à l'écrit en E2.")

    d.regle("Regardez le mot juste après",
            "Un verbe suit : c'est « qui ». Un sujet suit : c'est « que ».",
            precision="Le test tient en une seconde : si l'on peut mettre « il », "
                      "« nous » ou « vous » juste après, c'est « que ».",
            notes="Diapositive à photographier. C'est le seul truc à retenir de la "
                  "séance, et il règle quatre-vingts pour cent des cas.")

    d.tableau('Quatre pronoms', "Ce que chacun remplace",
              ['Le pronom', 'Ce qu\'il remplace'],
              [["qui", "le sujet du verbe qui suit"],
               ["que", "le complément direct"],
               ["où", "un lieu, ou un moment"],
               ["dont", "un complément avec « de »"]],
              cle=1,
              notes="Faire construire une phrase du module pour chaque ligne, en direct. "
                    "Les exemples inventés par le groupe valent mieux que les miens.")

    d.cartes("Quatre phrases du bulletin", "Repérez le mot qui suit", [
        ("La bretelle qui mène à la 40",
         "Un verbe suit : « mène »."),
        ("Le chemin que nous prenons",
         "Un sujet suit : « nous »."),
        ("L'endroit où l'accident s'est produit",
         "Un lieu : « où »."),
        ("La sortie dont je vous parlais",
         "On parle « de » la sortie : « dont »."),
    ], notes="Faire lire chaque carte à voix haute, puis couper la phrase en deux au "
             "tableau. Voir d'où vient le pronom vaut mieux que l'apprendre.")

    d.piege("Raccourcir « qui » devant une voyelle",
            "Le camion qu'est arrêté sur l'accotement.",
            "Le camion qui est arrêté sur l'accotement.",
            "« Qui » ne s'élide jamais. Seul « que » devient « qu' » : le chemin "
            "qu'on prend, l'entrave qu'il annonce.",
            notes="Une des rares règles du français sans aucune exception. La faire "
                  "répéter à voix haute : l'erreur vient de l'oral, elle se corrige à "
                  "l'oral.")

    d.piege("Dire « le jour que »",
            "Le jour que je suis arrivée au Québec.",
            "Le jour où je suis arrivée au Québec.",
            "Pour un moment comme pour un lieu, c'est « où ». « Le jour que » "
            "s'entend beaucoup, mais ce n'est pas ce qui s'écrit — et le module "
            "travaille aussi l'écrit.",
            notes="Dire honnêtement que la forme fautive s'entend partout : les élèves "
                  "l'ont entendue, et ne pas le reconnaître les met en doute sur le "
                  "reste.")

    d.pratique('Grammaire', "Complétez avec qui, que, où ou dont",
               "Une seule réponse par phrase.", [
        ("La bretelle ___ mène à la 40 ouest est fermée.", "qui"),
        ("Le chemin ___ nous prenons passe par le boulevard.", "que"),
        ("C'est l'endroit ___ l'accident s'est produit.", "où"),
        ("La voie de droite est la seule ___ reste ouverte.", "qui"),
        ("La sortie ___ je vous parlais est après le pont.", "dont"),
        ("Le matin ___ le pont était fermé, nous étions en retard.", "où"),
    ], corrige=True,
       notes="Les six mêmes phrases sont dans l'exercice `t2rel`. Faire dire la phrase "
             "complète après chaque correction, et faire nommer le mot qui suit le "
             "pronom : c'est le test.")

    d.billet(
        "Écrivez deux phrases sur votre trajet, une avec « qui » et une avec « que ».",
        exemples=[
            "L'autobus qui passe devant chez moi part à six heures trente.",
            "La ligne que je prends s'arrête au métro.",
        ],
        notes="Ramasser les billets. Les erreurs « qui / que » sont les plus faciles à "
              "corriger individuellement : il suffit de montrer le mot qui suit.")

    return d.save(dossier)
