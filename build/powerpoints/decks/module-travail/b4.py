# -*- coding: utf-8 -*-
"""B4 · Laisser un message dans une boîte vocale.
Bloc B · couleur teal (écoute et réponds) · 60 min.
Source : production orale du défi 1, appuyée sur B1 et B2.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='teal',
        titre='Laisser un message',
        chapeau="Trente secondes, seul face à un répondeur, sans personne pour aider. "
                "C'est l'exercice oral que les élèves redoutent le plus — et celui "
                "qu'ils utiliseront le plus souvent.",
        duree='60 minutes')

    d.titre(notes="Séance de production orale. Prévoir des téléphones ou un "
                  "enregistreur : s'entendre est ce qui fait progresser le plus vite. "
                  "Rendre les billets de B1 et B2 au début.")

    d.objectifs([
        "laisser un message complet en trente secondes ;",
        "dire son nom et son numéro lentement et deux fois ;",
        "garder le calme quand le répondeur se déclenche ;",
        "écouter son propre message et le corriger.",
    ])

    d.regle('La règle des trente secondes',
            "Six parties, une phrase chacune, et on raccroche.",
            precision="Un message de plus d'une minute est rarement écouté jusqu'au bout. "
                      "Six phrases suffisent : salutation, identité, raison, demande, "
                      "remerciement, salutation finale.",
            notes="Chronométrer un message modèle devant le groupe. Trente secondes, "
                  "c'est plus long qu'ils ne le croient.")

    d.cartes('Avant de composer', "Quatre choses à préparer", [
        ("Écrivez votre message",
         "Six lignes sur un papier, devant vous. Ce n'est pas tricher : tous les "
         "professionnels le font."),
        ("Ayez votre numéro écrit",
         "On oublie son propre numéro quand on est nerveux. Écrivez-le en gros "
         "chiffres."),
        ("Trouvez un endroit calme",
         "Un message enregistré dans le bruit est inaudible. Deux minutes de plus pour "
         "trouver un coin tranquille valent la peine."),
        ("Respirez avant de parler",
         "Le répondeur ne coupe pas au bout de deux secondes. Prenez le temps de "
         "commencer calmement."),
    ], notes="La première carte lève une gêne réelle : beaucoup d'élèves croient qu'il "
             "faudrait pouvoir improviser. Non — on écrit d'abord.")

    d.tableau('Analyse', "Le message modèle, chronométré",
              ['La phrase', 'Durée'],
              [["Bonjour, Madame Bélisle.", "2 secondes"],
               ["Ici Karim Haddad.", "2 secondes"],
               ["Je vous appelle parce que ma voiture est tombée en panne.", "4 secondes"],
               ["J'aurai environ trente minutes de retard.", "3 secondes"],
               ["Pouvez-vous me rappeler au 514 555-0134 ? Je répète : 514 555-0134.", "10 secondes"],
               ["Merci beaucoup. Bonne journée.", "3 secondes"]],
              cle=0, props=[0.75, 0.25],
              notes="Vingt-quatre secondes en tout, dont dix pour le numéro répété. "
                    "C'est le bon rapport : le numéro mérite un tiers du message.")

    d.pratique('Pratique · 1 de 4', "Dites votre numéro",
               "Lentement, par groupes de trois ou quatre chiffres, deux fois.", [
        ("514 555-0134", "cinq-un-quatre… cinq-cinq-cinq… zéro-un-trois-quatre"),
        ("438 555-0182", "quatre-trois-huit… cinq-cinq-cinq… zéro-un-huit-deux"),
        ("Votre propre numéro", "à dire deux fois, lentement"),
    ], corrige=True,
       notes="Faire dire chiffre par chiffre, pas par nombres à deux chiffres : "
             "« zéro-un-trois-quatre », pas « zéro-treize-quatre ». C'est plus clair au "
             "téléphone.")

    d.pratique('Pratique · 2 de 4', "Épelez votre nom",
               "L'alphabet français, lentement. Un nom mal noté n'est jamais rappelé.", [
        ("HADDAD", "H-A-D-D-A-D"),
        ("BENSALEM", "B-E-N-S-A-L-E-M"),
        ("Votre propre nom de famille", "lettre par lettre, à voix haute"),
    ], corrige=True,
       notes="Beaucoup d'élèves n'ont jamais épelé leur nom en français. Prendre le "
             "temps : les lettres G, J, E et I sont les plus problématiques.")

    d.piege("Le piège du répondeur qui surprend",
            "« Allô ? Ah, c'est un répondeur… euh… bonjour… »",
            "Bonjour, Madame Bélisle. Ici Karim Haddad.",
            "On appelle en s'attendant à parler à quelqu'un, et le répondeur surprend. "
            "Les trois premières secondes du message sont alors perdues. Préparez-vous à "
            "tomber sur un répondeur : c'est le cas le plus fréquent.",
            notes="Faire l'expérience : appeler un vrai numéro de messagerie devant le "
                  "groupe et laisser un message. La démonstration vaut mieux que "
                  "l'explication.")

    d.piege("Le piège de la vitesse",
            "Le numéro dit en deux secondes, une seule fois.",
            "Le numéro dit lentement, deux fois, à la fin.",
            "Personne n'écoute une boîte vocale avec un crayon à la main. La personne "
            "réécoutera le message pour prendre le numéro — s'il est audible. Sinon, "
            "elle ne rappellera pas.",
            notes="Faire écouter deux versions du même numéro, rapide et lente. Demander "
                  "au groupe de le noter : seule la seconde version fonctionne.")

    d.pratique('Pratique · 3 de 4', "Enregistrez votre message",
               "Six phrases, trente secondes. Puis réécoutez-vous.", [
        ("Situation 1", "Vous serez en retard de quarante minutes : panne d'autobus."),
        ("Situation 2", "Vous serez absent demain : rendez-vous médical pour votre enfant."),
        ("Situation 3", "Vous devez abandonner le cours : vous déménagez dans une autre ville."),
    ], corrige=False,
       notes="Chacun choisit une situation, écrit son message, l'enregistre sur son "
             "téléphone, puis se réécoute. Vingt minutes. Circuler et écouter deux ou "
             "trois enregistrements.")

    d.pratique('Pratique · 4 de 4', "Écoutez-vous et corrigez",
               "Cinq vérifications sur votre propre enregistrement.", [
        ("Ai-je dit mon nom complet ?", "prénom et nom de famille"),
        ("Ai-je dit la raison en une phrase ?", "sans excuse longue"),
        ("Ai-je donné une heure ?", "d'arrivée ou de retour"),
        ("Ai-je répété mon numéro ?", "deux fois, lentement"),
        ("Est-ce que ça tient en trente secondes ?", "chronométrez"),
    ], corrige=True,
       notes="C'est l'exercice le plus formateur de la séance. Insister pour que chacun "
             "se réécoute vraiment : beaucoup n'oseront pas.")

    d.billet(
        "Après vous être réécouté : qu'est-ce que vous changeriez dans votre message ?",
        exemples=[
            "Une chose seulement, précise.",
            "Exemple : « je parlais trop vite pour le numéro ».",
        ],
        notes="Relever les réponses les plus fréquentes et y revenir en C4, où le même "
              "exercice se fait en conversation directe.")

    return d.save(dossier)
