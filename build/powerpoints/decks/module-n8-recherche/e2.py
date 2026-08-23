# -*- coding: utf-8 -*-
"""E2 · Le courriel du lendemain matin, et le bilan
Bloc E « Je me lance » · couleur framboise · 75 min.
Source : exercice `t3courriel` (type `texte`) et production écrite du bloc
`custom`. La tâche vient des attentes de fin de cours du niveau 8, la
situation « Recherche d'emploi » ne portant aucune intention de production
écrite — c'est écrit ici pour qu'on ne la prenne pas pour une invention.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Ce qu'on écrit le lendemain, et ce qu'on emporte",
        chapeau="On l'appelle courriel de remerciement, et c'est trompeur : "
                "remercier occupe une phrase. Le reste vous donne une "
                "deuxième chance sur un point, un seul.",
        duree='75 minutes')

    d.titre(notes="Dernière séance. Elle se coupe en deux : le courriel d'abord, une "
                  "heure ; le bilan du module ensuite, un quart d'heure.")

    d.objectifs([
        "écrire un courriel d'affaires en trois paragraphes ;",
        "revenir sur un seul point mal expliqué, en le concédant puis en le complétant ;",
        "confirmer par écrit ce qui a été convenu de vive voix ;",
        "faire le bilan de ce qu'on sait faire à la fin du module.",
    ], notes="Le deuxième objectif est celui qui distingue ce courriel d'une formule "
             "de politesse. Sans lui, l'exercice ne vaut rien.")

    d.declencheur(
        'Discussion', "Après une entrevue, qu'est-ce que vous auriez voulu dire autrement ?",
        pistes=[
            "Y a-t-il une réponse à laquelle vous repensez encore ?",
            "Avez-vous déjà écrit à un employeur après une rencontre ?",
            "Combien de temps après ?",
            "Qu'est-ce que vous y avez mis ?",
        ],
        notes="Presque personne n'écrit, et ceux qui le font ne mettent qu'un "
              "remerciement. Les deux constats ouvrent la séance.")

    d.regle("Dans les vingt-quatre heures, et un seul point",
            "Le comité écrit ses notes le jour même ou le lendemain. Passé "
            "deux jours, votre message arrive sur une décision déjà prise et "
            "ne change plus rien.",
            precision="Un seul point repris. Trois reprises se lisent comme un aveu "
                      "d'entrevue ratée, et le lecteur se demande ce que vous avez "
                      "encore mal dit. Choisissez celui qui pèse, et laissez les "
                      "autres.",
            notes="Diapositive à photographier. Le « un seul » est la règle la plus "
                  "importante de la séance, et celle qu'on enfreint le plus.")

    d.tableau('Analyse', "Les cinq pièces du courriel",
              ['La pièce', 'Ce qu\'elle fait'],
              [["L'objet, avec le titre du poste et la date",
                "rend le message retrouvable dans six semaines"],
               ["Le remerciement, une phrase",
                "referme l'entrevue, et rien de plus"],
               ["La reprise : annoncer, concéder, compléter",
                "remplace une affirmation par des faits vérifiables"],
               ["La confirmation de ce qui est convenu",
                "fige l'accord : ce qui est écrit ne se rediscute plus"],
               ["La disponibilité et le numéro",
                "rend la réponse possible sans nouvelle recherche"]],
              cle=0,
              notes="Diapositive à photographier. Aucune des cinq n'est décorative : "
                    "c'est ce qui fait qu'on vous répond.")

    d.cartes('Analyse', "La reprise, en trois mouvements", [
        ("Annoncer",
         "Je souhaiterais revenir sur un point que j'ai mal expliqué. On "
         "prévient : le lecteur sait ce qui vient, et il lit autrement."),
        ("Concéder",
         "C'est vrai, mais incomplet. On ne se dédit pas — se contredire par "
         "écrit après coup fait bien pire que la réponse imparfaite de la "
         "veille."),
        ("Compléter",
         "J'ai formé onze nouveaux opérateurs et rédigé les fiches de "
         "démarrage de deux lignes. Des faits, avec des nombres. Puis dire "
         "pourquoi ils ne figuraient nulle part."),
    ], notes="Faire relire le courriel de Shirin, dans le module. Les trois mouvements "
             "y sont, dans cet ordre, en quatre lignes.")

    d.pratique('Pratique', "Quelle pièce manque ?",
               "Lisez le passage et dites quelle fonction il remplit.", [
        ("Entrevue du 25 octobre, poste de superviseure de production", "l'objet, retrouvable"),
        ("Je vous remercie du temps que vous m'avez accordé hier après-midi.", "le remerciement, une phrase"),
        ("Je souhaiterais revenir sur un point que j'ai mal expliqué.", "l'annonce de la reprise"),
        ("J'ai formé onze opérateurs et rédigé deux fiches de démarrage.", "les faits vérifiables"),
        ("Comme convenu, je vous fais parvenir les attestations traduites.", "la confirmation"),
        ("Je demeure disponible, au 819 555-0148.", "la disponibilité"),
    ], corrige=True,
       notes="Reprend l'exercice de texte du module, où l'élève clique dans le "
             "courriel. Ici, on nomme la fonction : c'est le même travail à l'envers.")

    d.piege('Piège', "ajouter une demande qu'on n'a pas osé formuler",
            "confirmer seulement",
            "Négocier par écrit ce qu'on n'a pas dit en personne se retourne "
            "toujours contre celui qui écrit : il paraît avoir attendu d'être "
            "seul devant son clavier. Le courriel de suivi confirme, précise, "
            "complète — il n'ouvre pas.",
            notes="Question fréquente : « et si j'ai oublié de demander le salaire ? » "
                  "Réponse : on attend l'offre, et on négocie à ce moment-là.")

    d.tableau('Bilan', "Ce que vous savez faire à la fin du module",
              ['Ce qui a changé', 'Où c\'était'],
              [["Poser trois questions au lieu d'en subir vingt",
                "défi 1, l'appel de présélection"],
               ["Lire un profil et une offre pour décider",
                "défi 2, les deux documents"],
               ["Répondre à l'objection avant qu'on la pose",
                "défi 3, l'entrevue"],
               ["Négocier en offrant une contrepartie",
                "défi 3, la fin de l'entrevue"],
               ["Refermer une question interdite sans se fâcher",
                "défi 3, et la phrase apprise par cœur"]],
              cle=0,
              notes="Diapositive de clôture, à photographier. Relire la thèse écrite au "
                    "tableau depuis A1 : « ce qui gêne ne se dit presque jamais à voix "
                    "haute ». C'est là que le module se referme.")

    d.billet(
        "Écrivez le courriel du lendemain et déposez-le dans le module.",
        exemples=[
            "De 10 à 14 phrases, trois paragraphes, un seul point repris.",
            "Deux faits avec un nombre, et un numéro de téléphone à la fin.",
        ],
        notes="Dépôt dans « Je me lance ». Le bouton d'envoi n'apparaît qu'une fois la "
              "correction demandée : on ne dépose pas un texte non relu.")

    return d.save(dossier)
