# -*- coding: utf-8 -*-
"""B4 · Mes droits comme locataire.
Bloc B · couleur acier · 60 min.
Source : mini-leçon `t1trib`, exercice `t1trib` et son encadré culturel.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='acier',
        titre='Mes droits comme locataire',
        chapeau="Un problème de logement se règle presque toujours par étapes, et sauter "
                "une marche fait perdre du temps. On parle, on écrit, et seulement si "
                "rien ne bouge, on s'adresse au Tribunal administratif du logement.",
        duree='60 minutes')

    d.titre(notes="Séance de culture et de droits. Beaucoup d'élèves ignorent l'existence "
                  "du TAL, ou le croient réservé aux propriétaires. Prévoir des questions.")

    d.objectifs([
        "connaître les trois marches d'un problème de logement, dans l'ordre ;",
        "écrire un avis écrit qui contient les quatre éléments nécessaires ;",
        "savoir ce qu'est le Tribunal administratif du logement et quand s'y adresser ;",
        "savoir ce qu'il ne faut jamais faire, même quand une réparation traîne.",
    ])

    d.cartes('Les trois marches', "Dans cet ordre, jamais autrement", [
        ("1 · On parle",
         "Un appel, une conversation dans l'entrée. C'est là que neuf problèmes sur dix "
         "se règlent. Rapide, direct, sans conflit."),
        ("2 · On écrit",
         "Un courriel daté qui reprend ce qui a été dit. Ça ne remplace pas l'appel : "
         "ça le double. Cette marche existe surtout pour protéger la troisième."),
        ("3 · On dépose une demande",
         "Au Tribunal administratif du logement, si rien ne bouge. C'est un recours, "
         "pas un premier réflexe."),
        ("Pourquoi l'ordre compte",
         "Sauter la marche 1 braque la personne propriétaire pour rien. Sauter la marche 2 "
         "rend la marche 3 presque impossible : sans écrit, il ne reste que votre parole "
         "contre la sienne."),
    ], notes="Faire dessiner les trois marches dans le cahier. C'est le schéma le plus "
             "utile de tout le module.")

    d.tableau('Analyse', "Ce que contient un bon avis écrit",
              ['Élément', 'Exemple', 'Pourquoi'],
              [["Le fait", "le calorifère ne chauffe plus", "ce qui ne va pas"],
               ["Depuis quand", "depuis le 4 novembre", "c'est la date qui compte"],
               ["L'effet", "il fait 14 °C chez moi", "un chiffre dit l'urgence"],
               ["La demande", "faire venir un électricien", "ce que vous voulez"]],
              cle=1,
              note="Un courriel de trois lignes suffit s'il contient ces quatre éléments. "
                   "C'est exactement la structure d'une plainte à l'oral — fait, effet, "
                   "demande — avec une date en plus.",
              notes="Faire écrire le courriel complet au tableau, collectivement, à partir "
                    "des quatre éléments. Trois lignes, pas plus.")

    d.regle('Pourquoi la date change tout',
            "Devant le tribunal, la question n'est pas « le problème existe-t-il ? » mais « depuis quand la propriétaire le sait-elle ? »",
            precision="Un courriel envoyé le 4 novembre prouve qu'elle savait le 4 novembre. "
                      "Un appel téléphonique ne prouve rien. Gardez aussi vos photos avec la "
                      "date, et notez l'heure de chaque appel. Ça prend trente secondes et "
                      "ça vaut beaucoup plus tard.",
            notes="Relier à la séance A1 : c'est exactement le conseil de Bertrand, mais on "
                  "sait maintenant pourquoi.")

    d.cartes('Le Tribunal administratif du logement', "Ce qu'il faut en savoir", [
        ("Ce que c'est",
         "L'organisme public du Québec qui tranche les désaccords entre locataires et "
         "propriétaires. C'est le nouveau nom de la Régie du logement, créée en 1980."),
        ("Ce qu'il fait",
         "Il informe les deux parties sur leurs droits et leurs obligations, et il décide "
         "quand elles n'arrivent pas à s'entendre : loyer, réparations, bail, expulsion."),
        ("Ce qu'on y trouve",
         "Un service téléphonique, des rencontres individuelles, de la documentation "
         "gratuite, et des formulaires officiels — dont le modèle de bail obligatoire "
         "au Québec."),
        ("Bon à savoir",
         "Déposer une demande coûte quelques dizaines de dollars. Il n'est pas obligatoire "
         "d'être représenté par un avocat : beaucoup de gens s'y présentent seuls."),
    ], notes="La dernière carte est celle qui rassure le plus. Insister : on peut se "
             "présenter seul et expliquer sa situation dans ses mots.")

    d.pratique('Pratique', 'Quelle marche pour quelle situation ?',
               "Marche 1 : on parle. Marche 2 : on écrit. Marche 3 : on dépose une demande.", [
        ("Le robinet goutte depuis hier.", "marche 1 — un simple appel suffit"),
        ("Deux courriels sans réponse depuis un mois.", "marche 3 — l'écrit a déjà été fait"),
        ("Le chauffage est mort, il fait 14 °C.", "marches 1 et 2 le même jour — c'est urgent"),
        ("La propriétaire refuse par écrit de réparer.", "marche 3 — le refus écrit est votre preuve"),
    ], corrige=True,
       notes="Le dernier cas surprend : un refus écrit n'est pas une mauvaise nouvelle, "
             "c'est la meilleure preuve possible devant le tribunal.")

    d.vocabulaire('Écrire', "Des phrases à réutiliser telles quelles", [
        ("Je vous écris pour faire suite à notre conversation téléphonique du 4 novembre.",
         "Rappeler l'appel."),
        ("Le problème dure depuis deux semaines et il s'aggrave.",
         "Situer dans le temps."),
        ("Vous trouverez une photo en pièce jointe.",
         "Joindre la preuve."),
        ("J'aimerais savoir quelle date est prévue pour la réparation.",
         "Demander clairement."),
        ("Merci de me confirmer la réception de ce message.",
         "Obtenir une trace de réception."),
    ], notes="Faire copier ces cinq phrases. Elles serviront à la production écrite de la "
             "séance E1.")

    d.piege('Ce qu\'il ne faut jamais faire',
            "J'arrête de payer mon loyer pour la faire réagir.",
            "Je continue à payer et je dépose une demande.",
            "Arrêter de payer ne fait pas pression : ça donne au contraire un motif "
            "d'expulsion. Le loyer se paie même quand la réparation traîne. C'est "
            "contre-intuitif, mais c'est la règle, et c'est le conseil le plus important "
            "de la séance.",
            notes="Le dire deux fois. C'est une erreur qui coûte très cher et que des gens "
                  "de bonne foi commettent chaque année.")

    d.piege('La deuxième erreur',
            "Je règle tout par téléphone, c'est plus rapide.",
            "Je double chaque appel d'un courriel de deux lignes.",
            "Un appel règle vite, mais ne laisse aucune trace. Le courriel envoyé après "
            "l'appel prend une minute et c'est lui qui vous protège en cas de désaccord. "
            "Il n'a pas besoin d'être long ni formel : « Bonjour, je vous confirme notre "
            "conversation de ce matin au sujet du calorifère » suffit.",
            notes="Montrer qu'un courriel de confirmation n'est pas un geste hostile. "
                  "Beaucoup d'élèves craignent de paraître méfiants.")

    d.pratique('Vérification', 'Vrai ou faux',
               "Répondez sans regarder vos notes.", [
        ("Le Tribunal administratif du logement s'appelait avant la Régie du logement.", "VRAI"),
        ("Il s'occupe seulement des personnes propriétaires.", "FAUX — les deux parties"),
        ("On peut y obtenir de la documentation gratuite et des formulaires.", "VRAI"),
        ("Il faut s'adresser au tribunal avant de parler à sa propriétaire.", "FAUX — c'est la dernière marche"),
        ("Un courriel daté est une meilleure preuve qu'un appel téléphonique.", "VRAI"),
        ("Il est obligatoire d'être représenté par un avocat.", "FAUX"),
    ], corrige=True)

    d.billet(
        "Écrivez les trois lignes du courriel que vous enverriez après votre appel.",
        exemples=[
            "Quatre éléments : le fait · depuis quand · l'effet · la demande.",
            "Datez-le. C'est la date qui fait toute la valeur du message.",
        ],
        notes="Fin du bloc B. Ramasser les billets : ils constituent un premier brouillon "
              "de la production écrite de la séance E1.")

    return d.save(dossier)
