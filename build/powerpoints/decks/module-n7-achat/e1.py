# -*- coding: utf-8 -*-
"""E1 · Réclamez à voix haute
Bloc E « Je me lance » · couleur teal · jeu de rôle et production orale ·
75 min.
Source : bloc `appli` de `custom.js` — trois cas de jeu de rôle, huit sujets
à couvrir, production orale en trois temps.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Réclamez à voix haute",
        chapeau="Tout ce que le module a préparé tient dans quatre-vingt-dix "
                "secondes : le dossier, la panne en trois coordonnées, la "
                "garantie, la demande.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Prévoir que chacun parle deux fois : une fois "
                  "en jeu de rôle avec l'assistant, une fois seul pour "
                  "l'enregistrement. Garder trente minutes pour la seconde.")

    d.objectifs([
        "annoncer un dossier avec sa date et son montant, en deux phrases ;",
        "décrire un problème de fonctionnement en trois coordonnées ;",
        "nommer la garantie invoquée et démontrer qu'on était dedans ;",
        "formuler une demande précise et annoncer un délai.",
    ], notes="Ce sont les deux intentions orales de la situation, dans l'ordre où le "
             "programme les nomme. Le dire au groupe : ce n'est pas un exercice de "
             "plus, c'est la tâche du cours.")

    d.declencheur(
        'Mise en situation', "Par quoi commencez-vous, une fois devant le comptoir ?",
        pistes=[
            "Par ce qui vous est arrivé, ou par ce que vous voulez ?",
            "Par la date, ou par le problème ?",
            "Que se passe-t-il si vous commencez par « vous » ?",
            "Quelle phrase avez-vous préparée en C4 ?",
        ],
        notes="La quatrième question ramène le billet de C4. Les élèves qui l'ont gardé "
              "démarrent tout de suite ; les autres l'écrivent maintenant, en deux "
              "minutes.")

    d.tableau('Analyse', "Quatre-vingt-dix secondes, trois temps",
              ['Le temps', 'Ce qu\'on y dit'],
              [["1 · Le dossier", "la date, le bien, le montant"],
               ["2 · Le problème", "le symptôme, le moment, la fréquence"],
               ["3 · La garantie", "la catégorie, les dates, le kilométrage"],
               ["Puis la demande", "une seule, au conditionnel"],
               ["Et le délai", "avant vendredi, et ce qui suit"]],
              cle=0,
              notes="Diapositive à photographier, et à laisser affichée pendant tous "
                    "les enregistrements. Elle remplace la grille de correction.")

    d.cartes('Jeu de rôle', "Trois dossiers au choix", [
        ("La transmission qui cogne", "berline 2019, 11 400 $, catégorie C, 24 jours et 900 km"),
        ("La garantie qu'on n'a pas expliquée", "1 200 $ financés, aucune information sur la garantie légale"),
        ("La laveuse de quatorze mois", "1 150 $, garantie du fabricant expirée, durée raisonnable"),
    ], notes="Le troisième dossier n'est pas une auto : c'est voulu. Il montre que la "
             "garantie légale s'applique à tout bien, et que la garantie de bon "
             "fonctionnement, elle, ne vise que les véhicules.")

    d.cartes('Jeu de rôle', "Ce que l'assistant fera", [
        ("Il ouvrira par l'usure normale", "sans agressivité : c'est ce qu'on lui a appris"),
        ("Il ramènera à la garantie payée", "il en connaît les exclusions par cœur"),
        ("Il redemandera une date", "« récemment » ne lui suffira pas"),
        ("Il cédera devant un fait daté", "jamais devant un ton ni une accusation"),
    ], notes="Lire ces quatre cartes avant de lancer les postes. Un élève prévenu ne se "
             "décourage pas à la première réponse négative, et c'est là que la moitié "
             "du groupe abandonne d'habitude.")

    d.regle("On cède devant un fait daté, jamais devant un ton",
            "Hausser la voix ne fait pas avancer un dossier ; une date et un kilométrage, oui.",
            precision="C'est la même chose dans la vraie vie qu'avec l'assistant, et "
                      "c'est pour cela que le jeu de rôle sert. La personne au comptoir "
                      "traite vingt dossiers par jour : ce qui la fait bouger, c'est ce "
                      "qu'elle peut inscrire au dossier, pas ce qu'elle a ressenti.",
            notes="Diapositive à photographier. C'est aussi la réponse à la question "
                  "que quelqu'un posera : « et si je me fâche ? » On peut se fâcher — "
                  "après avoir donné les dates.")

    d.pratique('Production orale', "Préparez vos quatre phrases",
               "Écrivez-les, puis dites-les sans lire.", [
        ("Le dossier", "« J'ai acheté chez vous… le… au prix de… »"),
        ("Le problème", "« C'est un… , à… , systématiquement… »"),
        ("La garantie", "« L'étiquette dit… : la garantie courait jusqu'au… »"),
        ("La demande", "« Ce que je demande, c'est… Accepteriez-vous… ? »"),
    ], corrige=True,
       notes="Dix minutes d'écriture, puis chacun dit ses quatre phrases à son voisin "
             "sans regarder sa feuille. C'est le seul moyen d'arriver à "
             "l'enregistrement sans lire.")

    d.piege('Piège', "lire son texte pendant l'enregistrement",
            "écrire quatre repères plutôt que quatre phrases",
            "Une production orale lue s'entend tout de suite : le débit est plat, les "
            "hésitations disparaissent, et la rétroaction porte à faux. Quatre mots "
            "sur un papier — date, bruit, catégorie, demande — suffisent à tenir "
            "quatre-vingt-dix secondes.",
            notes="Faire tourner la feuille des quatre phrases face contre table avant "
                  "de lancer l'enregistrement. Le geste est symbolique et il marche.")

    d.billet(
        "Après le jeu de rôle : quelle phrase de l'assistant t'a le plus arrêté ?",
        exemples=[
            "Une phrase, et ce que tu as répondu.",
            "Ou ce que tu répondras la prochaine fois.",
        ],
        notes="Trois minutes. Presque tous écriront « c'est de l'usure normale ». Faire "
              "lire trois réponses à voix haute : elles font la meilleure révision "
              "possible avant E2.")

    return d.save(dossier)
