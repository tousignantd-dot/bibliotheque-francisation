# -*- coding: utf-8 -*-
"""D1 · La réclamation : qui paie quoi.
Bloc D « Défi 3 · La réclamation » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3a` et `t3qui`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-degat/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="La réclamation : qui paie quoi",
        chapeau="Deux assurances, deux démarches, et une réduction de loyer "
                "qui ne relève ni de l'une ni de l'autre. Se tromper de porte "
                "coûte des semaines.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 3. Demander d'abord qui, dans le groupe, a une "
                  "assurance habitation. Au Québec, un locataire sur trois n'en a pas — "
                  "et la séance prend un autre sens selon la réponse.")

    d.objectifs([
        "distinguer ce que couvre chaque assurance ;",
        "comprendre à quoi sert une franchise ;",
        "savoir à qui s'adresser selon la situation ;",
        "connaître l'ordre des étapes si rien ne bouge.",
    ])

    d.declencheur(
        'Mise en situation', "Votre matelas est trempé et votre plafond est taché. "
                             "Vous appelez qui, pour quoi ?",
        image=IMG + 'assecheur-chambre.jpg',
        pistes=[
            "Le plafond, c'est à qui ?",
            "Le matelas, c'est à qui ?",
            "Et les trois nuits sur le divan ?",
            "Est-ce que ça se demande à la même personne ?",
        ],
        notes="Presque personne ne sépare spontanément les trois. C'est exactement le "
              "contenu de la séance : trois choses, trois portes.")

    d.dialogue('Dialogue · 1 de 3', "Raconter dans l'ordre", [
        ("SYLVIE", "Assurances Bellerive, Sylvie Painchaud à l'appareil.", True),
        ("MARIAMA", "Bonjour. Je voudrais ouvrir une réclamation. J'ai eu un "
                    "dégât d'eau chez moi le 10 novembre.", True),
        ("SYLVIE", "Je vous écoute. Racontez-moi ce qui est arrivé, dans l'ordre.", True),
        ("MARIAMA", "Le chauffe-eau du logement du dessus a lâché pendant la "
                    "nuit. Quand je me suis levée, l'eau coulait du plafond.", False),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="« Dans l'ordre » : c'est tout le défi 1 qui revient. Faire remarquer que "
             "Mariama emploie l'imparfait et le passé composé sans y penser.")

    d.dialogue('Dialogue · 2 de 3', "Ce qui vous appartient", [
        ("SYLVIE", "Maintenant, ce qui est endommagé chez vous : qu'est-ce qui "
                   "vous appartient ?", True),
        ("MARIAMA", "Ce qui m'appartient, c'est le matelas, une commode et une "
                    "boîte de documents. Le plafond et le plancher, eux, "
                    "appartiennent à l'immeuble.", True),
        ("SYLVIE", "Exactement. Le bâtiment, c'est l'assurance du propriétaire ; "
                   "vos biens, c'est la vôtre. Vous avez des photos ?", True),
        ("MARIAMA", "J'en ai vingt-deux, prises le matin même, avec la date. Et "
                    "j'ai gardé le matelas : je ne l'ai pas jeté.", True),
    ], notes="« Ce qui m'appartient, c'est… » est une phrase emphatique : elle sera le "
             "point de grammaire de D2. La signaler en passant.")

    d.dialogue('Dialogue · 3 de 3', "La franchise, et ce qui n'en relève pas", [
        ("MARIAMA", "Il y a une franchise, je pense ?", True),
        ("SYLVIE", "Cinq cents dollars à votre contrat. En dessous de ce "
                   "montant-là, ça ne vaut pas la peine de réclamer.", True),
        ("MARIAMA", "Et pour les trois nuits où je n'ai pas pu dormir dans ma "
                    "chambre ?", True),
        ("SYLVIE", "Ça, c'est une autre démarche : c'est au propriétaire que "
                   "vous demandez une réduction de loyer, par écrit.", True),
    ], notes="La dernière réplique est la charnière du module : elle envoie vers la "
             "lettre de D2 et la production écrite de E2.")

    d.regle("Deux assurances, deux périmètres",
            "Le bâtiment est au propriétaire ; vos biens sont à vous.",
            precision="Le plafond, le plancher, les murs et la plomberie relèvent de "
                      "l'assurance du propriétaire : c'est lui qui fait la démarche et "
                      "lui qui fait réparer. Le matelas, les meubles, les vêtements et "
                      "les papiers relèvent de la vôtre. Faire cette séparation dès le "
                      "premier appel évite d'être renvoyé d'une porte à l'autre pendant "
                      "deux semaines.",
            notes="Diapositive à photographier. Elle a déjà été annoncée en A4 : la "
                  "reprendre ici avec les mots de l'assurance.")

    d.tableau('La franchise', "Le montant qui reste à votre charge",
              ['La situation', 'Ce qu\'il faut en conclure'],
              [["franchise de 500 $, perte de 300 $", "on ne réclame pas"],
               ["franchise de 500 $, perte de 1 400 $", "on réclame, et on reçoit 900 $"],
               ["plusieurs petites réclamations", "elles restent au dossier, et la prime monte"],
               ["le doute", "on appelle et on demande sans ouvrir de dossier"]],
              cle=0,
              note="Un assureur répond volontiers à une question sans ouvrir de dossier.",
              notes="La dernière ligne est utile et peu connue : on peut téléphoner pour "
                    "savoir, sans que ça compte comme une réclamation.")

    d.pratique('Pratique · exercice t3qui', "À qui s'adresse-t-on ?",
               "Pour chaque situation, la bonne démarche.",
               [("Le plafond est taché et le plancher gondole.",
                 "j'avertis le propriétaire"),
                ("Mon matelas et ma commode sont abîmés.",
                 "j'ouvre une réclamation à mon assureur"),
                ("Je n'ai pas pu coucher dans ma chambre pendant trois nuits.",
                 "je demande une réduction de loyer, par écrit"),
                ("Le propriétaire ne répond pas depuis trois semaines.",
                 "je lui envoie une mise en demeure"),
                ("La mise en demeure est restée sans réponse.",
                 "je dépose une demande au Tribunal administratif du logement"),
                ("L'eau coule maintenant et personne ne répond.",
                 "j'appelle un plombier d'urgence et je garde la facture")],
               corrige=True, cols=1,
               notes="Les deux dernières lignes forment l'escalier des recours. Le "
                     "dessiner au tableau : lettre, mise en demeure, Tribunal.")

    d.piege("Jeter avant de faire constater",
            "Le matelas était fini, je l'ai mis au chemin.",
            "Je l'ai sorti de la chambre et je l'ai gardé.",
            "C'est la première cause de refus d'une réclamation. Un bien jeté est un bien "
            "qui n'a jamais existé du point de vue du dossier. Personne ne vous demande "
            "de dormir à côté : on le sort de la pièce, on le met sur le balcon ou dans "
            "la remise, et on attend le passage de l'expert.",
            notes="Répétition volontaire de la règle de A1. Elle vaut d'être dite deux "
                  "fois : c'est celle qui coûte le plus cher quand elle est ignorée.")

    d.billet(
        "Trois lignes : ce qui est au propriétaire, ce qui est à vous, ce qui se demande.",
        exemples=[
            "« Le plafond et le plancher : au propriétaire. »",
            "« Le matelas : à moi. Les trois nuits : une réduction de loyer. »",
        ],
        notes="Deux minutes. C'est la vérification la plus utile de la séance.")

    return d.save(dossier)
