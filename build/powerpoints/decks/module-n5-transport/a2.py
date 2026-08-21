# -*- coding: utf-8 -*-
"""A2 · Le son de « an » et le son de « on »
Bloc A « Je découvre » · couleur indigo · 75 min. Graphie-phonie.
Source : exercice `prPhon` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Le son de « an » et le son de « on »",
        chapeau="Ralentissement, accident, sens, quarante d'un côté ; pont, "
                "bouchon, camion, direction de l'autre. Deux voyelles du nez "
                "portent la moitié des mots du bulletin, et les confondre "
                "fait refaire son trajet pour rien.",
        duree='75 minutes')

    d.titre(notes="Séance de graphie-phonie. Commencer sans explication : dire « le pan » "
                  "puis « le pont », et demander au groupe si c'est le même mot. Une "
                  "partie du groupe dira oui. C'est le point de départ de la séance et "
                  "ce n'est ni une faute ni une surdité : ces deux voyelles n'existent "
                  "pas dans beaucoup de langues.")

    d.objectifs([
        "entendre la différence entre la voyelle de « an » et celle de « on » ;",
        "reconnaître les quatre façons d'écrire le son de « an » ;",
        "prononcer les deux voyelles en surveillant la position des lèvres ;",
        "dire un mot qui contient les deux sons, comme « contournement ».",
    ], notes="Le troisième objectif est le plus concret : la différence est visible sur "
             "les lèvres. Faire travailler devant une vitre ou un téléphone en mode "
             "photo — voir sa propre bouche vaut dix explications.")

    d.regle("Deux sons du nez, deux bouches différentes",
            "Sur « an », la bouche est grande ouverte. Sur « on », les lèvres "
            "se ferment en petit rond.",
            precision="Dans les deux cas, l'air passe par le nez et la lettre n ne "
                      "se prononce pas : elle indique seulement la nasale.",
            notes="Diapositive à photographier. Faire le geste avec la main devant la "
                  "bouche en même temps que le groupe : sur « an » la main sent une "
                  "ouverture large, sur « on » un rond serré.")

    d.tableau('Quatre orthographes', "Le son de « an » s'écrit de quatre façons",
              ['On écrit', 'On lit'],
              [["an", "quarante, dans"],
               ["am", "ambulance, camp"],
               ["en", "lentement, sens"],
               ["em", "embouteillage, temps"]],
              cle=1,
              note="Un seul son pour quatre orthographes.",
              notes="Insister : ce n'est pas l'écriture qui décide, c'est l'oreille. "
                    "Beaucoup d'élèves cherchent quatre prononciations là où il n'y en a "
                    "qu'une, et se fatiguent pour rien.")

    d.cartes("Les paires", "Écoutez la voyelle, pas la consonne", [
        ("lent · long", "Bouche ouverte, puis lèvres en rond."),
        ("sans · son", "Même consonne au départ, deux voyelles."),
        ("banc · bon", "La différence est à la fin du mot."),
        ("le pan · le pont", "La paire qui coûte le plus cher."),
    ], notes="Dire chaque paire deux fois, puis dans le désordre, et faire lever la main "
             "sur « on ». Terminer par « le pan / le pont » : c'est celle qui a des "
             "conséquences réelles un matin de semaine.")

    d.vocabulaire('Les mots du bulletin', "Rangés par voyelle", [
        ("un ralentissement", "le son de « an », deux fois"),
        ("un embouteillage", "le son de « an » au début"),
        ("dans les deux sens", "le son de « an », deux fois"),
        ("un pont", "le son de « on »"),
        ("un bouchon", "le son de « on » à la fin"),
        ("la circulation", "le son de « on » à la fin"),
    ], notes="Faire classer les mots par le groupe avant d'afficher la colonne de droite. "
             "Les six mots reviennent tous dans les exercices de l'activité interactive.")

    d.piege("Prononcer le n ou le m qui suit la voyelle",
            "Un ralentisse-menne, un bouchonne.",
            "Un ralentissement, un bouchon — la langue ne touche rien.",
            "Dans une voyelle nasale, la lettre n ne se prononce pas : elle dit "
            "seulement que l'air passe par le nez. Le n s'entend uniquement quand "
            "une voyelle suit, comme dans « un accident ».",
            notes="Faire tenir la voyelle finale longtemps, sans jamais fermer la bouche "
                  "sur un n. C'est l'erreur la plus tenace, et elle s'entend "
                  "immédiatement dans une production orale.")

    d.pratique('Discrimination', "Quelle voyelle entendez-vous ?",
               "Dites si c'est le son de « an » ou celui de « on ».", [
        ("un ralentissement", "le son de « an »"),
        ("un pont", "le son de « on »"),
        ("un accident", "le son de « an »"),
        ("un bouchon", "le son de « on »"),
        ("dans les deux sens", "le son de « an »"),
        ("la circulation", "le son de « on »"),
        ("quarante minutes", "le son de « an »"),
        ("un camion", "le son de « on »"),
    ], corrige=True,
       notes="Dire les mots sans les montrer, une fois chacun, à débit normal. Puis "
             "recommencer plus lentement pour ceux qui hésitent. Les huit mêmes items "
             "sont dans l'exercice interactif, avec l'audio.")

    d.regle("Le mot qui contient les deux",
            "En direction de. Un contournement.",
            precision="« An » d'abord, « on » ensuite. Dites-les une syllabe à la "
                      "fois jusqu'à ce que les deux sons soient nets.",
            notes="Terminer la séance là-dessus : c'est l'exercice le plus utile du "
                  "module, et « en direction de » revient dix fois par bulletin.")

    d.billet(
        "Écrivez deux mots de votre journée : un avec le son de « an », un avec le son de « on ».",
        exemples=[
            "Ils n'ont pas besoin de venir de la route : maman, salon, enfant, maison.",
            "Dites-les à voix basse en surveillant vos lèvres avant d'écrire.",
        ],
        notes="Ramasser les billets et relire quelques paires à voix haute au début de "
              "la séance A3. Les erreurs de classement disent exactement qui a besoin "
              "d'un retour individuel.")

    return d.save(dossier)
