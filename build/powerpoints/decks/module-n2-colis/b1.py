# -*- coding: utf-8 -*-
"""B1 · Les cinq lignes de l'adresse.
Bloc B « Défi 1 · J'écris l'adresse » · couleur acier · 75 min.
Source : dialogue `t1`, exercices `t1vf`, `t1adresse`, mini-leçon `t1adresse`.

« Adresser une enveloppe » est l'une des deux seules intentions que le
programme rattache à cette situation au niveau 2, et elle est en production
écrite. C'est donc la séance centrale du module : tout ce qui précède
prépare la main qui écrit ici.

L'ordre des lignes n'a rien d'universel. Beaucoup d'élèves viennent de pays
où l'adresse se lit de haut en bas dans l'autre sens, ou sans code postal.
"""
import os

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-colis/images/')


def _photo(nom):
    """La photo si elle est sur le disque, sinon rien. Voir `a1.py`."""
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Les cinq lignes de l'adresse",
        chapeau="Écrire une adresse du Québec sur une enveloppe : le nom, le "
                "numéro et la rue, la ville, la province, le code postal.",
        duree='75 minutes')

    d.titre(notes="Distribuer deux enveloppes vierges par élève dès l'entrée : une pour "
                  "l'essai, une pour la bonne copie. Toute la séance se fait le crayon à "
                  "la main.")

    d.objectifs([
        "mettre les cinq lignes d'une adresse dans le bon ordre ;",
        "écrire la province entre parenthèses ;",
        "placer le numéro d'appartement après la rue ;",
        "savoir où va le timbre et où va l'expéditeur.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qui est écrit sur une enveloppe ?",
        image=_photo('poste-enveloppe.jpg'),
        pistes=[
            "Combien de lignes voyez-vous ?",
            "Dans votre pays, l'adresse s'écrit-elle dans le même ordre ?",
            "Où est le timbre ?",
            "Qu'est-ce qu'il y a en haut, à gauche ?",
        ],
        notes="La deuxième question est celle qui fait parler. Laisser deux ou trois "
              "élèves décrire l'ordre de leur pays d'origine, au tableau si possible : "
              "la comparaison fixe l'ordre du Québec mieux qu'une règle.")

    d.dialogue('Dialogue · 1 de 2', "Karim prend le crayon", [
        ("AMARA", "Karim, je ne sais pas où écrire.", True),
        ("KARIM", "Regarde. Au milieu, tu écris le nom.", True),
        ("AMARA", "Ousmane Diallo. C'est mon frère.", True),
        ("KARIM", "Bien. En dessous, le numéro et la rue.", True),
        ("AMARA", "145, rue King Ouest, app. 6.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Karim Haddad est dans la même classe qu'Amara depuis deux ans. Faire "
             "remarquer qu'il ne fait pas le travail à sa place : il montre, elle écrit.")

    d.dialogue('Dialogue · 2 de 2', "La ville, la province, le code", [
        ("KARIM", "Parfait. Après, la ville et la province.", True),
        ("AMARA", "Sherbrooke, Québec.", True),
        ("KARIM", "Oui. Et le code postal à la fin.", True),
        ("AMARA", "J1H 1P4.", True),
        ("KARIM", "C'est bon. Ton enveloppe est prête.", True),
    ], notes="Faire écrire l'adresse complète au tableau, ligne par ligne, pendant qu'on "
             "réécoute. Les élèves recopient sur leur première enveloppe.")

    d.tableau('Analyse', "Une adresse du Québec, ligne par ligne",
              ['La ligne', 'Ce qu\'on y écrit'],
              [["1 — le nom", "Ousmane Diallo — le prénom, puis le nom de famille"],
               ["2 — le numéro et la rue", "145, rue King Ouest, app. 6"],
               ["3 — la ville et la province", "Sherbrooke (Québec)"],
               ["4 — le code postal", "J1H 1P4 — à la fin, toujours"]],
              cle=2,
              note="L'appartement vient après la rue, jamais devant le numéro.",
              notes="Diapositive à photographier. C'est la diapositive la plus importante "
                    "du module : la laisser affichée pendant toute la pratique.")

    d.regle("La province entre parenthèses",
            "Sherbrooke (Québec) J1H 1P4",
            precision="La ville d'abord, la province ensuite, entre parenthèses. Le code "
                      "postal se met sur la même ligne, après un espace, ou sur la ligne "
                      "en dessous. Les deux se font ; ce qui ne se fait pas, c'est de le "
                      "mettre avant la ville.",
            notes="Diapositive à photographier. Beaucoup d'élèves écrivent le code postal "
                  "en premier, comme dans leur pays. Le montrer sans le corriger comme "
                  "une faute : c'est un usage différent, pas une erreur.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Karim montre à Amara comment écrire l'adresse.", "vrai"),
        ("Le nom s'écrit au milieu de l'enveloppe.", "vrai"),
        ("Ousmane Diallo habite à Montréal.", "faux — à Sherbrooke"),
        ("Le numéro d'appartement est le 6.", "vrai"),
        ("Le code postal s'écrit avant la ville.", "faux — à la fin"),
    ], corrige=True, cols=1,
       notes="Les cinq mêmes énoncés sont dans le module en ligne, exercice `t1vf`. Les "
             "faire à l'oral d'abord.")

    d.pratique('Écriture', "Chaque ligne à sa place",
               "Complétez avec un seul mot.", [
        ("Sur la première ligne, on écrit le ___.", "nom"),
        ("Après le numéro, on écrit le nom de la ___.", "rue"),
        ("Le numéro d'appartement s'écrit ___ la rue.", "après"),
        ("La province s'écrit entre ___.", "parenthèses"),
        ("Le ___ postal vient à la fin.", "code"),
        ("On écrit Sherbrooke ___.", "(Québec)"),
    ], corrige=True, cols=2,
       notes="Les six mêmes phrases sont dans le module en ligne, exercice `t1adresse`. "
             "La mini-leçon du même nom reprend les quatre lignes une par une, avec "
             "l'audio.")

    d.pratique('Pratique · à deux', "L'enveloppe de mon voisin",
               "Deux par deux, avec la deuxième enveloppe.", [
        ("Étape 1", "Donnez votre adresse à votre voisin, à voix haute, ligne par ligne."),
        ("Étape 2", "Votre voisin l'écrit sur son enveloppe, sans la voir écrite."),
        ("Étape 3", "Vérifiez ensemble les quatre lignes et le code postal."),
        ("Étape 4", "Changez de rôle."),
    ], cols=1,
       notes="Vingt minutes. C'est l'exercice le plus utile du module : dicter son adresse "
             "sert au médecin, à la banque et au comptoir postal. Circuler et faire "
             "épeler les noms de rue difficiles.")

    d.billet(
        "Écrivez votre adresse complète, les quatre lignes.",
        exemples=[
            "Amara Diallo",
            "4520, rue Bélanger, app. 3",
            "Montréal (Québec) H1T 1C5",
        ],
        notes="Devoir court, et vrai : demander leur adresse à eux. La séance C1 s'en "
              "servira pour remplir le formulaire du colis.")

    return d.save(dossier)
