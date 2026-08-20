# -*- coding: utf-8 -*-
"""A1 · Je ne trouve pas.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-epicerie/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre='Je ne trouve pas',
        chapeau="Une grande épicerie compte quinze allées et vingt mille "
                "produits. Celui qu'on cherche n'est pas toujours là où on "
                "l'attend — et demander est plus rapide que chercher.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Demander d'abord au groupe qui fait ses "
                  "courses dans une grande épicerie et qui préfère les petits commerces. "
                  "Les réponses ouvrent la séance.")

    d.objectifs([
        "nommer ce qu'on trouve dans une épicerie ;",
        "comprendre qu'un produit peut être rangé ailleurs qu'avec sa famille ;",
        "demander de l'aide à un commis ;",
        "comprendre une réponse qui donne un numéro d'allée.",
    ])

    d.declencheur(
        'Observation', "Où chercheriez-vous de la farine de maïs ?",
        image=IMG + 'allee-numerotee.jpg',
        pistes=[
            "Avec les autres farines ?",
            "Avec le pain ?",
            "Ailleurs ?",
            "Et si vous ne trouvez pas, que faites-vous ?",
        ],
        notes="Presque tout le monde répond « avec les farines ». C'est logique — et c'est "
              "faux dans la plupart des épiceries d'ici. C'est le point de départ du "
              "module.")

    d.dialogue('Dialogue · 1 de 3', "La question", [
        ("MARISOL", "Excusez-moi, monsieur. Je cherche quelque chose.", True),
        ("ÉRIC", "Oui ? Qu'est-ce que vous cherchez ?", True),
        ("MARISOL", "De la farine de maïs. Pour faire des tortillas.", True),
        ("ÉRIC", "De la farine de maïs… Attendez. Vous avez regardé où ?", False),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Marisol commence par « Excusez-moi » et ne pose sa question qu'après. Faire "
             "remarquer les deux temps.")

    d.dialogue('Dialogue · 2 de 3', "Pas où on croit", [
        ("MARISOL", "Là-bas. Avec les autres farines. Il n'y en a pas.", True),
        ("ÉRIC", "Ah, non. Elle n'est pas avec les farines. Elle est dans les produits du monde.", True),
        ("MARISOL", "Les produits du monde ? Qu'est-ce que c'est ?", True),
        ("ÉRIC", "C'est une allée pour les produits d'autres pays. Allée douze, tout au fond.", True),
    ], notes="Marisol ne fait pas semblant de comprendre : elle demande ce que veut dire "
             "l'expression. C'est exactement ce qu'il faut faire.")

    d.dialogue('Dialogue · 3 de 3', "La porte reste ouverte", [
        ("MARISOL", "Allée douze. Merci beaucoup.", True),
        ("ÉRIC", "Si vous ne trouvez pas, revenez me voir. Je suis ici toute la journée.", True),
    ], notes="Cette dernière réplique est vraie : les commis le disent, et ils le pensent. "
             "Beaucoup d'élèves croient qu'on ne peut demander qu'une seule fois.")

    d.tableau('Analyse', "Trois choses à retenir de ce dialogue",
              ['Ce qui arrive', 'Ce qu\'on fait'],
              [["Le produit n'est pas là où on croit", "on demande, au lieu de chercher"],
               ["Un mot qu'on ne connaît pas", "on demande ce qu'il veut dire"],
               ["Une réponse avec un numéro", "on le répète pour vérifier"],
               ["On n'a toujours pas trouvé", "on revient voir la même personne"]],
              cle=0,
              note="Chercher seul dans quinze allées prend vingt minutes. Demander en prend une.",
              notes="Diapo à photographier. C'est le résumé du module en quatre lignes.")

    d.regle("Les produits du monde",
            "Une allée à part, pour les produits d'autres pays.",
            precision="Beaucoup d'épiceries d'ici rassemblent dans une seule allée les "
                      "produits d'Amérique latine, d'Asie et d'Afrique — au lieu de les "
                      "ranger avec leur famille. La farine de maïs n'est donc pas avec les "
                      "farines, et le lait de coco n'est pas avec les autres laits.",
            notes="Diapo à photographier. C'est l'information la plus utile de la séance "
                  "pour des élèves nouvellement arrivés.")

    d.cartes("Ce qu'on trouve dans une épicerie", "Quatre repères", [
        ("Les allées numérotées",
         "Un grand chiffre suspendu au bout de chaque rangée, visible des deux côtés."),
        ("Les affichettes",
         "Le panneau au-dessus de l'allée, qui nomme les familles : pâtes, riz, conserves."),
        ("Le frais, sur les murs",
         "Fruits, viande, lait et pain sont presque toujours sur les côtés du magasin."),
        ("Les caisses, à la sortie",
         "Et souvent, un comptoir de service à la clientèle juste à côté."),
    ], notes="Faire dessiner au tableau le plan d'une épicerie que le groupe connaît.")

    d.piege("Chercher seul par fierté",
            "Je vais bien finir par le trouver.",
            "Excusez-moi, je cherche…",
            "Les commis répondent à cette question cent fois par jour : elle fait partie de "
            "leur travail, et ils ne trouvent pas étrange qu'on la pose. Chercher seul dans "
            "quinze allées peut prendre vingt minutes ; demander en prend une.",
            notes="Rassurer : personne ne juge quelqu'un qui demande où est un produit.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Marisol cherche de la farine de maïs.", "vrai"),
        ("La farine de maïs est avec les autres farines.", "faux — dans les produits du monde"),
        ("C'est l'allée cinq.", "faux — l'allée douze"),
        ("Marisol demande ce que veut dire « produits du monde ».", "vrai"),
        ("Le commis lui dit de revenir si elle ne trouve pas.", "vrai"),
        ("Marisol veut faire du pain.", "faux — des tortillas"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Notez un produit que vous cherchez souvent sans le trouver.",
        exemples=[
            "Dans quelle allée est-il, dans votre épicerie ?",
            "Si vous ne le savez pas, allez demander cette semaine.",
        ],
        notes="Devoir concret. Il prépare le défi 1 et donne des exemples réels pour la "
              "séance suivante.")

    return d.save(dossier)
