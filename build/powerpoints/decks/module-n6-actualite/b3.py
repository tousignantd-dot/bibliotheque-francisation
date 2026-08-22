# -*- coding: utf-8 -*-
"""B3 · Le, en, y : trois mots qui renvoient en arrière
Bloc B « Défi 1 · La chronique pratique » · couleur ambre · 75 min.
Source : exercice `t1repr` et sa mini-leçon « Le, en, y : trois mots qui
renvoient en arrière ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Le, en, y : trois mots qui renvoient en arrière",
        chapeau="« Je vous en parle », « je le sais », « j'y reviens ». "
                "Chaque fois, un mot de deux lettres renvoie à quelque chose "
                "dit trente secondes plus tôt. Perdre le fil, c'est perdre "
                "ça.",
        duree='75 minutes')

    d.titre(notes="Troisième séance du Défi 1. C'est la séance la plus grammaticale du "
                  "bloc, et la plus utile : le programme du niveau 6 demande de suivre "
                  "un discours détaillé, et c'est exactement ce qui s'y joue.")

    d.objectifs([
        "retrouver à quoi renvoie « le » dans un texte suivi ;",
        "employer « en » pour remplacer « de » et une chose ;",
        "employer « y » pour remplacer « à » et une chose, ou un lieu ;",
        "placer le pronom devant le verbe, y compris à la forme négative.",
    ], notes="Le premier objectif est de compréhension, les trois autres de production. "
             "Si le temps manque, garder le premier : c'est celui que l'écoute exige.")

    d.declencheur(
        'Observation', "Ces petits mots renvoient à quoi ?",
        pistes=[
            "« Je vous en parle. » - de quoi ?",
            "« Je le sais. » - sais quoi ?",
            "« J'y reviens toujours. » - où ?",
            "Dans chaque cas, il faut reculer d'une phrase. Essayons.",
        ],
        notes="Faire chercher les trois réponses dans la transcription de la chronique. "
              "Le geste de reculer d'une phrase est la vraie compétence : le faire "
              "faire physiquement, doigt sur la ligne.")

    d.tableau('Analyse', "Trois pronoms, trois emplois",
              ['Le pronom', 'Ce qu\'il remplace'],
              [["le", "une idée entière déjà dite : je sais que la garantie court"],
               ["en", "« de » et une chose : elle parle de la garantie légale"],
               ["y", "« à » et une chose, ou un lieu : je pense à ma facture"],
               ["de lui, d'elle", "« de » et une personne : elle parle de son voisin"]],
              cle=0,
              note="La quatrième ligne est l'exception : pour une personne, on garde la préposition.",
              notes="Diapositive à photographier. La quatrième ligne fait toute la "
                    "différence entre un élève de niveau 5 et un de niveau 6 : la "
                    "montrer, la faire répéter, mais ne pas s'y attarder.")

    d.regle("Le « le » qui remplace une phrase",
            "Ce « le » ne s'accorde jamais : il ne désigne ni un homme, ni une femme, ni un pluriel.",
            precision="« Je sais que la garantie court encore » devient « je le sais ». "
                      "Le pronom remplace toute une phrase, pas un objet. C'est pour "
                      "cela qu'on ne dira jamais « je la sais » ni « je les sais » : "
                      "une idée n'a pas de genre.",
            notes="Diapositive à photographier. Erreur attendue et fréquente : « je la "
                  "sais » chez les élèves hispanophones et lusophones. La corriger sans "
                  "insister, elle disparaît d'elle-même avec l'usage.")

    d.regle("Où se place le pronom",
            "Devant le verbe, toujours - et devant l'infinitif quand il y en a un.",
            precision="Je le sais. Je ne le savais pas. Je vais en parler. Il faut y "
                      "penser. La négation entoure le bloc pronom-verbe : « ne » avant "
                      "le pronom, « pas » après le verbe. C'est la seule position "
                      "possible en français, et c'est ce qui la rend facile.",
            notes="Diapositive à photographier. Écrire les quatre exemples au tableau et "
                  "les faire répéter en chœur : c'est un automatisme de rythme, pas une "
                  "règle à comprendre.")

    d.pratique('Grammaire', "Remplacez par le, en ou y",
               "Récrivez la deuxième phrase avec le bon pronom.", [
        ("Claudine explique que la garantie légale existe. Théo ... savait déjà.", "le"),
        ("Elle parle souvent de l'Office. Elle ... parle presque chaque mois.", "en"),
        ("Nadège pense à sa facture. Elle ... pense depuis mardi.", "y"),
        ("Ils vont aux petites créances. Ils ... vont sans avocat.", "y"),
        ("Beaucoup de gens ignorent qu'ils ont un recours. Ils ... ignorent longtemps.", "l'"),
        ("Elle a besoin d'une pièce de rechange. Elle ... a besoin depuis cinq semaines.", "en"),
    ], corrige=True, cols=2,
       notes="Le cinquième item est le seul avec apostrophe : « ils l'ignorent ». Le "
             "faire remarquer avant la correction, sinon la moitié du groupe écrira "
             "« ils le ignorent ».")

    d.piege("Employer « en » pour une personne",
            "Elle parle de son voisin. Elle en parle souvent.",
            "Elle parle de son voisin. Elle parle souvent de lui.",
            "Pour une chose, « de » et le nom se réduisent à « en ». Pour une personne, "
            "on garde la préposition et on met un pronom fort : de lui, d'elle, d'eux. "
            "La faute ne gêne pas la compréhension, mais elle s'entend tout de suite - "
            "et elle se corrige en une leçon.",
            notes="Faire fabriquer deux phrases par élève : une avec une chose, une avec "
                  "une personne. La comparaison immédiate fixe la règle mieux qu'une "
                  "explication.")

    d.cartes("Le réflexe de lecture", "Quand tu entends le, en ou y", [
        ("Arrête-toi",
         "un pronom vient de passer : le fil vient de se resserrer."),
        ("Recule d'une phrase",
         "la réponse est presque toujours dans la phrase juste avant."),
        ("Demande : ça remplace quoi ?",
         "une idée, une chose, un lieu ? La forme du pronom te le dit."),
        ("Reprends la lecture",
         "si tu ne trouves pas, continue : la suite éclaire souvent le pronom."),
    ], notes="Quatre gestes, à copier dans le cahier. Le dernier compte autant que les "
             "autres : un élève qui bloque sur un pronom perd tout le reste du texte.")

    d.billet(
        "Écris une phrase avec « le », « en » ou « y », et dis ce que le pronom remplace.",
        exemples=[
            "Par exemple : « J'y pense » - à ma facture.",
            "Une phrase, et sa traduction en clair.",
        ],
        notes="Deux minutes. Les billets qui ne disent pas ce que le pronom remplace "
              "signalent exactement les élèves à reprendre en B4.")

    return d.save(dossier)
