# -*- coding: utf-8 -*-
"""E1 · À toi : commander et raconter.
Bloc E « Je me lance » · couleur teal · 90 min.
Source : dialogue `appli`, jeu de rôle et productions orale et écrite.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='À toi : commander et raconter',
        chapeau="Trois productions, dans l'ordre : un repas complet avec "
                "l'assistant, un repas raconté à voix haute, un restaurant "
                "recommandé par écrit.",
        duree='90 minutes')

    d.titre(notes="Séance de production. Prévoir les postes et les écouteurs. Rendre "
                  "d'abord les billets corrigés de B2, B4 et C2 : ce sont les brouillons.")

    d.objectifs([
        "commander un repas complet, à l'oral, avec un interlocuteur ;",
        "raconter un repas au restaurant en trois temps ;",
        "recommander un endroit par écrit ;",
        "me relire et me corriger avant d'envoyer.",
    ])

    d.dialogue('Le modèle', "Le midi, en semaine", [
        ("ANDRÉS", "Est-ce que le menu du midi est encore servi ?", True),
        ("SOPHIE", "Jusqu'à deux heures. Il vous reste vingt minutes.", False),
        ("ANDRÉS", "La soupe-repas, c'est quoi exactement ?", True),
        ("SOPHIE", "Une grosse soupe avec des légumes, des pâtes et du poulet. Servie avec du pain.", False),
    ], consigne="Repérez tout ce que vous avez appris dans ces quatre répliques.",
       notes="Faire chercher : une question sur une formule, une question sur un plat, le "
             "mot « exactement », et un accompagnement. Tout le module y est.")

    d.cartes('Production 1 · Le jeu de rôle', "Comment ça marche", [
        ("Tu choisis le moment",
         "La commande, pendant le repas, ou l'addition. Trois moments d'un même repas."),
        ("Tu choisis ton rôle",
         "Le client, ou le serveur. Servir est plus difficile : il faut répondre aux "
         "questions."),
        ("L'assistant ne récite pas le menu",
         "Il répond à ce que tu demandes. Il ne parlera pas du pourboire avant que tu ne "
         "poses la question."),
        ("Ton but",
         "Commander ce que tu veux vraiment, en sachant ce que ça comprend et ce que ça "
         "coûtera en tout."),
    ], notes="Vingt-cinq minutes. Rappeler les six questions du bloc B au tableau.")

    d.cartes('Production 2 · Un repas raconté', "Trois temps, quarante-cinq secondes", [
        ("Temps 1 · Où, avec qui, quelle occasion",
         "« C'était un petit restaurant du quartier, avec une collègue. »"),
        ("Temps 2 · Ce que tu as commandé",
         "« J'ai pris la table d'hôte : la soupe, la truite, et un dessert. »"),
        ("Temps 3 · Ce que tu en as pensé",
         "« C'était très bon. Le service était rapide. J'y retournerais. »"),
    ], notes="Le repas peut être ici ou dans le pays d'origine. Plusieurs élèves racontent "
             "un repas de fête : c'est très bien et souvent plus riche.")

    d.cartes('Production 3 · Une recommandation', "Par écrit", [
        ("Ce qu'elle doit contenir",
         "Le nom et l'endroit ; ce qu'on y mange, avec une formule ; le prix, à peu près ; "
         "un conseil pratique."),
        ("Ce qu'on vérifie",
         "Au moins une formule du menu — table d'hôte, menu du jour, à la carte — et une "
         "forme polie. Cinq à huit phrases."),
        ("Le conseil pratique",
         "« Réserve le vendredi », « arrive avant deux heures pour le menu du midi », "
         "« l'eau du robinet est servie en carafe ». C'est ce qui rend une recommandation "
         "utile."),
    ], notes="La troisième carte est ce qui distingue une vraie recommandation d'un avis "
             "général. L'exiger.")

    d.regle("Avant d'envoyer",
            "Relis-toi une fois, à voix basse.",
            precision="Trois choses à vérifier, toujours les mêmes : la forme polie — « je "
                      "voudrais » plutôt que « je veux » —, le nom exact de la formule, et "
                      "« s'il vous plaît » là où il manque. Ce sont les trois oublis du "
                      "module.",
            notes="Diapo à photographier. C'est la liste de vérification de tout le module.")

    d.piege("Recommander sans dire ce qu'on y mange",
            "C'est un bon restaurant, j'ai bien aimé.",
            "C'est un petit restaurant de quartier. La table d'hôte est à 32 $ : soupe, poisson du jour, dessert.",
            "Une recommandation sans détail ne sert à personne. Le nom d'une formule, un "
            "prix approximatif et un plat suffisent à donner une idée — et c'est exactement "
            "le vocabulaire du module.",
            notes="Faire comparer les deux versions à voix haute.")

    d.cartes("Ce que l'enseignant reçoit", "Et ce qu'il ne reçoit pas", [
        ("Le repas raconté",
         "Ton enregistrement et sa transcription, si tu choisis de les envoyer. Rien ne "
         "part tant que tu n'as pas cliqué."),
        ("La recommandation écrite",
         "Le texte que tu déposes, tel que tu l'as écrit. Tu peux le reprendre autant de "
         "fois que tu veux."),
        ("Ce qui n'est jamais conservé",
         "Les corrections de l'assistant et la conversation du jeu de rôle. Elles servent "
         "à t'entraîner, pas à t'évaluer."),
    ], notes="Le dire clairement, comme dans les autres modules.")

    d.billet(
        "Après avoir envoyé : notez une chose que vous corrigeriez si vous recommenciez.",
        exemples=[
            "Une seule chose, la plus importante pour vous.",
            "Exemple : « j'ai oublié de demander ce qui était servi avec ».",
        ],
        notes="Rendre annoté à la séance E2, où les élèves font leur autoévaluation.")

    return d.save(dossier)
