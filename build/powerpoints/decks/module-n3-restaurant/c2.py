# -*- coding: utf-8 -*-
"""C2 · Je voudrais.
Bloc C « Défi 2 · Commander au comptoir » · couleur ambre · 75 min.
Source : exercice `t2voudrais`, mini-leçon `t2voudrais`.

Le programme du niveau 3 nomme ce point dans ses attentes de fin de cours :
« certains auxiliaires de modalité au conditionnel de politesse ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Je voudrais',
        chapeau="« Je veux un café » et « Je voudrais un café » veulent dire "
                "la même chose. Une syllabe les sépare, et ce n'est pas la "
                "même personne qu'on entend.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire et de registre. Le point de langue est nommé "
                  "explicitement dans les attentes de fin de cours du niveau 3.")

    d.objectifs([
        "employer « je voudrais » pour commander ;",
        "employer « est-ce que je peux avoir » pour demander ;",
        "placer « s'il vous plaît » à la bonne place ;",
        "vouvoyer un préposé qu'on ne connaît pas.",
    ])

    d.regle("La formule qui ouvre toutes les portes",
            "« Je voudrais un café, s'il vous plaît. »",
            precision="Trois morceaux, toujours dans le même ordre : la "
                      "formule, ce qu'on veut, la politesse. Cette phrase "
                      "seule permet de commander n'importe quoi, dans "
                      "n'importe quel commerce.",
            notes="Diapo à photographier. Faire répéter la phrase à voix haute par tout "
                  "le groupe, trois fois, avec trois plats différents.")

    d.tableau('Analyse', "Sec ou poli ?",
              ['On entend', "Ce qu'il vaut mieux dire"],
              [["Je veux un café.", "Je voudrais un café, s'il vous plaît."],
               ["Donnez-moi une soupe.", "J'aimerais une soupe, s'il vous plaît."],
               ["Une serviette.", "Est-ce que je peux avoir une serviette ?"],
               ["Un jus, vite.", "Je prendrais un jus, s'il vous plaît."]],
              cle=1,
              note="La colonne de gauche n'est pas fausse : elle est dure à entendre.",
              notes="Diapo à photographier. Lire les deux colonnes à voix haute, l'une "
                    "après l'autre. La différence de ton s'entend immédiatement.")

    d.tableau('Analyse', "Trois formules, un seul sens",
              ['La formule', 'Quand on la dit'],
              [["Je voudrais…", "la plus courante, partout, tout le temps"],
               ["J'aimerais…", "la même chose, un peu plus douce"],
               ["Je prendrais…", "quand on a fini de choisir"]],
              cle=0,
              note="Choisis-en une et garde-la : mieux vaut une formule bien tenue.",
              notes="Faire choisir chaque élève, à voix haute, laquelle il adopte. Le "
                    "choix aide à la mémoriser.")

    d.regle("Demander n'est pas commander",
            "« Est-ce que je peux avoir une cuillère ? »",
            precision="Pour un ustensile, une serviette, un sac ou un "
                      "couvercle, on ne commande pas : on demande. La formule "
                      "change, et elle sert dans tout le défi 3.",
            notes="Diapo à photographier. Cette phrase revient à la séance D1 : la poser "
                  "ici évite de tout apprendre en même temps plus tard.")

    d.pratique('Écriture', "Rendez la phrase polie",
               "Récrivez avec « je voudrais » ou « est-ce que je peux avoir ».", [
        ("Donnez-moi un café.", "Je voudrais un café, s'il vous plaît."),
        ("Je veux une soupe aux légumes.", "Je voudrais une soupe aux légumes, s'il vous plaît."),
        ("Un trio poulet.", "Je voudrais un trio au poulet, s'il vous plaît."),
        ("Donne une serviette.", "Est-ce que je peux avoir une serviette ?"),
        ("Je veux payer avec ma carte.", "Est-ce que je peux payer avec ma carte ?"),
    ], corrige=True,
       notes="Faire écrire dans le cahier avant de corriger. Les deux derniers items "
             "sont des demandes, pas des commandes : le faire remarquer.")

    d.piege("Tutoyer le préposé",
            "Tu me donnes un café ?",
            "Je voudrais un café, s'il vous plaît.",
            "Au comptoir, on ne connaît pas la personne qui sert : on vouvoie. Le "
            "tutoiement se garde pour les camarades de classe, les amis et la famille. "
            "Beaucoup de langues n'ont pas cette distinction, et beaucoup d'élèves "
            "l'apprennent d'abord par erreur.",
            notes="Rappeler que dans le module, Yolette tutoie Fatou et vouvoie Steve. "
                  "Les deux dialogues sont là pour le montrer, pas seulement pour le "
                  "dire.")

    d.pratique('Production orale', "Commandez poliment",
               "Une phrase complète, debout, à voix haute.", [
        ("un café", "Je voudrais un café, s'il vous plaît."),
        ("une soupe aux légumes", "Je voudrais une soupe aux légumes, s'il vous plaît."),
        ("un trio au jambon", "J'aimerais un trio au jambon, s'il vous plaît."),
        ("une cuillère", "Est-ce que je peux avoir une cuillère ?"),
    ], corrige=True,
       notes="En paires, debout, face à face. Un élève joue le préposé et répond "
             "« Certainement ». Deux minutes par paire.")

    d.billet(
        "Écrivez cinq demandes polies.",
        exemples=[
            "Trois avec « je voudrais », deux avec « est-ce que je peux avoir ».",
            "Terminez par « s'il vous plaît » quand c'est une commande.",
        ],
        notes="Devoir court. Il prépare la séance C3, où le préposé prend la parole à "
              "son tour.")

    return d.save(dossier)
