# -*- coding: utf-8 -*-
"""D2 · Je vais payer, je la prends.
Bloc D « Défi 3 · Payer et faire livrer » · couleur ambre (écriture) · 60 min.
Source : exercices `t3futur`, `t3pronoms` et `t3b`, mini-leçons `t3futur` et
`t3pronoms`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre='Je vais payer, je la prends',
        chapeau="Deux outils pour finir un achat : dire ce qui va arriver "
                "samedi, et répondre au vendeur sans répéter le nom de "
                "l'appareil.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture, deux points de langue. Les deux servent dans la "
                  "même phrase — « Je vais la prendre » — donc les enseigner l'un après "
                  "l'autre, puis les réunir à la fin.")

    d.objectifs([
        "employer le futur proche : aller + un verbe ;",
        "remplacer le nom d'un appareil par le, la ou les ;",
        "placer le petit mot avant le verbe ;",
        "lire un bon de livraison et en tirer l'information.",
    ])

    d.regle("Le futur proche : aller, puis le verbe",
            "« Je vais payer. »  ·  « Le camion va arriver samedi. »",
            precision="Le verbe aller au présent, puis le second verbe sans "
                      "rien y changer. C'est le futur du magasin, de la "
                      "livraison et de la vie de tous les jours.",
            notes="Diapo à photographier. Le futur en -rai attendra le niveau suivant : "
                  "ne pas l'introduire ici.")

    d.tableau('Analyse', "Les quatre formes utiles",
              ['Qui', 'Aller', 'Exemple'],
              [["je", "vais", "Je vais payer à la caisse."],
               ["tu", "vas", "Tu vas garder le bon ?"],
               ["il, elle, le camion", "va", "Le camion va arriver samedi."],
               ["ils, elles, les livreurs", "vont", "Ils vont monter la laveuse."]],
              cle=1,
              note="À l'oral, on entend beaucoup « on va » : « On va être là samedi. »",
              notes="Diapo à photographier. Faire produire une phrase par ligne, avec un "
                    "élève différent.")

    d.pratique('Écriture', "Vais, vas, va ou vont ?",
               "Complétez chaque phrase.", [
        ("Je ___ payer à la caisse.", "vais"),
        ("Le camion ___ arriver samedi matin.", "va"),
        ("Les livreurs ___ monter la laveuse au troisième.", "vont"),
        ("Tu ___ garder le bon de livraison ?", "vas"),
        ("Ils ___ emporter la vieille machine.", "vont"),
    ], corrige=True,
       notes="Faire écrire, puis corriger au tableau. Insister sur la forme du second "
             "verbe : elle ne change jamais.")

    d.regle("Remplacer l'appareil par un petit mot",
            "« Je prends la laveuse. »  devient  « Je la prends. »",
            precision="Le petit mot se met AVANT le verbe : « je le prends », "
                      "jamais « je prends le ». Avec deux verbes, il se glisse "
                      "entre les deux : « Je vais le prendre. »",
            notes="Diapo à photographier. C'est l'ordre inverse de plusieurs langues : "
                  "le signaler explicitement plutôt que de corriger dix fois.")

    d.tableau('Analyse', "Le, la ou les ?",
              ['Ce qu\'on remplace', 'Le petit mot', 'Exemple'],
              [["le micro-ondes", "le", "Je le prends."],
               ["la laveuse", "la", "Je la prends."],
               ["les deux appareils", "les", "Je les prends."],
               ["devant une voyelle", "l'", "Je l'achète."]],
              cle=1,
              note="C'est le genre du mot qui décide, jamais celui de l'objet.",
              notes="Diapo à photographier. Faire produire les quatre phrases avec "
                    "d'autres appareils.")

    d.pratique('Écriture', "Le, la ou les ?",
               "Complétez chaque réponse.", [
        ("— Vous prenez la laveuse ? — Oui, je ___ prends.", "la"),
        ("— Et le micro-ondes ? — Oui, je ___ prends aussi.", "le"),
        ("Les deux sont en spécial : je ___ achète tout de suite.", "les"),
        ("Cette cuisinière est trop grande. Je ne ___ prends pas.", "la"),
        ("Mes vieux appareils, le magasin va ___ emporter.", "les"),
    ], corrige=True,
       notes="La dernière phrase réunit les deux points de la séance : futur proche et "
             "pronom entre les deux verbes.")

    d.piege("Mettre le petit mot après le verbe",
            "Je prends le.",
            "Je le prends.",
            "En français, ce petit mot passe toujours avant le verbe. C'est l'inverse de "
            "l'anglais et de plusieurs autres langues, et c'est la faute la plus "
            "fréquente à ce niveau. Une fois le réflexe pris, il ne se reperd plus.",
            notes="Faire répéter les trois réponses courtes — je le prends, je la "
                  "prends, je les prends — jusqu'à ce qu'elles sortent sans réfléchir.")

    d.cartes("Le bon de livraison de Marisol", "Ce qui est écrit dessus", [
        ("Client",
         "M. Ramos — 555 0148. Le nom et le numéro où joindre la personne."),
        ("Adresse",
         "2140, rue des Trembles, app. 3, Saint-Hubert."),
        ("Appareil et livraison",
         "Laveuse Norlac LT 4200, blanche. Samedi 8 novembre, entre 8 h et midi, 60 $."),
        ("Reprise",
         "Ancienne laveuse reprise, gratuit. C'est ce que Marisol a demandé au comptoir."),
    ], notes="Projeter, puis poser les questions à l'oral sans montrer : quel jour, "
             "quelle heure, combien, et est-ce qu'on reprend l'ancienne.")

    d.billet(
        "Écrivez quatre phrases sur votre livraison.",
        exemples=[
            "« Je vais payer à la caisse. »",
            "« Le camion va arriver samedi matin. » « Je vais être là. »",
        ],
        notes="Devoir d'écriture. Ces phrases sont le brouillon de la production écrite "
              "de E1 : le dire aux élèves.")

    return d.save(dossier)
