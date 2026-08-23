# -*- coding: utf-8 -*-
"""A2 · Le « e » qu'on garde et le « e » qui tombe
Bloc A « Je découvre » · couleur indigo · graphie-phonie · 75 min.
Source : exercice `prSon` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Le « e » qu'on garde et le « e » qui tombe",
        chapeau="Dans « samedi », personne ne le dit. Dans « petit », tout le "
                "monde le dit. Ce n'est pas du désordre : deux règles "
                "décident, et elles s'apprennent en une séance.",
        duree='75 minutes')

    d.titre(notes="Séance de graphie-phonie. Le savoir vient du programme du niveau 7, "
                  "système prosodique : maintenir le e devant les groupes en r plus i "
                  "ou l plus i, et dans une syllabe initiale qui commence par une "
                  "occlusive.")

    d.objectifs([
        "entendre si le « e » du milieu se prononce ou s'il disparaît ;",
        "reconnaître les deux cas où il se garde ;",
        "prononcer les mots du dossier au débit courant ;",
        "savoir que le « e » tombé reste toujours écrit.",
    ], notes="Le quatrième objectif évite une faute d'écriture qui se répand vite : "
             "« la s'maine » ne s'écrit jamais.")

    d.declencheur(
        'Écoute', "Dis « samedi » à voix haute, puis « petit ». Que remarques-tu ?",
        pistes=[
            "Combien de syllabes entends-tu dans chacun ?",
            "Est-ce que le « e » du milieu s'entend dans les deux ?",
            "Essaie « la semaine », puis « demander ».",
            "Lequel des deux est plus facile à dire vite ?",
        ],
        notes="Laisser le groupe chercher deux minutes sans expliquer. Presque tout le "
              "monde entend la différence sans savoir la nommer : c'est le bon point de "
              "départ.")

    d.regle("Règle 1 — le « e » se garde devant r plus i et l plus i",
            "Un atelier, un chandelier, nous serions, vous feriez.",
            precision="Deux consonnes glissées ensemble avec un « i » derrière, c'est "
                      "trop serré pour laisser tomber le « e » avant. La bouche a "
                      "besoin de la petite voyelle pour passer. Dès qu'on voit -lier, "
                      "-rions ou -riez, le « e » reste.",
            notes="Diapositive à photographier. Aucune exception à retenir : c'est la "
                  "plus mécanique des deux règles.")

    d.regle("Règle 2 — le « e » se garde après p, b, t, d, k, g",
            "Petit, debout, tenir, demander, peser, dehors.",
            precision="Ces consonnes-là ferment complètement la bouche, puis l'ouvrent "
                      "d'un coup. Après un tel départ, le français garde le « e » "
                      "plutôt que d'enchaîner deux consonnes. Le programme dit "
                      "« plusieurs des mots » et non « tous » : la règle est forte, "
                      "elle n'est pas absolue.",
            notes="Diapositive à photographier. Faire chercher au groupe d'autres mots "
                  "qui commencent par ces lettres : besoin, tenez, degré, quenouille.")

    d.tableau('Analyse', "Douze groupes de mots, deux colonnes",
              ['On garde le e', 'Le e tombe'],
              [["un petit bruit", "samedi matin"],
               ["un atelier de vélos", "la semaine prochaine"],
               ["tenir un registre", "maintenant"],
               ["nous serions d'accord", "acheter du caoutchouc"],
               ["demander une date", "au revoir, monsieur"],
               ["vous feriez mieux", "la fenêtre de la chambre"]],
              notes="Faire lire la colonne de gauche par une moitié du groupe et celle "
                    "de droite par l'autre, puis échanger. L'oreille apprend plus vite "
                    "que la règle.")

    d.piege('Prononciation',
            "Prononcer tous les « e » pour être plus clair",
            "Les garder seulement dans les deux cas de la règle",
            "Un débit où chaque « e » s'entend sonne récité et ralentit tout. "
            "Paradoxalement, il rend moins clair : l'interlocuteur cherche un mot "
            "là où il n'y en a pas. À l'inverse, avaler le « e » de « demander » "
            "ou de « tenir » rend le mot difficile à reconnaître.",
            notes="Faire dire les deux versions de « demander une date » : d'abord "
                  "avec le « e », puis sans. La seconde est presque incompréhensible.")

    d.pratique('Pratique', "On garde le « e » ou il tombe ?",
               "Écoutez chaque groupe de mots, puis répondez.", [
        ("un petit bruit", "on garde le e - p occlusive en première syllabe"),
        ("samedi matin", "le e tombe"),
        ("un atelier de vélos", "on garde le e - suivi de l plus i"),
        ("la semaine prochaine", "le e tombe"),
        ("nous serions d'accord", "on garde le e - suivi de r plus i"),
        ("maintenant", "le e tombe"),
        ("demander une date", "on garde le e - d occlusive en première syllabe"),
        ("la fenêtre de la chambre", "le e tombe"),
    ], corrige=True,
       notes="Faire répéter chaque groupe après la correction. Ne pas passer à la "
             "suite avant que le groupe entende la différence sur au moins deux paires.")

    d.billet(
        "Écris deux mots du module : un où le « e » se garde, un où il tombe.",
        exemples=[
            "Souligne le « e » dont tu parles.",
            "Dis les deux à voix basse avant d'écrire.",
        ],
        notes="Deux minutes. Ramasser : ceux qui écrivent « la s'maine » ont compris "
              "la prononciation et pas l'orthographe. Le reprendre à la séance suivante.")

    return d.save(dossier)
