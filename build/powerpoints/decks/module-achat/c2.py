# -*- coding: utf-8 -*-
"""C2 · Quand ça va arriver.
Bloc C · couleur ambre (écriture) · 75 min.
Source : mini-leçon `t2futur`, exercice `t2futur`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Quand ça va arriver',
        chapeau="« Ils vont livrer jeudi. » « On vous appellera la veille. » "
                "Deux façons de parler du futur : celle de la conversation, et "
                "celle des engagements.",
        duree='75 minutes')

    d.titre(notes="Écrire les deux phrases du chapeau au tableau et demander laquelle "
                  "vient du magasin. Le groupe sent la différence de registre.")

    d.objectifs([
        "employer le futur proche : aller + infinitif ;",
        "former le futur simple sur l'infinitif ;",
        "connaître cinq verbes irréguliers au futur ;",
        "comprendre un engagement de livraison.",
    ])

    d.tableau('Analyse', "Deux futurs, deux usages",
              ['La forme', 'Quand on l\'emploie'],
              [["aller + infinitif", "décidé, prévu, tout proche — à l'oral"],
               ["futur simple", "engagement, promesse, écrit officiel"],
               ["Les deux", "corrects presque partout"]],
              cle=1,
              note="Le magasin s'engage au futur simple ; vous pouvez répondre au futur proche.",
              notes="Diapo centrale. Faire recopier. La note lève l'inquiétude du choix.")

    d.regle("Le futur proche : un verbe que vous connaissez",
            "aller au présent, puis l'infinitif.",
            precision="« Ils <b>vont livrer</b> jeudi. » · « Je <b>vais prendre</b> "
                      "l'installation. » · « Nous <b>allons payer</b> en douze "
                      "versements. » Aucune forme nouvelle à apprendre : c'est le verbe "
                      "aller que vous employez déjà.",
            notes="Faire produire six formes par six élèves, une par personne du verbe "
                  "aller.")

    d.regle("Le futur simple : l'infinitif plus une terminaison",
            "-ai, -as, -a, -ons, -ez, -ont.",
            precision="livrer › je livrer<b>ai</b>, il livrer<b>a</b>, ils livrer<b>ont</b>. "
                      "Les verbes en <b>-re</b> perdent leur e : prendre › je prendr<b>ai</b>. "
                      "Les terminaisons sont les mêmes pour tous les verbes, sans exception.",
            notes="Écrire les six terminaisons au tableau et les y laisser. Elles ne "
                  "changent jamais.")

    d.cartes('Cinq irréguliers', "La base change, pas la terminaison", [
        ("être › je serai · avoir › j'aurai",
         "Les deux plus fréquents. « La livraison sera gratuite. » « Vous aurez un an de "
         "garantie. »"),
        ("aller › j'irai · faire › je ferai",
         "« J'irai au magasin samedi. » « Ils feront l'installation jeudi. »"),
        ("venir › je viendrai",
         "« Le technicien viendra l'après-midi. » Très employé dans les rendez-vous de "
         "service."),
        ("Et quelques doublements",
         "appeler › j'appellerai · jeter › je jetterai. Une petite liste, pas une règle "
         "générale."),
    ], notes="Ces cinq-là couvrent la majorité des phrases au futur qu'on entend dans un "
             "magasin. Les apprendre comme une liste.")

    d.piege("Former le futur sur autre chose que l'infinitif",
            "je livrai, je prendai",
            "je livrerai, je prendrai",
            "La base du futur simple est l'infinitif entier, pas le radical. « Livrer » "
            "donne « je livrerai » — avec le -er au complet. C'est plus simple qu'il n'y "
            "paraît : on ajoute, on n'enlève rien.",
            notes="Le dire ainsi rassure : le futur simple est un des temps les plus "
                  "réguliers du français.")

    d.pratique('Pratique · 1 de 2', "Futur proche",
               "Mettez au futur proche.", [
        ("Ils (livrer) jeudi prochain.", "Ils vont livrer jeudi prochain."),
        ("Je (prendre) l'installation.", "Je vais prendre l'installation."),
        ("Nous (payer) en douze versements.", "Nous allons payer en douze versements."),
        ("Elle (choisir) le modèle silencieux.", "Elle va choisir le modèle silencieux."),
    ], corrige=True, cols=1,
       notes="Aucune difficulté de forme : c'est le verbe aller plus l'infinitif.")

    d.pratique('Pratique · 2 de 2', "Futur simple",
               "Mettez au futur simple.", [
        ("On vous (appeler) la veille.", "On vous appellera la veille."),
        ("Le technicien (venir) l'après-midi.", "Le technicien viendra l'après-midi."),
        ("La livraison (être) gratuite.", "La livraison sera gratuite."),
        ("Vous (avoir) un an de garantie.", "Vous aurez un an de garantie."),
        ("Ils (reprendre) l'ancienne laveuse.", "Ils reprendront l'ancienne laveuse."),
    ], corrige=True, cols=1,
       notes="Trois irréguliers sur cinq lignes : c'est représentatif de ce qu'on entend "
             "dans un magasin.")

    d.cartes("Comprendre un engagement", "Trois phrases du magasin", [
        ("« On vous appellera la veille. »",
         "Un engagement de contact. S'il n'est pas tenu, vous pouvez le rappeler."),
        ("« Le technicien viendra l'après-midi. »",
         "Un créneau, pas une heure. Prévoyez la demi-journée."),
        ("« La livraison sera gratuite au-dessus de mille dollars. »",
         "Une condition. Vérifiez si votre total, taxes comprises ou non, l'atteint."),
    ], notes="La troisième carte annonce la séance C3 : le prix affiché n'est pas le "
             "total.")

    d.billet(
        "Écrivez six phrases au futur sur un achat que vous ferez.",
        exemples=[
            "Trois au futur proche, trois au futur simple.",
            "Employez au moins deux verbes irréguliers.",
        ],
        notes="Corriger surtout la base du futur simple : l'infinitif entier.")

    return d.save(dossier)
