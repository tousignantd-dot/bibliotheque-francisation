# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots.
Bloc E · couleur foret (vocabulaire et bilan) · 60 min.
Source : les 16 cartes mémoire du module, autoévaluation, révision des 9 savoirs.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='foret',
        titre='Je retiens des mots',
        chapeau="Dernière séance du module. On rassemble le vocabulaire, on revoit les "
                "neuf savoirs, et chacun fait le point sur ce qu'il est maintenant "
                "capable de faire.",
        duree='60 minutes')

    d.titre(notes="Séance de bilan. Ton différent des autres : on ne présente rien de "
                  "nouveau. Laisser beaucoup de place aux questions restées en suspens.")

    d.objectifs([
        "revoir les seize mots essentiels du module ;",
        "retrouver les neuf savoirs travaillés et savoir où chacun sert ;",
        "évaluer honnêtement ce que je suis maintenant capable de faire ;",
        "savoir où retourner chercher ce qui n'est pas encore acquis.",
    ])

    d.vocabulaire('Vocabulaire · 1 de 3', "Le logement et ses appareils", [
        ("un calorifère", "L'appareil fixé au mur qui chauffe une pièce."),
        ("un disjoncteur", "L'interrupteur du panneau électrique qui coupe le courant."),
        ("un chauffage d'appoint", "Un petit appareil de chauffage ajouté temporairement."),
        ("le bail", "Le contrat signé entre le locataire et le propriétaire."),
        ("un couvreur", "La personne qui répare les toitures."),
        ("un dégraissant", "Un produit fort qui enlève l'huile et la graisse."),
    ], notes="Cacher la colonne de droite et faire donner les définitions par le groupe. "
             "Puis l'inverse : cacher la gauche et faire retrouver les mots.")

    d.vocabulaire('Vocabulaire · 2 de 3', "Ce qui abîme un logement", [
        ("une infiltration", "De l'eau qui entre par le toit ou par un mur."),
        ("la moisissure", "Des taches noires ou vertes causées par l'humidité."),
        ("l'insalubrité", "L'état d'un logement malpropre ou dangereux pour la santé."),
        ("l'ampleur", "La grandeur, l'importance d'un problème."),
        ("encombrer", "Occuper une place et gêner le passage."),
    ], notes="Faire produire une phrase complète avec chaque mot, en lien avec le logement "
             "réel de l'élève.")

    d.vocabulaire('Vocabulaire · 3 de 3', "Demander et garder une trace", [
        ("se plaindre", "Dire qu'on n'accepte plus une situation et demander qu'elle change."),
        ("un avis écrit", "Une lettre ou un courriel qui garde une trace d'une demande."),
        ("un recours", "Le moyen légal de faire régler un problème qui traîne."),
        ("une partie commune", "Un espace de l'immeuble partagé par tous les locataires."),
        ("une sortie de secours", "Le chemin à garder libre pour évacuer en cas d'incendie."),
    ], notes="Ces cinq mots sont ceux du droit et de la démarche. Ce sont aussi ceux que "
             "les élèves oublient le plus vite, parce qu'ils servent moins souvent.")

    d.tableau('Révision · 1 de 2', "Les savoirs du module",
              ['Le savoir', 'La règle en une phrase', 'Séance'],
              [["[ø] et [œ]", "la fin du mot écrit décide", "A2"],
               ["Les métiers", "on retient la matière, pas le problème", "A3"],
               ["Les droits", "on parle, on écrit, puis on dépose", "B4"],
               ["leur / leurs", "le nom qui suit décide, lui seul", "B2"]],
              cle=1, props=[0.28, 0.57, 0.15],
              note="Pour chaque ligne : est-ce que vous sauriez l'expliquer à quelqu'un "
                   "qui n'était pas là ? C'est le vrai test.",
              notes="Faire cocher individuellement. Les lignes non cochées indiquent où "
                    "renvoyer l'élève dans le module en ligne.")

    d.tableau('Révision · 2 de 2', "Les savoirs du module",
              ['Le savoir', 'La règle en une phrase', 'Séance'],
              [["depuis / ça fait… que", "regardez ce qui vient après", "B3"],
               ["avant de / après avoir", "après « avant de », l'action est deuxième", "C2"],
               ["faire + infinitif", "les deux verbes se touchent", "C3"],
               ["Privé, coop, HLM", "trois logiques, trois interlocuteurs", "C4"],
               ["Se plaindre", "le fait, l'effet sur moi, la demande", "D2"]],
              cle=1, props=[0.28, 0.57, 0.15],
              note="Neuf savoirs en tout. Le dernier sert le plus souvent.",
              notes="Faire nommer par le groupe le savoir qui leur a semblé le plus utile. "
                    "Utile pour ajuster la prochaine fois qu'on donne le module.")

    d.cartes('Bilan', "Je suis maintenant capable de…", [
        ("Nommer un problème précisément",
         "Avec l'appareil, la pièce, la durée et un chiffre — pas avec « il y a un "
         "problème ». Séances A1 et A4."),
        ("Savoir qui appeler, et dans quel ordre",
         "Le bon métier pour le bon problème, mais surtout : prévenir la propriétaire "
         "avant tout. Séances A3 et B4."),
        ("Mener l'appel jusqu'au bout",
         "Me présenter, décrire, donner un chiffre, dire ce que j'ai vérifié, demander "
         "une solution temporaire. Séances B1 et E1."),
        ("Laisser une trace écrite",
         "Un courriel de trois lignes, daté, avec une demande claire. C'est ce qui protège "
         "quand ça traîne. Séances B4 et E1."),
    ], notes="Faire l'autoévaluation à main levée, honnêtement. Sur les points faibles, "
             "renvoyer aux séances précises indiquées.")

    d.cartes('Bilan', "Et aussi…", [
        ("Me plaindre sans me fâcher",
         "Le fait, l'effet sur moi, la demande — et une échelle d'intensité que je monte "
         "seulement si rien ne bouge. Séance D2."),
        ("Comprendre où j'habite",
         "Privé, coopérative ou HLM : qui décide, qui paie, à qui je m'adresse. Séance C4."),
        ("Dire depuis quand",
         "Trois façons de répondre à la question la plus posée au téléphone, avec le verbe "
         "au présent. Séance B3."),
        ("Prononcer le vocabulaire du logement",
         "Les mots en -eur et en -eux, qui sont partout dans ce champ lexical. Séance A2."),
    ], notes="Terminer là-dessus : le module a servi à parler, pas seulement à apprendre "
             "des règles.")

    d.regle('La phrase à emporter',
            "Signaler tôt, nommer précisément, garder une trace.",
            precision="Trois gestes, dans cet ordre, quel que soit le problème et quel que "
                      "soit le type de logement. Tout le reste du module n'est que la "
                      "manière de les faire en français.",
            notes="Écrire les trois gestes au tableau et les y laisser jusqu'à la fin du "
                  "cours. C'est ce qui restera dans six mois.")

    d.billet(
        "Qu'est-ce que vous ferez différemment la prochaine fois qu'un problème surviendra chez vous ?",
        exemples=[
            "Une phrase, concrète. Pas une intention générale.",
            "Exemple : « Je vais prendre une photo avec la date avant d'appeler. »",
        ],
        notes="Dernier billet du module. Le lire à voix haute, anonymement, à la fin du "
              "cours : c'est le meilleur bilan collectif possible.")

    return d.save(dossier)
