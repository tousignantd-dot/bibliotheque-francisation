# -*- coding: utf-8 -*-
"""A1 · Le papier qu'on a pris pour de la publicité.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-services/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Le papier qu'on a pris pour de la publicité",
        chapeau="La brochure de la Ville arrive avec les circulaires, et "
                "finit avec elles. Dedans, il y a l'horaire des collectes, "
                "un lieu dont personne n'a entendu parler, et la réponse à "
                "une question qu'on se pose depuis deux semaines.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Demander d'abord au groupe : qui a déjà "
                  "reçu du courrier du gouvernement ou de la Ville sans savoir si c'était "
                  "important ? Les réponses ouvrent la séance et disent, tout de suite, "
                  "combien d'élèves jettent ce qu'ils devraient lire.")

    d.objectifs([
        "reconnaître une communication officielle dans son courrier ;",
        "nommer les trois bacs et dire ce qui va dans chacun ;",
        "savoir ce qu'est un écocentre et ce qu'on y apporte ;",
        "savoir qu'un horaire de collecte dépend de l'adresse.",
    ])

    d.declencheur(
        'Observation', "Vous trouvez ce dépliant dans votre boîte aux lettres. "
                       "Qu'est-ce que vous en faites ?",
        image=IMG + 'brochure-ville.jpg',
        pistes=[
            "Est-ce que c'est de la publicité ?",
            "Comment le savez-vous avant de l'ouvrir ?",
            "Qui l'envoie, à votre avis ?",
            "Qu'est-ce qui arrive si vous ne le lisez pas ?",
        ],
        notes="La réponse la plus fréquente est « je le mets avec les circulaires ». "
              "C'est exactement le point de départ du module. Ne pas corriger tout de "
              "suite : laisser le dialogue le faire à votre place.")

    d.dialogue('Dialogue · 1 de 3', "Trois bacs, et je n'en ai que deux", [
        ("LEÏLA", "Pierre-Luc, tu as reçu ça, toi ? C'est arrivé dans ma boîte aux "
                  "lettres hier.", True),
        ("PIERRE-LUC", "Fais voir… Oui, c'est la brochure de la Ville. Ils "
                       "l'envoient à tout le monde deux fois par année.", True),
        ("LEÏLA", "Il y a trois bacs dessus. Trois. Chez moi, dans l'entrée, il y "
                  "en a deux.", True),
        ("PIERRE-LUC", "Le gris, c'est les ordures. Le vert, c'est le recyclage. "
                       "Et le brun, c'est les restes de table.", False),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire lever la main : qui a un bac brun chez soi ? Qui s'en sert ? L'écart "
             "entre les deux réponses est presque toujours large, et il est intéressant.")

    d.dialogue('Dialogue · 2 de 3', "Le jour de la collecte", [
        ("LEÏLA", "Les restes de table dans un bac ? Pour quoi faire ?", True),
        ("PIERRE-LUC", "Ça devient du compost. C'est ramassé une fois par semaine, "
                       "mais pas le même jour que le reste.", True),
        ("LEÏLA", "Et je le sais comment, le jour ?", True),
        ("PIERRE-LUC", "Tu entres ton code postal sur le site de la Ville, et il te "
                       "sort ton horaire. Ça s'appelle Info-collectes.", True),
    ], notes="Point capital, et contre-intuitif pour beaucoup : l'horaire n'est pas le "
             "même d'une rue à l'autre. Un voisin de quartier n'est pas une source fiable.")

    d.dialogue('Dialogue · 3 de 3', "Un mot que personne ne connaît en arrivant", [
        ("LEÏLA", "Et ça, en bas de la page, « écocentre » ? Le mot ne me dit rien.", True),
        ("PIERRE-LUC", "C'est un endroit où tu apportes ce qui n'entre dans aucun "
                       "bac. Un vieux micro-ondes, de la peinture, des branches.", True),
        ("LEÏLA", "C'est payant ?", True),
        ("PIERRE-LUC", "Pas pour les résidents, dans la plupart des cas. Mais il "
                       "faut que tu apportes une preuve que tu habites la ville.", True),
    ], notes="« Preuve de résidence » revient dans tout le module et jusqu'au défi 3. "
             "L'écrire au tableau maintenant et l'y laisser.")

    d.regle("Un horaire de collecte se vérifie par son adresse",
            "Ce n'est pas le même jour d'une rue à l'autre, même dans un quartier.",
            precision="On entre son code postal dans l'outil de la Ville et on obtient "
                      "son horaire à soi. Demander à un voisin d'une autre rue est la "
                      "façon la plus courante de sortir son bac le mauvais jour pendant "
                      "des mois sans comprendre pourquoi.",
            notes="Diapositive à photographier. Si les élèves ne retiennent qu'une chose "
                  "de cette séance, c'est celle-là — et elle se vérifie le soir même.")

    d.cartes("Les trois bacs et l'écocentre", "Ce qui va où", [
        ("Le bac gris",
         "Les ordures : ce qui ne se recycle pas et ne se composte pas."),
        ("Le bac vert",
         "Le recyclage : papier, carton, verre, métal, plastique. Souvent aux deux semaines."),
        ("Le bac brun",
         "Les restes de table et les résidus de jardin. Ils deviennent du compost."),
        ("L'écocentre",
         "Ce qui n'entre dans aucun bac : peinture, meubles, appareils, branches. On s'y déplace."),
    ], notes="Faire remarquer la différence de nature de la quatrième carte : les trois "
             "premiers viennent à vous, le quatrième exige que vous alliez à lui.")

    d.tableau('Où va cet objet ?', "Quatre cas qui trompent",
              ['Objet', 'Destination'],
              [["Un vieux micro-ondes", "à l'écocentre — jamais dans un bac"],
               ["Un pot de peinture avec son étiquette", "à l'écocentre"],
               ["Les épluchures de légumes", "au bac brun"],
               ["Un contenant de plastique rincé", "au bac vert"]],
              cle=0,
              note="En cas de doute : ni le bac gris ni le chemin — on téléphone ou on lit la page.",
              notes="Ajouter deux ou trois objets proposés par le groupe et les faire "
                    "classer. C'est là que sortent les vrais cas d'incertitude.")

    d.piege("Prendre une communication officielle pour de la publicité",
            "C'est arrivé avec les circulaires, donc c'est de la publicité.",
            "Je regarde qui l'envoie avant de décider si je le garde.",
            "Une brochure municipale, un avis de renouvellement, un formulaire à remplir : "
            "tous arrivent dans la même boîte aux lettres que les circulaires. Le tri se "
            "fait sur l'expéditeur, jamais sur l'apparence.",
            notes="Nommer la gêne : plusieurs élèves n'osent pas dire qu'ils jettent ce "
                  "courrier parce qu'ils ne le comprennent pas. Le dire pour eux.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Leïla avait rangé la brochure avec les circulaires.", "vrai"),
        ("Le bac brun sert au recyclage du papier.", "faux — aux restes de table"),
        ("Les trois bacs sont ramassés le même jour.", "faux — pas le même jour"),
        ("On trouve son horaire en entrant son code postal.", "vrai"),
        ("Un vieux micro-ondes se met dans le bac gris.", "faux — à l'écocentre"),
        ("L'écocentre demande une preuve qu'on habite la ville.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte du dialogue.")

    d.billet(
        "Cherchez votre horaire de collecte avec votre code postal.",
        exemples=[
            "Notez le jour de chacun des bacs que vous avez.",
            "Regardez aussi à quelle heure il faut les sortir. Nous en reparlerons.",
        ],
        notes="Devoir concret et vérifiable, qui prépare directement le défi 1 : la moitié "
              "du groupe découvrira qu'elle sort ses bacs trop tard.")

    return d.save(dossier)
