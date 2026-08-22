# -*- coding: utf-8 -*-
"""C2 · Lire l'avis sur la porte.
Bloc C « Défi 2 » · couleur ambre · 75 min. Dernière séance du défi.
Source : dialogue `t2b`, exercices `t2avis`, `t2imper` et `t2b`, mini-leçon
« Les consignes et les règlements du centre ».

C'est la séance de l'intention la plus précise du programme pour cette
situation : **lire un avis simple de l'établissement de formation**. Quatre
lignes collées sur une porte, une date, ce qui est fermé, une consigne, une
signature. Rien de plus, et c'est déjà beaucoup pour quelqu'un qui déchiffre.

Elle règle aussi les quatre mots du règlement que le lexique du programme
nomme : c'est permis, interdit, autorisé, possible. Ils reviennent partout,
bien au-delà du centre.
"""
import pathlib
from theme import Deck

IMG = (pathlib.Path(__file__).resolve().parents[4]
       / 'assets' / 'interactive' / 'module-n2-secretaire' / 'images')


def img(nom):
    """La photo si elle existe, sinon rien — voir a1.py."""
    chemin = IMG / (nom + '.jpg')
    return str(chemin) if chemin.exists() else None


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Lire l'avis sur la porte",
        chapeau="Trouver la date, ce qui est fermé et ce qu'il faut faire.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 2. Apporter en classe trois vrais avis "
                  "affichés dans le centre. Les élèves reconnaissent la forme avant de "
                  "connaître son nom, et ça suffit au niveau 2.")

    d.objectifs([
        "trouver la date dans un avis affiché ;",
        "dire ce qui est ouvert et ce qui est fermé ;",
        "lire une consigne écrite sans « vous » devant ;",
        "employer c'est permis, c'est interdit, je peux, je dois.",
    ])

    d.declencheur(
        'Observation', "Il y a un papier sur la porte. Que dit-il ?",
        image=img('lieu-avis'),
        pistes=[
            "Où est-ce que ce papier est collé ?",
            "Qu'est-ce qu'on cherche en premier quand on le lit ?",
            "À qui est-ce qu'il parle ?",
            "Qu'est-ce qu'on fait si un mot manque ?",
        ],
        notes="La deuxième piste est la bonne réponse de la séance : on cherche la "
              "date. Elle est presque toujours à la première ligne, et elle décide de "
              "tout le reste.")

    d.dialogue('Dialogue', "C'est un congé", [
        ("AMEL", "Monsieur Ouellet ! Il y a un papier sur la porte.", True),
        ("MARC", "Oui, c'est un avis. Vous savez lire ça ?", True),
        ("AMEL", "Je lis… « Lundi 13 octobre : le centre est fermé. »", True),
        ("MARC", "C'est ça. Lundi, c'est un congé.", True),
        ("AMEL", "Alors il n'y a pas de cours lundi ?", True),
        ("MARC", "Non. Pas de cours, et le secrétariat est fermé aussi.", True),
    ], consigne="Écoutez, puis dites la date que vous avez entendue.",
       notes="Faire écouter deux fois. Amel lit à voix haute avant de comprendre : "
             "c'est la bonne stratégie, et il faut la nommer.")

    d.tableau('Analyse · 1 de 2', "AVIS — Centre Sainte-Émilie",
              ["Ligne", "Ce qui est écrit"],
              [["1", "Lundi 13 octobre : le centre est fermé."],
               ["2", "Il n'y a pas de cours et le secrétariat est fermé."],
               ["3", "Mardi 14 octobre : les cours reprennent à 8 h 30."],
               ["4", "Soyez à l'heure."],
               ["Signature", "La direction"]],
              cle=1,
              note="Quatre lignes : la date, ce qui ferme, quand ça reprend, une consigne.",
              notes="Diapositive à photographier. Poser quatre questions dessus : "
                    "quel jour ? qu'est-ce qui est fermé ? quand ça reprend ? qui a "
                    "écrit ? C'est la grille de lecture de n'importe quel avis.")

    d.tableau('Analyse · 2 de 2', "Ce qui est écrit sur les portes",
              ["La forme", "Exemples"],
              [["un verbe, sans « vous »", "Écrivez votre nom. · Lisez l'avis."],
               ["la plus fréquente", "Soyez à l'heure."],
               ["ce qui est possible", "C'est permis. · C'est possible."],
               ["ce qui ne l'est pas", "C'est interdit. · C'est fermé."],
               ["ce que je dis, moi", "Je peux venir. · Je dois prévenir."]],
              cle=1,
              note="Sur une affiche, jamais « vous écrivez » : le verbe est seul.",
              notes="Diapositive à photographier. Faire remarquer le « -ez » final, qui "
                    "s'entend « é » : même terminaison que dans allez et venez.")

    d.regle("Cherchez la date d'abord.",
            "Elle est presque toujours à la première ligne.",
            precision="Un avis se lit dans cet ordre : la <b>date</b>, ce qui est "
                      "<b>fermé</b> ou <b>ouvert</b>, puis la <b>consigne</b>. Si un "
                      "mot manque, on va le demander au comptoir — on ne devine jamais "
                      "une date.",
            notes="Diapositive à photographier. Le dernier point est important : une "
                  "date devinée fait manquer un cours ou fait venir un jour de congé.")

    d.pratique('Pratique · 1 de 2', "Vrai ou faux, d'après l'avis",
               "Relisez les quatre lignes de l'avis.", [
        ("Le centre est fermé lundi.", "vrai"),
        ("Lundi, le secrétariat est ouvert.", "faux - il est fermé aussi"),
        ("Les cours reprennent mardi.", "vrai"),
        ("Mardi, le cours commence à huit heures et demie.", "vrai"),
        ("C'est l'enseignante qui signe l'avis.", "faux - c'est la direction"),
    ], corrige=True, cols=1,
       notes="Le dernier énoncé est le plus utile : savoir qui écrit dit à qui aller "
             "poser la question.")

    d.pratique('Pratique · 2 de 2', "Complétez la consigne",
               "Écrivez le mot qui manque.", [
        ("___ votre nom sur la feuille.", "Écrivez"),
        ("___ l'avis sur la porte.", "Lisez"),
        ("___ à l'heure, s'il vous plaît.", "Soyez"),
        ("Manger dans le local, c'est ___.", "interdit"),
        ("Le midi, le bureau est ___.", "fermé"),
        ("Je ___ prévenir avant mon absence.", "dois"),
    ], corrige=True, cols=2,
       notes="Faire à l'oral d'abord. « Soyez » est irrégulier : le donner comme un "
             "mot, pas comme une conjugaison.")

    d.pratique('Pratique · les affiches du centre', "Cinq affiches à trouver",
               "Vingt minutes, à deux, dans le centre.", [
        ("Étape 1", "Trouvez cinq papiers affichés dans le centre."),
        ("Étape 2", "Pour chacun : quelle date ? qu'est-ce qui est fermé ?"),
        ("Étape 3", "Trouvez un verbe de consigne : écrivez, lisez, fermez, soyez."),
        ("Étape 4", "Revenez et lisez une affiche au groupe, à voix haute."),
    ], cols=1,
       notes="Sortir vraiment. Cet exercice-là est ce que la séance apprend : lire dans "
             "le bâtiment, pas sur la diapositive.")

    d.billet(
        "Écrivez ce que dit une affiche de votre centre.",
        exemples=[
            "Le secrétariat est fermé de 12 h à 13 h.",
            "Soyez à l'heure.",
            "C'est interdit de manger dans le local.",
        ],
        notes="Devoir court. Accepter une affiche trouvée ailleurs : au dépanneur, à la "
              "clinique, dans l'autobus. Les mêmes quatre mots y servent.")

    return d.save(dossier)
