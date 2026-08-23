# -*- coding: utf-8 -*-
"""C3 · Lire une fiche de droits sans la lire en entier
Bloc C « Défi 2 · La réclamation au comptoir » · couleur ambre · compréhension
écrite · 75 min.
Source : exercice `t2contrat` (type `texte`, treize passages cliquables) et sa
mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Lire une fiche de droits sans la lire en entier",
        chapeau="On n'arrive pas devant une fiche officielle : on arrive "
                "avec une question. Le titre en majuscules est l'index, et "
                "la phrase à retenir porte presque toujours un nombre.",
        duree='75 minutes')

    d.titre(notes="Séance de lecture. Le document est long et la méthode est courte : "
                  "trois gestes. Le montrer au tableau une fois, puis laisser chacun "
                  "travailler sur l'exercice du module, qui met les questions à côté "
                  "du texte.")

    d.objectifs([
        "formuler sa question avant d'ouvrir un document ;",
        "repérer le paragraphe par son titre en majuscules ;",
        "reconnaître six formules du vocabulaire juridique ;",
        "citer la phrase qui répond, plutôt que de la résumer.",
    ], notes="Cette compétence est une attente de fin de cours du niveau 7. Elle sert "
             "pour un bail, une police d'assurance, un formulaire : le dire, sinon le "
             "groupe croit qu'on travaille l'automobile.")

    d.declencheur(
        'Mise en situation', "Que faites-vous devant un document officiel de quatre pages ?",
        pistes=[
            "Le lisez-vous du début à la fin ?",
            "Le rangez-vous pour plus tard ?",
            "Demandez-vous à quelqu'un de le lire pour vous ?",
            "Qu'est-ce qui vous ferait le lire en deux minutes ?",
        ],
        notes="La dernière question amène la méthode d'elle-même : ce qui fait lire un "
              "document, c'est une question précise. Sans question, on ne lit pas, on "
              "parcourt.")

    d.tableau('Analyse', "Trois gestes, dans cet ordre",
              ['Le geste', 'Comment'],
              [["Écrire sa question", "une phrase, avant d'ouvrir"],
               ["Parcourir les titres", "ils annoncent la question traitée"],
               ["Lire un paragraphe", "celui-là seulement, en entier"],
               ["Repérer le nombre", "c'est presque toujours la réponse"],
               ["Citer, pas résumer", "la phrase exacte servira dans la lettre"]],
              cle=0,
              notes="Diapositive à photographier. Le cinquième geste est celui qui "
                    "distingue le niveau 7 des niveaux inférieurs : on cite pour "
                    "réutiliser, pas pour comprendre.")

    d.tableau('Analyse', "Six formules à reconnaître",
              ['La formule', 'Ce qu\'elle veut dire'],
              [["à titre onéreux", "contre de l'argent"],
               ["est réputé", "la loi le considère comme acquis"],
               ["à compter de", "à partir de : la formule du délai"],
               ["à défaut", "si cela n'est pas fait"],
               ["au préalable", "avant"],
               ["compte tenu de", "en tenant compte de, en pesant"]],
              cle=0,
              notes="Diapositive à photographier. « Est réputé » est la plus utile : "
                    "quand la loi le dit, on n'a pas à démontrer l'intention. C'est en "
                    "faveur du consommateur.")

    d.regle("« Compte tenu du prix payé » n'est pas une échappatoire",
            "C'est un argument : plus vous avez payé, plus la durée attendue est longue.",
            precision="La formule paraît vague et ne l'est pas. Elle nomme les éléments "
                      "qui servent à juger : le prix, le contrat, les conditions "
                      "d'utilisation. Dans une lettre, la façon la plus efficace de "
                      "s'en servir tient en une phrase : « onze mille quatre cents "
                      "dollars pour vingt-quatre jours de service ». Le prix et la "
                      "durée côte à côte, et le lecteur conclut lui-même.",
            notes="Diapositive à photographier. Faire fabriquer trois phrases de ce "
                  "modèle par le groupe, avec des biens de leur choix. Une minute "
                  "chacune, et l'effet est net.")

    d.pratique('Compréhension', "Cherchez la réponse dans la fiche",
               "Donnez le titre du paragraphe, puis le nombre qu'il contient.", [
        ("Combien de temps suis-je couvert en catégorie C ?", "DURÉES : un mois ou 1 700 km"),
        ("Puis-je annuler la garantie que j'ai payée ?", "ANNULER : dix jours, par avis écrit"),
        ("Quel délai accorde une mise en demeure ?", "SI LE COMMERÇANT REFUSE : dix jours"),
        ("Jusqu'à quel montant aux petites créances ?", "SI RIEN NE BOUGE : 15 000 $ ou moins"),
        ("Que devient la garantie pendant la réparation ?", "IMMOBILISATION : elle se prolonge d'autant"),
        ("Que doit faire le commerçant avant de vendre ?", "AVANT DE VENDRE : informer, verbalement et par écrit"),
    ], corrige=True,
       notes="Treize questions dans le module ; en projeter six. Chronométrer : deux "
             "minutes pour les six, ce qui est faisable avec la méthode et impossible "
             "sans elle. C'est la démonstration.")

    d.piege('Piège', "prendre « généralement » pour une obligation",
            "le lire comme un usage, pas comme une règle",
            "« Un délai raisonnable, généralement de dix jours » : dix jours est ce "
            "qui se fait, pas ce qui est imposé. Quinze jours reste raisonnable ; deux "
            "ne le sont pas. Le mot « généralement » se lit, il ne se saute pas.",
            notes="Faire chercher dans la fiche un autre mot du même genre — "
                  "« notamment », « le cas échéant ». Ils marquent tous une souplesse "
                  "qu'un lecteur pressé prend pour une règle.")

    d.pratique('Compréhension', "Traduisez en langue de tous les jours",
               "Une phrase par formule.", [
        ("à titre onéreux", "contre de l'argent, pas gratuitement"),
        ("est réputé passer sous silence un fait important", "la loi le considère comme s'il avait caché quelque chose"),
        ("à compter de la réception de la présente", "à partir du jour où vous recevrez cette lettre"),
        ("selon la première limite atteinte", "celle des deux qui arrive en premier arrête tout"),
    ], corrige=True,
       notes="Faire écrire les quatre traductions dans le cahier. Elles resservent "
             "telles quelles en D2, quand la lettre s'écrit.")

    d.billet(
        "Écris la question que tu poserais à l'Office si tu avais un bien brisé.",
        exemples=[
            "Une phrase, la plus précise possible.",
            "C'est cette question-là qui te fera trouver le bon paragraphe.",
        ],
        notes="Trois minutes. Ramasser : les questions trop larges — « qu'est-ce que "
              "j'ai le droit de faire ? » — montrent qui n'a pas encore la méthode.")

    return d.save(dossier)
