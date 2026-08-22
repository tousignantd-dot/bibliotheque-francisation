# -*- coding: utf-8 -*-
"""B2 · « Ce qui bouge : le passé composé »
Bloc B « Défi 1 · Ce qui est arrivé » · couleur acier · 75 min.
Source : exercice `t1pc`, mini-leçon `t1pc`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='acier',
        titre="Ce qui bouge : le passé composé",
        chapeau="Le feu a commencé. Un locataire s'est réveillé. Il a cogné "
                "à toutes les portes. Les pompiers sont arrivés. Quatre "
                "verbes, quatre moments qui se suivent — c'est le temps du "
                "récit, et c'est celui qu'un fait divers emploie le plus.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, mais elle est au service du récit de B1. "
                  "Ouvrir en relisant les quatre phrases du chapeau à voix haute et "
                  "en demandant ce qu'elles ont en commun. La réponse — elles se "
                  "suivent — vaut mieux que « elles sont au passé composé ».")

    d.objectifs([
        "former le passé composé avec le bon auxiliaire ;",
        "accorder le participe passé après « être » ;",
        "employer les participes que le fait divers emploie tous les jours ;",
        "placer la négation autour de l'auxiliaire.",
    ], notes="Le quatrième objectif est le plus vite acquis et le plus vite perdu. Le "
             "traiter en fin de séance, avec « personne n'a été blessé » : c'est la "
             "phrase que tout fait divers d'incendie contient.")

    d.regle("Deux morceaux : l'auxiliaire, puis le participe",
            "Un verbe conjugué au présent — avoir ou être — et le "
            "participe passé juste après.",
            precision="Le feu a détruit l'immeuble. Les pompiers sont arrivés. Le "
                      "sens est dans le deuxième morceau, la grammaire dans le "
                      "premier : c'est l'auxiliaire qui porte la personne, le temps "
                      "et la négation.",
            notes="Diapositive à photographier. Le mot « morceau » est volontaire : "
                  "il rend visible que la faute la plus fréquente — oublier "
                  "l'auxiliaire — est un morceau manquant, pas une subtilité.")

    d.tableau('Le bon auxiliaire', "Qui prend avoir, qui prend être",
              ['Auxiliaire', 'Les verbes du fait divers'],
              [["avoir", "détruire, brûler, commencer, appeler, voir, perdre, dire"],
               ["", "La Croix-Rouge a hébergé les sinistrés."],
               ["être", "aller, venir, arriver, partir, entrer, sortir, rester, tomber"],
               ["", "Les pompiers sont arrivés. Une résidente est sortie."],
               ["être aussi", "tous les verbes en se : un locataire s'est réveillé."]],
              cle=0,
              notes="Faire dire les deux exemples à voix haute avant d'expliquer "
                    "l'accord. Insister : la liste de « être » est courte et se "
                    "retient ; « avoir » est le cas normal, pas l'exception.")

    d.regle("Avec être, le participe s'accorde avec le sujet",
            "Les pompiers sont arrivés. Une résidente est sortie. "
            "Onze personnes ont perdu leur logement.",
            precision="Avec être, on ajoute un s au pluriel et un e au féminin : "
                      "arrivés, sortie, sorties. Avec avoir, le participe ne bouge "
                      "pas quand le complément suit le verbe — et dans un fait "
                      "divers, il suit presque toujours.",
            notes="Ne pas ouvrir la règle de l'accord du complément placé avant : "
                  "elle ne sert à rien au niveau 5 et elle brouille tout. S'en tenir "
                  "à « avec être, on accorde ; avec avoir, on ne touche à rien ».")

    d.cartes("Les participes du métier", "Ceux qu'un fait divers emploie tous les jours", [
        ("Le sinistre",
         "détruit · brûlé · éclaté · évacué · inondé · perdu"),
        ("Les secours",
         "appelé · arrivé · hébergé · relogé · pompé"),
        ("Le délit",
         "volé · retrouvé · arrêté · signalé · entré"),
        ("Le conseil",
         "Apprenez-les comme des mots, pas comme des règles."),
    ], notes="La quatrième carte est le conseil de la séance. Un participe irrégulier "
             "s'apprend par l'usage : le faire répéter dans une phrase courte, jamais "
             "seul.")

    d.pratique('Écriture', "Mettez le verbe au passé composé",
               "Attention à l'auxiliaire et à l'accord.", [
        ("Le feu ___ (éclater) vers quatre heures du matin.", "a éclaté"),
        ("Les pompiers ___ (arriver) huit minutes après l'appel.", "sont arrivés"),
        ("Un locataire ___ (se réveiller) et il a cogné aux portes.", "s'est réveillé"),
        ("Personne ___ (ne pas être) blessé.", "n'a pas été"),
        ("Onze personnes ___ (perdre) leur logement.", "ont perdu"),
        ("La Croix-Rouge ___ (héberger) les sinistrés.", "a hébergé"),
    ], corrige=True,
       notes="Exercice t1pc de l'activité interactive. Faire dire chaque phrase à "
             "voix haute avant de l'écrire : l'oreille attrape « sont arrivés » plus "
             "vite que la règle.")

    d.regle("La négation entoure l'auxiliaire, jamais le participe",
            "Personne n'a été blessé. Le feu n'a pas touché l'immeuble "
            "d'à côté. La Ville n'a pas voulu dire quand.",
            precision="Le ne et le pas se placent autour du premier morceau. "
                      "« Il n'a pas dormi », jamais « il a ne pas dormi ». La règle "
                      "est simple parce que l'auxiliaire est toujours au même "
                      "endroit.",
            notes="Faire produire trois négations à l'oral avec les verbes de la "
                  "séance. « Personne n'a été blessé » mérite d'être apprise telle "
                  "quelle : c'est une phrase entière de fait divers.")

    d.piege("Oublier l'auxiliaire",
            "Les pompiers arrivés huit minutes après.",
            "Les pompiers sont arrivés huit minutes après.",
            "Le participe seul ne conjugue rien : il n'a ni personne ni temps. Sans "
            "auxiliaire, la phrase n'est pas au passé — elle n'est nulle part.",
            notes="Faute très fréquente chez les élèves dont la langue première "
                  "n'emploie pas d'auxiliaire. Ne pas la traiter comme de la "
                  "distraction : c'est une structure absente, il faut la construire.")

    d.piege("Prendre « avoir » pour un verbe de mouvement",
            "Les pompiers ont arrivés.",
            "Les pompiers sont arrivés.",
            "aller, venir, arriver, partir, entrer, sortir, monter, descendre, "
            "rester, tomber : ces dix-là prennent être, et le participe s'accorde. "
            "Ce sont exactement les verbes qui font bouger un récit.",
            notes="Faire écrire les dix verbes au tableau et les laisser pendant les "
                  "exercices. Une liste visible vaut mieux qu'une liste récitée.")

    d.billet(
        "Écrivez trois évènements de l'incendie, au passé composé, dans l'ordre.",
        exemples=[
            "Trois phrases, chacune sur une ligne, chacune avec son auxiliaire.",
            "Vérifiez l'accord de celles qui prennent « être ».",
        ],
        notes="Ramasser. Les trois phrases serviront directement à l'exercice t1red "
              "de la séance B4 : le prévenir, ça motive le soin.")

    return d.save(dossier)
