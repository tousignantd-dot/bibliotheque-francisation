# -*- coding: utf-8 -*-
"""C4 · Les cinq niveaux, et les mots qu'on entend sans les comprendre.
Bloc C « Défi 2 » · couleur acier · 75 min.
Source : exercices `t2triage` et `t2mots`, et la mini-leçon du triage.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-urgence/images/')


def build(dossier):
    d = Deck(
        code='C4', section='acier',
        titre="Les cinq niveaux, et l'attente",
        chapeau="Toutes les urgences du Québec emploient la même échelle : "
                "cinq niveaux, du plus pressant au moins pressant. La "
                "comprendre change complètement une nuit d'attente.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 2. Relire deux billets de C3, puis annoncer "
                  "que la séance porte enfin sur les questions qu'on ose poser soi-même.")

    d.objectifs([
        "expliquer ce qu'est un niveau de priorité ;",
        "poser la bonne question pendant l'attente ;",
        "demander une réévaluation si l'état empire ;",
        "employer les mots du triage dans une phrase juste.",
    ])

    d.declencheur(
        'Situation', "Deux heures d'attente. Une personne arrivée après vous vient "
                     "d'entrer. Vous faites quoi ?",
        image=IMG + 'triage.jpg',
        pistes=[
            "Est-ce un oubli ? Une erreur ? Une injustice ?",
            "Qu'est-ce qui décide de l'ordre ?",
            "Quelle question peut-on poser au comptoir ?",
            "Qu'est-ce qui n'a jamais de réponse ?",
        ],
        notes="Laisser la colère s'exprimer : elle est légitime et très répandue. Puis "
              "donner l'explication. Le soulagement dans le groupe est visible.")

    d.tableau('Les cinq niveaux', "L'échelle canadienne de triage, appliquée partout au Québec",
              ['Niveau', 'Ce que ça veut dire', 'Un exemple'],
              [["1 · réanimation", "la vie est en danger", "on ne respire plus"],
               ["2 · très urgent", "une atteinte grave est possible",
                "une douleur à la poitrine"],
               ["3 · urgent", "l'état peut se dégrader", "une fracture possible"],
               ["4 · moins urgent", "il faut un médecin, mais ça tient",
                "une coupure à recoudre"],
               ["5 · non urgent", "cela peut attendre longtemps", "un mal de gorge"]],
              cle=0,
              note="Le triage dure moins de cinq minutes.",
              notes="Faire remarquer le niveau 5 : c'est exactement l'appel que le 8-1-1 "
                    "aurait réglé au téléphone, gratuitement. La boucle avec A4 se ferme "
                    "ici.")

    d.regle("Un niveau 4 ou 5 est une bonne nouvelle",
            "Cela veut dire que rien ne menace de s'aggraver pendant l'attente.",
            precision="Beaucoup de gens vivent un niveau élevé comme un mépris. C'est "
                      "l'inverse : le personnel vous dit que votre état est stable.",
            notes="Diapositive à photographier. Elle désamorce une frustration réelle et "
                  "évite des départs prématurés de la salle d'attente.")

    d.cartes("Ce qu'on peut demander, et ce qu'on ne peut pas", "Deux questions, deux réponses", [
        ("« Quel niveau a-t-elle reçu ? »",
         "Se répond, et donne une idée de la suite."),
        ("« Qu'est-ce qui est prévu ? »",
         "Se répond : radiographie, prise de sang, médecin."),
        ("« Dans combien de temps exactement ? »",
         "Ne se répond pas : une seule ambulance peut tout changer."),
        ("« Sa douleur a beaucoup augmenté. »",
         "Ce n'est pas une question, et c'est la phrase la plus utile de la nuit."),
    ], notes="La quatrième carte est le cœur de la séance : signaler une aggravation "
             "n'est pas se plaindre, c'est donner une information clinique.")

    d.piege("Attendre en silence pour ne pas déranger",
            "Ça fait deux heures qu'elle a plus mal, mais je ne veux pas déranger.",
            "Sa douleur a beaucoup augmenté, est-ce que vous pouvez la revoir ?",
            "Le triage n'est pas une décision définitive : on peut réévaluer et reclasser. "
            "Personne ne le fera si personne ne le dit.",
            notes="Insister. C'est le conseil qui a le plus d'effet réel dans une vraie "
                  "salle d'attente.")

    d.piege("Partir sans prévenir",
            "On s'en va, ça sert à rien.",
            "Nous partons — pouvez-vous nous retirer de la liste ?",
            "Sinon, on vous appellera, puis on vous cherchera, et le nom reste au tableau "
            "pendant des heures. Trente secondes au comptoir évitent tout cela.",
            notes="Le dire sans juger : partir est parfois raisonnable. Ce qui ne l'est "
                  "pas, c'est de partir en silence.")

    d.pratique('Emploi', "Le mot juste",
               "Complétez chaque phrase avec un mot du module.", [
        ("Au ___, une infirmière écoute votre récit et donne un niveau de priorité.", "triage"),
        ("Les ___ ont installé Amparo sur une civière.", "ambulanciers"),
        ("L'infirmière prend les ___ ___ avant ses questions.", "signes vitaux"),
        ("La ___ de la hanche a montré une fracture.", "radiographie"),
        ("Le ___ répond au 9-1-1 et envoie les secours.", "répartiteur"),
        ("Sa mère a reçu un niveau de ___ de trois.", "priorité"),
        ("Elle n'a pas ___ connaissance.", "perdu"),
        ("Il faut apporter la carte d'___ ___ et la liste des médicaments.", "assurance maladie"),
    ], corrige=True,
       notes="Exercice de fin de bloc : il reprend le vocabulaire de A3 dans le contexte "
             "où il sert vraiment.")

    d.billet(
        "Écrivez les trois phrases que vous diriez au comptoir du triage, à trois moments.",
        exemples=[
            "En arrivant · après une heure d'attente · si l'état empire.",
            "Une phrase chacune, polie et factuelle.",
        ],
        notes="Fin du bloc C. Annoncer le bloc D : l'urgence est finie, l'hospitalisation "
              "commence, et il faudra donner des nouvelles à ceux qui ne savent rien.")

    return d.save(dossier)
