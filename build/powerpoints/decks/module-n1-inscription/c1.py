# -*- coding: utf-8 -*-
"""C1 · Les petits mots coupés.
Bloc C « Défi 2 · L'adresse et le téléphone » · couleur acier · 75 min.
Source : dialogue `t2`, exercices `t2vf` et `t2abrev`, mini-leçon `t2abrev`.

Première séance du défi 2. Une fiche est pleine de mots tronqués ; une fois
qu'on les connaît, tout le bas du formulaire devient lisible.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Les petits mots coupés',
        chapeau="app., av., boul., QC, Tél., C.P. — ce ne sont pas des mots "
                "nouveaux, ce sont des mots connus écrits en plus court.",
        duree='75 minutes')

    d.titre(notes="Apporter deux ou trois enveloppes vraiment reçues, adresse cachée : les "
                  "abréviations y sont toutes, et l'objet rend la séance concrète.")

    d.objectifs([
        "lire les abréviations d'une adresse ;",
        "dire ce que le point signifie ;",
        "écrire une adresse sur deux lignes ;",
        "demander « j'écris quoi ici ? ».",
    ])

    d.declencheur(
        'Observation', "Que veulent dire ces petits mots ?",
        pistes=[
            "app. · av. · boul.",
            "QC · Tél. · C.P.",
            "Pourquoi y a-t-il un point à la fin ?",
            "Lequel avez-vous déjà vu sur une enveloppe ?",
        ],
        notes="Laisser deviner avant d'expliquer : la plupart auront déjà vu « app. » sur "
              "leur bail ou leur boîte aux lettres.")

    d.dialogue('Dialogue · 1 de 2', "J'écris quoi dans cette case ?", [
        ("CARLOS", "Yusuf, regarde. J'écris quoi ici ?", True),
        ("YUSUF", "C'est l'adresse. Le numéro et la rue.", True),
        ("CARLOS", "J'habite au 3120, avenue Papineau. Appartement 4.", True),
        ("YUSUF", "Écris « a v point » pour avenue. Et « a p p point 4 ».", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Ici, ce sont deux élèves qui se parlent : on se tutoie. Le faire remarquer — "
             "avec madame Côté, c'était « vous ».")

    d.dialogue('Dialogue · 2 de 2', "Et ça, c'est quoi ?", [
        ("CARLOS", "Et ça ? « T é l point » ?", True),
        ("YUSUF", "C'est le téléphone. Dix chiffres.", True),
        ("CARLOS", "Merci ! Tu écris vite, toi.", True),
        ("YUSUF", "Non. Je demande souvent, c'est tout.", True),
    ], notes="La dernière réplique est la morale du module : demander n'est pas un aveu de "
             "faiblesse, c'est la méthode.")

    d.tableau('Analyse · 1 de 2', "Les mots de l'adresse",
              ['On écrit', 'On lit'],
              [["app.", "un appartement"],
               ["av.", "une avenue"],
               ["boul.", "un boulevard"],
               ["n°", "un numéro"]],
              cle=2,
              note="Le point dit que le mot n'est pas fini.",
              notes="Diapo à photographier. « rue » ne s'abrège pas : c'est déjà court, on "
                    "l'écrit en entier.")

    d.tableau('Analyse · 2 de 2', "Les mots des cases du bas",
              ['On écrit', 'On lit'],
              [["QC", "Québec, la province — sans point"],
               ["Tél.", "le téléphone — dix chiffres après"],
               ["C.P.", "une case postale"],
               ["H2K 1N4", "le code postal — jamais un mot"]],
              cle=2,
              note="C.P. et code postal ne sont pas la même case.",
              notes="Diapo à photographier. La case postale est une boîte au bureau de "
                    "poste : on en prend une quand on n'a pas encore d'adresse à soi.")

    d.regle("L'adresse, de haut en bas",
            "Le numéro d'abord, la rue ensuite.",
            precision="Première ligne : <b>3120, avenue Papineau, app. 4</b>. Deuxième "
                      "ligne : <b>Montréal, QC  H2K 1N4</b>. Dans plusieurs pays, le "
                      "numéro vient après le nom de la rue — ici, il vient toujours "
                      "avant, et il est suivi d'une virgule.",
            notes="Diapo à photographier. Faire écrire sa propre adresse sur ces deux "
                  "lignes tout de suite, au crayon, sur la fiche vierge.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Carlos habite avenue Papineau.", "vrai"),
        ("Il habite à l'appartement 4.", "vrai"),
        ("« Tél. » veut dire téléphone.", "vrai"),
        ("Un numéro de téléphone a six chiffres.", "faux — il en a dix"),
        ("Yusuf dit qu'il demande souvent.", "vrai"),
    ], corrige=True, cols=1,
       notes="Cinq énoncés, comme dans l'exercice `t2vf`.")

    d.pratique('Pratique', "Écrivez le mot complet",
               "L'abréviation est entre parenthèses.", [
        ("3120, ___ Papineau  (av.)", "avenue"),
        ("___ 4  (app.)", "appartement"),
        ("Montréal, ___  (QC)", "Québec"),
        ("940, ___ Saint-Laurent  (boul.)", "boulevard"),
    ], corrige=True, cols=1,
       notes="Ce sont quatre des cinq énoncés de l'exercice `t2adresse`. Le cinquième — "
             "« Tél. » — se garde pour la séance C2.")

    d.pratique('Pratique · à deux', "Votre adresse, la sienne",
               "L'un dicte, l'autre écrit sur deux lignes.", [
        ("Ligne 1", "le numéro, la rue, l'appartement"),
        ("Ligne 2", "la ville, QC, le code postal"),
        ("Vérification", "Montrez ce que vous avez écrit. C'est bien ça ?"),
        ("Échange", "Puis on inverse les rôles."),
    ], cols=1,
       notes="Vingt minutes. Faire épeler le nom de la rue : c'est là que ça bloque le "
             "plus, et l'épellation a été travaillée dans le module précédent.")

    d.billet(
        "Écrivez votre adresse sur deux lignes, avec les abréviations.",
        exemples=[
            "Ligne 1 : le numéro, la rue, l'appartement.",
            "Ligne 2 : la ville, QC, le code postal.",
        ],
        notes="Deux minutes. Relever surtout la position du numéro : avant la rue.")

    return d.save(dossier)
