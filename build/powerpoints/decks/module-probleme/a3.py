# -*- coding: utf-8 -*-
"""A3 · Qui faut-il appeler ?
Bloc A · couleur teal · 60 min.
Source : mini-leçon `prPro`, exercice `prPro` (photos des métiers).
"""
from theme import Deck

IMG = '/Users/danieltousignant/Claude/bibliotheque-francisation/assets/interactive/module-probleme/images/'


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre='Qui faut-il appeler ?',
        chapeau="Vous n'êtes pas obligé de savoir réparer. Mais nommer le bon métier "
                "accélère tout : « le drain de la douche est bouché, ça prendrait un "
                "plombier » se règle beaucoup plus vite que « il y a un problème dans "
                "la salle de bain ».",
        duree='60 minutes')

    d.titre(notes="Séance de vocabulaire des métiers. Prévoir de projeter les photos du "
                  "module : le lien image-mot est beaucoup plus solide que la liste seule.")

    d.objectifs([
        "nommer les neuf professionnels qui interviennent dans un logement ;",
        "associer un problème au métier qui peut le régler ;",
        "dire ces noms de métier au masculin et au féminin ;",
        "savoir qui prévenir en premier — et ce n'est jamais le professionnel.",
    ])

    d.declencheur('Mise en route', "Le calorifère ne chauffe plus. Qui appelez-vous ?",
                  image=IMG + 'electricien.jpg',
                  pistes=[
                      "Un chauffagiste ? Un plombier ? Un électricien ?",
                      "Au Québec, les calorifères des logements sont électriques.",
                      "C'est donc un problème de circuit — un électricien.",
                      "Et surtout : à qui téléphonez-vous en premier ?",
                  ],
                  notes="Laisser le groupe se tromper. L'erreur « plombier » est très "
                        "fréquente, parce que dans beaucoup de pays le chauffage passe par "
                        "l'eau. Ici, il est électrique.")

    d.tableau('Les neuf métiers', "Retenez-les par ce qu'ils touchent",
              ['Ce que ça touche', 'La personne', 'Exemples'],
              [["Tout ce qui coule", "le plombier / la plombière",
                "tuyaux, robinets, drains"],
               ["Tout ce qui est électrique", "l'électricien / l'électricienne",
                "panneau, prises, calorifères"],
               ["Tout ce qui est en bois", "le menuisier / la menuisière",
                "portes, armoires, planchers"],
               ["Le toit", "le couvreur / la couvreuse",
                "toiture, infiltration"],
               ["Les serrures", "le serrurier / la serrurière",
                "clé perdue, serrure forcée"]],
              cle=1,
              note="Retenez la matière, pas le nom du problème : ce qui coule, ce qui est "
                   "électrique, ce qui est en bois.",
              notes="Lire une ligne à la fois, faire répéter les deux formes, demander un "
                    "exemple supplémentaire au groupe avant de passer à la suivante.")

    d.tableau('Les neuf métiers', "Et les quatre autres",
              ['Ce que ça touche', 'La personne', 'Exemples'],
              [["Les animaux nuisibles", "l'exterminateur / l'exterminatrice",
                "souris, fourmis, punaises"],
               ["La pose d'appareils", "l'installateur / l'installatrice",
                "électroménagers, ventilateur"],
               ["La peinture", "le peintre / la peintre",
                "murs et plafonds réparés"],
               ["L'immeuble au quotidien", "le concierge / la concierge",
                "parties communes, premier contact"]],
              cle=1,
              note="Deux exceptions : peintre et concierge ne changent pas de forme. Seul le "
                   "déterminant change — le peintre, la peintre ; le concierge, la concierge.",
              notes="Insister sur les deux exceptions : c'est exactement le genre de détail "
                    "qui fait hésiter au téléphone.")

    d.regle('Le masculin et le féminin',
            "La plupart de ces métiers ont deux formes ; deux n'en ont qu'une.",
            precision="Un plombier / une plombière · un électricien / une électricienne · "
                      "un menuisier / une menuisière · un serrurier / une serrurière · "
                      "un installateur / une installatrice · un exterminateur / une "
                      "exterminatrice · un couvreur / une couvreuse. Mais : le peintre / "
                      "la peintre, le concierge / la concierge.",
            notes="Faire lire la liste à voix haute par paires : un élève dit le masculin, "
                  "son voisin répond au féminin.")

    d.pratique('Pratique', 'Un problème, un métier',
               "Qui faut-il appeler pour chacun de ces problèmes ?", [
        ("Le drain de la douche est complètement bouché.", "un plombier"),
        ("Le disjoncteur du salon retombe chaque fois qu'on le remonte.", "un électricien"),
        ("La porte de la chambre a gonflé et ne ferme plus.", "un menuisier"),
        ("La clé tourne dans le vide depuis que la porte a été forcée.", "un serrurier"),
        ("Il y a des souris derrière la cuisinière.", "une exterminatrice"),
        ("L'eau de pluie traverse le toit et tache le plafond.", "un couvreur"),
    ], corrige=True,
       notes="Le quatrième cas piège : « la porte a été forcée » fait penser au menuisier, "
             "mais c'est la serrure qui est brisée, pas le bois.")

    d.piege('Choisir le métier',
            "La porte ne ferme plus : j'appelle le serrurier.",
            "La porte ne ferme plus : c'est un travail de menuisier.",
            "Une porte qui ne ferme plus, c'est presque toujours du bois qui a gonflé avec "
            "l'humidité — donc le menuisier. Le serrurier s'occupe du mécanisme : la clé, "
            "le cylindre, la serrure forcée. Si la clé tourne normalement mais que la porte "
            "coince, le problème est dans le bois.",
            notes="Faire trouver le critère au groupe : « est-ce que la clé fonctionne ? » "
                  "Si oui, c'est le bois.")

    d.cartes('Au téléphone', "Des phrases prêtes à dire", [
        ("Proposer sans imposer",
         "« Je pense que ça prendrait un plombier. » Vous suggérez, vous ne décidez pas "
         "à la place de la propriétaire."),
        ("Demander poliment",
         "« Est-ce que vous pouvez faire venir un électricien ? » La formule « faire venir » "
         "est celle qu'on emploie ici."),
        ("Situer la cause",
         "« Le problème vient de la toiture, il faudrait un couvreur. » Vous expliquez "
         "d'où vient le problème, pas seulement ce que vous voyez."),
        ("Préciser ce qui a déjà été fait",
         "« Le concierge est passé, mais il ne peut pas régler ça lui-même. » Cette phrase "
         "évite qu'on vous renvoie au concierge une deuxième fois."),
    ], notes="Faire répéter chaque phrase par le groupe entier. Elles sont réutilisables "
             "telles quelles, et elles reviendront au jeu de rôle de la séance E1.")

    d.regle('La règle qui prime sur toutes les autres',
            "Dans un logement loué, on ne choisit pas le professionnel soi-même.",
            precision="Vous signalez le problème ; c'est la personne propriétaire qui décide "
                      "et qui paie. Si vous engagez quelqu'un sans autorisation, elle n'est "
                      "pas obligée de vous rembourser — sauf en cas d'urgence réelle où vous "
                      "n'avez pas pu la joindre.",
            notes="Point important pour des adultes qui paient un loyer. Le répéter deux fois. "
                  "La séance B4 y reviendra en détail avec les recours.")

    d.pratique('Vérification', 'Quatre questions rapides',
               "Répondez sans regarder vos notes.", [
        ("Le calorifère du salon ne chauffe plus. Qui faut-il ?",
         "un électricien — les calorifères sont électriques"),
        ("L'eau de pluie tache le plafond du dernier étage. Qui faut-il ?",
         "un couvreur — le peintre viendra après"),
        ("Quelle forme est correcte : la peintre ou la peintresse ?",
         "la peintre — le mot ne change pas de forme"),
        ("Vous découvrez un dégât d'eau. Quelle est la première chose à faire ?",
         "prévenir la propriétaire ou le concierge"),
    ], corrige=True,
       notes="Si plus du tiers du groupe se trompe sur la première question, reprendre "
             "l'explication du chauffage électrique avant de terminer la séance.")

    d.billet(
        "Nommez un problème de votre logement et la personne qu'il faudrait faire venir.",
        exemples=[
            "En une phrase, avec la formule « il faudrait faire venir… ».",
            "Exemple : « Le drain de mon évier est bouché, il faudrait faire venir un plombier. »",
        ],
        notes="Ramasser les billets. Ceux qui nomment un professionnel impossible signalent "
              "un vocabulaire à revoir individuellement.")

    return d.save(dossier)
