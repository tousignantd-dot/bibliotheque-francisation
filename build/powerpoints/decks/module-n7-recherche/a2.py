# -*- coding: utf-8 -*-
"""A2 · Le « e » qu'on avale
Bloc A « Je découvre » · couleur indigo · graphie-phonie · 75 min.
Source : exercice `prE`, mini-leçon `prE`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Le « e » qu'on avale",
        chapeau="Vous allez téléphoner à des employeurs. Le mot que vous "
                "connaissez très bien devient méconnaissable quand un « e » "
                "tombe — et vous croyez avoir manqué du vocabulaire.",
        duree='75 minutes')

    d.titre(notes="Séance de prononciation, mais son enjeu est l'écoute. Le dire dès "
                  "le début : on travaille ici pour comprendre au téléphone, pas pour "
                  "bien parler.")

    d.objectifs([
        "entendre le « e » intérieur d'un mot, ou son absence ;",
        "savoir dans quels cas il se maintient ;",
        "reconnaître un mot connu sous sa forme courte ;",
        "prononcer les deux formes sans crainte de se tromper.",
    ], notes="Le quatrième objectif est un objectif de tranquillité : garder un « e » "
             "qui aurait pu tomber ne provoque aucun malentendu. Le dire tôt.")

    d.declencheur(
        'Écoute', "Combien de syllabes entendez-vous ?",
        pistes=[
            "« rapidement » : quatre morceaux, ou trois ?",
            "« la semaine » : trois, ou deux ?",
            "Écrivez ce que vous entendez avant de regarder le mot.",
            "Est-ce que la personne parle mal ?",
        ],
        notes="Faire écrire avant de montrer. La surprise est utile : plusieurs "
              "élèves écrivent « rapidment » et croient s'être trompés. Ils ont "
              "parfaitement entendu.")

    d.regle("Deux prononciations, toutes deux correctes",
            "Ce « e » n'est pas avalé par négligence. Sa place dans le mot "
            "décide s'il se dit ou s'il tombe.",
            precision="On l'appelle le « e caduc » — caduc veut dire « qui tombe ». "
                      "Un journaliste, une conseillère et un employeur le font tomber "
                      "aux mêmes endroits, sans y penser. Ce n'est pas du français "
                      "relâché : c'est le français normal.",
            notes="Diapositive à photographier. Anticiper l'objection : « mais on "
                  "m'a appris à tout prononcer ». On n'a rien appris de faux ; on a "
                  "appris la forme lente.")

    d.tableau('Analyse', "Trois cas où le « e » se maintient",
              ['Le cas', 'Les mots'],
              [["Début de mot, après p, b, t, d, k, g",
                "demander · peser · debout · un devis"],
               ["Devant les sons « ri » et « li »",
                "un atelier · un hôtelier"],
               ["Quand deux consonnes le précèdent",
                "le premier · autrement · appartement"],
               ["Partout ailleurs, au milieu : il tombe",
                "rapidement · seulement · la semaine · un médecin"]],
              cle=0,
              note="Une seule consonne devant, au milieu du mot : il tombe. C'est le cas le plus fréquent.",
              notes="Diapositive à photographier. C'est le tableau de référence ; le "
                    "faire recopier dans le carnet plutôt que le distribuer.")

    d.cartes('Analyse', "Ce qui est écrit, ce qui se dit", [
        ("demander", "de-man-der — le « e » se dit"),
        ("rapidement", "ra-pid'ment — le « e » tombe"),
        ("peser", "pe-ser — le « e » se dit"),
        ("la relève", "la r'lève — le « e » tombe"),
        ("un atelier", "a-te-lier — le « e » se dit"),
        ("un médecin", "un méd'cin — le « e » tombe"),
    ], notes="Faire dire les deux formes à voix haute, puis seulement la forme courte. "
             "C'est celle-là qu'il faut savoir reconnaître.")

    d.piege('Prononciation',
            "prononcer chaque « e » écrit, un par un",
            "laisser tomber ceux du milieu du mot",
            "« Ra-pi-de-ment » en quatre morceaux se comprend, mais sonne "
            "appliqué et ralentit tout. Personne ne parle comme ça, et "
            "surtout pas au téléphone, où la vitesse est ordinaire.",
            notes="Rassurer aussitôt : cette faute-là ne gêne personne. Le vrai "
                  "problème est l'inverse — ne pas reconnaître le mot amputé.")

    d.pratique('Écoute', "On l'entend, ou il disparaît ?",
               "Écoutez chaque mot et cochez.", [
        ("demander", "on l'entend"),
        ("rapidement", "il disparaît"),
        ("peser", "on l'entend"),
        ("la relève", "il disparaît"),
        ("debout", "on l'entend"),
        ("seulement", "il disparaît"),
        ("un devis", "on l'entend"),
        ("la semaine", "il disparaît"),
        ("un atelier", "on l'entend"),
        ("un médecin", "il disparaît"),
        ("le premier", "on l'entend"),
        ("la boulangerie", "il disparaît"),
    ], corrige=True,
       notes="Les douze mots du module interactif, exercice `prE`. Passer deux fois : "
             "la première pour cocher, la seconde pour répéter la forme courte.")

    d.billet(
        "Écrivez trois mots que vous n'aviez jamais reconnus à l'oral.",
        exemples=[
            "Un mot que vous lisez sans problème mais que vous ne saisissez pas quand on le dit.",
            "Essayez de deviner s'il perd un « e ».",
        ],
        notes="Ramasser les billets : ils donnent la liste de reprise pour la séance "
              "E2, et elle est différente d'un groupe à l'autre.")

    return d.save(dossier)
