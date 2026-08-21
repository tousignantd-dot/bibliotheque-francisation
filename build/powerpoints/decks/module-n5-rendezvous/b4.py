# -*- coding: utf-8 -*-
"""B4 · Sept lignes sur un papier.
Bloc B « Défi 1 » · couleur acier · 75 min. Compréhension orale et notes.
Source : exercices `t1fiche` et `t1phrases`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-rendezvous/images/')


def build(dossier):
    d = Deck(
        code='B4', section='acier',
        titre="Sept lignes sur un papier",
        chapeau="Un appel de trois minutes contient sept renseignements. "
                "À la fin, on en retient trois — et on est persuadé de les "
                "avoir tous les sept.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 1. Faire un test avant toute explication : "
                  "lire l'appel de Rachid à voix haute, une seule fois, sans prévenir. "
                  "Puis demander la date, l'heure et l'heure d'arrivée. Le résultat parle "
                  "de lui-même.")

    d.objectifs([
        "noter les sept renseignements d'un rendez-vous ;",
        "poser les trois questions que personne ne pose ;",
        "répéter la date et l'heure pour les faire confirmer ;",
        "reconnaître à quel moment de l'appel se dit chaque phrase.",
    ])

    d.declencheur(
        'Écoute', "Après l'appel : à quelle heure faut-il arriver, et qu'est-ce qu'il "
                  "faut apporter ?",
        image=IMG + 'appel-carnet.jpg',
        pistes=[
            "Qui a noté quelque chose pendant l'écoute ?",
            "Qui se souvient de l'heure exacte ?",
            "Et de l'heure d'arrivée, qui est différente ?",
            "Qu'est-ce qui aurait aidé ?",
        ],
        notes="Ne pas transformer ça en reproche : personne ne retient sept choses en "
              "écoutant et en préparant sa phrase suivante. C'est le propos de la séance.")

    d.regle("L'heure d'arrivée n'est pas l'heure du rendez-vous",
            "Quinze minutes avant, souvent trente pour un premier rendez-vous.",
            precision="Ces minutes servent à l'inscription : la carte, le dossier, la "
                      "salle d'attente. Arriver à l'heure exacte, c'est arriver en retard "
                      "— le rendez-vous commence tard et finit quand même à l'heure.",
            notes="Diapositive à photographier. C'est la ligne que les élèves oublient le "
                  "plus souvent, et celle qui coûte un rendez-vous entier.")

    d.cartes("La fiche du rendez-vous", "Sept lignes, écrites d'avance", [
        ("1 · La date", "Le jour et la date, écrits en toutes lettres."),
        ("2 · L'heure du rendez-vous", "Celle qui est au dossier de la clinique."),
        ("3 · Avec qui", "Le nom du médecin ou du professionnel."),
        ("4 · Où", "L'adresse, l'étage, parfois le numéro de porte."),
        ("5 · L'heure d'arrivée", "Presque jamais la même que la ligne 2."),
        ("6 · Ce qu'il faut apporter", "La carte, la liste des médicaments, un papier."),
    ], cols=3,
       notes="La septième ligne — le délai d'annulation — a sa propre diapositive. "
             "L'annoncer maintenant.")

    d.regle("Le délai d'annulation se demande le jour où tout va bien",
            "« Et si je ne peux plus venir ? »",
            precision="Personne ne vous donnera cette information de lui-même. Vingt-quatre "
                      "heures dans la plupart des cliniques, quarante-huit dans certaines. "
                      "On la note le jour où l'on prend le rendez-vous, pas le jour où "
                      "l'on doit annuler.",
            notes="Deuxième diapositive à photographier de la séance. Elle prépare "
                  "directement le défi 3.")

    d.tableau('Trois questions que personne ne pose', "Et ce qu'elles rapportent",
              ['La question', 'Ce qu\'on apprend'],
              [["À quelle heure faut-il arriver ?", "quinze ou trente minutes avant"],
               ["Est-ce que je dois apporter quelque chose ?", "carte, médicaments, papiers"],
               ["Est-ce que je dois être à jeun ?", "non ici, oui pour bien des prises de sang"],
               ["Et si je ne peux plus venir ?", "le délai, et les frais"]],
              cle=0,
              notes="Faire apprendre les quatre phrases telles quelles : elles se "
                    "réemploient dans n'importe quelle clinique, sans rien changer.")

    # `capture` n'existe que dans theme.Deck : les présentations la portent, les
    # fiches imprimées non (build/powerpoints/fiche.py n'a pas la méthode). Une
    # fiche noir et blanc n'a de toute façon rien à faire d'une capture d'écran.
    if hasattr(d, 'capture'):
        d.capture('t1phrases', "La phrase et le moment de l'appel",
                  consigne="Choisissez une phrase, puis le moment de l'appel où elle se dit.",
                  notes="Projeter, faire placer deux phrases à l'oral en groupe, puis laisser "
                        "chacun finir à l'écran.")

    d.piege("Remercier avant d'avoir tout noté",
            "« Merci beaucoup, bonne journée ! » — et la fiche a trois lignes vides.",
            "« Un instant… l'heure d'arrivée, c'est bien seize heures quarante-cinq ? »",
            "Le remerciement ferme l'appel : après lui, on ne peut plus poser de question "
            "sans rappeler. Tant qu'une ligne de la fiche est vide, on ne remercie pas.",
            notes="Faire pratiquer la phrase « un instant, je prends une feuille » à voix "
                  "haute. Beaucoup d'élèves n'osent pas la dire.")

    d.pratique('Compréhension', "La phrase et le moment de l'appel",
               "À quel moment de l'appel chaque phrase se dit-elle ?", [
        ("« J'aimerais prendre un rendez-vous, s'il vous plaît. »", "dire ce qu'on veut"),
        ("« Rachid Benali, B, E, N, A, L, I. »", "s'identifier et épeler"),
        ("« J'ai des étourdissements depuis trois mois. »", "donner le motif"),
        ("« Je finis à seize heures. »", "expliquer sa contrainte"),
        ("« Est-ce que je dois apporter quelque chose ? »", "poser ses questions"),
        ("« Jeudi 19 juin, dix-sept heures. C'est bien ça ? »", "répéter pour confirmer"),
    ], corrige=True,
       notes="Faire dire chaque phrase à voix haute avec l'intonation du moment : la "
             "dernière monte à la fin, les autres non.")

    d.billet(
        "Dessinez votre fiche de rendez-vous : sept lignes, vides, sur une demi-page.",
        exemples=[
            "Gardez-la dans votre portefeuille ou photographiez-la.",
            "Vous la remplirez pour de vrai au prochain appel — et pendant E1.",
        ],
        notes="Objet concret et réutilisable. Ceux qui la font vraiment reviennent en E1 "
              "avec un appel nettement meilleur.")

    return d.save(dossier)
