# -*- coding: utf-8 -*-
"""C3 · Lire une étiquette de prix.
Bloc C « Défi 2 · Comparer deux prix » · couleur teal · 60 min.
Source : dialogue `t2b`, exercices `t2etiquette` et `t2b`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-vetements/images/')


def build(dossier):
    d = Deck(
        code='C3', section='teal',
        titre='Lire une étiquette de prix',
        chapeau="Une grande affiche annonce trente pour cent de rabais. Elle "
                "ne dit pas sur quoi. La réponse est sur la petite étiquette "
                "attachée au vêtement.",
        duree='60 minutes')

    d.titre(notes="Séance d'écoute et de lecture. C'est l'intention « lire une étiquette » "
                  "du programme, appliquée au prix. L'entretien viendra en D1.")

    d.objectifs([
        "comprendre qu'un rabais ne s'applique pas à tout le magasin ;",
        "lire les six mentions d'une étiquette de prix ;",
        "savoir que le vrai prix apparaît à la caisse ;",
        "signaler poliment un prix qui ne correspond pas.",
    ])

    d.declencheur(
        'Observation', "Trente pour cent de rabais — sur quoi ?",
        image=IMG + 'affiche-rabais.jpg',
        pistes=[
            "Sur tout le magasin ?",
            "Sur une partie seulement ?",
            "Comment le savoir ?",
            "Où faut-il regarder ?",
        ],
        notes="Presque personne ne répond « sur une partie seulement ». C'est pourtant le "
              "cas le plus fréquent, et c'est écrit en petit sous l'affiche.")

    d.dialogue('Dialogue · 1 de 2', "Sur les chandails seulement", [
        ("FARIDA", "Il y a une grande affiche : trente pour cent de rabais.", True),
        ("JOCELYNE", "Oui, sur les chandails seulement. Pas sur les manteaux.", True),
        ("FARIDA", "Comment je fais pour savoir ?", True),
        ("JOCELYNE", "Regardez la petite étiquette. Si elle est rouge, l'article est en rabais.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="La couleur de l'étiquette est un vrai repère, employé par la plupart des "
             "magasins d'ici. Ce n'est pas une règle universelle, mais elle est fiable.")

    d.dialogue('Dialogue · 2 de 2', "Le vrai prix est à la caisse", [
        ("FARIDA", "Trente-neuf dollars quatre-vingt-dix-neuf.", True),
        ("JOCELYNE", "C'est le prix régulier. Avec le rabais, ça fait environ vingt-huit dollars.", True),
        ("FARIDA", "Et si ce n'est pas le bon prix ?", True),
        ("JOCELYNE", "Vous le dites tout de suite. On corrige, ça arrive souvent.", True),
    ], notes="Deux choses à retenir : le rabais se calcule à la caisse, et une erreur se "
             "signale sans gêne.")

    d.tableau('Analyse · 1 de 2', "Ce qui est écrit en gros",
              ['Ce qui est écrit', 'Ce que ça veut dire'],
              [["Prix régulier 130,00 $", "le prix des autres semaines"],
               ["50 % de rabais", "on enlève la moitié"],
               ["Liquidation", "les derniers articles"]],
              cle=0,
              note="Ces trois mentions parlent du prix qu'on paie aujourd'hui.",
              notes="Diapo à photographier. Apporter une vraie étiquette si possible.")

    d.tableau('Analyse · 2 de 2', "Ce qui est écrit en petit",
              ['Ce qui est écrit', 'Ce que ça veut dire'],
              [["2 pour 25 $", "il faut en prendre deux"],
               ["Vente finale", "ni retour ni échange"],
               ["Taxes en sus", "le prix va monter à la caisse"]],
              cle=1,
              note="Écrit petit, mais c'est le plus important.",
              notes="Insister sur « taxes en sus » : sur les vêtements, il y en a, "
                    "contrairement aux aliments de base.")

    d.regle("Le vrai prix apparaît à la caisse",
            "C'est là qu'il faut vérifier.",
            precision="Le rabais n'est presque jamais réécrit sur l'étiquette : c'est la "
                      "caisse qui l'applique. Regarder l'écran pendant que le caissier "
                      "passe les articles, et vérifier la facture avant de partir. Un prix "
                      "qui ne correspond pas se corrige en trente secondes.",
            notes="Diapo à photographier. Faire remarquer que « ça arrive souvent » est "
                  "dit par la conseillère elle-même : ce n'est pas une accusation.")

    d.cartes("Trois façons de calculer vite", "Sans calculatrice", [
        ("10 %",
         "On enlève le dernier chiffre : 10 % de 40 $, c'est 4 $. Le prix devient 36 $."),
        ("50 %",
         "C'est la moitié : 50 % de 130 $, c'est 65 $. Le calcul le plus facile, et le "
         "rabais le plus fréquent en liquidation."),
        ("30 %",
         "C'est trois fois 10 % : 30 % de 40 $, c'est 12 $. Le prix devient 28 $. Ça "
         "donne un ordre de grandeur, ce qui suffit pour décider."),
    ], notes="Faire calculer trois exemples au tableau avec le groupe. L'ordre de grandeur "
             "suffit : il s'agit de décider, pas de vérifier la caisse.")

    d.piege("Croire que l'affiche vaut pour tout",
            "Trente pour cent, donc mon manteau aussi.",
            "Regardez la petite étiquette.",
            "Une affiche annonce un rabais sur une famille d'articles, rarement sur tout "
            "le magasin. La petite étiquette du vêtement, elle, dit la vérité — souvent "
            "par sa couleur.",
            notes="C'est la déception la plus fréquente à la caisse. La prévenir vaut "
                  "mieux que la corriger.")

    d.pratique('Pratique · 1 de 2', "Qu'est-ce que ça veut dire ?",
               "Associez chaque mention à son sens.", [
        ("« Prix régulier 130,00 $ »", "le prix des autres semaines"),
        ("« 50 % de rabais »", "on enlève la moitié"),
        ("« Liquidation »", "les derniers articles"),
        ("« 2 pour 25 $ »", "il faut en prendre deux"),
        ("« Vente finale »", "ni retour ni échange"),
        ("« Taxes en sus »", "le prix monte à la caisse"),
    ], corrige=True,
       notes="Utiliser l'exercice 3 du défi 2.")

    d.pratique('Pratique · 2 de 2', "Vrai ou faux ?",
               "D'après le dialogue « Trente pour cent de rabais ».", [
        ("Le rabais vaut pour tout le magasin.", "faux — les chandails seulement"),
        ("L'étiquette rouge signale un rabais.", "vrai"),
        ("39,99 $ est le prix régulier.", "vrai"),
        ("Avec le rabais, le chandail coûte environ 28 $.", "vrai"),
        ("Le vrai prix apparaît à la caisse.", "vrai"),
        ("Il ne faut jamais signaler un prix erroné.", "faux — on le dit tout de suite"),
    ], corrige=True,
       notes="Utiliser l'exercice 5 du défi 2.")

    d.billet(
        "Calculez le prix de trois vêtements avec 30 % de rabais.",
        exemples=[
            "Prenez des prix réels, vus en magasin ou dans une circulaire.",
            "Écrivez le calcul, pas seulement le résultat.",
        ],
        notes="Devoir de calcul. Corriger l'ordre de grandeur plutôt que la précision au "
              "cent près.")

    return d.save(dossier)
