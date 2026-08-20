# -*- coding: utf-8 -*-
"""D2 · Lire sa facture.
Bloc D « Défi 3 » · couleur ambre · 60 min.
Source : dialogue `t3b`, mini-leçon et exercice `t3facture`, exercice `t3erreur`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-epicerie/images/')


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre='Lire sa facture',
        chapeau="Une ligne par produit, un sous-total, les taxes, un total. "
                "Deux choses à vérifier seulement : que les spéciaux sont "
                "passés, et que rien n'est compté deux fois.",
        duree='60 minutes')

    d.titre(notes="Apporter quelques factures d'épicerie réelles, anonymisées. Elles "
                  "circulent pendant la séance.")

    d.objectifs([
        "reconnaître les quatre parties d'une facture ;",
        "savoir sur quoi il y a des taxes ;",
        "vérifier qu'un spécial est bien passé ;",
        "signaler une erreur poliment.",
    ])

    d.declencheur(
        'Observation', "Que regardez-vous sur ce papier ?",
        image=IMG + 'facture-epicerie.jpg',
        pistes=[
            "Le total, seulement ?",
            "Vérifiez-vous les lignes ?",
            "Que faites-vous de la facture après ?",
            "Avez-vous déjà trouvé une erreur ?",
        ],
        notes="Presque personne ne vérifie. Les erreurs de prix sont pourtant fréquentes, "
              "surtout le jeudi matin, quand les spéciaux changent.")

    d.tableau('Analyse', "Les quatre parties",
              ['La partie', "Ce qu'elle contient"],
              [["Les lignes", "un produit par ligne, nom écrit court"],
               ["Le sous-total", "le total avant les taxes"],
               ["TPS et TVQ", "les deux taxes"],
               ["Le total", "ce qu'on paie vraiment"]],
              cle=1,
              note="Le sous-total correspond aux prix affichés dans les allées.",
              notes="Diapo à photographier. Faire retrouver les quatre parties sur les "
                    "factures apportées.")

    d.regle("Les taxes sur l'alimentation",
            "Sur les aliments de base, il n'y en a pas.",
            precision="Pain, lait, légumes, viande, œufs : <b>aucune taxe</b>. Les taxes "
                      "s'ajoutent sur les produits d'entretien, les boissons gazeuses, les "
                      "plats préparés et les portions individuelles. C'est pour cela que la "
                      "ligne des taxes est souvent très petite sur une facture d'épicerie.",
            notes="Diapo à photographier. C'est une particularité fiscale d'ici, utile à "
                  "connaître pour prévoir sa dépense.")

    d.dialogue('Dialogue', "Ce n'est pas le bon prix", [
        ("MARISOL", "Excusez-moi. Je regarde ma facture. Le poulet, c'est cinq dollars.", True),
        ("STÉPHANE", "Oui, cinq dollars la livre.", False),
        ("MARISOL", "Mais dans la circulaire, c'est trois dollars.", True),
        ("STÉPHANE", "Vous avez la circulaire ?", False),
        ("MARISOL", "J'ai la photo sur mon téléphone.", True),
        ("STÉPHANE", "Attendez, je regarde… Vous avez raison. Le spécial n'est pas passé.", True),
    ], consigne="Écoutez, puis relevez les trois phrases de Marisol.",
       notes="Marisol décrit ce qu'elle voit, sans accuser. Et elle a une preuve. Ce sont "
             "les deux conditions d'un signalement qui aboutit.")

    d.regle("Signaler sans accuser",
            "On décrit le fait, on ne met personne en cause.",
            precision="« Le poulet, c'est cinq dollars sur la facture. Dans la circulaire, "
                      "c'est trois. » La personne à la caisse n'a pas fixé le prix : le "
                      "plus souvent, c'est un spécial qui n'est pas entré dans le système. "
                      "Décrire l'écart obtient une vérification ; accuser obtient une "
                      "discussion.",
            notes="Diapo à photographier. Faire dire la phrase à voix haute par trois "
                  "élèves.")

    d.cartes("La ligne des économies", "Le contrôle le plus rapide", [
        ("Elle est en bas",
         "« Vous avez économisé 8,40 $ » — la somme de tous les spéciaux appliqués."),
        ("Si elle est à zéro",
         "Aucun spécial n'est passé. C'est le signal qu'il faut regarder les lignes une "
         "par une."),
        ("Un coup d'œil suffit",
         "Avant de quitter le magasin, regardez ce chiffre. S'il correspond à peu près à "
         "ce que vous attendiez, tout va bien."),
    ], notes="Diapo à photographier. C'est le contrôle en trois secondes, à faire près de "
             "la sortie plutôt qu'à la maison.")

    d.piege("Découvrir l'erreur à la maison",
            "En rangeant les sacs, je vois que le prix n'est pas le bon.",
            "Dix secondes près de la sortie.",
            "Une fois rentré, il faut revenir au magasin avec la facture et le produit. Dix "
            "secondes de vérification avant de partir évitent un deuxième déplacement — et "
            "beaucoup de gens ne reviennent jamais, ce qui revient à payer l'erreur.",
            notes="Faire le geste : s'arrêter deux pas après la caisse, regarder la ligne "
                  "des économies, ranger la facture.")

    d.pratique('Pratique · 1 de 2', "Que dit cette ligne ?",
               "Répondez en une phrase.", [
        ("POULET 3 LB · 15,00", "trois livres de poulet, quinze dollars"),
        ("SOUS-TOTAL · 38,40", "le total avant les taxes"),
        ("TPS · 0,45", "la taxe fédérale — faible, car peu d'aliments sont taxés"),
        ("TOTAL · 42,15", "ce qu'on paie vraiment"),
        ("ÉCONOMIES · 8,40", "la somme des spéciaux appliqués"),
    ], corrige=True, cols=1,
       notes="Utiliser l'exercice 3 du module.")

    d.pratique('Pratique · 2 de 2', "À deux · signaler une erreur",
               "Un client, une personne à la caisse.", [
        ("Le client", "décrit l'écart entre la facture et la circulaire"),
        ("La caisse", "demande la preuve, vérifie, propose la solution"),
        ("Le client", "remercie et vérifie le remboursement"),
        ("On change de rôle", "avec un autre produit"),
    ], cols=1,
       notes="Vingt minutes. Exiger que le client décrive sans accuser : c'est le point de "
             "langue de la séance.")

    d.billet(
        "Gardez la facture de votre prochaine épicerie et vérifiez-la.",
        exemples=[
            "La ligne des économies correspond-elle à ce que vous attendiez ?",
            "Un prix vous surprend-il ?",
        ],
        notes="Fin du bloc D. Prendre cinq minutes à la séance suivante pour entendre deux "
              "ou trois résultats.")

    return d.save(dossier)
