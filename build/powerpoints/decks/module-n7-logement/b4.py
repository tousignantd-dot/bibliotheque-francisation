# -*- coding: utf-8 -*-
"""B4 · Mettre en avant, concéder, demander
Bloc B « Défi 1 · L'avis du propriétaire » · couleur teal · écoute et réponds ·
75 min.
Source : exercices `t1emph` et `t1nego` et leurs mini-leçons ; savoir
« phrases emphatiques » du niveau 7 (cinq points).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='teal',
        titre="Mettre en avant, concéder, demander",
        chapeau="Une phrase de négociation a deux moitiés, et l'ordre "
                "décide de la réponse : on reconnaît d'abord l'argument de "
                "l'autre, on présente le sien ensuite.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 1. C'est la séance la plus orale du bloc : "
                  "prévoir des paires et beaucoup de temps de parole, peu de tableau.")

    d.objectifs([
        "mettre un élément en avant avec « c'est… qui » et « ce qui…, c'est » ;",
        "concéder un argument avant de présenter le sien ;",
        "reconnaître ce qui fait avancer une négociation et ce qui la bloque ;",
        "terminer une entente en demandant un écrit.",
    ], notes="Le troisième objectif se joue sur des exemples, pas sur une règle : les "
             "huit énoncés de `t1nego` suffisent à faire entendre la différence.")

    d.declencheur(
        'Écoute', "Deux façons de dire la même chose",
        pistes=[
            "« Le montant me dérange. »",
            "« Ce qui me dérange, c'est le montant. »",
            "Laquelle des deux se retient ? Pourquoi ?",
            "Dans laquelle sait-on d'avance de quoi on va parler ?",
        ],
        notes="La seconde annonce l'objet du désaccord avant de le nommer : c'est ce "
              "qui laisse à l'autre une seconde pour se préparer, et à vous une seconde "
              "pour choisir la fin de votre phrase.")

    d.cartes('Analyse', "Trois moules pour mettre en avant", [
        ("c'est… qui / c'est… que", "On sort un élément et on le place entre « c'est » et « qui » ou « que ». Qui si c'est le sujet, que si c'est le complément."),
        ("ce qui…, c'est…", "Le plus utile pour ouvrir une discussion difficile : on annonce, puis on pose. Variantes : ce que je demande…, ce dont j'ai besoin…"),
        ("La fenêtre, c'est elle le sujet", "On nomme, puis on reprend par un pronom. Très fréquent à l'oral au Québec ; à éviter dans une lettre."),
        ("Une seule par idée", "Si tout est mis en avant, plus rien ne l'est. Choisissez le mot qui doit rester dans la tête de l'autre."),
    ], notes="Faire produire une phrase de chaque moule par le groupe, sur le dossier "
             "de Sokhna, avant de passer à l'exercice.")

    d.pratique('Écoute et réponds', "Emphatique : qui ou que ?",
               "Complétez, puis dites la phrase à voix haute.", [
        ("C'est la date de réception ___ compte.", "qui - la date est le sujet"),
        ("C'est cette date-là ___ je note.", "que - je est le sujet"),
        ("C'est votre immeuble ___ garde la fenêtre.", "qui - l'immeuble est le sujet"),
        ("Ce ___ je demande, c'est deux lignes signées.", "que"),
        ("Ce ___ me dérange, c'est le montant d'un seul coup.", "qui"),
    ], corrige=True,
       notes="Le test est le même à chaque fois : ce qui suit est-il un verbe (qui) ou "
             "un sujet (que) ? Le faire dire par le groupe, pas par l'enseignante.")

    d.regle("Concéder d'abord, demander ensuite",
            "Reconnaître l'argument de l'autre ne le renforce pas : ça vous donne le droit de présenter le vôtre.",
            precision="Quatre entrées : « je comprends que… », « c'est vrai que… », "
                      "« vous avez raison sur… », « admettons que… ». Puis on tourne "
                      "avec « mais », « cela dit », « par contre », « n'empêche que ». "
                      "Et alors seulement vient la demande — avec un chiffre, une raison "
                      "et une contrepartie.",
            notes="Diapositive à photographier. Faire construire trois phrases "
                  "complètes en paires, avec les deux moitiés dans le bon ordre.")

    d.pratique('Écoute et réponds', "Ça fait avancer ou ça fait reculer ?",
               "Dites, pour chaque phrase, ce qu'elle produit chez l'autre.", [
        ("Je comprends que vos taxes ont monté, cela dit, 84 $ d'un coup, c'est beaucoup.", "ça fait avancer"),
        ("Vous exagérez, comme d'habitude.", "ça fait reculer"),
        ("Je vous proposerais 55 $, à condition que la fenêtre soit regardée.", "ça fait avancer"),
        ("Si vous ne baissez pas, je vous amène au Tribunal.", "ça fait reculer"),
        ("Est-ce que vous accepteriez de m'écrire deux lignes avec la date ?", "ça fait avancer"),
        ("Ce n'est pas la peine de discuter, vous avez déjà décidé.", "ça fait reculer"),
    ], corrige=True,
       notes="Six des huit énoncés de `t1nego`. Après correction, demander de "
             "réécrire chaque phrase « qui fait reculer » pour qu'elle fasse avancer.")

    d.piege('Négociation',
            "C'est trop cher.",
            "Je vous proposerais cinquante-cinq dollars.",
            "Une demande sans chiffre n'appelle aucune réponse : l'autre n'a rien à "
            "accepter ni à refuser. Un montant précis, lui, oblige à répondre — et il "
            "montre que vous avez réfléchi avant d'entrer dans la pièce. Décidez deux "
            "chiffres avant la rencontre : celui que vous demandez, et celui en dessous "
            "duquel vous n'irez pas.",
            notes="Le second chiffre ne se dit jamais à l'autre. Le préciser : c'est "
                  "une décision pour soi, pas une carte à jouer.")

    d.billet(
        "Écris ta phrase de négociation complète : concession, puis demande.",
        exemples=[
            "« Je comprends que…, cela dit…, je vous proposerais… »",
            "Deux phrases au maximum.",
        ],
        notes="Trois minutes. Ces billets sont la répétition du jeu de rôle de E1 : "
              "les garder et les redistribuer à ce moment-là.")

    return d.save(dossier)
