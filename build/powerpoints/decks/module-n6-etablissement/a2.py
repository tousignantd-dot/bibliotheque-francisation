# -*- coding: utf-8 -*-
"""A2 · Quand la lettre ment : ch, x, sh
Bloc A « Je découvre » · couleur indigo · 75 min. Graphie-phonie.
Source : exercice `prGraphie` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Quand la lettre ment : ch, x, sh",
        chapeau="Vous entendez « psi-co-lo-gie » dans un bureau, vous "
                "l'écrivez comme vous l'avez entendu, et vous ne le trouvez "
                "nulle part. Trois cas seulement, et ils sont partout dans "
                "les noms de matières.",
        duree='75 minutes')

    d.titre(notes="Séance de prononciation. Elle est courte en contenu et longue en "
                  "répétition : prévoir au moins vingt minutes de répétition à voix "
                  "haute, en groupe puis individuellement.")

    d.objectifs([
        "reconnaître les lettres ch qui se disent comme un k ;",
        "reconnaître la lettre x qui se dit comme un s ;",
        "reconnaître les lettres sh et sch qui se disent comme un ch ;",
        "retrouver un mot dans un dictionnaire quand on ne l'a qu'entendu.",
    ], notes="Le quatrième objectif est le plus utile dans la vraie vie : c'est celui "
             "qui débloque un adulte devant un mot administratif entendu une fois.")

    d.declencheur(
        'Observation', "Un mot que vous avez entendu sans jamais le trouver écrit",
        pistes=[
            "Ça vous est-il déjà arrivé de chercher un mot et de ne pas le trouver ?",
            "Est-ce qu'il y a des lettres qui ne se disent pas dans votre langue ?",
            "Comment faites-vous, en général, quand un mot vous échappe ?",
        ],
        notes="Laisser trois minutes. Presque tout le monde a une histoire de mot "
              "introuvable. Ne pas donner la solution tout de suite.")

    d.tableau('Analyse', "Cas 1 · les lettres ch qui se disent comme un k",
              ['On écrit', 'On dit'],
              [["la psychologie", "psi-co-lo-gie"],
               ["une chronologie", "cro-no-lo-gie"],
               ["un orchestre", "or-kestre"],
               ["la technologie", "tec-no-lo-gie"],
               ["un écho", "é-co"]],
              cle=0,
              note="Des mots venus du grec, et les noms de matières en sont pleins.",
              notes="Faire répéter chaque mot deux fois. Insister ensuite sur "
                    "l'exception qui rassure : « chercher », « chaque », « chose » "
                    "gardent le son normal. Le k est l'exception, jamais la règle.")

    d.tableau('Analyse', "Cas 2 · la lettre x qui se dit comme un s",
              ['On écrit', 'On dit'],
              [["six", "sisse, tout seul"],
               ["six semaines", "si semaines, devant une consonne"],
               ["six ans", "siz ans, devant une voyelle"],
               ["dix", "disse, tout seul"],
               ["soixante", "soi-sante"]],
              cle=0,
              note="Trois nombres, entendus dix fois par rendez-vous.",
              notes="Le piège du nombre est le seul point difficile de la séance. Le "
                    "faire pratiquer avec des dates : six février, dix novembre, "
                    "six heures, dix heures.")

    d.tableau('Analyse', "Cas 3 · les lettres sh et sch qui se disent comme un ch",
              ['On écrit', 'On dit'],
              [["un schéma", "ché-ma"],
               ["un shampoing", "cham-poin"],
               ["un short", "chort"]],
              cle=0,
              note="Des mots courts, empruntés à l'anglais ou à l'allemand, et devenus tout à fait courants.",
              notes="« Un schéma » revient très souvent dans une brochure de "
                    "programme : c'est le dessin qui accompagne une explication. Le "
                    "faire répéter plus que les deux autres.")

    d.regle("Chercher avec la lettre écrite, pas avec le son entendu",
            "Quand un mot entendu ne se trouve pas, essayez ch à la place du k, et x à la place du s.",
            precision="Vous entendez « cronologie », vous cherchez « cronologie » : "
                      "rien. Vous essayez « chronologie » : vous le trouvez. Cette "
                      "seule habitude vaut des dizaines de mots par année.",
            notes="Diapositive à photographier. Faire l'essai en direct avec un "
                  "téléphone si le groupe en a un : l'effet est immédiat.")

    d.piege('Prononciation',
            "prononcer chaque ch comme dans chat",
            "reconnaître les mots savants",
            "« Technologie » dite avec le son de « chat » ne se comprend pas du "
            "tout, et l'interlocuteur ne devine pas. Ces mots-là sont peu "
            "nombreux : ils s'apprennent un par un, et la liste tient sur une "
            "carte.",
            notes="Dédramatiser tout de suite après : personne ne reprendra un adulte "
                  "qui dit « diz jours » au lieu de « di jours ». Ce qui compte, "
                  "c'est de reconnaître les formes à l'écoute.")

    d.pratique('Pratique', "Quel son entendez-vous ?",
               "Écoutez chaque mot. Comme un K, comme un S, ou comme un CH ?", [
        ("la psychologie", "comme un K"),
        ("une chronologie", "comme un K"),
        ("un orchestre", "comme un K"),
        ("six", "comme un S"),
        ("soixante", "comme un S"),
        ("un schéma", "comme un CH"),
        ("un shampoing", "comme un CH"),
        ("un short", "comme un CH"),
    ], corrige=True, cols=2,
       notes="Lire les mots soi-même, deux fois chacun, sans montrer l'écrit. Les "
             "élèves lèvent la main pour K, S ou CH. Puis afficher la correction et "
             "faire répéter le mot en le voyant écrit.")

    d.billet(
        "Écris deux mots de la séance et note à côté comment ils se disent.",
        exemples=[
            "Choisis ceux que tu risques d'employer au centre.",
            "Écris la prononciation à ta façon : personne ne te corrigera là-dessus.",
        ],
        notes="Trois minutes. Le but n'est pas l'alphabet phonétique, c'est de laisser "
              "une trace personnelle que l'élève relira. Accepter toutes les "
              "transcriptions.")

    return d.save(dossier)
