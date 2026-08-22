# -*- coding: utf-8 -*-
"""C1 · On lit ce qui est écrit
Bloc C « Défi 2 · Ce que disent les documents » · couleur acier · 75 min.
Source : dialogue `t2`, exercices `t2vf` et `t2mise`, mini-leçon `t2mise`.
Intention du programme : lire de la documentation interne reliée à son emploi.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="On lit ce qui est écrit",
        chapeau="Deux documents, deux façons d'écrire. La note explique et "
                "dit « vous » ; la politique fixe des règles et dit "
                "« l'employé ».",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 2. Apporter en classe une vraie note de service "
                  "du centre, si l'on en a une : la comparer à celle du module vaut "
                  "toutes les explications.")

    d.objectifs([
        "reconnaître ce que l'en-tête d'un document apprend ;",
        "lire ce que les puces, les numéros et l'encadré veulent dire ;",
        "distinguer une note de service d'une politique interne ;",
        "employer les quatre mots des documents écrits.",
    ], notes="Le deuxième objectif est celui du bloc : la mise en page parle avant "
             "les phrases, et cette lecture-là s'apprend en une séance.")

    d.declencheur(
        'Observation', "Quand tu reçois un papier au travail, par où commences-tu ?",
        pistes=[
            "Par le haut, par le bas, ou par le milieu ?",
            "Combien de temps te faut-il pour savoir s'il te concerne ?",
            "Qu'est-ce que tu regardes en premier sur une feuille inconnue ?",
        ],
        notes="La réponse habituelle est « je lis tout ». C'est justement ce que la "
              "séance vient corriger : deux lignes en haut, un encadré en bas.")

    d.dialogue('Dialogue · 1 de 3', "L'en-tête dit si ça te concerne", [
        ("YANETH", "J'ai les deux papiers. La note de service, et l'article quatre de la politique.", True),
        ("GHISLAIN", "Regarde d'abord comment c'est fait, avant de lire les phrases. La note, en haut, elle a quoi ?", True),
        ("YANETH", "Une date, un destinataire — « à l'ensemble du personnel » — et une ligne « Objet ».", True),
        ("GHISLAIN", "Deux lignes, et tu sais déjà si tu continues.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Faire relever les trois lignes d'en-tête sur un vrai document projeté. "
             "C'est le geste le plus rentable de toute la lecture professionnelle.")

    d.dialogue('Dialogue · 2 de 3', "Des puces, ou des numéros ?", [
        ("YANETH", "Et les petits points noirs au milieu ?", True),
        ("GHISLAIN", "Des puces. Chaque puce est une chose à faire, et elles sont dans l'ordre.", True),
        ("YANETH", "La politique, elle, n'a pas de puces. Elle a des numéros : 4.1, 4.2, 4.3.", True),
        ("GHISLAIN", "Une note explique, une politique fixe des règles. On numérote une règle pour pouvoir la nommer.", True),
    ], notes="« Selon 4.3 » : le faire dire à voix haute. Retenir un numéro d'article "
             "est un vrai pouvoir, et c'est une idée neuve pour beaucoup.")

    d.dialogue('Dialogue · 3 de 3', "Laquelle gagne sur l'autre ?", [
        ("YANETH", "La note dit « veuillez consulter la politique » et la politique dit « voir la note ». Chacune renvoie à l'autre.", True),
        ("GHISLAIN", "C'est normal, et c'est une bonne nouvelle : ça veut dire qu'il n'y a qu'une seule règle.", True),
        ("GHISLAIN", "Le jour où elles ne diront plus la même chose, c'est la politique qui gagne.", True),
        ("GHISLAIN", "Une note, ça explique ; ça ne change jamais une règle.", True),
    ], notes="La dernière réplique est la règle du bloc. La faire répéter, et la "
             "rapporter au tableau d'A4 : le poids des papiers.")

    d.tableau('Analyse', "Ce que la mise en page t'apprend",
              ['L\'élément', 'Ce qu\'il te dit'],
              [["La ligne « À : »", "si le document te concerne, toi"],
               ["La ligne « Objet : »", "de quoi il parle, en une seule ligne"],
               ["Les puces", "une suite de gestes, et ils sont dans l'ordre"],
               ["Les numéros 4.1, 4.2", "des règles qu'on pourra citer sans les recopier"],
               ["L'encadré gris", "ce que l'auteur ne veut surtout pas qu'on manque"],
               ["Le mot en gras", "le mot le plus important de la phrase"]],
              cle=0,
              notes="Diapositive à photographier. Six rangées sans note : c'est le "
                    "maximum lisible de loin. L'encadré est l'élément le plus souvent "
                    "manqué, parce que le regard descend au texte et saute le bas de "
                    "page.")

    d.regle("Une note explique, une politique décide",
            "En cas de contradiction, c'est la politique qui s'applique.",
            precision="Une note de service s'adresse au personnel et dit « vous ». "
                      "Une politique ne s'adresse à personne en particulier et dit "
                      "« l'employé ». C'est la différence la plus visible entre les "
                      "deux, et c'est aussi la plus utile : quand un doute surgit, on "
                      "sait lequel des deux papiers aller chercher.",
            notes="Diapositive à photographier. Ajouter oralement ce que le module dit "
                  "au Défi 2 : une politique interne vient de l'employeur, pas de la "
                  "loi. C'est un engagement d'entreprise, ni plus ni moins.")

    d.vocabulaire('Vocabulaire', "Quatre mots des documents écrits", [
        ("une note de service", "Un court document que l'employeur envoie au personnel pour expliquer."),
        ("une politique interne", "L'ensemble des règles écrites que l'entreprise se donne."),
        ("les exigences du poste", "Ce qu'il faut absolument avoir ou savoir faire pour l'occuper."),
        ("un droit de retour", "La possibilité de revenir à son ancien poste si le nouveau ne convient pas."),
    ], notes="Le droit de retour protège les deux côtés : le dire tout de suite, sinon "
             "le groupe le prend pour une faveur, et la question revient trois fois.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la lecture de Yaneth et de Ghislain.", [
        ("La note porte une date, un destinataire et une ligne « Objet ».", "vrai"),
        ("Les puces marquent des choses à faire, dans l'ordre.", "vrai"),
        ("La politique interne emploie des puces, elle aussi.", "faux - des articles numérotés"),
        ("On numérote les articles pour pouvoir nommer une règle.", "vrai"),
        ("Une note de service peut changer une règle de la politique.", "faux - elle explique seulement"),
        ("La note et la politique se renvoient l'une à l'autre.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique. Le cinquième est celui "
             "qui compte : il décide de ce qu'on va citer dans une discussion.")

    d.billet(
        "Nomme deux endroits d'un document que tu liras dorénavant en premier.",
        exemples=[
            "Deux mots suffisent.",
            "Dis pourquoi pour l'un des deux.",
        ],
        notes="Deux minutes. La réponse attendue : la ligne « Objet » et l'encadré. "
              "C'est la mesure de la séance, et le pont vers C2.")

    return d.save(dossier)
