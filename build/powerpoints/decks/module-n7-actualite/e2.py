# -*- coding: utf-8 -*-
"""E2 · Écrire son billet dans Le fil du Ruisseau
Bloc E « Je me lance » · couleur framboise · bilan · 75 min.
Source : bloc `appli` — production écrite —, banc FC_CARDS, autoévaluation.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n7-actualite/images/')


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Écrire son billet dans Le fil du Ruisseau",
        chapeau="Dernière séance : vous passez de lecteur à auteur. Dix "
                "lignes, des faits, une opinion annoncée comme telle, et la "
                "question que personne n'a posée.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Rendre les billets de sortie de E1 : "
                  "chacun a déjà sa question, c'est la dernière ligne de son texte.")

    d.objectifs([
        "écrire un billet de blogue de huit à douze phrases ;",
        "y séparer clairement les faits de l'opinion ;",
        "employer une concession, une mise en relief et un connecteur de sujet ;",
        "évaluer ce qu'on est maintenant capable de faire.",
    ], notes="C'est l'intention de production écrite du programme : intervenir dans un "
             "blogue. Le dire au groupe, ça donne du poids à l'exercice.")

    d.declencheur(
        'Mise en situation', "Suzie vous ouvre le blogue du quartier",
        image=IMG + 'local-vide.jpg',
        pistes=[
            "Qui va vous lire ? Des voisins, pas des spécialistes.",
            "Par quoi commencez-vous : les faits ou l'accord ?",
            "Comment montrez-vous que vous avez vérifié ?",
            "Sur quoi finissez-vous ?",
        ],
        notes="La quatrième piste a une seule bonne réponse : sur la question. Un "
              "billet qui finit sur une opinion se referme ; un billet qui finit sur "
              "une question ouvre les commentaires.")

    d.tableau('Analyse', "Le plan en trois paragraphes",
              ['Le paragraphe', 'Ce qu\'on y met'],
              [["1. Ce qui est établi",
                "deux faits vérifiables au moins, avec un chiffre ou une date"],
               ["2. Ce qui ne l'est pas, et ce que j'en pense",
                "une information au conditionnel, une parole rapportée, puis une concession"],
               ["3. Ma question",
                "une seule, adressée aux lecteurs"]],
              cle=0,
              note="Huit à douze phrases en tout. Un billet plus long ne se lit pas.",
              notes="Diapositive à photographier. Écrire le plan au tableau et le "
                    "laisser pendant toute la rédaction.")

    d.regle("Nommez vos sources, protégez-vous",
            "« À ma connaissance » est la formule la plus utile de tout le module.",
            precision="On ne reproche jamais à quelqu'un d'avoir dit ce qu'il ignorait ; "
                      "on lui reproche d'avoir affirmé sans vérifier. Écrire « à ma "
                      "connaissance », « selon le reportage de mardi » ou « la "
                      "conseillère a dit que » coûte cinq mots et rend un texte "
                      "inattaquable.",
            notes="Diapositive à photographier. C'est ce qui permet à un élève de "
                  "publier sans crainte, et donc de publier.")

    d.cartes("Les sept exigences du billet", "À cocher avant d'envoyer", [
        ("Deux faits vérifiables",
         "avec un chiffre ou une date."),
        ("Une information non confirmée",
         "marquée au conditionnel : « serait », « ouvrirait »."),
        ("Une parole rapportée",
         "« la conseillère a dit que... » - attention au temps du verbe."),
        ("Une concession",
         "« bien que » + subjonctif, ou « même si » + indicatif."),
        ("Une mise en relief",
         "« ce qui... c'est » ou « c'est... qui »."),
        ("Un connecteur de sujet",
         "« quant à », « en ce qui concerne »."),
        ("Une question aux lecteurs",
         "à la toute fin, une seule."),
    ], notes="Ces sept exigences sont affichées dans l'activité, sous la zone de "
             "rédaction. L'assistant les vérifie une à une et donne une rétroaction "
             "immédiate ; elle n'est pas conservée.")

    d.piege("Un titre qui juge",
            "Scandale du dépôt : le quartier trahi",
            "Point de dépôt : la question des heures",
            "Le titre d'un billet annonce de quoi on parle, pas ce qu'on en pense. Un "
            "titre qui juge fait fuir exactement les lecteurs qu'on voulait convaincre, "
            "et il affaiblit le texte : celui qui a besoin d'un titre fort a souvent des "
            "arguments faibles.",
            notes="Faire proposer trois titres au tableau et voter. L'exercice prend "
                  "cinq minutes et améliore tous les billets.")

    d.vocabulaire('Bilan', "Les mots du module, une dernière fois", [
        ("un reportage", "Le compte rendu d'un journaliste qui va sur place."),
        ("une chronique", "L'avis signé d'une personne, semaine après semaine."),
        ("une source", "Ce qui permet de vérifier une information."),
        ("un fait", "Ce qu'on peut aller vérifier, même s'il se révèle faux."),
        ("une opinion", "Ce que quelqu'un pense, et qui se discute."),
        ("un communiqué", "L'annonce officielle d'un organisme."),
        ("la période de questions", "Le moment où les citoyens interrogent leurs élus."),
        ("un argument", "La raison qu'on donne pour appuyer son opinion."),
    ], notes="Révision par les cartes mémoire dans l'activité, puis autoévaluation. "
             "Douze énoncés à évaluer : pas encore, un peu, oui.")

    d.pratique('Production écrite', "Votre billet, huit à douze phrases",
               "Le fil du Ruisseau - nouveau billet.", [
        ("Paragraphe 1", "ce qui est établi : deux faits, avec un chiffre ou une date"),
        ("Paragraphe 2", "ce qui ne l'est pas, une parole rapportée, une concession"),
        ("Paragraphe 3", "votre question, une seule, adressée aux lecteurs"),
        ("Le titre", "il annonce le sujet, il ne juge pas"),
        ("La prudence", "« à ma connaissance » partout où vous n'êtes pas certain"),
        ("Avant d'envoyer", "relisez à voix haute : les phrases trop longues s'entendent"),
    ], corrige=False,
       notes="Rédaction dans l'activité interactive, avec vérification par l'assistant, "
             "puis envoi à l'enseignant. Les élèves rapides peuvent commenter le billet "
             "d'un camarade - c'est exactement ce que fait un blogue.")

    d.billet(
        "Qu'est-ce que vous saurez faire lundi que vous ne saviez pas faire il y a quatre semaines ?",
        exemples=[
            "Une phrase, la vôtre.",
            "Pensez à ce que vous ferez la prochaine fois qu'on vous enverra une nouvelle.",
        ],
        notes="Dernier billet du module. Le lire à voix haute en groupe si l'ambiance "
              "s'y prête : c'est une bonne façon de fermer quatre semaines de travail.")

    return d.save(dossier)
