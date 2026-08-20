# -*- coding: utf-8 -*-
"""C1 · La circulaire de la semaine.
Bloc C « Défi 2 · Choisir » · couleur acier · 75 min.
Source : dialogue `t2`, exercices `t2vf` et `t2circulaire`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-epicerie/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='La circulaire de la semaine',
        chapeau="Le papier qu'on jette avec la publicité annonce les prix de "
                "la semaine. Bien lue, elle change une facture d'épicerie de "
                "vingt ou trente dollars.",
        duree='75 minutes')

    d.titre(notes="Apporter deux ou trois circulaires réelles, si possible de chaînes "
                  "différentes. Elles circulent pendant le déclencheur.")

    d.objectifs([
        "savoir ce qu'est une circulaire et quand elle arrive ;",
        "lire un prix au poids et un prix « deux pour » ;",
        "trouver la date de fin d'un spécial ;",
        "comprendre les limites : quantité, format, exclusions.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce que c'est, et qu'est-ce qu'on en fait ?",
        image=IMG + 'circulaire-ouverte.jpg',
        pistes=[
            "Où le recevez-vous ?",
            "Le lisez-vous, ou le jetez-vous ?",
            "Quand arrive-t-il ?",
            "Qu'est-ce qu'on y trouve, exactement ?",
        ],
        notes="La plupart des élèves le jettent. C'est le point de bascule de la séance : "
              "montrer ce qu'il y a dedans.")

    d.dialogue('Dialogue · 1 de 3', "Un papier qu'on jette", [
        ("GINETTE", "Marisol ! Vous magasinez ici aussi ?", False),
        ("MARISOL", "Bonjour, madame Ginette. Oui, mais c'est cher.", True),
        ("GINETTE", "Vous regardez la circulaire avant de venir ?", True),
        ("MARISOL", "La circulaire ? Le papier dans la boîte aux lettres ?", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="La question de Marisol est celle de beaucoup d'élèves : ils reçoivent la "
             "circulaire sans savoir ce que c'est.")

    d.dialogue('Dialogue · 2 de 3', "Ce qu'elle contient", [
        ("GINETTE", "Oui. Elle arrive le mercredi. Elle montre les spéciaux de la semaine.", True),
        ("MARISOL", "Je la jette. Je pensais que c'était de la publicité.", True),
        ("GINETTE", "C'est de la publicité, mais elle est utile. Regardez : le poulet est à trois dollars la livre cette semaine.", True),
        ("MARISOL", "Et la semaine prochaine ?", False),
    ], notes="« C'est de la publicité, mais elle est utile » : la nuance est juste et vaut "
             "d'être reprise.")

    d.dialogue('Dialogue · 3 de 3', "Les dates", [
        ("GINETTE", "La semaine prochaine, ce sera autre chose. Les spéciaux changent le jeudi.", True),
        ("MARISOL", "Alors je dois acheter aujourd'hui.", True),
        ("GINETTE", "Ou demain. Le spécial finit mercredi soir. C'est écrit en petit, en bas.", True),
    ], notes="La date de fin est toujours écrite, toujours en petit. La faire chercher sur "
             "les circulaires apportées en classe.")

    d.tableau('Analyse', "Ce quon lit dans une circulaire",
              ['La mention', "Ce qu'elle veut dire"],
              [["3,99 $ / lb", "un prix à la livre — le total dépend du poids"],
               ["2 pour 5 $", "il faut en prendre deux pour ce prix"],
               ["Prix régulier 6,49 $", "le prix des autres semaines"],
               ["Jusqu'au mercredi 27", "la date de fin du spécial"]],
              cle=1,
              note="« 2 pour 5 $ » : un seul article coûte souvent presque le même prix que deux.",
              notes="Diapo à photographier. Faire trouver chacune de ces mentions sur une "
                    "vraie circulaire.")

    d.regle("Les spéciaux changent le jeudi",
            "Une semaine de spéciaux va du jeudi au mercredi.",
            precision="La circulaire arrive le mardi ou le mercredi dans la boîte aux "
                      "lettres, et annonce les prix qui commenceront le <b>jeudi</b>. Le "
                      "spécial finit le <b>mercredi soir</b> suivant. Acheter le jeudi "
                      "matin, c'est avoir le choix complet ; acheter le mercredi soir, "
                      "c'est risquer que le produit soit épuisé.",
            notes="Diapo à photographier. Les dates varient un peu d'une chaîne à l'autre, "
                  "mais le rythme hebdomadaire est le même partout.")

    d.cartes("Les limites, écrites en petit", "Trois à connaître", [
        ("Limite de 4 par famille",
         "On ne peut pas acheter dix articles au prix du spécial. Au-delà, c'est le prix "
         "régulier."),
        ("Quantités limitées",
         "Il peut ne plus y en avoir. Aucune obligation pour le magasin d'en recommander."),
        ("Certains formats seulement",
         "Le spécial vaut souvent pour un format précis. Le grand format à côté peut être "
         "au prix régulier."),
    ], notes="La troisième est la plus sournoise : on prend le grand format en croyant "
             "profiter du rabais.")

    d.piege("Acheter parce que c'est en spécial",
            "C'est à moitié prix, j'en prends quatre.",
            "En avais-je besoin ?",
            "Un rabais sur un produit qu'on n'utilise pas ne fait économiser rien du tout. "
            "La circulaire sert à acheter <b>moins cher</b> ce qu'on achète déjà — pas à "
            "acheter davantage.",
            notes="Nuance importante. C'est le mécanisme même de la publicité, et le dire "
                  "clairement rend la circulaire plus utile, pas moins.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("La circulaire arrive le mercredi.", "vrai"),
        ("Marisol lisait la circulaire chaque semaine.", "faux — elle la jetait"),
        ("Le poulet est à trois dollars la livre.", "vrai"),
        ("Les spéciaux durent tout le mois.", "faux — une semaine"),
        ("Les spéciaux changent le jeudi.", "vrai"),
        ("La date de fin est écrite en petit, en bas.", "vrai"),
    ], corrige=True,
       notes="Faire justifier les deux « faux » par la réplique exacte.")

    d.billet(
        "Apportez la circulaire de cette semaine à la prochaine séance.",
        exemples=[
            "Entourez trois produits que vous achetez d'habitude.",
            "Notez leur prix régulier et leur prix en spécial.",
        ],
        notes="Devoir essentiel : la séance C3 s'appuie dessus.")

    return d.save(dossier)
