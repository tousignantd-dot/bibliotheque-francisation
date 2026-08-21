# -*- coding: utf-8 -*-
"""A2 · Le son ON et le son AN.
Bloc A « Je découvre » · couleur indigo (graphie-phonie) · 60 min.
Source : mini-leçon `prPhon`, exercice `prPhon` (cartes à écouter).

Les sons sont nommés par leurs lettres et par un mot repère — « le son ON,
comme dans livraison ». L'alphabet phonétique reste dans le module
interactif : sur une diapositive projetée, il ne servirait à personne.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre='Le son ON et le son AN',
        chapeau="Livraison, comptant, grand, cent : les deux sons qui passent "
                "par le nez sont partout dans un magasin. Les distinguer, "
                "c'est entendre la différence entre « cent » et « son ».",
        duree='60 minutes')

    d.titre(notes="Séance de phonétique. Prévoir les haut-parleurs : tout se joue à "
                  "l'oreille, et les élèves doivent entendre avant de voir écrit.")

    d.objectifs([
        "entendre la différence entre le son ON et le son AN ;",
        "prononcer les deux sons en plaçant la bouche ;",
        "reconnaître les quatre écritures : on, om, an, en ;",
        "lire à voix haute les mots du magasin.",
    ])

    d.regle("Deux voyelles qui passent par le nez",
            "livraison  ·  grand",
            precision="L'air sort par le nez en même temps que par la bouche. "
                      "Beaucoup de langues n'ont aucun son de ce genre : c'est "
                      "pour ça qu'il faut les travailler, et pas seulement les "
                      "écouter.",
            notes="Diapo à photographier. Faire le test des deux doigts sur le nez : si "
                  "le son change quand on bouche le nez, c'est bien une voyelle nasale.")

    d.tableau('Analyse', "Où va la bouche ?",
              ['Le son', 'La bouche', 'Mots repères'],
              [["ON", "les lèvres en rond, bien avancées", "livraison, rond, onze"],
               ["AN", "la bouche grande ouverte, lèvres plates", "grand, cent, dimanche"]],
              cle=0,
              note="Les lèvres décident : rondes pour ON, ouvertes pour AN.",
              notes="Faire prononcer les deux sons en tenant un miroir, ou en se "
                    "regardant deux par deux. La forme des lèvres se voit.")

    d.tableau('Graphie-phonie', "Quatre écritures, deux sons",
              ['On écrit', 'On entend', 'Exemple'],
              [["on", "ON", "livraison"],
               ["om devant b et p", "ON", "comptant"],
               ["an, am", "AN", "grand, chambre"],
               ["en, em", "AN", "vendeur, temps"]],
              cle=1,
              note="Le piège est la dernière ligne : les lettres e et n se disent AN.",
              notes="Diapo à photographier. C'est la ligne « en » qui coûte le plus cher "
                    "aux élèves : « vendeur » ne se dit pas comme il s'écrit.")

    d.pratique('Écoute', "ON ou AN ?",
               "Écoutez le mot, puis dites quel son vous entendez.", [
        ("la livraison", "ON"),
        ("grand", "AN"),
        ("un rond", "ON"),
        ("dimanche", "AN"),
        ("le savon", "ON"),
        ("quarante", "AN"),
    ], corrige=True,
       notes="Dire chaque mot deux fois, sans le montrer. Les élèves lèvent une main pour "
             "ON, deux pour AN : l'enseignante voit tout de suite qui hésite.")

    d.cartes("Les paires qui trompent l'oreille", "Quatre paires", [
        ("son / cent",
         "Le premier est un mot de tous les jours, le second est un prix. Les confondre "
         "change le sens de la phrase."),
        ("rond / rang",
         "Les ronds de la cuisinière, le rang à la caisse. Deux mots courants du module."),
        ("onze / anse",
         "Le son est au début du mot, là où il s'entend le mieux."),
        ("livraison / vendeur",
         "La paire à retenir : elle contient les deux sons et les deux écritures les "
         "plus fréquentes."),
    ], notes="Faire répéter chaque paire trois fois : d'abord lentement, puis vite, puis "
             "les yeux fermés pour la reconnaissance.")

    d.piege("Prononcer la lettre n à la fin",
            "li-vrai-son-ne",
            "livraison",
            "Le n ne se prononce pas tout seul : il rend la voyelle nasale, puis il "
            "disparaît. La bouche ne se referme pas à la fin du mot. C'est l'erreur la "
            "plus fréquente chez les élèves dont la langue prononce toutes les lettres.",
            notes="Faire tenir le dernier son deux secondes, bouche ouverte, sans fermer "
                  "les lèvres. L'erreur s'entend tout de suite.")

    d.pratique('Lecture', "Lisez à voix haute",
               "Six phrases du magasin. Marquez les sons ON et AN.", [
        ("La livraison coûte soixante dollars.", "ON trois fois"),
        ("Le vendeur est dans le grand rayon.", "AN quatre fois"),
        ("Onze appareils sont en spécial.", "ON puis AN"),
        ("Ce modèle est trop grand pour ma chambre.", "AN trois fois"),
        ("Je paie comptant, pas par carte.", "les deux sons dans un seul mot"),
        ("Mon ordinateur a quatre ans.", "ON puis AN"),
    ], corrige=True,
       notes="Faire lire chaque phrase par deux élèves différents. Corriger seulement les "
             "deux sons de la séance : le reste attendra.")

    d.billet(
        "Trouvez trois mots avec le son ON et trois mots avec le son AN.",
        exemples=[
            "Dans la circulaire de votre boîte aux lettres, si vous en avez une.",
            "Écrivez-les, et soulignez les lettres qui font le son.",
        ],
        notes="Devoir court. Rapporter la circulaire en classe si possible : elle servira "
              "au bloc B.")

    return d.save(dossier)
