# -*- coding: utf-8 -*-
"""B3 · Ce qui aurait pu se passer et ne s'est pas passé
Bloc B « Défi 1 · La dernière scène » · couleur ambre · 75 min.
Source : exercices `t1cond` et `t1irreel`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Ce qui aurait pu se passer et ne s'est pas passé",
        chapeau="« Elle aurait pu détacher la corde. » Elle ne l'a pas fait, "
                "et pourtant la phrase place le geste sous nos yeux. Une œuvre "
                "se comprend aussi par ce qu'elle écarte.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, et elle n'est pas décorative : sans le "
                  "conditionnel passé, on ne peut parler que de ce qui arrive. Avec "
                  "lui, on parle du travail de l'auteur.")

    d.objectifs([
        "former le conditionnel passé avec avoir et avec être ;",
        "nommer un geste que le personnage n'a pas fait ;",
        "construire l'hypothèse irréelle : si + plus-que-parfait ;",
        "ne jamais mettre de conditionnel après « si ».",
    ], notes="Le quatrième objectif est celui qu'un correcteur regarde en premier. "
             "L'annoncer comme tel : c'est la faute la plus surveillée du français "
             "écrit.")

    d.declencheur(
        'Observation', "Qu'est-ce qu'elle n'a pas fait ?",
        pistes=[
            "Elle s'assoit dans la chaloupe. Qu'aurait-elle pu faire d'autre ?",
            "Détacher la corde, démarrer le moteur, répondre au téléphone.",
            "Comment dit-on ces trois choses en français ?",
            "Pourquoi est-ce utile de les dire, puisqu'elles n'arrivent pas ?",
        ],
        notes="La quatrième question est celle qui justifie la séance. Réponse : parce "
              "qu'une réalisatrice a écarté ces trois gestes, et que ce sont ses "
              "choix qui font la scène.")

    d.tableau('Analyse', "Le conditionnel passé, en deux morceaux",
              ['Avec', 'Ce que ça donne'],
              [["avoir", "elle aurait pu, j'aurais compris, nous aurions aimé"],
               ["être", "elle serait partie, ils seraient restés"],
               ["l'accord", "avec être seulement : elle serait restée"]],
              cle=0,
              note="Vous connaissez déjà les deux moitiés : rien de neuf à apprendre.",
              notes="Diapositive à photographier. Le choix entre avoir et être est le "
                    "même qu'au passé composé — le rappeler évite une demi-heure.")

    d.regle("Trois emplois, un seul temps",
            "Le geste non fait, le regret ou le reproche, l'information qu'on "
            "rapporte sans la garantir.",
            precision="« Elle aurait pu détacher la corde » nomme un geste écarté. "
                      "« Tu aurais dû me le dire » reproche. « Le tournage aurait duré "
                      "onze jours » rapporte sans certifier. Le troisième se reconnaît "
                      "à ce qu'il n'y a aucun « si » dans la phrase.",
            notes="Diapositive à photographier. Le troisième emploi est celui des "
                  "journaux : le signaler, il change la façon de lire une nouvelle.")

    d.piege('Piège', "« elle aurait comprise »",
            "« elle aurait compris »",
            "Avec l'auxiliaire avoir, le participe ne s'accorde jamais avec le "
            "sujet. L'oreille entend un sujet féminin et veut un « e » ; il ne "
            "faut pas le suivre. Avec être, au contraire, il s'accorde toujours : "
            "« elle serait restée ». Deux auxiliaires, deux règles opposées — "
            "c'est ce qui rend ce temps-là difficile, et rien d'autre.",
            notes="Écrire les deux formes côte à côte au tableau et les y laisser "
                  "toute la séance.")

    d.pratique('Pratique', "Le conditionnel passé",
               "Mettez le verbe au conditionnel passé.", [
        ("Elle ___ (pouvoir) détacher la corde.", "aurait pu"),
        ("La réalisatrice ___ (devoir) couper ce plan.", "aurait dû"),
        ("Estelle ___ (partir) au printemps.", "serait partie"),
        ("Nous ___ (aimer) un dernier plan sur le chalet.", "aurions aimé"),
        ("Le tournage ___ (durer) onze jours de plus.", "aurait duré"),
        ("Elle ___ (comprendre) tout de suite.", "aurait compris"),
    ], corrige=True,
       notes="Exercice `t1cond` du module. Le troisième et le sixième mettent les deux "
             "règles d'accord côte à côte : les faire écrire au tableau par deux "
             "élèves différents.")

    d.tableau('Analyse', "Trois marches de l'hypothèse",
              ['La marche', 'La forme'],
              [["C'est encore possible", "si elle part, je le dirai"],
               ["C'est imaginé", "si elle partait, je le dirais"],
               ["C'est fini", "si elle était partie, je l'aurais dit"]],
              cle=0,
              note="Une œuvre est finie : c'est la troisième marche qui sert.",
              notes="Diapositive à photographier. Lire les trois à voix haute dans "
                    "l'ordre : on entend la langue reculer d'un cran à chaque ligne, "
                    "des deux côtés à la fois.")

    d.pratique('Pratique', "L'hypothèse irréelle du passé",
               "Complétez.", [
        ("Si elle avait voulu partir, elle ___ (détacher) la corde.", "aurait détaché"),
        ("Si elle ___ (démarrer) le moteur, la série finissait autrement.", "avait démarré"),
        ("Si le plan ___ (durer) deux secondes, personne ne l'aurait vu.", "avait duré"),
        ("Nous ___ (comprendre) plus vite si on nous avait montré.", "aurions compris"),
        ("Si vous ___ (venir) mardi, vous auriez entendu trois lectures.", "étiez venu"),
        ("Si j'avais su, je ___ (regarder) deux fois.", "aurais regardé"),
    ], corrige=True,
       notes="Exercice `t1irreel` du module. Surveiller le deuxième et le cinquième : "
             "c'est là que le conditionnel s'invite après « si ».")

    d.billet(
        "Écrivez deux phrases sur la fin de votre œuvre : une avec « elle "
        "aurait pu », une avec « si… avait…, … aurait… ».",
        exemples=[
            "« Il aurait pu répondre, et il n'a rien dit. »",
            "« Si elle avait ouvert la lettre, on saurait ce qu'elle contient. »",
        ],
        notes="Ramasser. Le deuxième exemple contient une petite faute volontaire de "
              "marche (« on saurait » au lieu de « on aurait su ») : demander au "
              "groupe s'il la voit, en début de B4.")

    return d.save(dossier)
