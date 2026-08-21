# -*- coding: utf-8 -*-
"""B4 · La lettre en cinq parties.
Bloc B « Défi 1 » · couleur ambre · 75 min. Fin du Défi 1.
Source : exercices `t1pass`, `t1form` et `t1lettre`, et leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="La lettre en cinq parties",
        chapeau="Une lettre qui règle un problème tient en une page : on "
                "rattache, on expose, on nomme l'écart, on demande, on date. "
                "Tout le reste allonge sans rien ajouter.",
        duree='75 minutes')

    d.titre(notes="Séance de production écrite. Prévoir que la rédaction occupe la "
                  "seconde moitié du temps : c'est le premier texte formel du module.")

    d.objectifs([
        "transformer une accusation en constat par la voix passive ;",
        "reconnaître le rôle de chaque phrase d'une lettre d'affaires ;",
        "écrire un objet qui se lit seul ;",
        "fixer une échéance de réponse sans menacer.",
    ], notes="L'objectif 1 est le pivot : c'est la grammaire au service de la "
             "diplomatie, et c'est ce qui rend la lettre efficace.")

    d.regle("Le déplacement du projecteur",
            "La majoration n'a pas été appliquée.",
            precision="Comparez : « Vous n'avez pas appliqué la majoration » met le "
                      "projecteur sur une personne, qui va se défendre. « La majoration "
                      "n'a pas été appliquée » met le projecteur sur le fait, qui, lui, "
                      "peut être corrigé. La passive n'est pas de la lâcheté : c'est un "
                      "outil de règlement.",
            notes="Diapositive à photographier. C'est la phrase que Nadia emploie au "
                  "téléphone comme dans sa lettre.")

    d.tableau('Analyse', "Fabriquer une passive, en trois gestes",
              ['Le geste', 'L\'exemple'],
              [["Le complément monte en sujet", "Le système a mêlé les dossiers, donc : Les dossiers…"],
               ["Le verbe devient être + participe", "a mêlé devient : ont été mêlés"],
               ["L'auteur devient facultatif", "…par le système : souvent inutile"]],
              cle=0,
              note="Le participe s'accorde toujours avec le sujet, qui est juste devant.",
              notes="Diapositive à photographier. L'accord est plus simple qu'avec "
                    "« avoir » : il n'y a rien à chercher.")

    d.cartes("Cinq parties, dans cet ordre", "Une lettre d'affaires qui règle un problème", [
        ("1. Rattacher",
         "Je donne suite à notre conversation téléphonique du 19 août."),
        ("2. Exposer, daté et chiffré",
         "Les 10 et 11 août, j'ai travaillé quatre heures au-delà de quarante."),
        ("3. Nommer l'écart",
         "Or, la majoration de cinquante pour cent n'a pas été appliquée."),
        ("4. Demander, une seule fois",
         "Je vous demande donc de corriger les deux périodes visées."),
        ("5. Dater et saluer",
         "Je vous saurais gré de me confirmer avant le 27 août. Veuillez agréer…"),
    ], cols=1,
       notes="Diapositive à photographier. « Or » est le mot le plus utile de la "
             "lettre : il oppose l'attendu au constaté sans accuser personne.")

    d.piege("S'excuser d'avoir raison",
            "Je suis vraiment désolée de vous déranger, je sais que vous êtes occupé.",
            "Je donne suite à notre conversation du 19 août.",
            "L'excuse affaiblit une demande légitime et invite au report. Son contraire "
            "— la menace de porter plainte dès la première lettre — ferme la porte à un "
            "règlement simple et met l'autre en défense. Entre les deux : on expose, on "
            "demande, on date. Le recours existe et reste disponible.",
            notes="Faire remarquer que la lettre de Nadia ne contient ni excuse ni "
                  "menace, et qu'elle obtient la correction.")

    d.pratique('Grammaire', "À la voix passive",
               "Réécrivez sans nommer le responsable.", [
        ("Vous n'avez pas appliqué la majoration.", "La majoration n'a pas été appliquée."),
        ("Quelqu'un a saisi quarante-quatre heures.", "Quarante-quatre heures ont été saisies."),
        ("On fermera la période mercredi midi.", "La période sera fermée mercredi midi."),
        ("Le système a mêlé plusieurs dossiers.", "Plusieurs dossiers ont été mêlés."),
        ("La direction doit approuver la modification.", "La modification doit être approuvée."),
        ("On a corrigé les deux périodes.", "Les deux périodes ont été corrigées."),
    ], corrige=True,
       notes="Vérifier l'accord du participe à chaque réponse : c'est là que tout se "
             "joue à l'écrit.")

    d.pratique('Rédaction', "Les formules justes",
               "Complétez la lettre de Nadia.", [
        ("Objet : ___ des heures supplémentaires — périodes du 2 au 15 août", "correction"),
        ("Madame, je donne ___ à notre conversation du 19 août.", "suite"),
        ("___, la majoration de cinquante pour cent n'a pas été appliquée.", "Or"),
        ("Je vous ___ donc de corriger les deux périodes visées.", "demande"),
        ("Vous trouverez ___ les deux courriels d'autorisation.", "ci-joint"),
        ("Je vous saurais ___ de me confirmer avant le 27 août.", "gré"),
        ("Veuillez ___, Madame, mes salutations distinguées.", "agréer"),
    ], corrige=True,
       notes="Ces sept formules sont à apprendre par cœur. Elles serviront dix ans.")

    d.billet(
        "Écrivez la lettre au complet, en cinq parties, sur une seule page.",
        exemples=[
            "Un objet qui se lit seul, avec la période visée.",
            "Une seule demande, et une date de réponse.",
        ],
        notes="Travail à remettre. C'est la première des trois productions écrites du "
              "module ; les deux autres sont le compte rendu (C4) et la demande de "
              "formation (E2).")

    return d.save(dossier)
