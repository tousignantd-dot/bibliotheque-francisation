# -*- coding: utf-8 -*-
"""B1 · Le service de renseignements
Bloc B « Défi 1 · Ce que dit le site » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf`, mini-leçon `t1vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Le service de renseignements",
        chapeau="Un numéro gratuit, une préposée, et quatre questions notées "
                "d'avance. La conversation du Défi 2 se joue ici.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 1. Rappeler où on en est : Farida a lu la page "
                  "hier soir, elle n'a pas tout compris, elle téléphone. Le module "
                  "montre exprès la démarche dans le bon ordre.")

    d.objectifs([
        "suivre une explication longue donnée au téléphone ;",
        "distinguer ce qu'un service de renseignements peut faire de ce "
        "qu'il ne peut pas ;",
        "nommer les cinq mots de la démarche ;",
        "préparer par écrit les questions d'un appel.",
    ], notes="Le quatrième objectif se pratique en fin de séance et se réutilise "
             "toute la vie : personne n'appelle un service public sans avoir noté "
             "ses questions, et presque tout le monde le fait quand même.")

    d.declencheur(
        'Discussion', "Avez-vous déjà téléphoné à un service public au Québec ?",
        pistes=[
            "Qu'est-ce qui était le plus difficile : comprendre, ou se faire comprendre ?",
            "Aviez-vous préparé vos questions avant d'appeler ?",
            "Qu'est-ce que vous auriez voulu savoir avant de composer le numéro ?",
        ],
        notes="Sujet sensible : plusieurs ont raccroché sans oser redemander. Le dire "
              "soi-même désamorce la honte. Rappeler qu'on a le droit de faire répéter "
              "trois fois, et que c'est le travail de la personne au bout du fil.")

    d.dialogue('Dialogue · 1 de 3', "La situation, en gros puis au précis", [
        ("MYLÈNE", "Tribunal administratif du logement, service de renseignements, Mylène Poitras. Bonjour.", True),
        ("FARIDA", "Bonjour madame. J'ai lu votre page sur la sous-location hier soir et il me reste deux ou trois choses que je n'ai pas comprises.", True),
        ("MYLÈNE", "C'est exactement pour ça que le service existe. Dites-moi d'abord votre situation, en gros, et on ira au précis après.", True),
        ("FARIDA", "Je pars travailler six mois à l'extérieur. Je voudrais sous-louer mon logement pendant ce temps-là et le reprendre en juillet.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Faire remarquer la méthode de la préposée : la situation d'abord, les "
             "détails ensuite. C'est aussi celle de la production orale du bloc E.")

    d.dialogue('Dialogue · 2 de 3', "L'avis, et ce qu'il doit contenir", [
        ("FARIDA", "Est-ce que je peux simplement lui en parler quand je le croise dans l'escalier ?", True),
        ("MYLÈNE", "Vous pouvez, mais ça ne remplace pas l'avis. L'avis doit être écrit. Et il doit contenir le nom et l'adresse de la personne à qui vous voulez sous-louer.", True),
        ("FARIDA", "Donc il faut que j'aie déjà trouvé quelqu'un avant d'écrire.", True),
        ("MYLÈNE", "Il le faut. Beaucoup de gens font la démarche à l'envers : ils demandent la permission en général, et on leur répond en général.", True),
    ], notes="La dernière réplique explique pourquoi Farida a visité avec Nicolas "
             "avant d'écrire. C'est contre-intuitif pour presque tout le monde : on "
             "croit qu'on demande d'abord la permission.")

    d.dialogue('Dialogue · 3 de 3', "Quinze jours, et le silence qui dit oui", [
        ("MYLÈNE", "Le locateur a quinze jours pour vous répondre à partir du moment où il reçoit votre avis.", True),
        ("FARIDA", "Et s'il ne répond pas du tout ?", True),
        ("MYLÈNE", "S'il ne répond pas dans les quinze jours, il est réputé avoir consenti. Son silence vaut un oui.", True),
        ("FARIDA", "Alors il faut que je puisse prouver quel jour il l'a reçu.", True),
    ], notes="C'est la diapositive à faire réécouter deux fois. « Réputé avoir "
             "consenti » sera repris en B2 dans le texte écrit : ici, on veut "
             "seulement que l'oreille l'ait entendu une fois.")

    d.tableau('Analyse', "Ce que ce service fait, et ne fait pas",
              ['Il donne', 'Il ne donne pas'],
              [["une règle", "une décision sur votre cas"],
               ["un délai", "un conseil de stratégie"],
               ["le mot juste", "une lettre rédigée pour vous"],
               ["ce qu'un papier doit contenir", "un appel à votre place"]],
              cle=0,
              notes="Expliquer la raison : le même organisme tranche les litiges. Il ne "
                    "peut pas conseiller une partie et juger l'autre. Ce n'est pas de "
                    "la mauvaise volonté, c'est une règle d'impartialité.")

    d.regle("Un motif sérieux regarde la personne, pas votre projet",
            "Le locateur peut refuser — mais pas pour n'importe quoi.",
            precision="Un motif sérieux se rapporte à la personne proposée ou au "
                      "logement, et il doit pouvoir se montrer : un défaut de "
                      "paiement inscrit à un dossier, par exemple. Préférer un "
                      "couple à un étudiant n'est pas un motif sérieux. Et le refus "
                      "doit être écrit, avec ses raisons.",
            notes="Diapositive à photographier. Ne pas laisser croire que le refus est "
                  "toujours abusif : c'est au Tribunal d'apprécier, jamais à l'élève. "
                  "Ce qu'on apprend ici, c'est quoi regarder.")

    d.vocabulaire('Vocabulaire', "Les cinq mots de la démarche", [
        ("la sous-location", "Le fait de prêter son logement à quelqu'un pour un temps, en gardant son bail."),
        ("la cession de bail", "Le fait de transmettre son bail et de sortir du contrat pour de bon."),
        ("la résiliation", "La fin d'un contrat avant la date prévue, dans les cas que la loi permet."),
        ("un motif sérieux", "Une raison solide, vérifiable, qui touche la personne ou le logement."),
        ("les obligations", "Ce qu'une personne doit faire à cause du contrat ou de la loi."),
    ], notes="Trois de ces mots ont été vus en A2 : les redire vite. Les deux nouveaux "
             "— motif sérieux, obligations — méritent une phrase d'exemple chacun, "
             "prise dans le dialogue.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'appel de Farida.", [
        ("L'avis peut se donner de vive voix dans l'escalier.", "faux - il doit être écrit"),
        ("L'avis doit contenir le nom et l'adresse de la personne.", "vrai"),
        ("Le locateur a quinze jours pour répondre.", "vrai"),
        ("S'il ne répond pas, la sous-location est refusée.", "faux - son silence vaut un oui"),
        ("Le locateur qui refuse doit dire pourquoi, par écrit.", "vrai"),
        ("Préférer un couple à un étudiant est un motif sérieux.", "faux - c'est une préférence"),
    ], corrige=True,
       notes="Le quatrième énoncé est celui qui se trompe le plus : le réflexe veut "
             "que le silence soit un refus. Prendre le temps de le retourner.")

    d.billet(
        "Écrivez les trois questions que vous poseriez si vous téléphoniez demain.",
        exemples=[
            "Des questions précises, pas générales.",
            "« Il a combien de temps ? » est vague ; « à partir de quel jour ? » ne l'est pas.",
        ],
        notes="Cinq minutes. Corriger deux ou trois questions à voix haute en les "
              "rendant plus précises : c'est l'exercice le plus utile de la séance, et "
              "il ne demande aucun matériel.")

    return d.save(dossier)
