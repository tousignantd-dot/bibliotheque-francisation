# -*- coding: utf-8 -*-
"""A2 · Quand les lettres mentent : ch, x, sh
Bloc A « Je découvre » · couleur indigo · 75 min. Graphie-phonie.
Source : exercice `prGraphie` et sa mini-leçon, savoir « Graphie-phonie » du
niveau 6 — associer des phonèmes à des graphèmes inhabituels.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Quand les lettres mentent : ch, x, sh",
        chapeau="Trois cas où l'écriture trompe l'oreille. Ce sont ceux que "
                "le programme du niveau 6 nomme, et ce sont ceux qu'on "
                "rencontre dans une usine.",
        duree='75 minutes')

    d.titre(notes="Séance de prononciation. Le matériel tient dans l'exercice 2 du "
                  "module et sa mini-leçon. Prévoir des écouteurs : l'exercice se "
                  "fait carte par carte, en écoutant.")

    d.objectifs([
        "reconnaître à l'oreille le son [k] écrit « ch » ;",
        "reconnaître le son [s] écrit « x » dans les nombres ;",
        "reconnaître le son de « chat » écrit « sh » ou « sch » ;",
        "chercher un mot entendu en essayant l'autre graphie.",
    ], notes="Le quatrième objectif est le plus utile de la séance : il transforme "
             "un savoir de prononciation en savoir de recherche. Un mot qu'on "
             "n'écrit pas comme on l'entend est un mot qu'on ne retrouve pas.")

    d.declencheur(
        'Observation', "As-tu déjà cherché un mot dans le dictionnaire sans le trouver ?",
        pistes=[
            "Tu l'avais entendu, tu l'as écrit comme tu l'entendais.",
            "Quel mot était-ce ? Qu'est-ce qui manquait ?",
            "Dans ta langue, est-ce qu'on écrit comme on prononce ?",
        ],
        notes="Presque tous les élèves ont vécu ça. La séance leur donne trois "
              "règles qui règlent une bonne part des cas, au travail surtout.")

    d.tableau('Analyse', "Trois cas, et rien d'autre",
              ['On écrit', 'On entend'],
              [["ch (mot savant)", "[k], comme dans « kilo » — un technicien, un chronomètre"],
               ["x (dans un nombre)", "[s], comme dans « dis » — dix, six, soixante"],
               ["sh, sch", "le son de « chat » — un schéma, un shampoing, un short"],
               ["ch (mot courant)", "le son normal — chercher, chaque, chose, machine"]],
              cle=0,
              note="Le [k] est l'exception, pas la règle : la plupart des « ch » se disent comme dans « chat ».",
              notes="Diapositive à photographier. La quatrième ligne est là exprès : "
                    "sans elle, le groupe repart en prononçant « machine » avec un k.")

    d.regle("Le repère du mot savant",
            "Le « ch » qui dit [k] se cache presque toujours dans un mot venu du grec.",
            precision="Un technicien, un chronomètre, le chlore, un écho, la "
                      "psychologie : ce sont des mots techniques, et une usine en est "
                      "pleine. Ils portent souvent un « y » ou un « ph » à côté. Ce "
                      "sont les mêmes mots dans beaucoup de langues, ce qui aide.",
            notes="Faire chercher au groupe le mot équivalent dans leur langue : "
                  "« technicien » se dit presque pareil partout, et le [k] y est.")

    d.pratique('Écoute', "Quel son entends-tu ?",
               "L'enseignante lit chaque mot deux fois. Écrivez K, S ou CH.", [
        ("un technicien", "K"),
        ("un chronomètre", "K"),
        ("le chlore", "K"),
        ("dix", "S"),
        ("soixante", "S"),
        ("un schéma", "CH"),
        ("un shampoing", "CH"),
        ("un t-shirt", "CH"),
    ], corrige=True,
       notes="Lire les mots dans le désordre, jamais dans l'ordre du tableau. Deux "
             "passages : le premier pour trancher, le second pour vérifier. Ne pas "
             "montrer l'écriture avant la correction.")

    d.piege('Piège', "chercher « tecnicien » parce qu'on l'a entendu ainsi",
            "essayer « ch » à la place du k, et « x » à la place du s",
            "Un mot entendu qui ne se trouve nulle part est presque toujours un mot "
            "à graphie inhabituelle. Deux essais suffisent : remplacer le k par "
            "« ch », remplacer le s par « x ». C'est le geste le plus utile de la "
            "séance, et il sert bien au-delà de ces trois cas.",
            notes="Faire l'essai en direct sur un téléphone, avec « cronomètre » puis "
                  "« chronomètre ». Voir la différence à l'écran vaut dix explications.")

    d.tableau('Le cas de « dix »', "Trois prononciations, et toutes se comprennent",
              ['Ce qu\'on écrit', "Ce qu'on entend"],
              [["dix", "« dis » — tout seul, le x se dit"],
               ["dix jours", "« di jours » — devant une consonne, il se tait"],
               ["dix ans", "« diz ans » — devant une voyelle, il se lie"],
               ["six mois", "« si mois » — même règle que dix"]],
              cle=0,
              note="Personne ne vous reprendra si vous dites « diz jours » : l'important est de reconnaître les trois.",
              notes="C'est la partie la plus rassurante de la séance. Le dire "
                    "explicitement : on travaille l'oreille, pas la perfection.")

    d.pratique('Prononciation', "Lire à voix haute",
               "Chacun lit une ligne. Le groupe corrige seulement le son visé.", [
        ("Le technicien passe deux fois par quart.", "« tec-nicien »"),
        ("Un chronomètre mesure le temps de cycle.", "« cro-nomètre »"),
        ("L'affichage reste dix jours ouvrables.", "« di jours »"),
        ("Il faut six mois d'ancienneté.", "« si mois »"),
        ("La cafétéria compte soixante places.", "« soi-sante »"),
        ("La note était accompagnée d'un schéma.", "« ché-ma »"),
    ], corrige=True,
       notes="Ne corriger que le son de la séance. Reprendre un élève sur autre "
             "chose ici casse la confiance et fait perdre le point travaillé.")

    d.billet(
        "Écris deux mots que tu prononçais autrement avant aujourd'hui.",
        exemples=[
            "Un mot du travail si possible.",
            "Écris-le comme tu l'entends, puis comme il s'écrit.",
        ],
        notes="Deux minutes. Ramasser les billets : ils disent quels mots reprendre "
              "en A4, et ils font une liste de classe très concrète.")

    return d.save(dossier)
