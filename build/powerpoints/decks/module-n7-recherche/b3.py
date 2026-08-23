# -*- coding: utf-8 -*-
"""B3 · Les mots qui font tourner un long discours
Bloc B « Défi 1 » · couleur teal · écoute et réponds · 75 min.
Source : exercice `t1conn`, mini-leçon `t1conn`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='teal',
        titre="Les mots qui font tourner un long discours",
        chapeau="Ce qui empêche un auditeur de décrocher pendant vingt "
                "minutes, ce n'est pas le contenu : c'est une douzaine de "
                "petits mots qui annoncent chaque virage.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire du texte, mais elle se travaille à l'oreille. "
                  "Ces mots ne s'apprennent pas dans une liste : ils s'entendent "
                  "dans un discours qui tourne.")

    d.objectifs([
        "repérer les connecteurs qui annoncent un changement de sujet ;",
        "employer « quant à », « en ce qui concerne », « à propos de » ;",
        "distinguer ajouter un angle et opposer une idée ;",
        "reconnaître le résumé annoncé par « en somme ».",
    ], notes="Le deuxième objectif est celui qui coûte le plus : ces connecteurs "
             "sont rares dans la bouche des élèves, alors qu'ils sont partout dans "
             "les documents qu'on leur demande de lire.")

    d.declencheur(
        'Écoute', "Écoutez les deux versions du même passage.",
        pistes=[
            "Version 1 : « La fabrication occupe 11,2 %. La construction occupe 8,9 %. »",
            "Version 2 : « La fabrication occupe 11,2 %. En ce qui concerne la construction, elle occupe 8,9 %. »",
            "Le contenu est identique. Laquelle suivez-vous le mieux ?",
            "Qu'est-ce que la deuxième vous a dit de plus ?",
        ],
        notes="Lire les deux à voix haute, à débit égal. La différence s'entend "
              "immédiatement et elle se passe de théorie : la deuxième annonce le "
              "virage, la première le fait subir.")

    d.regle("Un connecteur de topicalisation annonce le sujet suivant",
            "« J'ai fini avec ce dont je parlais, voici ce dont je parle "
            "maintenant. » Le mot est savant, l'idée est simple.",
            precision="Ils se placent en tête de phrase et sont toujours suivis d'un "
                      "nom : quant à, en ce qui concerne, à propos de, à l'égard de. "
                      "Sans eux, l'auditeur croit qu'on lui répète la même chose et "
                      "cesse d'écouter.",
            notes="Diapositive à photographier. Insister sur « suivis d'un nom » : "
                  "c'est ce qui les distingue des conjonctions.")

    d.tableau('Analyse', "Quatre familles, douze mots",
              ['Ce qu\'on veut faire', 'Les mots'],
              [["Ouvrir, rappeler", "d'abord · pour commencer · rappelons que"],
               ["Changer de sujet", "quant à · en ce qui concerne · à propos de"],
               ["Ajouter un angle", "par ailleurs · d'autre part · en outre"],
               ["Redire, conclure", "autrement dit · en somme · par conséquent"]],
              cle=0,
              note="Douze mots à apprendre, et vingt minutes de radio deviennent suivables.",
              notes="Diapositive à photographier. C'est le tableau de référence du "
                    "bloc ; il resservira à l'écrit, dans la lettre du bloc D.")

    d.cartes('Analyse', "Ce que chacun annonce", [
        ("d'abord", "le socle : ce qu'il faut savoir avant tout"),
        ("rappelons que", "une information ancienne, nécessaire à la suite"),
        ("quant à", "je change de sujet, voici le suivant"),
        ("par ailleurs", "un autre angle du même dossier, pas une objection"),
        ("autrement dit", "la version simple de ce que je viens de dire"),
        ("en somme", "le résumé : la phrase à retenir si l'on n'en retient qu'une"),
    ], notes="« Autrement dit » est le plus utile à l'écoute : il annonce presque "
             "toujours la traduction de la phrase qu'on vient de ne pas comprendre. "
             "Apprendre à l'attendre.")

    d.piege('Grammaire',
            "« quand aux services », « quant à les services »",
            "« quant aux services »",
            "Deux fautes en une. « Quand » interroge sur le moment, « quant "
            "à » annonce un sujet — ils se prononcent presque pareil, ce qui "
            "n'aide personne. Et « quant à » se contracte comme tout « à » : "
            "quant au secteur, quant aux services, quant à la région.",
            notes="Faire écrire les trois formes contractées au tableau. La faute "
                  "d'orthographe se voit immédiatement dans une lettre de candidature.")

    d.pratique('Grammaire', "Le connecteur qui convient",
               "Chacun ne sert qu'une fois.", [
        ("___ , la région compte 286 395 habitants.", "D'abord"),
        ("___ que la moyenne québécoise est de 2 %.", "Rappelons"),
        ("Le primaire est à 4,2 %. ___ , la région tire deux fois plus de son sol.", "Autrement dit"),
        ("___ la construction, elle occupe 8,9 % de l'emploi.", "En ce qui concerne"),
        ("___ services, ils représentent plus des trois quarts de l'emploi.", "Quant aux"),
        ("___ la relève, la région n'est pas la seule à en manquer.", "À propos de"),
        ("___ : une région d'usines, une main-d'œuvre qui manque.", "En somme"),
    ], corrige=True,
       notes="Exercice `t1conn` du module interactif. Faire lire la phrase corrigée à "
             "voix haute, avec la pause après le connecteur : elle s'entend.")

    d.billet(
        "Écrivez trois phrases sur votre semaine, reliées par « d'abord », « quant à » et « en somme ».",
        exemples=[
            "N'importe quel sujet : le travail, l'école, la maison.",
            "L'important est que les trois connecteurs soient à leur place.",
        ],
        notes="Ramasser les billets : ils montrent tout de suite qui a compris que "
              "« quant à » est suivi d'un nom, et qui l'a pris pour « quand ».")

    return d.save(dossier)
