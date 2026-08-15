# -*- coding: utf-8 -*-
"""A4 · Deux appels au centre de formation.
Bloc A · couleur acier (compréhension orale) · 60 min.
Source : dialogues `dial1` et `dial2`, exercice `aSecretaire`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='acier',
        titre='Deux appels au centre de formation',
        chapeau="Un changement d'horaire, une entrevue confirmée. Deux appels courts, "
                "et dans les deux cas la même question à se poser : qu'est-ce que je "
                "dois retenir avant de raccrocher ?",
        duree='60 minutes')

    d.titre(notes="Séance de compréhension orale. Prévenir le groupe : on écoutera "
                  "chaque dialogue deux fois, pas plus. Prendre des notes est autorisé "
                  "et même attendu.")

    d.objectifs([
        "repérer le but d'un appel dès les premières phrases ;",
        "noter les documents à apporter et les dates ;",
        "comprendre une heure de rendez-vous et la confirmer ;",
        "savoir quoi noter pendant un appel.",
    ])

    d.regle("Ce qu'il faut noter pendant un appel",
            "Qui appelle · pourquoi · quelle date · quels documents · quel numéro.",
            precision="Cinq informations. Un appel professionnel en contient rarement "
                      "plus, et presque jamais moins. Avoir un papier et un crayon près "
                      "du téléphone change tout.",
            notes="Écrire les cinq au tableau avant la première écoute. Les élèves "
                  "prendront des notes sur cette grille.")

    d.dialogue('Dialogue 1 · un changement d\'horaire', "Est-il possible de changer mon horaire ?", [
        ("LA SECRÉTAIRE", "Bonjour, centre de formation, je vous écoute.", False),
        ("OMAR", "Bonjour, j'aimerais savoir s'il est possible de changer mon horaire de "
                 "cours.", True),
        ("LA SECRÉTAIRE", "Oui, c'est possible. Vous devez seulement apporter une preuve "
                          "d'emploi et remplir un formulaire signé.", True),
        ("OMAR", "D'accord, et la nouvelle grille horaire s'applique à partir de quand ?",
         True),
        ("LA SECRÉTAIRE", "Dès le mois prochain.", True),
    ], consigne="Écoutez deux fois, diapo masquée. Notez les cinq informations.",
       notes="Faire remarquer la formule d'Omar : « j'aimerais savoir s'il est possible "
             "de… ». C'est la formule polie du module 2, réemployée ici.")

    d.pratique('Pratique · 1 de 4', "Dialogue 1 — trois questions",
               "Répondez d'après ce que vous avez noté.", [
        ("Le but de l'appel concerne un changement de quoi ?", "d'horaire de cours"),
        ("Quels documents faut-il apporter ?", "une preuve d'emploi et un formulaire signé"),
        ("Quand la nouvelle grille entre-t-elle en vigueur ?", "le mois prochain"),
    ], corrige=True,
       notes="La deuxième question est celle qui compte : deux documents, pas un. "
             "Beaucoup n'en retiendront qu'un.")

    d.dialogue('Dialogue 2 · une confirmation de poste', "Est-ce que quinze heures vous convient ?", [
        ("L'EMPLOYEUSE", "Bonjour, je vous appelle pour confirmer votre entrevue pour le "
                         "poste d'aide-cuisinier.", True),
        ("AZIZ", "Ah oui, parfait, merci de me rappeler.", False),
        ("L'EMPLOYEUSE", "Est-ce que quinze heures cet après-midi vous convient ?", True),
        ("AZIZ", "Oui, tout à fait, je serai là.", True),
        ("L'EMPLOYEUSE", "Très bien, à tout à l'heure.", False),
    ], consigne="Écoutez deux fois, diapo masquée. Notez les cinq informations.",
       notes="Faire remarquer la réponse d'Aziz : « je serai là » confirme. Un simple "
             "« oui » aurait laissé un doute.")

    d.pratique('Pratique · 2 de 4', "Dialogue 2 — trois questions",
               "Répondez d'après ce que vous avez noté.", [
        ("Quel est le but de l'appel ?", "confirmer une entrevue"),
        ("Pour quel poste Aziz a-t-il postulé ?", "aide-cuisinier"),
        ("À quelle heure doit-il se présenter ?", "à quinze heures, cet après-midi"),
    ], corrige=True,
       notes="Faire écrire « 15 h » et « quinze heures » au tableau. Les deux se lisent, "
             "et l'oral n'en donne qu'une des deux.")

    d.cartes('Analyse', "Quatre réflexes au téléphone", [
        ("Répétez l'heure et la date",
         "« Quinze heures cet après-midi, c'est noté. » L'autre personne corrigera tout "
         "de suite si vous avez mal entendu."),
        ("Épelez votre nom",
         "« Haddad, H-A-D-D-A-D. » Un nom mal noté, c'est un dossier introuvable et un "
         "rappel qui n'arrive jamais."),
        ("Demandez à qui vous parlez",
         "« À qui est-ce que je parle, s'il vous plaît ? » Notez le nom : il faudra "
         "peut-être rappeler."),
        ("Confirmez avant de raccrocher",
         "« Donc j'apporte une preuve d'emploi et le formulaire signé, c'est bien "
         "ça ? » Trente secondes qui évitent un deuxième déplacement."),
    ], notes="Ces quatre réflexes valent pour tous les appels du module. Les faire "
             "copier et les rappeler à chaque jeu de rôle.")

    d.tableau('Analyse', "L'heure, à l'oral et à l'écrit",
              ['On dit', 'On écrit'],
              [["neuf heures et demie", "9 h 30"],
               ["quinze heures", "15 h"],
               ["dix heures et quart", "10 h 15"],
               ["midi et demi", "12 h 30"],
               ["seize heures quarante-cinq", "16 h 45"]],
              cle=1,
              note="Au Québec, l'écrit officiel emploie l'heure de zéro à vingt-quatre. "
                   "L'oral emploie souvent les deux.",
              notes="Faire lire la colonne de droite à voix haute : c'est la conversion "
                    "qu'on doit faire en écoutant un message.")

    d.pratique('Pratique · 3 de 4', "Écrivez l'heure",
               "Passez de l'oral à l'écrit.", [
        ("neuf heures et demie du matin", "9 h 30"),
        ("trois heures de l'après-midi", "15 h"),
        ("dix heures et quart", "10 h 15"),
        ("une heure moins le quart de l'après-midi", "12 h 45"),
        ("huit heures moins dix du matin", "7 h 50"),
    ], corrige=True,
       notes="Les deux derniers items emploient « moins ». C'est la construction la plus "
             "difficile : la travailler lentement.")

    d.piege("Le piège du « oui » qui ne confirme rien",
            "— Est-ce que quinze heures vous convient ? — Oui.",
            "— Oui, quinze heures, je serai là.",
            "Un « oui » seul peut vouloir dire « j'ai entendu ». En répétant l'heure et "
            "en ajoutant « je serai là », vous confirmez vraiment — et vous vérifiez en "
            "même temps que vous avez bien entendu.",
            notes="Faire pratiquer trois confirmations à voix haute. C'est un réflexe qui "
                  "s'installe vite.")

    d.pratique('Pratique · 4 de 4', "Le message de la secrétaire",
               "Un message est laissé à monsieur Diallo au sujet d'une inscription.", [
        ("Quel est le but de l'appel ?",
         "l'informer des dates et des documents pour l'inscription"),
        ("Quand les inscriptions commencent-elles ?", "la semaine prochaine"),
        ("Pourquoi doit-il se rendre au centre ?", "pour confirmer son inscription"),
        ("Quels documents faut-il apporter ?", "une pièce d'identité et une preuve de résidence"),
    ], corrige=True,
       notes="Lire le message à voix haute deux fois avant d'afficher les questions. "
             "Programme visé : soutien informatique.")

    d.billet(
        "Écrivez les cinq informations à noter pendant un appel.",
        exemples=[
            "Qui · pourquoi · quelle date · quels documents · quel numéro.",
            "Ajoutez une sixième ligne : ce que vous répétez avant de raccrocher.",
        ],
        notes="Ces cinq lignes forment une grille de prise de notes. Suggérer de la "
              "recopier près du téléphone à la maison.")

    return d.save(dossier)
