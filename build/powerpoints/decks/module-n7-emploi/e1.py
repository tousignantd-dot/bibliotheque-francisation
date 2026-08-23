# -*- coding: utf-8 -*-
"""E1 · Présentez votre projet
Bloc E « Je me lance » · couleur teal · 75 min.
Source du module : jeu de rôle « projet » et production orale de « Je me lance ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Présentez votre projet",
        chapeau="Quinze minutes à l'ordre du jour ; prenez-en deux. Le "
                "constat, la cause, ce que ça coûte, deux correctifs et une "
                "date. C'est l'intention même du programme : présenter un "
                "projet, une évaluation sommaire ou un problème à ses "
                "collègues.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Tout ce que l'élève a écrit depuis A1 se "
                  "rassemble ici. Prévoir : quinze minutes de répétition avec "
                  "l'assistant, quinze minutes de préparation, et le reste en "
                  "passages devant le groupe.")

    d.objectifs([
        "défendre un projet devant quelqu'un qui objecte le coût ;",
        "présenter en cinq temps, sans notes rédigées ;",
        "employer les connecteurs et une mise en relief ;",
        "obtenir une suite précise : une date, un document, un nom.",
    ], notes="Le deuxième objectif est le plus difficile : la plupart des élèves "
             "voudront lire leur texte. Autoriser un plan de cinq mots, pas plus.")

    d.declencheur(
        'Préparation', "Ce que vous allez dire, en cinq mots",
        pistes=[
            "Constat. Cause. Conséquence. Correctif. Échéance.",
            "Écrivez ces cinq mots sur un carton, et rien d'autre.",
            "Sous chacun, un chiffre ou une date, pas une phrase.",
            "Vous parlerez de mémoire, avec le carton sous les yeux.",
        ],
        notes="Passer dans les rangées pendant la préparation. Refuser les phrases "
              "rédigées : un élève qui lit ne présente pas, il récite, et l'intonation "
              "travaillée en A2 disparaît immédiatement.")

    d.cartes('Jeu de rôle', "L'assistant joue votre chef de production", [
        ("Trois dossiers au choix", "Le poste 4 - l'essai de rotation - la demande de soumission. Ou le vôtre, si vous en avez un vrai."),
        ("Il n'est pas contre vous", "Mais il a un budget, un horaire et cinq autres dossiers. Il objectera le coût au moins une fois."),
        ("Il demande vos sources", "« D'où vient ce chiffre ? » Préparez la réponse : le registre, le relevé, un appel."),
        ("Il n'offre jamais la suite", "Il faut la demander. Une date, un document, un nom. Sans ça, la rencontre finit sur rien."),
    ], notes="Quinze minutes en autonomie, sur le module, au casque. Passer et écouter "
             "deux ou trois échanges. L'assistant vouvoie : c'est une rencontre de "
             "travail avec un supérieur.")

    d.tableau('Analyse', "Les cinq temps de votre présentation",
              ['Le temps', 'Ce que vous dites'],
              [["1 · Le constat", "deux chiffres que vous avez comptés vous-même"],
               ["2 · La cause", "pourquoi, sans désigner un coupable"],
               ["3 · La conséquence", "ce que ça coûte si rien ne change"],
               ["4 · Deux correctifs", "le gratuit d'abord, le payant ensuite"],
               ["5 · L'échéance", "une date, et ce que vous demandez à la salle"]],
              cle=0,
              note="Et quelque part, la phrase qui vous grandit : « je n'ai pas ce chiffre, telle personne l'a ».",
              notes="Diapositive à photographier, et à laisser projetée pendant les "
                    "passages : c'est la grille d'écoute du groupe autant que le plan "
                    "de celui qui parle.")

    d.regle("Deux minutes, pas dix",
            "Une présentation courte et complète bat une présentation longue.",
            precision="Cinq temps en deux minutes, cela fait vingt-cinq secondes par "
                      "temps. C'est peu, et c'est exactement ce qui oblige à choisir "
                      "les deux chiffres qui comptent plutôt que d'énumérer les "
                      "quinze qu'on a. Une présentation qui déborde son temps se fait "
                      "couper, et c'est toujours la fin - donc la demande - qu'on "
                      "coupe.",
            notes="Diapositive à photographier. Chronométrer visiblement : poser le "
                  "téléphone sur la table, minuterie à deux minutes trente. Les élèves "
                  "s'y font en deux passages.")

    d.pratique('Pratique', "La grille d'écoute du groupe",
               "Pendant chaque passage, cochez ce que vous entendez.", [
        ("Le plan est annoncé au début.", ""),
        ("Il y a au moins deux chiffres.", ""),
        ("La cause est nommée sans accuser personne.", ""),
        ("Deux correctifs, dont un gratuit.", ""),
        ("Une date précise.", ""),
        ("Une demande claire adressée à la salle.", ""),
    ], notes="Distribuer la grille sur papier, une par élève et par passage. Les "
             "remettre à celui qui a présenté : une rétroaction écrite par six "
             "personnes vaut mieux qu'un commentaire de l'enseignante.")

    d.piege('Prise de parole',
            "lire son texte",
            "parler avec cinq mots sous les yeux",
            "Un texte lu se reconnaît en trois secondes : l'intonation devient plate, "
            "les yeux restent baissés, et la salle décroche. Cinq mots sur un carton "
            "obligent à chercher ses phrases, donc à regarder les gens, donc à "
            "descendre la voix à la fin de chaque phrase. Ce sera moins parfait et "
            "beaucoup plus écouté.",
            notes="C'est le retour de la séance A2. Si l'intonation s'est aplatie, "
                  "faire refaire trente secondes debout, sans carton du tout.")

    d.billet(
        "Après votre passage : notez une chose à améliorer, et une seule.",
        exemples=[
            "Qu'est-ce que le groupe n'a pas coché sur sa grille ?",
            "Est-ce que vous avez obtenu une suite précise ?",
            "Vous enregistrerez votre présentation dans le module, et vous l'enverrez.",
        ],
        notes="La production orale du module se dépose : l'élève s'enregistre, obtient "
              "une rétroaction de l'IA, corrige, puis envoie. Rappeler que la "
              "correction de l'IA reste privée et que seul l'envoi arrive à "
              "l'enseignante.")

    return d.save(dossier)
