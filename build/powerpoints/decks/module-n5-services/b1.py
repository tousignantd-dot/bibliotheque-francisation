# -*- coding: utf-8 -*-
"""B1 · L'appel au 311.
Bloc B « Défi 1 · L'appel » · couleur acier · 75 min.
Source : dialogue `t1`, exercices `t1vf` et `t1phrases`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-services/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="L'appel au service",
        chapeau="Un menu automatisé, quatre minutes d'attente, puis "
                "quelqu'un décroche. Ce qui décide de la suite, c'est la "
                "première phrase — et le numéro qu'on note avant de "
                "raccrocher.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Ramasser le devoir A4 : quels mots officiels "
                  "chacun a-t-il relevés ? En écrire cinq au tableau avant de commencer.")

    d.objectifs([
        "comprendre un menu téléphonique automatisé ;",
        "dire en une seule phrase pourquoi on appelle ;",
        "reconnaître les cinq moments d'un appel à un service ;",
        "savoir ce qu'est une requête et pourquoi il faut la demander.",
    ])

    d.declencheur(
        'Discussion', "Qu'est-ce qui vous arrête quand vous devez téléphoner ?",
        image=IMG + 'appel-telephone.jpg',
        pistes=[
            "Le menu au début ?",
            "La peur de ne pas comprendre la réponse ?",
            "Ne pas savoir quoi dire en premier ?",
            "Devoir écrire en même temps qu'on écoute ?",
        ],
        notes="Laisser parler longuement : c'est la séance où les blocages se disent. "
              "Les noter au tableau ; les quatre séances du bloc B les traitent tous, "
              "et le dire rassure.")

    d.dialogue('Dialogue · 1 de 3', "Le menu, puis quelqu'un", [
        ("VOIX", "Vous avez joint le service à la clientèle de la Ville. Pour le "
                 "français, faites le un.", True),
        ("VOIX", "Pour un problème de collecte, faites le trois. Pour parler à un "
                 "préposé, restez en ligne. Le temps d'attente est d'environ "
                 "quatre minutes.", True),
        ("MICHELINE", "Bonjour, Micheline à l'appareil. Comment puis-je vous aider ?", True),
        ("LEÏLA", "Bonjour. Je vous appelle parce que mon bac brun n'a pas été "
                  "ramassé depuis deux semaines.", False),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer la dernière réplique : une phrase, un fait, une durée. "
             "C'est le modèle de tout le défi. La faire répéter par trois élèves.")

    d.dialogue('Dialogue · 2 de 3', "S'identifier, et épeler", [
        ("MICHELINE", "Deux semaines, d'accord. Vous êtes à quelle adresse ?", True),
        ("LEÏLA", "Au 7412, rue De Normanville, appartement 3. À Villeray.", True),
        ("MICHELINE", "Et votre code postal, s'il vous plaît ?", True),
        ("LEÏLA", "H2R 2V8. Je peux vous l'épeler : H, deux, R, deux, V, huit.", True),
    ], notes="Leïla épelle sans qu'on le lui demande. C'est le geste à installer : on "
             "n'attend pas de ne pas être compris pour épeler.")

    d.dialogue('Dialogue · 3 de 3', "Le numéro de requête", [
        ("LEÏLA", "Je voudrais savoir si le bac va être vidé cette semaine quand même.", True),
        ("MICHELINE", "J'ouvre une requête pour un ramassage supplémentaire. Le "
                      "délai est de trois jours ouvrables.", True),
        ("LEÏLA", "Trois jours ouvrables. Et comment est-ce que je fais pour suivre "
                  "ma demande ?", True),
        ("MICHELINE", "Je vous donne un numéro de requête. Vous notez ? 24-118-7690.", True),
    ], notes="Deux choses à souligner : c'est Leïla qui demande comment suivre sa demande, "
             "et c'est cette question qui fait apparaître le numéro.")

    d.regle("Une demande sans requête n'existe pas",
            "Sans numéro, personne ne peut la retrouver — et vous n'avez rien à rappeler.",
            precision="La question qui change un appel en démarche tient en huit mots : "
                      "« Est-ce que vous ouvrez une requête ? » Beaucoup d'appels se "
                      "terminent par une promesse orale que rien ne conserve.",
            notes="Diapositive à photographier. Faire répéter la question à voix haute par "
                  "tout le groupe, deux fois. C'est un automatisme à installer.")

    d.tableau('Les cinq moments d\'un appel', "Toujours le même ordre",
              ['Moment', 'Ce qu\'on y fait'],
              [["1. Le menu", "on écoute et on appuie — rien à dire"],
               ["2. La raison", "une phrase, un fait, une durée"],
               ["3. L'identification", "adresse, code postal, on épelle au besoin"],
               ["4. Les questions", "deux ou trois, précises"],
               ["5. La clôture", "on note le numéro, on le répète, on remercie"]],
              cle=0,
              note="Le moment 5 est celui qu'on saute quand on est pressé — et c'est celui qui coûte le plus cher.",
              notes="Diapositive à photographier. C'est la carte de route du défi 1 tout "
                    "entier ; les élèves peuvent l'avoir sous les yeux en appelant.")

    d.piege("Raconter au lieu d'annoncer",
            "Bonjour, alors voilà, c'est parce que je suis arrivée ici il y a huit mois et…",
            "Bonjour, je vous appelle parce que mon bac n'a pas été ramassé depuis deux semaines.",
            "Un préposé trie les appels : il a besoin de savoir en dix secondes de quoi "
            "il s'agit. Le contexte viendra s'il le demande. Commencer par l'histoire "
            "fait perdre l'attention avant d'arriver au fait.",
            notes="Faire vivre l'erreur : demander à un élève de raconter longuement "
                  "pendant que vous jouez le préposé, et montrer que vous ne savez "
                  "toujours pas quoi noter.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'appel.", [
        ("Le menu annonce environ quatre minutes d'attente.", "vrai"),
        ("Micheline demande le numéro d'assurance sociale.", "faux — l'adresse et le code postal"),
        ("Leïla épelle son code postal sans qu'on le lui demande.", "vrai"),
        ("La collecte se fait le mardi matin dans son secteur.", "vrai"),
        ("Leïla sortait son bac au bon moment depuis le début.", "faux — vers midi, trop tard"),
        ("Le délai annoncé est de trois jours ouvrables.", "vrai"),
        ("Leïla répète le numéro de requête pour le confirmer.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. La cinquième est "
             "celle qui explique tout le problème : la faire retrouver dans le dialogue.")

    d.billet(
        "Écrivez la première phrase de l'appel que vous auriez à faire.",
        exemples=[
            "Une seule phrase : « Bonjour, je vous appelle parce que… »",
            "Un fait, et depuis quand. Nous les lirons ensemble à la séance B2.",
        ],
        notes="Devoir très court et très ciblé. Il donne le matériel d'ouverture de B2 et "
              "permet de corriger la formulation avant que l'appel réel ait lieu.")

    return d.save(dossier)
