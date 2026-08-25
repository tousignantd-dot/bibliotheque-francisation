# -*- coding: utf-8 -*-
"""C1 · Ibrahim en parle à sa sœur.
Bloc C · couleur acier (compréhension orale) · 60 min.
Source : dialogue `t2`, exercices `t2vf` et `t2q`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Ibrahim en parle à Leyla',
        chapeau="La visite est finie. Ibrahim raconte à Leyla ce qui lui a plu et ce qui "
                "l'inquiète. C'est la conversation qui décide vraiment — pas la visite.",
        duree='60 minutes')

    d.titre(notes="Ouverture du défi 2. Demander : à qui parlez-vous après avoir visité "
                  "un logement ? Presque tout le monde en parle à quelqu'un avant de "
                  "décider.")

    d.objectifs([
        "comprendre une conversation où l'on pèse le pour et le contre ;",
        "distinguer ce qui plaît de ce qui inquiète ;",
        "repérer les solutions proposées à un problème ;",
        "reconnaître la construction qui met un élément en évidence.",
    ])

    d.dialogue('Dialogue · 1 de 3', "Ce qui m'a plu, c'est la chambre", [
        ("LEYLA", "Alors, ce logement au-dessus de la boulangerie ? Tu as l'air content, "
                  "toi.", False),
        ("IBRAHIM", "Ce qui m'a plu, c'est la chambre : elle donne sur la cour, loin de "
                    "la rue. Je vais pouvoir dormir le matin après mes quarts.", True),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="Passer l'audio du défi 2. « Ce qui m'a plu, c'est… » est la construction du "
             "défi. La signaler sans l'expliquer : elle sera le sujet de C2.")

    d.dialogue('Dialogue · 2 de 3', "Celui que je crains", [
        ("LEYLA", "Et l'odeur du pain chaud à cinq heures, ça ne va pas te déranger ?",
         False),
        ("IBRAHIM", "Ça, c'est un cadeau ! Celui que je crains, c'est plutôt le camion de "
                    "farine qui recule dans la ruelle.", True),
        ("LEYLA", "Mets des rideaux épais et un ventilateur, le bruit passe au deuxième "
                  "plan.", True),
    ], notes="Faire remarquer que Leyla ne discute pas l'inquiétude : elle propose une "
             "solution. C'est ce qu'on attend d'un proche à qui on demande conseil.")

    d.dialogue('Dialogue · 3 de 3', "Rappelle-la avant vendredi", [
        ("IBRAHIM", "Petite, mais claire. Ce que je changerais, c'est la couleur des "
                    "murs : un vert olive un peu triste.", True),
        ("LEYLA", "Ginette fournit la peinture, non ? Rappelle-la avant vendredi : les "
                  "logements tranquilles partent vite à Sherbrooke.", True),
    ], notes="« Petite, mais claire » : deux jugements dans trois mots. Faire remarquer "
             "le « mais », qui pose le contraste.")

    d.tableau('Analyse', "Ce qui plaît et ce qui inquiète",
              ['Ce qui plaît', 'Ce qui inquiète'],
              [["la chambre donne sur la cour", "le camion de farine dans la ruelle"],
               ["l'odeur du pain chaud", "la couleur des murs, un vert olive"],
               ["la cuisine est claire", "la cuisine est petite"],
               ["la peinture est fournie", "il faut décider avant vendredi"]],
              cle=0,
              note="La troisième ligne montre que la même pièce peut plaire et déplaire. "
                   "C'est normal : aucun logement n'est parfait.",
              notes="Faire remplir ce tableau par les élèves pendant la deuxième écoute, "
                    "avant de l'afficher.")

    d.regle('La règle du défi 2',
            "On ne cherche pas le logement parfait : on pèse ce qui plaît et ce qui inquiète.",
            precision="La chambre sur la cour règle le vrai problème d'Ibrahim. Le "
                      "camion de farine reste un inconvénient, mais des rideaux épais le "
                      "réduisent. C'est ce calcul qui décide, pas une liste de défauts.",
            notes="Diapo centrale du défi. Beaucoup d'élèves cherchent un logement sans "
                  "défaut et ne trouvent rien : le dire.")

    d.pratique('Pratique · 1 de 4', "Vrai ou faux",
               "D'après le dialogue.", [
        ("Ce qui rassure Ibrahim, c'est que la chambre donne sur la cour.", "VRAI"),
        ("L'odeur du pain chaud dérange beaucoup Ibrahim.", "FAUX — il dit que c'est un cadeau"),
        ("Ibrahim aimerait changer la couleur des murs de la cuisine.", "VRAI"),
        ("Leyla conseille d'attendre encore quelques semaines.",
         "FAUX — elle dit de rappeler avant vendredi"),
    ], corrige=True,
       notes="Le deuxième énoncé est le piège : Leyla pose la question, Ibrahim répond le "
             "contraire de ce qu'elle suggère.")

    d.pratique('Pratique · 2 de 4', "Quatre questions",
               "Répondez par une phrase complète.", [
        ("Pourquoi Ibrahim est-il content de la chambre ?",
         "Elle donne sur la cour, loin du bruit de la rue."),
        ("Qu'est-ce qu'il craint le plus ?",
         "Le camion de farine qui recule dans la ruelle le matin."),
        ("Que propose Leyla pour atténuer le bruit ?", "Des rideaux épais et un ventilateur."),
        ("Que voudrait-il changer dans la cuisine ?",
         "La couleur des murs, un vert olive qu'il trouve triste."),
    ], corrige=True,
       notes="La troisième question porte sur une solution, pas sur un problème. C'est "
             "celle qui compte le plus.")

    d.cartes('Ouvrir la mini-leçon', "Le 1er juillet, jour de déménagement", [
        ("Une tradition québécoise",
         "La plupart des baux se terminent le 30 juin. Le 1er juillet, des milliers de "
         "ménages déménagent le même jour."),
        ("Ce que cela change",
         "Les camions de location se réservent des mois d'avance, et les déménageurs "
         "coûtent plus cher ce jour-là qu'un autre."),
        ("D'autres dates existent",
         "Le bail d'Ibrahim commence le 1er septembre. C'est fréquent dans une ville "
         "universitaire comme Sherbrooke."),
        ("Ce qu'il faut prévoir",
         "Réserver le camion dès qu'on signe. Et prévoir que l'ancien locataire partira "
         "peut-être le matin même de votre arrivée."),
    ], notes="Savoir culturel propre au Québec. Beaucoup d'élèves l'apprennent en le "
             "subissant : autant le dire d'avance.")

    d.piege("Le piège du logement parfait",
            "Il y a le camion de farine, je cherche autre chose.",
            "La chambre donne sur la cour : c'est ce qui compte pour moi.",
            "Chaque logement a un défaut. La question n'est pas « y a-t-il un problème ? » "
            "mais « est-ce que ce problème me touche, moi ? ». Le camion de farine "
            "dérangerait quelqu'un qui dort le matin dans une chambre sur rue. Pas "
            "Ibrahim.",
            notes="Boucler sur la règle du module : ce qui compte dépend de la vie qu'on "
                  "mène.")

    d.pratique('Pratique · 3 de 4', "Problème ou solution ?",
               "Ce que dit chaque réplique.", [
        ("« Le camion de farine recule dans la ruelle. »", "un problème"),
        ("« Mets des rideaux épais et un ventilateur. »", "une solution"),
        ("« Ce que je changerais, c'est la couleur des murs. »", "un problème"),
        ("« Ginette fournit la peinture, non ? »", "une solution"),
    ], corrige=True,
       notes="Faire remarquer l'alternance : chaque problème d'Ibrahim reçoit une "
             "solution de Leyla. C'est le rythme de la conversation.")

    d.pratique('Pratique · 4 de 4', "À deux · racontez votre visite",
               "Trois choses qui plaisent, deux qui inquiètent, une solution.", [
        ("Ce qui vous a plu", "trois choses, la plus importante en premier"),
        ("Ce qui vous inquiète", "deux choses, précises"),
        ("Ce que propose votre partenaire", "une solution concrète"),
        ("Votre décision", "en une phrase, avec « parce que »"),
    ], corrige=False,
       notes="Quinze minutes. Se servir des visites du jeu de rôle de B4 : le groupe a "
             "déjà de la matière.")

    d.billet(
        "Après une visite : trois choses qui plaisent, deux qui inquiètent.",
        exemples=[
            "Une visite réelle ou celle du jeu de rôle.",
            "Ajoutez une solution possible pour l'une des deux inquiétudes.",
        ],
        notes="Ramasser. Ces listes serviront en C2, où l'on apprendra à les dire avec "
              "la construction emphatique.")

    return d.save(dossier)
