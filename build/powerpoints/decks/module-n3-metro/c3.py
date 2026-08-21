# -*- coding: utf-8 -*-
"""C3 · Je voudrais, je peux, je dois, il faut.
Bloc C « Défi 2 · Demander au guichet » · couleur ambre · 75 min.
Source : exercice `t2modal` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre='Je voudrais, je peux, je dois, il faut',
        chapeau="Toute la conversation du guichet tient sur quatre petits "
                "verbes. Ils ne disent pas la même chose, et le verbe qui les "
                "suit ne bouge jamais.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Le programme de niveau 3 les appelle les "
                  "auxiliaires de modalité. Ouvrir en écrivant les quatre au tableau et "
                  "en demandant au groupe lequel il emploierait pour entrer en "
                  "conversation. Les réponses seront partagées.")

    d.objectifs([
        "choisir entre je voudrais, je peux, je dois et il faut ;",
        "distinguer l'obligation personnelle et la règle générale ;",
        "laisser le deuxième verbe à sa forme de base ;",
        "employer « je voudrais » plutôt que « je veux » au comptoir.",
    ])

    d.tableau('Analyse', "Quatre verbes, quatre intentions",
              ["Le verbe", "Ce qu'il fait"],
              [["je voudrais", "demander poliment une chose"],
               ["est-ce que je peux", "demander la permission"],
               ["je dois", "dire mon obligation à moi"],
               ["il faut", "dire la règle, pour tout le monde"]],
              cle=0,
              note="Ils ne sont pas interchangeables : chacun dit autre chose.",
              notes="Diapositive à photographier. Faire trouver un exemple pour chacun "
                    "dans le dialogue de la séance C1 : les quatre y sont.")

    d.regle("La formule d'entrée, encore",
            "« Je voudrais un titre mensuel, s'il vous plaît. »",
            precision="« Je veux » n'est pas faux, mais sonne sec, presque "
                      "impoli. « Je voudrais » demande exactement la même chose "
                      "et ouvre bien mieux la conversation. Ajoutez « s'il vous "
                      "plaît » : au Québec, c'est presque obligatoire.",
            notes="Diapositive à photographier. Ne pas moraliser : expliquer que c'est "
                  "une convention locale, comme la virgule dans les prix. Les élèves "
                  "qui disent « je veux » ne sont pas impolis, ils traduisent.")

    d.tableau('Analyse', "Je dois ou il faut ?",
              ["La phrase", "Qui est obligé"],
              [["Je dois apporter une preuve d'âge.", "moi, personnellement"],
               ["Il faut une carte avec photo.", "tout le monde, sans exception"],
               ["Je dois venir avec ma fille.", "moi, dans ma situation"],
               ["Il faut valider son titre.", "toute personne qui monte"]],
              cle=1,
              note="« Il faut » ne change jamais de forme. C'est le verbe le plus simple.",
              notes="Diapositive à photographier. La distinction est fine mais utile : "
                    "un élève qui dit « il faut que j'apporte » se fait comprendre, mais "
                    "« je dois apporter » est plus direct et plus court.")

    d.regle("Ce qui vient après les quatre",
            "Je voudrais ACHETER · Je peux PAYER · Il faut VENIR",
            precision="Le deuxième verbe garde toujours sa forme de base, celle "
                      "du dictionnaire. On ne dit jamais « je voudrais j'achète » "
                      "ni « il faut je viens ». Un seul verbe se conjugue : le "
                      "premier.",
            notes="Diapositive à photographier. C'est ce qui rend ces quatre verbes "
                  "faciles : ils dispensent de conjuguer le verbe qui porte le sens. "
                  "Le dire ainsi au groupe, c'est une bonne nouvelle.")

    d.piege('Grammaire',
            "« Je voudrais j'achète un titre. »",
            "« Je voudrais acheter un titre. »",
            "Un seul verbe se conjugue : le premier. Le second garde sa forme de "
            "base — acheter, payer, venir, valider, apporter. C'est vrai des "
            "quatre verbes de la séance.",
            notes="Erreur très fréquente et facile à corriger. Faire l'exercice inverse : "
                  "donner une phrase à deux verbes conjugués et demander au groupe de "
                  "la réparer.")

    d.pratique('Grammaire', "Le bon verbe",
               "Complétez avec je voudrais, je peux, je dois ou il faut.", [
        ("Bonjour. ___ un titre mensuel, s'il vous plaît.", "Je voudrais"),
        ("Est-ce que ___ payer par carte ?", "je peux"),
        ("Pour le tarif réduit, ___ une carte avec photo.", "il faut"),
        ("___ apporter une preuve de son âge.", "Je dois / Il faut"),
        ("Est-ce que ___ recharger ma vieille carte ?", "je peux"),
        ("___ valider son titre en montant dans l'autobus.", "Il faut"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice 3 du défi 2. Le quatrième énoncé accepte les deux "
             "réponses : c'est l'occasion de faire dire la différence de sens plutôt "
             "que de trancher.")

    d.pratique('Répétition', "Six phrases du défi 2",
               "Écoutez, puis répétez.", [
        ("Bonjour. Je voudrais un titre mensuel, s'il vous plaît.", "demander poliment"),
        ("Est-ce que je peux payer par carte ?", "demander la permission"),
        ("Est-ce que je dois acheter une nouvelle carte ?", "mon obligation"),
        ("Pour le tarif réduit, il faut une carte avec photo.", "la règle"),
        ("Il faut valider son titre en montant.", "la règle"),
        ("Je voudrais acheter un titre pour le mois.", "poliment, devant un verbe"),
    ], corrige=True,
       notes="Répétition en binômes : l'un joue le client, l'autre répond « oui » ou "
             "« non ». C'est la première mise en situation du défi 2, très courte, et "
             "elle prépare le jeu de rôle de la séance E1.")

    d.billet(
        "Écrivez une phrase avec chacun des quatre verbes.",
        exemples=[
            "Je voudrais ___ .",
            "Il faut ___ .",
        ],
        notes="Devoir court. Vérifier au ramassage que le deuxième verbe n'est jamais "
              "conjugué : c'est le seul point qui compte.")

    return d.save(dossier)
