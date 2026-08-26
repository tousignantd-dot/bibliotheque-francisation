# -*- coding: utf-8 -*-
"""C4 · Le bail et le 1er juillet.
Bloc C · couleur framboise (vocabulaire) · 60 min.
Source : savoir culturel du défi 2, vocabulaire du contrat de location.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='framboise',
        titre='Le bail et le 1er juillet',
        chapeau="Douze mois, une signature, et une date que tout le Québec connaît. Le "
                "bail est le document le plus engageant qu'un locataire signe — et "
                "presque personne ne le lit.",
        duree='60 minutes')

    d.titre(notes="Apporter un vrai formulaire de bail si possible : celui du Tribunal "
                  "administratif du logement est public et gratuit. Le manipuler change "
                  "tout.")

    d.objectifs([
        "nommer les parties d'un bail ;",
        "comprendre ce qu'on signe et pour combien de temps ;",
        "connaître la tradition du 1er juillet et ses conséquences ;",
        "savoir ce qu'il faut vérifier avant de signer.",
    ])

    d.tableau('Analyse', "Ce qu'un bail contient",
              ['La partie', 'Ce qu\'elle dit'],
              [["les parties", "le nom du propriétaire et celui du locataire"],
               ["le logement", "l'adresse, le numéro, le nombre de pièces"],
               ["la durée", "la date de début et la date de fin"],
               ["le loyer", "le montant, et la date de paiement chaque mois"],
               ["les inclusions", "chauffage, électricité, stationnement, électros"],
               ["les règlements", "animaux, fumée, bruit, sous-location"]],
              cle=0, props=[0.28, 0.72],
              notes="Six parties. Faire chercher chacune dans le vrai formulaire si vous "
                    "en avez un.")

    d.regle('La règle du bail',
            "Ce qui n'est pas écrit dans le bail n'existe pas.",
            precision="Une promesse faite pendant la visite — « je repeindrai le "
                      "salon », « le stationnement est à vous » — n'engage à rien si "
                      "elle n'est pas dans le bail. Faites-la ajouter avant de signer.",
            notes="Diapo centrale de la séance. C'est un savoir juridique simple et il "
                  "évite des mois de discussions.")

    d.cartes('Ouvrir la mini-leçon', "Le 1er juillet au Québec", [
        ("Une tradition",
         "La plupart des baux se terminent le 30 juin. Le 1er juillet, des milliers de "
         "ménages déménagent le même jour, partout dans la province."),
        ("Les conséquences pratiques",
         "Les camions de location se réservent des mois d'avance. Les déménageurs "
         "coûtent plus cher ce jour-là. Les rues sont pleines de meubles."),
        ("D'autres dates existent",
         "Le bail d'Ibrahim commence le 1er septembre. C'est fréquent dans une ville "
         "universitaire comme Sherbrooke."),
        ("Le bail se renouvelle tout seul",
         "Si personne ne dit rien, le bail se renouvelle automatiquement pour un an. "
         "Pour partir, il faut envoyer un avis écrit, plusieurs mois à l'avance."),
    ], notes="La quatrième carte est celle que personne ne connaît et qui coûte le plus "
             "cher. La souligner.")

    d.vocabulaire('Vocabulaire · 1 de 2', "Le contrat", [
        ("un bail", "Le contrat de location signé entre le locataire et le propriétaire."),
        ("signer un bail", "S'engager à louer pour la durée prévue."),
        ("renouveler un bail", "Le prolonger pour une nouvelle période."),
        ("résilier un bail", "Y mettre fin avant la date prévue."),
        ("un avis écrit", "Une lettre officielle envoyée dans un délai prévu."),
        ("sous-louer", "Laisser quelqu'un d'autre habiter le logement à sa place."),
    ], notes="« Résilier » et « sous-louer » sont les deux mots du départ. Les faire "
             "prononcer et écrire.")

    d.vocabulaire('Vocabulaire · 2 de 2', "Le déménagement", [
        ("emménager", "S'installer dans un nouveau logement."),
        ("déménager", "Quitter un logement pour aller dans un autre."),
        ("l'état des lieux", "La description du logement au début du bail."),
        ("un dépôt", "Une somme demandée d'avance — interdite au Québec, sauf le premier mois."),
        ("le Tribunal administratif du logement", "L'organisme qui règle les conflits entre locataire et propriétaire."),
    ], notes="Le mot « dépôt » mérite une explication : au Québec, un propriétaire ne "
             "peut pas exiger plus que le premier mois de loyer. C'est un droit.")

    d.pratique('Pratique · 1 de 4', "Que veut dire le mot ?",
               "Vocabulaire du bail.", [
        ("signer un bail", "s'engager à louer pour la durée prévue"),
        ("résilier un bail", "y mettre fin avant la date prévue"),
        ("sous-louer", "laisser quelqu'un d'autre habiter à sa place"),
        ("un avis écrit", "une lettre officielle envoyée dans un délai prévu"),
        ("l'état des lieux", "la description du logement au début du bail"),
    ], corrige=True,
       notes="Faire employer chaque mot dans une phrase. Ce sont des mots qu'on lit plus "
             "qu'on ne les dit : les faire produire à l'oral.")

    d.pratique('Pratique · 2 de 4', "Dans quelle partie du bail ?",
               "Six parties : les parties, le logement, la durée, le loyer, les inclusions, les règlements.", [
        ("« Les chats sont acceptés, les chiens ne le sont pas. »", "les règlements"),
        ("« 890 $ par mois, payable le premier de chaque mois. »", "le loyer"),
        ("« Du 1er septembre au 31 août. »", "la durée"),
        ("« Chauffage et eau chaude compris. »", "les inclusions"),
        ("« 4 ½, deuxième étage, rue Galt. »", "le logement"),
    ], corrige=True,
       notes="Faire chercher ces cinq informations dans le vrai formulaire. Elles y sont "
             "toutes, dans cet ordre.")

    d.piege("Le piège de la promesse orale",
            "Elle m'a dit qu'elle repeindrait le salon.",
            "Faites-le écrire dans le bail avant de signer.",
            "Une promesse faite pendant une visite n'engage à rien. Ce n'est pas une "
            "question de confiance : le propriétaire peut changer, ou oublier. Une ligne "
            "ajoutée au bail règle la question pour douze mois.",
            notes="Le dire sans méfiance excessive : c'est une pratique normale, et un "
                  "propriétaire sérieux acceptera sans problème.")

    d.piege("Le piège du renouvellement automatique",
            "Je pars en juin, je n'ai rien à faire.",
            "Il faut envoyer un avis écrit, plusieurs mois à l'avance.",
            "Sans avis, le bail se renouvelle tout seul pour une année complète. Le "
            "délai est fixé par la loi et il se compte en mois, pas en semaines. C'est "
            "l'erreur la plus coûteuse d'un locataire.",
            notes="Donner le repère pratique : pour un bail de douze mois, l'avis se "
                  "donne entre trois et six mois avant la fin.")

    d.pratique('Pratique · 3 de 4', "Vrai ou faux",
               "D'après ce que vous venez d'apprendre.", [
        ("La plupart des baux se terminent le 30 juin.", "VRAI"),
        ("Un bail peut commencer une autre date que le 1er juillet.", "VRAI"),
        ("Un propriétaire peut demander trois mois de loyer d'avance.",
         "FAUX — le premier mois seulement"),
        ("Si je ne dis rien, mon bail se termine tout seul.",
         "FAUX — il se renouvelle automatiquement"),
        ("Une promesse orale a la même valeur qu'une clause du bail.", "FAUX"),
    ], corrige=True,
       notes="Ces cinq énoncés sont du savoir pratique. Les faire noter dans le cahier, "
             "avec les réponses.")

    d.pratique('Pratique · 4 de 4', "Que vérifiez-vous avant de signer ?",
               "Cinq points, dans l'ordre.", [
        ("La durée", "les dates de début et de fin"),
        ("Le loyer", "le montant, et ce qu'il comprend"),
        ("Les inclusions", "écrites, pas promises"),
        ("Les règlements", "animaux, fumée, sous-location"),
        ("Les promesses de la visite", "sont-elles écrites ?"),
    ], corrige=True,
       notes="Cette liste de cinq points est le vrai résultat de la séance. La faire "
             "copier et garder.")

    d.billet(
        "Écrivez les cinq points à vérifier avant de signer un bail.",
        exemples=[
            "Une ligne chacun.",
            "Ajoutez une sixième ligne : la question que vous poseriez avant de signer.",
        ],
        notes="Ce billet est une fiche pratique à garder. Suggérer de le photographier "
              "et de le conserver dans le téléphone.")

    return d.save(dossier)
