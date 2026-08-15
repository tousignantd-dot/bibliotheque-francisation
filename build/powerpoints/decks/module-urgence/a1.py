# -*- coding: utf-8 -*-
"""A1 · Une brûlure en cuisine — mise en situation.
Bloc A « Je découvre » · couleur teal · 75 min.
Source du module : dialogue `prep`, exercices `prVocab` et `pr1`, cartes mémoire.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='teal',
        titre='Une brûlure en cuisine',
        chapeau="En pleine heure de pointe, de l'huile chaude éclabousse l'avant-bras de "
                "Fatou. Ce qui se passe dans les quinze minutes suivantes décidera de "
                "tout le reste.",
        duree='75 minutes')

    d.titre(notes="Ouverture du module 2. Écrire au tableau : QUINZE MINUTES. C'est le "
                  "chiffre de la séance, et le seul geste qui compte vraiment.")

    d.objectifs([
        "nommer une brûlure et décrire son aspect ;",
        "connaître le premier geste à faire, et pendant combien de temps ;",
        "savoir ce qu'il ne faut jamais faire sur une brûlure ;",
        "distinguer le 911 du 811.",
    ], notes="Prévenir qu'on reviendra à ces objectifs sur le billet de sortie.")

    d.declencheur(
        'Mise en situation', "De l'huile chaude vient de vous éclabousser le bras. Que faites-vous ?",
        pistes=[
            "Quel est votre tout premier geste ?",
            "Pendant combien de temps ?",
            "Est-ce qu'on met quelque chose sur la peau ? Quoi ?",
            "Est-ce qu'on appelle ? Qui ?",
        ],
        notes="Cinq minutes en grand groupe. Noter les réponses au tableau sans corriger. "
              "Plusieurs proposeront la glace, le beurre ou le dentifrice : ce sont "
              "précisément les trois erreurs, et on y reviendra.")

    d.cartes('La situation', "Ce qu'on sait de Fatou", [
        ("Où elle est",
         "En cuisine, en pleine heure de pointe. L'accident arrive vers onze heures, "
         "pendant le service."),
        ("Ce qui est arrivé",
         "L'huile chaude a éclaboussé son avant-bras droit. La peau devient rouge, puis "
         "de petites cloques apparaissent."),
        ("Qui réagit",
         "Mathieu, son collègue. Il l'amène à l'évier avant de faire quoi que ce soit "
         "d'autre."),
        ("Qui décide",
         "Une infirmière d'Info-Santé, au bout du fil. Ce n'est ni Fatou ni Mathieu qui "
         "tranche : c'est une professionnelle."),
    ], notes="La quatrième carte est le message caché de la séance : on n'a pas à savoir "
             "seul si c'est grave. Quelqu'un répond, jour et nuit, gratuitement.")

    d.dialogue('Dialogue · 1 de 3', "Viens à l'évier, tout de suite", [
        ("FATOU", "Mathieu ! L'huile a éclaboussé, je me suis brûlé l'avant-bras.", True),
        ("MATHIEU", "Ne touche à rien. Viens à l'évier, on met ça sous l'eau froide tout "
                    "de suite.", True),
        ("FATOU", "Ça chauffe beaucoup… et la peau devient rouge.", False),
        ("MATHIEU", "On laisse couler quinze minutes, c'est ce qu'il faut faire. Pendant "
                    "ce temps, j'appelle Info-Santé au 811.", True),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="Passer l'audio de « Je découvre » avant d'afficher le texte. Faire "
             "remarquer que Mathieu ne pose aucune question avant d'agir : l'eau "
             "d'abord, les questions ensuite.")

    d.dialogue('Dialogue · 2 de 3', "Pourquoi pas le 911 ?", [
        ("FATOU", "Pourquoi pas le 911 ?", True),
        ("MATHIEU", "Le 911, c'est quand la vie est en danger. Là, une infirmière va nous "
                    "dire quoi faire.", True),
    ], notes="Deux répliques, mais c'est le cœur du module. Écrire au tableau : 911 = la "
             "vie en danger. 811 = un conseil.")

    d.dialogue('Dialogue · 3 de 3', "Décrivez-moi la brûlure", [
        ("L'INFIRMIÈRE", "Info-Santé, bonjour. Décrivez-moi la brûlure.", False),
        ("MATHIEU", "Une brûlure à l'avant-bras avec de l'huile chaude. La peau est rouge "
                    "et il y a de petites cloques.", True),
        ("L'INFIRMIÈRE", "Des cloques, c'est une brûlure du deuxième degré. Continuez "
                         "l'eau froide, ne percez rien, et rendez-vous à l'urgence "
                         "aujourd'hui.", True),
    ], notes="Faire compter les informations données par Mathieu : l'endroit, la cause, "
             "l'aspect de la peau. Trois éléments, et l'infirmière peut décider.")

    d.regle('Le premier geste',
            "De l'eau fraîche qui coule, pendant quinze minutes, tout de suite.",
            precision="Pas de glace, pas de beurre, pas de dentifrice, pas de pommade. "
                      "Rien d'autre que de l'eau qui coule. Et quinze minutes, montre en "
                      "main : trois minutes ne suffisent pas.",
            notes="Diapo centrale du module. La laisser affichée longtemps. Demander à "
                  "quelqu'un de compter quinze minutes à voix haute — le groupe "
                  "comprendra que c'est très long.")

    d.tableau('Analyse', "Les trois degrés d'une brûlure",
              ['Le degré', 'Ce qu\'on voit', 'Quoi faire'],
              [["premier", "la peau est rouge", "eau fraîche, surveiller"],
               ["deuxième", "des cloques apparaissent", "eau fraîche, puis consulter"],
               ["troisième", "la peau est blanche ou noire", "911, sans attendre"]],
              cle=0,
              note="Les cloques sont la limite : dès qu'il y en a, on consulte le jour "
                   "même.",
              notes="Insister sur le troisième degré : une brûlure profonde ne fait "
                    "parfois pas mal, parce que les nerfs sont détruits. L'absence de "
                    "douleur n'est pas rassurante.")

    d.vocabulaire('Vocabulaire · 1 de 2', "La blessure", [
        ("une brûlure", "Une blessure causée par la chaleur, le feu ou un liquide chaud."),
        ("une cloque", "Une petite poche de liquide sur la peau brûlée."),
        ("une plaie", "Une blessure ouverte sur la peau."),
        ("le deuxième degré", "Le niveau d'une brûlure avec des cloques."),
        ("une cicatrice", "La marque qui reste sur la peau après une blessure."),
        ("éclabousser", "Projeter un liquide en gouttes."),
    ], notes="Faire prononcer « éclabousser » plusieurs fois : c'est un mot long et "
             "rare, mais c'est celui qui raconte exactement l'accident.")

    d.vocabulaire('Vocabulaire · 2 de 2', "Les soins et les services", [
        ("Info-Santé", "Une ligne téléphonique, le 811, où une infirmière conseille."),
        ("l'urgence", "Le service de l'hôpital pour les cas qui ne peuvent pas attendre."),
        ("un pansement", "Ce qu'on pose sur une plaie pour la protéger."),
        ("désinfecter", "Nettoyer pour éliminer les microbes."),
        ("un congé de maladie", "Des jours autorisés pour ne pas travailler quand on est blessé."),
        ("la salle d'attente", "L'endroit où les gens attendent leur tour."),
    ], notes="Vérifier que chacun a noté le 811 dans son téléphone avant de sortir. "
             "C'est le geste le plus utile de la séance.")

    d.pratique('Pratique', "Vrai ou faux — une brûlure en cuisine",
               "Répondez sans relire le dialogue.", [
        ("Fatou s'est brûlée avec de l'eau bouillante.", "FAUX — avec de l'huile chaude"),
        ("Mathieu met tout de suite le bras sous l'eau froide.", "VRAI"),
        ("Il faut laisser couler l'eau froide quinze minutes.", "VRAI"),
        ("Mathieu appelle le 911.", "FAUX — il appelle le 811"),
        ("Le 911 sert quand la vie est en danger.", "VRAI"),
        ("Il y a de petites cloques sur la peau de Fatou.", "VRAI"),
        ("L'infirmière conseille de percer les cloques.", "FAUX — de ne rien percer"),
        ("Des cloques indiquent une brûlure du deuxième degré.", "VRAI"),
    ], corrige=True,
       notes="La quatrième trompe presque tout le monde : les deux numéros sont "
             "prononcés dans le dialogue, à quelques secondes d'écart.")

    d.piege('Le piège des remèdes de maison',
            "Je mets du beurre — ou de la glace, ou du dentifrice.",
            "De l'eau fraîche qui coule, rien d'autre.",
            "Le beurre garde la chaleur dans la peau et aggrave la brûlure. La glace "
            "gèle les tissus déjà abîmés. Le dentifrice infecte la plaie. Ces trois "
            "gestes sont courants dans beaucoup de familles, et tous les trois nuisent.",
            notes="Traiter cette diapo avec respect : ces remèdes viennent souvent de "
                  "la famille de l'élève. Expliquer pourquoi ils nuisent, sans juger "
                  "ceux qui les emploient.")

    d.billet(
        "En une phrase : que ferez-vous la prochaine fois que vous vous brûlerez ?",
        exemples=[
            "Nommez le geste, la durée, et qui vous appellerez.",
            "Exemple : « De l'eau fraîche quinze minutes, puis j'appelle le 811. »",
        ],
        notes="Ramasser. Si un billet mentionne encore la glace ou le beurre, y revenir "
              "individuellement : c'est un savoir de sécurité, pas seulement de langue.")

    return d.save(dossier)
