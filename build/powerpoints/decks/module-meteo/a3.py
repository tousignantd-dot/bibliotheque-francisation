# -*- coding: utf-8 -*-
"""A3 · Le vocabulaire de l'hiver québécois.
Bloc A · couleur framboise (vocabulaire) · 60 min.
Source : cartes mémoire et exercice `prImg`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/assets/'
       'interactive/module-meteo/images/')


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Le vocabulaire de l'hiver",
        chapeau="Poudrerie, grésil, redoux, facteur éolien. Quatre mots qu'aucune "
                "méthode de français ne contient, et qu'on entend tous les matins de "
                "janvier à la radio.",
        duree='60 minutes')

    d.titre(notes="Séance de vocabulaire pur. Beaucoup d'élèves connaissent le phénomène "
                  "sans connaître le mot français. Partir de ce qu'ils voient.")

    d.objectifs([
        "nommer les six formes de précipitations de l'hiver ;",
        "distinguer la poudrerie de la neige qui tombe ;",
        "comprendre le facteur éolien et pourquoi il compte ;",
        "reconnaître le temps qu'il fait à partir d'une description.",
    ])

    d.declencheur(
        'Mise en situation', "Que voyez-vous, et comment ça s'appelle en français ?",
        image=IMG + 'poudrerie.jpg',
        pistes=[
            "Est-ce qu'il neige sur cette photo ?",
            "D'où vient la neige qu'on voit dans l'air ?",
            "Est-ce qu'on peut conduire là-dedans ?",
            "Comment ça s'appelle, dans votre langue ?",
        ],
        notes="Trois minutes. La deuxième question donne la réponse : la neige ne tombe "
              "pas, elle est soulevée. C'est la définition de la poudrerie.")

    d.tableau('Analyse', "Six formes de précipitations",
              ['Le mot', 'Ce que c\'est'],
              [["la neige", "des flocons qui tombent du ciel"],
               ["la poudrerie", "de la neige déjà tombée que le vent soulève"],
               ["le grésil", "de petits grains de glace qui tombent"],
               ["la pluie verglaçante", "une pluie qui gèle en touchant une surface"],
               ["la grêle", "des billes de glace, surtout en été"],
               ["le verglas", "la couche de glace qui reste sur les surfaces"]],
              cle=0, props=[0.32, 0.68],
              notes="Faire distinguer les deux derniers : la pluie verglaçante tombe, le "
                    "verglas est ce qu'elle laisse. C'est la confusion la plus fréquente.")

    d.regle('La distinction la plus utile',
            "La neige tombe. La poudrerie est soulevée.",
            precision="Il peut y avoir de la poudrerie sans qu'un seul flocon tombe : il "
                      "suffit de vent et de neige au sol. C'est pour ça qu'une journée "
                      "ensoleillée peut avoir une visibilité nulle sur l'autoroute.",
            notes="Diapo centrale de la séance. Cette distinction est essentielle pour "
                  "comprendre les avertissements routiers du défi 2.")

    d.cartes('Analyse', "Quatre mots qui décrivent la journée", [
        ("Un redoux",
         "Un réchauffement court au milieu de l'hiver. La neige fond, l'eau coule, puis "
         "elle regèle la nuit : c'est ce qui fabrique le verglas au sol."),
        ("Une éclaircie",
         "Un moment où les nuages s'ouvrent. Ce n'est pas la fin de la tempête, c'est "
         "une pause."),
        ("Le facteur éolien",
         "L'effet du vent sur le froid ressenti. Moins quinze avec du vent peut se "
         "ressentir comme moins vingt-huit : la peau gèle plus vite."),
        ("Le mercure",
         "Une autre façon de dire la température. « Le mercure descendra à moins six » "
         "veut dire « il fera moins six »."),
    ], notes="Le facteur éolien n'est pas une curiosité : c'est ce qui décide du temps "
             "d'exposition sécuritaire au travail. Le dire.")

    d.pratique('Pratique · 1 de 4', "Reconnaissez le temps qu'il fait",
               "D'après la description.", [
        ("Le vent soulève la neige et efface les lignes de la route.", "la poudrerie"),
        ("La pluie a gelé sur les branches et l'escalier.", "la pluie verglaçante"),
        ("La neige fond et l'eau coule dans le stationnement.", "un redoux"),
        ("Le ciel s'ouvre entre les nuages et le soleil revient.", "une éclaircie"),
        ("De petits grains de glace frappent les fenêtres.", "le grésil"),
    ], corrige=True,
       notes="Faire l'exercice avec les images du module. Cette diapo sert de correction "
             "et de trace écrite.")

    d.pratique('Pratique · 2 de 4', "Neige ou poudrerie ?",
               "Est-ce que ça tombe, ou est-ce que c'est soulevé ?", [
        ("Il fait soleil, mais on ne voit pas la route.", "poudrerie"),
        ("Deux à quatre centimètres sont attendus ce soir.", "neige"),
        ("Le vent du nord-est réduit la visibilité.", "poudrerie"),
        ("Les flocons tombent depuis le matin.", "neige"),
        ("Les chasse-neige circulent, mais la route se recouvre aussitôt.", "poudrerie"),
    ], corrige=True,
       notes="Le premier item est le plus révélateur : soleil et visibilité nulle en "
             "même temps. C'est propre à la poudrerie.")

    d.piege("Le piège de la journée ensoleillée",
            "Il fait beau, donc la route est bonne.",
            "Il peut faire soleil et y avoir de la poudrerie.",
            "La poudrerie n'a besoin que de vent et de neige au sol. Un ciel parfaitement "
            "dégagé n'empêche rien. C'est pour cela qu'on consulte les avertissements "
            "routiers avant de partir, même par beau temps.",
            notes="Point pratique important pour ceux qui conduisent. Le relier au "
                  "dialogue du défi 2.")

    d.piege("Le piège du facteur éolien",
            "Il fait moins quinze, ça va, je sors sans tuque.",
            "Avec le vent, ça se ressent comme moins vingt-huit.",
            "La température seule ne dit pas le risque. Le facteur éolien peut doubler la "
            "sensation de froid et faire geler la peau exposée en quelques minutes. Les "
            "bulletins le donnent toujours : il faut l'écouter.",
            notes="Donner le repère pratique : sous moins vingt-sept ressenti, la peau "
                  "exposée gèle en une trentaine de minutes.")

    d.pratique('Pratique · 3 de 4', "Expliquez le mot",
               "Dans vos propres mots, sans employer le mot lui-même.", [
        ("la poudrerie", "de la neige déjà tombée que le vent soulève"),
        ("un redoux", "un réchauffement court au milieu de l'hiver"),
        ("le facteur éolien", "l'effet du vent, qui fait ressentir un froid plus intense"),
        ("la chaussée", "la partie de la route où roulent les véhicules"),
        ("une éclaircie", "un moment où les nuages s'ouvrent"),
    ], corrige=True,
       notes="C'est l'exercice de reformulation du module 5, appliqué ici. Le signaler à "
             "ceux qui l'ont fait.")

    d.pratique('Pratique · 4 de 4', "Décrivez la journée",
               "Trois phrases avec trois mots différents du module.", [
        ("Ce matin", "Il y a de la poudrerie et la visibilité est mauvaise."),
        ("Cet après-midi", "Une éclaircie est prévue, mais le facteur éolien restera fort."),
        ("Ce soir", "Le mercure descendra et la chaussée deviendra glissante."),
    ], corrige=True,
       notes="Faire écrire trois phrases sur la vraie météo du jour. C'est plus motivant "
             "et cela ancre le vocabulaire.")

    d.billet(
        "Décrivez la météo d'aujourd'hui en trois phrases.",
        exemples=[
            "Employez au moins trois mots du module.",
            "Une phrase pour le ciel, une pour le vent, une pour la température.",
        ],
        notes="Ramasser. Ces descriptions serviront en E1, où chacun écrira un vrai "
              "bulletin météo.")

    return d.save(dossier)
