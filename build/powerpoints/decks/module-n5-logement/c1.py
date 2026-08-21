# -*- coding: utf-8 -*-
"""C1 · La visite du quatre et demie.
Bloc C « Défi 2 · La visite » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-logement/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="La visite du quatre et demie",
        chapeau="Une visite dure quinze minutes. C'est court pour voir un "
                "logement où on habitera un an.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2. Commencer par la troisième colonne des feuilles "
                  "d'appel du devoir B4 : ce sont les vraies questions de visite du "
                  "groupe. Les écrire au tableau.")

    d.objectifs([
        "comprendre les renseignements donnés pendant une visite ;",
        "repérer ce qu'un propriétaire dit spontanément et ce qu'il faut demander ;",
        "poser la question du loyer de l'ancien locataire ;",
        "savoir quoi regarder, et pas seulement quoi écouter.",
    ])

    d.declencheur(
        'Observation', "Vous entrez dans ce logement. Que regardez-vous en premier ?",
        image=IMG + 'salon-ensoleille.jpg',
        pistes=[
            "La lumière ? Les planchers ? Les fenêtres ?",
            "Qu'est-ce qu'on ne peut pas voir en quinze minutes ?",
            "Comment savoir s'il fait froid l'hiver ?",
            "Comment savoir si les voisins sont bruyants ?",
        ],
        notes="Faire dire ce qui ne se voit pas : le bruit, le froid, l'humidité en "
              "automne, le déneigement. Ces choses-là se demandent — c'est tout l'objet "
              "de la séance.")

    d.dialogue('Dialogue · 1 de 4', "Entrer et regarder", [
        ("HÉLÈNE", "Entrez, entrez. Vous enlevez vos bottes, si ça ne vous dérange pas.", True),
        ("NADÈGE", "Bien sûr. Oh, c'est clair, ici.", True),
        ("HÉLÈNE", "C'est la pièce que tout le monde aime. Les fenêtres donnent au "
                   "sud, alors le salon est ensoleillé jusqu'à quatre heures.", True),
        ("NADÈGE", "Et le plancher, c'est du bois franc ?", False),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Enlever ses bottes est un usage d'ici, en toute saison et dans presque toutes "
             "les maisons. Le dire : c'est une information culturelle utile et rarement "
             "enseignée.")

    d.dialogue('Dialogue · 2 de 4', "Les pièces", [
        ("HÉLÈNE", "Du bois franc dans le salon et dans le corridor. Les chambres, "
                   "c'est du flottant, refait l'an dernier.", True),
        ("NADÈGE", "Il y a deux chambres ?", True),
        ("HÉLÈNE", "Deux vraies chambres, oui. Celle-ci donne sur la cour, donc "
                   "c'est la plus tranquille. En arrivant, vous avez vu la ruelle : "
                   "c'est de ce côté-là qu'il y a du passage.", True),
        ("NADÈGE", "Ma fille prendrait celle qui donne sur la cour, alors. Est-ce que "
                   "c'est insonorisé entre les logements ?", True),
    ], notes="Deux points de langue à venir sont ici : le relatif « qui donne sur la cour » "
             "et le gérondif « en arrivant ». Les souligner sans les expliquer — ils sont "
             "l'objet des séances C3 et C4.")

    d.dialogue('Dialogue · 3 de 4', "Ce qui n'est pas parfait", [
        ("HÉLÈNE", "Honnêtement, on entend marcher au-dessus. Ce n'est pas un "
                   "immeuble neuf. Les voisins d'en haut sont un couple retraité, "
                   "très tranquilles.", True),
        ("NADÈGE", "Merci de me le dire. Et la cuisine, la hotte fonctionne ?", True),
        ("HÉLÈNE", "Elle fonctionne. Le poêle et le réfrigérateur restent. Là, "
                   "derrière la porte, c'est une remise : c'est petit, mais ça prend "
                   "deux vélos.", True),
        ("NADÈGE", "Ça, c'est utile.", True),
    ], notes="Hélène annonce un défaut sans qu'on le lui demande. Faire remarquer que "
             "Nadège la remercie : un défaut annoncé d'avance est une information ; "
             "découvert après la signature, c'est un conflit.")

    d.dialogue('Dialogue · 4 de 4', "La question qui compte", [
        ("NADÈGE", "Une dernière chose, madame : depuis quand le loyer n'a pas "
                   "augmenté ?", True),
        ("HÉLÈNE", "Bonne question. Le locataire actuel payait mille vingt dollars, "
                   "et il est ici depuis trois ans. Je vais l'écrire dans le bail, "
                   "c'est obligatoire.", True),
        ("NADÈGE", "Je vous remercie. En regardant les autres logements cette "
                   "semaine, je vais comparer, mais je vous rappelle vendredi.", True),
        ("HÉLÈNE", "Prenez le temps qu'il faut. Je garde votre numéro.", True),
    ], notes="La réponse d'Hélène — 1 020 $ pour un logement offert à 1 050 $ — est une "
             "hausse normale. Faire calculer l'écart : trente dollars, soit moins de 3 %.")

    d.cartes("Quoi regarder pendant la visite", "Quatre choses qui coûtent cher après", [
        ("Les fenêtres",
         "Ouvrez-en une, fermez-la. Si elle coince, l'hiver sera froid et la facture salée."),
        ("Le panneau de disjoncteurs",
         "Demandez où il est. Vous en aurez besoin le premier soir où tout s'éteint."),
        ("Les taches au plafond",
         "Une marque d'humidité se demande : d'où vient-elle, et a-t-elle été réparée ?"),
        ("L'escalier et l'entrée",
         "Vous le monterez chargé de sacs, et vous le déneigerez tout l'hiver."),
    ], notes="Faire ajouter au groupe ce qu'ils ont appris à leurs dépens dans leur "
             "logement actuel. Cette liste s'allonge toujours, et les meilleures entrées "
             "viennent des élèves.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Les fenêtres du salon donnent au nord.", "faux — au sud"),
        ("Il y a du bois franc dans le salon et le corridor.", "vrai"),
        ("La chambre qui donne sur la cour est la plus tranquille.", "vrai"),
        ("Hélène cache que l'immeuble est mal insonorisé.", "faux — elle le dit d'elle-même"),
        ("Le poêle et le réfrigérateur restent dans le logement.", "vrai"),
        ("Le locataire actuel payait mille cent dollars.", "faux — mille vingt"),
        ("Nadège veut comparer avant de décider.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Regardez votre logement actuel avec les yeux d'un visiteur.",
        exemples=[
            "Notez trois choses que vous auriez voulu savoir avant de signer.",
            "Notez une chose que vous n'aviez pas remarquée pendant la visite.",
        ],
        notes="Devoir de réflexion. Les réponses alimentent la séance C2 et donnent des "
              "exemples réels, souvent frappants — plusieurs élèves habitent des logements "
              "avec des défauts qu'on ne leur avait pas signalés.")

    return d.save(dossier)
