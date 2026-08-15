# -*- coding: utf-8 -*-
"""E1 · À toi : la capsule et le slogan.
Bloc E · couleur teal (je me lance) · 90 min.
Source : section `appli` — analyser une publicité, puis créer la sienne.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='À toi : la capsule et le slogan',
        chapeau="Tout le module en une séance. Écrire une capsule de trente secondes, "
                "trouver son slogan, et la dire à voix haute devant le groupe — avec un "
                "seul mot mis en avant.",
        duree='90 minutes')

    d.titre(notes="Séance d'application. Aucun contenu nouveau. Rendre les billets de "
                  "A1, A4 et B3 : l'événement, la valeur et les slogans y sont déjà.")

    d.objectifs([
        "écrire une capsule de trente secondes pour un récepteur précis ;",
        "y placer un slogan et un seul mot mis en avant ;",
        "la dire à voix haute au bon rythme ;",
        "évaluer la capsule d'un autre selon les critères du module.",
    ])

    d.regle('La règle de la capsule',
            "Un récepteur · trois faits · un slogan · un mot mis en avant.",
            precision="Trente secondes ne permettent rien de plus. Trois faits : quoi, "
                      "quand, où. Un slogan à la fin. Et un seul mot dit plus fort que "
                      "les autres — celui qu'on veut qu'on retienne.",
            notes="Écrire les quatre au tableau. C'est le cahier des charges de la "
                  "production, et il tient en une ligne.")

    d.tableau('Analyse', "La capsule de Solange, décomposée",
              ['Le morceau', 'Le contenu'],
              [["le récepteur", "les gens qui gardent un appareil brisé chez eux"],
               ["fait 1", "on répare les objets brisés"],
               ["fait 2", "samedi 12 avril, de 9 h à 16 h"],
               ["fait 3", "au sous-sol du centre Sainte-Odile"],
               ["le slogan", "Rien ne se jette, tout se répare."],
               ["le mot mis en avant", "gratuit"]],
              cle=0, props=[0.3, 0.7],
              notes="Six lignes, trente secondes. C'est le modèle exact de ce que les "
                    "élèves vont produire.")

    d.pratique('Pratique · 1 de 4', "Écrivez votre capsule",
               "Trois faits, un slogan, trente secondes.", [
        ("Le récepteur", "celui de votre billet de A1 — écrivez-le en haut de la feuille"),
        ("Les trois faits", "quoi, quand, où — une phrase courte chacun"),
        ("Le slogan", "celui de votre billet de B3, ou un nouveau"),
        ("Le mot à mettre en avant", "soulignez-le"),
    ], corrige=False,
       notes="Vingt-cinq minutes d'écriture. Circuler et vérifier une seule chose : le "
             "récepteur est-il écrit en haut de la feuille ? Sans lui, rien ne tient.")

    d.pratique('Pratique · 2 de 4', "Chronométrez et coupez",
               "Lisez à voix haute et comptez les secondes.", [
        ("Plus de trente-cinq secondes ?", "coupez une phrase — n'accélérez pas"),
        ("Quelle phrase couper ?", "celle qui n'aide pas votre récepteur"),
        ("Moins de vingt secondes ?", "ajoutez un détail concret, pas une phrase vague"),
        ("Relisez à voix haute", "et rechronométrez"),
    ], corrige=False,
       notes="C'est l'étape que tout le monde saute. L'imposer : chacun chronomètre son "
             "voisin, puis on échange.")

    d.cartes('Dire', "Quatre points avant de lire à voix haute", [
        ("Un seul mot mis en avant",
         "Syllabe allongée, ton qui monte. Un seul, sinon rien ne ressort. C'est la "
         "leçon de A2."),
        ("Le rythme, pas la vitesse",
         "Trente secondes, c'est du texte qu'on dit calmement. Si vous devez accélérer, "
         "c'est qu'il y a trop de texte."),
        ("Les pauses",
         "Une courte pause avant le slogan lui donne du poids. C'est le seul silence "
         "de la capsule, et il fait tout."),
        ("La fin nette",
         "Le slogan se dit d'un trait, puis on s'arrête. Ne rien ajouter après : "
         "c'est la dernière chose qu'on entend."),
    ], notes="La troisième carte est celle qu'on n'enseigne jamais et qui change le plus "
             "l'effet. Faire essayer avec et sans la pause.")

    d.pratique('Pratique · 3 de 4', "Dites votre capsule",
               "Devant le groupe, debout, sans se presser.", [
        ("Avant de commencer", "respirez, et dites d'abord à qui vous parlez"),
        ("Pendant", "un seul mot mis en avant, une pause avant le slogan"),
        ("Le groupe écoute", "et note le mot mis en avant"),
        ("Après", "le groupe dit ce qu'il a retenu"),
    ], corrige=False,
       notes="Vingt minutes. C'est le moment le plus exposé du module : féliciter chaque "
             "passage avant toute remarque. Le groupe note, mais ne corrige pas.")

    d.pratique('Pratique · 4 de 4', "Évaluez la capsule d'un autre",
               "Cinq questions, dans l'ordre.", [
        ("À qui cette capsule s'adressait-elle ?", "si vous ne savez pas, c'est raté"),
        ("Quel mot était mis en avant ?", "un seul mot doit ressortir"),
        ("Quels trois faits avez-vous retenus ?", "quoi, quand, où"),
        ("Quel était le slogan ?", "de mémoire, sans regarder"),
        ("Quelle valeur portait-elle ?", "écologie, entraide, autonomie…"),
    ], corrige=True,
       notes="L'évaluation par les pairs est plus formatrice que la vôtre. Insister sur "
             "« de mémoire » : c'est le vrai test d'un slogan.")

    d.piege("Le piège de la capsule sans récepteur",
            "Vous écrivez pour tout le monde, et personne ne se reconnaît.",
            "Vous écrivez pour les gens qui gardent un appareil brisé.",
            "C'est le piège de la première séance et c'est celui qui revient à la "
            "dernière. Une capsule sans récepteur choisi contient trop de choses, dépasse "
            "trente secondes, et ne se retient pas.",
            notes="Boucler le module sur sa règle centrale. Si un seul élément est acquis "
                  "en sortant, ce doit être celui-là.")

    d.billet(
        "En une phrase : qu'est-ce que vous remarquez maintenant dans les publicités ?",
        exemples=[
            "Une seule chose, précise.",
            "Exemple : « je cherche toujours à qui elles parlent ».",
        ],
        notes="Lire quelques billets à voix haute, sans nommer les auteurs. C'est la "
              "meilleure préparation à la séance de bilan.")

    return d.save(dossier)
