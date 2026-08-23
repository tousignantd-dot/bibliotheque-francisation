# -*- coding: utf-8 -*-
"""C1 · La chronique du samedi : trois écoutes, trois consignes
Bloc C « Défi 2 · Ce qui n'est pas écrit » · couleur acier · 75 min.
Source : dialogue `t2` (le quasi-monologue), exercice `t21`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="La chronique du samedi : trois écoutes, trois consignes",
        chapeau="Quatorze répliques d'affilée du même locuteur, coupées par "
                "deux questions. Ce n'est plus une conversation : c'est un "
                "exposé suivi, et il s'écoute autrement.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 2, et la seule séance du module bâtie sur un "
                  "exposé long. Le programme du niveau 8 le nomme : « il suit le "
                  "déroulement d'exposés bien structurés ». Annoncer les trois écoutes "
                  "dès le début, sinon le groupe s'épuise à la première.")

    d.objectifs([
        "suivre un exposé de quatorze répliques sans perdre le fil ;",
        "écouter trois fois avec une consigne différente à chaque fois ;",
        "distinguer ce que le chroniqueur décrit de ce qu'il juge ;",
        "retenir les mots du livre et du poème : recueil, strophe, narrateur.",
    ], notes="Le deuxième objectif est la méthode, et elle vaut hors du cours : on "
             "n'écoute pas un exposé long « en général », on l'écoute avec une "
             "question en tête.")

    d.declencheur(
        'Préparation', "Comment écoute-t-on quelqu'un qui parle seul dix minutes ?",
        pistes=[
            "Est-ce qu'on peut tout retenir ? Essayez de vous rappeler la météo d'hier.",
            "Qu'est-ce qu'on retient, alors ?",
            "Que feriez-vous si vous saviez d'avance quoi chercher ?",
            "Combien de fois faut-il écouter pour tout avoir ?",
        ],
        notes="Question de méthode, cinq minutes. La réponse est celle de la séance : "
              "trois écoutes courtes valent mieux qu'une écoute longue et attentive.")

    d.tableau('Analyse', "Trois écoutes, trois consignes",
              ['L\'écoute', 'Ce qu\'on cherche'],
              [["Première", "de quelles œuvres parle-t-il ? combien ?"],
               ["Deuxième", "les chiffres : pages, strophes, vers, année"],
               ["Troisième", "ce qu'il dit deux fois"]],
              cle=0,
              note="Une consigne à la fois. Trois questions en même temps, c'est aucune.",
              notes="Diapositive à photographier, et à afficher pendant les trois "
                    "écoutes. La troisième consigne est la plus riche : ce qu'un "
                    "chroniqueur répète est ce qu'il tient à faire passer.")

    d.dialogue('Écoute 1 · les œuvres', "Deux textes courts, un même geste", [
        ("GASPARD", "Deux textes courts, et je les ai choisis ensemble parce qu'ils font le même geste par deux moyens différents. Une nouvelle et un poème.", True),
        ("GASPARD", "La nouvelle d'abord. Elle s'appelle « La chaise du fond », elle est d'Odile Brassard-Vézina, et elle ouvre son recueil « Les jours de semaine ».", True),
        ("GASPARD", "Six pages. Une femme arrive à son propre pot de départ à la retraite, dans la cafétéria de l'usine où elle a travaillé trente et un ans.", True),
        ("JOSYANE", "Qu'est-ce qu'on est censé comprendre de cette nappe ?", True),
    ], consigne="Première écoute : de quelles œuvres parle-t-il ?",
       notes="Ne pas commenter entre les écoutes. Recueillir seulement les réponses à "
             "la consigne, au tableau, en trois mots.")

    d.dialogue('Écoute 2 · les chiffres', "Six pages, vingt-deux vers", [
        ("GASPARD", "Rien n'est censé, et c'est tout l'art de cette auteure-là. Deux lectures se défendent, et l'une n'est pas plus fine que l'autre.", True),
        ("GASPARD", "La phrase entre parenthèses tranche en faveur de la seconde. Une seule parenthèse dans six pages.", True),
        ("GASPARD", "« Déneigement », de Régine Amyot. Vingt-deux vers, trois strophes. Une personne dégage son auto tous les matins de janvier, avant six heures.", True),
        ("GASPARD", "La troisième strophe change un seul mot, et ce mot fait basculer les vingt et un autres.", True),
    ], consigne="Deuxième écoute : relevez tous les chiffres.",
       notes="Six pages, trente et un ans, une parenthèse, vingt-deux vers, trois "
             "strophes, un mot, vingt et un vers. Sept chiffres : les écrire au "
             "tableau à mesure.")

    d.dialogue('Écoute 3 · ce qui revient', "Ce qui compte est dit une fois", [
        ("GASPARD", "Ce qui ne veut pas dire que la première lecture est fausse. Elle explique moins de choses, voilà tout. C'est le seul critère que je connaisse.", True),
        ("GASPARD", "Le lecteur a l'impression d'avoir été distrait pendant deux strophes. C'est faux : il n'a rien manqué. L'information n'était pas là.", True),
        ("GASPARD", "Chez Brassard-Vézina, ce qui compte est dit une seule fois, entre parenthèses. Chez Amyot, ce qui compte est dit à la fin, en un mot.", True),
        ("GASPARD", "Dans les deux cas, un lecteur pressé passe à côté et n'en saura jamais rien.", True),
    ], consigne="Troisième écoute : qu'est-ce qu'il dit deux fois ?",
       notes="La réponse : « ce qui compte est dit une seule fois ». Il le dit de deux "
             "façons pour deux œuvres, et c'est le titre du défi. Le faire trouver "
             "plutôt que le donner.")

    d.regle("Une lecture n'est pas fausse parce qu'une autre explique plus",
            "Elle explique moins de choses, voilà tout. C'est le seul critère.",
            precision="Gaspard Thivierge le dit d'une nouvelle ; c'est la même règle "
                      "qu'en B2, appliquée à un texte au lieu d'une scène. Elle vaut "
                      "partout dans ce module, et c'est la seule qui y vaille.",
            notes="Diapositive à photographier. Faire remarquer qu'un critique de "
                  "journal emploie exactement la règle du cercle du mardi : ce n'est "
                  "pas un savoir scolaire.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la chronique.", [
        ("« La chaise du fond » ouvre un recueil.", "vrai"),
        ("La nouvelle fait une trentaine de pages.", "faux - six pages"),
        ("Gisèle a travaillé trente et un ans à l'usine.", "vrai"),
        ("Il dit que la lecture tendre est fausse.", "faux - elle explique moins"),
        ("Le poème compte trois strophes.", "vrai"),
        ("Le basculement se produit à la deuxième strophe.", "faux - à la troisième"),
    ], corrige=True,
       notes="Exercice `t21` du module. Le quatrième est le seul qui demande "
             "réflexion : « moins » n'est pas « faux », et c'est toute la nuance du "
             "module.")

    d.billet(
        "Écoutez une chronique ou un reportage de dix minutes cette semaine, "
        "et notez trois choses : le sujet, deux chiffres, une phrase répétée.",
        exemples=[
            "Radio, balado, ou une capsule vidéo : peu importe.",
            "Écoutez deux fois si vous le pouvez, avec une consigne différente.",
        ],
        notes="Devoir d'écoute. La méthode transférée hors du module est la vraie "
              "acquisition de la séance.")

    return d.save(dossier)
