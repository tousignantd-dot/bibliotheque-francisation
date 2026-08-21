# -*- coding: utf-8 -*-
"""B1 · L'annonce sur le babillard.
Bloc B « Défi 1 · La petite annonce » · couleur acier · 75 min.
Source : dialogue `t1`, exercices `t1vf` et `t1annonce`, mini-leçon `t1heure`.

C'est la première des deux intentions du programme, et elle est en
compréhension écrite : repérer des renseignements sur un cours dans une
petite annonce. Le texte est court, la difficulté est ailleurs — tout ce qui
compte est écrit en chiffres, et les chiffres ne se devinent pas au contexte.

Le point de langue est le groupe prépositionnel de temps : à pour une heure,
de… à pour une durée, du… au pour deux dates. Trois mots, et toute la ligne
d'horaire de l'annonce s'ouvre.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-inscription/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="L'annonce sur le babillard",
        chapeau="Trouver dans une petite annonce ce qu'on cherche vraiment : "
                "quoi, quand, à quelle heure, où.",
        duree='75 minutes')

    d.titre(notes="Apporter de vraies annonces : celles du babillard du centre, de "
                  "l'épicerie du coin, de la bibliothèque de quartier. Le module marche "
                  "beaucoup mieux avec du papier réel dans les mains.")

    d.objectifs([
        "trouver la date, l'heure et le lieu dans une annonce ;",
        "employer à, de… à, du… au ;",
        "dire un horaire de cours à voix haute ;",
        "poser la question quand l'annonce ne dit pas tout.",
    ])

    d.declencheur(
        'Observation', "Vous voyez cette annonce. Qu'est-ce que vous cherchez en premier ?",
        pistes=[
            "Est-ce que vous lisez tout ?",
            "Qu'est-ce que vous regardez d'abord ?",
            "Qu'est-ce qui manque le plus souvent ?",
            "Qu'est-ce que vous faites si le papier ne le dit pas ?",
        ],
        notes="La deuxième piste porte la séance : personne ne lit une annonce en "
              "entier. On y cherche quatre choses, et le reste ne sert à rien.")

    d.dialogue('Dialogue', "Marco montre le papier à Yara", [
        ("MARCO", "Yara, regarde ce papier. C'est pour toi.", True),
        ("YARA", "C'est quoi ?", True),
        ("MARCO", "Une annonce. Un cours de français, au Centre Delorme.", True),
        ("YARA", "Ça commence quand ?", True),
        ("MARCO", "Le 7 septembre. Et ça finit le 11 décembre.", True),
        ("YARA", "Et c'est à quelle heure ?", True),
    ], consigne="Écoutez, puis comptez les questions de Yara.",
       notes="Trois questions en six répliques : c'est quoi, ça commence quand, c'est à "
             "quelle heure. Faire compter par le groupe — c'est le plan de leur propre "
             "prise de notes.")

    d.tableau('Analyse', "L'annonce du Centre Delorme",
              ["Ce qui est écrit", "Ce que ça veut dire"],
              [["Cours de français, niveau 2", "le groupe du matin"],
               ["Du 7 septembre au 11 décembre", "trois mois de cours"],
               ["Du lundi au vendredi, 8 h 30 à 12 h 30", "cinq matins par semaine"],
               ["Local 214, deuxième étage", "où on va le premier jour"]],
              cle=0,
              note="Quatre lignes. Tout le reste de l'annonce est du décor.",
              notes="Diapositive à photographier. C'est le texte de compréhension écrite "
                    "du défi : le laisser affiché pendant tout l'exercice suivant.")

    d.tableau('Analyse · suite', "Et l'inscription, elle, se passe ailleurs",
              ["Ce qui est écrit", "Ce que ça veut dire"],
              [["Inscription du 24 au 28 août", "avant le début du cours"],
               ["De 9 h à 15 h", "les heures d'ouverture du bureau"],
               ["Local 005", "le secrétariat, au rez-de-chaussée"],
               ["Apporter une pièce d'identité", "sans elle, on repart"]],
              cle=0,
              note="Deux locaux, deux dates : celles du cours et celles de l'inscription.",
              notes="Diapositive à photographier. Le tableau a été coupé en deux : six "
                    "rangées ne tiennent pas sur une diapositive projetée. La coupure "
                    "sert aussi le sens — le cours d'un côté, la démarche de l'autre.")

    d.regle("À, de… à, du… au",
            "Trois petits mots portent toute la ligne d'horaire.",
            precision="<b>À</b> pour une seule heure : le cours commence <b>à</b> "
                      "8 h 30. <b>De… à</b> pour une durée : <b>de</b> 8 h 30 <b>à</b> "
                      "12 h 30. <b>Du… au</b> pour deux jours ou deux dates : <b>du</b> "
                      "lundi <b>au</b> vendredi, <b>du</b> 24 <b>au</b> 28 août.",
            notes="Diapositive à photographier. Écrire la ligne d'horaire de l'annonce "
                  "au tableau et l'entourer mot à mot : elle contient les trois emplois "
                  "d'un coup.")

    d.pratique('Compréhension écrite', "Vrai ou faux, d'après l'annonce ?",
               "Relisez le tableau, puis répondez.", [
        ("Le cours finit le 11 décembre.", "vrai"),
        ("Le cours est le samedi.", "faux - du lundi au vendredi"),
        ("Le cours dure quatre heures par jour.", "vrai - de 8 h 30 à 12 h 30"),
        ("On s'inscrit dans le local du cours.", "faux - au local 005, pas au 214"),
        ("Il faut apporter une pièce d'identité.", "vrai"),
    ], corrige=True, cols=1,
       notes="Le quatrième énoncé est celui qui fait tomber tout le monde la première "
             "fois. Le garder pour la fin et le faire relever dans le tableau.")

    d.pratique('Pratique · avec de vraies annonces', "Quatre choses, pas une de plus",
               "Vingt minutes, avec les annonces apportées en classe.", [
        ("Étape 1", "Chaque équipe reçoit une vraie annonce."),
        ("Étape 2", "Elle souligne quatre choses : quoi, quand, à quelle heure, où."),
        ("Étape 3", "Elle dit son annonce au groupe, en quatre phrases."),
        ("Étape 4", "Le groupe dit ce qui manque dans l'annonce."),
    ], cols=1,
       notes="L'étape 4 est la plus utile : beaucoup d'annonces réelles ne disent pas "
             "tout, et c'est précisément ce qui oblige à téléphoner — la séance B2.")

    d.billet(
        "Écrivez l'horaire de votre propre cours, en une phrase complète.",
        exemples=[
            "Mon cours est du lundi au vendredi.",
            "Il commence à 8 h 30.",
            "Il est de 8 h 30 à 12 h 30.",
        ],
        notes="Devoir court. Corriger surtout les trois prépositions : c'est le seul "
              "point de langue de la séance.")

    return d.save(dossier)
