# -*- coding: utf-8 -*-
"""D2 · À la caisse.
Bloc D « Défi 3 · L'étiquette et le paiement » · couleur teal · 60 min.
Source : dialogue `t3b`, exercices `t3payer`, `t3b` et `t3montant`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-vetements/images/')


def build(dossier):
    d = Deck(
        code='D2', section='teal',
        titre='À la caisse',
        chapeau="Le caissier pose toujours les mêmes questions. Il reste "
                "ensuite un chiffre à comprendre, une carte à insérer, et un "
                "papier à garder.",
        duree='60 minutes')

    d.titre(notes="Séance d'écoute. Prévoir le son : les montants doivent être entendus, "
                  "pas lus. C'est ce qui est difficile.")

    d.objectifs([
        "comprendre les questions courantes d'un caissier ;",
        "comprendre un montant dit à voix haute ;",
        "demander de répéter le montant ;",
        "vérifier un prix et garder sa facture.",
    ])

    d.declencheur(
        'Observation', "Que vous demande-t-on, à la caisse ?",
        image=IMG + 'terminal-paiement.jpg',
        pistes=[
            "Combien de questions, d'habitude ?",
            "Lesquelles comprenez-vous bien ?",
            "Laquelle est la plus difficile ?",
            "Que faites-vous quand vous n'avez pas compris ?",
        ],
        notes="Le montant est presque toujours la réponse : il est dit vite et il contient "
              "deux nombres.")

    d.dialogue('Dialogue · 1 de 3', "Le montant", [
        ("KEVIN", "Le manteau grand, et les bottes en liquidation. Ça fait cent soixante-quatre dollars et quatre-vingt-quinze.", True),
        ("FARIDA", "Pardon, vous pouvez répéter le montant ?", True),
        ("KEVIN", "Cent soixante-quatre quatre-vingt-quinze. Cent soixante-quatre dollars et quatre-vingt-quinze cents.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Le caissier répète en deux façons : le raccourci, puis la forme complète. "
             "C'est ce que font les gens d'ici quand on leur demande de répéter.")

    d.dialogue('Dialogue · 2 de 3', "La vérification", [
        ("FARIDA", "Attendez… les bottes, c'est bien soixante-cinq ?", True),
        ("KEVIN", "Je regarde… oui, soixante-cinq. La liquidation est passée.", True),
    ], notes="Farida vérifie le prix du défi 2. C'est la boucle du module : elle emploie ce "
             "qu'elle a appris trois séances plus tôt.")

    d.dialogue('Dialogue · 3 de 3', "La facture", [
        ("KEVIN", "Vous voulez la facture dans le sac ?", True),
        ("FARIDA", "Non, je la garde dans ma poche.", True),
        ("KEVIN", "Bonne idée. Gardez-la : c'est elle qui prouve le prix que vous avez payé.", True),
    ], notes="Dernière réplique du module. Elle dit pourquoi on garde une facture, sans "
             "aller jusqu'à l'échange — qui appartient au niveau 4.")

    d.tableau('Analyse', "Cinq questions, cinq réponses",
              ['Le caissier demande', 'On répond'],
              [["Vous avez tout trouvé ?", "« Oui, merci. »"],
               ["Ça fait cent soixante-quatre.", "« Vous pouvez répéter ? »"],
               ["Débit ou crédit ?", "« Débit, s'il vous plaît. »"],
               ["Insérez votre carte.", "on insère et on tape le NIP"],
               ["La facture dans le sac ?", "« Non, je la garde. »"]],
              cle=0,
              note="Cinq échanges, et l'achat est fini.",
              notes="Diapo à photographier. C'est le script complet de la caisse.")

    d.regle("Un montant contient deux nombres",
            "« Cent soixante-quatre quatre-vingt-quinze »",
            precision="Les dollars d'abord, les cents ensuite, et souvent sans dire ni "
                      "« dollars » ni « cents ». C'est ce raccourci qui rend le montant "
                      "difficile à saisir. Demander de répéter fait presque toujours "
                      "obtenir la forme longue — celle qu'on comprend.",
            notes="Diapo à photographier. Faire écouter cinq montants au raccourci, puis "
                  "les mêmes en forme longue.")

    d.cartes("Trois façons de payer", "Ce que le caissier demande", [
        ("Comptant",
         "En argent, avec des billets et de la monnaie. Le caissier demande « vous payez "
         "comptant ? »."),
        ("Débit",
         "La carte de la banque : l'argent sort du compte tout de suite. On insère la "
         "carte et on tape son NIP."),
        ("Crédit",
         "La carte de crédit : on paie plus tard, et il y a des intérêts si on ne paie "
         "pas tout le mois suivant."),
    ], notes="Ne pas donner de conseil financier : nommer les trois modes et leur "
             "fonctionnement suffit à ce niveau.")

    d.piege("Dire oui sans avoir compris le montant",
            "Oui, oui… (et on insère la carte)",
            "Pardon, vous pouvez répéter le montant ?",
            "Le montant est le seul chiffre que la machine vous fera approuver. Une fois "
            "la carte insérée, c'est fait. Deux secondes de question valent mieux qu'une "
            "surprise sur le relevé.",
            notes="Faire répéter la question par tout le groupe. C'est la même phrase de "
                  "secours que celle du défi 1.")

    d.vocabulaire('Vocabulaire', "Les huit derniers mots du module", [
        ("un cintre", "Le crochet qui tient le vêtement suspendu."),
        ("serré", "Se dit d'un vêtement trop petit, qui presse le corps."),
        ("un rabais", "L'argent qu'on enlève du prix pendant quelques jours."),
        ("une étiquette de prix", "Le petit carton attaché au vêtement, qui dit le prix."),
        ("la liquidation", "La vente des derniers articles, à très bas prix."),
        ("une étiquette d'entretien", "L'étiquette du col, qui dit comment laver."),
        ("la sécheuse", "La machine chaude qui sèche le linge."),
        ("la facture", "Le papier qui prouve le prix payé."),
    ], notes="Seconde moitié du banc, la première était en A4. Faire répéter avec "
             "l'article.")

    d.pratique('Pratique', "Moins de 50 $ ou plus de 50 $ ?",
               "Écoutez chaque montant.", [
        ("quarante-neuf dollars et quatre-vingt-dix-neuf", "moins de 50 $"),
        ("soixante-cinq dollars", "plus de 50 $"),
        ("vingt-huit dollars et cinquante", "moins de 50 $"),
        ("cent trente dollars", "plus de 50 $"),
        ("quatorze dollars et quatre-vingt-dix-neuf", "moins de 50 $"),
        ("cent soixante-quatre dollars et quatre-vingt-quinze", "plus de 50 $"),
    ], corrige=True,
       notes="Utiliser l'exercice 5 du défi 3, à cartes écoutables. Deux écoutes avant de "
             "corriger. Le premier montant est le piège : il est tout près de 50 $.")

    d.billet(
        "Écrivez cinq montants en lettres, puis lisez-les à voix haute.",
        exemples=[
            "Prenez des prix réels de vêtements.",
            "Ex. : « 39,99 $ — trente-neuf quatre-vingt-dix-neuf ».",
        ],
        notes="Fin du défi 3. Rendre à la séance suivante. Corriger surtout la lecture à "
              "voix haute.")

    return d.save(dossier)
