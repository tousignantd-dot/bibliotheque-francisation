# -*- coding: utf-8 -*-
"""D1 · L'addition.
Bloc D « Défi 3 · L'addition » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf`, `t3addition` et `t3payer`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-restaurant/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="L'addition",
        chapeau="Cinquante-huit dollars quarante, taxes comprises. Et le "
                "pourboire ? Il n'est pas sur l'addition — et au Québec, il "
                "fait partie du salaire du serveur.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc D. C'est la partie la plus utile du module pour "
                  "quelqu'un qui vient d'arriver : les usages du pourboire varient "
                  "énormément d'un pays à l'autre.")

    d.objectifs([
        "demander l'addition ;",
        "répondre à « ensemble ou séparé ? » ;",
        "comprendre que les taxes sont déjà comprises ;",
        "savoir que le pourboire s'ajoute, et combien.",
    ])

    d.declencheur(
        'Observation', "Le repas est fini. Que se passe-t-il maintenant ?",
        image=IMG + 'facture-table.jpg',
        pistes=[
            "Comment obtient-on l'addition ?",
            "Est-ce que les taxes sont déjà dedans ?",
            "Et le pourboire ?",
            "Comment ça se passe dans votre pays ?",
        ],
        notes="Cinq à dix minutes. La dernière piste est essentielle : dans plusieurs pays, "
              "le service est compris et le pourboire n'existe pas. Ce n'est pas le cas ici.")

    d.dialogue('Dialogue · 1 de 3', "Demander, et décider", [
        ("ANDRÉS", "L'addition, s'il vous plaît.", True),
        ("VINCENT", "Tout de suite. Ensemble ou séparé ?", True),
        ("ANDRÉS", "Ensemble, c'est moi qui invite.", True),
        ("MANON", "Andrés, non, on partage.", False),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="« Ensemble ou séparé ? » est posé avant l'impression. Une fois l'addition "
             "imprimée ensemble, la séparer prend plusieurs minutes.")

    d.dialogue('Dialogue · 2 de 3', "Le montant", [
        ("VINCENT", "Voilà. Cinquante-huit dollars et quarante, taxes comprises.", True),
        ("ANDRÉS", "Manon, le pourboire, c'est combien ici ?", True),
        ("MANON", "Quinze pour cent du montant avant taxes, en général. Ici, ça fait environ sept dollars et demi.", True),
        ("ANDRÉS", "Ce n'est pas sur l'addition ?", True),
    ], notes="« Taxes comprises » : le montant est final. Le pourboire, lui, s'ajoute. "
             "C'est la distinction centrale du bloc.")

    d.dialogue('Dialogue · 3 de 3', "Pourquoi ça compte", [
        ("MANON", "Non, tu l'ajoutes toi-même. Le terminal te propose des pourcentages, mais tu peux entrer le montant que tu veux.", True),
        ("ANDRÉS", "Et si le service n'était pas bon ?", False),
        ("MANON", "Tu peux donner moins. Mais ici, le pourboire fait partie du salaire du serveur, ce n'est pas juste un remerciement.", True),
    ], notes="La dernière réplique est le point culturel du module. Le salaire de base du "
             "personnel de service est plus bas au Québec, précisément parce que le "
             "pourboire est attendu.")

    d.tableau('Analyse', "Ce qui est compris, ce qui s'ajoute",
              ['Élément', 'Sur l\'addition ?'],
              [["Le prix des plats", "oui"],
               ["Les taxes", "oui, presque toujours comprises"],
               ["Le pourboire", "non — on l'ajoute soi-même"],
               ["Le service", "il n'existe pas comme ligne séparée ici"]],
              cle=2,
              note="La troisième ligne est celle qui surprend le plus les nouveaux arrivants.",
              notes="Diapo à photographier. Faire recopier.")

    d.regle("Le pourboire s'ajoute",
            "Environ 15 % du montant avant taxes.",
            precision="Il n'est jamais sur l'addition. Le calcul rapide : le dixième du "
                      "montant, plus la moitié de ce dixième. 50 $ donne 5 + 2,50 = 7,50 $. "
                      "Le terminal propose des pourcentages, mais on peut entrer le montant "
                      "qu'on veut.",
            notes="Diapo à photographier. Faire faire le calcul sur trois montants au "
                  "tableau.")

    d.regle("Pourquoi c'est attendu, ici",
            "Le pourboire fait partie du revenu du personnel de service.",
            precision="Au Québec, le salaire de base des employés au pourboire est plus bas "
                      "que le salaire minimum ordinaire, précisément parce que le pourboire "
                      "est prévu. Ce n'est pas un simple remerciement : laisser beaucoup "
                      "moins que 15 % se remarque.",
            notes="Dire aussi qu'on peut donner moins si le service a vraiment été mauvais. "
                  "Ce n'est pas une obligation légale.")

    d.piege("Croire que le service est compris",
            "Taxes comprises, donc tout est payé.",
            "Taxes comprises, oui. Le pourboire, non — il s'ajoute.",
            "Dans plusieurs pays, le service est inclus dans le prix et le pourboire "
            "n'existe pas, ou reste symbolique. Ici, l'addition affiche les taxes mais "
            "jamais le service : c'est au client de l'ajouter.",
            notes="Ne pas juger : cette différence est une des plus déroutantes à "
                  "l'arrivée, et elle met les gens dans l'embarras.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le serveur demande si c'est ensemble ou séparé.", "vrai"),
        ("Le total ne comprend pas les taxes.", "faux — taxes comprises"),
        ("Le pourboire habituel est de quinze pour cent.", "vrai"),
        ("Il se calcule après les taxes.", "faux — avant"),
        ("Le pourboire est déjà sur l'addition.", "faux — on l'ajoute"),
        ("Le pourboire fait partie du salaire du serveur.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Calculez le pourboire sur cinq montants.",
        exemples=[
            "20 $, 35 $, 48 $, 62 $, 90 $.",
            "Employez la méthode : le dixième, plus sa moitié.",
        ],
        notes="Devoir de calcul mental. Après cinq fois, la méthode devient automatique.")

    return d.save(dossier)
