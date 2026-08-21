# -*- coding: utf-8 -*-
"""C2 · Le décor et l'évènement.
Bloc C « Défi 2 » · couleur ambre · 75 min. Écriture.
Source : exercice `t2recit` et sa mini-leçon.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-rendezvous/images/')


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Le décor et l'évènement",
        chapeau="L'imparfait plante le décor, le passé composé fait avancer "
                "l'histoire. Deux temps, deux métiers — et un récit tient "
                "sur eux deux, sans rien d'autre.",
        duree='75 minutes')

    d.titre(notes="Rendre les billets de C1 et en lire trois à voix haute. Souligner au "
                  "tableau les verbes employés : la classe verra d'elle-même que les deux "
                  "temps sont déjà là, mélangés.")

    d.objectifs([
        "former l'imparfait à partir du « nous » du présent ;",
        "former le passé composé, avec avoir et avec être ;",
        "choisir le temps selon qu'on décrit ou qu'on raconte ;",
        "employer les deux dans la même phrase.",
    ])

    d.declencheur(
        'Observation', "« Je montais l'escalier quand la tête m'a tourné. » Deux "
                       "temps dans une phrase : pourquoi ?",
        image=IMG + 'salle-attente.jpg',
        pistes=[
            "Lequel des deux dure ?",
            "Lequel arrive d'un coup ?",
            "Que se passerait-il si les deux étaient au passé composé ?",
            "Et si les deux étaient à l'imparfait ?",
        ],
        notes="Faire produire les deux versions fautives à voix haute. Entendre « je suis "
              "monté quand la tête m'a tourné » suffit à sentir ce qui cloche.")

    d.regle("L'imparfait décrit, le passé composé raconte",
            "« Je me levais et tout tournait » — puis « j'ai dû m'asseoir ».",
            precision="L'imparfait n'a ni début ni fin visibles : c'était comme ça, ça se "
                      "répétait. Le passé composé, lui, est un fait, une fois, souvent "
                      "daté — et c'est lui qui fait agir un médecin.",
            notes="Diapositive à photographier. C'est la règle centrale du bloc C.")

    d.cartes("Comment ils se forment", "Deux recettes courtes", [
        ("L'imparfait",
         "Le radical du « nous » du présent, plus -ais, -ais, -ait, -ions, -iez, -aient. "
         "nous dorm-ons donne je dormais"),
        ("Le seul irrégulier",
         "être donne j'étais. Tous les autres suivent la règle, même faire : nous fais-ons donne je faisais."),
        ("Le passé composé",
         "avoir ou être au présent, plus le participe passé. j'ai dormi · je suis tombé"),
        ("L'accord avec être",
         "Le participe s'accorde avec le sujet : elle est tombée, ils sont allés."),
    ], notes="Le radical du « nous » est la clé : le faire chercher à voix haute pour cinq "
             "verbes avant de continuer.")

    d.tableau('Les verbes qui prennent être', "Ceux du module, justement",
              ['Famille', 'Exemples'],
              [["Le déplacement", "aller, venir, entrer, sortir, monter, partir, arriver, tomber"],
               ["Le changement d'état", "naître, mourir, devenir, rester"],
               ["Tous les pronominaux", "se lever, s'asseoir, se tenir, se sentir"],
               ["Dans ce module", "je suis tombé · je me suis assis · je me suis levé"]],
              cle=0,
              notes="En santé, ce sont justement les verbes utiles. Les apprendre avec "
                    "être dès le départ évite de les corriger pendant des mois.")

    d.piege("Oublier « être » avec un verbe pronominal",
            "« Je m'ai levé trop vite. »",
            "« Je me suis levé trop vite. »",
            "Tous les verbes pronominaux prennent être, sans exception : je me suis levé, "
            "je me suis assis, je me suis tenu au mur. C'est l'erreur la plus fréquente du "
            "récit de symptômes.",
            notes="Faire répéter les trois formes justes trois fois, en chœur. C'est "
                  "mécanique, et ça marche.")

    d.pratique('Écriture', "Imparfait ou passé composé ?",
               "Le verbe est entre parenthèses.", [
        ("Au début, ça ___ (arriver) une fois par semaine.", "arrivait"),
        ("Le mois dernier, j'___ (avoir) trois étourdissements.", "ai eu"),
        ("Avant, je ___ (jouer) au soccer tous les dimanches.", "jouais"),
        ("J'___ (arrêter) le soccer au mois d'avril.", "ai arrêté"),
        ("Je ___ (monter) l'escalier quand la tête m'a tourné.", "montais"),
        ("La semaine dernière, j'___ (devoir) m'asseoir.", "ai dû"),
        ("Quand ça a commencé, je ___ (dormir) très mal.", "dormais"),
        ("Ce matin-là, je ___ (se tenir) au mur dix secondes.", "me suis tenu"),
    ], corrige=True, cols=2,
       notes="Faire justifier chaque choix par un repère : une date ou un nombre de fois "
             "appelle le passé composé ; « avant », « d'habitude », « tous les jours » "
             "appellent l'imparfait.")

    d.pratique('Production', "Quatre phrases de récit",
               "Sur un problème vrai ou inventé, dans l'ordre.", [
        ("Le début, au passé composé.", "Ça a commencé au mois de janvier."),
        ("Le décor, à l'imparfait.", "Je marchais et mon genou faisait mal."),
        ("Un fait daté, au passé composé.", "La semaine dernière, j'ai dû m'arrêter."),
        ("Aujourd'hui, au présent.", "Maintenant, ça fait mal tous les jours."),
    ], corrige=True,
       notes="Circuler pendant l'écriture. Corriger le temps à voix basse, individuellement "
             "— c'est là que la règle entre vraiment.")

    d.billet(
        "Continuez votre récit de C1 : ajoutez ce qui a changé et où vous en êtes.",
        exemples=[
            "Une phrase au passé composé, avec une date ou un nombre de fois.",
            "Une phrase au présent, qui dit comment c'est aujourd'hui.",
        ],
        notes="Avec les deux phrases de C1, le récit fait maintenant quatre phrases. Le "
              "dire au groupe : il reste une séance pour le finir.")

    return d.save(dossier)
