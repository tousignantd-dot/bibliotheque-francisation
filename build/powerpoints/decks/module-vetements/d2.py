# -*- coding: utf-8 -*-
"""D2 · La mise de côté.
Bloc D « Défi 3 » · couleur ambre · 60 min.
Source : mini-leçon `t3echange`, exercice `t3echange`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre='La mise de côté',
        chapeau="Payer un peu maintenant, le reste plus tard, et le manteau "
                "attend au magasin. C'est un service gratuit que beaucoup de "
                "gens ignorent — avec des règles à connaître.",
        duree='60 minutes')

    d.titre(notes="Peu de gens connaissent ce service. Demander d'abord si quelqu'un l'a "
                  "déjà utilisé : en général, personne.")

    d.objectifs([
        "demander une mise de côté ;",
        "comprendre le dépôt et le délai ;",
        "employer le conditionnel de politesse ;",
        "réviser les formules du défi 3.",
    ])

    d.declencheur(
        'Mise en situation', "Le manteau coûte 200 $. Vous en avez 60. Que faire ?",
        pistes=[
            "Attendre la paie, et risquer qu'il soit vendu ?",
            "Payer avec une carte de crédit ?",
            "Existe-t-il une autre solution ?",
            "Que se passe-t-il si vous ne revenez pas ?",
        ],
        notes="La troisième piste amène la mise de côté. La quatrième amène la règle du "
              "dépôt non remboursable, qu'il faut dire d'emblée.")

    d.regle("La mise de côté",
            "Le magasin garde l'article ; vous payez un dépôt.",
            precision="Vous versez une partie du prix — souvent vingt pour cent — et le "
                      "magasin met l'article de côté. Vous avez un délai — souvent "
                      "quatorze jours, parfois trente — pour payer le reste et le "
                      "reprendre. Le service est "
                      "gratuit : il n'y a ni intérêt ni frais.",
            notes="Diapo à photographier. Insister sur « gratuit » : c'est l'inverse d'une "
                  "carte de crédit.")

    d.tableau('Analyse', "Les quatre chiffres à demander",
              ['La question', 'La réponse type'],
              [["Le dépôt ?", "vingt pour cent du prix"],
               ["Le délai ?", "souvent quatorze jours"],
               ["Des frais ?", "aucun, normalement"],
               ["Si je ne reviens pas ?", "le dépôt est perdu"]],
              cle=3,
              note="C'est la seule mauvaise nouvelle : la poser avant de signer.",
              notes="Diapo à photographier. Faire poser les quatre questions à voix haute.")

    d.cartes("Trois façons de reporter un achat", "Ce qui les distingue", [
        ("La mise de côté",
         "Gratuite. L'article attend au magasin. Vous ne l'avez pas tout de suite, mais "
         "vous ne payez aucun intérêt."),
        ("La carte de crédit",
         "Vous avez l'article tout de suite. Si vous ne payez pas le solde complet, les "
         "intérêts sont très élevés — souvent près de vingt pour cent par année."),
        ("Attendre et économiser",
         "Gratuit aussi, mais l'article peut être vendu, et les manteaux d'hiver se "
         "vendent vite en novembre."),
    ], notes="Ne pas moraliser sur la carte de crédit : donner le chiffre et laisser "
             "comparer.")

    d.regle("Le conditionnel de politesse",
            "« Je voudrais », « auriez-vous », « est-ce que je pourrais »",
            precision="« Je veux échanger » se comprend, mais sonne comme un ordre. "
                      "« Je <b>voudrais</b> échanger » est la forme normale au comptoir. De "
                      "même : « Auriez-vous la taille au-dessus ? », « Est-ce que je "
                      "pourrais le mettre de côté ? ». Ces trois formes se retiennent en "
                      "bloc.",
            notes="Diapo à photographier. Ne pas enseigner la conjugaison du conditionnel : "
                  "trois formes toutes faites suffisent à ce niveau.")

    d.piege("Croire que le dépôt revient",
            "Si je change d'avis, on me rend mon soixante dollars.",
            "Le dépôt est rarement remboursable.",
            "C'est ce qui garantit au magasin que l'article n'a pas été retiré de la vente "
            "pour rien. Demandez la règle avant de verser le dépôt — elle est écrite sur le "
            "reçu de mise de côté, qu'il faut garder comme une facture.",
            notes="Le dire clairement : c'est la seule chose qui peut mal tourner.")

    d.pratique('Pratique · 1 de 2', "Quelle formule ?",
               "Reformulez poliment.", [
        ("Je veux échanger ça.", "Je voudrais échanger ceci, s'il vous plaît."),
        ("Donnez-moi la taille au-dessus.", "Auriez-vous la taille au-dessus ?"),
        ("Je le mets de côté.", "Est-ce que je pourrais le mettre de côté ?"),
        ("Remboursez-moi.", "Est-ce que je pourrais être remboursé ?"),
    ], corrige=True, cols=1,
       notes="Faire dire à voix haute : le ton compte autant que la forme.")

    d.pratique('Pratique · 2 de 2', "Échange, remboursement ou mise de côté ?",
               "Choisissez la bonne demande.", [
        ("Les bottes sont trop petites.", "un échange"),
        ("Le manteau ne vous plaît plus, non porté, facture en main.", "un remboursement"),
        ("Vous n'avez pas assez d'argent aujourd'hui.", "une mise de côté"),
        ("L'article était en vente finale.", "rien — ni échange ni remboursement"),
    ], corrige=True, cols=1,
       notes="La dernière ligne rappelle la règle de D1.")

    d.billet(
        "Écrivez une demande de mise de côté, avec les quatre questions.",
        exemples=[
            "Commencez par « Est-ce que je pourrais… »",
            "Posez le dépôt, le délai, les frais, et ce qui arrive si vous ne revenez pas.",
        ],
        notes="Fin du bloc D. Ce billet est la répétition écrite du jeu de rôle.")

    return d.save(dossier)
