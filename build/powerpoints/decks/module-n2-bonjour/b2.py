# -*- coding: utf-8 -*-
"""B2 · Ma journée, au présent.
Bloc B « Défi 1 · Ça va ? Et toi ? » · couleur ambre · 75 min.
Source : dialogue `t1b`, exercices `t1verbes` et `t1repond`, mini-leçon `t1verbes`.

La séance qui répond à l'intention de production orale du programme :
« décrire ses activités quotidiennes ». Un seul temps — l'indicatif présent
—, une douzaine de verbes usuels, et les trois moments de la journée pour
les ranger.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-bonjour/images/')


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Ma journée, au présent",
        chapeau="Trois phrases suffisent pour répondre à « tu fais quoi de "
                "ta journée ? ».",
        duree='75 minutes')

    d.titre(notes="Séance de production. Chaque élève doit sortir d'ici avec trois "
                  "phrases vraies sur sa propre journée : ce sont celles qu'il dira en "
                  "E1, et elles doivent être à lui.")

    d.objectifs([
        "conjuguer les verbes en -er au présent ;",
        "employer aller, prendre, faire et dormir ;",
        "situer une activité dans la journée ;",
        "raconter sa journée en trois phrases.",
    ])

    d.declencheur(
        'Observation', "Que fait-on à ce moment-là ?",
        image=IMG + 'matin-dejeuner.jpg',
        pistes=[
            "Quelle heure est-il, à votre avis ?",
            "Que fait cette personne ?",
            "À quelle heure déjeunez-vous ?",
            "Que faites-vous juste après ?",
        ],
        notes="Laisser répondre en une phrase, même incomplète. Reprendre chaque réponse "
              "en phrase entière et la faire répéter : c'est le modèle de la séance.")

    d.dialogue('Dialogue · 1 de 2', "Tu fais quoi, le matin ?", [
        ("GILBERTE", "Tu es fatiguée, Nadia ?", True),
        ("NADIA", "Un peu. Ma journée est longue.", True),
        ("GILBERTE", "Tu fais quoi, le matin ?", True),
        ("NADIA", "Je déjeune à sept heures. Après, je marche jusqu'au centre.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire remarquer « après » : c'est le seul connecteur du niveau, et il "
             "suffit à enchaîner deux actions.")

    d.dialogue('Dialogue · 2 de 2', "Et l'après-midi ?", [
        ("GILBERTE", "Et l'après-midi ?", True),
        ("NADIA", "J'étudie à la maison. Le soir, je travaille.", True),
        ("GILBERTE", "Tu soupes à quelle heure ?", True),
        ("NADIA", "À neuf heures, avec ma sœur. Après, je dors !", True),
    ], notes="Quatre répliques, et toute une journée est racontée. Le faire compter au "
             "groupe : ils croient qu'il en faut vingt.")

    d.tableau('Analyse', "Les verbes en -er, au présent",
              ['La personne', 'La forme'],
              [["je", "je déjeun<b>e</b> · je travaill<b>e</b> · je march<b>e</b>"],
               ["tu", "tu déjeun<b>es</b> · tu travaill<b>es</b>"],
               ["vous", "vous déjeun<b>ez</b> · vous travaill<b>ez</b>"],
               ["à part", "aller : je vais · prendre : je prends · faire : je fais"]],
              cle=2,
              note="« je » et « tu » se disent pareil : le -s ne s'entend pas.",
              notes="Diapositive à photographier. Insister sur la dernière ligne : ces "
                    "trois verbes reviennent dans presque toutes les phrases.")

    d.vocabulaire('Vocabulaire', "Les verbes de la journée", [
        ("déjeuner", "Manger le premier repas, le matin."),
        ("travailler", "Faire un métier, dans un magasin ou un bureau."),
        ("étudier", "Apprendre, à l'école ou à la maison."),
        ("souper", "Manger le repas du soir."),
    ], notes="Diapositive à photographier. Au Québec : on déjeune le matin, on dîne le "
             "midi, on soupe le soir. Le dire clairement, plusieurs élèves connaissent "
             "l'autre usage.")

    d.regle("Devant une voyelle, « j' »",
            "« je » perd son e devant a, e, i, o, u.",
            precision="<b>j'</b>étudie, <b>j'</b>habite, <b>j'</b>arrive. On ne dit jamais "
                      "« je étudie ». Le h de « habite » ne compte pas : il ne se "
                      "prononce pas.",
            notes="Diapositive à photographier. Faire chercher par le groupe trois autres "
                  "verbes qui commencent par une voyelle.")

    d.pratique('Compréhension', "Complétez la journée de Nadia",
               "Écrivez le verbe au présent.", [
        ("Le matin, je ___ à sept heures. (déjeuner)", "déjeune"),
        ("Je ___ jusqu'au centre. (marcher)", "marche"),
        ("L'après-midi, j' ___ à la maison. (étudier)", "étudie"),
        ("Le soir, je ___ à la pharmacie. (travailler)", "travaille"),
        ("Samir ___ le métro. (prendre)", "prend"),
        ("Et toi, tu ___ au centre à pied ? (aller)", "vas"),
    ], corrige=True, cols=2,
       notes="Faire d'abord à l'oral. Les deux dernières lignes sont les plus difficiles : "
             "les garder pour la fin et les corriger ensemble.")

    d.pratique('Pratique · à deux', "Trois phrases vraies",
               "Deux par deux, chacun raconte sa vraie journée.", [
        ("Étape 1", "Écrivez trois phrases : le matin, l'après-midi, le soir."),
        ("Étape 2", "Dites-les à votre voisin, lentement."),
        ("Étape 3", "Votre voisin pose une question : « à quelle heure ? »"),
        ("Étape 4", "Changez de rôle."),
    ], cols=1,
       notes="Vingt-cinq minutes. Ramasser les trois phrases de chacun : elles servent "
             "de point de départ à la production orale de E1.")

    d.billet(
        "Écrivez votre journée en trois phrases.",
        exemples=[
            "Le matin, je déjeune à sept heures.",
            "L'après-midi, je viens au centre.",
            "Le soir, je soupe avec ma famille.",
        ],
        notes="Devoir court, à garder : c'est le brouillon de la production orale.")

    return d.save(dossier)
