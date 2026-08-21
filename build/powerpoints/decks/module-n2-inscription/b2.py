# -*- coding: utf-8 -*-
"""B2 · Le 7 septembre, pas le 9 juillet.
Bloc B « Défi 1 · La petite annonce » · couleur ambre · 75 min.
Source : exercices `t1date` et `t1notes`, mini-leçons `t1date` et `t1notes`,
dialogue `t1b`.

La séance d'écriture du défi 1, et c'est la seconde moitié de l'intention du
programme : prendre les renseignements en note. On n'écrit pas l'annonce, on
écrit quatre lignes.

Le savoir du programme est explicite ici — « comprendre les différentes façons
de présenter une date abrégée ». Trois écritures pour le même jour, et une
seule chose qui ne bouge jamais : le mois est au milieu.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-inscription/images/')


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Le 7 septembre, pas le 9 juillet",
        chapeau="Lire une date écrite en chiffres, puis prendre une annonce "
                "en note en quatre lignes.",
        duree='75 minutes')

    d.titre(notes="Séance d'écriture. Prévoir du papier et un crayon pour chacun dès le "
                  "début : la moitié de la séance se passe à écrire, pas à écouter.")

    d.objectifs([
        "lire une date écrite avec des barres ou des traits ;",
        "nommer les douze mois dans l'ordre ;",
        "écrire sa date de naissance dans la forme des formulaires ;",
        "prendre une annonce en note en quatre lignes.",
    ])

    d.declencheur(
        'Observation', "07/09/2026 — c'est quel jour ?",
        pistes=[
            "Est-ce que c'est en juillet ou en septembre ?",
            "Comment on fait pour être sûr ?",
            "Quel nombre ne dépasse jamais 12 ?",
            "Et dans votre pays, on écrit comment ?",
        ],
        notes="Le groupe se sépare toujours en deux sur la première piste, et c'est "
              "exactement le but. La quatrième ouvre une discussion utile : plusieurs "
              "pays écrivent le mois en premier.")

    d.tableau('Analyse', "Trois écritures, un seul jour",
              ["Comment c'est écrit", "Comment ça se lit"],
              [["le 7 septembre 2026", "en toutes lettres — la plus claire"],
               ["07/09/2026", "jour, mois, année — les reçus"],
               ["2026-09-07", "année, mois, jour — les formulaires"],
               ["Le nombre du milieu", "c'est toujours le mois"]],
              cle=1,
              note="Le mois ne dépasse jamais 12. C'est le seul repère nécessaire.",
              notes="Diapositive à photographier. Faire écrire la date du jour dans les "
                    "trois formes, sur une seule ligne du cahier.")

    d.piege('Le piège du jour',
            "« 07/09, c'est le 9 juillet »",
            "c'est le 7 septembre",
            "Dans cette écriture, au Québec, le premier nombre est le <b>jour</b> et le "
            "deuxième est le <b>mois</b>. C'est l'inverse de l'habitude américaine, et "
            "l'erreur coûte deux mois : on se présente le mauvais jour, à la mauvaise "
            "saison.",
            notes="Écrire les deux lectures au tableau, l'une sous l'autre, et laisser "
                  "le groupe trancher avant de donner la réponse.")

    d.tableau('Analyse', "Les douze mois et leur numéro",
              ["01 à 06", "07 à 12"],
              [["janvier, février, mars", "juillet, août, septembre"],
               ["avril, mai, juin", "octobre, novembre, décembre"],
               ["pas de majuscule", "pas de majuscule non plus"]],
              cle=0,
              note="On écrit le 7 septembre, jamais « le 7 Septembre ».",
              notes="Diapositive à photographier. Les faire réciter en chœur trois fois "
                    "dans la séance : la liste doit être automatique.")

    d.pratique('Pratique', "Écrivez le mois",
               "Lisez la date, puis écrivez le mois en lettres.", [
        ("07/09/2026", "le 7 septembre 2026"),
        ("2026-12-11", "le 11 décembre 2026"),
        ("24/08/2026", "le 24 août 2026"),
        ("1994-03-07", "le 7 mars 1994"),
        ("05/01/2027", "le 5 janvier 2027"),
        ("2026-10-02", "le 2 octobre 2026"),
    ], corrige=True, cols=2,
       notes="Six dates. Faire dire la date à voix haute avant de l'écrire : l'erreur "
             "s'entend avant de se voir.")

    d.regle("Prendre en note, c'est écrire quatre choses",
            "Quoi, quand, à quelle heure, où. Rien d'autre.",
            precision="On ne recopie jamais une annonce : personne ne relit un "
                      "paragraphe. Quatre lignes se relisent en dix secondes, dans "
                      "l'autobus. Et les chiffres se copient <b>en regardant</b> "
                      "l'annonce, jamais de mémoire.",
            notes="Diapositive à photographier. C'est la stratégie centrale du défi 1, "
                  "et elle vaut pour toutes les situations écrites du niveau.")

    d.dialogue('Dialogue', "Ce que l'annonce ne disait pas", [
        ("YARA", "L'inscription, c'est quel jour ?", True),
        ("MME BOURGEOIS", "Du 24 au 28 août, de 9 h à 15 h.", True),
        ("YARA", "Du 24 au 28 août. Et c'est où ?", True),
        ("MME BOURGEOIS", "Au local 005, au rez-de-chaussée.", True),
        ("YARA", "J'apporte quelque chose ?", True),
        ("MME BOURGEOIS", "Une pièce d'identité. C'est tout.", True),
    ], consigne="Écoutez, puis dites ce que Yara écrit pendant l'appel.",
       notes="Faire remarquer la deuxième réplique de Yara : elle redit la date avant "
             "de poser sa question suivante. C'est ce qui l'empêche de se tromper.")

    d.pratique('Production écrite', "Ma fiche de notes",
               "Quinze minutes. Quatre lignes, pas une de plus.", [
        ("Cours", "français, niveau 2"),
        ("Quand", "du 7 septembre au 11 décembre"),
        ("Heure", "de 8 h 30 à 12 h 30, du lundi au vendredi"),
        ("Où", "local 214 — inscription au local 005"),
    ], cols=1,
       notes="Faire écrire la fiche en regardant l'annonce projetée, puis relire une "
             "fois. Ramasser les fiches : les erreurs de chiffre se voient d'un coup "
             "d'œil et se corrigent en trente secondes.")

    d.billet(
        "Écrivez votre date de naissance dans les trois formes, sur une seule ligne.",
        exemples=[
            "le 7 mars 1994",
            "07/03/1994",
            "1994-03-07",
        ],
        notes="Devoir court, et le plus utile du module : c'est exactement ce qu'on "
              "leur demandera d'écrire dans une case, à la séance suivante.")

    return d.save(dossier)
