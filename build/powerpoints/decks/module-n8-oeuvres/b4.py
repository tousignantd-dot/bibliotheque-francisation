# -*- coding: utf-8 -*-
"""B4 · Mettre en avant l'indice qui porte votre lecture
Bloc B « Défi 1 · La dernière scène » · couleur ambre · 75 min.
Source : exercice `t1emph` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Mettre en avant l'indice qui porte votre lecture",
        chapeau="Une lecture repose presque toujours sur un seul détail. "
                "Énumérés à la file, trois arguments se valent ; mis en "
                "relief, un seul dit à l'autre quoi contester.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 1. C'est l'outil de langue qui sert le plus "
                  "en D1 et en E2 : l'emphase désigne le morceau de phrase sur lequel "
                  "tout repose.")

    d.objectifs([
        "extraire un morceau de phrase avec « c'est… qui » et « c'est… que » ;",
        "annoncer puis nommer avec « ce qui… c'est » ;",
        "choisir la forme d'après la préposition du verbe ;",
        "s'en tenir à deux mises en relief par texte.",
    ], notes="Le quatrième objectif surprend, et il est réel : au-delà de deux, "
             "l'effet s'use et le lecteur cesse de chercher ce qui compte.")

    d.declencheur(
        'Observation', "Ces deux phrases disent-elles la même chose ?",
        pistes=[
            "« Le téléphone compte le plus. »",
            "« Ce qui compte le plus, c'est le téléphone. »",
            "Qu'est-ce qui change ? Les mots, ou autre chose ?",
            "Laquelle des deux vous dit sur quoi porter votre réponse ?",
        ],
        notes="Le contenu est identique ; ce qui change est l'endroit où l'on regarde. "
              "La quatrième piste dit à quoi sert l'emphase : elle organise la "
              "réponse de l'autre.")

    d.tableau('Analyse', "Deux façons de mettre en avant",
              ['La forme', 'Un exemple'],
              [["c'est... qui", "C'est elle qui a remis la chaloupe à l'eau."],
               ["c'est... que", "C'est la corde que vous passez sous silence."],
               ["ce qui... c'est", "Ce qui compte le plus, c'est le téléphone."],
               ["ce dont... c'est", "Ce dont il parle, c'est du dernier vers."],
               ["ce à quoi... c'est", "Ce à quoi je pense, c'est la parenthèse."]],
              cle=0,
              note="« qui » si le morceau extrait est sujet. « que » dans tous les autres cas.",
              notes="Diapositive à photographier. La note du bas est la seule décision "
                    "à prendre pour le clivage ; le reste suit la préposition du "
                    "verbe.")

    d.regle("La préposition du verbe choisit la forme",
            "Je pense à... donne « ce à quoi ». Je parle de... donne « ce dont ».",
            precision="Faites la phrase à l'endroit pour trouver la préposition, puis "
                      "reconstruisez. C'est mécanique, et cela évite le tâtonnement : "
                      "on ne choisit pas entre « ce dont » et « ce à quoi » à "
                      "l'oreille, on le déduit du verbe.",
            notes="Diapositive à photographier. Faire l'opération à voix haute deux "
                  "fois : « il parle de ce détail » — de — dont.")

    d.cartes('Analyse', "Avant, après", [
        ("Le téléphone compte le plus.", "Ce qui compte le plus, c'est le téléphone."),
        ("Elle a remis la chaloupe à l'eau.", "C'est elle qui a remis la chaloupe à l'eau."),
        ("Vous passez la corde sous silence.", "C'est la corde que vous passez sous silence."),
        ("Je pense à la parenthèse.", "Ce à quoi je pense, c'est la parenthèse."),
        ("Il parle du dernier vers.", "Ce dont il parle, c'est du dernier vers."),
        ("Le cercle se réunit au sous-sol.", "C'est au sous-sol que le cercle se réunit."),
    ], notes="Faire lire les deux colonnes à voix haute, par deux personnes qui se "
             "répondent. La deuxième colonne s'entend plus longue et plus lente : "
             "c'est l'effet recherché.")

    d.piege('Piège', "« Ce qui comptent, ce sont les bottes »",
            "« Ce qui compte, ce sont les bottes »",
            "Après « ce qui », le verbe reste au singulier, même quand ce qui "
            "suit est au pluriel. Seule la seconde moitié peut se mettre au "
            "pluriel : « c'est » ou « ce sont », les deux se disent. La faute "
            "vient de l'accord fait à l'oreille, sur le mot qu'on entend le plus "
            "fort — et c'est précisément le mot qu'on a mis en relief.",
            notes="Le montrer au tableau en encadrant « ce qui » : le sujet du verbe "
                  "est là, pas plus loin.")

    d.pratique('Pratique', "Mettez en relief",
               "Récrivez le début de la phrase.", [
        ("Le téléphone compte le plus.", "Ce qui compte le plus, c'est..."),
        ("Elle a remis la chaloupe à l'eau.", "C'est elle qui..."),
        ("Vous passez la corde sous silence.", "C'est la corde que..."),
        ("Je pense à la parenthèse.", "Ce à quoi je pense, c'est..."),
        ("Il parle du dernier vers.", "Ce dont il parle, c'est..."),
        ("Elle emporte la nappe.", "Ce qu'elle emporte, c'est..."),
    ], corrige=True,
       notes="Exercice `t1emph` du module. Faire écrire la phrase entière, pas "
             "seulement le début : c'est l'accord du verbe qui est en jeu.")

    d.pratique('Production', "Défendez une lecture en trois phrases",
               "Une lecture, un indice mis en relief, une concession.", [
        ("Phrase 1", "Je crois qu'elle choisit de rester."),
        ("Phrase 2", "Ce qui me le fait dire, c'est le téléphone laissé sonner."),
        ("Phrase 3", "Bien sûr, la corde reste attachée."),
        ("À votre tour", "sur l'œuvre de votre billet de B2"),
    ], corrige=False,
       notes="En dyades, dix minutes, debout. C'est la répétition générale de D1 et de "
             "E1 : trois phrases, pas une de plus, et l'indice au milieu.")

    d.billet(
        "Écrivez les trois phrases de l'exercice précédent sur votre propre "
        "œuvre, et soulignez la mise en relief.",
        exemples=[
            "Une seule mise en relief : celle de la deuxième phrase.",
            "La troisième phrase accorde quelque chose, elle ne se rétracte pas.",
        ],
        notes="Ces trois phrases sont le noyau de la production orale d'E1. Les "
              "ramasser et les rendre annotées avant le bloc D.")

    return d.save(dossier)
