# -*- coding: utf-8 -*-
"""B1 · Le message de Farida.
Bloc B · couleur acier (compréhension orale) · 75 min.
Source : message `t1`, exercice `t1mirna` et les quatre messages `t1msg1` à `t1msg4`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Le message de Farida',
        chapeau="Trois phrases dans une boîte vocale, et huit informations dedans. "
                "Comprendre un message enregistré est plus difficile qu'une "
                "conversation : personne ne peut répéter.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Prévenir : on écoutera chaque message deux fois. "
                  "Dans la vraie vie on peut réécouter, mais pas demander de préciser.")

    d.objectifs([
        "comprendre un message laissé dans une boîte vocale ;",
        "repérer qui appelle, pourquoi, et ce qu'on attend de nous ;",
        "noter les heures, les durées et les noms ;",
        "savoir ce qu'un message doit contenir.",
    ])

    d.dialogue('Le message · 1 de 3', "Bonjour, c'est Farida", [
        ("FARIDA", "Bonjour, c'est Farida. Je vous appelle parce que j'ai un rendez-vous "
                   "à l'hôpital avec le spécialiste de ma fille, le docteur Bernard, "
                   "orthopédiste.", True),
    ], consigne="Écoutez deux fois, diapo masquée. Notez tout ce que vous entendez.",
       notes="Une seule phrase, et déjà quatre informations : qui, pourquoi, avec qui, "
             "quelle spécialité. Faire compter par le groupe.")

    d.dialogue('Le message · 2 de 3', "Le rendez-vous est à 9 h 30", [
        ("FARIDA", "Le rendez-vous est à 9 h 30 demain matin. Ma fille s'est blessée au "
                   "bras la semaine dernière, et je dois apporter une preuve pour "
                   "justifier mon absence au cours de francisation.", True),
    ], notes="Faire relever l'heure et le jour : 9 h 30, demain matin. Puis la raison, "
             "au passé composé — révision du module 2.")

    d.dialogue('Le message · 3 de 3', "Je devrais être de retour vers 10 h 15", [
        ("FARIDA", "La consultation devrait durer environ 45 minutes. Je devrais être de "
                   "retour au centre de formation vers 10 h 15. Merci de votre "
                   "compréhension.", True),
    ], notes="C'est la phrase qui distingue un bon message d'un message ordinaire : elle "
             "donne une heure de retour. Le destinataire sait à quoi s'attendre.")

    d.tableau('Analyse', "Les huit informations du message",
              ['Ce qu\'on apprend', 'Où c\'est dit'],
              [["qui appelle", "Farida, dès le premier mot"],
               ["avec qui est le rendez-vous", "le docteur Bernard, orthopédiste"],
               ["quand", "9 h 30, demain matin"],
               ["pourquoi", "sa fille s'est blessée au bras"],
               ["combien de temps", "environ 45 minutes"],
               ["l'heure de retour", "vers 10 h 15"]],
              cle=0, props=[0.4, 0.6],
              notes="Huit informations en trois phrases. Faire remarquer qu'aucune n'est "
                    "inutile — et qu'il n'y a aucune excuse longue.")

    d.regle("Ce qui fait un bon message",
            "Qui je suis · pourquoi j'appelle · quand · combien de temps · quand je reviens.",
            precision="Cinq éléments, dans cet ordre. Farida les donne tous les cinq en "
                      "trois phrases. C'est le modèle à reproduire, et il tient en "
                      "trente secondes.",
            notes="Écrire les cinq au tableau. Ils reviendront en B2, où l'on remettra "
                  "des messages dans l'ordre, et en B4, où l'on en enregistrera un.")

    d.pratique('Pratique · 1 de 4', "Le message de Farida",
               "Répondez d'après vos notes.", [
        ("Farida a un rendez-vous avec qui ?", "le docteur Bernard, orthopédiste"),
        ("Le rendez-vous est à quelle heure ?", "9 h 30"),
        ("Pourquoi sa fille doit-elle voir un orthopédiste ?", "elle s'est blessée au bras"),
        ("Quand a lieu le rendez-vous ?", "demain matin"),
        ("Combien de temps va durer la consultation ?", "environ 45 minutes"),
        ("Vers quelle heure sera-t-elle de retour ?", "vers 10 h 15"),
    ], corrige=True,
       notes="Corriger sans réécouter d'abord. Puis réécouter une troisième fois pour "
             "vérifier : c'est là que les élèves voient ce qu'ils ont manqué.")

    d.cartes('Quatre autres messages', "Qui appelle, et pourquoi", [
        ("Message 1 · Léa",
         "L'infirmière de l'école appelle les parents de Léa : elle fait de la fièvre et "
         "doit être récupérée à l'école."),
        ("Message 2 · monsieur Bertrand",
         "Il appelle son collègue Simon Nadeau pour confirmer les détails d'une "
         "livraison prévue pour demain."),
        ("Message 3 · madame Okafor",
         "Le centre l'informe d'un changement de salle pour son cours de francisation. "
         "Rien de particulier à apporter."),
        ("Message 4 · le centre de formation",
         "Le centre est fermé à cause d'une panne de chauffage. La direction informera "
         "les élèves par courriel ou par téléphone."),
    ], notes="Faire écouter les quatre messages avant d'afficher cette diapo. Elle sert "
             "de correction, pas de présentation.")

    d.pratique('Pratique · 2 de 4', "Qui appelle qui, et pourquoi ?",
               "Deux réponses par message.", [
        ("Message 1 — Léa", "l'infirmière appelle les parents : Léa fait de la fièvre"),
        ("Message 2 — monsieur Bertrand", "il appelle Simon Nadeau : confirmer une livraison"),
        ("Message 3 — madame Okafor", "le centre l'informe : changement de salle"),
        ("Message 4 — le centre", "la direction informe : fermeture pour panne de chauffage"),
    ], corrige=True,
       notes="Les deux questions — qui, pourquoi — suffisent à comprendre n'importe quel "
             "message. Le dire explicitement.")

    d.pratique('Pratique · 3 de 4', "Les détails du message 3",
               "Madame Okafor et le changement de salle.", [
        ("À quel cours était-elle inscrite ?", "un cours de francisation"),
        ("Doit-elle apporter quelque chose de particulier ?",
         "non — seulement ses effets habituels"),
        ("Comment peut-elle joindre la secrétaire ?", "par téléphone ou par courriel"),
    ], corrige=True,
       notes="La deuxième question demande une réponse justifiée : « non, parce que le "
             "changement concerne seulement la salle ». Insister sur la justification.")

    d.piege("Le piège du message trop court",
            "Bonjour, c'est moi, je ne serai pas là. Merci.",
            "Bonjour, c'est Farida Bensalem. Je vous appelle parce que…",
            "« C'est moi » ne dit rien à une secrétaire qui reçoit vingt messages. Sans "
            "nom complet, sans raison et sans heure de retour, le message oblige à "
            "rappeler — et personne ne rappelle une boîte vocale anonyme.",
            notes="Faire écouter un mauvais message improvisé par vous-même, puis le bon. "
                  "Le contraste est plus parlant qu'une explication.")

    d.pratique('Pratique · 4 de 4', "Complétez le message",
               "Les cinq éléments, dans l'ordre.", [
        ("Qui je suis", "Bonjour, c'est Karim Haddad."),
        ("Pourquoi j'appelle", "Je vous appelle parce que ma fille est malade."),
        ("Quand", "Je dois aller la chercher ce matin."),
        ("Combien de temps", "Je serai absent environ deux heures."),
        ("Quand je reviens", "Je devrais être de retour vers onze heures."),
    ], corrige=True,
       notes="Faire dire le message complet d'un seul trait par trois élèves différents. "
             "Chronométrer : il doit tenir en trente secondes.")

    d.billet(
        "Écrivez un message de boîte vocale en cinq phrases.",
        exemples=[
            "Qui vous êtes · pourquoi · quand · combien de temps · quand vous revenez.",
            "Choisissez une situation vraie ou inventée.",
        ],
        notes="Ramasser. Ces messages seront enregistrés en B4 : demander aux élèves de "
              "garder leur brouillon.")

    return d.save(dossier)
