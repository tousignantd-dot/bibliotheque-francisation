# -*- coding: utf-8 -*-
"""B2 · Les cinq parties, et la phrase qui les ouvre
Bloc B « Défi 1 · La réunion de production » · couleur teal · 75 min.
Source du module : exercice `t1plan`, mini-leçon `t1plan`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='teal',
        titre="Les cinq parties, et la phrase qui les ouvre",
        chapeau="Une présentation de projet suit presque toujours le même "
                "plan, quel que soit le métier. Ce n'est pas une convention : "
                "c'est l'ordre dans lequel les questions montent dans la tête "
                "de celui qui écoute.",
        duree='75 minutes')

    d.titre(notes="Séance d'analyse. On reprend la présentation d'hier, non plus pour "
                  "la comprendre mais pour voir comment elle est faite. C'est le "
                  "passage de l'écoute au modèle.")

    d.objectifs([
        "nommer les cinq mouvements d'une présentation de projet ;",
        "reconnaître la phrase qui ouvre chacun d'eux ;",
        "expliquer pourquoi on annonce le nombre d'étapes avant de les dire ;",
        "expliquer pourquoi on nomme ses risques soi-même.",
    ], notes="Les deux derniers objectifs sont des gestes de présentateur, pas des "
             "points de langue. Ils valent autant que le reste.")

    d.declencheur(
        'Rappel', "Dans quel ordre monsieur Cormier a-t-il parlé ?",
        pistes=[
            "Qu'a-t-il dit en premier : le prix, ou le but ?",
            "Quand a-t-il donné ses dates ?",
            "À quel moment a-t-il parlé de ce qui pourrait mal aller ?",
            "Est-ce qu'un autre ordre aurait été possible ?",
        ],
        notes="Faire reconstituer l'ordre au tableau, à partir des billets de la veille. "
              "Ne pas corriger tout de suite : laisser deux versions concurrentes "
              "s'installer, puis trancher avec le tableau qui suit.")

    d.tableau('Analyse', "Les cinq mouvements, et leur phrase d'ouverture",
              ['Le mouvement', 'Ce que monsieur Cormier a dit'],
              [["L'objectif", "« L'objectif tient en une phrase : ramener l'attente sous vingt minutes. »"],
               ["Les étapes", "« Il y en a quatre. D'abord, on mesure... »"],
               ["L'échéancier", "« Les relevés commencent le 8 septembre. »"],
               ["Le budget", "« L'essai coûte quatre cents dollars. »"],
               ["Les risques", "« Il y en a trois, et je préfère les nommer moi-même. »"]],
              cle=0,
              note="Puis la sortie : « En somme : on mesure, on trace, on essaie, on installe. »",
              notes="Diapositive à photographier. C'est l'exercice `t1plan` du module "
                    "sous forme de tableau. Faire cacher la colonne de droite et "
                    "retrouver les phrases de mémoire.")

    d.regle("L'objectif tient en une phrase",
            "S'il en prend trois, c'est qu'il y a trois objectifs.",
            precision="C'est le test le plus rapide d'un projet mal préparé. Quand "
                      "l'objectif ne se dit pas en une phrase, ce n'est pas la phrase "
                      "qui est trop courte : c'est le projet qui n'a pas encore choisi. "
                      "Écrivez la vôtre avant tout le reste, et récrivez-la jusqu'à ce "
                      "qu'elle tienne.",
            notes="Diapositive à photographier. Faire écrire une phrase d'objectif à "
                  "partir du billet de la séance A1. Ramasser deux ou trois exemples et "
                  "les récrire au tableau avec le groupe.")

    d.cartes('Analyse', "Deux gestes qui changent tout", [
        ("Annoncer le nombre", "« Il y en a quatre. » Cinq mots qui donnent une carte à l'auditeur : il sait combien de temps il en a, il peut cocher, il ne se demande pas si ça va durer."),
        ("Le corollaire", "Annoncez quatre étapes, donnez-en quatre. Une cinquième surprise défait tout le bénéfice."),
        ("Nommer ses risques", "Un projet présenté sans risque a l'air préparé par quelqu'un qui n'a pas réfléchi. On lui trouvera ses risques de toute façon, et depuis la salle."),
        ("Le bon nombre", "Trois. Un seul a l'air d'une concession polie ; six ont l'air d'un projet auquel on ne croit pas soi-même."),
    ], notes="Le deuxième point est celui qu'on oublie. Faire raconter au groupe une "
             "présentation où quelqu'un avait annoncé trois points et en avait fait "
             "sept : tout le monde en a un exemple.")

    d.pratique('Pratique', "À quelle partie appartient cette phrase ?",
               "Dites de quel mouvement chaque phrase fait partie.", [
        ("« On charge dix-neuf camions par jour, contre quatorze l'an dernier. »", "le contexte de l'objectif"),
        ("« Un mois à l'essai, sans rien acheter. »", "les étapes"),
        ("« Du 13 octobre au 14 novembre. »", "l'échéancier"),
        ("« Entre onze et treize mille dollars, estimé. »", "le budget"),
        ("« Un piéton distrait peut se retrouver dans une zone de manoeuvre. »", "les risques"),
        ("« On mesure, on trace, on essaie, on installe. »", "le résumé final"),
    ], corrige=True,
       notes="Forme papier de l'exercice `t1plan`. Faire répondre sans regarder le "
             "tableau précédent : c'est le moment où l'on vérifie que le plan est "
             "entré.")

    d.piege('Présentation',
            "commencer par le prix",
            "commencer par l'objectif",
            "Une présentation qui s'ouvre sur un montant fait entendre une demande "
            "d'argent, et la salle passe le reste du temps à chercher comment dire "
            "non. Le même montant, annoncé après l'objectif et les étapes, s'entend "
            "comme le coût d'une chose qu'on a déjà comprise. Ce n'est pas de la "
            "manipulation : c'est l'ordre dans lequel les questions arrivent.",
            notes="Beaucoup d'élèves ont l'habitude inverse, par souci d'honnêteté : "
                  "annoncer le coût d'emblée pour ne rien cacher. Reconnaître "
                  "l'intention et montrer qu'elle se dessert.")

    d.billet(
        "Écrivez l'objectif de votre projet, en une seule phrase.",
        exemples=[
            "Commencez par « L'objectif tient en une phrase : ... »",
            "Une seule idée. Si vous en avez deux, choisissez.",
            "Relisez-la à voix haute : est-ce qu'elle tient d'un souffle ?",
        ],
        notes="Ramasser. La séance C2 partira de ces phrases : celles qui n'en sont "
              "pas encore une seront récrites en classe.")

    return d.save(dossier)
