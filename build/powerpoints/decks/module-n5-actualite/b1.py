# -*- coding: utf-8 -*-
"""B1 · « Le feu de la rue Alexandre »
Bloc B « Défi 1 · Ce qui est arrivé » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1a`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-actualite/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="« Le feu de la rue Alexandre »",
        chapeau="Un immeuble de quatre logements a brûlé pendant la nuit, "
                "à quatre rues de la cafétéria. Sylvain n'a rien entendu et "
                "n'a rien lu. Pour qu'il comprenne, il ne suffit pas de "
                "connaître les faits : il faut les mettre en ordre.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Demander d'abord au groupe : quand vous "
                  "racontez une nouvelle à quelqu'un, par quoi commencez-vous ? "
                  "Noter deux ou trois débuts au tableau. Presque toujours, quelqu'un "
                  "commencera par l'heure ou par le lieu — et c'est précisément ce "
                  "que la séance va corriger.")

    d.objectifs([
        "commencer un récit par la nouvelle, pas par le détail ;",
        "suivre l'ordre des évènements dans un récit entendu ;",
        "repérer ce qui est arrivé, où et quand ;",
        "comprendre ce que le dernier paragraphe d'un fait divers apporte.",
    ], notes="Le premier objectif est celui de toute la séance. Les trois autres sont "
             "de la compréhension orale : le dialogue s'écoute deux fois, pas plus, "
             "pour que l'exercice reste réaliste.")

    d.declencheur(
        'Observation', "Deux pompiers, un boyau, une façade. "
                       "Par quoi commenceriez-vous le récit ?",
        image=IMG + 'pompiers-boyau.jpg',
        pistes=[
            "« Il était quatre heures du matin… » — un détail avant la nouvelle.",
            "« Un immeuble a passé au feu cette nuit. » — la nouvelle d'abord.",
            "Laquelle des deux permet à l'autre de se représenter la scène ?",
            "Que faut-il ajouter tout de suite après : où, ou quand ?",
        ],
        notes="Faire choisir à main levée entre les deux premières pistes, puis "
              "argumenter. La deuxième gagne toujours, mais il faut que le groupe "
              "dise pourquoi : sans la nouvelle, la personne ne sait pas où ranger "
              "les détails qu'on lui donne.")

    d.dialogue('Dialogue · 1 de 5', "Il est arrivé quoi ?", [
        ("SYLVAIN", "Bon, raconte. Il est arrivé quoi ?", True),
        ("MARISOL", "Un immeuble a passé au feu, cette nuit, sur la rue "
                    "Alexandre.", True),
        ("SYLVAIN", "Cette nuit ? Je n'ai rien entendu.", True),
        ("MARISOL", "Vers quatre heures du matin. Tout le monde dormait.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire relever la première réponse de Marisol : quoi, quand, où, dans "
             "cet ordre et dans une seule phrase. C'est le modèle de tout le défi. "
             "Faire remarquer aussi le passé composé pour l'évènement et l'imparfait "
             "pour le décor — sans encore les nommer.")

    d.dialogue('Dialogue · 2 de 5', "Personne de blessé", [
        ("SYLVAIN", "Il y a du monde de blessé ?", True),
        ("MARISOL", "Non, personne. C'est ça qui est chanceux.", True),
        ("SYLVAIN", "Comment ça, personne ? Un immeuble au complet ?", True),
        ("MARISOL", "Quatre logements. Un locataire s'est réveillé et il a "
                    "cogné à toutes les portes.", True),
    ], notes="Sylvain pose les questions que la personne en face pose toujours : y "
             "a-t-il des blessés, combien de monde. Faire noter que Marisol y répond "
             "sans se faire prier : dans le jeu de rôle de E1, l'assistant posera les "
             "mêmes.")

    d.dialogue('Dialogue · 3 de 5', "Huit minutes après l'appel", [
        ("SYLVAIN", "Il a fait le tour de l'immeuble pendant que ça "
                    "brûlait ?", True),
        ("MARISOL", "Oui. Les pompiers sont arrivés huit minutes après "
                    "l'appel.", True),
        ("SYLVAIN", "Et l'immeuble ?", True),
        ("MARISOL", "Perdu. Il ne reste que les murs. Onze personnes n'ont "
                    "plus de logement.", True),
    ], notes="« Pendant que ça brûlait » est la première phrase à deux temps du "
             "module : une durée à l'imparfait, un évènement dedans. La signaler sans "
             "l'expliquer — elle sera le cœur de B3.")

    d.dialogue('Dialogue · 4 de 5', "Elles ont dormi où, après ?", [
        ("SYLVAIN", "Onze ! Elles ont dormi où, après ?", True),
        ("MARISOL", "La Croix-Rouge les a hébergées. Le journal le dit à "
                    "la fin.", True),
        ("SYLVAIN", "Et le feu, il est parti d'où ?", True),
        ("MARISOL", "De la cuisine du deuxième. Mais ce n'est pas encore "
                    "certain.", True),
    ], notes="Deux choses à faire remarquer. « Le journal le dit à la fin » : c'est "
             "le dernier paragraphe, celui qui dit ce qui reste. Et « ce n'est pas "
             "encore certain » : Marisol ne donne pas la cause pour un fait, parce "
             "que le journal ne la donne pas non plus.")

    d.dialogue('Dialogue · 5 de 5', "J'essaie de le dire dans l'ordre", [
        ("SYLVAIN", "Tu racontes ça comme si tu étais là.", True),
        ("MARISOL", "Je raconte ce que j'ai lu. Et j'essaie de le dire "
                    "dans l'ordre.", False),
    ], notes="La dernière réplique est la phrase du défi. Elle dit les deux choses "
             "à retenir : on raconte ce qu'on a lu, et on le dit dans l'ordre. La "
             "laisser à l'écran pendant la mise en commun.")

    d.regle("La grosse nouvelle d'abord, les détails après",
            "Ce qui est arrivé, puis où, puis quand. Une seule phrase, "
            "et la personne en face sait de quoi vous parlez.",
            precision="Un immeuble a passé au feu, cette nuit, sur la rue "
                      "Alexandre. Tout ce que vous ajoutez ensuite se range tout "
                      "seul : l'heure, le nombre de logements, les pompiers, les "
                      "sinistrés. Commencez par l'heure, et l'autre attend encore "
                      "de savoir de quoi il s'agit.",
            notes="Diapositive à photographier. C'est la règle que le jeu de rôle de "
                  "E1 vérifiera en premier : l'assistant ne comprend rien tant que la "
                  "nouvelle n'est pas dite.")

    d.tableau('Le récit', "Ce que Marisol dit, et dans quel ordre",
              ['Le moment', 'Ce qu\'elle dit'],
              [["La nouvelle", "Un immeuble a passé au feu, rue Alexandre"],
               ["Le décor", "Vers quatre heures. Tout le monde dormait."],
               ["Les évènements", "Un locataire s'est réveillé, il a cogné aux portes"],
               ["La suite", "Les pompiers sont arrivés huit minutes après"],
               ["Ce qui reste", "Onze personnes n'ont plus de logement"]],
              cle=1,
              notes="Faire remplir la colonne de droite de mémoire, sans réécouter. "
                    "Les cinq moments sont exactement ceux de l'exercice t1red de la "
                    "séance B4 : le tableau y servira de plan.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue de la pause.", [
        ("L'incendie a eu lieu vers quatre heures du matin.", "vrai"),
        ("Deux personnes ont été blessées.", "faux — personne n'a été blessé"),
        ("Un locataire s'est réveillé et a cogné à toutes les portes.", "vrai"),
        ("Les pompiers sont arrivés une demi-heure après l'appel.", "faux — huit minutes"),
        ("L'immeuble comptait quatre logements.", "vrai"),
        ("Onze personnes se retrouvent sans logement.", "vrai"),
        ("La Croix-Rouge a hébergé les sinistrés.", "vrai"),
        ("La cause du feu est déjà certaine.", "faux — ce n'est pas encore certain"),
    ], corrige=True,
       notes="Exercice t1a de l'activité. Faire justifier chaque réponse par la "
             "réplique exacte. La dernière est celle qui compte : la prudence de "
             "Marisol sur la cause reviendra au bloc C et au bloc D.")

    d.billet(
        "Racontez en une seule phrase ce qui est arrivé rue Alexandre.",
        exemples=[
            "Quoi, où, quand — dans cet ordre, et rien d'autre.",
            "Relisez : est-ce qu'on comprend sans avoir lu le journal ?",
        ],
        notes="Ramasser. Lire trois billets à voix haute en ouverture de B2 : ceux "
                  "qui commencent par l'heure font entendre le problème mieux que "
                  "n'importe quelle explication.")

    return d.save(dossier)
