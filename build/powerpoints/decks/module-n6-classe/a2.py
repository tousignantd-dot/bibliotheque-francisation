# -*- coding: utf-8 -*-
"""A2 · Le mot qu'on ne trouve pas au dictionnaire
Bloc A « Je découvre » · couleur indigo · 75 min. Graphie-phonie.
Source du module : exercice `prGraphie` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Le mot qu'on ne trouve pas au dictionnaire",
        chapeau="Vous entendez un mot, vous l'écrivez comme vous l'avez "
                "entendu, et le catalogue de la bibliothèque ne trouve rien. "
                "Trois familles de lettres expliquent presque tous ces "
                "échecs.",
        duree='75 minutes')

    d.titre(notes="Séance de sons, mais elle sert une tâche précise : trouver "
                  "un document. Le dire d'entrée de jeu, sinon la séance a "
                  "l'air d'un exercice de prononciation détaché du reste.")

    d.objectifs([
        "reconnaître les lettres ch qui se disent comme un k ;",
        "reconnaître la lettre x qui se dit comme un s ;",
        "reconnaître sh et sch qui se disent comme un ch ;",
        "essayer la lettre muette quand un mot reste introuvable.",
    ], notes="Le savoir est commun à tout le niveau 6 : les huit modules du "
             "niveau portent cet exercice. Les mots, eux, changent d'un "
             "module à l'autre.")

    d.declencheur(
        'Observation', "Comment écrivez-vous le mot que vous venez d'entendre ?",
        pistes=[
            "Dites « cronomètre » et faites-le écrire au tableau.",
            "Combien de graphies différentes dans la classe ?",
            "Laquelle trouverait le mot dans un catalogue ?",
        ],
        notes="Faire écrire avant de montrer. La diversité des réponses est "
              "le meilleur argument de la séance, et elle rassure : tout le "
              "monde s'est trompé de la même façon.")

    d.tableau('Analyse', "Les lettres ch qui se disent comme un k",
              ['Ce qu\'on lit', 'Ce qu\'on entend'],
              [["le chlore", "clore, avec un k au début"],
               ["un chronomètre", "cro-no-mètre"],
               ["l'archéologie", "ar-ké-o-lo-gie"],
               ["le chaos", "ca-o, sans aucun souffle"],
               ["la technique", "tec-nique, comme technologie"]],
              cle=0,
              note="Des mots de science, venus du grec. Une petite liste, apprise une fois.",
              notes="Diapositive à photographier. Rassurer tout de suite : "
                    "« chercher », « chaque » et « chose » n'appartiennent pas "
                    "à cette famille.")

    d.tableau('Analyse', "La lettre x qui se dit comme un s",
              ['Ce qu\'on lit', 'Ce qu\'on entend'],
              [["six", "sisse, quand le mot est seul"],
               ["six sources", "si sources, devant une consonne"],
               ["six ans", "siz ans, devant une voyelle"],
               ["dix", "disse, puis di ou diz de la même façon"],
               ["soixante", "soi-sante, jamais soi-ksante"]],
              cle=0,
              note="Trois nombres seulement, mais ce sont ceux d'une échéance.",
              notes="Diapositive à photographier. Faire dire une date à voix "
                    "haute : « le six novembre » fait entendre les trois "
                    "formes en une phrase.")

    d.tableau('Analyse', "Les lettres sh et sch, comme un ch",
              ['Ce qu\'on lit', 'Ce qu\'on entend'],
              [["un schéma", "ché-ma, un seul souffle"],
               ["un shampoing", "cham-poin"],
               ["un short", "chort, à la française"]],
              cle=0,
              note="Des mots venus d'ailleurs, courts, et que rien ne signale à l'œil.",
              notes="« Un schéma » est le plus utile des trois ici : une page "
                    "d'information municipale en contient presque toujours un.")

    d.regle("Devant un mot introuvable, essayez la lettre muette",
            "Un k qui ne donne rien ? Essayez ch. Un s qui ne donne rien ? Essayez x.",
            precision="C'est un geste de recherche, pas un point de "
                      "grammaire. Il fait gagner un quart d'heure à chaque "
                      "fois qu'il sert, et il sert souvent.",
            notes="Diapositive à photographier. Faire essayer en direct dans "
                  "le catalogue de la bibliothèque si un poste est "
                  "disponible.")

    d.piege('Prononciation',
            "donner à tous les ch le souffle de chat",
            "apprendre la petite liste savante",
            "Prononcer « technique » avec le souffle de « chat » rend le mot "
            "méconnaissable, et personne ne devinera de quoi vous parlez. Ces "
            "mots-là se comptent sur les doigts d'une main et demie : une "
            "carte suffit à les tenir.",
            notes="Ne pas laisser croire que la liste est infinie. C'est "
                  "l'inquiétude qui fait abandonner, pas la difficulté.")

    d.pratique('Pratique', "Quelle famille ?",
               "Pour chaque mot, dites si les lettres marquées font k, s ou ch.", [
        ("le chlore", "comme k"),
        ("un chronomètre", "comme k"),
        ("l'archéologie", "comme k"),
        ("une orchidée", "comme k"),
        ("six", "comme s"),
        ("soixante", "comme s"),
        ("un schéma", "comme ch"),
        ("un short", "comme ch"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice `prGraphie` du module. En classe, dire le mot "
             "avant de le montrer : l'oreille doit travailler la première.")

    d.billet(
        "Écris deux mots de la séance et, à côté, ce qu'on entend.",
        exemples=[
            "Un mot avec ch, un mot avec x ou sh.",
            "Exemple : la technique · tec-nique",
        ],
        notes="Deux minutes. Ce billet sert surtout à vérifier que la "
              "consigne « ce qu'on entend » a été comprise : certains "
              "recopient le mot deux fois.")

    return d.save(dossier)
