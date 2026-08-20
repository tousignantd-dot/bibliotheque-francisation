# -*- coding: utf-8 -*-
"""B1 · Quelle ligne, quelle direction ?
Bloc B « Défi 1 · Demander son chemin » · couleur acier · 75 min.
Source : dialogue `t1`, exercices `t1vf` et `t1quai`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Quelle ligne, quelle direction ?',
        chapeau="Nour doit aller à l'hôpital Charles-Le Moyne. Une ligne de "
                "métro, un terminus, un autobus, trois arrêts. Le plus "
                "difficile n'est pas le chemin : c'est de choisir le bon quai.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc B. Si possible, apporter un plan de réseau papier — "
                  "les sociétés de transport en distribuent gratuitement.")

    d.objectifs([
        "demander comment se rendre quelque part en transport en commun ;",
        "comprendre une réponse en plusieurs étapes ;",
        "choisir le bon quai en lisant le nom du terminus ;",
        "demander combien de temps dure le trajet.",
    ])

    d.declencheur(
        'Mise en situation', "Vous devez aller à l'hôpital, à l'autre bout de la ville. Par où commencez-vous ?",
        pistes=[
            "À qui demandez-vous : un passant, un employé, une application ?",
            "Quelle est la première question à poser ?",
            "Comment savez-vous si vous montez du bon côté ?",
            "Combien de temps prévoyez-vous d'avance ?",
        ],
        notes="Cinq minutes. Plusieurs élèves utilisent déjà une application : très bien. "
              "Faire remarquer qu'elle ne dit pas quel quai prendre dans une station.")

    d.dialogue('Dialogue · 1 de 3', "La ligne et le terminus", [
        ("NOUR", "Bonjour. Je dois aller à l'hôpital Charles-Le Moyne. Est-ce que je peux y aller en métro ?", True),
        ("GILLES", "En métro puis en autobus. Prenez la ligne jaune jusqu'à Longueuil, c'est le terminus.", True),
        ("NOUR", "La ligne jaune. Et je monte de quel côté ?", False),
        ("GILLES", "Du côté « direction Longueuil ». Faites attention : l'autre quai va vers Berri, dans le sens contraire.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Trois répliques teintées : la question complète, la réponse en deux moyens, "
             "et l'avertissement sur le quai. C'est le cœur du bloc.")

    d.dialogue('Dialogue · 2 de 3', "Comment savoir", [
        ("NOUR", "Comment je sais que c'est le bon quai ?", True),
        ("GILLES", "Regardez le panneau au-dessus de l'escalier. Le nom du terminus est toujours écrit dessus.", True),
        ("NOUR", "D'accord. Et après Longueuil ?", False),
        ("GILLES", "Sortez du métro, montez au terminus d'autobus. Prenez celui qui va vers Gaétan-Boucher.", True),
    ], notes="La règle d'or du module est dans la deuxième réplique. L'écrire au tableau et "
             "l'y laisser jusqu'à la fin : « le nom du terminus donne la direction ».")

    d.dialogue('Dialogue · 3 de 3', "Combien de temps", [
        ("NOUR", "Celui qui va vers Gaétan-Boucher. Il passe souvent ?", False),
        ("GILLES", "Aux quinze minutes. Descendez au troisième arrêt, l'hôpital est juste en face.", True),
        ("NOUR", "Ça prend combien de temps en tout ?", True),
        ("GILLES", "Comptez quarante minutes, une heure si vous manquez l'autobus. Partez d'avance.", False),
    ], notes="« Aux quinze minutes » est une fréquence, pas une heure de départ. "
             "L'expliquer : c'est une source de malentendu constante.")

    d.tableau('Analyse', "Les quatre questions à poser",
              ['La question', 'Ce qu\'on apprend'],
              [["Quelle ligne ?", "le numéro ou la couleur"],
               ["Quelle direction ?", "le nom du terminus"],
               ["Où je descends ?", "l'arrêt ou la station"],
               ["Ça prend combien de temps ?", "quand partir de chez soi"]],
              cle=1,
              note="La deuxième est celle qu'on oublie — et c'est la seule qui empêche de "
                   "partir dans le mauvais sens.",
              notes="Faire recopier. Ces quatre questions sont la liste de vérification du "
                    "module.")

    d.regle("La règle d'or",
            "Le nom du terminus donne la direction. Lisez-le en premier.",
            precision="Sur un quai, sur un autobus, sur un panneau : c'est toujours le nom "
                      "du terminus qu'il faut lire avant tout le reste. Le numéro de la "
                      "ligne ne suffit pas — le même numéro circule dans les deux sens.",
            notes="C'est la diapo à photographier du bloc B. La faire répéter par deux "
                  "élèves différents.")

    d.piege('Se fier au numéro seul',
            "Je prends le 45, c'est le bon numéro.",
            "Je prends le 45 direction Saint-Hubert.",
            "L'autobus 45 existe dans les deux directions, avec exactement le même numéro. "
            "Monter dans le bon numéro du mauvais côté de la rue est l'erreur la plus "
            "fréquente — et la plus longue à réparer.",
            notes="Cette erreur revient au dialogue de C4, où Nour la commet vraiment. "
                  "L'annoncer.")

    d.pratique('Pratique', "Bon quai ou mauvais quai ?",
               "Nour veut aller à Longueuil. Cet indice l'envoie-t-il du bon côté ?", [
        ("Le panneau dit « direction Longueuil ».", "bon quai"),
        ("Le panneau dit « direction Berri-UQAM ».", "mauvais quai"),
        ("Le nom du terminus écrit sur le train est Longueuil.", "bon quai"),
        ("Elle suit la foule sans rien vérifier.", "mauvais quai"),
        ("Elle a demandé au préposé, qui a confirmé.", "bon quai"),
        ("Le panneau montre une flèche, sans nom de terminus.", "mauvais quai — l'information manque"),
    ], corrige=True,
       notes="La dernière ligne mérite discussion : une flèche sans nom n'est pas une "
             "erreur, c'est une information incomplète. Il faut chercher ailleurs.")

    d.billet(
        "Décrivez le trajet entre chez vous et l'école : ligne, direction, arrêt, durée.",
        exemples=[
            "Employez les quatre questions du tableau.",
            "Si vous venez à pied, décrivez le trajet en repères de rue.",
        ],
        notes="Ramasser. Ces trajets réels serviront à la production orale de E1.")

    return d.save(dossier)
