# -*- coding: utf-8 -*-
"""D2 · Mettre en avant, et demander fermement
Bloc D « Défi 3 · Une opération que je n'ai pas faite » · couleur ambre · 90 min.
Source : exercices `t3emph`, `t3subj` et `t3lettre`, et leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre='Mettre en avant, et demander fermement',
        chapeau="Deux tournures, et une lettre de réclamation devient "
                "lisible par quelqu'un de pressé : la mise en relief et le "
                "subjonctif après un verbe de volonté.",
        duree='90 minutes')

    d.titre(notes="Séance de grammaire au service de l'écrit du bloc E. Annoncer la "
                  "lettre dès l'ouverture : tout ce qui est fait ici y sert.")

    d.objectifs([
        "mettre un mot en avant avec c'est... qui et c'est... que ;",
        "annoncer avant de dire avec ce qui... c'est ;",
        "employer le subjonctif après je demande que et il faut que ;",
        "reconnaître les faux amis qui veulent l'indicatif.",
    ], notes="Le quatrième objectif est celui qui économise le plus de fautes : "
             "« j'espère que » prend l'indicatif, et presque tout le monde s'y trompe.")

    d.declencheur(
        'Observation', "À l'oral, on appuie sur un mot avec la voix. À l'écrit ?",
        pistes=[
            "Comment fait-on entendre le mot important dans une lettre ?",
            "Le souligner suffit-il ?",
            "Connais-tu des phrases qui commencent par « ce que » ?",
            "Que dirais-tu pour insister sur un montant ?",
        ],
        notes="La deuxième question mérite une vraie réponse : souligner se voit, mais "
              "ne change pas la phrase. La mise en relief, oui.")

    d.tableau('Analyse', "Trois façons de mettre en avant",
              ['La tournure', "Ce qu'elle met devant"],
              [["c'est... qui", "celui qui fait l'action"],
               ["c'est... que", 'tout le reste : objet, date, lieu'],
               ["ce qui..., c'est", 'un sujet, annoncé avant'],
               ["ce que..., c'est", 'un complément, annoncé avant']],
              cle=0,
              note="Qui ne s'élide jamais : c'est moi qui ai, jamais qu'ai.",
              notes="Diapositive à photographier. La note est la faute d'orthographe la "
                    "plus fréquente de la séance.")

    d.regle("Le verbe s'accorde avec le mot mis en avant",
            "C'est moi qui ai appelé. C'est nous qui avons écrit.",
            precision="Le verbe ne s'accorde pas avec « c'est » mais avec le pronom "
                      "qu'on a fait passer devant. Et la virgule avant « c'est », dans "
                      "« ce qui m'inquiète, c'est le délai », n'est pas décorative : "
                      "elle marque la pause qui fait tout le travail à l'oral.",
            notes="Diapositive à photographier. Faire lire les deux exemples à voix "
                  "haute avec la pause : elle s'entend.")

    d.pratique('Application', "Récrivez en mettant le groupe en avant",
               "La tournure est indiquée.", [
        ("L'agent a bloqué la carte. (c'est... qui)", "C'est l'agent qui a bloqué la carte."),
        ("J'ai appelé le quinze mars. (c'est... que)", "C'est le quinze mars que j'ai appelé."),
        ("Le délai m'inquiète. (ce qui... c'est)", "Ce qui m'inquiète, c'est le délai."),
        ("Je demande un écrit. (ce que... c'est)", "Ce que je demande, c'est un écrit."),
        ("J'ai signalé l'opération moi-même. (c'est... qui)", "C'est moi qui ai signalé l'opération."),
    ], corrige=True,
       notes="Faire écrire au tableau. Le cinquième est le seul qui pose problème, et "
             "c'est à cause de l'élision.")

    d.regle("C'est le mot d'avant qui décide du subjonctif",
            "Je demande que, il faut que, à condition que, avant que, bien que : "
            "subjonctif, sans exception.",
            precision="Ce n'est pas le doute qui commande, c'est le déclencheur. "
                      "« Bien que la carte soit restée dans mon portefeuille » est "
                      "parfaitement certain et prend quand même le subjonctif. À "
                      "l'inverse, « j'espère que » est bien plus incertain et prend "
                      "l'indicatif.",
            notes="Diapositive à photographier. Faire copier les deux listes, "
                  "déclencheurs et faux amis, dans le cahier.")

    d.tableau('Analyse', "Ce qui déclenche, ce qui ne déclenche pas",
              ['Subjonctif', 'Indicatif'],
              [['je demande que', "j'espère que"],
               ['il faut que', 'je pense que'],
               ['à condition que', 'parce que'],
               ['avant que', 'après que'],
               ['bien que', 'puisque']],
              cle=0,
              notes="Diapositive à photographier. Faire remarquer la paire avant que / "
                    "après que : la chose est faite dans un cas, pas encore dans "
                    "l'autre.")

    d.pratique('Application', "Mettez le verbe au subjonctif présent",
               "Le verbe est entre parenthèses.", [
        ("Je demande que le montant ___ (être) retiré de mon relevé.", "soit"),
        ("Il faut que vous ___ (faire) bloquer la carte aujourd'hui.", "fassiez"),
        ("Je souhaite que ma contestation ___ (avoir) une réponse écrite.", "ait"),
        ("J'accepte, à condition que le taux ___ (rester) fixe.", "reste"),
        ("Écrivez avant que le délai de trente jours ___ (finir).", "finisse"),
        ("Bien que la carte ___ (être) restée chez moi, l'achat a passé.", "soit"),
    ], corrige=True,
       notes="Le sixième surprend toujours : « bien que » avec un fait certain. C'est "
             "la meilleure preuve que le déclencheur commande, pas le sens.")

    d.piege('Le piège', "j'espère que le montant soit retiré",
            "j'espère que le montant sera retiré",
            "Espérer prend l'indicatif, souhaiter prend le subjonctif. Deux verbes "
            "voisins, deux modes. Et quand les deux verbes ont le même sujet, on "
            "n'emploie pas « que » du tout : « je veux obtenir une réponse », jamais "
            "« je veux que j'obtienne ».",
            notes="Faire produire les trois formes au tableau : j'espère que, je "
                  "souhaite que, je veux obtenir.")

    d.tableau('La lettre', "Six parties, six travaux",
              ['La partie', "Ce qu'on y écrit"],
              [["l'objet", 'motif, numéro de dossier, montant'],
               ['1er paragraphe', "ce qui s'est passé, et quand"],
               ['2e paragraphe', 'les faits qui appuient'],
               ['3e paragraphe', 'ce que je demande, pour quelle date'],
               ['la salutation', 'fermée, neutre, sans remerciement']],
              cle=0,
              notes="Diapositive à photographier. C'est le plan exact de la lettre du "
                    "bloc E, et il se recopie tel quel.")

    d.billet("Écris la première phrase de ta lettre, avec une mise en relief.",
             exemples=["Ce que je conteste, ce n'est pas le service, c'est une "
                       "opération de 780 $ que je n'ai pas faite."],
             notes="Trois minutes. Cette phrase-là est celle qui décide de la lecture "
                   "de toute la lettre : y consacrer le temps qu'il faut.")

    return d.save(dossier)
