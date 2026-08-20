# -*- coding: utf-8 -*-
"""A4 · Dans le magasin.
Bloc A « Je découvre » · couleur teal · 50 min.
Source : exercice `prImg`, cartes mémoire.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-vetements/images/')


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre='Dans le magasin',
        chapeau="Huit endroits et objets d'un magasin de vêtements, du "
                "présentoir au comptoir des échanges. Les nommer, c'est "
                "savoir où aller.",
        duree='50 minutes')

    d.titre(notes="Séance visuelle et courte. Elle clôt le bloc A.")

    d.objectifs([
        "nommer huit éléments d'un magasin de vêtements ;",
        "savoir où se fait un échange ;",
        "employer l'article juste : une cabine, la taille, un dépôt ;",
        "savoir ce qu'il faut garder après un achat.",
    ])

    d.declencheur(
        'Observation', "Où est-ce, et à quoi ça sert ?",
        image=IMG + 'cabines.jpg',
        pistes=[
            "Comment ça s'appelle ?",
            "Combien de vêtements peut-on y apporter ?",
            "Faut-il demander la permission ?",
            "Que fait-on des vêtements qu'on n'a pas pris ?",
        ],
        notes="Dans beaucoup de magasins, on donne un jeton avec le nombre d'articles. Les "
              "vêtements non pris se laissent au crochet prévu ou se rendent à la personne "
              "à l'entrée.")

    d.cartes('Où on essaie', "Quatre choses à savoir", [
        ("La cabine d'essayage",
         "Fermée par un rideau ou une porte. On peut y apporter plusieurs vêtements — "
         "souvent un maximum de six."),
        ("Le miroir",
         "Il y en a un dans la cabine, et souvent un grand dehors pour se voir de loin. "
         "Sortir pour se regarder est parfaitement normal."),
        ("Le jeton",
         "Dans certains magasins, on vous remet un numéro qui dit combien d'articles vous "
         "apportez. On le rend en sortant."),
        ("Ce qu'on ne peut pas essayer",
         "Les sous-vêtements et les maillots de bain, dans beaucoup de magasins. Ils ne "
         "sont pas non plus repris."),
    ], notes="La dernière carte prépare le bloc D : certains articles ne s'échangent jamais.")

    d.cartes("Où on paie et où on échange", "Deux comptoirs différents", [
        ("La caisse",
         "Pour payer. On y reçoit la facture — le papier à garder."),
        ("Le service à la clientèle",
         "Pour échanger, se faire rembourser, ou mettre de côté. Souvent un comptoir "
         "distinct, parfois au fond du magasin."),
        ("La facture",
         "Le papier sans lequel presque rien n'est possible. Photographiez-la : le papier "
         "des reçus s'efface en quelques mois."),
        ("La boîte",
         "Pour des chaussures, gardez-la : beaucoup de magasins l'exigent pour un "
         "échange."),
    ], notes="Diapo à photographier. Les deux dernières cartes évitent des refus "
             "d'échange très fréquents.")

    d.tableau('Analyse', "Le mot et l'endroit",
              ['Le mot', 'Où'],
              [["un présentoir", "où les vêtements sont suspendus"],
               ["une cabine d'essayage", "au fond, souvent en rangée"],
               ["la caisse", "pour payer"],
               ["le service à la clientèle", "pour échanger"]],
              cle=3,
              note="Ce ne sont pas les mêmes comptoirs : demandez où aller.",
              notes="Beaucoup de gens font la file à la caisse pour un échange, et sont "
                    "renvoyés au fond du magasin.")

    d.regle("Ce qu'il faut garder",
            "La facture, les étiquettes, et la boîte.",
            precision="La <b>facture</b> prouve la date d'achat. Les <b>étiquettes</b> "
                      "attachées prouvent que l'article n'a pas été porté. La <b>boîte</b> "
                      "est souvent exigée pour des chaussures. Sans ces trois-là, un "
                      "échange devient difficile ou impossible.",
            notes="Diapo à photographier. C'est le conseil pratique le plus rentable du "
                  "bloc A.")

    d.piege("Enlever les étiquettes tout de suite",
            "J'ai coupé l'étiquette en rentrant, avant de l'essayer une dernière fois.",
            "Je garde les étiquettes jusqu'à ce que je sois sûr.",
            "Un vêtement dont les étiquettes sont coupées est considéré comme porté. "
            "Gardez-les attachées le temps de décider — quelques jours suffisent, et cela "
            "ne coûte rien.",
            notes="Erreur très fréquente et impossible à réparer. Insister.")

    d.pratique('Pratique', "Le mot juste",
               "Complétez avec le mot du vocabulaire.", [
        ("Les ___ d'essayage sont au fond.", "cabines"),
        ("Vous faites quelle ___ ?", "taille"),
        ("Pour des bottes, on parle de ___ .", "pointure"),
        ("Le mode d'___ est sur l'étiquette du col.", "entretien"),
        ("Je voudrais faire un ___ .", "échange"),
        ("La mise de côté demande un ___ .", "dépôt"),
    ], corrige=True,
       notes="Ces six mots sont dans le banc de vocabulaire du module.")

    d.billet(
        "Notez ce que vous faites de vos factures.",
        exemples=[
            "Où les rangez-vous ? Combien de temps ?",
            "Prenez en photo la prochaine, et notez où la photo est rangée.",
        ],
        notes="Bilan du bloc A. Devoir minuscule, et qui change une habitude durablement.")

    return d.save(dossier)
