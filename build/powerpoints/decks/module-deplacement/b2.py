# -*- coding: utf-8 -*-
"""B2 · L'impératif.
Bloc B · couleur ambre (écriture) · 90 min.
Source : mini-leçon `t1imper`, exercice `t1imper`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="L'impératif",
        chapeau="« Continuez tout droit. » « Tournez à gauche. » « Ne traversez "
                "pas le parc. » Un itinéraire est une suite d'ordres, et le "
                "français a un temps pour ça.",
        duree='90 minutes')

    d.titre(notes="Séance de grammaire longue et très rentable : l'impératif ressert dans "
                  "les recettes, les consignes de sécurité et les modes d'emploi.")

    d.objectifs([
        "employer l'impératif aux formes vous et tu ;",
        "savoir que le -s disparaît aux verbes en -er à la forme tu ;",
        "construire la forme négative avec ne et pas ;",
        "choisir entre tu et vous selon la personne à qui je parle.",
    ])

    d.tableau('Analyse', "Trois personnes, aucun sujet",
              ['Au présent', "À l'impératif"],
              [["vous continuez", "Continuez !"],
               ["tu continues", "Continue !"],
               ["nous continuons", "Continuons !"]],
              cle=0,
              note="Le sujet ne s'écrit jamais. Et au « tu », le -s des verbes en -er tombe.",
              notes="Diapo centrale. Faire recopier avant de continuer. Les deux "
                    "particularités sont dans la note.")

    d.regle('La forme vous — avec un inconnu',
            "Dans la rue, avec quelqu'un qu'on ne connaît pas, on vouvoie toujours.",
            precision="« Continuez », « tournez », « marchez », « prenez », « descendez », "
                      "« sortez », « passez ». C'est la forme du présent, sans le mot "
                      "« vous ». Aucune irrégularité.",
            notes="Faire produire les sept formes à voix haute par le groupe. Elles sont "
                  "toutes régulières : c'est la bonne nouvelle de la séance.")

    d.regle('La forme tu — et le -s qui tombe',
            "Aux verbes en -er, le -s du présent disparaît à l'impératif.",
            precision="« tu tournes » devient « tourne ! ». « tu traverses » devient "
                      "« traverse ! ». Les autres verbes gardent leur -s : « prends », "
                      "« sors », « descends ».",
            notes="C'est la faute la plus fréquente à l'écrit. Écrire les six formes au "
                  "tableau, trois en -er et trois autres, et les y laisser.")

    d.regle('La forme négative',
            "ne et pas entourent le verbe, comme partout ailleurs.",
            precision="« Ne traversez pas le parc s'il pleut. » · « Ne la manquez pas, elle "
                      "est petite. » À l'oral, le « ne » tombe presque toujours — on entend "
                      "« traversez pas ». À l'écrit, il est obligatoire.",
            notes="Faire le lien avec le « ne » de jamais, si le groupe a déjà fait le "
                  "module 11. Même mécanique, même faute.")

    d.piege('Le -s de trop',
            "Tournes à droite après la pharmacie.",
            "Tourne à droite après la pharmacie.",
            "« Tu tournes » prend un -s au présent. À l'impératif, ce -s disparaît — mais "
            "seulement aux verbes en -er. C'est arbitraire, il faut simplement le savoir. "
            "Le test : si l'infinitif finit en -er, pas de -s.",
            notes="Faire écrire cinq impératifs en -er au tableau par cinq élèves "
                  "différents. La répétition est ce qui installe cette règle.")

    d.pratique('Pratique · 1 de 2', "Mettez à l'impératif, forme vous",
               "Vous parlez à une personne que vous ne connaissez pas.", [
        ("(Continuer) ___ tout droit jusqu'au feu.", "Continuez"),
        ("(Tourner) ___ à gauche sur Chambly.", "Tournez"),
        ("(Prendre) ___ la ligne jaune jusqu'au terminus.", "Prenez"),
        ("(Descendre) ___ au troisième arrêt.", "Descendez"),
        ("(Ne pas manquer) ___ la rue, elle est petite.", "Ne manquez pas"),
        ("(Être) ___ prudent en traversant.", "Soyez"),
    ], corrige=True,
       notes="La dernière est irrégulière : soyez, ayez, sachez. Trois formes à reconnaître, "
             "surtout sur les affiches.")

    d.pratique('Pratique · 2 de 2', "Mettez à l'impératif, forme tu",
               "Vous parlez à un collègue de classe. Attention au -s.", [
        ("(Sortir) ___ par la porte principale.", "Sors"),
        ("(Traverser) ___ le parc par le sentier.", "Traverse"),
        ("(Marcher) ___ jusqu'au coin de la rue.", "Marche"),
        ("(Prendre) ___ celui de 7 h 51.", "Prends"),
        ("(Ne pas courir) ___, le plancher est mouillé.", "Ne cours pas"),
        ("(Tourner) ___ à droite après la caisse.", "Tourne"),
    ], corrige=True,
       notes="Les lignes 2, 3 et 6 sont en -er : pas de -s. Les lignes 1, 4 et 5 le "
             "gardent. Faire justifier chaque réponse.")

    d.cartes('Où vous le retrouverez', "L'impératif hors du chemin", [
        ("Dans les recettes",
         "« Mélangez, ajoutez, laissez reposer. » Toujours à la forme vous."),
        ("Sur les affiches de sécurité",
         "« Ne bloquez pas la sortie. » · « Soyez prudent. » · « Ayez votre titre en main. »"),
        ("Dans les modes d'emploi",
         "« Branchez l'appareil, appuyez sur le bouton. » Le temps de toutes les "
         "instructions écrites."),
    ], notes="Le dire au groupe : le travail d'aujourd'hui ressert loin du sujet du module. "
             "C'est ce qui justifie les quatre-vingt-dix minutes.")

    d.billet(
        "Écrivez six instructions à l'impératif pour venir de l'école chez vous.",
        exemples=[
            "Trois à la forme vous, trois à la forme tu.",
            "Au moins une à la forme négative.",
        ],
        notes="Corriger individuellement, surtout le -s de la forme tu. Rendre avant E1 : "
              "ce billet est le brouillon de la production écrite.")

    return d.save(dossier)
