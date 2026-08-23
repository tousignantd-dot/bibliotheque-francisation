# -*- coding: utf-8 -*-
"""D1 · Ça ne prouve rien, ton comptage
Bloc D « Défi 3 » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf`, `t3anim` et `t3conc`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-classe' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Ça ne prouve rien, ton comptage",
        chapeau="Deux coéquipiers ne s'entendent plus, et aucun des deux n'a "
                "tort. Animer, c'est reformuler jusqu'à ce que chacun se "
                "reconnaisse — et découvrir que le désaccord était plus "
                "étroit qu'il ne paraissait.",
        duree='75 minutes')

    d.titre(notes="Première des deux séances du Défi 3, et la plus vivante du module. "
                  "Prévoir du temps pour le jeu de rôle : c'est là que la classe "
                  "apprend, pas dans les tableaux.")

    d.objectifs([
        "reconnaître les six gestes de parole de la personne qui anime ;",
        "reformuler la position de quelqu'un pour qu'il la corrige ;",
        "accorder un point avec bien que ou même si, puis maintenir le sien ;",
        "fermer une rencontre sur des décisions vérifiées à voix haute.",
    ], notes="Le deuxième objectif est celui du module entier. Les autres l'outillent.")

    d.declencheur(
        'Observation', "Deux positions, et personne n'a tort",
        image=IMG + 'jeune-arbre-tuteurs.jpg',
        pistes=[
            "L'un veut compter les arbres de deux rues, samedi matin.",
            "L'autre dit que le nombre ne mesure pas ce qu'on cherche.",
            "Qui a raison ? Et est-ce la bonne question ?",
            "Que feriez-vous si vous animiez cette rencontre ?",
        ],
        notes="Laisser la classe prendre parti trois minutes, puis poser la troisième "
              "piste. La bonne question n'est pas qui a raison : c'est sur quoi "
              "porte exactement le désaccord.")

    d.dialogue('Dialogue · 1 de 4', "Elle ouvre, il propose", [
        ("NEUSA", "Il est sept heures cinq, on a quarante minutes. Je rappelle où on en est : on cherche pourquoi certaines rues sont plus chaudes.", True),
        ("YOUSSOUF", "Samedi matin, on descend la rue des Ormes et la rue Bellechasse, et on compte les arbres. Un côté chacun.", True),
        ("MIGUEL", "Franchement, ça ne prouve rien, ton comptage.", True),
        ("NEUSA", "Attends, Miguel. Youssouf, avant qu'on discute : tu comptes quoi exactement ?", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Deux gestes en quatre répliques : l'ouverture, et la retenue d'une "
             "réponse le temps que la proposition soit comprise. Les faire nommer.")

    d.dialogue('Dialogue · 2 de 4', "Elle reformule les deux", [
        ("NEUSA", "Je reformule, et vous me dites si je me trompe. Youssouf, tu dis qu'une donnée que nous avons prise nous-mêmes vaut mieux qu'un chiffre repris ailleurs.", True),
        ("YOUSSOUF", "C'est ça. Et on est les seuls à être allés voir.", True),
        ("NEUSA", "Miguel, tu dis que compter des troncs ne mesure pas ce qu'on cherche, et qu'un chiffre qui ne répond pas à la question est un chiffre perdu.", True),
        ("MIGUEL", "C'est exactement ça. Je ne suis pas contre aller marcher. Je suis contre compter la mauvaise chose.", True),
    ], notes="Le cœur du module. Faire remarquer que les deux disent « c'est ça » : "
             "c'est la preuve que la reformulation est réussie, et c'est ce qui "
             "désamorce.")

    d.dialogue('Dialogue · 3 de 4', "Le désaccord rétrécit", [
        ("NEUSA", "Alors écoutez ce que je viens d'entendre : vous n'êtes pas en désaccord sur le fait d'y aller. Vous êtes en désaccord sur ce qu'on note en y allant.", True),
        ("MIGUEL", "Bien que ce soit plus long, on pourrait noter autre chose. Par exemple, à chaque coin de rue, est-ce que le trottoir est à l'ombre ou au soleil.", True),
        ("NEUSA", "Répète ça, Miguel, je le note. L'ombre au sol, à une heure fixe, à des endroits fixes.", True),
        ("YOUSSOUF", "Même si je trouve qu'on complique, je suis d'accord. On note les deux.", True),
    ], notes="Deux concessions coup sur coup, une avec le subjonctif et une avec "
             "l'indicatif. Les écrire au tableau : elles servent d'exemples pour "
             "l'exercice de la fin.")

    d.dialogue('Dialogue · 4 de 4', "Elle ferme sur des décisions", [
        ("NEUSA", "Je résume les décisions, et Youssouf, tu vérifies tes notes pendant que je parle.", True),
        ("NEUSA", "Un : on y va samedi à dix heures, pas à neuf, parce que l'ombre à neuf heures ne veut rien dire.", True),
        ("NEUSA", "Deux : à chaque coin, on note le nombre d'arbres et si le trottoir est à l'ombre. Trois : Miguel écrit à Perrine.", True),
        ("YOUSSOUF", "Tout y est. Et il est sept heures trente-cinq.", True),
    ], notes="La fermeture, et le détail qui compte : c'est une autre personne qui "
             "vérifie. Deux minutes, et personne ne sort avec une version "
             "différente.")

    d.tableau('Analyse', "Six gestes, six phrases",
              ['Le geste', 'La phrase toute prête'],
              [["Ouvrir",
                "Je rappelle où on en est. Il nous reste quarante minutes."],
               ["Donner la parole",
                "Youssouf, tu voulais commencer."],
               ["Faire préciser",
                "Tu comptes quoi, exactement ?"],
               ["Reprendre la parole",
                "Je t'arrête une seconde, Miguel n'a pas répondu."],
               ["Reformuler",
                "Je reformule, et vous me dites si je me trompe."],
               ["Fermer",
                "Je résume les décisions ; vérifie tes notes."]],
              cle=0,
              notes="Diapositive à photographier, et la plus utile du module. Faire "
                    "recopier les six phrases : elles s'emploient telles quelles.")

    d.regle("Bien que veut le subjonctif, même si veut l'indicatif",
            "Bien que ce soit plus long. Même si c'est plus long. Le sens "
            "est le même ; la construction ne l'est pas.",
            precision="Une concession accorde un point à l'autre avant de "
                      "maintenir sa position. Elle appelle toujours une suite : "
                      "sans elle, vous n'avez pas concédé, vous avez changé d'avis.",
            notes="Diapositive à photographier. L'erreur numéro un du niveau est "
                  "« même si ce soit » : l'écrire au tableau barrée, une fois.")

    d.pratique('Grammaire', "Accordez, puis maintenez",
               "Complétez avec bien que ou même si, et le bon mode.", [
        ("___ ce ___ (être) plus long, on note l'ombre.", "Bien que ce soit"),
        ("___ je ___ (trouver) qu'on complique, je suis d'accord.", "Même si je trouve"),
        ("___ nous ___ (avoir) trois semaines, c'est serré.", "Bien que nous ayons"),
        ("___ le chiffre ___ (venir) de la ville, on cite la date.", "Même si le chiffre vient"),
        ("___ ça ___ (prendre) deux heures, ça en vaut la peine.", "Même si ça prend"),
    ], corrige=True,
       notes="Faire dire la suite à chaque fois : « …mais je maintiens que… ». Sans "
             "la suite, la concession n'existe pas.")

    d.billet(
        "Écrivez une phrase qui accorde un point à quelqu'un et maintient le vôtre.",
        exemples=[
            "Commencez par bien que ou par même si.",
            "N'oubliez pas ce qui vient après la virgule.",
        ],
        notes="Devoir concret, et répétition du jeu de rôle du bloc E. Les phrases "
              "reçues qui s'arrêtent à la virgule montrent exactement qui n'a pas "
              "compris.")

    return d.save(dossier)
