# -*- coding: utf-8 -*-
"""C1 · La chronique en trois écoutes
Bloc C « Défi 2 · L'éditorial et sa thèse » · couleur acier · 75 min.
Source : dialogue `t2` (la chronique de Grégoire Ferland), exercices `t21` et
`t2trois`, mini-leçon `t2trois`. C'est l'écoute longue du module : douze
répliques d'affilée du même locuteur, coupées à la fin par deux questions.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n8-actualite' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Douze minutes, et personne pour vous attendre",
        chapeau="Un chroniqueur de radio parle seul, vite, et ne reformule "
                "jamais. On ne suit pas un exposé en essayant de tout "
                "comprendre : on le suit en trois écoutes, avec une consigne "
                "différente chaque fois.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc C. Prévenir tout de suite que l'extrait est "
                  "long et rapide : c'est voulu. La voix de Grégoire Ferland n'est "
                  "pas ralentie, contrairement à celle des autres personnages du "
                  "module — le débit d'une chronique de radio est précisément ce que "
                  "la séance fait travailler. Ne pas s'en excuser auprès du groupe : "
                  "l'annoncer comme l'objet du jour.")

    d.objectifs([
        "suivre un exposé de douze minutes sans interlocuteur ;",
        "trouver la position de l'auteur dans les trente premières secondes ;",
        "noter trois ou quatre chiffres avec ce qu'ils recouvrent ;",
        "repérer ce qui est dit deux fois, et en tirer la vraie thèse.",
    ], notes="Le quatrième objectif surprend et il est le plus rentable : dans un "
             "texte préparé, une répétition n'est jamais un hasard.")

    d.declencheur(
        'Observation', "Que retenez-vous de douze minutes de radio ?",
        image=IMG + 'studio-radio.jpg',
        pistes=[
            "Combien de chiffres pouvez-vous retenir sans rien écrire ?",
            "Que faites-vous quand un mot vous échappe au milieu d'une phrase ?",
            "Écoutez-vous pour comprendre, ou pour préparer votre réponse ?",
            "À quel moment décidez-vous si la personne est pour ou contre ?",
        ],
        notes="La troisième question est celle qui ouvre la séance. Presque tout le "
              "monde prépare sa réplique et cesse d'entendre. Le dire sans reproche : "
              "c'est ce qui fait qu'on répond à côté dans les tribunes.")

    d.regle("Trois écoutes, trois consignes",
            "Première écoute : quelle est sa position ? Deuxième écoute : "
            "quels sont les chiffres ? Troisième écoute : qu'est-ce qui est "
            "dit deux fois ?",
            precision="Une seule consigne par écoute. Celui qui cherche tout à la "
                      "fois ne trouve rien et abandonne à la quatrième minute. Ce "
                      "découpage est ce que le programme du niveau 8 appelle "
                      "« suivre le déroulement d'exposés bien structurés » : ce n'est "
                      "pas un truc, c'est un savoir-faire d'écoute.",
            notes="Diapositive à photographier. L'écrire aussi au tableau et la "
                  "laisser pendant toute la séance : on y revient trois fois.")

    d.dialogue('Écoute 1 de 3', "De quel côté est-il ?", [
        ("GRÉGOIRE", "Ma chronique de la semaine. Elle sera longue, et je vous préviens tout de suite : je vais vous dire ce que je pense, ce qui n'est pas mon travail habituel.", True),
        ("GRÉGOIRE", "Je suis pour le projet du boisé Sainte-Perpétue. Voilà. Vous savez maintenant dans quel sens lire ce qui suit, et vous avez le droit de fermer la radio.", True),
        ("GRÉGOIRE", "Trois raisons. La première est un chiffre que personne ne conteste.", True),
    ], consigne="Première écoute : cherchez une seule chose, sa position.",
       notes="Interdire la prise de notes à cette écoute-là. La position arrive en "
             "trente secondes, comme presque toujours dans une chronique d'opinion. "
             "Faire remarquer « je vous préviens tout de suite » et « trois "
             "raisons » : ce sont des charnières, elles annoncent la suite.")

    d.dialogue('Écoute 2 de 3', "Les chiffres, et ce qu'ils recouvrent", [
        ("GRÉGOIRE", "Le taux d'inoccupation des logements locatifs de la ville est de zéro virgule trois pour cent. Trois logements libres sur mille.", True),
        ("GRÉGOIRE", "Les quarante-cinq logements abordables sont écrits dans le règlement, avec une pénalité de deux millions si le promoteur ne les livre pas.", True),
        ("GRÉGOIRE", "Depuis quinze ans, chaque fois qu'on a proposé du logement dense ici, un comité s'est formé et le projet est mort. Cinq fois sur cinq.", True),
        ("GRÉGOIRE", "La Ville a voté quatre jours après avoir reçu l'évaluation du terrain. Quatre jours.", True),
    ], consigne="Deuxième écoute : notez les nombres, et ce à quoi chacun se rapporte.",
       notes="Trois ou quatre chiffres suffisent. Un chiffre noté sans son unité ni ce "
             "qu'il mesure est pire que rien. Faire comparer les notes par deux : les "
             "écarts se voient tout de suite.")

    d.dialogue('Écoute 3 de 3', "Ce qui revient, et ce qu'il demande", [
        ("GRÉGOIRE", "Maintenant, la partie où je me contredis, parce qu'un chroniqueur qui ne se contredit jamais est un chroniqueur qui ne lit rien.", True),
        ("GRÉGOIRE", "On ne vend pas un bien public en quatre jours, et surtout pas à vingt-deux heures cinquante devant onze personnes.", True),
        ("GRÉGOIRE", "Ce que je souhaite, c'est que le registre atteigne son nombre. Je suis pour le projet et je souhaite qu'il y ait un référendum.", True),
        ("MIRELA", "Vous dites que le projet est bon, mais vous voulez un référendum. Si le référendum le rejette, qu'est-ce que vous aurez gagné ?", True),
        ("GRÉGOIRE", "Excellente question, et je n'ai pas de bonne réponse. Je peux me tromper.", True),
    ], consigne="Troisième écoute : qu'est-ce qui est dit deux fois, et pourquoi ?",
       notes="« Vingt-deux heures cinquante » et « onze personnes » reviennent trois "
             "fois dans la chronique. Ce n'est pas une redite : c'est sa vraie "
             "question, qui est la procédure et non le boisé. Faire remarquer que sa "
             "conclusion n'est pas la répétition de sa thèse — il est pour le projet "
             "et il souhaite un référendum.")

    d.tableau('Analyse', "Une grille d'écoute en cinq lignes",
              ['Moment', "Ce qu'on y note"],
              [["avant d'écouter", "qui parle, et sur quel média"],
               ["première écoute", "la position, en une phrase"],
               ["deuxième écoute", "trois ou quatre chiffres, avec leur unité"],
               ["troisième écoute", "ce qui revient, et la concession"],
               ["après", "une seule question à poser, écrite en entier"]],
              cle=0,
              notes="Diapositive à photographier. Cette grille sert pour n'importe "
                    "quel exposé long : un discours, une conférence, une réunion "
                    "syndicale. La faire recopier au propre dans le cahier.")

    d.pratique('Pratique 1 de 2', "Vrai ou faux ?",
               "Répondez d'après la chronique.", [
        ("Grégoire Ferland annonce sa position dès le début.", "vrai"),
        ("Il est contre le projet du boisé.", "faux - il est pour"),
        ("Le taux d'inoccupation est de zéro virgule trois pour cent.", "vrai"),
        ("Les quarante-cinq logements reposent sur une promesse verbale.", "faux - ils sont au règlement"),
        ("Il refuse de reconnaître le moindre point au comité.", "faux - il lui donne raison deux fois"),
        ("Il souhaite que le registre atteigne son nombre.", "vrai"),
        ("Il admet qu'un référendum pourrait faire perdre les logements.", "vrai"),
        ("Mirela lui reproche de se contredire, et il le nie.", "faux - il l'admet"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Les deux "
             "derniers sont les plus intéressants : ils portent sur l'honnêteté du "
             "chroniqueur, pas sur les faits.")

    d.pratique('Pratique 2 de 2', "Il affirme, il concède, il demande",
               "Pour chaque phrase entendue, dites ce qu'elle fait dans le raisonnement.", [
        ("Le taux d'inoccupation est de zéro virgule trois pour cent.", "il affirme"),
        ("Le comité a raison sur un point, et il a raison durement.", "il concède"),
        ("Ce que je souhaite, c'est que le registre atteigne son nombre.", "il demande"),
        ("On ne vend pas un bien public en quatre jours.", "il concède"),
        ("Cinq projets de logement dense sont morts en quinze ans.", "il affirme"),
        ("Le terrain derrière l'aréna n'a jamais été étudié sérieusement.", "il concède"),
        ("Vous avez le droit de m'appeler et de me dire que je me contredis.", "il demande"),
    ], corrige=True,
       notes="C'est l'exercice `t2trois` du module. Le classement compte moins que la "
             "justification : demander à quoi on reconnaît une concession. La réponse "
             "est qu'elle donne raison à l'autre camp, et qu'elle est suivie d'un "
             "« mais » ou de rien du tout.")

    d.piege('Piège', "Tout noter pendant les douze minutes",
            "Noter cinq choses seulement",
            "Celui qui écrit tout n'écoute plus. Une page de notes pour douze "
            "minutes est le signe que l'écoute a échoué. Même règle pour un "
            "mot inconnu : s'arrêter dessus coûte le reste de l'exposé. On le "
            "note au vol dans la marge et on rattrape le fil.",
            notes="Le dire au moment où les cahiers se remplissent, pas avant. "
                  "Beaucoup d'élèves croient bien faire en transcrivant, et personne "
                  "ne le leur a jamais dit autrement.")

    d.billet(
        "Écoutez une chronique ou un discours de dix minutes et notez cinq choses.",
        exemples=[
            "La position en une phrase, trois chiffres, et ce qui revient.",
            "Puis une seule question à poser, écrite en entier.",
        ],
        notes="Devoir. La question écrite en entier sert au bloc D, où l'on "
              "intervient à la tribune. Une question improvisée à l'antenne se perd ; "
              "une question écrite tient en vingt secondes.")

    return d.save(dossier)
