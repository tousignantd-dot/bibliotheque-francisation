# -*- coding: utf-8 -*-
"""E1 · À toi : la rencontre et le récit.
Bloc E « Je me lance » · couleur teal · 90 min.
Source : dialogue `appli`, jeu de rôle et productions orale et écrite du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='À toi : la rencontre et le récit',
        chapeau="Trois productions, dans l'ordre : une conversation avec "
                "l'assistant, un récit enregistré, une carte écrite. La "
                "conversation sert de répétition aux deux autres.",
        duree='90 minutes')

    d.titre(notes="Séance de production. Prévoir les postes et les écouteurs. Rendre "
                  "d'abord les billets corrigés de B1, C2 et D2 : ce sont les brouillons.")

    d.objectifs([
        "faire connaissance avec quelqu'un dans une activité de loisir ;",
        "raconter une expérience personnelle en trois temps ;",
        "écrire une carte postale ou une carte de vœux ;",
        "me relire et me corriger avant d'envoyer.",
    ])

    d.dialogue('Le modèle', 'Au tournoi de Drummondville', [
        ("OLIVIER", "Qu'est-ce que tu faisais, cette année-là ?", False),
        ("MARIAMA", "Des cours de français le matin et du travail le soir. Le samedi, je dormais.", True),
        ("OLIVIER", "Et là, tu joues combien de fois par semaine ?", False),
        ("MARIAMA", "Une seule. Le jeudi. Mais je m'entraîne toute seule le dimanche, au parc où mes enfants jouent.", True),
    ], consigne="Voici la fin du dialogue commencé en B4. Repérez tout ce que vous avez appris.",
       notes="Faire chercher : une question ouverte, un imparfait, un passé composé, un "
             "« où », un verbe pronominal, une fréquence. Tout le module tient dans ces "
             "quatre répliques.")

    d.cartes('Production 1 · Le jeu de rôle', "Comment ça marche", [
        ("Tu choisis la situation",
         "Le volleyball du jeudi, la cuisine collective du samedi, ou la marche du "
         "dimanche. Trois activités de quartier bien réelles."),
        ("Tu choisis ton rôle",
         "La personne qui arrive pour la première fois, ou celle qui accueille. Les deux "
         "sont utiles à pratiquer."),
        ("L'assistant ne sait rien de toi",
         "Il ne racontera rien avant que tu poses des questions. C'est fait exprès : "
         "c'est toi qui mènes."),
        ("Ton but",
         "Apprendre trois choses sur l'autre, raconter une chose sur toi, et proposer de "
         "se revoir."),
    ], notes="Vingt-cinq minutes. Passer dans les rangées. Les élèves qui bloquent ont "
             "presque toujours oublié de poser une question : leur rappeler les cinq mots "
             "de B3.")

    d.cartes('Production 2 · Le récit oral', "Trois temps, quarante-cinq secondes", [
        ("Temps 1 · Le décor, à l'imparfait",
         "« C'était en janvier. Il faisait trente degrés chez moi et je portais des "
         "sandales. »"),
        ("Temps 2 · Les évènements, au passé composé",
         "« Je suis arrivée le douze janvier. J'ai eu mal aux oreilles en sortant. »"),
        ("Temps 3 · Ce que ça a changé",
         "« Grâce à une voisine, j'ai compris qu'on pouvait aimer l'hiver. »"),
    ], notes="Le sujet est libre : une arrivée, un déménagement, un voyage, un mariage, "
             "une naissance. Redire que personne n'est obligé de raconter quelque chose de "
             "difficile.")

    d.cartes('Production 3 · La carte', "Postale ou vœux, au choix", [
        ("Ce qu'elle doit contenir",
         "Une salutation ; où tu es ou quelle est l'occasion ; ce que tu as fait ou ce que "
         "tu souhaites ; une fin et ta signature."),
        ("Ce qu'on vérifie",
         "Au moins une fois qui, que ou où. Au moins un verbe au passé composé. Cinq à "
         "huit phrases."),
        ("Avant d'envoyer",
         "Relis-toi une fois à voix basse. Les fautes qu'on entend sont celles qu'on "
         "corrige le plus vite."),
    ], notes="Les élèves peuvent reprendre la carte écrite au billet de D2 : elle a déjà "
             "été corrigée. Le leur dire — c'est du temps gagné pour l'oral.")

    d.regle("Avant d'envoyer",
            "Relis-toi une fois, à voix basse, avant de cliquer.",
            precision="Trois choses à vérifier, toujours les mêmes : l'accord du participe "
                      "avec être, la place de l'adverbe et du pronom y, et le « ne » de "
                      "jamais. Ce sont les trois fautes du module.",
            notes="Diapo à photographier. C'est la liste de vérification de tout le module.")

    d.piege('Envoyer sans se relire',
            "Je suis arrivé en janvier et j'ai jamais vu la neige avant.",
            "Je suis arrivée en janvier et je n'avais jamais vu la neige avant.",
            "Deux fautes en une phrase, toutes deux corrigeables en dix secondes de "
            "relecture : l'accord du participe avec être, et le « ne » de jamais. La "
            "relecture n'est pas un luxe, c'est la moitié du travail d'écriture.",
            notes="Faire trouver les deux fautes par le groupe avant d'afficher la colonne "
                  "de droite.")

    d.cartes("Ce que l'enseignant reçoit", "Et ce qu'il ne reçoit pas", [
        ("La prise orale",
         "Ton enregistrement et sa transcription, si tu choisis de les envoyer. Rien ne "
         "part tant que tu n'as pas cliqué."),
        ("La carte écrite",
         "Le texte que tu déposes, tel que tu l'as écrit. Tu peux le reprendre autant de "
         "fois que tu veux avant d'envoyer."),
        ("Ce qui n'est jamais conservé",
         "Les corrections de l'assistant et la conversation du jeu de rôle. Elles servent "
         "à t'entraîner, pas à t'évaluer."),
    ], notes="Le dire clairement au groupe. Plusieurs élèves n'osent pas se tromper devant "
             "l'assistant parce qu'ils croient que tout est vu. Ce n'est pas le cas.")

    d.billet(
        "Après avoir envoyé : notez une chose que vous corrigeriez si vous recommenciez.",
        exemples=[
            "Une seule chose, la plus importante pour vous.",
            "Exemple : « j'ai oublié d'accorder le participe avec être ».",
        ],
        notes="Ce billet vaut mieux qu'une note. Le rendre annoté à la séance E2, où les "
              "élèves font leur autoévaluation.")

    return d.save(dossier)
