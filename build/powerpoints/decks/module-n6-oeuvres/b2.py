# -*- coding: utf-8 -*-
"""B2 · Avant ou après ? La seule question à tenir
Bloc B « Défi 1 · Le déroulement du film » · couleur teal · 75 min.
Source : exercice `t1sign` et sa mini-leçon « Avant ou après ? ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='teal',
        titre="Avant ou après ? La seule question à tenir",
        chapeau="Une seule question, posée à chaque changement d'image, et "
                "tenue jusqu'au générique. C'est tout ce qui sépare un "
                "spectateur qui suit d'un spectateur qui décroche.",
        duree='75 minutes')

    d.titre(notes="Deuxième séance du Défi 1. Commencer par les billets de B1 : s'ils "
                  "citent tous le même moment du film, reprendre celui-là image par "
                  "image avant d'entrer dans la séance.")

    d.objectifs([
        "poser la question « avant ou après ? » à chaque changement de scène ;",
        "reconnaître les signaux propres à un réalisateur ;",
        "dater une scène par l'âge des personnages et par les objets ;",
        "replacer huit moments du film dans leur époque.",
    ], notes="Le troisième objectif est celui qui sert au-delà de ce film-ci : les "
             "signaux changent d'un réalisateur à l'autre, les objets non.")

    d.declencheur(
        'Observation', "Regarde ces deux images du film. Laquelle vient avant ?",
        pistes=[
            "Qu'est-ce qui a changé dans la lumière ?",
            "Est-ce qu'on entend la même chose dans les deux ?",
            "Les personnages ont-ils le même âge ?",
            "Y a-t-il un objet qui n'est pas à la même place ?",
        ],
        notes="Projeter deux extraits de dix secondes, sans son d'abord, puis avec le "
              "son. L'écart entre les deux essais est la démonstration de la séance.")

    d.tableau('Analyse', "Quatre indices, quand les signaux échappent",
              ['L\'indice', 'Ce qu\'il permet de dater'],
              [["l'âge des personnages", "Réal a dix-neuf ans, et seulement en 1978"],
               ["les objets", "une lampe, un téléphone, une automobile"],
               ["la place d'un objet", "la lettre est dans le tiroir avant, dans la poche après"],
               ["la lumière", "vendredi il fait noir, samedi gris, dimanche il neige"]],
              cle=0,
              note="La troisième ligne date une scène plus sûrement qu'une date affichée à l'écran.",
              notes="Diapositive à photographier. Faire chercher d'autres objets "
                    "datants dans le film : le poste de radio, le manteau, la "
                    "camionnette.")

    d.regle("Une seule question, tenue jusqu'au bout",
            "À chaque changement d'image : est-ce que ça, c'est avant ou après ?",
            precision="Ce n'est pas une question à se poser une fois, au début. C'est "
                      "une habitude à tenir pendant deux heures. Un spectateur qui la "
                      "tient peut manquer trois mots de vocabulaire sans rien perdre ; "
                      "un spectateur qui la lâche peut tout comprendre et ne rien "
                      "suivre.",
            notes="Diapositive à photographier. Faire dire la question à voix haute "
                  "par le groupe. Elle doit devenir un automatisme, pas une "
                  "connaissance.")

    d.regle("Une règle cassée une fois est un effet",
            "Trois fois, c'est une erreur.",
            precision="À la fin du film, on entend la mer aujourd'hui — la seule fois. "
                      "La réalisatrice casse sa propre règle exprès, et c'est ce qui "
                      "donne son sens à la dernière scène. Un film qui casserait sa "
                      "règle sans raison serait simplement mal fait.",
            notes="Diapositive à photographier. Ne pas expliquer pourquoi elle la "
                  "casse : c'est le dénouement, et il se garde pour E1.")

    d.pratique('Compréhension', "Les trois jours, ou novembre 1978 ?",
               "Pour chaque moment, dites à quelle époque il appartient.", [
        ("Estelle descend de l'autobus devant l'église, le vendredi soir.", "les trois jours"),
        ("Le jeune homme et son chien attendent au bout du quai.", "novembre 1978"),
        ("Estelle vide les armoires de la cuisine et fait des boîtes.", "les trois jours"),
        ("La mère dit « ton frère avait le même manteau ».", "les trois jours"),
        ("Quelqu'un écrit une lettre à la table de cuisine, à la lampe.", "novembre 1978"),
        ("Le bateau quitte le quai pendant que la musique s'arrête.", "novembre 1978"),
    ], corrige=True,
       notes="Le quatrième item est le seul piège : la phrase parle du passé, mais "
             "elle est dite aujourd'hui. Le faire remarquer avant la correction, "
             "sinon la moitié du groupe se trompe.")

    d.piege("Croire qu'un jeune homme est forcément un fils",
            "Le jeune homme du quai, c'est le fils d'Estelle.",
            "Le jeune homme du quai, c'est son frère Réal, à dix-neuf ans.",
            "La phrase qui le dit dure une seconde : « ton frère avait le même "
            "manteau ». Elle est facile à manquer, surtout en lisant des sous-titres. "
            "Ce n'est pas une faute de compréhension, c'est une seconde d'attention "
            "prise ailleurs — et le film ne la répète pas.",
            notes="Rejouer la scène avec le son seulement, sans image ni sous-titres. "
                  "Presque tout le monde entend la phrase à la deuxième écoute.")

    d.cartes("Le réflexe de spectateur", "À chaque changement d'image", [
        ("Pose la question",
         "avant ou après ? Une seconde suffit, et elle ne coûte rien."),
        ("Écoute d'abord",
         "le son change avant l'image, presque toujours."),
        ("Cherche un âge",
         "un personnage qui rajeunit place la scène sans discussion."),
        ("Si tu te perds, continue",
         "la scène suivante réexplique presque toujours la précédente."),
    ], notes="Quatre gestes, à copier dans le cahier. Le dernier est celui qui évite "
             "l'abandon : se perdre une fois ne coûte rien.")

    d.billet(
        "Écris un moment du film et dis à quelle époque il appartient.",
        exemples=[
            "Par exemple : « la scène du quai - novembre 1978 ».",
            "Un moment, une époque, et l'indice qui te l'a dit.",
        ],
        notes="Deux minutes. Les billets sans indice signalent les élèves qui "
              "devinent : ce sont eux à reprendre en B3.")

    return d.save(dossier)
