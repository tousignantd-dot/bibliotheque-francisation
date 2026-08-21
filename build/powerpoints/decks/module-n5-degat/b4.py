# -*- coding: utf-8 -*-
"""B4 · Le courriel qui suit l'appel.
Bloc B « Défi 1 · Le constat » · couleur ambre · 75 min. Écriture.
Source : exercice `t1courriel`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-degat/images/')


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Le courriel qui suit l'appel",
        chapeau="Un appel ne laisse pas de trace. Un courriel, oui — et c'est "
                "la date de ce courriel qui comptera si la réparation traîne.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 1. Elle réunit tout le bloc : le récit au "
                  "passé, le gérondif, la description précise. Prévoir vingt minutes "
                  "d'écriture individuelle à la fin.")

    d.objectifs([
        "savoir pourquoi on écrit après avoir téléphoné ;",
        "résumer une entente en deux lignes ;",
        "annoncer et nommer ses pièces jointes ;",
        "garder un ton courtois dans un courriel de constat.",
    ])

    d.regle("Écrire après avoir téléphoné",
            "Le courriel prouve la date à laquelle le propriétaire a su.",
            precision="Un appel se conteste : « je ne me souviens pas », « vous m'avez "
                      "dit autre chose ». Un courriel affiche une date, et cette date ne "
                      "se discute pas. C'est elle qui compte si la réparation traîne, et "
                      "c'est elle que regardera un juge administratif s'il faut aller "
                      "jusque-là.",
            notes="Diapositive à photographier. Insister : ce n'est pas de la méfiance, "
                  "c'est de la méthode — et ça vaut pour toutes les démarches, pas "
                  "seulement le logement.")

    d.cartes("Les quatre parties d'un courriel de constat", "Court, et complet", [
        ("L'objet, précis",
         "« Dégât d'eau — logement 4, 118 rue Sainte-Hélène. » On le retrouve dans six mois."),
        ("Le rappel de l'appel",
         "« Je fais suite à notre conversation téléphonique de ce matin. »"),
        ("Le résumé de l'entente",
         "La date, l'entreprise, ce qu'on attend de vous. Deux lignes."),
        ("Les pièces jointes, nommées",
         "« Ci-joint 22 photos prises le 10 novembre au matin. »"),
    ], notes="Faire remarquer qu'aucune des quatre ne demande de raconter à nouveau : le "
             "récit a été fait au téléphone.")

    d.declencheur(
        'Observation', "Ces photos-là valent quelque chose. À quelles conditions ?",
        image=IMG + 'boite-documents-trempee.jpg',
        pistes=[
            "Quand ont-elles été prises ?",
            "Est-ce qu'on voit la pièce et le détail ?",
            "Combien y en a-t-il ?",
            "Où sont-elles maintenant ?",
        ],
        notes="La dernière question est celle qui pose problème : une photo dans un "
              "téléphone n'est pas une preuve transmise. C'est le courriel qui la rend "
              "utile.")

    d.tableau('Ce qui se dit, et ce qui s\'écrit', "Deux registres, deux moments",
              ['Au téléphone', 'Dans le courriel'],
              [["le récit complet, avec les détails",
                "deux lignes de rappel, pas plus"],
               ["les questions et les réponses",
                "le résumé de ce qui a été convenu"],
               ["« je vous envoie ça aujourd'hui »",
                "les photos réellement jointes, et nommées"],
               ["le ton de la conversation",
                "le ton courtois d'un écrit : on rapporte, on ne se plaint pas"]],
              cle=1,
              note="Le courriel n'est pas la transcription de l'appel : il en est le reçu.",
              notes="Formulation utile : « le courriel est le reçu de l'appel ». Elle "
                    "évite les courriels de deux pages.")

    d.pratique('Pratique · exercice t1courriel', "Complétez le courriel de Mariama",
               "Un mot ou un groupe de mots par trou.",
               [("Objet : Dégât d'eau — logement 4, 118 rue ___ .", "Sainte-Hélène"),
                ("Bonjour monsieur Cloutier, je fais suite à notre ___ téléphonique.",
                 "conversation"),
                ("Comme convenu, je vous envoie les ___ prises le 10 novembre.",
                 "photos"),
                ("Vous m'avez confirmé qu'une compagnie d' ___ passerait demain.",
                 "assèchement"),
                ("Les travaux devraient durer ___ ou quatre jours.", "trois"),
                ("Je vous remercie de votre diligence et je reste ___ votre disposition.",
                 "à")],
               corrige=True, cols=1,
               notes="Faire lire le courriel complet à voix haute une fois corrigé : "
                     "l'entendre d'un bloc montre à quel point il est court.")

    d.regle("Le ton d'un constat n'est pas celui d'une plainte",
            "On rapporte, on remercie, et on garde la demande pour plus tard.",
            precision="Au moment du constat, rien n'est encore refusé : le propriétaire "
                      "a promis une intervention. Se plaindre maintenant durcit une "
                      "discussion qui n'a pas encore eu lieu. La demande de compensation "
                      "viendra au défi 3, une fois qu'on saura ce que les travaux ont "
                      "réellement coûté en confort.",
            notes="Point de stratégie autant que de langue. Il vaut la peine d'être dit "
                  "explicitement : beaucoup d'élèves écrivent leur colère dans le premier "
                  "courriel et n'ont plus rien à jouer ensuite.")

    d.piege("Écrire trois paragraphes de récit",
            "Je raconte tout depuis le début, pour être sûr.",
            "Deux lignes de rappel, et les photos jointes.",
            "Le destinataire vient de vous parler : il connaît l'histoire. Un courriel "
            "long est un courriel qu'on remet à plus tard, puis qu'on oublie. La seule "
            "chose qui doit sauter aux yeux, c'est la date et ce qui a été convenu.",
            notes="Si un élève tient à raconter, lui proposer de le faire dans un "
                  "document à part, joint au courriel. La forme courte est préservée.")

    d.billet(
        "Écrivez l'objet et la première phrase de votre courriel.",
        exemples=[
            "« Objet : Dégât d'eau — logement 2, 45 rue Provencher »",
            "« Je fais suite à notre conversation de ce matin. »",
        ],
        notes="Deux minutes. Vérifier une seule chose dans l'objet : est-ce qu'il permet "
              "de retrouver le courriel dans six mois ?")

    return d.save(dossier)
