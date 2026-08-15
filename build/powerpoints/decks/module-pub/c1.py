# -*- coding: utf-8 -*-
"""C1 · Deux affiches sur le babillard.
Bloc C · couleur acier (compréhension écrite) · 75 min.
Source : exercice `t2pubs` — La Grande Réparation et La Nuit des ateliers.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Deux affiches sur le babillard',
        chapeau="Deux activités du même quartier, deux affiches côte à côte. Elles "
                "annoncent presque la même chose — et pourtant elles ne s'adressent pas "
                "aux mêmes gens.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2. Distribuer les deux affiches et laisser cinq "
                  "minutes de lecture silencieuse avant toute question.")

    d.objectifs([
        "lire une affiche et en tirer les informations pratiques ;",
        "comparer deux affiches sur plusieurs critères ;",
        "repérer un slogan dans un texte ;",
        "reconnaître un verbe au futur simple dans une publicité.",
    ])

    d.cartes('Affiche 1', "La Grande Réparation", [
        ("Ce qu'on annonce",
         "« Apportez votre grille-pain, votre lampe ou votre chaise bancale : dix "
         "bénévoles répareront vos objets devant vous. »"),
        ("Quand et où",
         "« Le samedi 12 avril, de 9 h à 16 h, au sous-sol du centre Sainte-Odile. »"),
        ("Ce qui est offert",
         "« Café et biscuits offerts à tous. »"),
        ("Le slogan",
         "« Rien ne se jette, tout se répare ! » — placé à la fin, comme il se doit."),
    ], notes="Faire remarquer « devant vous » : c'est un détail, et c'est ce qui distingue "
             "cet atelier d'un service de réparation ordinaire.")

    d.cartes('Affiche 2', "La Nuit des ateliers", [
        ("Ce qu'on annonce",
         "« La bibliothèque Saint-Charles ouvre ses ateliers : couture, vélo, petits "
         "appareils. »"),
        ("Quand et où",
         "« Le vendredi 7 novembre, de 18 h à 21 h, à la bibliothèque Saint-Charles. »"),
        ("Le prix",
         "« Entrée : 5 $, gratuite pour les moins de 16 ans. »"),
        ("La promesse",
         "« Vous repartirez avec un objet remis en état et l'envie de recommencer. »"),
    ], notes="Cette affiche n'a pas de slogan : elle finit par une promesse. Le faire "
             "remarquer — c'est une autre façon de terminer.")

    d.tableau('Analyse', "Les deux affiches, comparées",
              ['Le critère', 'La Grande Réparation', 'La Nuit des ateliers'],
              [["le moment", "samedi, de 9 h à 16 h", "vendredi, de 18 h à 21 h"],
               ["le prix", "gratuit pour tous", "5 $, gratuit sous 16 ans"],
               ["le lieu", "centre Sainte-Odile", "bibliothèque Saint-Charles"],
               ["la fin du texte", "un slogan", "une promesse"]],
              cle=0, props=[0.2, 0.4, 0.4],
              notes="Faire déduire le récepteur de chaque affiche : le samedi de jour "
                    "vise les familles, le vendredi soir vise les adultes qui "
                    "travaillent.")

    d.regle('La règle de lecture',
            "Le moment et le prix disent à qui l'affiche s'adresse.",
            precision="Un samedi de neuf à seize heures, gratuit : les familles. Un "
                      "vendredi de dix-huit à vingt et une heures, cinq dollars : les "
                      "adultes qui travaillent le jour. Le récepteur n'est jamais "
                      "nommé, mais il est décidé.",
            notes="Relier à la séance A3 : le récepteur se déduit. Ici, ce sont l'heure "
                  "et le prix qui le donnent.")

    d.pratique('Pratique · 1 de 4', "Six questions sur les deux affiches",
               "Répondez d'après les textes.", [
        ("Quelle affiche annonce une activité le soir ?", "La Nuit des ateliers, 18 h à 21 h"),
        ("Laquelle est gratuite pour tout le monde ?", "La Grande Réparation"),
        ("Qu'est-ce qu'on peut apporter à La Grande Réparation ?",
         "un grille-pain, une lampe ou une chaise bancale"),
        ("Dans quelle affiche parle-t-on de couture ?", "La Nuit des ateliers"),
        ("Quelle affiche se termine par un slogan ?",
         "La Grande Réparation : « Rien ne se jette, tout se répare ! »"),
        ("Combien de bénévoles à La Grande Réparation ?", "dix"),
    ], corrige=True,
       notes="Faire pointer la phrase exacte pour chaque réponse. C'est la méthode de "
             "lecture qu'on installe depuis le début du module.")

    d.pratique('Pratique · 2 de 4', "Trouvez le futur simple",
               "Un verbe au futur dans chaque affiche.", [
        ("Dans La Grande Réparation", "répareront — dix bénévoles répareront vos objets"),
        ("Dans La Nuit des ateliers", "repartirez — vous repartirez avec un objet"),
        ("Pourquoi le futur ?", "l'événement n'a pas encore eu lieu"),
        ("Quel effet ça produit ?", "on imagine déjà ce qui va se passer"),
    ], corrige=True,
       notes="Le futur d'une publicité fait imaginer le résultat. C'est une technique, "
             "pas seulement une question de temps verbal.")

    d.pratique('Pratique · 3 de 4', "À qui chaque affiche s'adresse-t-elle ?",
               "Déduisez le récepteur du moment et du prix.", [
        ("La Grande Réparation", "les familles du quartier — samedi de jour, gratuit"),
        ("La Nuit des ateliers", "les adultes qui travaillent le jour — vendredi soir"),
        ("Quel indice vous l'a fait deviner ?", "l'heure et le prix"),
        ("Une affiche pour les adolescents ?", "La Nuit — gratuite pour les moins de 16 ans"),
    ], corrige=True,
       notes="Le quatrième item est le plus fin : la gratuité sous seize ans vise aussi "
             "les jeunes. Une affiche peut avoir deux récepteurs.")

    d.piege("Le piège de l'affiche lue en diagonale",
            "C'est gratuit, j'y vais.",
            "Cinq dollars, gratuit pour les moins de 16 ans.",
            "Le mot « gratuit » attire l'œil, mais il est souvent accompagné d'une "
            "condition. Lisez la phrase entière avant de conclure : c'est vrai des "
            "affiches de quartier comme des publicités commerciales.",
            notes="Faire chercher, dans les deux affiches, tous les mots qui posent une "
                  "condition : « pour les moins de », « à tous », « sur place ».")

    d.piege("Le piège de la promesse prise pour un fait",
            "« Vous repartirez avec l'envie de recommencer. »",
            "C'est une promesse, pas une information.",
            "Une affiche mélange des faits — la date, le prix, l'adresse — et des "
            "promesses. « Vous repartirez avec un objet remis en état » est un fait "
            "vérifiable ; « l'envie de recommencer » est un espoir. Les deux sont dans "
            "la même phrase.",
            notes="Point d'analyse critique. Faire séparer, dans les deux affiches, les "
                  "faits des promesses.")

    d.pratique('Pratique · 4 de 4', "Fait ou promesse ?",
               "Vérifiable, ou espéré ?", [
        ("« Dix bénévoles répareront vos objets. »", "fait — on peut les compter"),
        ("« Vous repartirez avec l'envie de recommencer. »", "promesse"),
        ("« Café et biscuits offerts à tous. »", "fait"),
        ("« Rien ne se jette, tout se répare. »", "ni l'un ni l'autre — c'est un slogan"),
    ], corrige=True,
       notes="Le quatrième item introduit une troisième catégorie. Le slogan n'est pas "
             "une information : c'est une idée.")

    d.billet(
        "Comparez les deux affiches en trois phrases.",
        exemples=[
            "Employez « plus… que » ou « moins… que » dans chaque phrase.",
            "Trois critères différents : le moment, le prix, ce qu'on y fait.",
        ],
        notes="C'est la révision de B2 dans une situation nouvelle. Corriger la "
              "construction de la comparaison.")

    return d.save(dossier)
