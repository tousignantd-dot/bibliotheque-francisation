# -*- coding: utf-8 -*-
"""B1 · « Deux voies sur trois »
Bloc B « Défi 1 · Ce qui bloque la route » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1a`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="« Deux voies sur trois »",
        chapeau="Six heures quarante-huit. Un accident vient de se produire "
                "sur l'autoroute 40, en direction ouest. Tereza et Amine ont "
                "trente secondes pour décider s'ils y vont ou non — et le "
                "bulletin ne décidera pas à leur place.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 1. Faire écouter le bulletin de six heures "
                  "quarante-huit une première fois sans consigne, puis demander ce qui a "
                  "été retenu. Écrire au tableau les quatre questions du bloc A : quoi, "
                  "où, dans quel sens, combien de temps. Réécouter avec elles sous les "
                  "yeux : la différence est spectaculaire et vaut mieux qu'un discours.")

    d.objectifs([
        "repérer les quatre informations d'une annonce entendue une seule fois ;",
        "comprendre ce que « deux voies sur trois » veut dire concrètement ;",
        "reconnaître le sens d'une entrave et savoir si elle nous concerne ;",
        "juger, à partir du bulletin, s'il vaut la peine d'attendre.",
    ], notes="Le quatrième objectif est celui qui fait la différence de niveau : le "
             "bulletin ne dit jamais quoi faire. C'est l'élève qui décide, avec ce qu'on "
             "lui a donné. Y consacrer les dix dernières minutes.")

    d.dialogue('Dialogue · 1 de 3', "L'annonce de six heures quarante-huit", [
        ("GAÉTAN", "Un accident vient de se produire sur l'autoroute 40 en "
                   "direction ouest, à la hauteur de la sortie Côte-de-Liesse. "
                   "Deux voies sur trois sont bloquées.", True),
        ("TEREZA", "Deux voies sur trois. Ça, je l'ai eu.", True),
        ("GAÉTAN", "Les remorqueuses sont sur place, les policiers dirigent la "
                   "circulation sur la voie de droite.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire relever les quatre informations une par une : accident, sur la 40 à "
             "la hauteur de Côte-de-Liesse, direction ouest, deux voies sur trois. "
             "Chronométrer : l'annonce dure douze secondes.")

    d.dialogue('Dialogue · 2 de 3', "Est-ce que ça nous concerne ?", [
        ("TEREZA", "Attends. Il a dit « en direction ouest ». Nous, on va vers "
                   "l'ouest.", True),
        ("AMINE", "Oui. Ça nous tombe dessus en plein.", True),
        ("TEREZA", "Et il a dit à quelle hauteur ? Côte-de-Liesse ?", True),
        ("AMINE", "Côte-de-Liesse. C'est avant Marcel-Laurin, donc c'est avant "
                  "notre sortie.", True),
    ], notes="Deux vérifications successives : le sens, puis la position par rapport à "
             "sa propre sortie. C'est exactement le raisonnement travaillé en C4. Le "
             "faire refaire à voix haute par deux élèves.")

    d.dialogue('Dialogue · 3 de 3', "Vingt minutes, ou soixante ?", [
        ("TEREZA", "Alors c'est pareil. Vingt minutes en haut, vingt minutes "
                   "en bas.", True),
        ("AMINE", "Pas tout à fait. En haut, tu ne sais pas si c'est vingt ou "
                  "soixante. Les remorqueuses viennent d'arriver.", True),
        ("TEREZA", "Ah. Ça, c'est une bonne raison. On passe en bas.", False),
    ], notes="La réplique d'Amine est le cœur de la séance : ce n'est pas la durée qui "
             "décide, c'est l'incertitude sur la durée. Faire reformuler par le groupe "
             "avant de passer à la règle.")

    d.regle("Le bulletin informe, il ne décide pas",
            "Il donne les faits. C'est vous qui choisissez de partir, "
            "d'attendre ou de changer de chemin.",
            precision="Une durée annoncée pendant un accident est une estimation, "
                      "pas un horaire. Une durée annoncée pour des travaux, oui.",
            notes="Diapositive à photographier. Elle distingue les deux familles "
                  "d'entraves, qui seront le sujet complet de la séance B4.")

    d.tableau('Une annonce', "Les quatre informations, dans l\'ordre",
              ['La question', 'La réponse entendue'],
              [["Quoi ?", "Un accident"],
               ["Où ?", "Sur la 40, à Côte-de-Liesse"],
               ["Dans quel sens ?", "En direction ouest"],
               ["Combien de voies ?", "Deux sur trois bloquées"]],
              cle=1,
              notes="Refaire ce tableau vide au tableau, puis le faire remplir à la "
                    "volée pendant une deuxième écoute. C'est la technique de prise de "
                    "notes travaillée en C4.")

    d.piege("Croire qu'on peut éviter l'accident en sortant plus tôt",
            "On sortira avant, ça ira.",
            "L'accident est avant notre sortie : il faut ne pas y entrer.",
            "Un accident situé avant votre sortie se traverse forcément si vous "
            "entrez sur l'autoroute. La seule façon de l'éviter est de ne pas y "
            "monter du tout.",
            notes="Dessiner l'autoroute au tableau avec les deux sorties : c'est un "
                  "raisonnement d'espace, il se comprend mieux dessiné.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le bulletin et la discussion.", [
        ("L'accident est en direction ouest.", "vrai"),
        ("Une seule voie sur trois est bloquée.", "faux — deux sur trois"),
        ("L'accident est à la hauteur de Côte-de-Liesse.", "vrai"),
        ("Sortir plus tôt permettrait de l'éviter.", "faux — il est avant leur sortie"),
        ("Les remorqueuses ont fini leur travail.", "faux — elles viennent d'arriver"),
        ("Ils décident de passer par le boulevard.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la réplique exacte. Les six items sont "
             "ceux de l'exercice `t1a` de l'activité interactive.")

    d.billet(
        "Écrivez l'annonce du bulletin en une seule phrase, avec les quatre informations.",
        exemples=[
            "Commencez par ce qui bloque, finissez par la durée.",
            "N'oubliez pas le sens : c'est la moitié de l'information.",
        ],
        notes="Ramasser les billets : ils préparent directement l'exercice `t1red` de la "
              "séance B4. Relever ceux où le sens manque, c'est l'oubli le plus courant.")

    return d.save(dossier)
