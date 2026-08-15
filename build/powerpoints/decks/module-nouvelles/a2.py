# -*- coding: utf-8 -*-
"""A2 · Quatre sortes de nouvelles.
Bloc A · couleur foret (vocabulaire) · 60 min.
Source : exercice `prClass` — fait divers, régionale, nationale, internationale.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='foret',
        titre='Quatre sortes de nouvelles',
        chapeau="Un feu de forêt en Australie, une piste cyclable à Alma, un cycliste "
                "qui heurte un chevreuil. Trois nouvelles, trois catégories — et le "
                "classement n'est pas une question d'importance.",
        duree='60 minutes')

    d.titre(notes="Écrire les trois exemples du chapeau au tableau et demander au groupe "
                  "de les classer avant toute explication. Le classement spontané "
                  "confond souvent importance et portée.")

    d.objectifs([
        "distinguer une nouvelle régionale, nationale et internationale ;",
        "reconnaître un fait divers ;",
        "classer une nouvelle d'après sa portée, pas son importance ;",
        "nommer la catégorie d'une nouvelle qu'on entend.",
    ])

    d.tableau('Analyse', "Quatre catégories",
              ['La catégorie', 'Ce qu\'elle touche'],
              [["une nouvelle régionale", "une région de la province"],
               ["une nouvelle nationale", "la province ou le pays"],
               ["une nouvelle internationale", "l'extérieur du pays"],
               ["un fait divers", "des faits quotidiens qui attirent la curiosité"]],
              cle=0, props=[0.42, 0.58],
              note="Les trois premières se distinguent par le territoire. Le fait divers, "
                   "lui, se distingue par le sujet.",
              notes="C'est la clé de la séance : trois catégories de territoire, une "
                    "catégorie de sujet. Elles ne se classent pas sur le même axe.")

    d.regle('La règle',
            "La portée, pas l'importance.",
            precision="Une piste cyclable à Alma est une nouvelle régionale même si elle "
                      "compte beaucoup pour les gens d'Alma. Un feu de forêt en "
                      "Australie est international même s'il n'a aucun effet ici. La "
                      "question est : quel territoire est concerné ?",
            notes="Diapo centrale. Beaucoup d'élèves classent selon ce qui les touche : "
                  "corriger explicitement.")

    d.cartes('Analyse', "Comment reconnaître un fait divers", [
        ("Un événement unique",
         "Un accident, un sauvetage, une découverte étrange. Ce n'est pas une tendance "
         "ni une décision politique : c'est quelque chose qui est arrivé une fois."),
        ("Des personnes ordinaires",
         "Une fillette, un cycliste, une voisine. Pas de ministre, pas d'entreprise, "
         "pas d'institution en vedette."),
        ("Aucune conséquence générale",
         "Le chat retrouvé ne change rien pour personne d'autre que sa famille. C'est ce "
         "qui distingue le fait divers de la nouvelle nationale."),
        ("Ce qui attire la curiosité",
         "Le fait divers est raconté parce qu'il touche, surprend ou émeut — pas parce "
         "qu'il faut le savoir."),
    ], notes="La troisième carte est le critère le plus fiable. Faire l'appliquer à "
             "chaque énoncé de l'exercice.")

    d.pratique('Pratique · 1 de 4', "Classez la nouvelle",
               "Fait divers, régionale, nationale ou internationale ?", [
        ("En Australie, des feux de forêt forcent l'évacuation de plusieurs villages.",
         "internationale — hors du pays"),
        ("Une pénurie de main-d'œuvre touche plusieurs secteurs au Canada.",
         "nationale — tout le pays"),
        ("Un cycliste entre en collision avec un chevreuil sur une route de campagne.",
         "fait divers — un événement unique"),
        ("Une nouvelle piste cyclable aménagée à Alma.", "régionale — une ville"),
        ("L'endettement des ménages canadiens continue d'augmenter.",
         "nationale — une tendance au pays"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par le territoire ou par le sujet. Ne jamais "
             "accepter « parce que c'est important ».")

    d.pratique('Pratique · 2 de 4', "Régionale ou fait divers ?",
               "Le plus difficile : les deux se passent près de chez nous.", [
        ("Une école de Longueuil amasse deux cents paires de mitaines.",
         "fait divers ou régionale — les deux se défendent"),
        ("La Ville de Longueuil augmente les taxes de deux pour cent.",
         "régionale — une décision qui touche tout le monde"),
        ("Une fillette retrouve son chat grâce à une affiche.",
         "fait divers — un événement unique, sans conséquence générale"),
        ("Un nouveau CHSLD ouvrira à Sherbrooke l'an prochain.",
         "régionale — un service pour la région"),
    ], corrige=True,
       notes="Le premier item est volontairement ambigu. Laisser le groupe argumenter : "
             "les deux réponses se défendent, et c'est instructif.")

    d.piege("Le piège de l'importance personnelle",
            "C'est une nouvelle nationale, parce que ça me concerne beaucoup.",
            "La catégorie dépend du territoire touché, pas de moi.",
            "Une nouvelle qui vous concerne personnellement peut être régionale, ou même "
            "un fait divers. La catégorie ne juge pas de la valeur : elle dit seulement "
            "qui est concerné.",
            notes="Faire donner par chacun une nouvelle qui l'a touché personnellement, "
                  "puis la classer. L'exercice est éclairant.")

    d.piege("Le piège du lieu mentionné",
            "Un feu à Montréal : c'est régional, parce que Montréal est nommé.",
            "Cela dépend : un feu chez un particulier est un fait divers.",
            "Le nom d'une ville n'en fait pas une nouvelle régionale. Ce qui compte est "
            "l'étendue de ce qui est touché : un immeuble, un quartier, une ville "
            "entière ? Le lieu est un indice, pas une preuve.",
            notes="Nuance fine mais utile. Donner trois exemples de feux à Montréal, de "
                  "portées différentes.")

    d.pratique('Pratique · 3 de 4', "Trouvez la catégorie",
               "D'après le début de la nouvelle.", [
        ("« Le gouvernement du Québec annonce un investissement en santé… »", "nationale"),
        ("« Deux passants ont secouru un cycliste blessé à Trois-Pistoles… »", "fait divers"),
        ("« La bibliothèque de Rimouski prolonge ses heures d'ouverture… »", "régionale"),
        ("« Une tempête frappe la côte est des États-Unis… »", "internationale"),
        ("« Les élèves d'une classe de Victoriaville tournent un documentaire… »",
         "fait divers ou régionale"),
    ], corrige=True,
       notes="Faire remarquer que la première phrase suffit presque toujours à classer. "
             "C'est un réflexe d'écoute utile.")

    d.pratique('Pratique · 4 de 4', "Classez vos propres nouvelles",
               "Reprenez le billet de la séance A1.", [
        ("Votre nouvelle", "de quelle catégorie ?"),
        ("La justification", "quel territoire, ou quel type de sujet ?"),
        ("Une autre nouvelle de la semaine", "d'une catégorie différente"),
    ], corrige=False,
       notes="Dix minutes. Faire classer les nouvelles apportées par le groupe au "
             "tableau, en quatre colonnes. Le tableau collectif vaut mieux que l'exercice "
             "individuel.")

    d.billet(
        "Écrivez quatre titres de nouvelles, un par catégorie.",
        exemples=[
            "Une régionale, une nationale, une internationale, un fait divers.",
            "Un titre court : cinq à huit mots.",
        ],
        notes="Ces titres serviront en E1, où chacun développera l'un d'eux en un vrai "
              "fait divers.")

    return d.save(dossier)
