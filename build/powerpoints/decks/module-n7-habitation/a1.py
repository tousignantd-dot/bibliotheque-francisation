# -*- coding: utf-8 -*-
"""A1 · Trois semaines de cinq heures quarante-cinq
Bloc A « Je découvre » · couleur acier · compréhension orale · 75 min.
Séance d'ouverture.
Source : dialogue `prep`, exercice `prVF` et son bandeau de six mots.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Trois semaines de cinq heures quarante-cinq",
        chapeau="Un tapis roulant au-dessus d'une chambre, quarante minutes "
                "par matin, quinze jours de suite. Personne n'a rien brisé, "
                "et pourtant il y a un problème.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : "
                  "qui entend son voisin ? Tout le monde lève la main. Deuxième "
                  "question : qui lui en a parlé ? Presque personne. C'est là que le "
                  "module commence.")

    d.objectifs([
        "raconter un problème de bruit avec une heure et une durée ;",
        "distinguer ce qui se supporte de ce qui ne se supporte plus ;",
        "dire la conséquence d'un bruit sur sa vie plutôt que son émotion ;",
        "employer six mots du dossier avec leur article.",
    ], notes="Le deuxième objectif est le plus difficile et il tient tout le bloc : "
             "la loi ne promet le silence à personne, et il faut savoir de quel côté "
             "de la limite on se trouve.")

    d.declencheur(
        'Observation', "Qu'est-ce que tu entends de chez toi, et à quelle heure ?",
        pistes=[
            "Des pas, une porte, une musique, un chien, un appareil ?",
            "Le jour, le soir, ou la nuit ?",
            "Est-ce que ça revient tous les jours ?",
            "En as-tu déjà parlé à quelqu'un ?",
        ],
        notes="Question sans mauvaise réponse. Noter au tableau les heures qui "
              "sortent : elles serviront en A4 pour trier le normal de l'anormal.")

    d.dialogue('Dialogue · 1 de 3', "Vous avez une tête de déterrée", [
        ("MARLÈNE", "Ruslana, vous avez une tête de déterrée. Ça fait trois soirs que je vous le dis.", True),
        ("RUSLANA", "Je dors mal, Marlène. Je rentre à minuit et quart, je me couche vers une heure, et à cinq heures quarante-cinq je suis réveillée.", True),
        ("MARLÈNE", "Cinq heures quarante-cinq ? Vous avez un enfant qui se lève ?", True),
        ("RUSLANA", "Non. C'est le voisin du dessus. Il court sur un tapis roulant tous les matins de semaine, à peu près quarante minutes.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Écrire au tableau les trois nombres du dossier : 5 h 45, quarante "
             "minutes, quinze jours. Ils reviennent dans les quatre blocs et dans les "
             "deux lettres du bloc D.")

    d.dialogue('Dialogue · 2 de 3', "Ce n'est plus un petit dérangement", [
        ("MARLÈNE", "Et vous entendez quoi, exactement ?", True),
        ("RUSLANA", "Un bruit sourd, régulier. Le plafond vibre, le luminaire du salon bouge un peu. Je l'entends dans la chambre, qui est juste en dessous.", True),
        ("MARLÈNE", "Ça vous empêche de dormir depuis trois semaines, et vous travaillez avec des instruments stériles.", True),
        ("RUSLANA", "Jeudi, j'ai relu un plateau deux fois parce que je n'étais plus sûre de moi.", True),
    ], notes="Faire remarquer la dernière réplique : ce n'est plus une plainte, c'est "
             "une conséquence vérifiable. C'est tout le travail de la séance A3.")

    d.dialogue('Dialogue · 3 de 3', "Où est la limite ?", [
        ("RUSLANA", "Est-ce que j'ai le droit de me plaindre ? Il est chez lui. Il ne fait pas de fête, il ne crie pas. Il court.", True),
        ("MARLÈNE", "On doit accepter les inconvénients normaux du voisinage. Mais tous les matins pendant trois semaines, à cinq heures quarante-cinq, ce n'est plus normal.", True),
        ("RUSLANA", "Donc ce que je dois montrer, ce n'est pas que le bruit existe. C'est qu'il revient.", True),
        ("MARLÈNE", "Exactement. Notez-le. Chaque matin : la date, l'heure du début, l'heure de la fin, ce que vous avez entendu.", True),
    ], notes="La dernière réplique ouvre le module entier. Le geste utile du premier "
             "jour n'est pas de se plaindre : c'est d'écrire trois lignes.")

    d.tableau('Analyse', "Ce que Ruslana sait, et comment elle le sait",
              ['Le fait', "Comment elle l'a établi"],
              [["Le bruit commence à 5 h 45", "elle l'a noté chaque matin"],
               ["Il dure quarante minutes", "elle a noté la fin aussi"],
               ["Ça fait quinze jours", "elle a compté les lignes"],
               ["Le plafond vibre", "le luminaire du salon bouge"],
               ["Elle dort quatre heures", "elle se couche à une heure"]],
              cle=0,
              notes="Diapositive à photographier. Chaque ligne de gauche est un fait ; "
                    "chaque ligne de droite est la preuve. C'est le patron de tout le "
                    "module, et il revient dans la lettre du bloc D.")

    d.regle("La loi ne promet le silence à personne",
            "Les voisins doivent accepter les inconvénients normaux du voisinage.",
            precision="Des pas au-dessus de la tête, une porte qui claque, un enfant "
                      "qui court dix minutes : cela ne se plaide pas. Ce qui se plaide, "
                      "c'est ce qui dépasse — et ce qui dépasse se reconnaît à l'heure, "
                      "à la durée, à la répétition et à l'endroit.",
            notes="Diapositive à photographier. Insister sur le corollaire, qui est "
                  "rassurant : si la loi prévoit ce qu'il faut accepter, c'est qu'elle "
                  "prévoit aussi ce qu'il n'y a pas à accepter.")

    d.vocabulaire('Vocabulaire', "Six mots du problème", [
        ("un trouble de voisinage", "Le dérangement qu'une personne fait subir à celle qui habite à côté ou au-dessus."),
        ("une nuisance sonore", "Un bruit qui dépasse ce qu'une personne raisonnable accepterait."),
        ("la jouissance paisible", "Le droit d'habiter son logement tranquille."),
        ("un inconvénient normal", "Le petit dérangement que tout le monde subit en habitant près des autres."),
        ("un palier", "L'espace plat, devant les portes, où l'escalier s'arrête à chaque étage."),
        ("un registre des bruits", "Le carnet où l'on note chaque jour l'heure, la durée et ce qu'on entend."),
    ], notes="Faire répéter chaque mot avec son article. « La jouissance paisible » "
             "prend le défini : il n'y en a qu'une. Le faire remarquer.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la conversation de Ruslana et de Marlène.", [
        ("Ruslana entend le bruit surtout le soir, en rentrant.", "faux - le matin, à 5 h 45"),
        ("Le voisin court environ quarante minutes.", "vrai"),
        ("Ruslana a déjà parlé au voisin.", "faux - pas encore, et c'est le sujet du bloc B"),
        ("Elle entend aussi le vélo frapper la rampe de l'escalier.", "vrai"),
        ("Marlène lui conseille d'appeler tout de suite la propriétaire.", "faux - elle lui conseille de noter, puis de monter"),
        ("Selon Marlène, ce qu'il faut montrer, c'est que le bruit revient.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le troisième "
             "surprend : personne ne pense à commencer par le voisin.")

    d.billet(
        "Qu'est-ce que tu noterais ce soir, et à quel endroit ?",
        exemples=[
            "Une phrase suffit.",
            "Pense à un endroit que tu retrouveras dans six semaines.",
        ],
        notes="Deux minutes. Les réponses servent en A4 : elles montrent qui a compris "
              "que c'est la répétition qui fabrique la preuve.")

    return d.save(dossier)
