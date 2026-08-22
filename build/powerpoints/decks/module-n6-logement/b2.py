# -*- coding: utf-8 -*-
"""B2 · La page, du haut jusqu'en bas
Bloc B « Défi 1 · Ce que dit le site » · couleur teal · 90 min.
Source : exercice `t1page` (type texte) et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='teal',
        titre="La page, du haut jusqu'en bas",
        chapeau="Un texte qui ne parle de personne, et qui parle de vous. "
                "C'est l'intention même du programme : s'informer sur ses "
                "droits en consultant un site Web.",
        duree='90 minutes')

    d.titre(notes="Séance la plus longue du bloc, et la plus importante du module : "
                  "c'est ici que se travaille l'unique intention de la situation. "
                  "Prévoir les postes pour la seconde heure.")

    d.objectifs([
        "reconnaître les quatre morceaux d'une fiche de droits ;",
        "décoder quatre tournures juridiques courantes ;",
        "retrouver dans un texte suivi le passage qui répond à une "
        "question ;",
        "traduire chaque ligne de la fiche en phrase qui commence par "
        "« moi, je ».",
    ], notes="Le quatrième objectif est le seul qui compte vraiment. Les trois autres "
             "sont des chemins pour y arriver.")

    d.declencheur(
        'Observation', "Pourquoi un texte de droits ne dit-il jamais « vous » ?",
        pistes=[
            "À combien de personnes cette page doit-elle servir ?",
            "Que se passerait-il si elle nommait quelqu'un ?",
            "Est-ce plus difficile à lire ? Pourquoi ?",
        ],
        notes="La réponse est simple et elle rassure : la page doit être vraie pour "
              "tout le monde, donc elle ne peut nommer personne. La difficulté n'est "
              "pas dans les mots, elle est dans cette distance-là.")

    d.tableau('Analyse', "Les quatre morceaux, toujours dans cet ordre",
              ['Le morceau', 'Ce qu\'on y trouve'],
              [["1. Ce que c'est", "la définition, et ce avec quoi on la confond"],
               ["2. Ce qu'il faut faire", "l'action, sa forme, son contenu obligatoire"],
               ["3. Le délai", "le nombre de jours, et à partir de quand"],
               ["4. Ce qui suit", "le refus, les frais, les recours"]],
              cle=0,
              note="Le délai est au milieu, et c'est celui qu'on saute.",
              notes="Diapositive à photographier. Faire vérifier l'ordre sur la page "
                    "projetée : les quatre intertitres y sont, numérotés.")

    d.cartes('Décodage', "Quatre tournures, et ce qu'elles veulent dire", [
        ("« est réputé avoir consenti »", "La loi considère qu'il a dit oui, même s'il n'a rien dit. C'est le silence qui parle à sa place, et c'est ce qui protège le locataire."),
        ("« doit faire connaître »", "Il est obligé de le dire, et de le dire à vous. Un refus qu'on ne vous transmet pas n'a pas été fait."),
        ("« peut exiger »", "Il a le droit de demander. Ce n'est pas le droit d'obtenir n'importe quoi : ce qui suit le verbe fixe la limite."),
        ("« demeure tenu de »", "Ça reste sur vos épaules, malgré tout le reste. C'est la formule qui dit que la sous-location ne vous libère de rien."),
    ], notes="Lire chaque tournure à voix haute, puis sa traduction. Faire chercher "
             "laquelle des quatre est la plus dangereuse à mal comprendre : c'est la "
             "dernière, et la classe le trouve seule.")

    d.regle("« Peut » et « doit » ne se lisent jamais assez lentement",
            "Un texte de droits ne les emploie jamais l'un pour l'autre.",
            precision="« Le locataire doit aviser par écrit » : il n'a pas le "
                      "choix. « Le locateur peut exiger le remboursement » : il a "
                      "le droit de demander, et vous avez le droit de demander à "
                      "quoi cela correspond. Deux mots de trois lettres, et toute "
                      "la différence entre une obligation et une possibilité.",
            notes="Diapositive à photographier. Faire relever dans la page projetée "
                  "tous les « doit » et tous les « peut », au surligneur, avant de "
                  "passer à l'exercice.")

    d.pratique('Lecture', "Où est la réponse dans la page ?",
               "Nommez l'intertitre où se trouve la réponse.", [
        ("Que doit contenir l'avis ?", "1. Aviser le locateur"),
        ("Combien de temps le locateur a-t-il ?", "2. Le délai de réponse"),
        ("Que se passe-t-il s'il ne répond pas ?", "2. Le délai de réponse"),
        ("À quelle condition peut-il refuser ?", "3. Le refus"),
        ("Quel argent peut-il réclamer ?", "4. Les frais et les obligations"),
        ("Qui doit le loyer pendant la sous-location ?", "4. Les frais et les obligations"),
    ], corrige=True,
       notes="Exercice de repérage, pas de compréhension : on cherche l'endroit, pas "
             "la réponse. C'est exactement ce que fait l'exercice interactif, où "
             "l'élève clique le passage dans la page.")

    d.tableau('Traduction', "La fiche, dite en « moi, je »",
              ['La page écrit', 'Farida comprend'],
              [["aviser par écrit", "je dois écrire, pas seulement parler"],
               ["le nom et l'adresse", "je dois avoir trouvé quelqu'un avant"],
               ["quinze jours de la réception", "mon délai part du jour où il l'a eu"],
               ["demeure tenu de ses obligations", "je reste responsable du loyer"]],
              cle=0,
              notes="Faire l'exercice dans l'autre sens à la fin : l'enseignante dit la "
                    "colonne de droite, la classe retrouve la formule de gauche. C'est "
                    "ce qui prépare l'écriture de l'avis, en C2.")

    d.piege('Attention',
            "lire seulement le premier paragraphe",
            "descendre jusqu'au délai",
            "Le premier paragraphe définit ; il ne dit jamais ce qu'il faut "
            "faire ni quand. Gilles le disait dès la première séance : c'est "
            "toujours au milieu du texte qu'il y a le chiffre qui compte.",
            notes="Faire le compte à main levée : qui, dans la classe, lit un papier "
                  "officiel jusqu'au bout ? La réponse est toujours la même, et elle "
                  "rend la règle inoubliable.")

    d.billet(
        "Une page trouvée sur Internet : à quoi voyez-vous qu'elle est fiable ?",
        exemples=[
            "Deux indices suffisent.",
            "Pensez à ce qu'on regarde avant de lire.",
        ],
        notes="Deux minutes. Les réponses attendues : le nom de l'organisme et la date "
              "de mise à jour. Elles ouvrent la séance B3, qui porte justement sur ce "
              "qu'une page dit avant ses phrases.")

    return d.save(dossier)
