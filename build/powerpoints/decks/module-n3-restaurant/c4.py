# -*- coding: utf-8 -*-
"""C4 · Le préposé ou le client ?
Bloc C « Défi 2 · Commander au comptoir » · couleur teal · 75 min.
Source : exercices `t2qui` (cartes à écouter) et `t2phrases`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-restaurant/images/')


def build(dossier):
    d = Deck(
        code='C4', section='teal',
        titre='Le préposé ou le client ?',
        chapeau="Dans une file, on entend dix commandes avant la sienne. "
                "Savoir qui dit quoi, c'est arriver au comptoir en sachant "
                "déjà ce qui va se passer.",
        duree='75 minutes')

    d.titre(notes="Séance d'écoute et de reconnaissance. Le module interactif a le même "
                  "exercice avec des cartes écoutables : le projeter si possible.")

    d.objectifs([
        "reconnaître à l'oreille qui parle, du préposé ou du client ;",
        "comprendre les phrases affichées ou dites au comptoir ;",
        "profiter de la file pour se préparer ;",
        "comprendre un montant dit à voix haute.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'on entend, dans une file ?",
        image=IMG + 'file-comptoir.jpg',
        pistes=[
            "Combien de commandes passent avant la vôtre ?",
            "Est-ce que les questions changent d'une personne à l'autre ?",
            "Qu'est-ce qu'on peut apprendre en attendant ?",
            "Qu'est-ce qui est le plus difficile à entendre ?",
        ],
        notes="Amener le groupe à voir la file comme un temps d'écoute gratuite. C'est "
              "une stratégie d'apprenant, et elle vaut pour la banque, la pharmacie et "
              "le bureau de poste aussi.")

    d.pratique('Écoute', "Qui dit cette phrase ?",
               "Le préposé, ou le client ?", [
        ("Prochaine personne, s'il vous plaît.", "le préposé"),
        ("Je voudrais un trio sandwich au poulet.", "le client"),
        ("Pour ici ou pour emporter ?", "le préposé"),
        ("Est-ce que je peux avoir une soupe aussi ?", "le client"),
        ("Ça fait onze dollars et quarante.", "le préposé"),
        ("Débit, s'il vous plaît.", "le client"),
    ], corrige=True,
       notes="Dire chaque phrase sans la montrer. Les élèves lèvent une main pour le "
             "préposé, deux pour le client. L'enseignante voit tout de suite qui hésite.")

    d.tableau('Analyse', "Ce qui distingue les deux",
              ['Le préposé', 'Le client'],
              [["pose des questions", "répond, et pose peu de questions"],
               ["emploie l'impératif : servez-vous", "emploie « je voudrais »"],
               ["dit les montants et les numéros", "répète les numéros"],
               ["dit « vous »", "dit « vous » aussi"]],
              cle=0,
              note="Les deux se vouvoient : on ne se connaît pas.",
              notes="Diapo à photographier. La dernière ligne surprend souvent : le "
                    "vouvoiement va dans les deux sens, ce n'est pas une marque de "
                    "hiérarchie.")

    d.tableau('Analyse', "Les phrases du comptoir",
              ['On entend', 'Ça veut dire'],
              [["Ce sera tout ?", "avez-vous fini de commander ?"],
               ["Taxes en sus.", "le prix du tableau va monter un peu"],
               ["Servez-vous.", "prenez-en vous-même, sans demander"],
               ["Votre numéro est le 42.", "on appellera ce chiffre"]],
              cle=1,
              note="« Servez-vous » est une invitation, jamais un reproche.",
              notes="Diapo à photographier. Faire chercher où chaque phrase apparaît "
                    "dans les dialogues du module.")

    d.regle("Comprendre un montant dit vite",
            "« Ça fait onze dollars et quarante. »",
            precision="Le montant se dit en deux morceaux : les dollars, puis "
                      "les cents. « Onze quarante » veut dire onze dollars et "
                      "quarante cents. Si on n'a pas saisi, l'écran du terminal "
                      "l'affiche aussi.",
            notes="Diapo à photographier. Rappeler qu'on peut toujours regarder l'écran "
                  "du terminal : c'est le moyen le plus sûr, et personne ne le remarque.")

    d.pratique('Écoute', "Combien ça fait ?",
               "Écoutez le montant, puis écrivez-le en chiffres.", [
        ("onze dollars et quarante", "11,40 $"),
        ("six dollars et cinquante", "6,50 $"),
        ("neuf dollars et quinze", "9,15 $"),
        ("quatorze dollars et quatre-vingts", "14,80 $"),
    ], corrige=True,
       notes="Dire chaque montant deux fois, à vitesse normale. Corriger l'écriture : "
             "au Québec, la virgule sépare les cents et le signe de dollar est à droite.")

    d.piege("Attendre sans écouter son numéro",
            "rester assis, dos au comptoir",
            "garder le reçu en main et écouter",
            "Au poste de ramassage, les numéros sont appelés une ou deux fois, dans le "
            "bruit. Un numéro non réclamé reste sur le comptoir et refroidit. Le reçu "
            "en main, tourné vers le comptoir : c'est tout ce qu'il faut.",
            notes="Anecdote utile : demander qui a déjà manqué son numéro. Il y a "
                  "toujours quelqu'un, et ça détend le groupe.")

    d.billet(
        "Écoutez une file et notez trois phrases que vous entendez.",
        exemples=[
            "Dans un casse-croûte, un café ou une cantine.",
            "Notez qui les dit : le préposé ou le client.",
        ],
        notes="Devoir d'observation. Il fait le lien avec la vie réelle et donne du "
              "matériel authentique pour ouvrir le bloc D.")

    return d.save(dossier)
