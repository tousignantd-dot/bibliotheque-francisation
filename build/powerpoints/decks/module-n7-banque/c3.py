# -*- coding: utf-8 -*-
"""C3 · La phrase qui ne dit pas qui fait
Bloc C « Défi 2 · Faire travailler l'argent » · couleur ambre · 75 min.
Source : exercice `t2passif` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre='La phrase qui ne dit pas qui fait',
        chapeau="« Des frais seront exigés. » Par qui ? La voix passive "
                "permet d'annoncer ce qui arrive sans nommer qui le décide.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire tirée du document de C2, qui est écrit au passif "
                  "d'un bout à l'autre. Reprendre le document en main pour la séance.")

    d.objectifs([
        "reconnaître une phrase passive dans un document ;",
        "la former avec être et le participe passé ;",
        "accorder le participe avec le sujet ;",
        "poser la question que le passif escamote : par qui ?",
    ], notes="Le quatrième objectif est le seul qui ne soit pas grammatical, et c'est "
             "celui qui rend la séance utile.")

    d.declencheur(
        'Observation', "« Des frais seront exigés. » Qu'est-ce qui manque à cette "
                       "phrase ?",
        pistes=[
            "Qui exige ces frais ?",
            "Dans quel cas ?",
            "Pourquoi le document ne le dit-il pas ?",
            "Que demanderais-tu au comptoir ?",
        ],
        notes="Le groupe trouve toujours « par qui ». C'est exactement le réflexe que "
              "la séance installe.")

    d.regle("Être plus participe passé",
            "L'Autorité protège les dépôts devient : les dépôts sont protégés par "
            "l'Autorité.",
            precision="Le complément direct devient sujet, le verbe devient être au "
                      "même temps, suivi du participe passé. « Protège » donne « sont "
                      "protégés » ; « a protégé » donne « ont été protégés ». Seuls les "
                      "verbes qui ont un complément direct se mettent au passif.",
            notes="Diapositive à photographier. Le contre-exemple est utile : « elle "
                  "téléphone à la caisse » n'a pas de passif.")

    d.tableau('Analyse', "Trois formes de la même idée",
              ['La forme', 'La phrase'],
              [['active', "L'agent a bloqué la carte."],
               ['passive avec agent', "La carte a été bloquée par l'agent."],
               ['passive sans agent', "La carte a été bloquée."],
               ['ce que dit la 3e', "le geste compte, pas la personne"]],
              cle=0,
              notes="Diapositive à photographier. Aucune des trois n'est fautive : "
                    "elles ne mettent pas la même chose en avant, et c'est tout.")

    d.regle("Le participe s'accorde avec le sujet",
            "Le dépôt est protégé, la somme est protégée, les sommes sont protégées.",
            precision="À l'oral, les quatre formes se disent pareil : c'est pour cela "
                      "que la faute est si fréquente à l'écrit. Le réflexe : chercher "
                      "le sujet, lui demander son genre et son nombre, accorder. Le "
                      "complément introduit par « par » n'a aucune influence.",
            notes="Diapositive à photographier. Faire écrire les quatre formes au "
                  "tableau et les faire lire : elles se prononcent de la même façon.")

    d.pratique('Application', "Mettez la phrase à la voix passive",
               "Gardez le même temps.", [
        ("L'Autorité protège les dépôts.", "Les dépôts sont protégés par l'Autorité."),
        ("La caisse calcule les frais chaque jour.", "Les frais sont calculés chaque jour."),
        ("L'agent a bloqué la carte.", "La carte a été bloquée."),
        ("Le contrat fixe le taux.", "Le taux est fixé."),
        ("On immobilise la somme jusqu'à l'échéance.", "La somme est immobilisée."),
        ("La loi interdit les minimums sous cinq pour cent.", "Les minimums sous cinq pour cent sont interdits."),
    ], corrige=True,
       notes="Faire écrire au tableau plutôt qu'à l'oral : toute la difficulté est dans "
             "l'accord, et il ne s'entend pas.")

    d.tableau('Lecture', "Ce que le document écrit, ce qu'on dirait",
              ['Écrit au passif', 'Dit à la voix active'],
              [["l'argent est immobilisé", "vous ne pouvez pas le reprendre"],
               ['la cotisation est déduite', 'vous déduisez la cotisation'],
               ['des frais seront exigés', 'quelqu\'un vous demandera des frais'],
               ['le plafond est fixé', 'le fédéral fixe le plafond']],
              cle=0,
              notes="Diapositive à photographier. Faire remarquer la troisième ligne : "
                    "c'est celle où le passif cache une information utile.")

    d.piege('Le piège', "écrire toute sa lettre au passif pour faire sérieux",
            "revenir à « je » dans sa propre lettre",
            "Un texte tout au passif devient impossible à discuter : on ne sait plus "
            "qui fait quoi. Dans une réclamation, c'est le contraire de ce qu'on veut. "
            "« Je conteste cette opération » est plus fort que « la contestation de "
            "cette opération est demandée ».",
            notes="Annonce la lettre du bloc E. Le dire : on apprend le passif pour "
                  "lire, pas pour écrire.")

    d.billet("Trouve dans le document une phrase au passif et récris-la à la voix "
             "active.",
             exemples=["Les dépôts sont protégés par l'Autorité.",
                       "L'Autorité protège les dépôts."],
             notes="Trois minutes. Le document de C2 en contient une douzaine : "
                   "n'importe laquelle fait l'affaire.")

    return d.save(dossier)
