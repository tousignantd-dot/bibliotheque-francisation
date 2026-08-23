# -*- coding: utf-8 -*-
"""D2 · Le passé composé avec être, et le futur simple
Bloc D « Défi 3 · La note à remettre » · couleur ambre · 75 min.
Source du module : exercices `t3pc`, `t3futur` et `t3ecrit`.
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
        code='D2', section='ambre',
        titre="Le passé composé avec être, et le futur simple",
        chapeau="Deux temps, deux moitiés de la note. Le passé composé dit "
                "ce qui est arrivé ; le futur dit ce qui va se passer. Et "
                "entre les deux, une lettre qu'on n'entend pas et qui se "
                "voit : le « e » de « je suis allée ».",
        duree='75 minutes')

    d.titre(notes="Deuxième et dernière séance du bloc D. Deux points de grammaire dans "
                  "une seule séance, mais ils vont ensemble : ce sont les deux temps de "
                  "la note. Donner quarante minutes au premier, trente au second.")

    d.objectifs([
        "reconnaître les verbes qui prennent l'auxiliaire être ;",
        "accorder le participe passé avec le sujet ;",
        "reconnaître le futur simple à son « r » ;",
        "écrire les deux dernières lignes d'une note d'abandon.",
    ], notes="Le deuxième objectif est celui du jour. Rappeler que le module est écrit "
             "au féminin : Nourhane écrit « allée », « restée », « revenue ».")

    d.regle("Avec être, le participe s'accorde",
            "Il est allé. Elle est allée. Ils sont allés. Elles sont allées.",
            precision="Avec avoir, il ne bouge pas : elle a téléphoné, "
                      "jamais « téléphonée ».",
            notes="Diapositive à photographier. Les deux moitiés de la règle comptent "
                  "autant l'une que l'autre : on oublie l'accord avec être, et on en "
                  "ajoute un avec avoir.")

    d.tableau('Les verbes qui prennent être', "Une quinzaine, et la liste ne s'allonge pas",
              ['La famille', 'Les verbes'],
              [["Aller et venir", "aller, venir, revenir, retourner, arriver, partir"],
               ["Entrer et sortir", "entrer, sortir, monter, descendre, rester, tomber"],
               ["Naître et devenir", "naître, mourir, devenir, rentrer"],
               ["Tous les pronominaux", "se lever, se rendre, s'absenter, se présenter"]],
              note="Tous les autres verbes prennent avoir.",
              notes="La quatrième ligne est la plus rentable : tout verbe qui porte "
                    "« se » à l'infinitif prend être, sans exception à ce niveau.")

    d.cartes("Ce qui ne s'entend pas", "Et qui se voit quand même", [
        ("allé, allée",
         "Se prononcent exactement pareil. C'est pourquoi la faute survit à l'oral."),
        ("Le test en deux secondes",
         "Remplacez le sujet par « une femme » : une femme est allée."),
        ("revenu, revenue",
         "Ici, un peu de différence s'entend. Écoutez les deux."),
        ("Relire à voix haute",
         "C'est ainsi que Nourhane a entendu son « je suis allé » sans e."),
    ], notes="La deuxième carte est le geste à installer. Le faire pratiquer trois fois "
             "à voix haute sur des phrases du groupe, puis le laisser tomber : il doit "
             "devenir automatique.")

    d.pratique('Accord', "Écrivez le participe passé",
               "C'est une femme qui écrit.", [
        ("Je suis (aller) ___ à la clinique avec mon fils.", "allée"),
        ("Mon fils est (tomber) ___ malade dimanche soir.", "tombé"),
        ("Je suis (rester) ___ à la maison toute la journée.", "restée"),
        ("J'ai (téléphoner) ___ au centre à sept heures dix.", "téléphoné"),
        ("Elle est (revenir) ___ trop tard pour le cours.", "revenue"),
        ("Je me suis (lever) ___ à cinq heures.", "levée"),
    ], corrige=True,
       notes="La quatrième est le piège : « téléphoner » prend avoir, donc aucun "
             "accord. Elle est placée au milieu exprès. Faire justifier l'auxiliaire "
             "avant l'accord, chaque fois.")

    d.regle("Le futur se reconnaît à son « r »",
            "je remettrai, je rattraperai, je serai, j'irai, je viendrai.",
            precision="Le « r » est là dans tous les cas. Cherchez-le : "
                      "c'est le repère le plus sûr.",
            notes="Diapositive à photographier. Signaler les six irréguliers utiles : "
                  "être, avoir, aller, venir, pouvoir, devoir. Ils ne se déduisent pas "
                  "de l'infinitif.")

    d.tableau('Ce que vous promettez', "Six phrases de fin de note",
              ['La phrase', 'Ce qu\'elle promet'],
              [["Je serai en classe demain matin.", "Votre retour, avec le jour."],
               ["Je rattraperai la matière.", "Comment vous reprendrez ce qui a été manqué."],
               ["Je vous remettrai le papier jeudi.", "Une preuve, à une date."],
               ["Je vous rappellerai avant seize heures.", "Un second appel, aujourd'hui."],
               ["Je devrai quitter à onze heures.", "Un départ avant la fin, annoncé."],
               ["J'irai au secrétariat avant midi.", "Où vous irez, et avant quelle heure."]],
              cle=1,
              notes="Faire souligner le « r » dans chaque verbe. Puis faire produire "
                    "trois autres promesses à partir de la situation réelle de chaque "
                    "élève.")

    d.piege("Écrire « je remettrais » avec un s",
            "Je vous remettrais le papier jeudi.",
            "Je vous remettrai le papier jeudi.",
            "Avec un « s », c'est un conditionnel : cela veut dire « si les "
            "choses le permettaient ». Dans une note, on écrit le futur, sans "
            "« s » : c'est un engagement, pas une intention.",
            notes="Faire lire les deux phrases à voix haute : elles se prononcent "
                  "presque pareil, et la différence de sens est totale. C'est le même "
                  "mécanisme que le « e » de « allée », dans l'autre sens.")

    d.declencheur(
        'Écriture', "Vous arrêtez le cours du soir. "
                    "Trois phrases, pas une de plus.",
        image=img('note-remise-main.jpg'),
        pistes=[
            "Phrase 1 : le mot « abandonner » et le nom exact du cours.",
            "Phrase 2 : la date à partir de laquelle l'abandon prend effet.",
            "Phrase 3 : le motif, court et général.",
            "Et une quatrième, facultative : je souhaiterais me réinscrire plus tard.",
        ],
        notes="Vingt minutes d'écriture individuelle. Passer dans les rangées. Ne "
              "corriger que trois choses : le mot « abandonner », la date, et la "
              "longueur. Le reste attend E2.")

    d.regle("Le mot fait peur, et c'est lui qu'il faut écrire",
            "Un abandon annoncé avant la date limite ne laisse aucune trace "
            "négative. Un cours qu'on cesse de fréquenter, si.",
            precision="Le personnel entend ce mot dix fois par semaine et "
                      "n'y met aucun jugement.",
            notes="Dernière règle du bloc D. Beaucoup d'élèves du groupe sont dans cette "
                  "situation sans l'avoir dite. La séance est parfois l'occasion d'une "
                  "démarche réelle : le proposer, sans insister.")

    d.billet(
        "Écrivez votre note complète : les six lignes, avec le passé composé "
        "et le futur.",
        exemples=[
            "Vérifiez l'accord du participe passé avec être.",
            "Vérifiez qu'il n'y a pas de « s » au futur.",
        ],
        notes="Ramasser et annoter. Ces billets deviennent la production écrite de E2 : "
              "les rendre au début de la séance, pour que chacun parte d'un texte déjà "
              "relu une fois.")

    return d.save(dossier)
