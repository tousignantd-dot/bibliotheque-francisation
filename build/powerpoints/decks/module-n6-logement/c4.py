# -*- coding: utf-8 -*-
"""C4 · Ce qui était déjà fait, et ce qu'il faut qui se fasse
Bloc C « Défi 2 · L'avis et la réponse » · couleur ambre · 90 min.
Source : exercices `t2pqp` et `t2subj`, leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="Ce qui était déjà fait, et ce qu'il faut qui se fasse",
        chapeau="Deux temps de verbe pour un dossier : l'un place les faits "
                "les uns avant les autres, l'autre dit ce qu'on demande.",
        duree='90 minutes')

    d.titre(notes="Séance de grammaire dense. Deux points, deux demi-heures, et un "
                  "exercice interactif chacun. Ne pas chercher à tout couvrir en "
                  "profondeur : le plus-que-parfait est de compréhension, le "
                  "subjonctif de production.")

    d.objectifs([
        "comprendre qu'un plus-que-parfait place une action avant une "
        "autre ;",
        "le former avec l'auxiliaire à l'imparfait ;",
        "employer le subjonctif après « il faut que » et « je souhaite "
        "que » ;",
        "ne pas l'employer après « espérer que ».",
    ], notes="Le quatrième objectif est le piège du niveau. « Espérer » ressemble à "
             "« souhaiter » et ne se construit pas pareil : c'est une bizarrerie, il "
             "faut le dire comme telle.")

    d.declencheur(
        'Observation', "« Il a refusé parce qu'un locataire lui avait causé des ennuis. » Qu'est-ce qui est arrivé en premier ?",
        pistes=[
            "Est-ce l'ordre des mots qui le dit ?",
            "Qu'est-ce qui vous le fait comprendre, alors ?",
            "Que se passerait-il si les deux verbes étaient au passé composé ?",
        ],
        notes="Écrire la phrase au tableau avec les deux verbes au passé composé, puis "
              "avec le plus-que-parfait. La différence de sens saute aux yeux, et "
              "c'est tout ce que la première demi-heure doit établir.")

    d.tableau('Analyse', "Le plus-que-parfait, en une ligne",
              ['Comment', 'Exemple'],
              [["avoir à l'imparfait", "elle avait lu la page"],
               ["être à l'imparfait", "il était parti la veille"],
               ["ce qu'il dit", "c'était déjà fait avant"],
               ["les mots qui l'annoncent", "déjà, la veille, deux ans plus tôt"]],
              cle=0,
              notes="Diapositive à photographier. Si vous savez faire un passé composé, "
                    "vous savez faire un plus-que-parfait : il ne reste qu'à mettre "
                    "l'auxiliaire à l'imparfait. Le dire exactement ainsi.")

    d.pratique('Pratique', "Mettez le verbe au plus-que-parfait",
               "Les deux actions sont passées ; l'une est plus ancienne.", [
        ("Quand elle a remis son avis, elle … (lire) la page trois fois.", "avait lu"),
        ("Son cousin … (sous-louer) son logement deux ans plus tôt.", "avait sous-loué"),
        ("Il s'est méfié : un locataire lui … (causer) des ennuis.", "avait causé"),
        ("Le 29, il a écrit : il … (vérifier) le dossier la veille.", "avait vérifié"),
        ("Elle a pu prouver la date : elle … (faire) signer sa copie.", "avait fait"),
        ("Le délai finissait le 3 : il … (commencer) le 18.", "avait commencé"),
    ], corrige=True,
       notes="Faire dire à chaque fois laquelle des deux actions est la plus ancienne. "
             "C'est le sens qui se travaille, la forme suit.")

    d.regle("Après « il faut que », le verbe change",
            "Volonté, obligation, souhait : le subjonctif.",
            precision="« Il faut que vous répondiez par écrit. » Au moment où on le "
                      "dit, la réponse n'existe pas : elle est demandée. C'est le "
                      "temps de ce qui est visé et non constaté. Six formes "
                      "couvrent la moitié des cas : que je sois, que j'aie, que je "
                      "fasse, que j'aille, que je sache, que je puisse.",
            notes="Diapositive à photographier. Faire répéter les six formes à voix "
                  "haute, deux fois. Elles s'apprennent par la bouche, pas par la "
                  "règle.")

    d.cartes('Le piège', "Ce qui l'impose, ce qui ne l'impose pas", [
        ("Il faut que, je veux que", "Subjonctif, sans exception. « Il faut que Farida ait un nom avant d'écrire. » Rien n'est encore fait au moment où on parle."),
        ("J'exige que, je souhaite que", "Subjonctif aussi. « Il exige qu'on lui paie deux cents dollars » — la demande existe, le paiement non."),
        ("J'espère que", "Indicatif. « J'espère qu'il répondra avant le 3 décembre. » C'est la bizarrerie du français, et elle s'apprend telle quelle."),
        ("Je pense que, je vois que", "Indicatif également : ces verbes constatent ou prévoient. Le fait est posé comme réel, donc pas de subjonctif."),
    ], notes="Faire produire une phrase par carte, sur le dossier. Les phrases avec "
             "« il faut que » serviront directement dans le courriel de E2 : les "
             "meilleures vont au tableau.")

    d.pratique('Pratique', "Subjonctif ou indicatif ?",
               "Écrivez le verbe à la forme qui convient.", [
        ("Il faut que Farida … (avoir) un nom avant d'écrire.", "ait"),
        ("La loi exige que l'avis … (être) écrit.", "soit"),
        ("Il ne faut pas qu'un locataire … (partir) sans avertir.", "parte"),
        ("Elle veut que Nicolas … (savoir) qu'elle appellera ses références.", "sache"),
        ("Elle demande à monsieur Tardif de … (répondre) par écrit.", "répondre"),
        ("Elle espère qu'il … (répondre) avant le 3 décembre.", "répondra"),
    ], corrige=True,
       notes="Les deux dernières lignes sont le cœur de l'exercice : « de » commande "
             "l'infinitif, « espérer que » commande l'indicatif. Corriger lentement, "
             "et faire écrire les deux phrases au cahier.")

    d.billet(
        "Écrivez une phrase qui commence par « Il faut que vous… ».",
        exemples=[
            "Adressez-vous à un locateur.",
            "Attention à la forme du verbe.",
        ],
        notes="Deux minutes. Ramasser : les fautes de subjonctif se voient d'un coup "
              "d'œil et disent exactement qui aura besoin d'aide pour le courriel de "
              "E2.")

    return d.save(dossier)
