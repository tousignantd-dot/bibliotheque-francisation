# -*- coding: utf-8 -*-
"""A2 · Quand les lettres mentent : ch, x, sh
Bloc A « Je découvre » · couleur indigo · 75 min. Graphie-phonie.
Source : exercice `prGraphie` et sa mini-leçon « Quand les lettres mentent :
ch, x, sh ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Quand les lettres mentent : ch, x, sh",
        chapeau="Tu entends un mot à la radio, tu vas le chercher dans le "
                "dictionnaire, et il n'y est pas : tu l'as écrit comme tu "
                "l'as entendu. Trois cas expliquent presque tous ces échecs.",
        duree='75 minutes')

    d.titre(notes="Deuxième séance du bloc A. Commencer par faire écrire « une "
                  "chronique » sous la dictée, sans rien annoncer. Beaucoup écriront "
                  "« une cronique ». C'est le point de départ de la séance, et il vaut "
                  "mieux qu'une explication.")

    d.objectifs([
        "reconnaître les lettres ch qui se disent comme un k ;",
        "reconnaître la lettre x qui se dit comme un s ;",
        "reconnaître sh et sch, qui se disent comme un ch ;",
        "retrouver un mot entendu dans un dictionnaire ou un moteur de "
        "recherche.",
    ], notes="Le quatrième objectif est le vrai. Les trois autres ne servent qu'à lui : "
             "on n'apprend pas ces graphies pour elles-mêmes, on les apprend pour "
             "pouvoir chercher un mot qu'on vient d'entendre.")

    d.declencheur(
        'Observation', "Comment écrirais-tu ces mots que tu entends ?",
        pistes=[
            "Le premier mot du module : « une chronique ». Avec un c ou un ch ?",
            "Le nombre « soixante » : où est le son du s ?",
            "Le dessin qui accompagne une explication : « un schéma ».",
            "As-tu déjà cherché un mot sans le trouver, à cause de ça ?",
        ],
        notes="Laisser trois ou quatre propositions au tableau avant de corriger. "
              "L'erreur écrite au tableau se retient mieux que la règle donnée "
              "d'avance.")

    d.tableau('Analyse', "Trois cas où l'écriture trompe l'oreille",
              ['Ce qu\'on écrit', 'Ce qu\'on entend'],
              [["une chronique, la technique", "les lettres ch se disent comme un k"],
               ["un chœur, la psychologie", "les lettres ch se disent comme un k"],
               ["dix, six, soixante, Bruxelles", "la lettre x se dit comme un s"],
               ["un shérif, un short", "les lettres sh se disent comme un ch"],
               ["un schéma", "les lettres sch se disent comme un ch"]],
              cle=0,
              note="Le programme du niveau 6 nomme exactement ces trois cas, et rien d'autre.",
              notes="Diapositive à photographier. Lire chaque exemple à voix haute et "
                    "le faire répéter avant de passer à la ligne suivante. Ne pas "
                    "expliquer l'étymologie : ça n'aide personne à écrire.")

    d.regle("Les lettres ch qui se disent comme un k",
            "Un mot savant, et le ch se durcit : chronique, technique, psychologie.",
            precision="Ce sont presque tous des mots venus du grec, et il y en a "
                      "partout dans les médias. Le repère : un mot un peu savant, "
                      "souvent avec un y ou un ph tout près. Attention, c'est "
                      "l'exception et non la règle : chercher, chaque, chose gardent "
                      "le son ordinaire de chat.",
            notes="Diapositive à photographier. Faire chercher trois autres mots du même "
                  "type par le groupe : chorale, orchestre, archéologie. Les écrire.")

    d.regle("La lettre x qui se dit comme un s",
            "Dix, six et soixante n'ont pas le x de taxi.",
            precision="Et le nombre dix change encore selon ce qui le suit : dix tout "
                      "seul finit par le son s ; dix dollars perd la consonne "
                      "finale ; dix ans la fait entendre comme un z. Trois "
                      "prononciations pour le même mot écrit, et le groupe les emploie "
                      "déjà sans le savoir.",
            notes="Diapositive à photographier. Faire dire à voix haute : dix, dix "
                  "dollars, dix ans, dix jours. L'oreille du groupe a raison avant que "
                  "la règle soit énoncée ; le dire, ça rassure.")

    d.pratique('Discrimination', "Quel son entends-tu ?",
               "Écoutez chaque mot et dites : comme un k, comme un s, ou comme un ch.", [
        ("une chronique", "comme un k"),
        ("la technique", "comme un k"),
        ("la psychologie", "comme un k"),
        ("dix", "comme un s"),
        ("soixante", "comme un s"),
        ("Bruxelles", "comme un s"),
        ("un schéma", "comme un ch"),
        ("un shérif", "comme un ch"),
    ], corrige=True, cols=2,
       notes="Prononcer chaque mot deux fois, puis laisser le groupe répondre à voix "
             "haute avant d'afficher la correction. L'exercice existe aussi en version "
             "interactive, avec l'audio : le refaire seul en devoir.")

    d.piege("Croire que le ch se durcit toujours",
            "Je cherche une crose dans le catalogue.",
            "Je cherche une chose dans le catalogue.",
            "Les lettres ch se disent comme un k dans une petite famille de mots "
            "savants seulement. Dans les mots de tous les jours - chercher, chaque, "
            "chose, chemin, chaud - le son reste celui de chat. Un élève qui vient "
            "d'apprendre la règle a tendance à l'appliquer partout pendant une "
            "semaine : c'est normal, et ça passe.",
            notes="Piège observé chaque fois. Le nommer d'avance évite qu'un élève se "
                  "décourage quand il l'entend chez lui.")

    d.cartes("Retrouver un mot qu'on vient d'entendre", "La méthode en trois essais", [
        ("J'écris ce que j'entends",
         "premier essai, tout simple : cronique, chema, sis."),
        ("Je change la première consonne",
         "un c peut cacher un ch, un s peut cacher un x ou un sc."),
        ("Je pense au genre du mot",
         "un mot savant de la radio ? essaie ch. Un nombre ? essaie x."),
        ("Je demande le mot entier",
         "à un collègue, au professeur, ou en écrivant la phrase complète."),
    ], notes="C'est la stratégie de niveau 6 : on ne demande pas de deviner "
             "l'orthographe, on demande de savoir quoi essayer. La faire écrire dans "
             "le cahier.")

    d.billet(
        "Écris un mot que tu as entendu cette semaine et que tu n'as pas su écrire.",
        exemples=[
            "Écris-le comme tu l'as entendu, ce n'est pas une faute.",
            "On les cherchera ensemble au début de la prochaine séance.",
        ],
        notes="Deux minutes. Ramasser les billets et ouvrir A3 avec deux ou trois de "
              "ces mots : c'est cinq minutes bien employées et ça montre que les "
              "billets servent à quelque chose.")

    return d.save(dossier)
