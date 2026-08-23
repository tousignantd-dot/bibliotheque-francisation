# -*- coding: utf-8 -*-
"""B2 · Le conditionnel de ce qui n'est pas encore décidé
Bloc B « Défi 1 » · couleur acier · 75 min.
Source : exercice `t1cond` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='acier',
        titre="Rien n'est décidé, et la langue doit le dire",
        chapeau="Au moment de l'appel, l'employeur n'a rien décidé et vous "
                "non plus. Le conditionnel installe exactement cet état des "
                "choses : c'est possible, ce n'est pas fait.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Commencer par relire deux des billets de B1 : "
                  "presque tous sont écrits à l'indicatif, et cela s'entend.")

    d.objectifs([
        "former le conditionnel présent sans hésiter ;",
        "distinguer ses trois emplois : incertitude, politesse, proposition ;",
        "ne jamais mettre de conditionnel après « si » ;",
        "reconnaître le conditionnel chez l'autre, et savoir ce qu'il annonce.",
    ], notes="Le quatrième objectif est celui qu'on n'enseigne jamais et qui sert le "
             "plus : tant que l'employeur emploie le conditionnel, la porte est "
             "ouverte.")

    d.declencheur(
        'Observation', "Une lettre, un « s » : qu'est-ce qui change ?",
        pistes=[
            "« Je serai disponible dès novembre. »",
            "« Je serais disponible si vous le souhaitiez. »",
            "Laquelle des deux suppose qu'on vous a déjà engagée ?",
            "Laquelle écririez-vous dans un courriel de candidature ?",
        ],
        notes="Faire écrire les deux au tableau. La faute la plus fréquente à l'écrit "
              "est de mettre la première là où la seconde s'impose.")

    d.regle("Radical du futur, terminaisons de l'imparfait",
            "Je pourrais, tu viendrais, il faudrait, nous serions, vous "
            "auriez, elles conviendraient. Une seule forme, et le contexte "
            "dit lequel des trois emplois on fait.",
            precision="Les verbes irréguliers au futur le sont ici aussi : aller donne "
                      "j'irais, faire donne je ferais, savoir donne je saurais, devoir "
                      "donne je devrais, vouloir donne je voudrais.",
            notes="Diapositive à photographier. Faire conjuguer trois verbes à voix "
                  "haute avant de continuer : être, pouvoir, falloir.")

    d.cartes('Analyse', "Trois emplois, une seule forme", [
        ("L'incertitude",
         "Ce qui n'est pas décidé, ou ce qu'on rapporte sans le garantir. "
         "Est-ce que cet horaire vous conviendrait ? Le poste comporterait "
         "une part de recrutement."),
        ("La politesse",
         "Adoucir une demande ou une objection. Pourriez-vous me préciser... "
         "Je voudrais revenir sur un point. J'aimerais qu'on regarde le "
         "quatrième échelon."),
        ("La proposition",
         "Offrir sans imposer. Je proposerais le troisième échelon à "
         "l'embauche. Nous vous situerions au deuxième. C'est la forme de la "
         "négociation : on met une idée sur la table sans la planter."),
    ], notes="Insister sur le troisième : une proposition au conditionnel se discute, "
             "une exigence à l'indicatif s'accepte ou se refuse. L'élève choisit "
             "lequel des deux il veut, et il ne le sait pas.")

    d.pratique('Pratique 1 de 2', "Mettez au conditionnel présent",
               "Rien n'est encore conclu.", [
        ("Est-ce que cet horaire vous ___ (convenir) ?", "conviendrait"),
        ("___ (Pouvoir)-vous me préciser la taille des équipes ?", "Pourriez"),
        ("Je ___ (vouloir) revenir sur un point de l'annonce.", "voudrais"),
        ("Il ___ (falloir) que je sache ce que l'examen évalue.", "faudrait"),
        ("Nous vous ___ (situer) au deuxième échelon.", "situerions"),
        ("Ces onze années ___ (être)-elles vérifiables ?", "seraient"),
    ], corrige=True,
       notes="Écrire chaque réponse au tableau : c'est l'orthographe qui pose "
             "problème, pas la forme orale.")

    d.piege('Piège', "« si vous pourriez »",
            "« si vous pouviez »",
            "Aucun conditionnel après « si », jamais. On dit « si vous "
            "pouviez, je serais disponible » : l'imparfait dans la condition, "
            "le conditionnel dans l'autre moitié de la phrase. C'est la faute "
            "que tous les francophones remarquent, y compris ceux qui ne "
            "sauraient pas la nommer.",
            notes="Faire répéter la formule à voix haute : « après si, jamais de "
                  "conditionnel ». Elle reviendra au défi 3, avec le plus-que-parfait.")

    d.pratique('Pratique 2 de 2', "Réécrivez plus poliment",
               "Passez de l'indicatif au conditionnel.", [
        ("Précisez-moi la taille des équipes.", "Pourriez-vous me préciser la taille des équipes ?"),
        ("Je veux revenir sur ce point.", "Je voudrais revenir sur ce point."),
        ("Il faut que je sache ce que l'examen évalue.", "Il faudrait que je sache..."),
        ("Je demande le troisième échelon.", "Je proposerais le troisième échelon."),
    ], corrige=True,
       notes="Faire dire les deux versions à voix haute, l'une après l'autre. La "
             "nuance n'est audible qu'en comparaison, et c'est là que la séance A2 "
             "ressert : la mélodie compte autant que la forme.")

    d.tableau('Analyse', "Ce que le conditionnel de l'autre vous apprend",
              ['Ce qu\'il dit', 'Ce que cela signifie'],
              [["« Nous vous situerions au deuxième »",
                "rien n'est signé : la marge existe"],
               ["« Le poste comporterait du recrutement »",
                "il rapporte sans garantir : à faire confirmer"],
               ["« Nous vous situons au deuxième »",
                "c'est décidé : la discussion est fermée"]],
              cle=0,
              notes="Diapositive à photographier. C'est le contenu le plus utile de la "
                    "séance, et il n'est dans aucune grammaire : écouter le mode de "
                    "son interlocuteur renseigne sur sa marge.")

    d.billet(
        "Reprenez vos trois questions de B1 et réécrivez-les au conditionnel.",
        exemples=[
            "Pourriez-vous... / Je voudrais savoir si...",
            "Gardez la même question : changez seulement le mode.",
        ],
        notes="Les mêmes questions seront reprises une troisième fois en B3, à "
              "l'inversion. Trois passages sur la même phrase, trois hauteurs de "
              "langue : c'est la progression du bloc.")

    return d.save(dossier)
