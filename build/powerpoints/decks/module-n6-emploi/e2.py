# -*- coding: utf-8 -*-
"""E2 · Ton courriel aux ressources humaines
Bloc E « Je me lance » · couleur framboise · bilan · 75 min.
Source : production écrite du module et exercice `t3courriel` avec sa
mini-leçon. Intention du programme : rédiger un courriel dans le contexte de
relations professionnelles.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Ton courriel aux ressources humaines",
        chapeau="Un message à un ami se lit en entier ; un courriel de "
                "travail se lit en diagonale, par quelqu'un qui en a trente "
                "autres. Toute sa forme vient de là.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Elle porte la production écrite et le "
                  "bilan. Prévoir vingt minutes pleines pour l'écriture, et garder "
                  "l'autoévaluation pour la fin.")

    d.objectifs([
        "écrire un objet court, précis, sans phrase complète ;",
        "découper le message en trois paragraphes, un par idée ;",
        "formuler une demande au conditionnel ;",
        "signer avec le nom, le service et le quart.",
    ], notes="Le premier objectif est celui qui décide si le courriel est ouvert "
             "aujourd'hui ou vendredi. Ne pas le traiter comme un détail de forme.")

    d.declencheur(
        'Observation', "Tu reçois trente courriels. Lequel ouvres-tu en premier ?",
        pistes=[
            "Qu'est-ce que tu regardes avant d'ouvrir ?",
            "Lequel laisses-tu pour plus tard, et pourquoi ?",
            "Qu'est-ce qui te fait répondre tout de suite ?",
        ],
        notes="La réponse — l'objet — mène toute la séance. Écrire au tableau trois "
              "objets, dont « Bonjour » et « Urgent », et faire choisir.")

    d.tableau('Analyse', "Les six morceaux, et ce qu'on y met",
              ['Le morceau', 'Ce qu\'on écrit'],
              [["L'objet", "Candidature interne — poste de vérificatrice à la qualité"],
               ["L'appel", "Bonjour Madame Grenon,"],
               ["Pourquoi j'écris", "Je vous écris au sujet du poste affiché le 14 septembre."],
               ["Ce que je joins", "Vous trouverez ci-joint mon formulaire RH-04."],
               ["Ce que je demande", "Pourriez-vous me confirmer que vous l'avez bien reçu ?"],
               ["La salutation", "Cordialement, Yaneth Mosquera, expédition, quart de jour"]],
              cle=0,
              notes="Diapositive à photographier. Six rangées sans note : c'est le "
                    "modèle complet, et il tient sur une seule diapositive. Le faire "
                    "recopier avant d'écrire.")

    d.regle("Une demande se pose au conditionnel",
            "« Pourriez-vous me confirmer… » plutôt que « Confirmez-moi la réception ».",
            precision="Le conditionnel n'est pas de la faiblesse : c'est la forme "
                      "normale d'une demande écrite au travail. Il laisse à l'autre la "
                      "possibilité de dire non — et c'est justement ce qui fait qu'il "
                      "dit oui. « Serait-il possible de… » et « je vous serais "
                      "reconnaissante de… » font le même travail.",
            notes="Diapositive à photographier. Beaucoup d'élèves écrivent trop sec par "
                  "peur d'écrire trop long. Montrer que la politesse tient en un mot "
                  "de plus, pas en trois phrases.")

    d.pratique('Pratique', "Choisis le meilleur objet",
               "Un seul est utilisable. Dites pourquoi les autres ne le sont pas.", [
        ("Bonjour", "trop vague - ne dit rien du contenu"),
        ("Question", "trop vague - le lecteur ne peut pas classer"),
        ("URGENT !!!", "les majuscules crient, et rien n'est dit"),
        ("Candidature interne — poste de vérificatrice à la qualité", "le bon : court, précis, sans phrase"),
        ("Je vous écris au sujet du poste que vous avez affiché la semaine dernière.", "c'est une phrase, pas un objet"),
    ], corrige=True,
       notes="Faire dire à voix haute pourquoi chacun échoue. Le dernier est le plus "
             "instructif : il est poli, complet, et inutilisable — un objet n'est pas "
             "une phrase.")

    d.piege('Piège', "mettre deux sujets dans un courriel",
            "en écrire deux",
            "Le destinataire répond au premier et oublie le second : c'est "
            "systématique, et ce n'est pas de la mauvaise volonté. Un courriel, un "
            "sujet, un objet. Deux questions différentes valent deux messages, même "
            "courts.",
            notes="Ajouter les trois autres interdits : les majuscules qui crient, "
                  "« à qui de droit » quand on connaît le nom, et la signature sans "
                  "service ni quart.")

    d.pratique('Écriture', "Ce que l'IA regardera dans ton texte",
               "Relisez cette liste avant de demander la correction.", [
        ("Un objet court et précis", "sans phrase complète"),
        ("Une formule d'appel qui nomme la personne", "et une salutation à la fin"),
        ("Trois paragraphes séparés", "un par idée"),
        ("Une date précise", "l'affichage ou la limite"),
        ("Une demande au conditionnel", "pourriez-vous, serait-il possible"),
        ("Un « il faut que » ou « je souhaite que »", "suivi du subjonctif"),
        ("Une reprise sans répétition", "cette formation, ce poste"),
        ("Une signature complète", "nom, service, quart"),
    ], corrige=True,
       notes="Ces huit points sont ceux de la carte du module, mot pour mot. Les "
             "projeter pendant l'écriture. Vingt minutes d'écriture, puis correction "
             "par l'IA, puis dépôt.")

    d.tableau('Bilan du module', "Ce que tu sais faire maintenant",
              ['Le geste', 'Où tu l\'as appris'],
              [["Reconnaître les quatre écrits", "Je découvre"],
               ["Suivre une démarche en cinq étapes", "Défi 1"],
               ["Lire une note et une politique", "Défi 2"],
               ["Lire un compte rendu", "Défi 3"],
               ["Décrire la démarche à voix haute", "Je me lance"],
               ["Écrire un courriel professionnel", "Je me lance"]],
              cle=0,
              notes="Diapositive à photographier. Faire lever la main sur chaque ligne "
                    "avant d'ouvrir l'autoévaluation du module : le groupe voit alors "
                    "le chemin parcouru, ce qui change la façon de remplir la grille.")

    d.billet(
        "Une chose que tu feras différemment au travail à partir de maintenant.",
        exemples=[
            "Une phrase, la plus concrète possible.",
            "Pas « je vais mieux lire » : dis quoi, où, quand.",
        ],
        notes="Cinq minutes, pour finir. Ramasser et garder : ces billets sont ce qui "
              "dit si le module a servi, et ils valent mieux qu'un examen.")

    return d.save(dossier)
