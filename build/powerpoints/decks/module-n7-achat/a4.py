# -*- coding: utf-8 -*-
"""A4 · L'étiquette et le contrat, ligne par ligne
Bloc A « Je découvre » · couleur teal · compréhension écrite · 75 min.
Source : exercice `prEtiq` (type `texte`, treize passages cliquables) et sa
mini-leçon ; exercice `prImg`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre="L'étiquette et le contrat, ligne par ligne",
        chapeau="Deux documents, quatre chiffres. Le reste peut se lire plus "
                "tard ; ces quatre-là se lisent avant de signer.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. Deux documents à l'écran, et l'exercice "
                  "du module met les questions à côté du texte. Prévoir que chacun "
                  "l'ouvre sur son poste après la première demi-heure.")

    d.objectifs([
        "trouver la catégorie d'une auto d'occasion sur son étiquette ;",
        "dire ce que la catégorie annonce sur la durée de la garantie ;",
        "relever dans un contrat le taux, les frais et l'obligation totale ;",
        "repérer un usage antérieur particulier du véhicule.",
    ], notes="Le deuxième objectif est celui qui prépare tout le bloc C. Il ne sera "
             "compris qu'à moitié aujourd'hui, et c'est normal : la table des "
             "catégories revient en C2.")

    d.declencheur(
        'Observation', "Que regardez-vous en premier sur une auto à vendre ?",
        pistes=[
            "Le prix ? L'année ? Le kilométrage ? La couleur ?",
            "Saviez-vous qu'un papier obligatoire est collé dans la vitre ?",
            "Qu'est-ce qui pourrait y être écrit et que le vendeur ne dira pas ?",
            "Le papier reste-t-il au commerçant, ou vous appartient-il ?",
        ],
        notes="La quatrième question est la bonne surprise de la séance : l'étiquette "
              "est remise à l'acheteur et elle fait partie du contrat. Presque personne "
              "ne le sait.")

    d.tableau('Analyse', "Ce que l'étiquette doit dire",
              ['La ligne', 'Pourquoi elle y est'],
              [["Année et description", "elle décide de la catégorie avec le kilométrage"],
               ["Kilométrage réel", "s'il diffère de l'odomètre, le compteur a bougé"],
               ["Catégorie", "elle donne la durée de la garantie"],
               ["Usages antérieurs", "taxi, école de conduite, location, police"],
               ["Réparations faites", "ce que le commerçant a touché ; le reste, non"],
               ["Dernier propriétaire", "on peut en obtenir le nom sur demande"]],
              cle=0,
              notes="Diapositive à photographier. Six rangées, pas de note en plus : "
                    "elle se lit de loin telle quelle. C'est le document le plus utile "
                    "du terrain et le moins lu.")

    d.regle("Tout ce qui est écrit sur l'étiquette fait partie du contrat",
            "Sauf le prix et les caractéristiques de la garantie, qui peuvent être modifiés.",
            precision="Cela veut dire qu'une mention inexacte engage le commerçant, et "
                      "qu'une mention absente — un usage de location tu, par exemple — "
                      "est un manquement. C'est aussi la raison de la garder : sans "
                      "elle, prouver la catégorie six semaines plus tard demande de "
                      "faire ressortir le dossier du commerce.",
            notes="Diapositive à photographier. Dire de la ranger avec le contrat, dans "
                  "la même enveloppe, le jour même. C'est un geste de trente secondes.")

    d.pratique('Compréhension', "Cherchez dans l'étiquette",
               "Une réponse par ligne, en citant le document.", [
        ("De quelle année est le véhicule ?", "2019"),
        ("Combien de kilomètres à l'odomètre ?", "104 216 km, et le kilométrage réel est identique"),
        ("À quelle catégorie appartient-il ?", "catégorie C : sept ans ou moins, au plus 120 000 km"),
        ("A-t-il déjà servi à autre chose ?", "voiture de location à court terme, de 2019 à 2021"),
        ("Qu'a réparé le commerçant ?", "les quatre plaquettes de frein et la batterie"),
        ("Peut-on savoir qui le possédait avant ?", "oui, sur demande, avec son numéro de téléphone"),
    ], corrige=True,
       notes="Faire lire la ligne exacte à voix haute avant de donner la réponse. "
             "L'exercice du module fait cliquer dans le document : c'est le même geste, "
             "et il vaut mieux l'avoir fait une fois au tableau.")

    d.pratique('Compréhension', "Cherchez dans le contrat",
               "Une réponse par ligne, avec le montant.", [
        ("Combien a-t-elle versé comptant ?", "2 000,00 $"),
        ("Qu'est-ce qui s'ajoute au capital net ?", "une garantie supplémentaire de 1 200,00 $"),
        ("Quel est le taux de crédit ?", "9,45 % par année, fixe pour toute la durée"),
        ("À combien s'élèvent les frais de crédit ?", "2 741,60 $"),
        ("Combien de versements, et de quel montant ?", "soixante versements de 222,36 $"),
        ("Quelle est l'obligation totale ?", "13 341,60 $"),
    ], corrige=True,
       notes="Terminer par la question ouverte : pour 11 400 $ d'auto, combien sortira "
             "du compte en tout ? Treize mille trois cent quarante et un, plus les deux "
             "mille d'acompte. Le groupe fait le calcul lui-même.")

    d.cartes('Image', "Les cinq lieux du dossier d'Ernestine", [
        ("Le bureau de vente", "un petit bureau vitré au fond d'une salle de montre"),
        ("L'entrée de la maison", "la berline grise stationnée devant le bungalow"),
        ("L'atelier", "une auto levée sur un pont élévateur"),
        ("Le comptoir du service", "haut, avec deux tabourets vides devant"),
        ("La table de cuisine", "le soir, un portable et une pile de papiers"),
    ], notes="Les cinq photos sont dans le module, à associer à leur phrase. Les "
             "projeter ici sert à installer le décor du dossier avant le bloc B.")

    d.billet(
        "Tu achètes une auto de six ans avec 90 000 kilomètres. De quelle catégorie est-elle ?",
        exemples=[
            "Regarde le tableau : deux conditions, toutes les deux à respecter.",
            "Une lettre suffit.",
        ],
        notes="Deux minutes. La réponse est C : six ans dépasse les cinq ans de B. "
              "Corriger tout de suite, et annoncer que la table complète revient en C2.")

    return d.save(dossier)
