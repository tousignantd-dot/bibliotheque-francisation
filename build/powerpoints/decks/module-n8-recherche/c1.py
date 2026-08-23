# -*- coding: utf-8 -*-
"""C1 · La séance d'information aux candidats
Bloc C « Défi 2 · Lire l'entreprise » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t21`. C'est l'écoute longue du module :
douze répliques d'affilée du même locuteur, coupées par deux questions.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n8-recherche' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Écouter une présentation sans s'endormir",
        chapeau="Un directeur parle vingt minutes devant quatre candidats. "
                "Trois choses seulement sont à retenir, et une seule question "
                "bien posée vous fait remarquer.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc C. Prévenir que l'extrait est long : c'est "
                  "voulu, et c'est ce que le niveau 8 demande. Le faire écouter en "
                  "trois fois, avec une consigne différente chaque fois.")

    d.objectifs([
        "suivre un discours long et en retenir trois éléments seulement ;",
        "demander ce qu'un pourcentage recouvre ;",
        "repérer une contradiction apparente et la faire expliquer ;",
        "entendre ce qu'un employeur répète deux fois.",
    ], notes="Le quatrième objectif surprend et il est réel : ce qu'on répète est un "
             "message, jamais une redite.")

    d.declencheur(
        'Observation', "Que retenez-vous d'une présentation de vingt minutes ?",
        image=IMG + 'passerelle-usine.jpg',
        pistes=[
            "Combien de chiffres pouvez-vous retenir sans écrire ?",
            "Qu'est-ce que vous notez d'habitude : les chiffres ou les idées ?",
            "Est-ce qu'on a le droit d'interrompre pour poser une question ?",
            "Qu'est-ce qui vous empêche de le faire ?",
        ],
        notes="Trois éléments suffisent : un fait récent, un chiffre, une difficulté "
              "avouée. Le dire après la discussion, pas avant.")

    d.dialogue('Écoute 1 de 3', "Ce qui a changé cette année", [
        ("RÉAL", "Vous êtes quatre ce matin, et vous serez peut-être un dans trois semaines : autant que vous sachiez à quoi vous vous engagez.", True),
        ("RÉAL", "En janvier, l'entreprise a été acquise par le Groupe Landron, de Mississauga. Je préfère vous le dire moi-même.", True),
        ("RÉAL", "Ce qui est vrai : le carnet de commandes a doublé en dix-huit mois, et nous sommes passés de deux à trois quarts de travail.", True),
        ("RÉAL", "Ce qui est faux : personne n'a été mis à pied, et il n'est question de fermer aucune ligne.", True),
    ], consigne="Première écoute : qu'est-ce qui a changé dans cette entreprise ?",
       notes="Première consigne : le fait récent, rien d'autre. Interdire la prise de "
             "notes à cette écoute-là — on écoute pour comprendre, pas pour copier.")

    d.dialogue('Écoute 2 de 3', "Le chiffre, et ce qu'il recouvre", [
        ("RÉAL", "Les trois lignes du quart de soir tournent à quatre-vingt-deux pour cent de leur capacité. Notre objectif est quatre-vingt-douze.", True),
        ("SHIRIN", "Excusez-moi. Vous dites quatre-vingt-deux pour cent : est-ce que ce chiffre tient compte des arrêts planifiés, ou seulement des arrêts imprévus ?", True),
        ("RÉAL", "Bonne question, et la réponse est : seulement les imprévus. Autrement dit, les dix points qui manquent sont dix points qu'on perd sans l'avoir voulu.", True),
        ("RÉAL", "Elle en change énormément, et vous êtes la seule à l'avoir demandée en deux séances.", True),
    ], consigne="Deuxième écoute : notez les chiffres, et ce que chacun recouvre.",
       notes="C'est le geste de la séance. Un pourcentage n'a de sens qu'avec ce qu'on "
             "a mis dedans : de quoi, sur quelle période, avec ou sans quoi. Une "
             "seule question de ce genre vous fait remarquer.")

    d.dialogue('Écoute 3 de 3', "La contradiction, et ce qu'on répète", [
        ("RÉAL", "Vos neuf recrues arriveront dans une usine de quarante ans. Vous bâtissez du neuf à l'intérieur de quelque chose de vieux.", True),
        ("RÉAL", "L'échelle compte six échelons et on n'embauche pas obligatoirement au premier.", True),
        ("RÉAL", "Je le répète parce que peu de gens l'entendent : on n'embauche pas obligatoirement au premier échelon. À bon entendeur.", True),
        ("SHIRIN", "Merci. C'est noté.", True),
    ], consigne="Troisième écoute : qu'est-ce qui est dit deux fois, et pourquoi ?",
       notes="La répétition n'est pas une maladresse : c'est une porte qu'on ouvre à "
             "ceux qui écoutent. Faire remarquer que Shirin ne saute pas dessus — "
             "elle note, et elle s'en servira au défi 3.")

    d.tableau('Analyse', "Trois choses à retenir d'une présentation",
              ['À retenir', 'À laisser'],
              [["un fait récent : le rachat, le troisième quart",
                "l'année de fondation, que tout le monde peut citer"],
               ["un chiffre, et ce qu'il recouvre",
                "les valeurs affichées : le respect, l'excellence"],
               ["une difficulté avouée : la supervision sans soutien",
                "le vocabulaire d'ambiance"]],
              cle=0,
              note="Les trois de gauche se replacent dans une réponse d'entrevue. Ceux de droite, non.",
              notes="Diapositive à photographier. Le critère est simple : une "
                    "information qu'on ne pourrait pas contredire ne renseigne sur "
                    "rien.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la présentation.", [
        ("Boréalis fabrique des produits vendus au grand public.", "faux - à des transformateurs"),
        ("L'usine a été acquise en janvier par un groupe de Mississauga.", "vrai"),
        ("Des employés ont été mis à pied après l'acquisition.", "faux - personne"),
        ("Le taux de quatre-vingt-deux pour cent comprend les arrêts planifiés.", "faux - seulement les imprévus"),
        ("À partir de dix-huit heures, la supervision se fait sans soutien sur place.", "vrai"),
        ("L'échelle salariale est communiquée aux candidats avant l'entrevue.", "faux - elle ne l'est pas"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le dernier "
             "prépare la négociation du bloc D : l'échelle est cachée, et on peut "
             "quand même en parler.")

    d.billet(
        "Trouvez la page « À propos » d'une entreprise et notez trois choses.",
        exemples=[
            "Un fait daté, un chiffre, une difficulté reconnue.",
            "Si vous ne trouvez pas la troisième, écrivez-le : c'est un renseignement aussi.",
        ],
        notes="Devoir. La page servira à la séance C2, où l'on apprendra à la lire "
              "en cherchant ce qui manque.")

    return d.save(dossier)
