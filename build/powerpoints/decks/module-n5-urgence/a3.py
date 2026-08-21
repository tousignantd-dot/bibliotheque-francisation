# -*- coding: utf-8 -*-
"""A3 · Les mots de la nuit.
Bloc A « Je découvre » · couleur framboise · 75 min. Vocabulaire.
Source : `FC_CARDS`, exercices `prVocab` et `prImg`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-urgence/images/')


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Les mots de la nuit",
        chapeau="Seize mots, quatre moments : hésiter, appeler, attendre, "
                "être hospitalisé. Ce ne sont pas des mots de médecine — "
                "ce sont ceux qu'il faut dire ou comprendre au téléphone.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Prévenir le groupe qu'aucun terme technique "
                  "n'est exigé : on ne demande jamais à un proche de nommer une maladie, "
                  "on lui demande de décrire ce qu'il voit.")

    d.objectifs([
        "nommer les seize mots du module et les employer dans une phrase ;",
        "distinguer ce qu'on décrit de ce qu'on diagnostique ;",
        "associer chaque mot au moment où il sert ;",
        "reconnaître les mots à l'écoute, dans une phrase entière.",
    ])

    d.declencheur(
        'Observation', "Cet escalier est le lieu de tout le module. Quels mots "
                       "faut-il pour raconter ce qui s'y passe ?",
        image=IMG + 'escalier.jpg',
        pistes=[
            "Comment dit-on ce qui est arrivé, sans nommer une maladie ?",
            "Quels mots emploie-t-on au téléphone, et lesquels à l'hôpital ?",
            "Quels mots avez-vous déjà entendus sans les comprendre ?",
        ],
        notes="Noter au tableau les mots que le groupe apporte. Beaucoup viendront de "
              "l'anglais ou de la langue d'origine : les accueillir, puis donner "
              "l'équivalent français employé au Québec.")

    d.vocabulaire('Je découvre', "Hésiter, et choisir le numéro", [
        ("un malaise", "Un problème de santé qui arrive tout d'un coup et qui n'a pas "
                       "encore de nom."),
        ("le 8-1-1", "Le numéro gratuit où une infirmière répond au téléphone, jour et "
                     "nuit."),
        ("faire de la fièvre", "Avoir une température du corps plus haute que la "
                               "normale."),
        ("perdre connaissance", "Ne plus rien voir ni entendre pendant un moment, et "
                                "tomber."),
    ], notes="« Un malaise » est le mot le plus utile des quatre : il permet de décrire "
             "sans diagnostiquer. Le faire employer dans trois phrases avant de passer.")

    d.vocabulaire('Défi 1', "L'appel au 9-1-1", [
        ("le 9-1-1", "Le numéro à composer pour ce qui ne peut pas attendre dix minutes."),
        ("un répartiteur", "La personne qui répond au 9-1-1, pose les questions et "
                           "envoie les secours."),
        ("les ambulanciers", "Les deux personnes qui viennent en ambulance et donnent "
                             "les premiers soins."),
        ("une civière", "Le lit étroit à roues qui sert à transporter une personne "
                        "couchée."),
    ], notes="« Répartiteur » est presque toujours inconnu. Le faire répéter : c'est un "
             "mot qu'on entendra dans le jeu de rôle de la séance E1.")

    d.vocabulaire('Défi 2', "Le triage et l'attente", [
        ("le triage", "Le premier arrêt à l'urgence, où une infirmière décide qui passe "
                      "avant."),
        ("un niveau de priorité", "Un chiffre de 1 à 5 qui dit à quel point le cas est "
                                  "pressant."),
        ("les signes vitaux", "La tension, le pouls, la température et la respiration, "
                              "mesurés ensemble."),
        ("une radiographie", "Une image de l'intérieur du corps, qui montre entre autres "
                             "les os."),
    ], notes="Ces quatre mots sont ceux qu'on entend sans les comprendre à l'urgence. "
             "Annoncer que la séance C4 y reviendra en détail.")

    d.vocabulaire('Défi 3', "L'étage et le congé", [
        ("une fracture", "Un os cassé."),
        ("une hospitalisation", "Un séjour de plusieurs jours dans une chambre de "
                                "l'hôpital."),
        ("les heures de visite", "Les heures pendant lesquelles la famille peut entrer "
                                 "dans la chambre."),
        ("le congé de l'hôpital", "Le moment où le médecin autorise la personne à "
                                  "rentrer à la maison."),
    ], notes="« Le congé » surprend : dans la langue courante, un congé est un jour sans "
             "travail. Ici, c'est l'autorisation de sortir. Le dire explicitement.")

    d.piege("Chercher le mot savant",
            "Elle a une… comment on dit… une fracture du col fémoral, je pense ?",
            "Elle est tombée et elle ne peut plus bouger sa jambe.",
            "Personne n'attend de vous un terme médical. Décrire ce que vous voyez vaut "
            "mieux qu'un mot approximatif, qui peut envoyer l'équipe sur une fausse piste.",
            notes="Insister : c'est le conseil le plus libérateur de la séance. Beaucoup "
                  "d'élèves se taisent au téléphone parce qu'ils cherchent un mot.")

    d.pratique('Emploi', "Le mot juste",
               "Complétez chaque phrase avec un mot du module.", [
        ("Au ___, une infirmière écoute votre récit et donne un niveau de priorité.", "triage"),
        ("Les ___ ont installé Amparo sur une civière.", "ambulanciers"),
        ("L'infirmière prend les ___ ___ avant de poser ses questions.", "signes vitaux"),
        ("La ___ de la hanche a montré une fracture.", "radiographie"),
        ("Le ___ répond au 9-1-1 et envoie les secours.", "répartiteur"),
        ("Elle n'a pas ___ connaissance : elle répondait déjà.", "perdu"),
    ], corrige=True,
       notes="Faire relire chaque phrase complète à voix haute une fois corrigée : c'est "
             "l'oral qui fixe le mot, pas le trou rempli.")

    d.billet(
        "Choisissez trois mots et écrivez une phrase avec chacun.",
        exemples=[
            "Une phrase qui pourrait vraiment se dire au téléphone ou à l'hôpital.",
            "Évitez les phrases de dictionnaire : « le triage est un endroit où… ».",
        ],
        notes="Ramasser et corriger pour la séance A4 : les phrases justes serviront "
              "d'exemples au groupe, sans nommer les auteurs.")

    return d.save(dossier)
