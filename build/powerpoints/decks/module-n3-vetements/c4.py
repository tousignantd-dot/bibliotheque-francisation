# -*- coding: utf-8 -*-
"""C4 · Celui-ci, celui-là.
Bloc C « Défi 2 · Comparer deux prix » · couleur ambre (écriture) · 60 min.
Source : exercice `t2celui`, mini-leçon `t2celui`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre='Celui-ci, celui-là',
        chapeau="Devant deux manteaux, on ne répète pas le mot « manteau » "
                "trois fois. Quatre petits mots le remplacent — et ils vont "
                "avec le doigt qui montre.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture. Poser deux objets devant la classe et demander de "
                  "les comparer sans les nommer : le besoin apparaît tout seul.")

    d.objectifs([
        "employer celui, celle, ceux, celles ;",
        "distinguer -ci (près) et -là (plus loin) ;",
        "ne pas confondre avec « ce » et « cette » ;",
        "comparer deux articles sans répéter leur nom.",
    ])

    d.declencheur(
        'Question', "Comment comparer sans répéter le mot ?",
        pistes=[
            "« Le manteau bleu est moins cher que le manteau noir. »",
            "Combien de fois dit-on « manteau » ?",
            "Comment faire plus court ?",
            "Et si vous montrez du doigt ?",
        ],
        notes="Faire produire la phrase longue, puis demander de l'alléger. Le besoin du "
              "pronom démonstratif se sent avant qu'on l'explique.")

    d.tableau('Analyse', "Quatre formes, selon le vêtement",
              ['Le vêtement', 'On dit'],
              [["un manteau", "celui-ci · celui-là"],
               ["une tuque", "celle-ci · celle-là"],
               ["des gants", "ceux-ci · ceux-là"],
               ["des bottes", "celles-ci · celles-là"]],
              cle=0,
              note="C'est le seul endroit où il faut connaître le genre du vêtement.",
              notes="Diapo centrale, à photographier. Renvoyer à la séance A4 : le genre "
                    "appris là sert ici pour la première fois.")

    d.regle("-ci pour près, -là pour plus loin",
            "« Celui-ci est en nylon, celui-là est en laine. »",
            precision="On les emploie presque toujours par deux, pour opposer deux "
                      "articles. Seul, « celui-là » suffit quand on montre du doigt. Et "
                      "montrer du doigt dans un magasin est parfaitement poli : c'est même "
                      "plus clair qu'une longue description.",
            notes="Diapo à photographier. Faire pratiquer avec des objets réels de la "
                  "classe, un près et un loin.")

    d.cartes("Trois phrases à savoir par cœur", "Elles servent tous les jours", [
        ("Demander un prix",
         "« Celle-ci est à combien ? » — en montrant du doigt. Plus rapide que de décrire "
         "le vêtement."),
        ("Demander un rabais",
         "« Ceux-là sont en rabais ? » — la question qui évite la surprise à la caisse."),
        ("Dire son choix",
         "« Je préfère celles-là. » — la phrase qui termine une comparaison, et qui dit au "
         "vendeur ce qu'il doit aller chercher."),
    ], notes="Faire répéter les trois à voix haute, avec le geste. Le geste fait partie de "
             "la phrase.")

    d.regle("Ne pas confondre avec « ce » et « cette »",
            "<b>ce</b> manteau · <b>celui-ci</b>",
            precision="« Ce » est suivi du nom ; « celui-ci » remplace le nom. On dit « ce "
                      "manteau-ci » ou « celui-ci » — jamais « ce celui-ci ». Les deux "
                      "disent exactement la même chose ; le second est simplement plus "
                      "court.",
            notes="Diapo à photographier. L'erreur « ce celui-ci » est rare mais tenace "
                  "quand elle s'installe.")

    d.piege("Employer « celui » tout seul",
            "Celui est moins cher.",
            "Celui-ci est moins cher.",
            "« Celui » ne se dit jamais seul dans cette phrase : il lui faut « -ci », "
            "« -là », ou une suite comme « celui que je préfère ». Sans cela, la phrase "
            "n'est pas terminée.",
            notes="Faire compléter cinq phrases fautives au tableau, à l'oral.")

    d.pratique('Pratique', "Celui-ci ou celui-là ?",
               "Vous montrez ce qui est près de vous (-ci) ou plus loin (-là).", [
        ("Un manteau tout près : « Je voudrais essayer ___ . »", "celui-ci"),
        ("Une tuque au bout du rayon : « ___ est à combien ? »", "celle-là"),
        ("Des bottes près de vous : « ___ sont en liquidation ? »", "celles-ci"),
        ("Des gants plus loin : « Je prends ___ . »", "ceux-là"),
        ("Deux chandails : « ___ est plus chaud que celui-là. »", "celui-ci"),
    ], corrige=True, cols=1,
       notes="Utiliser l'exercice 4 du défi 2. Faire accompagner chaque réponse du geste.")

    d.billet(
        "Écrivez cinq phrases qui comparent deux vêtements, sans les nommer deux fois.",
        exemples=[
            "Ex. : « Celui-ci est moins cher que celui-là. »",
            "Variez : masculin, féminin, singulier, pluriel.",
        ],
        notes="Fin du défi 2. Ramasser : ces phrases se réemploient telles quelles dans la "
              "production orale de E1.")

    return d.save(dossier)
