# -*- coding: utf-8 -*-
"""B2 · Je peux, je dois, et ce que ça coûte.
Bloc B « Défi 1 · Au guichet automatique » · couleur ambre · 75 min.
Source : dialogue `t1b`, exercices `t1peux`, `t1notes`, `t1b`,
mini-leçons `t1peux`, `t1notes`, `t1b`.

Seconde séance du Défi 1. Le retrait est acquis depuis B1 ; ce qui manque,
c'est de savoir ce qu'on a le droit de faire et ce qu'on est obligé de
faire — et de comprendre le seul mot qui coûte de l'argent au guichet :
« frais ». C'est la séance qui protège le portefeuille.
"""
import os

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-guichet/images/')


def _photo(nom):
    """La photo si elle est sur le disque, sinon rien. Voir `a1.py`."""
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Je peux, je dois, et ce que ça coûte",
        chapeau="Dire ce qui est permis et ce qui est obligé au guichet, "
                "comprendre ce que sont des frais, et noter son retrait "
                "dans un carnet.",
        duree='75 minutes')

    d.titre(notes="Deuxième séance du Défi 1. Commencer par faire redire les six phrases "
                  "de l'écran, vues en B1 : elles doivent revenir sans lire. La séance "
                  "d'aujourd'hui ajoute ce qui entoure le retrait, pas le retrait "
                  "lui-même.")

    d.objectifs([
        "dire « je peux » quand c'est permis ;",
        "dire « je dois » quand c'est obligé ;",
        "comprendre ce que sont des frais de guichet ;",
        "écrire un retrait en quatre lignes dans un carnet.",
    ])

    d.declencheur(
        'Observation', "Combien d'argent est sorti de la machine ?",
        image=_photo('etape-billets.jpg'),
        pistes=[
            "Combien de billets voyez-vous ?",
            "Est-ce que le guichet donne toujours le montant exact ?",
            "Est-ce que retirer de l'argent coûte quelque chose ?",
            "Où avez-vous déjà vu un guichet, à part à votre caisse ?",
        ],
        notes="La troisième question surprend presque toujours : beaucoup pensent que "
              "retirer son propre argent est gratuit partout. Ne pas répondre tout de "
              "suite — le dialogue le fera.")

    d.regle("Je peux, c'est permis. Je dois, c'est obligé.",
            "Je peux choisir le montant. Je dois entrer mon NIP.",
            precision="Avec « je peux », j'ai le choix : je le fais ou je ne le fais "
                      "pas. Avec « je dois », rien ne marche si je ne le fais pas. "
                      "Après les deux, le verbe ne change jamais : je peux "
                      "prendre, je dois prendre.",
            notes="Diapositive à photographier. Faire chercher au groupe deux choses "
                  "qu'on doit faire à l'école, et deux qu'on peut faire. La règle "
                  "s'installe par les exemples des élèves, pas par la grammaire.")

    d.cartes("Au guichet, ce qui change", "Le choix et l'obligation", [
        ("Je dois", "entrer mon NIP · prendre ma carte · appuyer sur un bouton"),
        ("Je peux", "choisir 20, 40 ou 60 $ · demander un relevé · appuyer sur annuler"),
    ], cols=2, notes="Deux colonnes seulement, et beaucoup d'exemples dans chacune. Faire "
                     "ajouter au groupe une ligne dans chaque colonne, à partir de leur "
                     "propre caisse.")

    d.dialogue('Dialogue · 1 de 3', "L'écran écrit « des frais »", [
        ("AMADOU", "Monsieur Fontaine, l'écran écrit « des frais ». C'est quoi ?", True),
        ("CLAUDE", "C'est de l'argent en plus. Vous payez pour le retrait.", True),
        ("AMADOU", "Pourquoi ? Ici, c'est ma caisse.", True),
        ("CLAUDE", "Ici, non. Mais dans un magasin, oui : ce guichet n'est pas à nous.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire écouter deux fois, diapositive masquée. Le mot « frais » ne se devine "
             "pas : l'écrire au tableau avant de passer à la suite.")

    d.dialogue('Dialogue · 2 de 3', "Est-ce que je paie deux fois ?", [
        ("AMADOU", "Alors je paie deux fois ?", True),
        ("CLAUDE", "Un peu, oui. L'écran écrit le montant avant.", True),
        ("AMADOU", "Et je peux dire non ?", True),
        ("CLAUDE", "Oui. Vous appuyez sur « annuler » et vous reprenez la carte.", True),
    ], notes="« Je peux dire non » : c'est la phrase de la séance. La faire répéter par "
             "tout le groupe, deux fois.")

    d.dialogue('Dialogue · 3 de 3', "Toujours lire avant d'appuyer", [
        ("AMADOU", "D'accord. Je lis l'écran avant.", True),
        ("CLAUDE", "C'est ça. Toujours lire avant d'appuyer.", True),
    ], notes="Deux répliques, et c'est la conclusion du module entier. La laisser "
             "affichée pendant que le groupe recopie.")

    d.tableau('Analyse', "Les frais de guichet, ici",
              ["La question", "La réponse"],
              [["Où on en paie", "dans les guichets d'un magasin, d'un bar, d'un dépanneur"],
               ["Où on n'en paie pas", "au guichet de sa propre caisse ou de sa banque"],
               ["Ce que l'écran fait", "il écrit le montant des frais et il attend"],
               ["Ce qu'on peut faire", "appuyer sur « annuler » et aller à sa caisse"]],
              cle=1,
              note="Trois dollars de frais sur un retrait de vingt dollars, c'est "
                   "beaucoup. La machine du dépanneur est pratique, jamais gratuite.",
              notes="Diapositive à photographier. Demander qui a déjà payé des frais sans "
                    "le savoir : il y en a toujours, et ça vaut la discussion.")

    d.piege("Le mot qui trompe",
            "Le guichet est gratuit.",
            "Ce guichet-ci demande des frais.",
            "Un guichet automatique n'est pas gratuit partout. Celui de votre caisse "
            "l'est pour un retrait ordinaire ; celui du dépanneur ne l'est jamais. "
            "L'écran le dit toujours avant — il suffit de le lire.",
            notes="Faire relire l'écran d'un guichet de dépanneur si quelqu'un en a une "
                  "photo. Sinon, décrire : la ligne des frais est écrite en petit, mais "
                  "elle y est.")

    d.pratique('Écriture', "Je peux ou je dois ?",
               "Complétez avec « je peux » ou « je dois ».", [
        ("___ entrer mon NIP : c'est obligé.", "Je dois"),
        ("___ choisir vingt, quarante ou soixante dollars.", "Je peux"),
        ("___ prendre ma carte avant de partir.", "Je dois"),
        ("___ demander un relevé, ou non. C'est mon choix.", "Je peux"),
        ("Est-ce que je ___ retirer de l'argent ici ?", "peux"),
        ("Je ne ___ pas payer comptant au centre sportif.", "peux"),
    ], corrige=True, cols=2,
       notes="Les six mêmes phrases sont dans le module en ligne, exercice `t1peux`, avec "
             "sa mini-leçon.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Des frais, c'est de l'argent en plus.", "vrai"),
        ("Il y a des frais à tous les guichets.", "faux — pas à sa propre caisse"),
        ("L'écran écrit le montant des frais avant.", "vrai"),
        ("On ne peut pas dire non aux frais.", "faux — on appuie sur annuler"),
        ("Monsieur Fontaine dit de lire l'écran avant d'appuyer.", "vrai"),
    ], corrige=True, cols=1,
       notes="Les cinq mêmes énoncés sont dans le module en ligne, exercice `t1b`.")

    d.pratique('Pratique · seul', "Mon retrait dans mon carnet",
               "Quatre lignes, à remplir d'après le retrait d'Amadou.", [
        ("Opération :", "retrait"),
        ("Montant :", "40 dollars"),
        ("Nombre de billets :", "deux billets de 20 dollars"),
        ("Papier pris à la fin :", "le relevé"),
    ], corrige=True, cols=1,
       notes="Quinze minutes. Distribuer un vrai carnet de poche si l'école en a : les "
             "élèves qui notent leurs retraits ne se font pas surprendre à la fin du "
             "mois. C'est l'exercice `t1notes` du module en ligne.")

    d.billet(
        "Écrivez deux choses que vous devez faire au guichet, et une que vous pouvez faire.",
        exemples=[
            "Je dois entrer mon NIP.",
            "Je dois prendre ma carte.",
            "Je peux demander un relevé.",
        ],
        notes="Devoir court. Vérifier une seule chose à la correction : le verbe entier "
              "après « je peux » et « je dois ».")

    return d.save(dossier)
