# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 60 min. Dernière séance du module.
Source : dialogue `appli`, jeu de rôle `bonjour`, productions orale et écrite.

Séance de production. Tout ce que le module a montré revient ici, et rien de
neuf n'y est introduit — sauf une situation, la porte de la voisine le jour
de sa fête, où l'élève doit pour la première fois donner quelque chose et
refuser poliment autre chose.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-bonjour/images/')


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Je me lance",
        chapeau="Saluer un voisin et parler de sa journée à voix haute, puis "
                "écrire une carte de vœux.",
        duree='60 minutes')

    d.titre(notes="Dernière séance. Prévoir que la moitié du temps se passe en production "
                  "réelle : jeu de rôle, enregistrement, écriture. Les diapositives ne "
                  "sont qu'un cadre.")

    d.objectifs([
        "tenir un échange complet avec un voisin ;",
        "dire trois choses de sa journée ;",
        "s'enregistrer et s'écouter ;",
        "écrire une carte de vœux de trois lignes.",
    ])

    d.declencheur(
        'Observation', "Que se passe-t-il à cette porte ?",
        image=IMG + 'carte-table.jpg',
        pistes=[
            "Qu'est-ce qu'on apporte ?",
            "Que dit-on en donnant une carte ?",
            "Et si on nous invite à entrer, mais qu'on doit partir ?",
            "Comment refuser sans être impoli ?",
        ],
        notes="La dernière question est celle qui inquiète le plus : donner tout de suite "
              "la phrase « merci, mais je travaille à six heures », et faire remarquer "
              "que le « merci » suffit à rendre le refus poli.")

    d.dialogue('Dialogue', "Bonne fête, madame Roy !", [
        ("NADIA", "Bonjour, madame Roy. C'est pour vous.", True),
        ("GILBERTE", "Une carte ! Merci, Nadia.", True),
        ("NADIA", "Bonne fête ! Bonne santé !", True),
        ("GILBERTE", "Tu écris très bien. Entre, je fais du thé.", True),
        ("NADIA", "Merci, mais je travaille à six heures.", True),
        ("GILBERTE", "Alors bonne soirée. Et merci pour la carte.", True),
    ], consigne="Écoutez, puis comptez ce que Nadia a réussi à faire.",
       notes="Quatre choses en six répliques : elle salue, elle donne, elle souhaite "
             "deux fois, elle refuse poliment. Faire compter par le groupe.")

    d.tableau('Analyse', "Ce qui revient de tout le module",
              ['Ce qu\'on dit', 'Vu en'],
              [["Bonjour, madame Roy.", "A1 — saluer une personne qu'on croise"],
               ["Bonne fête ! Bonne santé !", "C2 — bon ou bonne"],
               ["Merci, mais je travaille à six heures.", "B2 — dire ce qu'on fait"],
               ["Alors bonne soirée.", "A3 — la formule du départ"]],
              cle=2,
              note="Rien de neuf dans cette colonne : le module entier tient dans ces "
                   "quatre lignes.",
              notes="Diapositive à photographier. Elle sert de révision de tout le module "
                    "en une seule page.")

    d.regle("Refuser poliment",
            "Un merci, puis la raison. Rien d'autre.",
            precision="« <b>Merci</b>, mais je travaille à six heures. » On remercie "
                      "d'abord, on dit la raison ensuite, en une phrase courte au "
                      "présent. On ne s'excuse pas longuement : ça met l'autre mal à "
                      "l'aise.",
            notes="Diapositive à photographier. Faire dire la phrase par chaque élève, "
                  "avec sa propre raison : « je travaille », « je vais chercher mon "
                  "fils », « j'ai mon cours ».")

    d.cartes("Trois situations pour le jeu de rôle", "Choisissez la vôtre", [
        ("Dans l'entrée, le matin",
         "Vous partez au centre. Votre voisine descend en même temps que vous."),
        ("Devant l'ascenseur",
         "Votre voisine a les mains pleines de sacs. Elle vous demande quelque chose."),
        ("Le jour de sa fête",
         "C'est la fête de votre voisine. Vous frappez à sa porte avec une carte."),
    ], cols=3, notes="Ce sont les trois situations du jeu de rôle en ligne. L'élève y joue "
                     "avec l'assistant, qui parle lentement et ne dit jamais plus de deux "
                     "ou trois phrases à la fois.")

    d.pratique('Production orale', "Saluez un voisin et parlez de votre journée",
               "Trois temps. Enregistrez-vous, écoutez-vous, recommencez.", [
        ("TEMPS 1", "Bonjour, madame. Ça va ?"),
        ("TEMPS 2", "Ça va bien, merci. Et vous ? … Le matin, je déjeune, puis je "
                    "marche jusqu'au centre."),
        ("TEMPS 3", "Bonne journée ! À demain !"),
    ], cols=1,
       notes="Vingt minutes. Le vouvoiement doit tenir du début à la fin : c'est ce que "
             "la correction en ligne regarde en premier. Laisser recommencer autant de "
             "fois qu'il le faut.")

    d.pratique('Production écrite', "Écrivez une carte de vœux",
               "De trois à cinq phrases, pour un voisin ou un camarade.", [
        ("À écrire", "Un souhait : bonne fête, bonne santé, bon voyage…"),
        ("À écrire", "Un merci, avec le mot « pour »."),
        ("À écrire", "Le nom de la personne à qui vous écrivez."),
        ("À écrire", "Votre prénom, sur la dernière ligne."),
    ], cols=1,
       notes="Vingt minutes. Rappeler l'astuce du « une » pour choisir entre bon et "
             "bonne : c'est ce qui sera regardé.")

    d.billet(
        "Saluez trois personnes cette semaine, et dites-leur une chose de votre journée.",
        exemples=[
            "Bonjour ! Ça va ? Et vous ?",
            "Le matin, je viens au centre à pied.",
            "Bonne journée ! À demain !",
        ],
        notes="Dernier devoir du module. Demander au cours suivant ce que les gens ont "
              "répondu : c'est souvent la première conversation qu'ils ont eue avec un "
              "voisin.")

    return d.save(dossier)
