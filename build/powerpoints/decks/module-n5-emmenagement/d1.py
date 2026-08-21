# -*- coding: utf-8 -*-
"""D1 · Le bruit du dimanche.
Bloc D « Défi 3 · Les voisins » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3immeuble`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-emmenagement/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Le bruit du dimanche",
        chapeau="Un immeuble a des règles écrites dans le bail, et des usages "
                "qui ne sont écrits nulle part.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 3. Demander au groupe ce qu'ils ne savaient pas en "
                  "arrivant dans leur immeuble. Le bac brun et le déneigement reviennent "
                  "presque toujours.")

    d.objectifs([
        "s'excuser du bruit en expliquant ce qui s'est passé ;",
        "demander comment fonctionne un immeuble ;",
        "comprendre les usages : lavage, bacs, déneigement ;",
        "reconnaître le ton d'un échange entre voisins.",
    ])

    d.declencheur(
        'Observation', "Ce bac est devant l'immeuble. Qu'est-ce qu'on met dedans, "
                       "et quel jour sort-il ?",
        image=IMG + 'bac-brun-trottoir.jpg',
        pistes=[
            "Le brun, le bleu, le noir : lequel pour quoi ?",
            "Qui décide du jour ?",
            "Où est-ce écrit ?",
            "À qui demande-t-on quand on ne sait pas ?",
        ],
        notes="Personne ne sait jamais où c'est écrit — parce que ce n'est écrit nulle "
              "part d'utile. La réponse du module : on le demande à un voisin. C'est le "
              "sujet du défi.")

    d.dialogue('Dialogue · 1 de 3', "Ce n'était pas un party", [
        ("AMADOU", "Thérèse, bonjour. Je voulais m'excuser pour hier. On a fait du "
                   "bruit jusqu'à neuf heures et demie.", True),
        ("THÉRÈSE", "J'ai entendu, oui. Mais c'était un déménagement, ce n'était "
                    "pas un party. Ce n'est pas pareil.", True),
        ("AMADOU", "Le camion est arrivé en retard, et après, il pleuvait. On "
                   "finissait de monter les boîtes pendant que mon garçon dormait "
                   "dans l'auto.", True),
        ("THÉRÈSE", "Pauvre petit. Vous savez, quand je suis arrivée ici, en "
                    "quatre-vingt-dix-huit, mon mari a échappé la laveuse dans "
                    "l'escalier.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Amadou s'excuse en racontant : c'est le passé composé et l'imparfait de la "
             "séance D2. Les signaler ici sans les expliquer.")

    d.dialogue('Dialogue · 2 de 3', "La salle de lavage et les bacs", [
        ("AMADOU", "Je voulais vous demander : la salle de lavage, ça fonctionne "
                   "comment ?", True),
        ("THÉRÈSE", "Au sous-sol, à droite. Deux dollars la brassée, en vingt-cinq "
                    "sous. Personne ne réserve, mais on ne laisse pas son linge "
                    "dedans.", True),
        ("AMADOU", "Compris. Et les poubelles ? J'ai vu un bac brun en avant.", True),
        ("THÉRÈSE", "Le bac brun, c'est le compost : les restes de table, les "
                    "pelures. Il se ramasse le mardi matin. Le bac bleu, le "
                    "recyclage, une semaine sur deux.", True),
    ], notes="Faire remarquer la forme de la question : « ça fonctionne comment ? ». C'est "
             "celle qu'on emploie vraiment entre voisins, pas « pourriez-vous m'expliquer "
             "le fonctionnement de… ».")

    d.dialogue('Dialogue · 3 de 3', "Le déneigement", [
        ("AMADOU", "Je vais écrire ça sur le frigo. Et l'hiver, pour le "
                   "stationnement ?", True),
        ("THÉRÈSE", "Le déneigement se fait tôt le matin. Quand la ville affiche "
                    "l'interdiction, il faut déplacer les autos avant sept heures, "
                    "sinon elles sont remorquées.", True),
        ("AMADOU", "Remorquées. D'accord, ça, je ne l'oublierai pas.", True),
        ("THÉRÈSE", "Vous allez voir, on s'habitue. Et si vous avez besoin d'une "
                    "clé anglaise ou d'un tournevis, cognez chez moi.", True),
    ], notes="La dernière réplique est le vrai résultat de l'échange : une porte ouverte. "
             "C'est ce que rapporte une conversation de trois minutes dans un escalier.")

    d.regle("Les usages d'un immeuble ne sont écrits nulle part",
            "Ils s'apprennent en parlant à quelqu'un qui est là depuis longtemps.",
            precision="Le bail donne les règles ; les usages donnent le reste : l'heure du "
                      "lavage, le jour des bacs, ce qu'on fait de la neige, à quelle "
                      "heure on arrête les travaux.",
            notes="Diapositive à photographier. Elle justifie la production orale du bloc E.")

    d.tableau('Les usages · 1 de 2', "Le lavage et les bacs",
              ['La chose', "L'usage"],
              [["La salle de lavage", "2 $ la brassée, en vingt-cinq sous ; on ne laisse pas son linge"],
               ["Le bac brun", "restes de table et pelures ; ramassé le mardi matin"],
               ["Le bac bleu", "papier, carton, verre, plastique ; une semaine sur deux"]],
              cle=0,
              notes="C'est la moitié de l'exercice t3immeuble. Faire ajouter au groupe les "
                    "usages de leur propre immeuble : ils diffèrent d'un quartier à l'autre.")

    d.tableau('Les usages · 2 de 2', "L'hiver, l'escalier, le soir",
              ['La chose', "L'usage"],
              [["Le déneigement", "auto déplacée avant sept heures, sinon remorquée"],
               ["L'escalier commun", "on laisse passer celui qui descend, on n'y entrepose rien"],
               ["Le bruit du soir", "après vingt-deux heures, ni gros travaux ni musique forte"]],
              cle=0,
              note="Les cartons vides se défont à plat avant d'aller au recyclage.",
              notes="Le déneigement est celui qui coûte le plus cher quand on l'ignore : "
                    "un remorquage se paie plus de cent dollars.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Amadou s'excuse du bruit de la veille.", "vrai"),
        ("Thérèse s'est fâchée à cause du bruit.", "faux — « ce n'était pas un party »"),
        ("Le camion était arrivé en retard et il pleuvait.", "vrai"),
        ("Le mari de Thérèse a échappé une laveuse dans l'escalier.", "vrai"),
        ("La salle de lavage coûte deux dollars la brassée.", "vrai"),
        ("Le bac brun se ramasse le vendredi.", "faux — le mardi matin"),
        ("Les autos non déplacées peuvent être remorquées.", "vrai"),
    ], corrige=True,
       notes="Faire justifier la deuxième ligne : Thérèse distingue un déménagement d'un "
             "party. C'est une nuance sociale, pas seulement une information.")

    d.billet(
        "Notez trois usages de votre immeuble que personne ne vous a expliqués.",
        exemples=[
            "Le jour des bacs, l'heure du lavage, ce qu'on fait des vieux meubles.",
            "S'il en manque un, demandez-le cette semaine à un voisin.",
        ],
        notes="Le devoir déclenche une vraie conversation de voisinage. C'est exactement "
              "l'intention du programme pour cette situation.")

    return d.save(dossier)
