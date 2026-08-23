# -*- coding: utf-8 -*-
"""D1 · L'appel à l'Office, et la lettre qui en sort
Bloc D « Défi 3 · La lettre de réclamation » · couleur acier · compréhension
orale et écrite · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3lettre` (type `texte`, onze
passages cliquables).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="L'appel à l'Office, et la lettre qui en sort",
        chapeau="Une mise en demeure n'est pas une lettre de plainte : c'est "
                "un document dont la forme est convenue, et cette forme est "
                "ce qui lui donne son poids.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 3, et séance la plus dense du module : un "
                  "dialogue de vingt-cinq répliques et un document. Prévoir de couper "
                  "l'écoute en trois, et de garder la lettre pour la seconde heure.")

    d.objectifs([
        "comprendre ce qu'un organisme de renseignements fait et ne fait pas ;",
        "savoir ce qu'une mise en demeure doit contenir ;",
        "reconnaître les six parties de la lettre d'Ernestine ;",
        "employer cinq mots de la lettre.",
    ], notes="Le premier objectif est important et se dit en une phrase : l'Office "
             "renseigne, il ne règle pas le dossier à votre place. Beaucoup d'élèves "
             "croient l'inverse et sont déçus.")

    d.declencheur(
        'Mise en situation', "À qui téléphone-t-on quand un commerçant refuse ?",
        pistes=[
            "Existe-t-il un organisme public pour cela ?",
            "Que peut-il faire, et que ne peut-il pas faire ?",
            "Faut-il un avocat pour écrire une mise en demeure ?",
            "Combien coûte un appel de renseignements ?",
        ],
        notes="Les deux dernières réponses surprennent toujours : aucun avocat n'est "
              "nécessaire, et l'appel ne coûte rien. Le dire clairement, c'est le seul "
              "obstacle réel entre l'élève et son recours.")

    d.dialogue('Dialogue · 1 de 3', "Ce que l'Office peut dire", [
        ("ÉDITH", "Office de la protection du consommateur, Édith Vanasse, bonjour.", True),
        ("ÉDITH", "Je ne peux pas régler le dossier à votre place, mais je peux vous dire quelles règles s'appliquent.", True),
        ("ERNESTINE", "J'ai l'étiquette. Catégorie C.", True),
        ("ÉDITH", "Alors la garantie de bon fonctionnement est d'un mois ou de mille sept cents kilomètres. Vous étiez dedans ?", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="La deuxième réplique est celle qu'il faut retenir. La faire répéter : "
             "un organisme de renseignements renseigne, et c'est déjà beaucoup.")

    d.dialogue('Dialogue · 2 de 3', "La durée raisonnable", [
        ("ÉDITH", "Même si vous n'y étiez plus, la garantie légale ne se compte pas en jours.", True),
        ("ÉDITH", "Un bien doit servir pendant une durée raisonnable, compte tenu du prix payé.", True),
        ("ÉDITH", "Onze mille quatre cents dollars pour vingt-quatre jours, personne ne trouvera ça raisonnable.", True),
        ("ERNESTINE", "Ils m'ont dit que c'était de l'usure normale.", True),
    ], notes="La troisième réplique est le modèle de phrase du bloc D : le prix et la "
             "durée côte à côte, et rien d'autre. L'écrire au tableau et l'y laisser "
             "jusqu'à E2.")

    d.dialogue('Dialogue · 3 de 3', "Ce que la lettre doit contenir", [
        ("ÉDITH", "Vous envoyez une mise en demeure.", True),
        ("ERNESTINE", "C'est un avocat qui la fait ?", True),
        ("ÉDITH", "Pas du tout. C'est une lettre que vous écrivez vous-même. Elle raconte les faits, elle dit ce que vous demandez, elle accorde un délai.", True),
        ("ÉDITH", "Écrivez les faits, pas ce que vous ressentez. Une lettre qui donne des dates obtient une réponse.", True),
    ], notes="La dernière réplique est le critère de correction de E2. La citer telle "
             "quelle le jour de la production écrite : elle vient d'une agente de "
             "l'Office, pas de l'enseignante.")

    d.tableau('Analyse', "Les six parties de la lettre",
              ['La partie', 'Ce qu\'elle fait'],
              [["L'objet", "annonce le genre et le dossier, sans verbe"],
               ["Les faits", "l'achat, puis la panne, par ordre de dates"],
               ["Le droit", "la garantie invoquée, en deux phrases"],
               ["La demande", "une seule, avec « à vos frais »"],
               ["Le délai", "dix jours, à compter de la réception"],
               ["La suite", "annoncée au futur, jamais menacée"]],
              cle=0,
              notes="Diapositive à photographier, et à laisser affichée pendant la "
                    "lecture du document. C'est le plan de E2, donné trois séances "
                    "d'avance.")

    d.vocabulaire('Vocabulaire', "Cinq mots de la lettre", [
        ("une mise en demeure", "Une lettre qui expose des faits, formule une demande et accorde un délai."),
        ("un délai raisonnable", "Le temps accordé pour agir : dix jours, le plus souvent."),
        ("une pièce justificative", "Un papier daté qui prouve ce qu'on avance."),
        ("un accusé de réception", "Ce qui prouve la date à laquelle la lettre est arrivée."),
        ("la Division des petites créances", "Le tribunal où l'on réclame soi-même, jusqu'à 15 000 $."),
    ], notes="Préciser pour le quatrième : l'accusé de réception ne prouve pas ce "
             "qu'on a écrit, il prouve la date. Et c'est la date qui fait courir les "
             "dix jours.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'appel à l'Office.", [
        ("Madame Vanasse propose de régler le dossier à sa place.", "faux - elle renseigne, elle ne règle pas"),
        ("En catégorie C, la garantie dure un mois ou 1 700 km.", "vrai"),
        ("La garantie légale se compte en jours.", "faux - en durée raisonnable, vu le prix"),
        ("Une mise en demeure doit être rédigée par un avocat.", "faux - on l'écrit soi-même"),
        ("Le délai habituel est de dix jours.", "vrai"),
        ("Aux petites créances, la réclamation doit être de 15 000 $ ou moins.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le quatrième est "
             "celui qui libère : personne n'a besoin de payer pour écrire cette "
             "lettre-là.")

    d.billet(
        "Quelle est la seule demande que tu ferais, si c'était ton dossier ?",
        exemples=[
            "Réparer, remplacer ou rembourser : une seule.",
            "Une phrase, avec « à vos frais ».",
        ],
        notes="Trois minutes. Ces billets sont la demande de la lettre de E2. Ceux qui "
              "en écrivent deux montrent qu'il faut y revenir : deux demandes en font "
              "une négociation.")

    return d.save(dossier)
