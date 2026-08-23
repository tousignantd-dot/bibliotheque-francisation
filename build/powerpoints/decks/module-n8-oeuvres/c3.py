# -*- coding: utf-8 -*-
"""C3 · « Déneigement » — vingt-deux vers, un mot
Bloc C « Défi 2 · Ce qui n'est pas écrit » · couleur teal · 75 min.
Source : exercices `t2poeme` (type `texte`) et `t2img`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n8-oeuvres' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='C3', section='teal',
        titre="« Déneigement » : vingt-deux vers, un mot",
        chapeau="Vingt et un vers parlent de neige, de gratte et de doigts "
                "froids. Le dernier change ce que sont les vingt et un "
                "autres. Rien n'était caché : l'information n'était pas là.",
        duree='75 minutes')

    d.titre(notes="Séance de lecture de poésie, et la seule du programme. Beaucoup "
                  "d'adultes en ont peur ; annoncer d'entrée qu'il n'y a rien à "
                  "décoder et aucune bonne réponse cachée.")

    d.objectifs([
        "compter les strophes avant de lire, et savoir ce qu'elles annoncent ;",
        "relire un poème court à partir de son dernier vers ;",
        "distinguer une comparaison d'une métaphore ;",
        "chercher ce qui se répète, et ce que la répétition protège.",
    ], notes="Le deuxième objectif est mécanique et il suffit presque à lui seul : un "
             "poème court est écrit pour la deuxième lecture.")

    d.declencheur(
        'Observation', "Que fait cette personne, et depuis combien de temps ?",
        image=IMG + 'pare-brise-givre.jpg',
        pistes=[
            "Quelle moitié est dégagée ? Laquelle ne l'est pas ?",
            "De quel côté de l'auto est-ce, vu de l'intérieur ?",
            "Combien de temps faut-il pour dégager une moitié de pare-brise ?",
            "Et si quelqu'un continuait plus longtemps qu'il ne faut ?",
        ],
        notes="La deuxième piste est celle qui porte : c'est le côté du passager. La "
              "quatrième prépare le dernier vers sans le donner.")

    d.tableau('Analyse', "Trois strophes, trois moments",
              ['La strophe', 'Ce qu\'elle contient'],
              [["Première", "le geste, ce matin-là, et « comme on m'a montré »"],
               ["Deuxième", "les règles, et personne ne les a écrites"],
               ["Troisième", "le moteur qui tourne, et le dernier vers"]],
              cle=0,
              note="Trois strophes annoncent presque toujours une mise en place, un développement, un retournement.",
              notes="Diapositive à photographier. Faire compter les strophes avant "
                    "toute lecture : c'est un geste de lecteur, pas de spécialiste.")

    d.regle("Le dernier vers relit tous les autres",
            "« Je déneige quelqu'un qui n'est plus là. »",
            precision="Après ce vers, chaque vers d'avant change d'objet. « La "
                      "banquette de droite est chaude pour rien » devient la place "
                      "vide du passager ; « comme on m'a montré » devient une "
                      "présence. Le lecteur n'a rien manqué à la première lecture : "
                      "l'information n'était pas encore donnée.",
            notes="Diapositive à photographier. Insister sur la dernière phrase : le "
                  "groupe se sent souvent fautif d'avoir « raté » quelque chose. Il "
                  "n'a rien raté.")

    d.cartes('Analyse', "Le vers, et ce qu'il devient", [
        ("« comme on m'a montré »", "quelqu'un a montré, et n'est plus là"),
        ("« personne n'a jamais écrit ces règles »", "elles viennent d'une personne"),
        ("« à voix basse, dans le froid »", "une récitation, presque une prière"),
        ("« la banquette de droite est chaude pour rien »", "la place vide du passager"),
        ("« plus longtemps qu'il ne faut »", "on fait durer, exprès"),
        ("« le côté droit, toujours le côté droit »", "une habitude prise à deux"),
    ], notes="Faire lire la colonne de gauche seule, d'abord. Puis la colonne de "
             "droite. Le groupe entend le poème changer sans qu'un mot ait bougé.")

    d.regle("Une comparaison se dit, une métaphore remplace",
            "« Le bruit d'une allumette qui rate » compare, et le dit. "
            "« Je déneige quelqu'un » ne compare pas.",
            precision="Dans la métaphore, le mot reste le même et ce qu'il désigne a "
                      "changé. « Déneiger quelqu'un » n'a aucun sens littéral, et "
                      "c'est exactement ce qui le rend juste : le geste continue sans "
                      "son objet.",
            notes="Diapositive à photographier. Ne pas exiger le vocabulaire technique "
                  "au-delà de ces deux mots-là : ils suffisent, et le programme n'en "
                  "demande pas plus.")

    d.piege('Piège', "chercher un message caché",
            "chercher ce qui se répète et ce qui bascule",
            "Un poème n'est pas une énigme à décoder, et il n'y a pas de "
            "spécialiste qui détiendrait la réponse. Il organise des mots pour "
            "produire un effet ; le travail du lecteur est de repérer "
            "l'organisation. Deux prises suffisent : ce qui revient — « toujours "
            "par la droite » — et l'endroit où quelque chose bascule.",
            notes="C'est le piège le plus utile de la séance pour un groupe adulte : "
                  "il désarme la peur de la poésie, qui vient presque toujours d'une "
                  "mauvaise expérience scolaire.")

    d.pratique('Compréhension', "Où est-ce écrit ?",
               "Retrouvez le passage qui répond.", [
        ("Le vers qui change le sens de tous les autres.", "je déneige quelqu'un..."),
        ("Montre que le geste a été appris de quelqu'un.", "comme on m'a montré"),
        ("La comparaison qui décrit le bruit.", "d'une allumette qui rate"),
        ("Ce que le poème dit de l'origine des règles.", "personne ne les a écrites"),
        ("Le détail qui ne se comprend qu'à la relecture.", "la banquette de droite"),
        ("Montre que la personne fait durer le geste.", "plus longtemps qu'il ne faut"),
    ], corrige=True,
       notes="Exercice `t2poeme` du module. À l'écran, l'élève clique dans le poème : "
             "le faire ensuite. Sur papier, faire souligner au crayon.")

    d.pratique('Pratique', "Les lieux des deux textes",
               "Reliez la photo à la phrase.", [
        ("Une cafétéria d'usine vide, éclairée au néon.", "la cafétéria"),
        ("Une table pliante au fond, deux chaises dépareillées.", "la table du fond"),
        ("Un papier blanc plié en quatre, près d'un sac.", "la nappe"),
        ("Des châssis de fenêtres debout sur des chevalets.", "l'atelier"),
        ("Un stationnement avant le jour, les autos sous la neige.", "le stationnement"),
        ("Un pare-brise givré, à moitié gratté.", "le pare-brise"),
    ], corrige=True,
       notes="Exercice `t2img` du module. Les six photos ne montrent aucune œuvre : "
             "seulement les lieux que les deux textes nomment. Le faire remarquer, "
             "c'est une leçon de lecture d'image.")

    d.billet(
        "Trouvez, dans une chanson que vous connaissez, un mot ou un vers qui "
        "change le sens de ce qui précède. Écrivez-le, et dites ce qu'il change.",
        exemples=[
            "Dans n'importe quelle langue : traduisez seulement le vers.",
            "Deux phrases suffisent.",
        ],
        notes="Devoir qui marche très bien : chacun arrive avec une chanson de sa "
              "langue d'origine, et le mécanisme du basculement se révèle universel. "
              "Prévoir dix minutes en C4 pour en entendre trois ou quatre.")

    return d.save(dossier)
