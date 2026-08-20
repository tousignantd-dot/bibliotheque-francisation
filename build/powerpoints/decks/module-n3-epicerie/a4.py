# -*- coding: utf-8 -*-
"""A4 · Où aller acheter ?
Bloc A « Je découvre » · couleur teal · 50 min.
Source : exercice `prCommerce` — le lexique « types de commerces » du programme.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre='Où aller acheter ?',
        chapeau="Six commerces, six usages. Le dépanneur dépanne, l'épicerie "
                "nourrit la semaine, et le marché public ne vend pas la même "
                "chose en janvier qu'en août.",
        duree='50 minutes')

    d.titre(notes="Séance courte qui clôt le bloc A. Elle prépare le vocabulaire du défi 2.")

    d.objectifs([
        "nommer six types de commerces d'alimentation ;",
        "savoir lequel convient à quel besoin ;",
        "comprendre pourquoi le dépanneur coûte plus cher ;",
        "employer « chez » et « à » devant un commerce.",
    ])

    d.declencheur(
        'Mise en situation', "Il est vingt-deux heures et il n'y a plus de lait. Où allez-vous ?",
        pistes=[
            "L'épicerie est-elle ouverte ?",
            "Combien coûte le lait au dépanneur ?",
            "Pourquoi cette différence ?",
            "Est-ce que ça vaut la peine quand même ?",
        ],
        notes="Le lait peut coûter un ou deux dollars de plus au dépanneur. Ce n'est pas "
              "un abus : c'est un petit commerce ouvert tard, avec peu de volume.")

    d.tableau('Analyse', "Trois commerces du quotidien",
              ['Le commerce', "Ce qu'on y va chercher"],
              [["l'épicerie, le supermarché", "tout pour la semaine, au meilleur prix"],
               ["le dépanneur", "une chose qui manque, tard le soir"],
               ["le marché public", "des fruits et légumes frais, l'été"]],
              cle=0,
              note="Aucun n'est meilleur : chacun répond à un besoin.",
              notes="Diapo à photographier. Faire nommer un commerce de chaque type dans "
                    "le quartier de l'école.")

    d.tableau('Analyse', "Trois commerces spécialisés",
              ['Le commerce', "Ce qu'on y va chercher"],
              [["la boucherie", "de la viande coupée devant vous"],
               ["la boulangerie", "du pain sorti du four le matin"],
               ["l'épicerie spécialisée", "les produits d'un pays"]],
              cle=2,
              note="La dernière est souvent la seule à vendre ce qu'on cherche.",
              notes="La troisième ligne compte beaucoup pour un groupe de francisation : "
                    "c'est là qu'on trouve les produits de son pays.")

    d.regle("Chez ou à ?",
            "Chez le boucher, à la boucherie.",
            precision="<b>Chez</b> s'emploie devant une <b>personne</b> : chez le boucher, "
                      "chez le boulanger, chez le pharmacien. <b>À</b> s'emploie devant un "
                      "<b>lieu</b> : à la boucherie, à la boulangerie, à l'épicerie, au "
                      "dépanneur. Les deux sont corrects — mais pas mélangés.",
            notes="Diapo à photographier. « Chez l'épicerie » est l'erreur la plus "
                  "fréquente, et elle s'entend tout de suite.")

    d.cartes("Le prix, et pourquoi il change", "Trois raisons", [
        ("Le volume",
         "Un supermarché achète par camions entiers ; un dépanneur, par caisses. Le prix "
         "d'achat n'est pas le même."),
        ("Les heures d'ouverture",
         "Rester ouvert jusqu'à minuit coûte cher en salaires, pour peu de clients."),
        ("Le service",
         "À la boucherie, quelqu'un coupe la viande devant vous et répond à vos questions. "
         "Ce temps se paie."),
    ], notes="Ne pas moraliser sur le prix du dépanneur : donner les raisons et laisser "
             "juger.")

    d.piege("Faire toutes ses courses au dépanneur",
            "C'est plus près, j'y vais tous les jours.",
            "Le dépanneur dépanne ; l'épicerie nourrit la semaine.",
            "Sur une semaine complète, la différence atteint facilement vingt ou trente "
            "dollars. Pour un ménage qui compte, c'est un montant qui se sent — et une "
            "sortie d'épicerie par semaine suffit à l'éviter.",
            notes="Le dire avec tact : plusieurs élèves n'ont pas d'auto et le dépanneur "
                  "est parfois le seul commerce accessible à pied.")

    d.pratique('Pratique · 1 de 2', "Où aller ?",
               "Choisissez le commerce qui convient.", [
        ("Les courses de la semaine pour quatre personnes", "l'épicerie ou le supermarché"),
        ("Du lait à vingt-deux heures", "le dépanneur"),
        ("Des tomates fraîches en août", "le marché public"),
        ("Un rôti coupé à l'épaisseur voulue", "la boucherie"),
        ("De la farine de maïs et des piments séchés", "une épicerie spécialisée"),
        ("Du pain chaud le dimanche matin", "la boulangerie"),
    ], corrige=True,
       notes="Faire justifier chaque réponse en une phrase.")

    d.pratique('Pratique · 2 de 2', "Chez ou à ?",
               "Complétez.", [
        ("Je vais ___ boucherie.", "à la"),
        ("Je vais ___ le boucher.", "chez"),
        ("Je vais ___ épicerie.", "à l'"),
        ("Je vais ___ dépanneur.", "au"),
        ("Je vais ___ le boulanger.", "chez"),
    ], corrige=True, cols=1,
       notes="Exercice mécanique. Faire dire à voix haute : l'oreille corrige plus vite que "
             "la règle.")

    d.billet(
        "Nommez quatre commerces d'alimentation de votre quartier.",
        exemples=[
            "Leur type, et ce que vous y achetez.",
            "Lequel est le plus près de chez vous ?",
        ],
        notes="Fin du bloc A. Les réponses servent d'exemples au bloc B.")

    return d.save(dossier)
