# -*- coding: utf-8 -*-
"""A4 · Lire une annonce, répondre à un avis.
Bloc A « Je découvre » · couleur ambre · 75 min.
Source : exercices `prAnnonce` et `prAvis`, mini-leçons du même nom.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-logement/images/')


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Lire une annonce, répondre à un avis",
        chapeau="Une annonce est un texte codé, et un avis est un papier "
                "auquel il faut répondre. Deux lectures, deux écritures — "
                "et la fin du bloc de découverte.",
        duree='75 minutes')

    d.titre(notes="Séance de lecture et d'écriture. Elle ferme le bloc A et arme les "
                  "élèves pour chercher un logement dès cette semaine.")

    d.objectifs([
        "décoder les abréviations d'une annonce ;",
        "comparer deux loyers en tenant compte de ce qui est inclus ;",
        "écrire une réponse à un avis de modification ;",
        "savoir ce qu'une annonce ne dit jamais.",
    ])

    d.declencheur(
        'Lecture', "Lequel de ces deux logements coûte le moins cher ?",
        image=IMG + 'panneau-a-louer.jpg',
        pistes=[
            "« 4 ½, 1 050 $, C/E, 1er juillet »",
            "« 4 ½, 1 000 $, N/C, 1er juillet »",
            "Lequel choisiriez-vous ?",
            "Que veulent dire C/E et N/C ?",
        ],
        notes="Presque tout le monde choisit le deuxième, qui est le plus cher en réalité : "
              "N/C veut dire non chauffé, et Hydro coûte environ cent dollars par mois "
              "l'hiver. Laisser le groupe se tromper avant d'expliquer.")

    d.tableau('Le code · 1 de 2', "Les pièces et ce qui est inclus",
              ['Abréviation', 'Ce que ça veut dire'],
              [["4 ½", "deux chambres, un salon, une cuisine"],
               ["C/E", "chauffé et éclairé : tout est compris"],
               ["N/C", "non chauffé : Hydro s'ajoute"]],
              cle=0,
              note="Le demi, c'est toujours la salle de bain.",
              notes="Diapositive à photographier. Ce sont les trois mentions qui décident "
                    "du prix réel.")

    d.tableau('Le code · 2 de 2', "La date, l'étage, le reste",
              ['Abréviation', 'Ce que ça veut dire'],
              [["Libre imm.", "libre immédiatement"],
               ["s/s · 2e ét.", "sous-sol · deuxième étage"],
               ["stat. · n/f", "stationnement · non-fumeur"]],
              cle=0,
              note="Lisez dans cet ordre : les pièces, le prix, ce qui est inclus, la date.",
              notes="Diapositive à photographier. C'est l'outil que les élèves emporteront "
                    "pour chercher un logement cette semaine.")

    d.regle("Le prix affiché n'est pas le prix payé",
            "Un 4 ½ à 1 050 $ chauffé coûte moins cher qu'un 4 ½ à 1 000 $ non chauffé.",
            precision="Comparez toujours le prix tout compris. Au Québec, le chauffage "
                      "électrique d'un quatre et demie tourne autour de cent dollars par "
                      "mois l'hiver, et beaucoup moins l'été — mais le loyer, lui, ne "
                      "baisse pas en juillet.",
            notes="Diapositive à photographier. Faire faire le calcul au tableau sur douze "
                  "mois : l'écart annuel dépasse souvent six cents dollars.")

    d.cartes("Ce qu'une annonce ne dit jamais", "Vos questions du défi 1", [
        ("Le bruit",
         "Aucune annonce n'écrit « mal insonorisé ». C'est pourtant la première "
         "cause de déménagement."),
        ("L'état des fenêtres",
         "Une fenêtre qui coince, c'est un hiver froid et une facture d'Hydro plus "
         "élevée."),
        ("La vraie facture de chauffage",
         "Demandez un montant en dollars, pas une impression : « c'est pas cher à "
         "chauffer » ne veut rien dire."),
        ("Le loyer de l'ancien locataire",
         "Il est pourtant obligatoire de l'inscrire au bail. C'est la question qui "
         "surprend le plus les propriétaires."),
    ], notes="Une annonce ne ment pas : elle se tait. Ce qui n'est pas écrit est exactement "
             "la liste des questions du téléphone — c'est le pont vers le défi 1.")

    d.pratique('Lecture', "Décodez ces annonces",
               "Écrivez ce que chaque ligne veut dire.", [
        ("4 ½, 1 050 $, N/C, 1er juillet",
         "deux chambres, 1 050 $, chauffage non inclus, bail au 1er juillet"),
        ("3 ½ C/E, meublé, libre imm.",
         "une chambre, chauffage et électricité compris, meubles fournis, libre tout de suite"),
        ("5 ½ s/s, n/f, stat. incl.",
         "trois chambres au sous-sol, non-fumeur, stationnement compris"),
        ("2 ½ 2e ét., animaux acceptés",
         "un studio au deuxième étage, animaux acceptés"),
    ], corrige=True,
       notes="Faire remarquer qu'aucune des quatre ne parle du bruit ni des fenêtres.")

    d.tableau('La lettre de réponse', "Cinq lignes, et c'est tout",
              ['La partie', 'Ce qu\'on écrit'],
              [["Le lieu et la date", "Sherbrooke, le 12 février 2026"],
               ["L'objet", "Réponse à votre avis de modification du bail du 3 février"],
               ["La décision", "Je refuse l'augmentation de loyer que vous proposez."],
               ["Le deuxième changement", "Je refuse également le retrait du stationnement."],
               ["La salutation", "Veuillez recevoir, Madame, mes salutations distinguées."]],
              cle=0,
              note="La loi ne vous demande pas de justifier votre refus. N'expliquez rien.",
              notes="Diapositive à photographier. Insister sur la dernière note : les élèves "
                    "veulent tous expliquer leur situation financière. C'est inutile et ça "
                    "affaiblit la lettre.")

    d.piege("Répondre par texto",
            "Je lui ai écrit sur son cellulaire.",
            "Une lettre ou un courriel, avec une date, et j'en garde une copie.",
            "Un texto se perd, se supprime et se conteste. Ce qui compte devant le "
            "Tribunal, c'est la preuve de la date. Photographiez votre lettre avant de "
            "l'envoyer.",
            notes="Question fréquente : « et un courriel ? » Oui, un courriel convient — "
                  "il porte une date et se conserve.")

    d.pratique('Écriture', "Écrivez la réponse de Nadège",
               "Le loyer passe de 720 $ à 795 $ et le stationnement est retiré. "
               "Elle refuse les deux.", [
        ("La première ligne", "Sherbrooke, le 12 février 2026"),
        ("L'objet", "Réponse à votre avis de modification du bail"),
        ("Le refus du loyer", "Je refuse l'augmentation de loyer que vous proposez."),
        ("Le refus du service", "Je refuse également le retrait de la case de stationnement."),
        ("Ce qui suit", "Il vous appartient de vous adresser au Tribunal administratif du logement."),
        ("La salutation", "Veuillez recevoir, Madame, mes salutations distinguées."),
    ], corrige=True,
       notes="Faire écrire la lettre entière au propre sur une feuille. C'est un document "
             "qu'ils garderont, et plusieurs s'en serviront pour vrai.")

    d.billet(
        "Trouvez trois annonces de logement dans votre quartier.",
        exemples=[
            "Copiez-les telles quelles, avec les abréviations.",
            "Pour chacune, calculez le prix réel si le chauffage n'est pas inclus.",
        ],
        notes="Devoir de repérage. Les trois annonces serviront de matériel réel pour "
              "l'appel du défi 1 : chacun appellera pour la sienne.")

    return d.save(dossier)
