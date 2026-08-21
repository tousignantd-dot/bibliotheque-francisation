# -*- coding: utf-8 -*-
"""B2 · Les huit questions à poser.
Bloc B « Défi 1 · L'appel » · couleur acier · 75 min.
Source : exercice `t1questions`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='acier',
        titre="Les huit questions à poser",
        chapeau="Un appel de quatre minutes bien mené évite une visite "
                "inutile à l'autre bout de la ville. Encore faut-il savoir "
                "quoi demander — et l'avoir écrit avant.",
        duree='75 minutes')

    d.titre(notes="Séance de production orale. Commencer par ramasser les feuilles de "
                  "questions du devoir B1 et en lire trois à voix haute, sans nommer les "
                  "auteurs. Le groupe complète.")

    d.objectifs([
        "poser huit questions précises sur un logement ;",
        "savoir ce que chaque question sert à apprendre ;",
        "formuler une question polie et directe à la fois ;",
        "poser la question que personne n'ose poser.",
    ])

    d.declencheur(
        'Discussion', "Vous avez quatre minutes au téléphone. Que demandez-vous ?",
        pistes=[
            "Quelle est la première question ?",
            "Et si vous n'aviez le droit qu'à trois questions ?",
            "Qu'est-ce qu'on oublie toujours de demander ?",
            "Qu'est-ce qu'on n'ose pas demander ?",
        ],
        notes="Noter au tableau toutes les questions proposées, sans trier. On les classe "
              "ensuite avec le tableau suivant. Les élèves proposent presque toujours le "
              "prix en premier — or le prix est déjà dans l'annonce.")

    d.tableau('Les questions · 1 de 2', "Ce qui coûte de l'argent",
              ['La question', 'Ce qu\'elle vous apprend'],
              [["Le chauffage est-il inclus ?", "si le loyer est le prix final"],
               ["Quels électroménagers sont fournis ?", "s'il faudra en acheter"],
               ["Le stationnement est-il inclus ?", "si l'auto aura une place l'hiver"],
               ["Depuis quand le loyer n'a-t-il pas augmenté ?", "si la hausse à venir sera raisonnable"]],
              cle=0,
              note="Le prix n'est pas dans la liste : il est déjà dans l'annonce.",
              notes="Diapositive à photographier. La dernière ligne est celle que presque "
                    "personne ne connaît.")

    d.tableau('Les questions · 2 de 2', "Ce qui décide de la vie quotidienne",
              ['La question', 'Ce qu\'elle vous apprend'],
              [["Y a-t-il une buanderie ?", "où vous laverez votre linge"],
               ["Quelle est la date d'occupation ?", "quand le bail commence"],
               ["L'immeuble est-il bien insonorisé ?", "si vous dormirez bien"],
               ["Les animaux sont-ils acceptés ?", "si vous gardez votre chat"]],
              cle=0,
              note="La question des animaux se pose tôt : elle est éliminatoire ou non.",
              notes="Diapositive à photographier. C'est le cœur du défi 1 et l'outil que "
                    "les élèves emporteront.")

    d.regle("Demandez depuis quand le loyer n'a pas augmenté",
            "La question qui surprend les propriétaires — et qui est parfaitement légitime.",
            precision="Le propriétaire doit de toute façon inscrire au bail le loyer le "
                      "plus bas payé dans les douze derniers mois. En le demandant au "
                      "téléphone, vous savez d'avance si le prix demandé est un bond ou "
                      "une hausse normale.",
            notes="Diapositive à photographier. Prévenir : certains propriétaires seront "
                  "surpris, quelques-uns seront agacés. C'est un droit, et un propriétaire "
                  "que la question fâche est déjà un renseignement.")

    d.cartes("Comment formuler", "Poli et direct à la fois", [
        ("Annoncez d'abord",
         "« J'aimerais vous poser quelques questions, si vous avez deux minutes. »"),
        ("Une question à la fois",
         "Deux questions ensemble et vous n'aurez la réponse qu'à la deuxième."),
        ("Demandez un chiffre",
         "« Comptez combien par mois l'hiver ? » plutôt que « c'est cher à chauffer ? »"),
        ("Gardez la plus délicate pour la fin",
         "Le loyer de l'ancien locataire se demande une fois le reste établi."),
    ], notes="La deuxième carte est la plus utile : les élèves enchaînent souvent deux ou "
             "trois questions par peur du silence, et perdent les réponses.")

    d.pratique('Formulation', "Posez la question",
               "Écrivez la question qui permet d'apprendre chaque chose.", [
        ("Si le loyer est vraiment le prix final",
         "Est-ce que le chauffage et l'électricité sont inclus ?"),
        ("S'il faudra acheter un réfrigérateur",
         "Quels électroménagers sont fournis ?"),
        ("Où laver son linge", "Est-ce qu'il y a une buanderie dans l'immeuble ?"),
        ("Si l'auto aura une place", "Le stationnement est-il inclus dans le loyer ?"),
        ("Quand le bail commence", "Quelle est la date d'occupation ?"),
        ("Si on dormira bien", "Est-ce que l'immeuble est bien insonorisé ?"),
        ("Si la prochaine hausse sera raisonnable",
         "Depuis quand le loyer n'a-t-il pas augmenté ?"),
        ("Si on garde son chat", "Est-ce que les animaux sont acceptés ?"),
    ], corrige=True,
       notes="Accepter toute formulation correcte et polie. L'important est la précision "
             "de ce qui est demandé, pas la tournure exacte.")

    d.piege("Enchaîner les questions par peur du silence",
            "Le chauffage est inclus, et les électroménagers, et le stationnement ?",
            "Une question. On attend la réponse. On note. Question suivante.",
            "Trois questions d'un coup : la personne répond à la dernière, ou à celle "
            "qu'elle préfère. Le silence pendant que vous écrivez est normal — vous avez "
            "d'ailleurs annoncé que vous preniez des notes.",
            notes="Faire vivre l'erreur : poser les trois questions d'un trait à un élève "
                  "et lui demander de répondre. Il ne répondra qu'à une.")

    d.pratique('Jeu de rôle', "Deux par deux, dos à dos",
               "L'un a l'annonce, l'autre a les réponses. Quatre minutes, puis on inverse.", [
        ("Le 4 ½ de la rue Bowen", "1 050 $, N/C, 1er juillet, buanderie, 1 stationnement"),
        ("Le 3 ½ du centre-ville", "690 $, C/E, meublé, pas de buanderie, pas de stationnement"),
        ("Le 5 ½ de Fleurimont", "1 390 $, N/C, 1er juillet, 2 stationnements, pas d'électroménagers"),
    ], corrige=False,
       notes="Dos à dos : c'est la seule façon de reproduire le téléphone en classe. "
             "Circuler et noter les questions oubliées, sans interrompre. Faire le bilan "
             "des oublis à la fin, au tableau, sans nommer personne.")

    d.billet(
        "Appelez pour une des trois annonces que vous avez trouvées.",
        exemples=[
            "Posez au moins cinq des huit questions.",
            "Notez les réponses. Nous les lirons ensemble à la séance B4.",
        ],
        notes="Devoir réel, et le plus exigeant du module. Prévenir que certains "
              "n'oseront pas : proposer de faire l'appel en classe, à côté de "
              "l'enseignante, à ceux qui le demandent.")

    return d.save(dossier)
