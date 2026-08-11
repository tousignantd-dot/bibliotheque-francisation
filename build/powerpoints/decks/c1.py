# -*- coding: utf-8 -*-
"""C1 · Samir monte au troisième.
Bloc C · couleur acier (compréhension orale) · 60 min.
Source : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck

IMG = '/Users/danieltousignant/Claude/bibliotheque-francisation/assets/interactive/module-probleme/images/'


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Samir monte au troisième',
        chapeau="Trois vélos dans le corridor, de la graisse sur le plancher, une porte "
                "qui n'ouvre plus au complet. Le concierge vient en parler au locataire "
                "du 3A — et l'affaire se règle sans lettre et sans conflit.",
        duree='60 minutes')

    d.titre(notes="Ouverture du bloc C : on passe du logement privé aux parties communes. "
                  "Faire remarquer le changement d'échelle — ici, le problème touche "
                  "plusieurs personnes à la fois.")

    d.objectifs([
        "comprendre une conversation entre un concierge et un locataire ;",
        "savoir ce qu'est une partie commune et ce qu'on n'a pas le droit d'y faire ;",
        "reconnaître une négociation réussie : chacun obtient quelque chose ;",
        "employer le vocabulaire de l'immeuble : encombrer, sortie de secours, case.",
    ])

    d.declencheur('Avant d\'écouter', "À qui appartient le corridor ?",
                  image=IMG + 'ordures.jpg',
                  pistes=[
                      "Est-ce que je peux laisser mes affaires devant ma porte ?",
                      "Et si personne ne s'en plaint, est-ce que c'est permis ?",
                      "Qui décide de ce qu'on met dans un corridor ?",
                      "Pourquoi un corridor doit-il rester libre ?",
                  ],
                  notes="Question volontairement ouverte. La réponse — c'est une partie "
                        "commune et une sortie de secours — arrive avec le dialogue. "
                        "Ne pas la donner tout de suite.")

    d.dialogue('Dialogue · 1 de 4', "Le concierge ouvre la conversation", [
        ("SAMIR", "Jean-Philippe, je peux vous parler deux minutes ? C'est au sujet du corridor du troisième.", True),
        ("JEAN-PHILIPPE", "Mes vélos, je suppose. Il y en a trois, je sais. Mais mon logement fait deux pièces et demie, je n'ai aucun rangement.", False),
        ("SAMIR", "Je comprends très bien. Seulement, ce n'est plus une question de place. Les voisins du 3B se plaignent depuis un mois : il y a de la graisse sur le plancher et leurs enfants marchent dedans.", True),
    ], consigne="Écoutez d'abord, diapo masquée. Repérez comment Samir commence.",
       notes="Faire remarquer les deux premières phrases de Samir : « je peux vous parler "
             "deux minutes ? » puis « je comprends très bien ». Il ouvre et il reconnaît "
             "le point de vue de l'autre AVANT d'exposer le problème. C'est la clé de "
             "toute la conversation.")

    d.dialogue('Dialogue · 2 de 4', "Les faits, un par un", [
        ("JEAN-PHILIPPE", "De la graisse ? Je fais pourtant mes réparations sur un grand carton.", False),
        ("SAMIR", "Le carton glisse quand on ouvre la porte. Et depuis que vous avez ajouté le troisième vélo, la porte du local à ordures n'ouvre plus au complet.", True),
        ("JEAN-PHILIPPE", "Ah ça, je ne l'avais pas remarqué. Vous savez, ces vélos-là, c'est mon gagne-pain : je les répare le soir et je les revends.", False),
    ], notes="« Depuis que vous avez ajouté le troisième vélo » — c'est exactement la "
             "structure de la séance B3. Le signaler au passage : le groupe la reconnaît "
             "maintenant.")

    d.dialogue('Dialogue · 3 de 4', "La règle, énoncée sans accuser", [
        ("SAMIR", "Personne ne vous demande d'arrêter. Mais avant d'occuper une partie commune, il faut me le demander : ce corridor est une sortie de secours, je dois le garder libre.", True),
        ("JEAN-PHILIPPE", "Qu'est-ce que vous proposez, d'abord ?", False),
        ("SAMIR", "Il reste deux cases vides au sous-sol. Je peux vous en faire attribuer une par la propriétaire, sans frais, si vous descendez vos vélos avant vendredi.", True),
    ], notes="Deux structures de ce bloc apparaissent ici : « avant d'occuper » (séance C2) "
             "et « faire attribuer par » (séance C3). Les nommer sans les enseigner encore.")

    d.dialogue('Dialogue · 4 de 4', "L'entente", [
        ("JEAN-PHILIPPE", "Et pour les taches sur le plancher ?", False),
        ("SAMIR", "Après avoir descendu les vélos, vous lavez le plancher avec un dégraissant. Sinon, je vais devoir le faire nettoyer par la compagnie d'entretien, et là, c'est facturé au locataire.", True),
        ("JEAN-PHILIPPE", "Bon. Je fais ça jeudi soir en revenant de l'atelier. Merci d'être venu m'en parler au lieu d'écrire une lettre.", True),
    ], notes="La dernière réplique est le vrai enseignement de la séance : parler d'abord "
             "évite l'escalade. Relier aux trois marches de la séance B4.")

    d.cartes('Analyse', "Pourquoi cette conversation fonctionne", [
        ("Samir reconnaît le point de vue de l'autre",
         "« Je comprends très bien. » Il ne commence pas par la règle : il commence par "
         "montrer qu'il a entendu le problème de logement de Jean-Philippe."),
        ("Il donne des faits, pas des jugements",
         "De la graisse sur le plancher, des enfants qui marchent dedans, une porte qui "
         "n'ouvre plus. Il ne dit jamais « vous êtes désordonné »."),
        ("Il propose une solution concrète",
         "Une case au sous-sol, sans frais, avec une date. La solution vient avec la "
         "demande — ce n'est pas un simple reproche."),
        ("Il annonce la conséquence, sans menacer",
         "« Sinon, c'est facturé au locataire. » C'est une information, dite calmement, "
         "pas un chantage."),
    ], notes="Ces quatre points structurent aussi la séance D2. Y revenir alors.")

    d.regle('La notion clé',
            "Une partie commune n'appartient à personne en particulier — et un corridor est aussi une sortie de secours.",
            precision="Corridors, escaliers, entrées, local à ordures, stationnement, "
                      "buanderie : ce sont des espaces partagés. On n'y range rien sans "
                      "demander. La raison n'est pas seulement la politesse : en cas "
                      "d'incendie, ces espaces doivent rester libres.",
            notes="Point de sécurité. Le dire clairement : c'est une obligation légale, "
                  "pas une préférence du concierge.")

    d.pratique('Pratique', 'Vrai ou faux',
               "Écoutez de nouveau le dialogue, puis répondez.", [
        ("Jean-Philippe garde quatre vélos dans le corridor.", "FAUX — trois"),
        ("Son logement est trop petit pour ranger ses vélos.", "VRAI — deux pièces et demie"),
        ("Les voisins se plaignent depuis une semaine.", "FAUX — depuis un mois"),
        ("Jean-Philippe travaille sur un carton pour protéger le plancher.", "VRAI"),
    ], corrige=True)

    d.pratique('Pratique', 'Suite',
               "Même consigne.", [
        ("Le corridor sert aussi de sortie de secours.", "VRAI"),
        ("Samir exige que Jean-Philippe cesse de réparer des vélos.", "FAUX — « personne ne vous demande d'arrêter »"),
        ("La case au sous-sol sera louée trente dollars par mois.", "FAUX — sans frais"),
        ("Si le plancher n'est pas lavé, le nettoyage sera facturé au locataire.", "VRAI"),
    ], corrige=True,
       notes="Le sixième énoncé est celui qui trompe le plus : le groupe entend un reproche "
             "et conclut à une interdiction. Faire relire la réplique.")

    d.vocabulaire('Vocabulaire', "Les mots de l'immeuble", [
        ("une partie commune", "Un espace de l'immeuble partagé par tous les locataires."),
        ("encombrer", "Occuper une place et gêner le passage."),
        ("une sortie de secours", "Le chemin à garder libre pour évacuer en cas d'incendie."),
        ("une case", "Un espace de rangement attribué à un logement, souvent au sous-sol."),
        ("un dégraissant", "Un produit fort qui enlève l'huile et la graisse."),
        ("le gagne-pain", "Ce qui permet à quelqu'un de gagner sa vie."),
    ], notes="« Gagne-pain » est une expression imagée : le faire deviner avant de donner "
             "la définition.")

    d.billet(
        "Nommez une partie commune de votre immeuble et un problème qu'on y trouve.",
        exemples=[
            "En une phrase, avec un fait précis — pas un jugement sur une personne.",
            "Exemple : « Dans la buanderie, les machines restent pleines toute la journée. »",
        ],
        notes="Ces billets alimentent la séance C2 et surtout la séance D1, où on classera "
              "les situations inacceptables.")

    return d.save(dossier)
