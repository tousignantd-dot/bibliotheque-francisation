# -*- coding: utf-8 -*-
"""C2 · Dire quelles journées.
Bloc C « Défi 2 · Le billet d'absence » · couleur teal (écoute et réponds) · 75 min.
Source : exercice `t2temps`, mini-leçon `t2temps`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='teal',
        titre='Dire quelles journées',
        chapeau="La secrétaire écrit des dates, pas des impressions. Une "
                "réponse vague oblige à redemander ; une réponse précise "
                "règle la démarche en trente secondes.",
        duree='75 minutes')

    d.titre(notes="Séance de langue orale. Le petit groupe de mots travaillé ici est "
                  "exactement celui dont l'élève aura besoin, et pas un de plus.")

    d.objectifs([
        "employer hier, avant-hier, la semaine passée ;",
        "dire une période avec du… au… ;",
        "distinguer depuis et pendant ;",
        "nommer les journées manquées dans l'ordre.",
    ])

    d.tableau('Analyse', "Les mots qui situent une absence",
              ["On dit", "Ce que ça veut dire"],
              [["hier, avant-hier", "la journée d'avant, celle d'encore avant"],
               ["la semaine passée", "la semaine qui vient de finir"],
               ["du lundi au mercredi", "les deux journées du bout sont comprises"],
               ["pendant trois jours", "une durée finie"],
               ["depuis lundi", "ça a commencé lundi et ça continue"]],
              cle=1,
              note="Au Québec, on dit « la semaine passée » plus souvent que "
                   "« la semaine dernière ». Les deux se comprennent.",
              notes="Diapo à photographier. Faire produire une phrase par ligne, avec "
                    "une vraie absence de l'élève ou d'un proche.")

    d.regle("Du lundi au mercredi, ça fait trois journées",
            "du… au… : le premier et le dernier sont compris",
            precision="C'est la source d'erreur la plus fréquente du défi, et "
                      "elle se voit sur le billet : « du 3 au 5 mars » justifie "
                      "trois journées, pas deux.",
            notes="Diapo à photographier. Faire compter sur les doigts, au tableau, "
                  "trois fois avec des dates différentes. La règle s'oublie ; le geste "
                  "reste.")

    d.pratique('Écoute et réponds', "Le bon marqueur de temps",
               "Complétez à l'oral, puis par écrit.", [
        ("J'ai été absente la semaine ___ , à cause de la grippe.", "passée"),
        ("J'ai manqué le cours ___ , mais je suis là aujourd'hui.", "hier"),
        ("Le billet dit : « ___ 3 au 5 mars ».", "du"),
        ("Je suis malade ___ lundi : ça fait quatre jours.", "depuis"),
        ("Je n'ai pas pu venir ___ trois jours.", "pendant"),
        ("J'ai manqué lundi, mardi ___ mercredi.", "et"),
    ], corrige=True,
       notes="La quatrième et la cinquième sont le cœur de la séance. Faire justifier : "
             "est-ce que c'est fini, ou est-ce que ça continue ?")

    d.piege("Confondre depuis et pendant",
            "je suis malade pendant lundi",
            "je suis malade depuis lundi",
            "Depuis part d'un jour et arrive jusqu'à aujourd'hui : si vous dites "
            "« depuis lundi », vous êtes encore malade. Pendant compte une durée finie : "
            "« pendant trois jours », c'est terminé.",
            notes="La différence n'existe pas dans beaucoup de langues. Faire dessiner "
                  "les deux au tableau : une flèche qui s'arrête, une flèche qui arrive "
                  "à aujourd'hui.")

    d.cartes("La même absence, trois façons de la dire", "Toutes correctes", [
        ("Les journées, une par une",
         "« J'ai manqué lundi, mardi et mercredi. » C'est la plus utile au comptoir : "
         "la secrétaire écrit exactement ce que vous dites."),
        ("La période",
         "« J'ai été absente du lundi au mercredi. » C'est la formule du billet, celle "
         "qui est écrite sur le papier."),
        ("La durée",
         "« Je n'ai pas pu venir pendant trois jours. » Utile au téléphone, quand on ne "
         "se rappelle plus les dates exactes."),
    ], cols=3,
       notes="Faire choisir : laquelle diriez-vous au comptoir ? La première. Les deux "
             "autres servent, mais la secrétaire aura à redemander les dates.")

    d.pratique('Production orale', "Racontez une absence",
               "Trois phrases par élève, à tour de rôle.", [
        ("Les journées", "nommées une par une, dans l'ordre"),
        ("La raison", "une phrase courte avec parce que"),
        ("Le papier", "j'ai un billet, ou je n'en ai pas"),
        ("Le retour", "je suis revenu hier, je reviens aujourd'hui"),
    ], corrige=False,
       notes="Tour de table debout. Corriger une seule chose : la précision des dates. "
             "Le reste attendra.")

    d.billet(
        "Écrivez quatre phrases avec hier, la semaine passée, du… au… et depuis.",
        exemples=[
            "« J'ai manqué le cours du 3 au 5 mars. »",
            "« Je suis au centre depuis septembre. »",
        ],
        notes="Devoir d'écriture. « Depuis » sert bien au-delà des absences : depuis "
              "quand êtes-vous au Québec, au centre, dans ce logement.")

    return d.save(dossier)
