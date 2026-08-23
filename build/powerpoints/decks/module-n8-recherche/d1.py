# -*- coding: utf-8 -*-
"""D1 · Quarante-cinq minutes devant deux personnes
Bloc D « Défi 3 · L'entrevue devant le comité » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t31` et `t3irreel`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n8-recherche' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Raconter une erreur, et s'en sortir grandi",
        chapeau="Une entrevue se gagne rarement sur les bonnes réponses : "
                "elle se gagne sur ce qu'on dit avant qu'on vous le demande.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc D, et séance la plus délicate du module. Prévenir "
                  "que l'entrevue contient une question qu'un employeur n'a pas le "
                  "droit de poser : elle sera reprise en D2, pas ici.")

    d.objectifs([
        "répondre par un exemple daté et chiffré, jamais par une qualité ;",
        "raconter une erreur en trois temps, et finir par la règle qu'on applique depuis ;",
        "nommer soi-même l'objection que personne ne formule ;",
        "employer l'hypothèse irréelle : si j'avais..., j'aurais...",
    ], notes="Le deuxième et le quatrième vont ensemble : c'est l'irréel du passé qui "
             "permet de raconter une erreur sans se dévaloriser.")

    d.declencheur(
        'Discussion', "Raconteriez-vous une erreur en entrevue ?",
        image=IMG + 'table-comite.jpg',
        pistes=[
            "Qu'est-ce qu'on vous a conseillé de faire, d'habitude ?",
            "Qu'est-ce qu'un employeur apprend de quelqu'un qui n'a jamais eu tort ?",
            "Deux chaises d'un côté, une de l'autre : qu'est-ce que ça change ?",
            "Combien de temps dure une entrevue de ce genre ?",
        ],
        notes="Le conseil courant est « n'en parlez jamais ». Le module dit le "
              "contraire, sous une condition stricte : la règle qu'on en a tirée. "
              "Sans elle, c'est un aveu.")

    d.dialogue('Dialogue 1 de 4', "Un choix que personne n'avait fait", [
        ("DANIELLE", "Vous avez classé les trois problèmes dans un ordre que personne d'autre n'a proposé. Expliquez-nous.", True),
        ("SHIRIN", "J'ai commencé par la palette mal étiquetée plutôt que par la ligne arrêtée.", True),
        ("SHIRIN", "La ligne arrêtée coûte de l'argent chaque minute, mais elle est visible : tout le monde la voit et quelqu'un la traite.", True),
        ("SHIRIN", "Une palette mal étiquetée sort de l'usine et revient six semaines plus tard en rappel de produit.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer la structure : le choix, puis la raison, puis la "
             "conséquence évitée. Trois phrases, et l'ordre n'est pas discutable.")

    d.dialogue('Dialogue 2 de 4', "L'erreur, ce qu'elle a coûté, la règle", [
        ("RÉAL", "Vous avez déjà vécu un rappel ?", True),
        ("SHIRIN", "Un seul, en 2016. Nous avions expédié quatre cents caisses avec une date de péremption erronée. C'est moi qui avais approuvé l'étiquette.", True),
        ("SHIRIN", "Nous les avons toutes reprises. Ça nous a coûté onze jours de production.", True),
        ("SHIRIN", "Si j'avais fait vérifier l'étiquette par une deuxième personne, ce qui prenait quatre minutes, rien de tout cela ne serait arrivé. Depuis, aucune étiquette ne part sans deux signatures sur mes lignes.", True),
    ], notes="Le modèle de la séance, et il tient en quatre parties : la date, les "
             "chiffres, l'irréel du passé, la règle appliquée depuis. Retirer la "
             "dernière, et tout s'effondre.")

    d.dialogue('Dialogue 3 de 4', "L'objection, posée franchement", [
        ("RÉAL", "Votre dossier me pose une question que je vais vous poser franchement, parce que je préfère ça à me la poser tout seul après votre départ.", True),
        ("RÉAL", "Onze ans de supervision là-bas, cinq ans d'opératrice ici. Si vous étiez capable de superviser, pourquoi être restée cinq ans à exécuter ?", True),
        ("SHIRIN", "Parce que personne ne m'a proposé autre chose, et que je n'ai pas su le demander. Les trois premières années, je ne parlais pas assez bien français pour tenir une réunion.", True),
        ("SHIRIN", "La cinquième, j'ai compris que ça n'arriverait jamais tout seul. Je suis ici pour cette raison-là.", True),
    ], notes="Point délicat. Shirin n'accuse personne et ne s'excuse pas : elle "
             "explique. C'est la seule des deux voies qui laisse quelque chose "
             "derrière elle. Faire relever qu'aucun ancien employeur n'est nommé.")

    d.dialogue('Dialogue 4 de 4', "Ce qu'on demande, et ce qu'on offre", [
        ("DANIELLE", "L'échelle compte six échelons. Compte tenu de vos cinq années ici, nous vous situerions au deuxième.", True),
        ("SHIRIN", "J'aimerais qu'on regarde le quatrième, et je vais vous dire pourquoi plutôt que de me contenter de le demander.", True),
        ("SHIRIN", "Vous avez neuf personnes à recruter d'ici février. J'ai fait ce travail-là onze fois. Un échelon vaut environ deux mille dollars par année ; une erreur d'embauche en vaut vingt mille.", True),
        ("SHIRIN", "Je propose le troisième à l'embauche, et le quatrième après six mois si les neuf postes sont pourvus. Écrivez-le dans la lettre : si je n'y arrive pas, je reste au troisième.", True),
    ], notes="La négociation entière est là, et elle sera reprise en D2. Faire "
             "remarquer que Shirin chiffre ce que sa contrepartie vaut pour "
             "l'employeur, jamais ce que l'échelon vaut pour elle.")

    d.regle("Si plus plus-que-parfait, puis conditionnel passé",
            "Si j'avais fait vérifier l'étiquette, rien ne serait arrivé. "
            "Jamais de conditionnel après « si » : c'est la faute que le "
            "correcteur cherche en premier.",
            precision="Plus-que-parfait : avoir ou être à l'imparfait, plus le "
                      "participe. Conditionnel passé : avoir ou être au conditionnel, "
                      "plus le même participe. Un seul mot bouge entre les deux "
                      "moitiés de la phrase.",
            notes="Diapositive à photographier. Faire écrire les deux moitiés l'une "
                  "sous l'autre, et souligner l'auxiliaire dans chacune.")

    d.pratique('Pratique', "Complétez l'hypothèse irréelle",
               "Écrivez seulement le groupe verbal demandé.", [
        ("Si j'avais fait vérifier l'étiquette, rien ___ (arriver).", "ne serait arrivé"),
        ("Si nous ___ (avoir) une deuxième signature, les caisses seraient parties.", "avions eu"),
        ("Si le groupe n'avait pas racheté l'usine, le poste ___ (ne jamais exister).", "n'aurait jamais existé"),
        ("Si la ligne était restée arrêtée, nous ___ (perdre) la commande.", "aurions perdu"),
        ("Si vous m'aviez communiqué l'échelle, je ___ (préparer) une proposition.", "aurais préparé"),
        ("Si j'___ (savoir) que l'équipe n'existait pas, j'aurais posé la question.", "avais su"),
    ], corrige=True,
       notes="Écrire chaque réponse au tableau. La négation encadre l'auxiliaire : "
             "« n'aurait jamais existé », et « jamais » se place entre les deux.")

    d.billet(
        "Préparez le récit d'une décision difficile, en quatre parties.",
        exemples=[
            "La situation avec une date, ce que vous avez fait, le résultat avec un chiffre.",
            "Puis : si j'avais..., j'aurais... Et enfin : depuis, je...",
        ],
        notes="Devoir central du bloc. C'est ce récit-là qui sera enregistré en E1 : "
              "le préparer ici, à l'écrit, économise une séance.")

    return d.save(dossier)
