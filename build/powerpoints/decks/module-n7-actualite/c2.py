# -*- coding: utf-8 -*-
"""C2 · Quand personne ne semble agir : la phrase passive
Bloc C « Défi 2 · L'article » · couleur ambre · 75 min.
Source : exercice `t2passif` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Quand personne ne semble agir : la phrase passive",
        chapeau="Lisez n'importe quel article : le communiqué a été publié, "
                "le local a été retenu, la décision sera prise. Personne n'y "
                "agit. Ce n'est pas un tic d'écriture, c'est un choix.",
        duree='75 minutes')

    d.titre(notes="Premier point de grammaire du Défi 2. Projeter d'abord l'article "
                  "du lendemain et faire compter les verbes : le groupe trouve seul "
                  "que presque tous sont au passif.")

    d.objectifs([
        "reconnaître une phrase passive à la lecture ;",
        "former le passif au passé composé et accorder le participe ;",
        "employer « par » quand l'auteur de l'action est nommé, et l'omettre sinon ;",
        "se demander, devant un passif sans « par », qui a réellement agi.",
    ], notes="Le quatrième objectif est de la lecture critique, pas de la grammaire. "
             "C'est pourtant lui qui justifie les trois autres.")

    d.declencheur(
        'Observation', "Qui a fait ça ?",
        pistes=[
            "« Le communiqué a été publié hier soir. » Par qui ?",
            "« Le local a été retenu par le comité. » Par qui ?",
            "Laquelle des deux phrases nomme le responsable ?",
            "Pourquoi l'autre ne le nomme-t-elle pas ?",
        ],
        notes="Ne pas donner la réponse à la quatrième piste. Les hypothèses des élèves "
              "- on ne le sait pas, ça n'a pas d'importance, ça arrange quelqu'un - sont "
              "toutes justes selon les cas.")

    d.tableau('Analyse', "Comment on la fabrique",
              ['La pièce', 'Ce que ça donne'],
              [["le verbe être, au temps voulu", "a été, sera, est"],
               ["le participe passé", "publié, retenu, pris, fixé"],
               ["au passé composé", "a été + participe passé"],
               ["la phrase active devient passive", "Le comité a retenu le local devient : le local a été retenu par le comité"]],
              cle=0,
              note="C'est le verbe être qui porte le temps. Le participe, lui, ne bouge pas.",
              notes="Diapositive à photographier. La dernière ligne se lit à voix haute "
                    "dans les deux sens, plusieurs fois.")

    d.regle("L'accord se fait avec le sujet",
            "Le sujet commande la terminaison du participe, jamais le complément.",
            precision="« La décision a été prise par le conseil » : le participe "
                      "s'accorde avec « la décision », féminin singulier, et non avec "
                      "« le conseil ». Regardez à gauche du verbe, pas à droite. C'est "
                      "l'erreur la plus fréquente et la plus facile à éviter.",
            notes="Diapositive à photographier. Faire l'exercice de repérage : entourer "
                  "le sujet avant d'écrire la terminaison.")

    d.cartes("Quatre accords à connaître", "Regardez toujours le sujet", [
        ("Masculin singulier", "Le dossier a été déposé."),
        ("Féminin singulier", "La décision a été prise."),
        ("Masculin pluriel", "Les locaux ont été visités."),
        ("Féminin pluriel", "Les heures ont été fixées."),
    ], notes="Faire lire les quatre à voix haute. Seul le féminin pluriel s'entend "
             "rarement à l'oral : d'où l'importance de l'écrit ici.")

    d.piege("Le passif sans « par »",
            "Le communiqué a été publié hier soir.",
            "Le service des communications a publié le communiqué hier soir.",
            "Les deux phrases sont correctes, et la première est parfaitement normale "
            "dans un article. Mais elle ne dit pas qui a agi. Parfois parce qu'on ne le "
            "sait pas, parfois parce que ça n'a aucune importance - et parfois parce que "
            "ça arrange celui qui écrit. Devant un passif sans « par », le lecteur "
            "attentif se pose toujours la question.",
            notes="Ce n'est pas une faute de langue mais un fait de lecture. Le "
                  "présenter comme un outil, pas comme une méfiance systématique.")

    d.pratique('Application', "Mettez à la voix passive, au passé composé",
               "Gardez « par » seulement si l'auteur de l'action est nommé.", [
        ("Le service des communications a publié le communiqué.", "Le communiqué a été publié par le service des communications."),
        ("Le comité a retenu le local de la rue Boisjoli.", "Le local a été retenu par le comité."),
        ("Le conseil a pris la décision.", "La décision a été prise par le conseil."),
        ("On a déposé le dossier hier.", "Le dossier a été déposé hier. - sans « par »"),
        ("On a inscrit cette mesure dans la recommandation.", "Cette mesure a été inscrite dans la recommandation."),
        ("On a refait la rue il y a quatre ans.", "La rue a été refaite il y a quatre ans."),
        ("Le comité a examiné trois raisons.", "Trois raisons ont été examinées par le comité."),
    ], corrige=True,
       notes="Les phrases avec « on » perdent leur « par » : c'est la règle à faire "
             "trouver plutôt qu'à donner. « On » ne se met jamais après « par ».")

    d.billet(
        "Récrivez une de ces phrases à la voix passive : « La Ville a loué le local. »",
        exemples=[
            "Une fois avec « par », une fois sans.",
            "Que perd-on dans la version sans « par » ?",
        ],
        notes="Deux minutes. La seconde question est la vraie : elle vérifie que la "
              "lecture critique a été comprise, pas seulement la mécanique.")

    return d.save(dossier)
