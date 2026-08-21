# -*- coding: utf-8 -*-
"""A4 · « Chaleureux, et vouvoyé »
Bloc A « Je découvre » · couleur ambre · 75 min. Registre et distance sociale.
Source : exercice `prReg`, mini-leçon `prReg`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Chaleureux, et vouvoyé",
        chapeau="Marisol et Réjean se croisent depuis trois ans. Ils "
                "s'entraident, ils mangeront à la même table au mois de "
                "juin, et ils se vouvoient. Entre voisins d'un même "
                "immeuble, le « vous » est la règle par défaut.",
        duree='75 minutes')

    d.titre(notes="Séance culturelle autant que linguistique. Elle répond à une question "
                  "que les élèves se posent tous et qu'ils osent rarement poser : "
                  "pourquoi ma voisine me vouvoie-t-elle encore après deux ans ? "
                  "Commencer par cette question.")

    d.objectifs([
        "savoir à qui l'on dit « vous » dans un immeuble, et pourquoi ;",
        "reconnaître comment le tutoiement s'installe entre voisins ;",
        "distinguer ce qui se demande à un voisin de ce qui ne se demande pas ;",
        "nommer quelqu'un correctement : monsieur, madame, et le nom de famille.",
    ], notes="Les quatre objectifs sont des règles sociales, pas grammaticales. Le rôle de "
             "l'enseignante est de les rendre explicites : personne ne les enseigne, et "
             "tout le monde est jugé dessus.")

    d.regle("Le vous ne vexe jamais, le tu peut mettre mal à l'aise",
            "Entre voisins d'un même immeuble, on se vouvoie tant que "
            "personne n'a proposé autre chose.",
            precision="Le tutoiement s'installe quand quelqu'un le propose à voix "
                      "haute : « on peut se tutoyer, hein ? ». Tant que la phrase "
                      "n'a pas été dite, le vous reste — et il n'a rien de froid.",
            notes="Diapositive à photographier. Faire remarquer que la proposition de "
                  "tutoiement est presque toujours dite avec ces mots-là, et qu'on peut "
                  "la faire soi-même.")

    d.tableau('Deux colonnes', "Ce qui se demande, ce qui ne se demande pas",
              ['Ça se dit à un voisin', "C'est trop personnel"],
              [["Il y a longtemps que vous habitez ici ?", "Vous payez combien de loyer ?"],
               ["Vous plantez quelque chose cette année ?", "Vous avez reçu vos papiers ?"],
               ["Je peux vous aider à monter vos sacs ?", "Vous gagnez combien ?"],
               ["Quand ramassent-ils le bac brun ?", "Vous êtes malade ?"],
               ["Vous avez changé d'horaire ?", "Pourquoi votre mari est parti ?"]],
              cle=1,
              notes="Faire remarquer le principe qui organise les deux colonnes : une "
                    "bonne question de voisinage porte sur quelque chose qu'on partage "
                    "tous les deux. C'est ce qui la rend facile à poser et à recevoir.")

    d.cartes("Nommer quelqu'un", "Quatre façons, et une à éviter", [
        ("Monsieur ou madame, plus le nom",
         "Bonjour monsieur Deslauriers. La forme normale, pendant des années."),
        ("Quand on ne sait pas le nom",
         "Bonjour ! Excusez-moi... Vous êtes du deuxième, je pense ?"),
        ("Pour proposer le tutoiement",
         "On peut se tutoyer, si vous voulez. Une phrase, dite une fois."),
        ("Ce qu'on évite",
         "Hé, la madame ! Un appel crié dans la cour ferme la porte."),
    ], notes="La deuxième carte est la plus utile : elle donne une façon d'ouvrir une "
             "conversation sans connaître le nom, ce qui est le cas de la moitié du "
             "groupe.")

    d.pratique('Jugement', "Ça se dit, ou c'est trop personnel ?",
               "Pour chaque phrase, choisissez.", [
        ("Il y a longtemps que vous habitez ici ?", "ça se dit"),
        ("Vous payez combien de loyer, vous ?", "trop personnel"),
        ("Vous plantez quelque chose cette année ?", "ça se dit"),
        ("Vous avez reçu vos papiers d'immigration ?", "trop personnel"),
        ("Je peux vous aider à monter vos sacs ?", "ça se dit"),
        ("Vous gagnez combien à votre nouvel emploi ?", "trop personnel"),
    ], corrige=True,
       notes="Exercice prReg de l'activité. Accepter la discussion sur les cas limites : "
             "dans certaines communautés, demander le loyer est banal et même utile. Dire "
             "que la règle décrite ici est celle du voisinage montréalais ordinaire, pas "
             "une vérité universelle.")

    d.piege("Poser une question personnelle en croyant s'intéresser",
            "Vous avez eu vos papiers ? (dit avec bienveillance)",
            "Il y a longtemps que vous habitez ici ?",
            "L'intention est bonne, l'effet est mauvais : la personne doit soit "
            "mentir, soit raconter une chose difficile devant les boîtes aux lettres. "
            "Parlez de l'immeuble ; le reste viendra si elle le veut.",
            notes="Point délicat : plusieurs élèves ont vécu la question et l'ont posée. "
                  "Ne pas moraliser. Dire simplement que la personne parlera d'elle-même "
                  "si elle le souhaite, et que le rôle du voisin est d'être disponible.")

    d.piege("Se justifier deux fois en refusant",
            "Je travaille, et puis mon fils est malade, et j'ai aussi...",
            "Je travaille ce jour-là. On se reprend ?",
            "Une raison suffit. Accumuler les raisons donne l'impression qu'aucune "
            "n'est vraie.",
            notes="Ce piège annonce le défi 1 : la justification en une phrase est "
                  "exactement ce que le programme demande au niveau 5.")

    d.billet(
        "Écrivez la phrase que vous direz demain à quelqu'un de votre immeuble.",
        exemples=[
            "Une seule phrase, et une question à laquelle on répond en dix mots.",
            "Notez à qui vous la direz : le nom, ou l'étage si vous ignorez le nom.",
        ],
        notes="Fin du bloc A. Demander à la séance suivante qui l'a fait : le taux de "
              "réussite est plus élevé qu'on ne croit, et un seul témoignage entraîne "
              "les autres.")

    return d.save(dossier)
