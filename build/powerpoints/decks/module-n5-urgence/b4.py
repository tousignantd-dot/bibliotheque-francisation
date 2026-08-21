# -*- coding: utf-8 -*-
"""B4 · « Couvrez-la » ou « ne la couvrez pas » — la place du pronom.
Bloc B « Défi 1 » · couleur ambre · 75 min. Écriture.
Source : exercice `t1pron` et sa mini-leçon.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-urgence/images/')


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="« Couvrez-la » ou « ne la couvrez pas »",
        chapeau="C'est la seule construction du français où le pronom passe "
                "derrière le verbe. Et c'est justement celle qu'on entend "
                "dans un appel d'urgence, dix fois en trois minutes.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 1. Relire deux billets de B3 et y ajouter les "
                  "pronoms au tableau : c'est la meilleure entrée en matière possible.")

    d.objectifs([
        "choisir entre le, la, les et lui, leur ;",
        "placer le pronom après le verbe à l'affirmatif, avant au négatif ;",
        "employer moi à l'affirmatif et me au négatif ;",
        "comprendre un ordre à pronom sans le faire répéter.",
    ])

    d.declencheur(
        'Observation', "« Couvrez-la. » / « Ne la couvrez pas. » Le même pronom, "
                       "deux places. Qu'est-ce qui décide ?",
        pistes=[
            "Quelle est la seule différence entre les deux phrases ?",
            "Où se place le pronom dans une phrase ordinaire ?",
            "Pourquoi un trait d'union dans la première ?",
            "Que devient « moi » à la forme négative ?",
        ],
        notes="La deuxième piste donne la clé : la place normale est devant le verbe. "
              "L'affirmatif de l'impératif est l'exception, pas la règle.")

    d.regle("Affirmatif : le pronom suit. Négatif : le pronom précède.",
            "Couvrez-la. · Ne la couvrez pas.",
            precision="À l'affirmatif, le pronom se colle au verbe par un trait d'union, "
                      "et « me » devient « moi ». Au négatif, tout reprend la place "
                      "ordinaire, entre le ne et le verbe.",
            notes="Diapositive à photographier. Deux phrases suffisent : ne pas ajouter "
                  "de cas rares, ils viendront au niveau 6.")

    d.tableau('Choisir le bon pronom', "C'est la préposition qui décide",
              ['Le verbe', 'Sans « à »', 'Avec « à »'],
              [["couvrir quelqu'un", "je la couvre", "—"],
               ["parler à quelqu'un", "—", "je lui parle"],
               ["déplacer quelqu'un", "je la déplace", "—"],
               ["donner qqch à quelqu'un", "je le donne", "je lui donne"],
               ["attendre quelqu'un", "je les attends", "—"]],
              cle=0,
              note="Le test se fait avec le verbe seul : parler À quelqu'un, couvrir quelqu'un.",
              notes="Insister : ce n'est pas le sens qui décide, c'est le verbe et sa "
                    "préposition. Les apprendre ensemble dès le premier jour.")

    d.cartes("Les quatre phrases de l'appel", "À reconnaître à l'oreille", [
        ("Couvrez-la.", "affirmatif · objet direct · trait d'union"),
        ("Ne la déplacez pas.", "négatif · objet direct · devant le verbe"),
        ("Parlez-lui.", "affirmatif · objet indirect · verbe + à"),
        ("Ne lui donnez rien.", "négatif · objet indirect · devant le verbe"),
        ("Écoutez-moi bien.", "affirmatif · me devient moi"),
        ("Ne me faites pas répéter.", "négatif · moi redevient me"),
    ], cols=3,
       notes="Faire dire chaque paire en alternance, dix fois. C'est le va-et-vient qui "
             "installe la règle, pas la règle elle-même.")

    d.pratique('Transformation', "Remplacez par un pronom",
               "À l'oral d'abord, puis à l'écrit.", [
        ("Couvrez votre mère. donne Couvrez-___.", "la"),
        ("Ne déplacez pas votre mère. donne Ne ___ déplacez pas.", "la"),
        ("Parlez à votre mère. donne Parlez-___.", "lui"),
        ("Ne donnez rien à votre mère. donne Ne ___ donnez rien.", "lui"),
        ("Écoutez-___ bien. (moi / me)", "moi"),
        ("Ne ___ faites pas répéter. (moi / me)", "me"),
        ("Prenez les médicaments. donne Prenez-___.", "les"),
        ("N'attendez pas les ambulanciers en haut. donne Ne ___ attendez pas en haut.", "les"),
    ], corrige=True,
       notes="Les deux dernières introduisent le pluriel sans le nommer : il ne pose "
             "presque jamais de problème une fois le singulier acquis.")

    d.piege("Garder « moi » à la forme négative",
            "Ne moi faites pas répéter.",
            "Ne me faites pas répéter.",
            "« Moi » ne s'emploie qu'après le verbe, à l'affirmatif. Devant le verbe, "
            "c'est toujours « me ».",
            notes="Erreur logique : l'élève applique la forme qu'il vient d'apprendre. "
                  "La montrer comme une conséquence, pas comme une faute d'inattention.")

    d.piege("Oublier le trait d'union",
            "Couvrez la avec une couverture.",
            "Couvrez-la avec une couverture.",
            "Sans trait d'union, « la » devient un article et la phrase attend un nom. "
            "À l'écrit, le lecteur s'arrête ; à l'oral, on ne l'entend pas — d'où "
            "l'importance de l'écrire correctement.",
            notes="Petit point d'orthographe, mais il tombe en évaluation de fin de cours.")

    d.pratique('Compréhension', "Qu'est-ce qu'on vous demande de faire ?",
               "Redites l'ordre entendu avec « je ».", [
        ("Couvrez-la.", "je la couvre"),
        ("Ne la faites pas asseoir.", "je ne la fais pas asseoir"),
        ("Parlez-lui, dites-lui que l'aide s'en vient.", "je lui parle, je lui dis que…"),
        ("Ne lui donnez rien à boire.", "je ne lui donne rien"),
        ("Dites-le-moi si elle change.", "je vous le dis si elle change"),
    ], corrige=True,
       notes="La dernière contient deux pronoms. La donner comme un bonus : elle "
             "s'entend souvent, et elle rassure les élèves rapides.")

    d.billet(
        "Récrivez trois ordres du défi 1 en remplaçant le nom par un pronom.",
        exemples=[
            "Un à l'affirmatif, un au négatif, un avec « moi » ou « me ».",
            "Vérifiez le trait d'union.",
        ],
        notes="Fin du bloc B. Annoncer le bloc C : l'ambulance est partie, on arrive à "
              "l'urgence, et là il faudra enfin raconter toute l'histoire.")

    return d.save(dossier)
