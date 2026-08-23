# -*- coding: utf-8 -*-
"""A1 · La signature du lundi
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `prVF` et son bandeau de six mots.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="La signature du lundi",
        chapeau="Onze mille quatre cents dollars, une garantie qu'on n'a pas "
                "demandée, et un contrat de cinq ans. Tout le module part "
                "de ce bureau vitré.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : qui "
                  "a déjà signé un contrat sans avoir lu la page du milieu ? Presque "
                  "tout le monde. C'est exactement le sujet du bloc, et il n'y a "
                  "aucune honte à le dire.")

    d.objectifs([
        "repérer dans un contrat de crédit le taux, les frais et le total ;",
        "comprendre ce qu'une garantie prolongée ajoute au montant financé ;",
        "savoir qu'une étiquette obligatoire accompagne toute auto d'occasion ;",
        "employer six mots du contrat avec leur article.",
    ], notes="Le troisième objectif est celui que personne ne connaît. Le poser dès la "
             "première séance : l'étiquette est le document le plus utile du terrain "
             "et le moins lu.")

    d.declencheur(
        'Observation', "As-tu déjà acheté quelque chose à crédit, et savais-tu combien ça coûtait en tout ?",
        pistes=[
            "Te souviens-tu du montant du versement mensuel ?",
            "Te souviens-tu du total, une fois tous les versements faits ?",
            "T'a-t-on proposé une garantie en plus ? L'as-tu prise ?",
            "As-tu relu le contrat après l'avoir signé ?",
        ],
        notes="Question sans mauvaise réponse. Presque tout le monde se souvient du "
              "versement mensuel et personne du total : c'est justement le point de la "
              "séance. Ne pas corriger tout de suite.")

    d.dialogue('Dialogue · 1 de 3', "Le chiffre qui ne concorde pas", [
        ("JEAN-ROCK", "Madame Kabuya ! Entrez, entrez. Elle est prête, la grise. Lavée, le plein fait.", True),
        ("ERNESTINE", "Merci. J'ai apporté le chèque de l'acompte, comme vous m'aviez dit. Deux mille.", True),
        ("ERNESTINE", "Le prix, c'est onze mille quatre cents, ça je l'ai vu sur le papier collé dans la vitre.", True),
        ("ERNESTINE", "Et là, en bas, il y a écrit dix mille six cents. D'où vient la différence ?", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Onze mille quatre cents, deux mille, neuf mille quatre cents, dix mille "
             "six cents : écrire les quatre nombres au tableau et les y laisser toute "
             "la séance. Ils reviennent dans les quatre blocs.")

    d.dialogue('Dialogue · 2 de 3', "Une garantie qu'on n'a pas demandée", [
        ("JEAN-ROCK", "Ah, ça, c'est la garantie prolongée. Douze cents. Je vous l'ai mise dedans, c'est plus simple.", True),
        ("ERNESTINE", "Je ne l'ai pas demandée, cette garantie.", True),
        ("ERNESTINE", "Et l'auto, elle n'a pas déjà une garantie ?", True),
        ("JEAN-ROCK", "Le fabricant, c'est fini depuis longtemps. Elle est de 2019.", True),
    ], notes="Faire remarquer que le vendeur répond à côté : la cliente ne parlait pas "
             "du fabricant. Cette réponse-là est le cœur du défi 2, et elle passe "
             "inaperçue à la première écoute. Y revenir.")

    d.dialogue('Dialogue · 3 de 3', "Les trois cases qui comptent", [
        ("JEAN-ROCK", "Neuf virgule quarante-cinq pour cent. Soixante versements de deux cent vingt-deux et trente-six.", True),
        ("ERNESTINE", "Ça fait combien, en tout ?", True),
        ("JEAN-ROCK", "L'obligation totale ? Treize mille trois cent quarante et un et soixante.", True),
        ("ERNESTINE", "Donc les frais de crédit, c'est deux mille sept cent quarante et un dollars.", True),
    ], notes="Refaire la soustraction au tableau : 13 341,60 moins 10 600 égale "
             "2 741,60. Le groupe voit alors ce que le versement mensuel cachait, et "
             "c'est le moment le plus utile de la séance.")

    d.tableau('Analyse', "Les trois cases d'un contrat de crédit",
              ['La case', 'Ce qu\'elle dit'],
              [["Le taux de crédit", "un pourcentage annuel, fixe pour toute la durée"],
               ["Les frais de crédit", "en dollars, ce que le crédit coûte"],
               ["L'obligation totale", "le montant financé plus les frais : le vrai total"],
               ["Le versement", "il ne dit rien : on le baisse en allongeant"],
               ["Le contrat accessoire", "ce qui a été ajouté au capital, s'il y en a"]],
              cle=0,
              notes="Diapositive à photographier. C'est le tableau de référence du "
                    "bloc A et il revient en A4, sous forme d'exercice sur le document "
                    "lui-même.")

    d.regle("Le versement mensuel ne dit rien",
            "Deux offres au même versement peuvent différer de trois mille dollars à l'obligation totale.",
            precision="Allonger un contrat de cinq à sept ans fait baisser le "
                      "versement et monter le total. C'est pour cela que la loi oblige "
                      "à inscrire l'obligation totale dans une case : c'est la seule "
                      "qui permette de comparer deux offres. Et ce qu'on ajoute au "
                      "capital — une garantie, par exemple — porte des frais de crédit "
                      "pendant toute la durée du contrat.",
            notes="Diapositive à photographier. Poser la question au groupe avant de "
                  "montrer la précision : pourquoi un vendeur préfère-t-il parler du "
                  "versement ? La réponse vient toute seule.")

    d.vocabulaire('Vocabulaire', "Six mots du contrat signé", [
        ("une étiquette", "Le document obligatoire apposé sur une auto d'occasion offerte par un commerçant."),
        ("l'odomètre", "Le compteur qui affiche le nombre total de kilomètres parcourus."),
        ("les frais de crédit", "Ce qu'on paie en plus du prix pour avoir le droit de payer plus tard."),
        ("l'obligation totale", "La somme complète qu'un acheteur à crédit s'engage à verser."),
        ("le taux de crédit", "Le pourcentage annuel qui exprime les frais de crédit."),
        ("une garantie prolongée", "Une protection payante proposée en plus, avec ses exclusions."),
    ], notes="Faire répéter chaque mot avec son article. « L'obligation totale » et "
             "« le taux de crédit » prennent le défini : il n'y en a qu'un par contrat. "
             "Le faire remarquer.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la conversation d'Ernestine et de monsieur Vachon.", [
        ("Le prix de vente de l'auto est de 11 400 $.", "vrai"),
        ("Ernestine a demandé elle-même la garantie prolongée.", "faux - le vendeur l'a mise dans le contrat"),
        ("La garantie prolongée s'ajoute au montant financé.", "vrai"),
        ("Le vendeur explique qu'une garantie existe déjà dans la loi.", "faux - il répond que le fabricant est expiré"),
        ("L'obligation totale est de 10 600 $.", "faux - 13 341,60 $ ; 10 600 $ est le montant financé"),
        ("Les frais de crédit s'élèvent à 2 741,60 $.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le quatrième "
             "prend deux minutes : le vendeur ne ment pas, il répond à une autre "
             "question. C'est la nuance à installer.")

    d.billet(
        "Quel chiffre regarderais-tu en premier, la prochaine fois qu'on te propose un contrat de crédit ?",
        exemples=[
            "Une phrase suffit.",
            "Dis aussi pourquoi celui-là et pas un autre.",
        ],
        notes="Deux minutes. Les réponses servent en A4 : elles montrent qui a compris "
              "que l'obligation totale est la seule case comparable.")

    return d.save(dossier)
