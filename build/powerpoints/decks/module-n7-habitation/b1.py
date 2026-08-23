# -*- coding: utf-8 -*-
"""B1 · Sur le palier du troisième
Bloc B « Défi 1 · Frapper à la porte d'en haut » · couleur acier ·
compréhension orale · 75 min.
Source : dialogue `t1`, exercice `t1vf` et son bandeau de quatre mots.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Sur le palier du troisième",
        chapeau="Une conversation de palier dure sept minutes et décide de "
                "tout ce qui suivra. Ruslana monte avec des heures, pas avec "
                "un reproche.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Rappeler la question de A4 : le voisin n'a "
                  "rien fait de mal. C'est ce qui rend la conversation difficile et "
                  "c'est ce que la séance travaille.")

    d.objectifs([
        "reconnaître ce qui ouvre une conversation et ce qui la ferme ;",
        "décrire un bruit avec une heure, une durée et un nombre de jours ;",
        "entendre une concession et une demande au conditionnel ;",
        "employer quatre mots de la négociation entre voisins.",
    ], notes="Le premier objectif est le plus utile hors du cours. Le poser dès la "
             "première diapositive et y revenir à chaque réplique.")

    d.declencheur(
        'Observation', "Tu montes parler à ton voisin. Par quoi commences-tu ?",
        pistes=[
            "Par ton nom, par le problème, ou par une excuse ?",
            "Est-ce que tu dis tout de suite ce que tu veux ?",
            "Qu'est-ce qui se passe si tu commences par « vous faites du bruit » ?",
            "Qu'est-ce que tu apportes avec toi ?",
        ],
        notes="Laisser trois ou quatre réponses. Presque personne ne pense à apporter "
              "des heures : c'est ce que la première réplique de Ruslana montre.")

    d.dialogue('Dialogue · 1 de 4', "Je viens vous le dire en personne", [
        ("RUSLANA", "Bonsoir. Excusez-moi de vous déranger à cette heure-ci — vous êtes bien monsieur Rondeau ?", True),
        ("CÉDRIC", "Cédric, oui. Vous êtes du quatre, en dessous ?", True),
        ("RUSLANA", "Je viens vous parler de quelque chose, et j'aime mieux venir vous le dire en personne que de le faire dire par quelqu'un d'autre.", True),
        ("CÉDRIC", "Ah. C'est le tapis roulant. Je m'en doutais un peu, pour être honnête.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Trois choses en quatre répliques : elle salue, elle se nomme, elle dit "
             "pourquoi elle vient. Faire compter les secondes : sept, pas plus.")

    d.dialogue('Dialogue · 2 de 4', "Je les ai comptés", [
        ("RUSLANA", "Je travaille de trois heures et demie à onze heures et demie du soir. Je rentre vers minuit et quart.", True),
        ("RUSLANA", "Et à cinq heures quarante-cinq, ça commence au-dessus de ma chambre. Je note ça depuis le 4 février : ce matin, c'était le quinzième jour de suite.", True),
        ("CÉDRIC", "Quinze jours de suite. Vous les avez comptés.", True),
        ("RUSLANA", "Je les ai comptés parce que je ne voulais pas venir vous dire « vous faites du bruit ». Je voulais venir avec des heures.", True),
    ], notes="La dernière réplique est la phrase-clé du bloc. La faire répéter par "
             "deux élèves, puis demander la différence entre les deux formulations.")

    d.dialogue('Dialogue · 3 de 4', "Même si votre horaire est difficile", [
        ("CÉDRIC", "Je pars à l'atelier à sept heures moins le quart. C'est le seul moment de la journée où je peux courir.", True),
        ("RUSLANA", "Je vous crois. Et même si votre horaire est difficile, le mien l'est aussi — c'est ça, notre problème.", True),
        ("CÉDRIC", "Bien que je coure tôt, je ne mets pas de musique, je ne fais pas de poids. Je pensais que c'était acceptable.", True),
        ("RUSLANA", "Le bruit est tellement régulier qu'il finit par me réveiller avant même qu'il commence.", True),
    ], notes="Trois points de langue du défi sont dans ces quatre répliques : « même "
             "si », « bien que » et « tellement… que ». Les faire repérer sans les "
             "expliquer : B2 et B3 s'en chargent.")

    d.dialogue('Dialogue · 4 de 4', "Deux choses, et elles sont petites", [
        ("RUSLANA", "Est-ce que vous accepteriez de reculer d'une heure ?", True),
        ("CÉDRIC", "Impossible. Je pars travailler à ce moment-là. Ça, je ne peux pas.", True),
        ("RUSLANA", "Alors la deuxième : est-ce que vous seriez prêt à mettre le tapis sur un tapis de caoutchouc ?", True),
        ("CÉDRIC", "Le caoutchouc, on en a des rouleaux à l'atelier. Ça, je peux.", True),
    ], notes="Deux demandes, une refusée et une acceptée. Faire remarquer qu'elle en "
             "avait préparé deux : c'est ce qui sauve la conversation.")

    d.tableau('Analyse', "Ce qui ouvre la porte, ce qui la ferme",
              ['Ça ferme', 'Ça ouvre'],
              [["Vous faites du bruit.", "Ça commence à 5 h 45 et ça dure 40 minutes."],
               ["Vous êtes sans-gêne.", "Cela m'empêche de dormir plus de 4 heures."],
               ["Arrêtez de courir.", "Accepteriez-vous de mettre du caoutchouc ?"],
               ["Il faut que ça change.", "Je vous propose deux choses."],
               ["C'est insupportable.", "Je ne me plains que du matin."]],
              cle=1,
              notes="Diapositive à photographier. La colonne de droite est le plan de "
                    "la conversation du jeu de rôle, au bloc E.")

    d.vocabulaire('Vocabulaire', "Quatre mots de la conversation", [
        ("un arrangement à l'amiable", "Une solution que deux personnes trouvent elles-mêmes, sans juge et sans papier officiel."),
        ("une concession", "Ce qu'une personne accepte de lâcher pour que l'autre accepte quelque chose à son tour."),
        ("un reproche", "Ce qu'on dit à quelqu'un pour lui signifier qu'il a mal agi."),
        ("un palier", "L'espace plat, devant les portes, où l'escalier s'arrête à chaque étage."),
    ], notes="« Un arrangement à l'amiable » : faire remarquer l'expression figée, qui "
             "ne se démonte pas. On ne dit pas « un arrangement amiable ».")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la conversation sur le palier.", [
        ("Ruslana commence par dire qu'elle a compté quinze matins.", "faux - elle salue et se nomme d'abord"),
        ("Cédric se doutait déjà que le tapis s'entendait en bas.", "vrai"),
        ("Cédric accepte de reculer son entraînement d'une heure.", "faux - il part travailler à ce moment-là"),
        ("Ruslana lui demande d'arrêter complètement de courir.", "faux - elle dit qu'elle n'en a pas le droit"),
        ("Cédric ignorait que son vélo faisait du bruit dans l'escalier.", "vrai"),
        ("Les deux se donnent deux semaines avant de se reparler.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le quatrième "
             "surprend : elle ne demande pas ce qu'elle n'a pas le droit d'obtenir.")

    d.billet(
        "Écris la première phrase que tu dirais en montant chez ton voisin.",
        exemples=[
            "Une seule phrase.",
            "Regarde la colonne de droite du tableau avant d'écrire.",
        ],
        notes="Deux minutes. Ramasser et relire deux ou trois réponses à voix haute au "
              "début de B2 : la différence entre elles se voit tout de suite.")

    return d.save(dossier)
