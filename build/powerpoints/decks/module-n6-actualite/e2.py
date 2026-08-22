# -*- coding: utf-8 -*-
"""E2 · Écris au courrier des lecteurs
Bloc E « Je me lance » · couleur framboise · bilan · 75 min.
Source : bloc `appli` de `custom.js` — production écrite, les huit exigences
du courriel —, banc FC_CARDS, autoévaluation en seize énoncés.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Écris au courrier des lecteurs",
        chapeau="Dernière séance : tu passes de lecteur à auteur. Un "
                "courriel de huit à douze phrases au Courrier de la "
                "Batture - ce que la chronique disait, puis ce que tu en "
                "penses, et jamais l'inverse.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Reprendre en cinq minutes les objections "
                  "restées sans réponse en E1, puis entrer dans la rédaction. Rendre les "
                  "premières phrases corrigées du billet de D2.")

    d.objectifs([
        "écrire un courriel formel de huit à douze phrases ;",
        "organiser le texte en deux ou trois paragraphes, un par idée ;",
        "séparer ce que la chronique disait de ce qu'on en pense ;",
        "évaluer ce qu'on est maintenant capable de faire.",
    ], notes="C'est l'attente de fin de cours du niveau 6, mot pour mot : rédiger un "
             "courriel pour informer son destinataire du contenu d'un article "
             "d'intérêt général, en organisant ses idées à l'aide de paragraphes.")

    d.declencheur(
        'Mise en situation', "Le Courrier de la Batture publie les lettres signées",
        pistes=[
            "Qui va te lire ? Des voisins, pas des spécialistes.",
            "Par quoi commences-tu : l'information ou ton avis ?",
            "Comment montres-tu que tu as bien compris la chronique ?",
            "Qu'est-ce que tu demandes, à la fin ?",
        ],
        notes="La deuxième piste a une seule bonne réponse, et le groupe la connaît "
              "depuis D1 : l'information d'abord. La quatrième est nouvelle : un "
              "courriel formel se termine sur une demande ou une proposition.")

    d.tableau('Analyse', "Le plan en trois paragraphes",
              ['Le paragraphe', 'Ce qu\'on y met'],
              [["1. Ce que la chronique disait", "les étapes dans l'ordre, avec au moins un chiffre"],
               ["2. Ce que j'en pense", "un connecteur de point de vue, et une raison"],
               ["3. Ce que je demande", "une proposition, ou une question au journal"]],
              cle=0,
              note="Huit à douze phrases en tout. Une formule d'appel au début, une salutation à la fin.",
              notes="Diapositive à photographier. Écrire le plan au tableau et l'y "
                    "laisser pendant toute la rédaction. C'est aussi le plan de la "
                    "lettre de madame Berthiaume, en D1 : le faire remarquer.")

    d.cartes("Les huit exigences du courriel", "À cocher avant d'envoyer", [
        ("Une formule d'appel et une salutation",
         "« Monsieur le rédacteur en chef, » au début, une salutation à la fin."),
        ("Deux ou trois paragraphes séparés",
         "un par idée principale, pas un bloc de douze phrases."),
        ("Les étapes dans l'ordre, avec un chiffre",
         "dix jours, trois ans, 780 dollars, quinze mille."),
        ("Un connecteur d'exemplification",
         "par exemple, notamment, ainsi."),
        ("Une hypothèse en « si »",
         "et jamais de futur après le « si »."),
        ("Un connecteur de point de vue",
         "à mon avis, pour ma part, selon moi."),
        ("Une reprise sans répétition",
         "cette machine, ce refus, cet incendie."),
        ("Un « il faut que » et un subjonctif",
         "il faut que les pièces existent."),
    ], notes="Ces huit exigences sont affichées dans l'activité, sous la zone de "
             "rédaction. L'assistant les vérifie une à une et donne une rétroaction "
             "immédiate ; elle n'est pas conservée.")

    d.regle("Séparer, c'est se faire publier",
            "Une lettre qui mêle l'information et l'avis se lit comme une plainte.",
            precision="Une lettre qui les sépare se lit comme un point de vue - et "
                      "c'est celle-là que le journal publie. Le lecteur doit pouvoir "
                      "s'arrêter après ton premier paragraphe en ayant appris quelque "
                      "chose, même s'il n'est pas d'accord avec la suite. C'est le "
                      "conseil que Raphaël donne à Nadège, et c'est aussi ce qui "
                      "distingue les deux lettres de la page du courrier.",
            notes="Diapositive à photographier. C'est le savoir de grammaire du texte du "
                  "niveau 6 : découper, disposer, formuler et présenter le contenu d'un "
                  "courriel formel.")

    d.piege("Un objet qui juge",
            "Scandale des garanties : les consommateurs abandonnés",
            "Garantie légale : ce que la chronique du 12 août rappelait",
            "L'objet d'un courriel annonce de quoi on parle, pas ce qu'on en pense. Un "
            "objet qui juge fait fuir exactement les lecteurs qu'on voulait convaincre, "
            "et il affaiblit le texte : celui qui a besoin d'un titre fort a souvent "
            "des arguments faibles.",
            notes="Faire proposer trois objets au tableau et voter. L'exercice prend "
                  "cinq minutes et améliore tous les courriels du groupe.")

    d.vocabulaire('Bilan', "Les mots du module, une dernière fois", [
        ("une chronique pratique", "Elle t'apprend quoi faire, étape par étape."),
        ("le courrier des lecteurs", "Des lettres signées par des gens ordinaires."),
        ("la garantie légale", "Elle existe même quand celle du fabricant est finie."),
        ("une durée raisonnable", "Elle dépend du prix payé, du contrat et de l'usage."),
        ("une mise en demeure", "Les faits, la demande, un délai. Une page suffit."),
        ("un recours", "Le moyen prévu par la loi quand on n'obtient rien autrement."),
        ("un organisme public", "L'Office : on appelle, ça ne coûte rien."),
        ("un point de vue", "Ce qu'une personne pense, et qu'une autre peut voir autrement."),
    ], notes="Révision par les cartes mémoire dans l'activité, puis autoévaluation. "
             "Seize énoncés à évaluer : pas encore, un peu, oui.")

    d.pratique('Production écrite', "Ton courriel, huit à douze phrases",
               "À : courrier@lecourrierdelabatture.example", [
        ("L'objet", "court, et sans jugement"),
        ("Paragraphe 1", "ce que la chronique disait : les étapes, avec un chiffre"),
        ("Paragraphe 2", "ce que tu en penses, annoncé par un connecteur de point de vue"),
        ("Paragraphe 3", "ce que tu demandes ou ce que tu proposes"),
        ("La liste des huit", "coche-les une par une avant de vérifier"),
        ("Avant d'envoyer", "relis à voix haute : les phrases trop longues s'entendent"),
    ], corrige=False,
       notes="Rédaction dans l'activité, avec vérification par l'assistant, puis envoi à "
             "l'enseignante. Les élèves rapides peuvent lire le courriel d'un camarade "
             "et lui dire laquelle des huit exigences manque.")

    d.billet(
        "Qu'est-ce que tu sauras faire lundi que tu ne savais pas faire il y a quatre semaines ?",
        exemples=[
            "Une phrase, la tienne.",
            "Pense au prochain appareil qui brisera chez toi.",
        ],
        notes="Dernier billet du module. Le lire à voix haute en groupe si l'ambiance "
              "s'y prête. Rappeler que le premier geste, la prochaine fois, tient en "
              "trois mots : garder la facture.")

    return d.save(dossier)
