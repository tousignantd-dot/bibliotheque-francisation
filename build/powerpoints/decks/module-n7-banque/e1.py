# -*- coding: utf-8 -*-
"""E1 · S'informer, puis décider à voix haute
Bloc E « Je me lance » · couleur teal · 90 min.
Source : jeu de rôle `produitfinancier` et production orale de « Je me lance ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="S'informer, puis décider à voix haute",
        chapeau="Deux tâches orales : poser ses questions à un conseiller "
                "sans rien signer, puis exposer deux produits et trancher en "
                "quatre-vingt-dix secondes.",
        duree='90 minutes')

    d.titre(notes="Avant-dernière séance. Rendre les billets de B1 et de C4 : ils "
                  "contiennent déjà le choix et la phrase de conclusion de chacun.")

    d.objectifs([
        "conduire un entretien d'information sans hocher la tête ;",
        "reprendre un mot non compris et faire répéter un chiffre ;",
        "exposer deux produits avec deux avantages et deux inconvénients ;",
        "trancher, et dire à quelle condition on changerait d'avis.",
    ], notes="Le quatrième objectif vient des attentes de fin de cours du niveau 7 : "
             "« il expose les avantages et les inconvénients de deux situations pour "
             "prendre une décision ».")

    d.declencheur(
        'Préparation', "Qu'est-ce qui fait qu'un rendez-vous a servi à quelque chose ?",
        pistes=[
            "Repartir avec un produit, ou avec une réponse ?",
            "Combien de questions as-tu posées la dernière fois ?",
            "Qu'est-ce que tu aurais aimé demander ?",
            "Qu'est-ce que tu ne signerais plus sur place ?",
        ],
        notes="Trois minutes, pas plus. La séance est une séance de production : le "
              "déclencheur sert à mettre en bouche, pas à discuter.")

    d.tableau('Jeu de rôle', "Ce qu'il faut couvrir",
              ['Le moment', 'Ce que je fais'],
              [["l'ouverture", 'je dis ce que je veux savoir'],
               ['le taux', 'je demande fixe ou variable'],
               ['un mot difficile', 'je le reprends entre guillemets'],
               ['un chiffre', 'je le redis pour vérifier'],
               ['la fin', "je demande un écrit, je ne signe pas"]],
              cle=0,
              notes="Diapositive à laisser affichée pendant le jeu de rôle. Les élèves "
                    "cochent au fur et à mesure.")

    d.cartes('Trois dossiers', "Choisissez le vôtre", [
        ('La dette de carte', "9 412 $ à 19,90 %. Marge à 9,45 % ou prêt à 11,20 % en 80 versements."),
        ("Les 6 200 $", "Un cégep dans deux ans. Compte, dépôt à terme, CELI ou REER."),
        ("L'opération de 780 $", "Un achat inconnu le 14, et la carte est restée dans le portefeuille."),
    ], notes="Chacun choisit un dossier et le garde pour les deux tâches. Le troisième "
             "est le plus facile à jouer et le plus difficile à conclure.")

    d.regle("Le conseiller n'explique que ce qu'on lui demande",
            "C'est la règle du jeu, et c'est aussi la réalité.",
            precision="L'assistant ne cache rien, mais il ne devine pas ce qui vous a "
                      "échappé. Un entretien réussi n'est pas celui où l'on a tout "
                      "compris du premier coup : c'est celui où l'on a fait répéter "
                      "trois fois sans gêne.",
            notes="Diapositive à photographier. Le dire avant de lancer les tablettes : "
                  "ça change complètement la façon dont les élèves jouent.")

    d.tableau('Production orale', "Trois temps, quatre-vingt-dix secondes",
              ['Le temps', 'Ce que je dis'],
              [['temps 1', "j'annonce les deux produits"],
               ['temps 2', 'deux avantages, deux inconvénients, des chiffres'],
               ['temps 3', 'je compare, je tranche, je date']],
              cle=0,
              note="La phrase de conclusion s'écrit en premier, et le reste s'organise autour.",
              notes="Diapositive à photographier. C'est le plan que l'IA de correction "
                    "attend, et il est écrit dans la consigne du module.")

    d.cartes('Modèles', "Des phrases pour chaque temps", [
        ('Temps 1', "J'ai deux possibilités : une marge à 9,45 % ou un prêt à 11,20 %."),
        ('Temps 2', "La marge coûte moins cher ; en revanche, rien ne m'oblige à finir."),
        ('Temps 2', "Le prêt est plus cher, mais il se termine au quatre-vingtième versement."),
        ('Temps 3', "C'est d'autant plus difficile que les deux se défendent."),
        ('Temps 3', "Je prends le prêt, parce que je n'ai jamais remboursé une marge."),
        ('Temps 3', "Je reverrai la question le jour où la carte sera à zéro."),
    ], notes="Faire répéter les six phrases avant l'enregistrement. Elles reprennent "
             "exactement les connecteurs de C4 et les comparaisons de B4.")

    d.pratique('Autoévaluation', "Avant d'envoyer, vérifiez",
               "Réécoutez-vous une fois et cochez.", [
        ("J'ai nommé les deux produits.", "temps 1"),
        ("J'ai donné deux avantages et deux inconvénients.", "temps 2"),
        ("Chaque avantage porte un chiffre.", "temps 2"),
        ("J'ai employé au moins deux connecteurs.", "temps 2"),
        ("J'ai tranché en disant lequel je prends.", "temps 3"),
        ("J'ai dit à quelle condition je changerais d'avis.", "temps 3"),
    ], corrige=False,
       notes="Faire réécouter avant d'envoyer. Les élèves qui s'écoutent une fois "
             "réenregistrent presque toujours, et le second essai est meilleur.")

    d.billet("Note ce que tu ferais autrement au prochain enregistrement.",
             exemples=["Je parlerais moins vite sur les chiffres.",
                       "J'ajouterais une phrase de conclusion."],
             notes="Deux minutes. Ramasser : ces billets préparent la relecture de la "
                   "lettre en E2.")

    return d.save(dossier)
