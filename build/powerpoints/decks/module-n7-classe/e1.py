# -*- coding: utf-8 -*-
"""E1 · Animer, puis présenter
Bloc E « Je me lance » · couleur teal · jeu de rôle et production orale · 75 min.
Source : section `appli` (jeu de rôle et production orale).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Animer, puis présenter",
        chapeau="Deux prises de parole dans la même séance : conduire une "
                "rencontre où quelqu'un n'est pas d'accord, puis présenter "
                "son sujet devant la classe. La première est la répétition "
                "de la seconde.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Redistribuer les six phrases d'animation de "
                  "D1 et l'annonce de plan écrite en B2 : les deux productions "
                  "s'appuient dessus.")

    d.objectifs([
        "conduire une rencontre d'équipe du début à la fin ;",
        "faire préciser et reformuler au lieu de trancher ;",
        "présenter un sujet concret en trois ou quatre minutes ;",
        "rapporter, dans l'exposé, ce que l'équipe a dit.",
    ], notes="Le quatrième objectif est ce qui distingue cet exposé d'un exposé "
             "ordinaire : on n'y présente pas seulement un contenu, on y rend compte "
             "d'un travail collectif.")

    d.declencheur(
        'Préparation', "Ce que fait celui qui anime, en trois minutes",
        pistes=[
            "Il ouvre en rappelant la question et le temps.",
            "Il donne la parole en nommant la personne.",
            "Il fait préciser : combien, où, comment le sais-tu ?",
            "Il ferme en énumérant les décisions.",
        ],
        notes="Relire les six gestes avant de commencer. Chronométrer les jeux de "
              "rôle : dix minutes chacun, pas plus, sinon la moitié de la classe ne "
              "passera pas.")

    d.tableau('Analyse', "Trois situations de jeu de rôle",
              ['La situation', 'Ce qui est difficile'],
              [["Le désaccord",
                "personne n'a tort, et il faut sortir avec une méthode"],
               ["La part non faite",
                "obtenir le travail sans perdre la personne"],
               ["Celui qui ne dit rien",
                "obtenir son avis sans le mettre mal à l'aise"]],
              cle=0,
              note="Le module fait jouer l'assistant ; en classe, on joue à deux.",
              notes="Diapositive à photographier. La deuxième situation est celle que "
                    "les élèves redoutent le plus, et celle qui leur servira le plus "
                    "au travail.")

    d.pratique('Jeu de rôle', "Animez, dix minutes",
               "À deux : l'un anime, l'autre joue le coéquipier.", [
        ("Ouvrir", "la question, le temps, ce qu'on doit décider"),
        ("Donner la parole", "en nommant la personne"),
        ("Faire préciser", "une question factuelle, jamais un jugement"),
        ("Reformuler", "jusqu'à ce que l'autre dise « c'est ça »"),
        ("Accorder puis maintenir", "bien que… ou même si…"),
        ("Fermer", "les décisions, avec un nom et une date"),
    ], corrige=False,
       notes="Faire inverser les rôles à mi-temps. Celui qui joue le coéquipier "
             "apprend autant : il découvre ce que ça fait d'être reformulé.")

    d.tableau('Analyse', "L'exposé, en quatre temps",
              ['Le temps', 'Ce qu\'on dit'],
              [["Le plan",
                "avant de commencer, je vous dis où je m'en vais"],
               ["Les trouvailles",
                "ce qu'on a trouvé, avec les sources et les conditionnels"],
               ["Le travail d'équipe",
                "ce que les coéquipiers ont dit, rapporté au passé"],
               ["La conclusion",
                "en somme, et une mise en relief de l'essentiel"]],
              cle=0,
              note="Trois ou quatre minutes. Debout, sans lire ses notes mot à mot.",
              notes="Diapositive à photographier. Le troisième temps est la marque de "
                    "ce module : un exposé qui rapporte le travail des autres, pas "
                    "seulement le sien.")

    d.piege('Oral',
            "« Euh, alors, moi j'ai trouvé que… genre, il y a des arbres. »",
            "« Je vais parler d'abord de ce que nous cherchions. »",
            "Un exposé se prépare par sa première phrase. Celle-là décide "
            "de tout le reste : si elle annonce un plan, l'auditoire suit ; "
            "si elle cherche ses mots, il décroche avant la deuxième.",
            notes="Point de méthode. Faire écrire et apprendre par cœur la seule "
                  "première phrase : le reste vient tout seul.")

    d.pratique('Production orale', "Votre exposé",
               "Trois ou quatre minutes, debout, devant la classe.", [
        ("Temps 1", "l'annonce du plan, en une phrase"),
        ("Temps 2", "ce que vous avez trouvé, avec vos sources"),
        ("Temps 3", "ce que votre équipe a dit, au discours rapporté"),
        ("Temps 4", "en somme, et ce qui compte le plus"),
        ("Pendant que vous parlez", "les autres notent une question chacun"),
    ], corrige=False,
       notes="Le module enregistre, corrige et permet de déposer. En classe, faire "
             "poser deux questions après chaque exposé : celui qui répond travaille "
             "encore, et les auditeurs écoutent mieux.")

    d.billet(
        "Notez une chose que vous avez bien faite en parlant, et une à reprendre.",
        exemples=[
            "Une phrase pour chacune.",
            "Parlez de vous, pas des autres.",
        ],
        notes="Billet de sortie. Les réponses valent d'être relues avant E2 : ceux "
              "qui n'ont trouvé aucune réussite en ont pourtant eu une, et il vaut "
              "la peine de la leur nommer.")

    return d.save(dossier)
