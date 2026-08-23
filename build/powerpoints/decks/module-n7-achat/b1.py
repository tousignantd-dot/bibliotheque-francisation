# -*- coding: utf-8 -*-
"""B1 · Ce que le bruit veut dire
Bloc B « Défi 1 · Le bruit qu'il faut décrire » · couleur acier ·
compréhension orale · 75 min.
Source : dialogue `t1` et exercice `t1vf` avec son bandeau de cinq mots.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Ce que le bruit veut dire",
        chapeau="Au comptoir d'un garage, un conseiller pose trois questions "
                "dans le même ordre à tout le monde. Y répondre précisément "
                "vaut deux heures de recherche en moins.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Annoncer d'entrée que ce bloc n'est pas de la "
                  "mécanique : c'est de la langue. Aucun élève n'aura à réparer quoi "
                  "que ce soit, tous auront à décrire quelque chose.")

    d.objectifs([
        "comprendre les trois questions d'un conseiller au service ;",
        "nommer un bruit avec un mot précis ou une comparaison ;",
        "dire quand un symptôme apparaît et à quelle fréquence ;",
        "employer cinq mots pour nommer une panne.",
    ], notes="La même compétence sert pour une laveuse, un four, un chauffe-eau. Le "
             "dire dès le début : personne ne quittera ce bloc en n'ayant appris que "
             "des mots d'automobile.")

    d.declencheur(
        'Mise en situation', "Comment décririez-vous un bruit que fait un appareil chez vous ?",
        pistes=[
            "Quel mot emploieriez-vous : sifflement, grincement, cognement ?",
            "Le bruit revient-il toujours, ou seulement dans certains cas ?",
            "À quel moment précis se produit-il ?",
            "L'avez-vous déjà expliqué à quelqu'un ? Vous a-t-on compris ?",
        ],
        notes="Beaucoup diront « ça fait un drôle de bruit ». Ne pas corriger : le "
              "dialogue va le faire, et le conseiller le fait mieux qu'un enseignant.")

    d.dialogue('Dialogue · 1 de 3', "Un bruit, ça ne suffit pas", [
        ("ERNESTINE", "Bonjour. Je viens pour mon auto. Elle fait un bruit.", True),
        ("WILFRID", "Un bruit. Bon. On va être plus précis que ça, sinon je vais chercher deux heures pour rien.", True),
        ("WILFRID", "Premièrement : quel genre de bruit ? Un sifflement, un grincement, un cognement, un cliquetis ?", True),
        ("ERNESTINE", "Un cognement. Comme si quelqu'un frappait une fois sous le plancher, du côté droit.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="La réponse d'Ernestine contient déjà deux choses : le mot précis et une "
             "comparaison. Le faire remarquer. Une comparaison juste vaut mieux qu'un "
             "mot technique employé de travers.")

    d.dialogue('Dialogue · 2 de 3', "Quand, exactement ?", [
        ("WILFRID", "Deuxièmement : quand ?", True),
        ("ERNESTINE", "Le matin, surtout. Quand l'auto a passé la nuit dehors.", True),
        ("WILFRID", "À froid, donc. Et après dix minutes de route, il est encore là ?", True),
        ("ERNESTINE", "Non. Après, il s'en va. Le soir en revenant, je ne l'entends presque jamais.", True),
    ], notes="Le conseiller traduit « le matin, quand l'auto a passé la nuit dehors » "
             "en « à froid ». C'est du vocabulaire technique offert gratuitement : le "
             "relever et l'écrire au tableau.")

    d.dialogue('Dialogue · 3 de 3', "Chaque fois, ou souvent ?", [
        ("WILFRID", "Troisièmement : à quel moment exactement ? En partant, en freinant, en montant une côte ?", True),
        ("ERNESTINE", "Quand ça change de vitesse. Au coin de la rue Notre-Dame, il y a une petite montée : c'est là que ça cogne.", True),
        ("WILFRID", "Chaque fois, ou souvent ?", True),
        ("ERNESTINE", "Chaque fois, le matin. Systématiquement.", True),
    ], notes="La dernière réplique ouvre B3. « Systématiquement » est le mot le plus "
             "utile du bloc, et un élève de niveau 7 doit pouvoir le dire sans "
             "hésiter. Le faire répéter par trois personnes.")

    d.tableau('Analyse', "Trois questions, trois coordonnées",
              ['La question', 'Ce qu\'elle cherche'],
              [["Quel genre de bruit ?", "le symptôme, nommé ou comparé"],
               ["Quand ?", "à froid, à chaud, à quelle vitesse"],
               ["À quel moment exactement ?", "la manœuvre : freiner, monter, changer"],
               ["Chaque fois ?", "la fréquence, chiffrée si possible"],
               ["Depuis quand ?", "la date, et ce qui a changé avant"]],
              cle=0,
              notes="Diapositive à photographier. C'est le tableau de référence du bloc "
                    "B, et il revient tel quel en B2 sous forme d'exercice.")

    d.vocabulaire('Vocabulaire', "Cinq mots pour nommer une panne", [
        ("un cognement", "Un bruit sourd et bref, comme un coup frappé une seule fois."),
        ("la transmission", "La partie mécanique qui transmet la force du moteur aux roues."),
        ("une fuite", "Un liquide qui s'écoule là où il ne devrait pas."),
        ("un diagnostic", "Le résultat de l'examen par lequel un spécialiste trouve la cause."),
        ("un témoin lumineux", "La petite lampe du tableau de bord qui signale un problème."),
    ], notes="Ajouter la couleur des liquides : rouge pour la transmission, vert ou "
             "orangé pour le refroidissement, noir pour l'huile. Une flaque est une "
             "information, pas une saleté.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la conversation au comptoir du garage.", [
        ("Le conseiller pose trois questions dans un ordre précis.", "vrai"),
        ("Le cognement se fait entendre surtout le soir.", "faux - le matin, à froid"),
        ("Le bruit revient au moment où l'auto change de vitesse.", "vrai"),
        ("La flaque rouge est apparue avant que le bruit commence.", "faux - le bruit avait commencé trois jours avant"),
        ("Une description précise fait gagner du temps de recherche.", "vrai"),
        ("Le conseiller conseille de faire réparer tout de suite chez lui.", "faux - il renvoie d'abord au vendeur"),
    ], corrige=True,
       notes="Le sixième item ouvre tout le bloc C. Le souligner : un garagiste "
             "honnête renvoie chez le vendeur quand la garantie peut courir encore.")

    d.billet(
        "Décris en une phrase un bruit ou un problème que tu as déjà eu avec un appareil.",
        exemples=[
            "Un symptôme, un moment, une fréquence.",
            "Pas de mot technique : dis ce que tu entends.",
        ],
        notes="Trois minutes. Ramasser : les billets sans coordonnée servent d'exemples "
              "anonymes en B2, et ils font mieux comprendre l'exercice que n'importe "
              "quelle consigne.")

    return d.save(dossier)
