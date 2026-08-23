# -*- coding: utf-8 -*-
"""C1 · Trois messages, trois choses à faire
Bloc C « Défi 2 · Les messages qu'on me laisse » · couleur acier · 75 min.
Source du module : dialogue `t2`, exercices `t2a` et `t2notes`.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n4-etablissement/images/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Trois messages, trois choses à faire",
        chapeau="Le soir venu, c'est le téléphone de Nourhane qui clignote. "
                "Le secrétariat, l'enseignant, puis le secrétariat encore. "
                "Aucun des trois ne se répète, aucun ne pose de question.",
        duree='75 minutes')

    d.titre(notes="Première séance du bloc C, et la seule du module qui travaille la "
                  "compréhension orale pure. Distribuer un papier et un crayon à chacun "
                  "AVANT de faire écouter quoi que ce soit : c'est la consigne de la "
                  "séance, et elle doit être vécue, pas dite.")

    d.objectifs([
        "écouter un message et en tirer qui appelle, pourquoi, et quoi faire ;",
        "noter pendant l'écoute plutôt qu'après ;",
        "accepter de ne pas comprendre tous les mots ;",
        "savoir quand rappeler, et quand ne pas rappeler.",
    ], notes="Le troisième objectif est le plus difficile à faire admettre et le plus "
             "libérateur. Un message de trente secondes contient une centaine de mots ; "
             "trois suffisent.")

    d.regle("Trois choses, jamais plus",
            "Qui appelle, au début. Pourquoi, juste après. Ce qu'on attend "
            "de vous, à la fin.",
            precision="Comprendre un message n'est pas comprendre tous les "
                      "mots.",
            notes="Diapositive à photographier. Elle sert de grille d'écoute pour les "
                  "trois messages du jour et pour tous ceux que les élèves recevront "
                  "ensuite.")

    d.dialogue('Message 1 · Le secrétariat', "Une note écrite avant vendredi", [
        ("MURIELLE", "Bonjour madame Ouazzani, ici Murielle Sansregret, du "
                     "secrétariat de la Pointe-aux-Ormes.", True),
        ("MURIELLE", "J'ai bien reçu votre message de ce matin et j'ai "
                     "inscrit votre absence au dossier.", True),
        ("MURIELLE", "Par contre, une absence n'est motivée que si vous nous "
                     "remettez une note écrite et signée.", True),
        ("MURIELLE", "Apportez-la-moi avant vendredi, au comptoir, avec le "
                     "papier de la clinique. Merci.", True),
    ], consigne="Écoutez d'abord, diapositive masquée, crayon en main.",
       notes="Faire écouter deux fois : la première pour saisir, la seconde en "
             "écrivant. Puis demander les trois renseignements. La troisième réplique "
             "est celle qui rappelle la règle des deux moitiés, vue en A1.")

    d.dialogue('Message 2 · L\'enseignant', "Le rattrapage au local 214", [
        ("FABIEN", "Bonjour Nourhane, c'est Fabien Corriveau, votre "
                   "enseignant du groupe 6.", True),
        ("FABIEN", "On a fait les nombres et l'heure ce matin ; je vous ai "
                   "gardé les feuilles.", True),
        ("FABIEN", "Le rattrapage a lieu demain sur l'heure du dîner, au "
                   "local 214, si ça vous convient.", True),
        ("FABIEN", "Ne vous inquiétez pas pour aujourd'hui : ça arrive à "
                   "tout le monde. À demain.", True),
    ], notes="Ce message-là ne demande presque rien : c'est un renseignement, plus une "
             "proposition. Faire remarquer la dernière réplique — quand un message dit "
             "« ne vous inquiétez pas », c'est aussi un renseignement, et il se note.")

    d.dialogue('Message 3 · Le secrétariat encore', "Un détail oublié", [
        ("MURIELLE", "Madame Ouazzani, Murielle Sansregret encore. Un détail "
                     "que j'ai oublié.", True),
        ("MURIELLE", "Vous êtes aussi inscrite au cours d'informatique du "
                     "soir. Si vous l'abandonnez, il faut nous le dire par "
                     "écrit avant la fin du mois.", True),
        ("MURIELLE", "Sinon, l'abandon est inscrit comme un échec, et ce "
                     "n'est pas la même chose du tout.", True),
        ("NOURHANE", "Ça, je ne le savais pas. Grâce à elle, je l'apprends à "
                     "temps.", False),
    ], notes="Le troisième message porte l'information la plus lourde du module. Le "
             "faire réécouter une fois de plus que les autres, et faire écrire la date "
             "limite au tableau : avant la fin du mois.")

    d.tableau('Ce que vous notez', "Trois messages, six renseignements",
              ['Le message', 'Ce qu\'on note'],
              [["1 · qui appelle", "Murielle Sansregret, du secrétariat."],
               ["1 · à faire", "Une note écrite et signée, avant vendredi."],
               ["2 · qui appelle", "Fabien Corriveau, l'enseignant du groupe 6."],
               ["2 · à faire", "Rattrapage demain midi, local 214."],
               ["3 · qui appelle", "Murielle Sansregret, une deuxième fois."],
               ["3 · à faire", "Annoncer l'abandon par écrit avant la fin du mois."]],
              cle=1,
              notes="Faire remplir la colonne de droite pendant l'écoute, pas après. "
                    "Comparer ensuite les notes de deux voisins : ce qui manque à l'un "
                    "et pas à l'autre montre où l'attention a lâché.")

    d.declencheur(
        'Observation', "Une feuille pliée qui passe d'une main à une autre. "
                       "Qu'est-ce qui est écrit dessus ?",
        image=img('note-remise-main.jpg'),
        pistes=[
            "Qu'est-ce qu'il faut écrire sur une note d'absence, à votre avis ?",
            "À qui la remet-on : à l'enseignant ou au secrétariat ?",
            "Faut-il la signer ? Pourquoi ?",
            "Que gardez-vous, vous, quand vous remettez ce papier ?",
        ],
        notes="Cette observation ouvre le bloc D. Ne pas donner les réponses "
              "aujourd'hui : les noter au tableau et les laisser jusqu'à D1, où on les "
              "vérifiera une à une.")

    d.piege("Vouloir tout comprendre",
            "Je réécoute dix fois la même phrase, je ne comprends pas un mot.",
            "Je note le nom, la raison et ce qu'il faut faire, et je passe.",
            "Le mot que vous n'avez pas compris n'est presque jamais l'un des "
            "trois renseignements utiles. Vérifiez à la fin s'il vous manque "
            "quelque chose : la plupart du temps, non.",
            notes="Ce piège coûte du temps et du courage. Le nommer soulage : plusieurs "
                  "élèves croient qu'ils écoutent mal alors qu'ils écoutent trop.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après les trois messages.", [
        ("L'absence de Nourhane est inscrite au dossier.", "vrai"),
        ("Le message enregistré suffit, aucun papier n'est demandé.",
         "faux — une note écrite avant vendredi"),
        ("Le rattrapage a lieu le midi, au local 214.", "vrai"),
        ("Monsieur Corriveau appelle pour reprocher son absence.",
         "faux — pour rassurer et proposer"),
        ("Un abandon non annoncé est inscrit comme un échec.", "vrai"),
        ("Les trois messages viennent de la même personne.",
         "faux — deux du secrétariat, un de l'enseignant"),
    ], corrige=True,
       notes="La sixième vérifie qu'on a bien identifié les voix. C'est le premier des "
             "trois renseignements, et c'est celui qu'on manque quand on n'écoute pas "
             "les cinq premières secondes.")

    d.billet(
        "Écrivez les trois choses qu'il faut attraper dans un message "
        "téléphonique.",
        exemples=[
            "Dans l'ordre où on les entend.",
            "Ajoutez, pour chacune, à quel moment du message elle se trouve.",
        ],
        notes="Ramasser. Ceux qui écrivent quatre ou cinq choses n'ont pas encore fait "
              "le tri : leur redire qu'il n'y en a que trois, et que le reste est du "
              "confort.")

    return d.save(dossier)
