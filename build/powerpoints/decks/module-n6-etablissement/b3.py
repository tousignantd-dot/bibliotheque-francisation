# -*- coding: utf-8 -*-
"""B3 · Le, en, y : trois mots qui renvoient en arrière
Bloc B « Défi 1 » · couleur ambre · 75 min. Grammaire du texte.
Source : exercice `t1repr`, son bandeau de savoir et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Le, en, y : trois mots qui renvoient en arrière",
        chapeau="On perd rarement le fil sur un mot inconnu. On le perd "
                "presque toujours sur un mot de deux lettres.",
        duree='75 minutes')

    d.titre(notes="Séance centrale du module et du niveau. La reprise de "
                  "l'information est le savoir qui distingue vraiment le niveau 6 "
                  "des niveaux 3 et 5. Prendre le temps ; ne pas ajouter d'exercice.")

    d.objectifs([
        "retrouver ce que remplacent « le », « en » et « y » dans une phrase suivie ;",
        "employer « le » pour reprendre une idée entière, sans l'accorder ;",
        "employer « en » pour « de + chose » et « y » pour « à + chose » ou un lieu ;",
        "garder la préposition quand il s'agit d'une personne.",
    ], notes="Le quatrième objectif est le plus souvent raté, et il s'entend "
             "immédiatement : « j'y pense » pour une personne est une faute qui "
             "s'installe si on ne la nomme pas tout de suite.")

    d.declencheur(
        'Observation', "« Je le sais. » — vous savez quoi ?",
        pistes=[
            "Écoutez la phrase seule : elle ne veut rien dire.",
            "Qu'est-ce qu'il faut avoir entendu avant pour la comprendre ?",
            "Est-ce qu'il existe des mots pareils dans votre langue ?",
        ],
        notes="Écrire « Je le sais. » au tableau, seule, et laisser le silence. Le "
              "groupe comprend en trente secondes ce que la séance va enseigner.")

    d.tableau('Analyse', "Trois mots, trois emplois",
              ['Le mot', 'Ce qu\'il remplace'],
              [["le, l'", "une idée entière, une phrase déjà dite : Je sais que c'est fini. Je le sais."],
               ["en", "de plus une chose : Il parle des préalables. Il en parle."],
               ["y", "à plus une chose, ou un lieu : Elle va au secrétariat. Elle y va."]],
              cle=0,
              note="Ils passent toujours devant le verbe conjugué, ou devant l'infinitif quand il y a deux verbes.",
              notes="Diapositive à photographier. Faire lire chaque exemple deux fois, "
                    "la phrase longue puis la courte : c'est le chemin que fait "
                    "l'oreille pendant un entretien.")

    d.regle("Le « le » d'idée ne s'accorde jamais",
            "Il ne désigne ni un homme, ni une femme, ni un pluriel : il désigne une phrase.",
            precision="« Elle sait que c'est vrai » devient « Elle le sait », jamais "
                      "« elle la sait ». Les verbes qui appellent ce « le » sont "
                      "toujours les mêmes : savoir, dire, croire, ignorer, expliquer, "
                      "répéter, comprendre.",
            notes="Diapositive à photographier. Faire répéter la liste de verbes : "
                  "elle est courte et elle couvre presque tous les cas d'un bureau.")

    d.piege('Grammaire',
            "je pense à ma fille, donc j'y pense",
            "je pense à elle",
            "« En » et « y » ne remplacent jamais une personne. Pour une "
            "personne, on garde la préposition et on met un pronom fort : je "
            "pense à elle, je parle de lui, je m'occupe d'eux. C'est la faute "
            "la plus fréquente du niveau, et elle s'entend tout de suite.",
            notes="Donner cinq phrases à trier oralement : chose ou personne ? Le tri "
                  "prend trois minutes et règle la moitié du problème.")

    d.pratique('Pratique', "Complétez avec le, l', en ou y",
               "Le passage souligné dans la première phrase est ce qu'il faut remplacer.", [
        ("Pascal explique que le test ne remplace pas un diplôme. Bintou ne ... savait pas.", "le"),
        ("Elle pense à sa demande d'admission. Elle ... pense depuis trois semaines.", "y"),
        ("Il parle souvent des préalables particuliers. Il ... parle à chaque rencontre.", "en"),
        ("On trouve les préalables dans l'encadré gris. On ... trouve aussi les dates.", "y"),
        ("Le conseiller a répété que ce n'était pas une équivalence. Il ... a répété deux fois.", "l'"),
        ("Bintou a besoin d'un relevé de notes. Elle ... a besoin avant février.", "en"),
    ], corrige=True,
       notes="Faire d'abord dire à voix haute ce que le mot remplace, avant d'écrire "
             "le pronom. Un élève qui nomme le référent ne se trompe presque jamais "
             "de pronom.")

    d.tableau('Analyse', "Les verbes qui commandent le pronom",
              ['Le verbe se construit avec', 'On emploie'],
              [["de : parler de, avoir besoin de", "en"],
               ["à : penser à, s'inscrire à", "y"],
               ["un lieu : aller à, être à", "y"],
               ["que : savoir que, dire que", "le, l'"]],
              cle=1,
              note="C'est la construction du verbe qui décide, jamais le sens de la phrase.",
              notes="Diapositive à photographier. Faire ajouter deux verbes par "
                    "rangée, trouvés par le groupe. La liste personnelle vaut plus "
                    "que celle du tableau.")

    d.pratique('Pratique', "Chose ou personne ?",
               "Récrivez la deuxième phrase, en remplaçant le passage souligné.", [
        ("Je pense à ma facture.", "j'y pense"),
        ("Je pense à ma sœur.", "je pense à elle"),
        ("Elle parle de son dossier.", "elle en parle"),
        ("Elle parle de sa conseillère.", "elle parle d'elle"),
        ("Il s'occupe de ses papiers.", "il s'en occupe"),
        ("Il s'occupe de ses enfants.", "il s'occupe d'eux"),
    ], corrige=True, cols=2,
       notes="Les six items vont deux par deux : la même construction, une chose puis "
             "une personne. Corriger par paires, pas dans l'ordre de la grille.")

    d.billet(
        "Écris deux phrases sur ta propre démarche, avec « y » et avec « en ».",
        exemples=[
            "Pense à ta demande, à ton dossier, à un papier qu'il te manque.",
            "Écris d'abord la phrase longue, puis la courte en dessous.",
        ],
        notes="Cinq minutes. Ramasser deux ou trois productions et les projeter au "
              "tableau la séance suivante : rien ne vaut une phrase écrite par "
              "quelqu'un du groupe.")

    return d.save(dossier)
