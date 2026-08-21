# -*- coding: utf-8 -*-
"""C1 · L'avis dans l'entrée.
Bloc C « Défi 2 · L'avis » · couleur acier · 75 min. Compréhension orale et écrite.
Source : dialogue `t2`, exercice `t2a`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-degat/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="L'avis dans l'entrée",
        chapeau="Quinze lignes affichées à côté des boîtes aux lettres, et "
                "elles vous obligent à quelque chose. C'est la seule intention "
                "que le programme donne à cette situation : lire un avis.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2, et cœur du module au regard du programme : la "
                  "situation « Problèmes reliés à l'habitation » n'a qu'une intention au "
                  "niveau 5, et c'est « lire un avis ». Le dire au groupe — savoir "
                  "pourquoi on travaille quelque chose change l'attention.")

    d.objectifs([
        "lire un avis dans l'ordre : à qui, quand, quoi faire, sinon ;",
        "repérer les trois données de date qu'un avis doit donner ;",
        "reconnaître le paragraphe qui vous engage ;",
        "savoir dans quelles conditions un propriétaire peut entrer chez vous.",
    ])

    d.declencheur(
        'Observation', "Cette feuille vient d'être affichée dans votre entrée. "
                       "Par quoi commencez-vous ?",
        image=IMG + 'avis-entree-immeuble.jpg',
        pistes=[
            "Est-ce que ça vous concerne ?",
            "Quelles dates faut-il noter ?",
            "Qu'est-ce qu'on vous demande de faire ?",
            "Qu'est-ce qui arrive si vous ne le faites pas ?",
        ],
        notes="Les quatre pistes sont l'ordre de lecture de la séance. Les garder "
              "affichées : le groupe y reviendra à chaque avis rencontré.")

    d.dialogue('Dialogue · 1 de 3', "Il vient d'être posé", [
        ("KIM", "Mariama, viens voir. Il y a un avis affiché dans l'entrée, à "
                "côté des boîtes aux lettres.", True),
        ("MARIAMA", "Il était là ce matin ?", True),
        ("KIM", "Non, il vient d'être posé. C'est écrit « Avis aux locataires » "
                "en gros, en haut.", True),
        ("MARIAMA", "« Des travaux d'assèchement seront effectués dans les "
                    "logements 3 et 4… » Ça, c'est chez toi et chez moi.", False),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="« Il vient d'être posé » n'est pas un détail : la date d'affichage lance "
             "le délai de vingt-quatre heures. Le relever.")

    d.dialogue('Dialogue · 2 de 3', "Ce qu'on vous demande", [
        ("KIM", "« … du mercredi 12 au vendredi 14 novembre, entre 8 h et 17 h. »", True),
        ("MARIAMA", "Trois jours. Et en dessous : « Il est nécessaire que les "
                    "occupants libèrent l'accès au mur touché. »", True),
        ("KIM", "Ça veut dire tasser les meubles. Ton lit, ta commode, tout ce "
                "qui est le long de ce mur-là.", True),
        ("MARIAMA", "« Veuillez prévoir un accès au logement. À défaut, "
                    "l'entrepreneur communiquera avec le propriétaire. »", True),
    ], notes="Kim traduit : c'est exactement le travail de la séance C2. Faire remarquer "
             "qu'elle dit la même chose en mots ordinaires, sans rien enlever.")

    d.dialogue('Dialogue · 3 de 3', "Ce qu'un avis lu sans réponse veut dire", [
        ("MARIAMA", "Est-ce qu'il a le droit d'entrer chez moi comme ça ?", True),
        ("KIM", "Pour des travaux, oui, mais il doit t'avertir vingt-quatre "
                "heures d'avance, et venir entre sept heures du matin et sept "
                "heures du soir.", True),
        ("MARIAMA", "Il y a une dernière ligne, en petit : « Le bruit des "
                    "appareils est important et continu. »", True),
        ("KIM", "Écris-le au propriétaire aujourd'hui même. Un avis qu'on lit "
                "sans répondre, c'est un avis qu'on accepte.", True),
    ], notes="La dernière réplique fait le pont avec le défi 3 : la ligne en petit sur le "
             "bruit deviendra la justification de la demande.")

    d.regle("Un avis dit toujours trois choses",
            "Ce qui va se passer, ce que vous devez faire, ce qui arrive sinon.",
            precision="Dans cet ordre, et toujours. La troisième partie commence par une "
                      "des trois formules : « à défaut », « le cas échéant », « faute de "
                      "quoi ». Les repérer, c'est trouver d'un coup d'œil le paragraphe "
                      "qui vous engage réellement.",
            notes="Diapositive à photographier. Elle vaut pour n'importe quel avis : "
                  "l'école, la ville, Hydro, l'assureur.")

    d.tableau('Les trois données de date', "Un avis complet les donne toutes",
              ['La donnée', 'Dans l\'avis de Mariama'],
              [["le premier jour", "du mercredi 12 novembre"],
               ["le dernier jour", "au vendredi 14 novembre"],
               ["la plage horaire", "entre 8 h et 17 h"],
               ["ce qui manque souvent", "l'heure — et vous avez le droit de la demander"]],
              cle=0,
              note="Un avis qui donne un jour sans heure est incomplet.",
              notes="Faire calculer au groupe combien de temps ça fait au total : trois "
                    "jours, neuf heures par jour. La durée réelle surprend toujours.")

    d.regle("Quand un propriétaire peut entrer",
            "Vingt-quatre heures d'avance, entre 7 h et 19 h.",
            precision="Pour des travaux ou une visite, il doit vous prévenir vingt-quatre "
                      "heures d'avance et venir entre sept heures du matin et sept heures "
                      "du soir. L'avis affiché est justement cet avertissement. La seule "
                      "exception est l'urgence — une fuite en cours : là, il entre sans "
                      "préavis, et c'est dans votre intérêt.",
            notes="Question fréquente et anxiogène. Répondre avec précision : le droit "
                  "existe des deux côtés et il est encadré.")

    d.pratique('Pratique · exercice t2a', "Vrai ou Faux — L'avis affiché",
               "Écoutez le dialogue, puis répondez.",
               [("L'avis était affiché depuis plusieurs jours.", "FAUX"),
                ("Les travaux touchent les logements 3 et 4.", "VRAI"),
                ("Les ouvriers passeront entre 8 h et 17 h.", "VRAI"),
                ("L'avis demande aux occupants de quitter le logement.", "FAUX"),
                ("Si personne n'ouvre, l'entrepreneur appellera le propriétaire.", "VRAI"),
                ("Le propriétaire peut entrer sans avertir, n'importe quand.", "FAUX")],
               corrige=True,
               notes="Six des neuf énoncés. Les trois autres se font dans l'activité "
                     "interactive.")

    d.billet(
        "Notez les trois données de date de l'avis, de mémoire.",
        exemples=[
            "Premier jour, dernier jour, plage horaire.",
            "Puis : qu'est-ce que ça vous enlève, à vous ?",
        ],
        notes="Deux minutes. La seconde question prépare le défi 3 : peu d'élèves y "
              "pensent seuls la première fois.")

    return d.save(dossier)
