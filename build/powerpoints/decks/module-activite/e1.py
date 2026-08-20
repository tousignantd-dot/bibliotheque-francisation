# -*- coding: utf-8 -*-
"""E1 · À toi : s'informer et expliquer.
Bloc E « Je me lance » · couleur teal · 90 min.
Source : dialogue `appli`, jeu de rôle et productions orale et écrite.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="À toi : s'informer et expliquer",
        chapeau="Trois productions, dans l'ordre : une conversation au "
                "comptoir avec l'assistant, une activité expliquée à voix "
                "haute, un courriel à sa ville.",
        duree='90 minutes')

    d.titre(notes="Séance de production. Prévoir les postes et les écouteurs. Rendre "
                  "d'abord les billets corrigés de A3, B2 et C2 : ce sont les brouillons.")

    d.objectifs([
        "m'informer sur une activité, à l'oral, avec un interlocuteur ;",
        "expliquer une activité que je connais en donnant de vraies consignes ;",
        "écrire à ma ville pour poser mes questions ;",
        "me relire et me corriger avant d'envoyer.",
    ])

    d.dialogue('Le modèle', "S'inscrire à la chorale", [
        ("ROSA", "Est-ce qu'il faut savoir lire la musique ?", True),
        ("LOUISE", "Pas du tout. Il est important d'avoir envie de chanter, c'est tout.", True),
        ("ROSA", "Trente dollars, c'est bien ça ?", True),
        ("LOUISE", "Trente pour les résidents. Avez-vous votre preuve d'adresse avec vous ?", False),
    ], consigne="Repérez tout ce que vous avez appris dans ces quatre répliques.",
       notes="Faire chercher : une question sur les conditions, une forme impersonnelle, "
             "un montant qu'on fait confirmer, une question sur les documents. Tout le "
             "module y est.")

    d.cartes('Production 1 · Le jeu de rôle', "Comment ça marche", [
        ("Tu choisis l'activité",
         "La natation pour un enfant, la chorale pour toi, ou le soccer. Trois situations "
         "ordinaires."),
        ("Tu choisis ton rôle",
         "La personne qui s'informe, ou celle au comptoir. Les deux sont utiles : "
         "renseigner quelqu'un est plus difficile."),
        ("L'assistant ne déroule pas la fiche",
         "Il répond à ce que tu demandes, rien de plus. Si tu oublies le matériel "
         "obligatoire, il ne te le dira pas de lui-même."),
        ("Ton but",
         "Tout savoir avant de partir, pour ne pas avoir à revenir. Les six questions de "
         "A3 sont ta liste."),
    ], notes="Vingt-cinq minutes. Passer dans les rangées. Rappeler les six questions au "
             "tableau — beaucoup d'élèves en oublient deux.")

    d.cartes('Production 2 · Expliquer une activité', "Trois temps, quarante-cinq secondes", [
        ("Temps 1 · Ce qu'il faut avoir",
         "« Il faut un ballon et deux équipes de cinq. Il est important d'avoir de bons "
         "souliers. »"),
        ("Temps 2 · Les consignes, à l'impératif",
         "« Prends le ballon à deux mains. Ne le lâche pas. Regarde-moi. »"),
        ("Temps 3 · Ce qu'il ne faut pas faire",
         "« Ne cours pas sur le bord. Sortez par l'échelle, pas par le bord. »"),
    ], notes="L'activité est libre : un sport, un jeu, une danse, une recette. Les billets "
             "de A4, B2 et C2 contiennent déjà tout le matériel.")

    d.cartes('Production 3 · Le courriel', "À ta ville", [
        ("Ce qu'il doit contenir",
         "L'activité qui t'intéresse ; pour qui, et l'âge ; trois questions précises ; une "
         "formule pour terminer."),
        ("Ce qu'on vérifie",
         "Au moins une fois « il faut » ou « il est important de », et une comparaison "
         "avec « le plus » ou « le moins ». Cinq à huit phrases."),
        ("Le registre",
         "Standard, toujours, même si vous connaissez la personne. C'est un courriel à un "
         "service."),
    ], notes="Le billet de D2 sur le registre est le brouillon direct de cette production. "
             "Le rappeler.")

    d.regle("Avant d'envoyer",
            "Relis-toi une fois, à voix basse.",
            precision="Trois choses à vérifier, toujours les mêmes : le singulier après "
                      "« chaque », la place du pronom à l'impératif, et l'accord du petit "
                      "mot au superlatif. Ce sont les trois fautes du module.",
            notes="Diapo à photographier. C'est la liste de vérification de tout le module.")

    d.piege("Écrire un courriel en registre familier",
            "Salut ! Ça coûte combien, votre affaire de natation ?",
            "Bonjour, j'aimerais des renseignements sur le cours de natation pour enfants.",
            "Un courriel à un service se écrit en registre standard, même si la personne "
            "au téléphone vous a tutoyé. Ce n'est pas de la froideur : c'est ce qu'on "
            "attend d'un message écrit à quelqu'un qu'on ne connaît pas.",
            notes="Faire trouver les trois différences par le groupe avant d'afficher la "
                  "colonne de droite.")

    d.cartes("Ce que l'enseignant reçoit", "Et ce qu'il ne reçoit pas", [
        ("L'activité expliquée",
         "Ton enregistrement et sa transcription, si tu choisis de les envoyer. Rien ne "
         "part tant que tu n'as pas cliqué."),
        ("Le courriel",
         "Le texte que tu déposes, tel que tu l'as écrit. Tu peux le reprendre autant de "
         "fois que tu veux."),
        ("Ce qui n'est jamais conservé",
         "Les corrections de l'assistant et la conversation du jeu de rôle. Elles servent "
         "à t'entraîner, pas à t'évaluer."),
    ], notes="Le dire clairement. Plusieurs élèves n'osent pas se tromper devant "
             "l'assistant parce qu'ils croient que tout est vu.")

    d.billet(
        "Après avoir envoyé : notez une chose que vous corrigeriez si vous recommenciez.",
        exemples=[
            "Une seule chose, la plus importante pour vous.",
            "Exemple : « j'ai oublié de demander ce qu'il faut apporter ».",
        ],
        notes="Rendre annoté à la séance E2, où les élèves font leur autoévaluation.")

    return d.save(dossier)
