# -*- coding: utf-8 -*-
"""A3 · Il neige, il pleut, il fait froid.
Bloc A « Je découvre » · couleur teal · 75 min.
Source : exercices `prIl` et `prImg`, mini-leçon « Le il de la météo ».

Le savoir du programme s'appelle la phrase impersonnelle, et le niveau 2 n'en
compte qu'un point. Il tombe pile sur la météo : c'est même le seul endroit
de la vie courante où un élève débutant en rencontre à tous les jours.

Trois formes, et l'hiver devient dicible : un verbe seul (il neige), « il
fait » plus un mot (il fait froid), « il y a » plus une chose (il y a des
nuages). La séance les sépare, puis les fait choisir devant six photos.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-neige/images/')


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre="Il neige, il pleut, il fait froid",
        chapeau="Trois façons de dire le temps qu'il fait, toutes avec « il ».",
        duree='75 minutes')

    d.titre(notes="Troisième séance. Écrire au tableau « ___ neige » et demander ce "
                  "qui manque. Personne ne propose « il » spontanément : c'est ce qui "
                  "rend la séance nécessaire.")

    d.objectifs([
        "employer « il » devant un verbe de météo ;",
        "dire « il fait froid », « il fait beau » ;",
        "dire « il y a du soleil », « il y a des nuages » ;",
        "choisir la bonne forme devant une photo.",
    ])

    d.regle("Ce « il » ne remplace personne.",
            "Il neige. Il pleut. Il vente.",
            precision="Ce n'est ni un homme, ni le ciel, ni le temps. C'est un mot "
                      "obligatoire, et il ne change jamais. On ne dit pas « la neige "
                      "neige », ni « ça fait froid ».",
            notes="Diapositive à photographier. Ne pas employer le mot « impersonnel » "
                  "devant le groupe : dire « un il qui n'est personne ». Le mot savant "
                  "ne sert à rien ici.")

    d.tableau('Analyse', "Trois formes, trois emplois",
              ["La forme", "Quand on l'emploie"],
              [["Il neige.", "un verbe suffit : neiger, pleuvoir, venter"],
               ["Il fait froid.", "« il fait » + un mot : froid, chaud, beau, mauvais"],
               ["Il y a du soleil.", "« il y a » + une chose : du soleil, des nuages"],
               ["Il fait moins huit.", "« il fait » sert aussi pour la température"]],
              cle=1,
              note="Trois formes, et toute la météo du niveau 2 est couverte.",
              notes="Diapositive à photographier. Faire classer à l'oral dix phrases "
                    "dites au hasard avant de passer à l'exercice écrit.")

    d.declencheur(
        'Observation', "Quel temps fait-il sur cette photo ?",
        image=IMG + 'temps-vent.jpg',
        pistes=[
            "Qu'est-ce qui bouge sur la photo ?",
            "Est-ce qu'on voit le vent ? Comment on le sait ?",
            "Est-ce qu'il fait froid ou chaud ?",
            "Quelle phrase dit ce qu'on voit : il vente, ou il y a du vent ?",
        ],
        notes="La quatrième piste est la vraie question : les deux se disent. Le dire "
              "clairement évite qu'un élève croie qu'il s'est trompé.")

    d.vocabulaire('Vocabulaire', "Ce qu'il y a dans le ciel", [
        ("un nuage", "La forme grise ou blanche qui cache le ciel."),
        ("la température", "Le nombre qui dit s'il fait froid ou chaud."),
        ("il fait beau", "Il y a du soleil et il ne pleut pas."),
        ("il fait mauvais", "Il pleut, ou il vente, ou les deux."),
    ], notes="Diapositive à photographier. « Il fait beau » et « il fait mauvais » "
             "s'apprennent ensemble : ce sont deux blocs, pas quatre mots.")

    d.pratique('Pratique · le bon mot', "Complétez la phrase",
               "Un seul mot par trou.", [
        ("___ neige depuis la nuit.", "Il"),
        ("Il ___ froid ce matin.", "fait"),
        ("Il ___ : prends ton parapluie.", "pleut"),
        ("Il y ___ beaucoup de nuages.", "a"),
        ("Il ___ fort. Mets ta tuque.", "vente"),
        ("Demain, il ___ beau.", "fait"),
    ], corrige=True, cols=2,
       notes="À faire d'abord à l'oral, en groupe, puis à l'écrit. Le quatrième est le "
             "plus raté : le « y » de « il y a » s'entend à peine.")

    d.pratique('Pratique · six photos', "Quelle phrase va avec quelle photo ?",
               "Ouvrez l'activité, exercice 3 de « Je découvre ».", [
        ("Il neige.", "les toits sont blancs"),
        ("Il pleut.", "les gens ouvrent leur parapluie"),
        ("Il fait soleil.", "le ciel est bleu, sans nuage"),
        ("Il vente.", "les arbres bougent beaucoup"),
        ("Il fait froid.", "le thermomètre est sous zéro"),
        ("Il y a de la glace.", "le trottoir est glissant"),
    ], cols=2,
       notes="Faire l'exercice sur l'appareil, pas au tableau : les photos sont dans "
             "l'activité. Passer dans les rangées pendant ce temps.")

    d.pratique('Pratique · à la fenêtre', "Trois par trois, debout",
               "Quinze minutes. Chacun dit trois phrases sur le temps du jour.", [
        ("Phrase 1", "avec un verbe seul : il neige, il pleut, il vente"),
        ("Phrase 2", "avec « il fait » : il fait froid, il fait beau"),
        ("Phrase 3", "avec « il y a » : il y a du soleil, des nuages"),
    ], cols=1,
       notes="Exiger les trois formes de chacun. C'est la seule façon de vérifier que "
             "la troisième, la moins naturelle, est vraiment acquise.")

    d.billet(
        "Écrivez trois phrases sur le temps qu'il fait aujourd'hui, une de chaque forme.",
        exemples=[
            "Il neige.",
            "Il fait moins huit degrés.",
            "Il y a beaucoup de nuages.",
        ],
        notes="Devoir court. Corriger surtout le « il » manquant et le « y » oublié : "
              "ce sont les deux erreurs qui restent longtemps.")

    return d.save(dossier)
