# -*- coding: utf-8 -*-
"""E1 · À toi : comparer et choisir.
Bloc E · couleur teal (je me lance) · 90 min.
Source : section `appli` — comparer deux logements à l'oral, puis justifier par écrit.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='À toi : comparer et choisir',
        chapeau="Tout le module en une séance. Comparer deux logements à voix haute, "
                "choisir une annonce, et écrire au propriétaire pour expliquer pourquoi "
                "elle vous convient.",
        duree='90 minutes')

    d.titre(notes="Séance d'application. Aucun contenu nouveau. Rendre les billets de A1, "
                  "C3 et D1 : les priorités, ce qui décide, les besoins y sont déjà.")

    d.objectifs([
        "comparer deux logements à voix haute ;",
        "choisir une annonce selon ses propres besoins ;",
        "écrire un message au propriétaire ;",
        "relire son message avant de l'envoyer.",
    ])

    # ── premier temps · l'oral ─────────────────────────────────────
    d.regle("À l'oral · la comparaison",
            "Trois critères, et une décision à la fin.",
            precision="« Le premier est moins cher, mais le deuxième est plus près de "
                      "l'autobus et il est plus tranquille. Ce qui me décide, c'est le "
                      "transport. » Trois comparaisons, une décision.",
            notes="Écrire la structure au tableau. Elle combine la comparaison du module "
                  "7 et la construction emphatique de C2.")

    d.pratique('Pratique · 1 de 4', "Comparez deux annonces",
               "À deux. Trois critères, puis votre décision.", [
        ("Le prix", "le vrai coût, chauffage compris"),
        ("L'emplacement", "transport, école, épicerie"),
        ("Le logement lui-même", "pièces, bruit, luminosité"),
        ("Votre décision", "« Ce qui me décide, c'est… »"),
    ], corrige=False,
       notes="Vingt minutes. Circuler et vérifier deux choses : les comparaisons "
             "emploient-elles « plus… que » ? La décision emploie-t-elle la "
             "construction emphatique ?")

    d.cartes('Analyse', "Quatre critères pour choisir", [
        ("Le vrai coût",
         "Le loyer plus l'électricité, plus l'assurance, plus les électroménagers s'il "
         "en manque. C'est le calcul de la séance A2."),
        ("Les vrais besoins",
         "Deux ou trois, pas plus. Ce sans quoi vous ne pouvez pas vivre là. C'est le "
         "tri de la séance D1."),
        ("Ce qui inquiète, et sa solution",
         "Un défaut avec une solution n'est plus un défaut. Des rideaux épais règlent "
         "un bruit de rue."),
        ("Ce qui décide",
         "Une seule chose décide vraiment. Nommez-la : c'est ce qui vous permettra de "
         "trancher entre deux logements presque équivalents."),
    ], notes="Ces quatre critères résument le module entier. Les faire copier avant la "
             "production écrite.")

    # ── deuxième temps · l'écrit ───────────────────────────────────
    d.regle("À l'écrit · le message au propriétaire",
            "Qui vous êtes · pourquoi ce logement · ce que vous demandez.",
            precision="Trois paragraphes courts. Le premier vous présente, le deuxième "
                      "dit pourquoi ce logement vous convient, le troisième demande une "
                      "visite ou une réponse. Rien de plus.",
            notes="Un propriétaire reçoit dix messages. Celui qui explique pourquoi ce "
                  "logement-là attire l'attention. Le dire.")

    d.tableau('Écrire', "Le message, paragraphe par paragraphe",
              ['Le paragraphe', 'Ce qu\'il contient'],
              [["qui vous êtes", "votre nom, votre travail ou vos études, avec qui vous vivez"],
               ["pourquoi ce logement", "deux raisons précises, tirées de l'annonce"],
               ["ce que vous demandez", "une visite, avec vos disponibilités"],
               ["la signature", "nom complet et numéro de téléphone"]],
              cle=0, props=[0.3, 0.7],
              notes="Le deuxième paragraphe est celui qui distingue le message. Insister : "
                    "deux raisons tirées de l'annonce, pas des généralités.")

    d.pratique('Pratique · 2 de 4', "Écrivez le message",
               "Trois paragraphes courts, plus la signature.", [
        ("L'annonce choisie", "une des trois de la séance A4, ou une vraie annonce"),
        ("Pourquoi elle vous convient", "deux raisons précises, tirées de l'annonce"),
        ("Ce que vous demandez", "une visite, avec deux ou trois disponibilités"),
        ("À ne pas oublier", "votre nom complet et votre numéro"),
    ], corrige=False,
       notes="Vingt-cinq minutes d'écriture individuelle. Ramasser : ce message est "
             "l'évaluation écrite du module.")

    d.piege("Le piège du message général",
            "Bonjour, je suis intéressé par votre logement. Merci.",
            "Bonjour, votre 4 ½ de la rue Galt m'intéresse, surtout parce que la chambre donne sur la cour.",
            "Un message général se confond avec les neuf autres. Une raison précise, "
            "tirée de l'annonce, montre que vous l'avez lue — et qu'il ne s'agit pas "
            "d'un envoi automatique.",
            notes="Montrer les deux versions côte à côte. Demander laquelle obtiendrait "
                  "une réponse.")

    d.piege("Le piège du message sans disponibilités",
            "J'aimerais visiter le logement.",
            "Je suis disponible mardi et jeudi après 17 h, ou samedi toute la journée.",
            "Sans vos disponibilités, le propriétaire doit écrire pour les demander, puis "
            "attendre votre réponse. Deux jours perdus, et le logement peut être loué "
            "entre-temps. Donnez trois plages horaires.",
            notes="Conseil pratique concret. Faire ajouter les disponibilités à chaque "
                  "message pendant la relecture.")

    d.pratique('Pratique · 3 de 4', "Relecture croisée",
               "Échangez les messages. Six vérifications.", [
        ("Est-ce qu'on sait qui vous êtes ?", "nom, travail ou études, avec qui vous vivez"),
        ("Y a-t-il deux raisons tirées de l'annonce ?", "précises, pas générales"),
        ("Est-ce qu'on sait quand vous êtes disponible ?", "au moins deux plages"),
        ("Le numéro de téléphone est-il là ?", "sans lui, personne ne rappelle"),
        ("Les phrases sont-elles courtes ?", "trois paragraphes, pas une page"),
        ("Y a-t-il des fautes de temps ou d'accord ?", "relire les verbes"),
    ], corrige=True,
       notes="Une relecture croisée trouve deux fois plus d'oublis. Ramasser les versions "
             "corrigées, pas les premières.")

    d.pratique('Pratique · 4 de 4', "Préparez votre visite",
               "Les six questions de la séance B4, adaptées à votre annonce.", [
        ("Trois questions sur le logement", "pièces, bruit, état"),
        ("Deux questions sur les coûts", "ce qui est inclus, l'électricité de l'hiver"),
        ("Une question sur le quotidien", "stationnement, déneigement, animaux"),
        ("Votre phrase de conclusion", "« Je vous rappelle avant… »"),
    ], corrige=False,
       notes="Dix minutes. Cette liste est le vrai résultat du module : elle sert la "
             "prochaine fois que l'élève cherchera un logement.")

    d.billet(
        "En une phrase : qu'est-ce que vous ferez différemment à votre prochaine visite ?",
        exemples=[
            "Une seule chose, précise.",
            "Exemple : « je vais demander les factures d'électricité de l'hiver ».",
        ],
        notes="Lire quelques billets à voix haute, sans nommer les auteurs. C'est la "
              "meilleure préparation à la séance de bilan.")

    return d.save(dossier)
