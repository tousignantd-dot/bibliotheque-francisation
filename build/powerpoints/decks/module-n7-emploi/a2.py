# -*- coding: utf-8 -*-
"""A2 · La voix qui monte et la voix qui descend
Bloc A « Je découvre » · couleur indigo (prosodie) · 75 min.
Source du module : exercice `prProso`, mini-leçon `prProso`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="La voix qui monte et la voix qui descend",
        chapeau="Un exposé dit sur une seule note s'entend comme une liste, "
                "et une liste ne se retient pas. Ce qui fait qu'on suit "
                "quelqu'un pendant douze minutes, ce n'est pas son "
                "vocabulaire : c'est sa mélodie.",
        duree='75 minutes')

    d.titre(notes="Séance de phonétique, mais pas de sons : de prosodie. Prévenir le "
                  "groupe que rien ne sera nouveau au niveau des mots - tout ce qu'on "
                  "va travailler, ils le disent déjà, mais sur une seule note.")

    d.objectifs([
        "découper une phrase en groupes rythmiques de trois à sept syllabes ;",
        "entendre que la voix monte quand la phrase continue ;",
        "entendre qu'elle descend quand la phrase est finie ;",
        "mettre un mot en avant en appuyant sa première syllabe, sans crier.",
    ], notes="Le quatrième objectif surprend toujours : les élèves croient qu'insister "
             "veut dire parler plus fort. En français, non.")

    d.declencheur(
        'Écoute', "Deux fois la même phrase. Qu'est-ce qui change ?",
        pistes=[
            "« D'abord, on mesure... » puis « Voilà. Des questions ? »",
            "Est-ce que la voix finit en haut ou en bas ?",
            "Dans votre première langue, est-ce pareil ?",
            "Comment savez-vous qu'une personne a fini de parler ?",
        ],
        notes="Lire les deux phrases soi-même, deux fois chacune, sans rien expliquer. "
              "Laisser le groupe nommer la différence avec ses propres mots avant "
              "d'introduire « monte » et « descend ».")

    d.regle("On ne parle pas mot par mot",
            "Le français se dit par groupes de trois à sept syllabes.",
            precision="Entre deux groupes, il y a un arrêt très court : trop court "
                      "pour être une pause, assez long pour être entendu. « D'abord, "
                      "on mesure / pendant deux semaines / chaque camion. » Trois "
                      "groupes, trois respirations minuscules, et la phrase devient "
                      "suivable. À l'intérieur d'un groupe, un seul mot est accentué : "
                      "le dernier.",
            notes="Diapositive à photographier. Faire découper trois phrases du "
                  "dialogue au tableau, à la barre oblique, avant de passer à la suite.")

    d.cartes('Analyse', "Ce que fait la voix, et ce que ça dit", [
        ("La voix monte", "À la fin d'un groupe qui n'est pas le dernier. Ce n'est pas une question : c'est un signal qui dit « ne partez pas, la suite arrive »."),
        ("La voix descend", "Au dernier groupe de la phrase, franchement. C'est le seul signal qui autorise l'autre à parler."),
        ("La question qui monte", "Seule la question sans mot interrogatif monte : « On décide en novembre ? »"),
        ("La question qui descend", "Une question avec mot interrogatif descend comme une phrase ordinaire : « Quand est-ce qu'on décide ? »"),
    ], notes="Les deux dernières cartes règlent une confusion très fréquente : les "
             "élèves croient que toute question monte. Faire dire les deux questions "
             "l'une après l'autre.")

    d.pratique('Écoute', "Est-ce que la voix monte ou descend ?",
               "Écoutez chaque groupe et dites ce que fait la voix.", [
        ("Il y a quatre étapes", "elle monte - la phrase continue"),
        ("Voilà. Des questions ?", "elle descend - la parole est rendue"),
        ("D'abord, on mesure", "elle monte"),
        ("Enfin, on installe pour de bon.", "elle descend"),
        ("Pour l'échéancier, maintenant", "elle monte"),
        ("Rien n'est acheté avant la mi-novembre.", "elle descend"),
    ], corrige=True,
       notes="Dire chaque groupe deux fois, sans exagérer la première fois. Faire "
             "lever la main : main en haut si ça monte, main en bas si ça descend. "
             "C'est l'exercice `prProso` du module.")

    d.regle("Insister, c'est appuyer, pas crier",
            "L'accent d'insistance porte sur la PREMIÈRE syllabe du mot.",
            precision="Pour qu'un mot ressorte, on ne monte pas le volume : on appuie "
                      "sa première syllabe, on la tient un peu plus longtemps, et on "
                      "ralentit juste avant. « C'est la partie la moins SPEC-taculaire "
                      "du projet. » Un ou deux accents d'insistance par minute suffisent. "
                      "Trois de suite, et plus rien ne ressort.",
            notes="Diapositive à photographier. Le faire entendre trois fois : sans "
                  "accent, avec l'accent au bon endroit, puis en criant. Le troisième "
                  "essai fait rire, et c'est ce qui fait comprendre.")

    d.piege('Prononciation',
            "monter la voix à la fin de chaque phrase",
            "descendre quand la phrase est finie",
            "C'est l'habitude la plus répandue chez les adultes qui présentent en "
            "français. Elle donne l'impression qu'on demande la permission à chaque "
            "phrase, et la salle finit par ne plus croire ce qu'on dit. Elle se "
            "corrige en une semaine, à condition de s'entendre : enregistrez-vous "
            "trente secondes et réécoutez-vous.",
            notes="Beaucoup d'élèves viennent de langues à intonation montante "
                  "généralisée. Nommer ce fait, sans le présenter comme un défaut : "
                  "c'est une habitude d'une langue transposée dans une autre.")

    d.pratique('Pratique', "Dites-les à voix haute",
               "Un groupe qui monte, puis un groupe qui descend, dans la même phrase.", [
        ("D'abord, on mesure, // pendant deux semaines.", ""),
        ("Il y a quatre étapes, // et je vais les nommer.", ""),
        ("Le budget, justement : // l'essai coûte quatre cents dollars.", ""),
        ("Trois risques, // et je préfère les nommer moi-même.", ""),
        ("Ce qui use le dos, // c'est de se pencher.", ""),
        ("En somme : // on mesure, on trace, on essaie, on installe.", ""),
    ], notes="La double barre marque la charnière : ça monte avant, ça descend après. "
             "Faire passer chaque élève sur une phrase, debout. Deux minutes par "
             "personne, pas plus.")

    d.billet(
        "Enregistrez-vous en disant trois phrases de votre choix.",
        exemples=[
            "Réécoutez-vous : est-ce que vos phrases finissent en haut ou en bas ?",
            "Redites-les en descendant nettement à la fin.",
        ],
        notes="Devoir d'écoute de soi. Le téléphone suffit. C'est le seul moyen de "
              "corriger une intonation : personne ne s'entend en parlant.")

    return d.save(dossier)
