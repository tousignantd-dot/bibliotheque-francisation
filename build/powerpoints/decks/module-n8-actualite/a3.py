# -*- coding: utf-8 -*-
"""A3 · Fait, opinion, propos rapporté
Bloc A « Je découvre » · couleur framboise · 75 min. Trois catégories, pas
deux, et le conditionnel journalistique.
Source : exercice `prFait` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Trois choses qu'on ne classe pas ensemble",
        chapeau="On vous a déjà appris à séparer le fait de l'opinion. C'est "
                "utile, et c'est insuffisant : la plus grande partie de ce "
                "que vous lisez n'est ni l'un ni l'autre.",
        duree='75 minutes')

    d.titre(notes="Séance charnière du bloc A. Annoncer le programme en une phrase : "
                  "aujourd'hui on apprend à classer, et tout le reste du module "
                  "s'appuie là-dessus, jusqu'à la lettre au journal.")

    d.objectifs([
        "distinguer un fait, une opinion et un propos rapporté ;",
        "repérer les marques de chacun : un nombre, un adjectif de jugement, « selon » ;",
        "reconnaître le conditionnel journalistique et savoir ce qu'il vaut ;",
        "séparer les trois dans son propre texte : ce que je sais, ce qu'on m'a dit, ce que j'en pense.",
    ], notes="Le quatrième objectif est celui qui rend une lettre publiable. Le "
             "rappeler à chaque fois qu'un élève mélange les trois à l'oral.")

    d.declencheur(
        'Observation', "Ces quatre phrases disent-elles la même chose ?",
        pistes=[
            "« Quatre-vingt-dix arbres seront abattus. »",
            "« Selon le promoteur, quatre-vingt-dix arbres seront abattus. »",
            "« Quatre-vingt-dix arbres seraient abattus. »",
            "« Abattre quatre-vingt-dix arbres est excessif. »",
        ],
        notes="Laisser chercher trois minutes. La plupart des élèves voient la "
              "quatrième et ratent l'écart entre la première et la deuxième. C'est "
              "précisément l'écart de la séance.")

    d.regle("Trois catégories, et non deux",
            "Un fait se vérifie ailleurs. Une opinion s'argumente sans "
            "jamais se prouver. Un propos rapporté n'engage que celui qui "
            "l'a dit.",
            precision="« Selon le promoteur, quatre-vingt-dix arbres seront abattus » "
                      "n'est pas l'information « quatre-vingt-dix arbres seront "
                      "abattus ». C'est l'information « le promoteur dit "
                      "quatre-vingt-dix ». Confondre les deux est l'erreur la plus "
                      "fréquente, et la plus utilisée.",
            notes="Diapositive à photographier. C'est l'énoncé central du module. "
                  "L'écrire au tableau et l'y laisser jusqu'à la séance E2.")

    d.cartes('Analyse', "Comment reconnaître chacun", [
        ("Le fait",
         "Quelqu'un d'autre, avec le même document, arriverait au même "
         "résultat : un procès-verbal, un cadastre, une date. Le signe : un "
         "nombre, un lieu, un verbe au passé composé."),
        ("L'opinion",
         "Elle porte une évaluation : trop, insuffisant, indécent, "
         "prioritaire. Le signe : un adjectif de jugement, « devrait », « il "
         "faut ». Deux personnes raisonnables peuvent ne pas s'accorder."),
        ("Le propos rapporté",
         "Le journaliste ne dit pas que c'est vrai : il dit que quelqu'un "
         "l'a dit. Le signe : selon, d'après, affirme, soutient, déclare. "
         "Ça vaut exactement ce que vaut la source nommée."),
        ("Le conditionnel journalistique",
         "« Le terrain aurait été évalué à deux millions. » Ni doute, ni "
         "politesse : on nous l'a dit, nous ne l'avons pas vérifié. C'est un "
         "propos rapporté sans source nommée, le plus fragile de tous."),
    ], notes="La quatrième carte est nouvelle pour presque tout le groupe. Faire "
             "chercher un « aurait » dans le reportage du bloc B avant de conclure : "
             "il y en a un, et il n'a pas de source.")

    d.tableau('Analyse', "La même information, quatre statuts",
              ['La phrase', "Ce qu'elle vaut"],
              [["Quatre-vingt-dix arbres seront abattus.",
                "donné comme un fait, et il ne l'est pas"],
               ["Selon le promoteur, quatre-vingt-dix arbres...",
                "propos rapporté, source nommée : correct"],
               ["Quatre-vingt-dix arbres seraient abattus.",
                "conditionnel : source non nommée"],
               ["Abattre quatre-vingt-dix arbres est excessif.",
                "opinion, assumée comme telle"]],
              cle=0,
              notes="Diapositive à photographier. Faire dire à haute voix la "
                    "différence entre la première et la deuxième ligne : c'est un mot "
                    "ajouté, et il change tout ce que la phrase engage.")

    d.pratique('Pratique 1 de 2', "Fait, opinion ou propos rapporté ?",
               "Classez chaque phrase dans l'une des trois catégories.", [
        ("Le règlement 1204 a été adopté lundi à vingt-deux heures cinquante.", "fait"),
        ("Céder un terrain public pour un dollar est indécent.", "opinion"),
        ("Selon le service de l'urbanisme, le rezonage prendrait vingt et un mois.", "rapporté"),
        ("Le boisé couvre onze hectares appartenant à la Ville.", "fait"),
        ("Le comité affirme avoir compté trois cent quarante-deux arbres.", "rapporté"),
        ("Quarante-cinq logements, c'est nettement insuffisant pour cette ville.", "opinion"),
        ("Le terrain aurait été évalué à un peu plus de deux millions.", "rapporté - sans source nommée"),
        ("On devrait toujours publier une évaluation avant un vote.", "opinion"),
    ], corrige=True,
       notes="Faire nommer la marque à chaque fois : le nombre, l'adjectif, le "
             "« selon ». La septième est celle qui sépare le groupe en deux : le "
             "conditionnel n'a pas de source, donc personne ne répond de la phrase.")

    d.regle("Un fait peut être faux",
            "C'est alors un fait erroné, pas une opinion. Ce qui en fait un "
            "fait, c'est qu'il soit vérifiable — pas qu'il soit vrai.",
            precision="Le comité compte trois cent quarante-deux arbres, le promoteur "
                      "en compte quatre-vingt-dix. Les deux comptages sont des faits. "
                      "L'un des deux est peut-être erroné, et il se peut aussi que les "
                      "deux soient exacts : ils ne comptent pas la même chose. "
                      "À partir de quel diamètre un jeune arbre est-il un arbre ?",
            notes="Diapositive à photographier. C'est la nuance la plus difficile de "
                  "la séance, et la plus utile : elle empêche de traiter de menteur "
                  "quelqu'un qui a simplement une autre définition.")

    d.piege('Piège', "écrire « le comité prétend avoir compté »",
            "écrire « le comité dit avoir compté »",
            "Ces verbes rapportent tous les deux, mais « prétendre » suppose "
            "un mensonge, comme « admettre » suppose une faute et "
            "« reconnaître » suppose qu'on résistait. Une rédaction "
            "rigoureuse s'en tient aux neutres : dit, affirme, déclare. Dans "
            "votre lettre, un seul de ces verbes suffit à vous faire écarter.",
            notes="Faire relire la même phrase avec les quatre verbes. Le groupe "
                  "entend le jugement glisser dans le verbe sans qu'un mot de "
                  "jugement soit écrit.")

    d.pratique('Pratique 2 de 2', "Réécrire honnêtement",
               "Chaque phrase présente une opinion ou une rumeur comme un "
               "fait. Réécrivez-la correctement.", [
        ("Le terrain vaut deux millions.", "Le terrain aurait été évalué à deux millions - à vérifier"),
        ("Le projet est mauvais.", "Je pense que le projet est mauvais"),
        ("Tout le monde sait que la Ville a caché l'évaluation.", "L'évaluation n'a pas été publiée - fait vérifiable"),
        ("Le rezonage prend vingt et un mois.", "Selon le service de l'urbanisme, le rezonage prendrait vingt et un mois"),
        ("Le comité prétend avoir compté 342 arbres.", "Le comité dit avoir compté 342 arbres"),
    ], corrige=True,
       notes="Accepter toute réformulation défendable : le but est de nommer le "
             "statut, pas de retrouver la phrase du corrigé. La troisième est la "
             "plus instructive : « tout le monde sait » remplace l'argument "
             "qui manque, et il n'y a presque jamais rien derrière.")

    d.billet(
        "Écrivez trois phrases sur le dossier du boisé : une de chaque catégorie.",
        exemples=[
            "Un fait avec son chiffre, une opinion annoncée comme telle, un propos rapporté avec sa source.",
            "Aucune des trois ne doit dépasser une ligne.",
        ],
        notes="Devoir court et exigeant. Les trois phrases se relisent en cinq "
              "minutes au début de A4, et elles servent de matière première à la "
              "lettre du bloc E.")

    return d.save(dossier)
