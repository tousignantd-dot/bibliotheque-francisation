# -*- coding: utf-8 -*-
"""C1 · Deux offres au babillard.
Bloc C « Défi 2 · L'annonce dit quoi ? » · couleur acier · 75 min.
Source du module : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Deux offres au babillard',
        chapeau="Fanta rapporte deux annonces prises à l'épicerie. Une seule "
                "lui convient, et ce n'est pas celle qui paie le mieux : "
                "c'est celle dont l'horaire est possible.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2. Si des élèves ont rapporté de vraies annonces "
                  "du quartier, les lire avant celles du dialogue : elles auront plus "
                  "d'effet.")

    d.objectifs([
        "suivre la lecture de deux offres d'emploi ;",
        "comprendre « de l'heure », « par semaine », « temps partiel » ;",
        "comparer deux offres et dire laquelle convient ;",
        "écarter une offre pour une bonne raison.",
    ])

    d.declencheur(
        'Décision', "Deux offres. Qu'est-ce qui vous fait choisir ?",
        pistes=[
            "Le salaire ? L'horaire ? La distance ?",
            "Qu'est-ce qui est impossible pour vous ?",
            "Est-ce qu'un bon salaire vaut un mauvais horaire ?",
            "Qu'est-ce que vous regarderiez en premier ?",
        ],
        notes="Faire voter à main levée sur le premier critère regardé. Le vote sera "
              "repris à la fin de la séance : il change souvent.")

    d.dialogue('Dialogue · 1 de 3', "Vingt heures par semaine", [
        ("SYLVIE", "Alors, la boulangerie ? Il vous a rappelée ?", True),
        ("FANTA", "Pas encore. Mais j'ai pris deux annonces au babillard de l'épicerie.", True),
        ("SYLVIE", "Montrez-moi. On va les lire ensemble. La première dit quoi ?", True),
        ("FANTA", "« Préposée à l'entretien. Vingt heures par semaine. Le soir. »", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Fanta ne s'arrête pas à un seul commerce : elle a continué à chercher. "
             "Le faire remarquer, c'est déjà une leçon de méthode.")

    d.dialogue('Dialogue · 2 de 3', "Seize dollars cinquante de l'heure", [
        ("SYLVIE", "Vingt heures, c'est du temps partiel. Et le salaire ?", True),
        ("FANTA", "« Seize dollars cinquante de l'heure. » Ça veut dire quoi, « de l'heure » ?", True),
        ("SYLVIE", "Que vous recevez seize dollars cinquante pour chaque heure travaillée.", True),
        ("FANTA", "Alors vingt heures, ça fait trois cent trente dollars par semaine.", True),
    ], notes="Le calcul est fait par Fanta elle-même. Le refaire au tableau avec le "
             "groupe : 16,50 fois 20. C'est le cœur de la séance C3.")

    d.dialogue('Dialogue · 3 de 3', "Demandez Hugo Pelletier", [
        ("SYLVIE", "Et l'horaire du soir, ça vous convient ?", True),
        ("FANTA", "Non. Mes enfants sont à la maison le soir. Je cherche le jour.", True),
        ("FANTA", "« Centre Léo-Bourdon. Aide à la cuisine, de neuf heures à une heure, du mardi au samedi. »", True),
        ("SYLVIE", "Alors c'est celle-là qu'il faut essayer. Demandez Hugo Pelletier.", True),
    ], notes="Écarter une offre est une décision, pas un échec. Insister : Fanta donne "
             "une raison précise, et elle passe à la suivante le jour même.")

    d.tableau('Analyse', "Les deux offres, ligne par ligne",
              ['', "Première offre", "Deuxième offre"],
              [["Le poste", "préposée à l'entretien", "aide à la cuisine"],
               ["Les heures", "20 h par semaine", "20 h par semaine"],
               ["Quand", "le soir", "de 9 h à 13 h, mardi au samedi"],
               ["Expérience", "non dit", "aucune exigée, formation sur place"],
               ["Pour Fanta", "impossible : les enfants", "possible"]],
              cle=0,
              note="Même nombre d'heures, et une seule des deux est possible.",
              notes="Diapo à photographier. Elle montre qu'une offre se juge sur "
                    "l'ensemble, pas sur le seul salaire.")

    d.regle("Une offre qu'on lit mal, c'est un matin perdu",
            "On lit les six lignes avant de se déplacer.",
            precision="Le poste, les heures, l'horaire, le salaire, l'expérience "
                      "demandée, à qui s'adresser. Six renseignements, et chacun peut "
                      "décider à lui seul que l'offre ne convient pas.",
            notes="Diapo à photographier. Elle annonce la séance C2, qui reprend les "
                  "six lignes une à une.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("La première offre est un poste d'entretien.", "vrai"),
        ("Vingt heures par semaine, c'est du temps plein.", "faux — temps partiel"),
        ("Le salaire est de 16,50 $ de l'heure.", "vrai"),
        ("Fanta écarte la première offre à cause de l'horaire.", "vrai"),
        ("La deuxième offre demande deux ans d'expérience.", "faux — aucune"),
        ("Il faut demander Hugo Pelletier.", "vrai"),
    ], corrige=True,
       notes="Mêmes énoncés que l'exercice t2vf du module. Faire justifier chaque "
             "« faux » par la ligne exacte de l'annonce.")

    d.pratique('Oral', "Deux par deux : laquelle choisiriez-vous ?",
               "Chacun choisit une offre et donne sa raison en une phrase.", [
        ("La phrase attendue", "Je choisis la deuxième, parce que…"),
        ("Une raison d'horaire", "Le soir, je ne peux pas : …"),
        ("Une raison d'expérience", "Aucune expérience exigée, alors je peux…"),
    ], notes="Dix minutes. Reprendre ensuite le vote du début : le premier critère a-t-il "
             "changé ?")

    d.billet(
        "Écrivez une raison d'écarter une offre.",
        exemples=[
            "Une phrase : « Je ne peux pas le soir, parce que… »",
            "Une raison vraie, la vôtre.",
        ],
        notes="Deux minutes. Ces raisons servent en E1 : savoir dire non poliment fait "
              "partie de la production orale.")

    return d.save(dossier)
