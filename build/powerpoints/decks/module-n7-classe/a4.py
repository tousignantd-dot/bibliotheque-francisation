# -*- coding: utf-8 -*-
"""A4 · À un ami, ou devant la classe ?
Bloc A « Je découvre » · couleur ambre · 75 min.
Source : exercice `prRegistre`, mini-leçon `prRegistre`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="À un ami, ou devant la classe ?",
        chapeau="La question n'est jamais « est-ce du bon français ? », mais "
                "« est-ce le français de cette situation-là ? ». Une phrase "
                "impeccable au mauvais endroit se remarque autant qu'une "
                "faute.",
        duree='75 minutes')

    d.titre(notes="Séance de langue, et elle porte sur un savoir du niveau : "
                  "reconnaître les variétés de langue et en tenir compte. Elle "
                  "prépare deux choses du bloc E : l'exposé, soigné, et la lettre au "
                  "camarade, familière mais organisée.")

    d.objectifs([
        "reconnaître le parler familier et la langue standard ;",
        "savoir que le familier n'est pas une faute, mais une variété située ;",
        "choisir la variété qui convient à l'équipe, à la classe, au jury ;",
        "tenir la même variété du début à la fin d'une intervention.",
    ], notes="Le quatrième objectif est celui qui s'entend le plus quand il n'est pas "
             "atteint : le mélange se remarque bien plus qu'une phrase entièrement "
             "familière.")

    d.declencheur(
        'Observation', "La même idée, deux façons",
        pistes=[
            "« Ça marche pas, ton affaire. »",
            "« Je ne suis pas certaine que ta méthode fonctionne. »",
            "Laquelle diriez-vous à un coéquipier ? À un employeur ?",
            "Est-ce que l'une des deux est fautive ?",
        ],
        notes="La réponse à la dernière question est non, et il faut le dire "
              "clairement. Beaucoup d'élèves ont appris que le familier est du "
              "mauvais français ; ce module dit qu'il est situé.")

    d.tableau('Analyse', "Trois variétés, trois endroits",
              ['La variété', 'Où elle est à sa place'],
              [["Familière",
                "entre camarades, à la pause, dans un message à un ami"],
               ["Standard",
                "en équipe, en classe, au travail, avec une personne inconnue"],
               ["Soutenue",
                "devant un groupe, devant un jury, dans une lettre officielle"]],
              cle=0,
              note="On tutoie ses coéquipiers et on parle standard : les deux vont ensemble.",
              notes="Diapositive à photographier. La note du bas règle la confusion "
                    "la plus fréquente : tutoiement et registre sont deux choses "
                    "différentes.")

    d.tableau('Analyse', "Ce qui change d'une variété à l'autre",
              ['Ce qui change', 'Exemple'],
              [["Les mots",
                "une affaire, une patente / un dossier, un document"],
               ["Les tournures",
                "on se voit-tu ? / est-ce que nous nous voyons ?"],
               ["Ce qu'on efface",
                "y'a rien là / il n'y a pas de problème"],
               ["La négation",
                "ça marche pas / cela ne fonctionne pas"]],
              cle=0,
              note="Ce n'est jamais la grammaire qui change : ce sont ces quatre choses.",
              notes="Diapositive à photographier. La note du bas est importante : le "
                    "familier a ses règles, il n'est pas de la grammaire relâchée.")

    d.pratique('Compréhension', "Familier ou standard ?",
               "Dites à quelle variété appartient chaque phrase.", [
        ("« Ça marche pas, ton affaire. »", "familier"),
        ("« Je ne suis pas certaine que ta méthode fonctionne. »", "standard"),
        ("« Wo, minute, tu vas ben trop vite. »", "familier"),
        ("« Pourrais-tu reprendre plus lentement ? »", "standard"),
        ("« Faque là, on fait quoi ? »", "familier"),
        ("« Quelle est la prochaine étape, alors ? »", "standard"),
    ], corrige=True,
       notes="Faire dire les deux versions à voix haute. Les élèves entendent la "
             "différence bien avant de savoir la nommer.")

    d.piege('Registre',
            "« Je vous remercie de votre attention, faque on se rappelle. »",
            "« Je vous remercie de votre attention. »",
            "Le mélange de deux variétés dans la même phrase s'entend "
            "beaucoup plus qu'une phrase entièrement familière. Choisissez "
            "la variété, puis tenez-la jusqu'au point final.",
            notes="Point de la séance. Cette phrase-là revient chaque année dans les "
                  "exposés : la fin d'une présentation soignée qui retombe d'un cran "
                  "parce que l'élève se détend.")

    d.pratique('Production', "Passez au standard",
               "Réécrivez chaque phrase pour une rencontre d'équipe.", [
        ("« Y'a rien là. »", "Ce n'est pas un problème."),
        ("« On se voit-tu samedi matin ? »", "Est-ce qu'on se voit samedi matin ?"),
        ("« C'est correct pour moi. »", "Cela me convient."),
        ("« Faque, on garde-tu ça ? »", "Est-ce qu'on garde cette phrase ?"),
        ("« Il est ben fin, le monsieur. »", "Il est très aimable."),
    ], corrige=True,
       notes="Exercice écrit puis oral. Insister : on ne corrige pas une faute, on "
             "change d'endroit. Les phrases de gauche sont bonnes à la pause.")

    d.regle("Trois variétés, une question",
            "Où suis-je, et à qui je parle ? Avec des camarades, familier. "
            "En équipe et en classe, standard. Devant un groupe, standard "
            "soigné avec vouvoiement.",
            precision="Et jamais deux variétés dans la même phrase. Le familier "
                      "n'est pas interdit : il est situé. Le danger n'est pas de "
                      "l'employer, c'est de ne pas savoir qu'on l'emploie.",
            notes="Diapositive à photographier. C'est la règle que l'élève emporte, "
                  "et elle vaut bien au-delà du module.")

    d.billet(
        "Écrivez une phrase familière que vous entendez souvent, et sa version standard.",
        exemples=[
            "Une phrase entendue au travail ou dans l'autobus.",
            "Les deux versions, l'une sous l'autre.",
        ],
        notes="Billet de sortie. Les réponses font un excellent début de séance B1 : "
              "en lire trois à voix haute avant de commencer.")

    return d.save(dossier)
