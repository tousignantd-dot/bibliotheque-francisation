# -*- coding: utf-8 -*-
"""B3 · « Ne la déplacez pas » — l'impératif présent.
Bloc B « Défi 1 » · couleur ambre · 75 min. Écriture.
Source : exercice `t1imp` et sa mini-leçon.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-urgence/images/')


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="« Ne la déplacez pas »",
        chapeau="Le mode de l'urgence : trois personnes, aucun sujet écrit, "
                "des phrases de quatre mots. On l'entend au téléphone, à "
                "l'arrivée des ambulanciers, au triage et au congé.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Prévenir que le ton direct du répartiteur n'est "
                  "pas de l'impolitesse : c'est le mode qui va avec la situation. "
                  "Plusieurs élèves le vivent mal la première fois.")

    d.objectifs([
        "former l'impératif présent aux trois personnes ;",
        "employer la forme négative avec ne… pas, ne… rien, ne… jamais ;",
        "reconnaître quatre impératifs irréguliers ;",
        "comprendre une consigne d'urgence et l'exécuter sans la faire répéter.",
    ])

    d.declencheur(
        'Écoute', "« Restez près d'elle. Ne la déplacez pas. Couvrez-la. » Trois "
                  "ordres en une phrase. Est-ce impoli ?",
        pistes=[
            "Combien de temps prendrait la version polie complète ?",
            "Qu'est-ce qui manque, par rapport à une phrase ordinaire ?",
            "Lequel des trois ordres est le plus important ?",
            "Que se passe-t-il si on n'a pas compris ?",
        ],
        notes="La troisième piste : c'est l'ordre négatif qui compte le plus. Déplacer "
              "quelqu'un qui a une fracture aggrave la blessure.")

    d.regle("Trois personnes, aucun sujet",
            "Reste · Restons · Restez. Le sujet ne s'écrit pas.",
            precision="On part du présent de l'indicatif et on enlève le sujet. Les "
                      "verbes en -er perdent leur s à la personne « tu » : tu écoutes donne "
                      "Écoute !",
            notes="Diapositive à photographier. Ajouter l'exception « Vas-y », où le s "
                  "revient devant y.")

    d.tableau('Les formes', "Affirmatif et négatif, côte à côte",
              ['Verbe', 'Affirmatif', 'Négatif'],
              [["rester", "Restez près d'elle.", "Ne restez pas dans le corridor."],
               ["déplacer", "Déplacez ce qui gêne.", "Ne la déplacez pas."],
               ["donner", "Donnez-lui la main.", "Ne lui donnez rien à boire."],
               ["raccrocher", "Raccrochez maintenant.", "Ne raccrochez pas."],
               ["aller", "Allez ouvrir la porte.", "N'allez pas la relever."]],
              cle=2,
              note="Le ne… pas entoure le verbe, exactement comme dans une phrase ordinaire.",
              notes="Faire lire la colonne de droite à voix haute : ce sont les phrases "
                    "que l'élève entendra vraiment.")

    d.cartes("Quatre irréguliers à connaître par cœur", "Ils reviennent partout en santé", [
        ("être", "sois · soyons · soyez — « Soyez à côté d'elle. »"),
        ("avoir", "aie · ayons · ayez — « Ayez sa carte à la main. »"),
        ("aller", "va · allons · allez — « Allez ouvrir la porte. »"),
        ("savoir", "sache · sachons · sachez — « Sachez que l'aide arrive. »"),
    ], notes="Les faire répéter dans les phrases, jamais en liste. Une conjugaison "
             "apprise hors contexte ne ressort pas sous pression.")

    d.pratique('Formation', "Mettez à l'impératif, à la forme « vous »",
               "À l'oral d'abord, puis à l'écrit.", [
        ("___ (rester) près d'elle et ___ (parler) lui doucement.", "Restez · parlez"),
        ("Ne la ___ (déplacer) pas.", "déplacez"),
        ("___ (couvrir) la avec une couverture.", "Couvrez"),
        ("Ne lui ___ (donner) rien à boire ni à manger.", "donnez"),
        ("___ (aller) déverrouiller la porte de l'immeuble.", "Allez"),
        ("___ (être) au téléphone quand ils arriveront.", "Soyez"),
        ("___ (avoir) sa carte d'assurance maladie à la main.", "Ayez"),
        ("Ne ___ (raccrocher) pas avant que je vous le dise.", "raccrochez"),
    ], corrige=True,
       notes="Les deux irréguliers arrivent en fin de liste, quand la mécanique est "
             "installée. Ne pas les donner d'avance.")

    d.piege("Garder le sujet",
            "Vous restez près d'elle.",
            "Restez près d'elle.",
            "Avec le sujet, c'est une affirmation — une description de ce que vous faites. "
            "Sans lui, c'est un ordre. Au téléphone, la différence s'entend tout de suite.",
            notes="Erreur très fréquente et facile à corriger. La montrer, puis passer.")

    d.piege("Laisser tomber le « ne »",
            "Déplacez-la pas.",
            "Ne la déplacez pas.",
            "On l'entend à l'oral familier, mais il est obligatoire à l'écrit et dans "
            "toute situation officielle — y compris dans un examen de fin de cours.",
            notes="Nommer l'usage oral sans le condamner : les élèves l'entendent partout. "
                  "Ce qui compte, c'est de savoir quand il ne passe pas.")

    d.pratique('Compréhension', "Ce que le répartiteur vous demande",
               "Écoutez et redites l'ordre dans vos mots.", [
        ("Restez près d'elle et parlez-lui.", "je reste, je lui parle"),
        ("Ne la déplacez pas.", "je ne la bouge pas"),
        ("Couvrez-la avec une couverture.", "je la couvre"),
        ("Ne lui donnez rien à boire.", "je ne lui donne rien"),
        ("Allez déverrouiller la porte.", "je descends ouvrir"),
        ("Soyez au téléphone quand ils arriveront.", "je reste en ligne"),
    ], corrige=True,
       notes="Reformuler un ordre est le vrai test de compréhension. Insister sur le fait "
             "de le dire à voix haute : au téléphone, le répartiteur ne voit rien.")

    d.billet(
        "Écrivez quatre consignes que vous donneriez à quelqu'un qui vous aide.",
        exemples=[
            "Deux à la forme affirmative, deux à la forme négative.",
            "Employez au moins un des quatre verbes irréguliers.",
        ],
        notes="Ramasser et corriger : les phrases justes serviront d'exemples au début "
              "de B4, où l'on ajoutera les pronoms.")

    return d.save(dossier)
