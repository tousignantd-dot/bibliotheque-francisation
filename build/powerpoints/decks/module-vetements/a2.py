# -*- coding: utf-8 -*-
"""A2 · Le féminin qu'on entend.
Bloc A « Je découvre » · couleur teal · 60 min.
Source : mini-leçon `prPhon`, exercice `prPhon` (cartes à écouter).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='teal',
        titre="Le féminin qu'on entend",
        chapeau="« Un manteau gris », « une veste grise ». Au masculin, la "
                "consonne finale dort ; au féminin, le -e la réveille. C'est "
                "ce qui permet d'entendre le genre.",
        duree='60 minutes')

    d.titre(notes="Séance d'écoute. Prévoir le son. Commencer en disant « gris » puis "
                  "« grise » lentement : la différence s'entend d'emblée.")

    d.objectifs([
        "entendre la consonne finale au féminin ;",
        "savoir qu'elle est muette au masculin ;",
        "employer le féminin pour trouver la lettre à écrire ;",
        "reconnaître les adjectifs qui ne changent pas.",
    ])

    d.declencheur(
        'Écoute', "Ces deux mots sont-ils différents ?",
        pistes=[
            "« gris » et « grise »",
            "« petit » et « petite »",
            "Qu'est-ce qui change à l'oreille ?",
            "Et à l'écrit ?",
        ],
        notes="Faire écouter les paires avant toute explication. Le groupe entend la "
              "consonne apparaître, même s'il ne sait pas encore la nommer.")

    d.tableau('Analyse', "La consonne se réveille",
              ['Masculin', 'Féminin'],
              [["gris — le s est muet", "grise — on entend le s"],
               ["petit — le t est muet", "petite — on entend le t"],
               ["vert — le t est muet", "verte — on entend le t"],
               ["grand — le d est muet", "grande — on entend le d"]],
              cle=0,
              note="C'est le -e du féminin qui fait sonner la consonne d'avant.",
              notes="Diapo centrale. Faire recopier. Le -e lui-même ne se prononce pas : il "
                    "ne fait que réveiller la consonne.")

    d.regle("Deux usages, tout de suite",
            "Pour comprendre, et pour écrire.",
            precision="À l'<b>écoute</b> : si vous entendez la consonne, l'objet est "
                      "féminin — vous savez qu'on parle d'une veste et non d'un manteau, "
                      "même si vous avez manqué le nom. À l'<b>écrit</b> : dites le mot au "
                      "féminin dans votre tête, et la lettre à écrire apparaît.",
            notes="Diapo à photographier. Le second usage est le plus utile au quotidien : "
                  "« court » ou « cour » ? Dites « courte ».")

    d.cartes('Les adjectifs qui ne changent pas', "Trois familles", [
        ("Ceux qui finissent déjà par -e",
         "rouge, jaune, beige, mince, large, ample. Un manteau rouge, une veste rouge : "
         "aucune différence."),
        ("Les couleurs venues de noms de choses",
         "marine, kaki, crème, orange, turquoise. Elles ne prennent ni -e ni -s : « des "
         "bottes marine »."),
        ("Ce qu'il faut en retenir",
         "Si l'adjectif finit déjà par -e au masculin, il ne bouge pas. C'est la seule "
         "exception à connaître."),
    ], notes="Cette carte évite la surcorrection : certains élèves ajoutent un -e partout "
             "une fois la règle apprise.")

    d.piege("Prononcer la consonne au masculin",
            "un manteau « griss »",
            "un manteau « gri »",
            "Au masculin, la consonne finale est muette. La prononcer donne un mot qui "
            "n'existe pas, et cela s'entend immédiatement. C'est l'erreur inverse de la "
            "plus fréquente — mais elle arrive quand on vient d'apprendre la règle.",
            notes="Faire dire les deux formes par le groupe, en alternance : gri / grise, "
                  "peti / petite.")

    d.pratique('Pratique · 1 de 2', "Masculin ou féminin ?",
               "Écoutez chaque mot.", [
        ("petit", "masculin — le t est muet"),
        ("petite", "féminin — on entend le t"),
        ("gris", "masculin"),
        ("grise", "féminin"),
        ("court", "masculin"),
        ("courte", "féminin"),
    ], corrige=True,
       notes="Utiliser l'exercice 2 du module. Deux écoutes avant de corriger.")

    d.pratique('Pratique · 2 de 2', "Quelle lettre écrire ?",
               "Dites le mot au féminin pour trouver la lettre finale.", [
        ("cour… (pas long)", "court — courte"),
        ("gran… (pas petit)", "grand — grande"),
        ("ver… (la couleur)", "vert — verte"),
        ("épai… (pas mince)", "épais — épaisse"),
        ("chau… (pas froid)", "chaud — chaude"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice le plus utile de la séance : il transforme une règle de "
             "prononciation en outil d'orthographe.")

    d.cartes("Pourquoi ça compte dans ce module", "Trois raisons", [
        ("Les vêtements ont un genre",
         "un manteau, une veste, un chandail, une tuque. L'adjectif suit — et il s'entend."),
        ("Les couleurs sont des adjectifs",
         "noir/noire, gris/grise, vert/verte. C'est le cas le plus fréquent de tout le "
         "module."),
        ("Les mesures aussi",
         "court/courte, long/longue, large, serré/serrée. Ce sont les mots de la cabine "
         "d'essayage."),
    ], notes="Faire produire une phrase de chaque type par le groupe : « une veste grise, un "
             "peu courte ».")

    d.billet(
        "Écrivez six phrases sur des vêtements, trois au masculin, trois au féminin.",
        exemples=[
            "Employez une couleur et un adjectif de mesure dans chacune.",
            "Soulignez les consonnes finales que vous entendez.",
        ],
        notes="Corriger surtout l'accord au féminin. Rendre à la séance suivante.")

    return d.save(dossier)
