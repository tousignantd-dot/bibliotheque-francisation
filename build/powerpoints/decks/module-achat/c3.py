# -*- coding: utf-8 -*-
"""C3 · Le prix affiché n'est pas le total.
Bloc C · couleur ambre (écriture) · 75 min.
Source : mini-leçon `t2paiement`, exercice `t2paiement`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Le prix affiché n'est pas le total",
        chapeau="Un appareil affiché à 800 $ peut en coûter 1 100. Taxes, "
                "livraison, installation, garantie prolongée : quatre lignes "
                "qui s'ajoutent, et qu'on peut toutes prévoir.",
        duree='75 minutes')

    d.titre(notes="Écrire « 800 $ » au tableau et demander combien on paiera vraiment. Les "
                  "estimations du groupe sont presque toujours trop basses.")

    d.objectifs([
        "calculer les taxes de tête, approximativement ;",
        "distinguer la livraison de l'installation ;",
        "comprendre ce que veut dire « douze versements sans intérêt » ;",
        "faire écrire ce qui a été promis.",
    ])

    d.tableau('Analyse', "Ce qui s'ajoute au prix affiché",
              ['Ligne', 'Combien'],
              [["Les taxes", "environ 15 %"],
               ["La livraison", "50 à 80 $, parfois gratuite"],
               ["L'installation", "un service à part, souvent 40 $"],
               ["La garantie prolongée", "facultative, 100 à 200 $"]],
              cle=0,
              note="Sur 800 $, le total dépasse fréquemment 1 000 $.",
              notes="Diapo à photographier. Faire le total avec le groupe, ligne par ligne.")

    d.regle("Calculer les taxes de tête",
            "Ajoutez le dixième, puis la moitié de ce dixième.",
            precision="800 $ › 80 $ + 40 $ = 120 $. Total : 920 $. Le calcul est "
                      "approximatif mais suffisant pour décider. Au Québec, les taxes ne "
                      "sont jamais incluses dans le prix affiché — c'est différent de "
                      "beaucoup de pays.",
            notes="Faire pratiquer sur trois montants au tableau. Après trois fois, le "
                  "calcul devient automatique.")

    d.regle("Monter n'est pas brancher",
            "La livraison apporte l'appareil. L'installation le met en marche.",
            precision="Les livreurs montent l'appareil à l'endroit voulu et repartent avec "
                      "l'emballage. Ils ne raccordent ni l'eau, ni l'électricité, ni le "
                      "renvoi. C'est la surprise la plus fréquente du jour de la "
                      "livraison.",
            notes="Diapo à photographier. La question à poser au moment de l'achat : "
                  "« est-ce que l'installation est comprise ? »")

    d.cartes("Les versements", "Ce que « sans intérêt » veut dire", [
        ("Le principe",
         "Le prix divisé en douze, sans frais supplémentaires. Douze mois pour payer un "
         "appareil au lieu d'un seul."),
        ("La condition",
         "Payer à temps chaque mois. Un retard fait souvent tomber la gratuité et applique "
         "un taux élevé sur tout le solde restant."),
        ("Où c'est écrit",
         "En petit, dans le contrat. Lisez la ligne qui commence par « en cas de retard » "
         "avant de signer."),
    ], notes="Point financier important : le taux appliqué après un retard dépasse souvent "
             "20 %. Le dire sans dramatiser.")

    d.piege("Ne rien faire écrire",
            "Le vendeur a dit qu'ils reprendraient l'ancienne laveuse.",
            "C'est noté sur le bon de livraison ?",
            "Une promesse orale ne voyage pas jusqu'au livreur. Le bon de livraison est le "
            "seul document que l'équipe de livraison consulte. Tout ce qui n'y est pas "
            "écrit n'arrivera pas — la reprise de l'ancien appareil en particulier.",
            notes="C'est exactement ce que dit le livreur dans le dialogue t2b. Faire le "
                  "lien.")

    d.pratique('Pratique · 1 de 2', "Calculez le total",
               "Appareil à 800 $. Ajoutez les lignes demandées.", [
        ("Avec les taxes seulement", "environ 920 $"),
        ("Plus la livraison à 60 $", "environ 980 $"),
        ("Plus l'installation à 40 $", "environ 1 020 $"),
        ("Plus la garantie prolongée à 120 $", "environ 1 140 $"),
    ], corrige=True, cols=1,
       notes="Faire le calcul au tableau, ligne par ligne. L'écart avec le prix affiché "
             "frappe.")

    d.pratique('Pratique · 2 de 2', "Quel service ?",
               "Livraison, installation, ou ni l'un ni l'autre ?", [
        ("Descendre l'appareil du camion", "livraison"),
        ("Le monter jusqu'au sous-sol", "livraison"),
        ("Brancher l'eau et l'électricité", "installation"),
        ("Vérifier que l'appareil est de niveau", "installation"),
        ("Repartir avec l'ancien appareil", "ni l'un ni l'autre — c'est la reprise"),
    ], corrige=True, cols=1,
       notes="La dernière ligne introduit un troisième service, souvent gratuit mais "
             "toujours à faire noter.")

    d.cartes("Les quatre questions du paiement", "À poser avant de signer", [
        ("« Ça fait combien, taxes comprises ? »",
         "Le seul chiffre qui compte vraiment."),
        ("« L'installation est-elle comprise ? »",
         "La réponse est presque toujours non. Autant le savoir."),
        ("« Vous reprenez l'ancien appareil ? »",
         "Souvent oui, souvent gratuit — mais seulement si c'est noté."),
        ("« Qu'est-ce qui arrive si je paie en retard ? »",
         "Pour les versements. La réponse est dans le contrat, en petit."),
    ], notes="Diapo à photographier. Ces quatre questions couvrent tout ce qui coûte cher "
             "et se règle en trente secondes.")

    d.billet(
        "Calculez le total réel d'un appareil qui vous intéresse.",
        exemples=[
            "Prix affiché, taxes, livraison, installation.",
            "Notez l'écart avec le prix affiché.",
        ],
        notes="Devoir concret. L'écart calculé surprend et se retient.")

    return d.save(dossier)
