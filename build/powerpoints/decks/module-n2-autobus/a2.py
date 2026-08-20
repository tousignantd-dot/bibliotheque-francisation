# -*- coding: utf-8 -*-
"""A2 · Entendre l'heure.
Bloc A « Je découvre » · couleur indigo (graphie-phonie) · 60 min.
Source : exercice `prHeure`, mini-leçon `t2horaire`.

La séance de graphie-phonie du module. Elle ne porte pas sur des lettres mais
sur les chiffres de l'heure : c'est là que l'oreille d'un élève de niveau 2
décroche à l'arrêt d'autobus, et le module tout entier en dépend.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-autobus/images/')


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Entendre l'heure",
        chapeau="L'écran de l'arrêt écrit 8 h 15. La personne à côté dit "
                "« huit heures et quart ». Il faut comprendre les deux.",
        duree='60 minutes')

    d.titre(notes="Séance d'écoute avant tout. Prévoir de dire chaque heure trois fois : "
                  "une fois lentement, une fois au rythme normal, une fois lentement.")

    d.objectifs([
        "reconnaître une heure dite à voix haute ;",
        "dire une heure de deux façons ;",
        "distinguer les heures qui se ressemblent ;",
        "comprendre « dans dix minutes ».",
    ])

    d.declencheur(
        'Écoute', "Quelle heure entendez-vous ?",
        image=IMG + 'horaire-affiche.jpg',
        pistes=[
            "Que voit-on sur ce panneau ?",
            "À quoi sert-il ?",
            "Qu'est-ce qui est écrit dessus ?",
            "Est-ce facile à lire ?",
        ],
        notes="Dire trois heures à voix haute avant d'afficher quoi que ce soit : 8 h 10, "
              "8 h 30, 8 h 45. Faire écrire les chiffres sur une feuille. Corriger après.")

    d.tableau('Analyse', "La même heure, deux façons",
              ['Sur l\'écran', 'Ce que dit la personne'],
              [["8 h 10", "huit heures dix"],
               ["8 h 15", "huit heures et quart"],
               ["8 h 30", "huit heures et demie"],
               ["8 h 45", "neuf heures moins le quart"]],
              cle=2,
              note="À 8 h 45, on annonce déjà NEUF heures : « moins le quart » se compte "
                   "sur l'heure qui vient.",
              notes="Diapositive à photographier. La dernière ligne est celle qui coûte le "
                    "plus cher : la faire répéter trois fois.")

    d.regle("Et quart, et demie, moins le quart",
            "Trois expressions couvrent presque tout.",
            precision="<b>Et quart</b> = 15 minutes. <b>Et demie</b> = 30 minutes. "
                      "<b>Moins le quart</b> = 45 minutes, sur l'heure suivante.",
            notes="Diapositive à photographier. Dessiner une horloge au tableau et montrer "
                  "les quarts : beaucoup l'ont appris ainsi dans leur langue.")

    d.piege('Piège', "huit heures moins le quart", "neuf heures moins le quart",
            "Pour 8 h 45, on annonce l'heure <b>qui vient</b>, pas celle qu'on quitte. "
            "C'est l'erreur la plus fréquente, et elle fait manquer l'autobus d'une heure.",
            notes="Prendre le temps sur cette diapositive. Faire dire 7 h 45, 9 h 45, "
                  "10 h 45 par le groupe, en chœur.")

    d.cartes("Deux mots à ne pas confondre", "« à » et « dans »", [
        ("dans cinq minutes",
         "À partir de maintenant. C'est ce que dit la personne à l'arrêt quand elle "
         "regarde l'écran."),
        ("à cinq heures",
         "Une heure fixe, sur l'horloge. Rien à voir avec le moment où on parle."),
        ("à cinq minutes",
         "Seulement pour une distance : « c'est à cinq minutes à pied »."),
    ], cols=3, notes="Diapositive à photographier. Faire produire une phrase de chaque "
                     "sorte par trois élèves différents.")

    d.pratique('Écoute', "Quelle heure entends-tu ?",
               "L'enseignant dit une heure. Écrivez les chiffres.", [
        ("« huit heures dix »", "8 h 10"),
        ("« huit heures et demie »", "8 h 30"),
        ("« neuf heures moins le quart »", "8 h 45"),
        ("« onze heures et quart »", "11 h 15"),
    ], corrige=True, cols=1,
       notes="Dire chaque heure deux fois. Laisser dix secondes entre chacune. Corriger au "
             "tableau, en écrivant les deux formes côte à côte.")

    d.pratique('Pratique · à deux', "Dites-vous l'heure",
               "Un élève dit une heure, l'autre l'écrit. Puis on échange.", [
        ("Étape 1", "Écrivez cinq heures sur une feuille, en chiffres."),
        ("Étape 2", "Dites-les à votre voisin, à voix haute."),
        ("Étape 3", "Votre voisin écrit ce qu'il entend."),
        ("Étape 4", "Comparez les deux feuilles."),
    ], cols=1,
       notes="Vingt minutes. C'est l'exercice qui fait le plus progresser de tout le "
             "module : il oblige à écouter pour de vrai.")

    d.billet(
        "Écrivez l'heure de trois choses de votre semaine.",
        exemples=[
            "Le cours commence à huit heures et demie.",
            "Je pars à sept heures moins le quart.",
        ],
        notes="Devoir court. Accepter les deux formes, chiffres ou mots.")

    return d.save(dossier)
