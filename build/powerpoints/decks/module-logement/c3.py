# -*- coding: utf-8 -*-
"""C3 · Dire ce qu'on aime et ce qu'on craint.
Bloc C · couleur teal (écoute et réponds) · 60 min.
Source : dialogue `t2`, production orale du défi 2.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='teal',
        titre="Dire ce qu'on aime et ce qu'on craint",
        chapeau="Après trois visites, tous les logements se ressemblent. Les dire à voix "
                "haute à quelqu'un est la seule façon de savoir ce qu'on en pense "
                "vraiment.",
        duree='60 minutes')

    d.titre(notes="Séance de production orale. Rendre les billets de C1 et C2 : chacun a "
                  "sa liste et ses phrases emphatiques. Disposer la classe en dyades.")

    d.objectifs([
        "dire ce qui plaît et ce qui inquiète dans un logement ;",
        "employer la construction emphatique à l'oral ;",
        "proposer une solution au problème d'un autre ;",
        "prendre une décision et la justifier.",
    ])

    d.regle('La règle des cinq phrases',
            "Trois choses qui plaisent · deux qui inquiètent · une décision.",
            precision="C'est la conversation d'Ibrahim et Leyla, ramenée à son squelette. "
                      "Six phrases suffisent pour faire le tour d'un logement, et pour "
                      "que l'autre puisse vous aider.",
            notes="Écrire la structure au tableau. C'est le plan du jeu de rôle et il "
                  "tient en une ligne.")

    d.cartes('Le modèle', "Quatre façons de le dire", [
        ("Ce qui plaît",
         "« Ce qui m'a plu, c'est la chambre : elle donne sur la cour. » La chose, "
         "puis la raison en deux mots."),
        ("Ce qui inquiète",
         "« Ce que je crains, c'est le camion de farine. » Un seul mot d'inquiétude, "
         "sans exagérer."),
        ("Ce qu'on changerait",
         "« Ce que je changerais, c'est la couleur des murs. » Cela dit que le reste "
         "convient."),
        ("Ce qui décide",
         "« Ce qui me décide, c'est le prix. » Une seule chose décide vraiment : "
         "nommez-la."),
    ], notes="La quatrième carte est la plus difficile et la plus utile. Beaucoup de gens "
             "ne savent pas ce qui les décide avant de le dire à voix haute.")

    d.pratique('Pratique · 1 de 4', "Dites ce qui plaît",
               "La chose, puis la raison en deux mots.", [
        ("La chambre donne sur la cour.",
         "Ce qui m'a plu, c'est la chambre : elle donne sur la cour."),
        ("La cuisine reçoit le soleil le matin.",
         "Ce qui m'a plu, c'est la cuisine : elle est très claire."),
        ("Le loyer comprend le chauffage.",
         "Ce qui m'a plu, c'est le prix : le chauffage est inclus."),
        ("L'arrêt d'autobus est à deux minutes.",
         "Ce qui m'a plu, c'est l'emplacement : l'autobus passe tout près."),
    ], corrige=True,
       notes="Faire dire les quatre à voix haute, debout. La construction est plus facile "
             "à l'oral qu'à l'écrit : le signaler pour encourager.")

    d.pratique('Pratique · 2 de 4', "Dites ce qui inquiète",
               "Sans exagérer, et sans minimiser.", [
        ("Le camion de farine arrive à cinq heures.",
         "Ce que je crains, c'est le camion de farine, trois matins par semaine."),
        ("Il n'y a pas d'ascenseur et le logement est au troisième.",
         "Ce qui m'inquiète, c'est l'escalier : je suis au troisième."),
        ("Les électroménagers ne sont pas fournis.",
         "Ce qui me dérange, c'est qu'il faut acheter les électroménagers."),
        ("Le bail se termine le 30 juin.",
         "Ce qui m'ennuie, c'est le 1er juillet : tout le monde déménage ce jour-là."),
    ], corrige=True,
       notes="Faire varier les verbes : craindre, inquiéter, déranger, ennuyer. Ils ne "
             "disent pas la même force.")

    d.tableau('Analyse', "Quatre verbes, quatre forces",
              ['Le verbe', 'La force'],
              [["ce qui m'ennuie", "un petit inconvénient"],
               ["ce qui me dérange", "un vrai inconvénient"],
               ["ce qui m'inquiète", "un doute sérieux"],
               ["ce que je crains", "une vraie crainte"]],
              cle=0,
              note="Choisir le bon verbe évite deux erreurs : dramatiser un détail, ou "
                   "minimiser un vrai problème.",
              notes="Faire classer trois inquiétudes réelles du groupe selon ces quatre "
                    "verbes. La discussion est instructive.")

    d.piege("Le piège de l'exagération",
            "Ce que je crains, c'est la couleur des murs.",
            "Ce qui m'ennuie, c'est la couleur des murs.",
            "« Craindre » est un verbe fort : il annonce un vrai problème. L'employer "
            "pour une couleur de peinture fait perdre sa force à toutes vos autres "
            "phrases. Gardez les verbes forts pour ce qui compte.",
            notes="Faire relire les phrases de l'exercice précédent en vérifiant le "
                  "verbe. Plusieurs seront trop forts.")

    d.piege("Le piège du silence sur l'inquiétude",
            "Tout est parfait, je le prends.",
            "Ce qui m'inquiète, c'est l'escalier. Mais le reste me convient.",
            "Ne rien dire de ce qui inquiète empêche l'autre de vous aider. Leyla propose "
            "des rideaux parce qu'Ibrahim a nommé le camion. Sans cette phrase, il "
            "n'aurait rien obtenu.",
            notes="Point important : nommer un problème est ce qui permet de le régler. "
                  "C'est vrai bien au-delà du logement.")

    d.pratique('Pratique · 3 de 4', "Proposez une solution",
               "À l'inquiétude de votre partenaire.", [
        ("« Ce que je crains, c'est le bruit de la rue. »",
         "Mets des rideaux épais, ou demande une chambre sur la cour."),
        ("« Ce qui m'inquiète, c'est l'escalier au troisième. »",
         "Demande s'il y a un ascenseur dans un autre immeuble du propriétaire."),
        ("« Ce qui me dérange, c'est qu'il faut acheter les électroménagers. »",
         "Regarde les électroménagers d'occasion, ou négocie le premier mois."),
        ("« Ce qui m'ennuie, c'est la couleur des murs. »",
         "Demande si le propriétaire fournit la peinture."),
    ], corrige=True,
       notes="Faire proposer les solutions par le groupe avant d'afficher. Elles seront "
             "souvent meilleures que celles-ci.")

    d.pratique('Pratique · 4 de 4', "Jeu de rôle · la conversation",
               "À deux. L'un raconte sa visite, l'autre écoute et propose. Puis on échange.", [
        ("Vous racontez", "trois choses qui plaisent, deux qui inquiètent"),
        ("Votre partenaire propose", "une solution à chaque inquiétude"),
        ("Vous décidez", "« Ce qui me décide, c'est… »"),
        ("Vous justifiez", "en une phrase, avec « parce que »"),
    ], corrige=False,
       notes="Vingt minutes. Circuler et vérifier une seule chose : la construction "
             "emphatique est-elle employée ? C'est le critère de la séance.")

    d.billet(
        "Écrivez ce qui vous déciderait à prendre un logement.",
        exemples=[
            "Une seule chose : « Ce qui me déciderait, c'est… »",
            "Puis une phrase avec « parce que » pour l'expliquer.",
        ],
        notes="Ce billet prépare directement E1, où chacun choisira une annonce et "
              "écrira pourquoi.")

    return d.save(dossier)
