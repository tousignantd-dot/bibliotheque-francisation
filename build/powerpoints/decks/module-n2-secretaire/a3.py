# -*- coding: utf-8 -*-
"""A3 · Au, dans, à côté de.
Bloc A « Je découvre » · couleur teal · 75 min. Dernière séance de découverte.
Source : exercices `prImg` et `prOu`, mini-leçon « Dire où c'est, dans le
centre ».

Le lexique du programme, pour cette situation, commence par « Direction :
prépositions de lieu » et « Lieux : secrétariat, couloir, premier étage,
rez-de-chaussée ». Cette séance est donc écrite mot pour mot sur le
programme : trois petits mots, quatre lieux, et un immeuble qui se laisse
décrire.

Le point qui fait perdre un mois à tout le monde y est réglé : au Québec,
l'étage de la porte d'entrée est le rez-de-chaussée, et le premier étage est
au-dessus. Dans plusieurs pays, on compte autrement.
"""
import pathlib
from theme import Deck

IMG = (pathlib.Path(__file__).resolve().parents[4]
       / 'assets' / 'interactive' / 'module-n2-secretaire' / 'images')


def img(nom):
    """La photo si elle existe, sinon rien — voir a1.py."""
    chemin = IMG / (nom + '.jpg')
    return str(chemin) if chemin.exists() else None


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre="Au, dans, à côté de",
        chapeau="Dire où se trouve un endroit, dans un immeuble.",
        duree='75 minutes')

    d.titre(notes="Troisième séance. Commencer par demander : « Votre local est à quel "
                  "étage ? » Noter les réponses au tableau. Il y en a toujours deux "
                  "pour le même local, et c'est le sujet de la séance.")

    d.objectifs([
        "dire à quel étage se trouve un endroit ;",
        "employer au, dans, à côté de et en face de ;",
        "reconnaître les lieux du centre sur une photo ;",
        "poser la question « Où est… ? ».",
    ])

    d.declencheur(
        'Observation', "Où est-ce, dans le centre ?",
        image=img('lieu-couloir'),
        pistes=[
            "Qu'est-ce qu'on voit de chaque côté ?",
            "Comment s'appelle ce long passage ?",
            "Comment sait-on où est le local 214 ?",
            "Vous, comment avez-vous trouvé votre classe le premier jour ?",
        ],
        notes="La quatrième piste vaut la séance : presque personne n'a trouvé seul, et "
              "presque personne n'a demandé. C'est ce qu'on apprend ici.")

    d.regle("Le rez-de-chaussée, puis le premier étage.",
            "L'étage de la porte d'entrée n'est pas le premier.",
            precision="Au Québec, l'étage de l'entrée s'appelle le "
                      "<b>rez-de-chaussée</b>. Celui du dessus est le <b>premier "
                      "étage</b>, puis le <b>deuxième</b>. Un élève qui compte "
                      "autrement monte toujours un étage trop haut.",
            notes="Diapositive à photographier. Demander au groupe comment on compte "
                  "dans leur pays : la comparaison prend cinq minutes et évite six "
                  "semaines de malentendus.")

    d.tableau('Analyse · 1 de 2', "Trois petits mots, trois emplois",
              ["Le petit mot", "Ce qu'il sert à dire"],
              [["au", "l'étage : au rez-de-chaussée, au deuxième étage"],
               ["dans", "un endroit fermé : dans le couloir, dans le local"],
               ["à côté de", "tout près : à côté de l'entrée"],
               ["en face de", "de l'autre côté : en face de l'escalier"]],
              cle=1,
              note="On ne dit pas « en le deuxième étage » ni « sur le couloir ».",
              notes="Diapositive à photographier. Faire produire une phrase avec chaque "
                    "mot, en montrant du doigt la vraie direction dans le local.")

    d.tableau('Analyse · 2 de 2', "Le numéro du local dit son étage",
              ["Le local", "L'étage"],
              [["005", "le rez-de-chaussée"],
               ["108", "le premier étage"],
               ["214", "le deuxième étage"],
               ["302", "le troisième étage"]],
              cle=1,
              note="Le premier chiffre suffit : on le lit, et on monte.",
              notes="Diapositive à photographier. Vérifier une fois dans le vrai "
                    "immeuble, avec le groupe : c'est vrai dans presque tous les "
                    "centres de formation du Québec.")

    d.vocabulaire('Vocabulaire', "Les lieux du centre", [
        ("le rez-de-chaussée", "L'étage d'en bas, celui de la porte d'entrée."),
        ("un étage", "Un niveau de l'immeuble, au-dessus de l'entrée."),
        ("le couloir", "Le long passage entre les portes des classes."),
        ("un local", "La salle du cours. Elle porte un numéro sur la porte."),
        ("le secrétariat", "Le bureau où on demande les papiers."),
        ("un comptoir", "Le meuble haut où on parle à la personne du bureau."),
    ], notes="Diapositive à photographier. Six mots, six endroits réels : faire montrer "
             "chacun du doigt, depuis la porte du local.")

    d.pratique('Pratique · 1 de 2', "Complétez avec le bon petit mot",
               "Un seul mot par phrase.", [
        ("Le secrétariat est ___ rez-de-chaussée.", "au"),
        ("Mon local est ___ deuxième étage.", "au"),
        ("Les portes des classes sont ___ le couloir.", "dans"),
        ("Le comptoir est à ___ de l'entrée.", "côté"),
        ("L'escalier est en ___ du secrétariat.", "face"),
        ("Le local 214 est au ___ du couloir.", "bout"),
    ], corrige=True, cols=2,
       notes="Faire à l'oral d'abord, en groupe. Les deux dernières lignes sont les "
             "plus difficiles : « au bout du » et « en face de » ne se traduisent pas "
             "mot à mot.")

    d.pratique('Pratique · 2 de 2', "Notre centre, en six phrases",
               "Vingt minutes, à deux, debout dans le couloir.", [
        ("Étape 1", "A demande : « Excusez-moi, où est le secrétariat ? »"),
        ("Étape 2", "B répond avec l'étage, puis avec un repère."),
        ("Étape 3", "A demande : « Et le local 214 ? » avec un vrai numéro du centre."),
        ("Étape 4", "B répond, A répète, puis on échange les rôles."),
    ], cols=1,
       notes="Sortir vraiment du local. Cinq minutes de couloir valent trente minutes "
             "de diapositives pour cette séance-là.")

    d.billet(
        "Écrivez où se trouvent trois endroits de votre centre.",
        exemples=[
            "Le secrétariat est au rez-de-chaussée, à côté de l'entrée.",
            "Mon local est au deuxième étage.",
            "Les toilettes sont en face de l'escalier.",
        ],
        notes="Devoir court. Exiger le petit mot : une phrase sans « au » ou sans "
              "« à côté de » ne compte pas, c'est justement ce qu'on travaille.")

    return d.save(dossier)
