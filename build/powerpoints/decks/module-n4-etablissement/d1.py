# -*- coding: utf-8 -*-
"""D1 · Lire sa note à voix haute
Bloc D « Défi 3 · La note à remettre » · couleur acier · 75 min.
Source du module : dialogue `t3`, exercices `t3a` et `t3note`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Lire sa note à voix haute",
        chapeau="Un message enregistré s'efface ; une note reste. Le centre "
                "demande donc un papier, cinq ou six lignes, daté et signé. "
                "Nourhane le lit devant monsieur Corriveau — et c'est en le "
                "lisant qu'elle entend ce qui cloche.",
        duree='75 minutes')

    d.titre(notes="Première des deux séances du bloc D. Elle est courte en grammaire et "
                  "longue en lecture à voix haute : c'est le geste qu'on veut installer. "
                  "Faire lire chaque élève, sans exception, même une seule ligne.")

    d.objectifs([
        "connaître les six lignes d'une note d'absence et leur ordre ;",
        "repérer ce qui manque à une note incomplète ;",
        "relire à voix haute pour entendre ses propres fautes ;",
        "savoir pourquoi on garde une copie.",
    ], notes="Le troisième objectif est le seul qui se transmette vraiment : personne "
             "ne relit une note d'absence, et c'est pour cela qu'elles sont mal "
             "écrites.")

    d.dialogue('Dialogue · 1 de 4', "Est-ce que je peux vous la lire ?", [
        ("NOURHANE", "Monsieur Corriveau, voici ma note pour lundi. Est-ce "
                     "que je peux vous la lire ?", True),
        ("FABIEN", "Lisez-la-moi, oui. C'est le meilleur moyen de voir ce "
                   "qui manque.", True),
        ("NOURHANE", "Laval, le 16 septembre. Madame, Monsieur. Je suis "
                     "Nourhane Ouazzani, du groupe 6.", True),
        ("FABIEN", "Bon début. La date et le groupe sont là dès les deux "
                   "premières lignes.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="« Lisez-la-moi » : deux pronoms, deux traits d'union, la grammaire de B2 "
             "en trois mots. La faire remarquer au passage, sans s'y arrêter.")

    d.dialogue('Dialogue · 2 de 4', "Une phrase, un motif", [
        ("NOURHANE", "J'ai été absente le lundi 14 septembre parce que mon "
                     "fils est tombé malade.", True),
        ("FABIEN", "Une phrase, un motif. C'est exactement ce qu'il faut.", True),
        ("NOURHANE", "Je suis allée à la clinique avec lui et je suis "
                     "revenue trop tard pour le cours.", True),
        ("FABIEN", "Attention : vous avez écrit « je suis allé », sans e. "
                   "C'est vous qui êtes allée.", True),
    ], notes="La correction de Fabien annonce D2 au complet. Ne pas l'expliquer "
             "aujourd'hui : la faire seulement remarquer, et dire qu'on y reviendra "
             "demain.")

    d.dialogue('Dialogue · 3 de 4', "Le futur, ici, c'est ce qu'on attend", [
        ("NOURHANE", "Avec être, le participe s'accorde. Je l'oublie chaque "
                     "fois.", True),
        ("FABIEN", "Chaque fois, mais vous vous en souvenez quand vous "
                   "relisez à voix haute. Continuez.", True),
        ("NOURHANE", "Je rattraperai la matière au local 214 et je vous "
                     "remettrai le papier de la clinique.", True),
        ("FABIEN", "Le futur, ici, c'est ce que le centre attend. Vous dites "
                   "ce qui va se passer.", True),
    ], notes="La réplique de Fabien contient la raison d'être du futur dans une note. "
             "L'écrire au tableau : une note qui ne parle que du passé demande à être "
             "excusée, une note qui finit au futur referme le dossier.")

    d.dialogue('Dialogue · 4 de 4', "Il manque une chose, et une seule", [
        ("NOURHANE", "Veuillez agréer mes salutations. Nourhane Ouazzani. Et "
                     "je signe en dessous.", True),
        ("FABIEN", "Il manque une chose, et une seule : à qui la note est "
                   "adressée.", True),
        ("NOURHANE", "Je réécris la ligne du haut et je descends au comptoir "
                     "avant midi.", True),
        ("FABIEN", "Faites-en une copie avant. Une note remise sans copie, "
                   "ça n'a jamais existé.", False),
    ], notes="La dernière réplique est la phrase que les élèves retiennent du module. "
             "La faire répéter. Puis demander qui, dans le groupe, a déjà remis un "
             "papier sans en garder de trace.")

    d.regle("Six lignes, et il faut les six",
            "La date. Le destinataire. Qui vous êtes. Ce qui est arrivé. Ce "
            "que vous ferez. La signature.",
            precision="Une note à laquelle il manque une ligne ne fait pas "
                      "ce qu'elle devrait faire.",
            notes="Diapositive à photographier. Elle sert de grille d'écriture en D2 et "
                  "de grille d'évaluation en E2.")

    d.tableau('Ce qui arrive quand une ligne manque', "Cinq conséquences",
              ['La ligne', 'Ce que la note ne peut plus faire'],
              [["La date", "Prouver quand elle a été écrite et remise."],
               ["Le groupe", "Arriver au bon dossier parmi douze listes."],
               ["Le destinataire", "Se distinguer d'un brouillon."],
               ["La signature", "Être officielle. Sans elle, c'est une feuille."],
               ["La copie", "Vous défendre le jour où le dossier dit le contraire."]],
              cle=1,
              notes="Faire lire les cinq et demander laquelle paraît la moins grave. "
                    "C'est presque toujours la copie — et c'est la seule qui protège "
                    "l'élève plutôt que l'établissement. Le dire.")

    d.cartes("La note de Nourhane", "Les six lignes, dans l'ordre", [
        ("Laval, le 16 septembre 2026.", "La ville et la date."),
        ("Madame, Monsieur,", "Le destinataire."),
        ("Je suis Nourhane Ouazzani, du groupe 6.", "Qui vous êtes."),
        ("J'ai été absente le lundi 14 septembre parce que mon fils est tombé malade.",
         "Ce qui est arrivé, au passé composé."),
        ("Je rattraperai la matière et je vous remettrai le papier.",
         "Ce que vous ferez, au futur."),
        ("Veuillez agréer mes salutations.", "La formule, puis la signature."),
    ], notes="Projeter la note en entier et la faire lire par six élèves, une ligne "
             "chacun. Puis effacer une ligne au hasard et demander laquelle manque : "
             "c'est l'exercice qui reste en mémoire.")

    d.piege("Écrire le motif au présent",
            "Je suis absente parce que mon fils est malade.",
            "J'ai été absente le lundi 14 parce que mon fils est tombé malade.",
            "Une note remise après coup parle du passé. Le présent laisse croire "
            "que vous êtes absente aujourd'hui aussi, et le secrétariat inscrit "
            "alors deux journées au lieu d'une.",
            notes="Ce piège a une conséquence concrète, pas seulement grammaticale. Le "
                  "dire ainsi : ce n'est pas une faute de temps, c'est une journée "
                  "d'absence de plus au dossier.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Nourhane lit sa note à voix haute devant son enseignant.", "vrai"),
        ("Sa note commence par la date et le nom de la ville.", "vrai"),
        ("Monsieur Corriveau trouve le motif trop court.", "faux — c'est ce qu'il faut"),
        ("Elle avait écrit « je suis allé » sans e.", "vrai"),
        ("Il manquait la signature.", "faux — le destinataire"),
        ("Il lui conseille de faire une copie.", "vrai"),
    ], corrige=True,
       notes="La cinquième demande d'écouter jusqu'au bout : la signature est bien là, "
             "c'est la ligne du haut qui manque. Faire réécouter la quatrième partie du "
             "dialogue avant de trancher.")

    d.billet(
        "Reprenez votre phrase de C4 et écrivez au-dessus les trois lignes "
        "qui manquent : la date, le destinataire, votre nom et votre groupe.",
        exemples=[
            "La ville et la date en toutes lettres.",
            "Madame, Monsieur — cela suffit comme destinataire.",
        ],
        notes="Ramasser : c'est le brouillon de la note de D2, qui deviendra la "
              "production écrite de E2. Trois séances pour un même texte, à chaque fois "
              "plus complet.")

    return d.save(dossier)
