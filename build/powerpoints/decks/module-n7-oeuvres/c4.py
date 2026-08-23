# -*- coding: utf-8 -*-
"""C4 · Tellement froid que j'oublie de compter
Bloc C « Défi 2 » · couleur teal · écoute et réponds · 75 min.
Source : exercices `t2int` et `t2gen`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='teal',
        titre="Tellement froid que j'oublie de compter",
        chapeau="« Le film est lent » se répond par « moi je ne trouve pas ». "
                "« Le film est assez lent pour que la moitié de la salle "
                "décroche » ne se répond plus.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, mais c'est en réalité la séance qui fabrique "
                  "les arguments de D1. Le dire au groupe d'entrée : ce qu'on "
                  "apprend ici servira jeudi.")

    d.objectifs([
        "exprimer un degré et sa conséquence avec « tellement... que » ;",
        "employer « trop » et « assez... pour que » avec le subjonctif ;",
        "alléger en « pour » plus infinitif quand le sujet est le même ;",
        "distinguer un nom pris en général d'un nom pris en particulier.",
    ], notes="Les trois premiers objectifs sont une seule construction sous trois "
             "formes. Le quatrième est un savoir distinct, placé ici parce que "
             "l'exemple du programme est lui-même musical.")

    d.declencheur(
        'Préparation', "Comment dit-on jusqu'à quel point ?",
        pistes=[
            "« Il fait froid » : comment dire que c'est vraiment beaucoup ?",
            "Et pour dire ce que ce froid entraîne ?",
            "Y a-t-il une différence entre « si froid que » et « trop froid pour » ?",
            "Dans laquelle des deux la chose arrive-t-elle vraiment ?",
        ],
        notes="La quatrième piste est la règle entière : « que » dit ce qui arrive, "
              "« pour que » dit ce qui est empêché. Le reste de la séance ne fait que "
              "l'installer.")

    d.tableau('Analyse', "Trois tournures, deux modes",
              ['La tournure', 'Ce qu\'elle dit'],
              [["si ou tellement + que",
                "le degré est fort, et la conséquence a lieu : indicatif"],
               ["tellement de ou tant de + nom",
                "avec un nom, il faut le « de »"],
               ["trop ou assez + pour que",
                "la conséquence est empêchée ou rendue possible : subjonctif"]],
              cle=0,
              note="Retenez la paire : « que » indicatif, « pour que » subjonctif.",
              notes="Diapositive à photographier. Toute la séance tient dans la "
                    "dernière ligne du tableau.")

    d.regle("Après « pour que », jamais l'indicatif",
            "« Trop cher pour qu'on puisse y aller », et non « pour qu'on peut ».",
            precision="Sept subjonctifs suffisent pour presque tous les cas : qu'il "
                      "soit, qu'il ait, qu'il fasse, qu'il aille, qu'il puisse, qu'il "
                      "sache, qu'il veuille. Ce sont les mêmes qui serviront à la "
                      "concession en D2.",
            notes="Diapositive à photographier. Faire répéter les sept d'affilée. Ils "
                  "reviennent dans deux séances et dans les deux productions.")

    d.piege('Grammaire',
            "« Elle est trop fatiguée pour qu'elle sorte. »",
            "« Elle est trop fatiguée pour sortir. »",
            "Quand c'est la même personne des deux côtés, on allège : « pour » "
            "plus infinitif. « Pour que » plus subjonctif ne sert que si les "
            "deux sujets diffèrent. La première phrase n'est pas seulement "
            "lourde, elle est fautive.",
            notes="Le test : demander qui fait quoi de chaque côté. Deux fois la même "
                  "personne, un seul verbe conjugué.")

    d.tableau('Analyse', "En général, ou cette chose-là",
              ['La phrase', 'De quoi on parle'],
              [["La musique, ça me calme",
                "de toute la musique : le « ça » est le signe"],
               ["La musique de ce film",
                "de celle-là, accrochée par un complément"],
               ["Il y a un sketch qui parle",
                "d'un seul, et c'est ainsi qu'on l'introduit à l'oral"]],
              cle=0,
              note="« Les films lents, ça m'endort » est un goût. « Ce film-là m'a endormie » est un avis.",
              notes="Diapositive à photographier. La note fait le lien avec A4 : la "
                    "différence de sens est aussi une différence d'honnêteté.")

    d.pratique('Grammaire', "Reliez le degré et sa conséquence",
               "Employez la tournure demandée.", [
        ("Le vent est froid. Elle oublie de compter. (tellement... que)", "tellement froid qu'elle oublie"),
        ("Il y a du monde. Nous restons debout. (tellement de... que)", "tellement de monde que nous restons"),
        ("Le refrain monte haut. Elle le manque. (trop... pour que)", "trop haut pour qu'elle le réussisse"),
        ("Le film est lent. La salle décroche. (assez... pour que)", "assez lent pour que la salle décroche"),
        ("Elle est fatiguée. Elle ne monte pas. (même sujet)", "trop fatiguée pour monter"),
        ("Le billet coûte cher. Nous n'y allons pas. (trop... pour que)", "trop cher pour que nous puissions y aller"),
    ], corrige=True,
       notes="Exercice `t2int` du module. Le troisième et le sixième portent le "
             "subjonctif : les faire corriger à voix haute, deux fois.")

    d.pratique('Écoute', "En général, ou cette chose-là ?",
               "Écoutez et classez chaque phrase.", [
        ("La musique, ça me calme.", "en général"),
        ("La musique de ce film intervient onze fois.", "cette chose-là"),
        ("Un bon sketch, ça se termine par une chute.", "en général"),
        ("Il y a un sketch qui parle d'un comptoir de pièces.", "cette chose-là"),
    ], corrige=True,
       notes="Exercice `t2gen` du module, qui en compte huit. Faire relever le signe "
             "à chaque fois : le « ça », ou le complément qui accroche.")

    d.billet(
        "Transformez un de vos avis en argument, avec un degré et sa conséquence.",
        exemples=[
            "Assez... pour que, ou tellement... que.",
            "Une seule phrase, et vérifiez le mode du verbe.",
        ],
        notes="Fin du bloc C. Ces phrases sont exactement ce que Marilou dira en D1 : "
              "les garder, elles serviront de modèle.")

    return d.save(dossier)
