# -*- coding: utf-8 -*-
"""C4 · Lire un billet de clinique.
Bloc C « Défi 2 · Le billet d'absence » · couleur acier · 60 min.
Source : exercices `t2billet` et `t2b`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='acier',
        titre='Lire un billet de clinique',
        chapeau="Six lignes sur un bout de papier, et chacune répond à une "
                "question du comptoir. Savoir les lire, c'est ne plus jamais "
                "repartir avec un papier incomplet.",
        duree='60 minutes')

    d.titre(notes="Séance de lecture. Si un élève accepte de montrer un vrai billet "
                  "reçu, le projeter en cachant le nom : rien ne vaut le vrai document.")

    d.objectifs([
        "trouver chaque renseignement dans un billet ;",
        "vérifier qu'un billet est complet ;",
        "comprendre ce que le centre fait du papier ;",
        "savoir quoi dire si le billet est incomplet.",
    ])

    d.tableau('Lecture', "Billet d'absence — Clinique de la rue Ontario",
              ["Ligne du billet", "Ce qu'elle donne"],
              [["Nawel Belkacem", "le nom de la personne qui a été absente"],
               ["Motif : maladie", "la raison, en un mot, sans détail"],
               ["Du 3 au 5 mars", "les journées que le billet justifie"],
               ["Retour le 6 mars", "la première journée où on est attendu"],
               ["Dre A. Mercier, 5 mars", "qui signe, et quand"]],
              cle=1,
              note="Le motif est toujours vague : maladie, rendez-vous. Aucune "
                   "clinique n'écrit de diagnostic sur un billet d'absence.",
              notes="Diapo à photographier. Rassurer sur le motif : c'est une inquiétude "
                    "réelle, surtout chez les personnes qui viennent de systèmes où le "
                    "papier en dit davantage.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le billet.", [
        ("Le billet couvre trois journées.", "vrai — du 3 au 5"),
        ("Nawel est attendue au cours le 6 mars.", "vrai"),
        ("Le billet ne porte aucune signature.", "faux — Dre A. Mercier"),
        ("Le billet dit quelle maladie Nawel a eue.", "faux — seulement « maladie »"),
        ("Le centre garde une photocopie du billet.", "vrai"),
        ("Nawel repart sans son papier.", "faux — elle garde l'original"),
    ], corrige=True,
       notes="Faire retrouver la ligne exacte pour chaque réponse. C'est la stratégie "
             "de lecture qu'on travaille, pas le contenu.")

    d.regle("Regardez le billet avant de sortir de la clinique",
            "une date, un nom, une signature",
            precision="S'il manque une des trois, le papier ne justifie rien "
                      "et il faudra y retourner. Trente secondes de "
                      "vérification au comptoir de la clinique évitent une "
                      "demi-journée perdue.",
            notes="Diapo à photographier. C'est le conseil le plus concret du module. "
                  "Le faire écrire au carnet, en trois mots.")

    d.cartes("Si quelque chose manque", "Trois phrases à avoir", [
        ("Au comptoir de la clinique",
         "« Est-ce que vous pouvez ajouter les dates, s'il vous plaît ? » On le fait "
         "sans discuter : c'est un oubli, pas un refus."),
        ("Au comptoir du centre",
         "« Le papier n'a pas de date. Qu'est-ce que je dois faire ? » La secrétaire le "
         "dira simplement, sans reproche."),
        ("Si vous n'avez aucun papier",
         "Dites-le. Une absence sans billet reste une absence annoncée, et c'est déjà "
         "beaucoup mieux que le silence."),
    ], cols=3,
       notes="La troisième carte compte autant que les deux autres : plusieurs élèves ne "
             "viennent pas au comptoir parce qu'ils n'ont pas de papier.")

    d.tableau('Analyse', "Ce que le centre fait du papier",
              ["Geste", "Pourquoi"],
              [["photocopie au dossier", "la trace reste au centre"],
               ["original rendu à l'élève", "il peut servir ailleurs"],
               ["absence notée justifiée", "l'enseignante le voit"],
               ["rien d'autre", "le motif n'est lu par personne d'autre"]],
              cle=1,
              note="Le billet ne circule pas : il est classé, et c'est tout.",
              notes="Diapo à photographier. La dernière ligne répond à une question "
                    "souvent tue : qui va lire mon papier ? Personne d'autre.")

    d.pratique('Production orale', "Rendez votre billet",
               "En paires, une minute chacun.", [
        ("Se nommer", "nom, prénom, groupe"),
        ("Dire les journées", "lundi, mardi et mercredi"),
        ("Présenter le papier", "voici mon billet de la clinique"),
        ("Demander l'original", "est-ce que je peux le garder ?"),
    ], corrige=False,
       notes="Un élève joue la secrétaire, l'autre revient d'absence, puis on change. "
             "Deux minutes en tout, et le défi 2 est joué en entier.")

    d.billet(
        "Écrivez les trois choses à vérifier sur un billet.",
        exemples=[
            "Une date, un nom, une signature.",
            "Gardez la liste dans votre portefeuille, avec votre carte d'élève.",
        ],
        notes="Fin du défi 2. Vérifier que la liste est bien écrite : c'est le seul "
              "devoir du module qui servira encore dans cinq ans.")

    return d.save(dossier)
