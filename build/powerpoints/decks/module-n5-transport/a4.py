# -*- coding: utf-8 -*-
"""A4 · Le mot juste pour l'état de la route
Bloc A « Je découvre » · couleur ambre · 75 min. Écriture et décision.
Source : exercice `prEtat` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Le mot juste pour l'état de la route",
        chapeau="Quatre états, quatre mots, et quatre décisions différentes. "
                "Ce n'est pas du vocabulaire de luxe : c'est de "
                "l'information qui vaut vingt minutes de votre matinée.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. Elle fait passer du mot à la décision : "
                  "savoir ce que veut dire « bouchon » ne sert que si l'on sait ce qu'on "
                  "fait en l'entendant. Ouvrir en demandant au groupe ce qu'il ferait, "
                  "ce matin, devant chacun des quatre états.")

    d.objectifs([
        "choisir le mot juste pour décrire l'état d'une route ;",
        "dire ce qu'on décide devant chacun des quatre états ;",
        "reconnaître les formules « dense mais fluide » et « pour le moment » ;",
        "écrire une annonce courte avec le mot juste.",
    ], notes="Le troisième objectif porte sur deux formules figées qui trompent tout le "
             "monde. Elles ne se déduisent pas des mots : elles s'apprennent d'un bloc.")

    d.regle("Le mot dit ce qu'il faut faire",
            "Ralentissement : on y va. Bouchon : on change de chemin. Fermé : "
            "on suit la directive.",
            precision="« Entrave » ne dit encore rien de précis : il faut écouter la "
                      "suite pour savoir de laquelle il s'agit.",
            notes="Diapositive à photographier. C'est la synthèse du bloc A, et elle "
                  "servira de grille de lecture pour tout le bloc C.")

    d.tableau('Quatre états', "Le mot, et la décision",
              ['Ce qu\'on entend', 'Ce qu\'on fait'],
              [["Un ralentissement", "On part un peu plus tôt"],
               ["Un bouchon", "On change de chemin"],
               ["Une route fermée", "On suit la directive"],
               ["Aucune entrave", "On part comme d'habitude"]],
              cle=1,
              notes="Faire compléter la colonne de droite avant de l'afficher, et "
                    "accepter les nuances : devant un bouchon, quelqu'un qui n'a pas "
                    "d'autre chemin ne peut que prévenir. C'est le défi 3.")

    d.cartes("Deux formules", "Ce qu'elles veulent vraiment dire", [
        ("Dense mais fluide",
         "Beaucoup d'autos, mais ça avance. Bonne nouvelle."),
        ("Pour le moment",
         "Ce n'est pas touché, mais on s'attend au pire."),
        ("En cours de dégagement",
         "Les remorqueuses travaillent. Ce n'est pas fini."),
        ("Aucune entrave à signaler",
         "Rien du tout. La meilleure phrase de la journée."),
    ], notes="Ces quatre formules sont figées : on les apprend telles quelles. « Pour le "
             "moment » est la plus utile — elle annonce que le bulletin suivant sera "
             "moins bon.")

    d.piege("Prendre « dense » pour « bloqué »",
            "C'est dense : on ne passera jamais.",
            "C'est dense mais fluide : il y a du monde, mais ça avance.",
            "Dense veut dire : beaucoup d'autos. Le bulletin ajoute presque "
            "toujours « mais fluide ». Les deux mots ensemble sont une bonne "
            "nouvelle, pas une mauvaise.",
            notes="Erreur très fréquente et coûteuse : elle fait prendre un détour de "
                  "quarante minutes pour éviter dix minutes d'attente.")

    d.piege("Croire qu'une voie fermée ferme la route",
            "La voie de gauche est fermée : on ne passe pas.",
            "Deux voies sur trois sont bloquées : il en reste une.",
            "Une voie n'est pas la route. Tant qu'il reste une voie, ça passe, "
            "lentement. Le bulletin dit autrement quand la route est fermée.",
            notes="Faire compter les voies sur une photo ou au tableau. La différence "
                  "entre « une voie fermée » et « la route fermée » se voit mieux "
                  "dessinée qu'expliquée.")

    d.pratique('Écriture', "Écrivez l'annonce",
               "Une phrase par situation, avec le mot juste.", [
        ("Les autos roulent à quarante à l'heure.", "On annonce un ralentissement de vingt minutes."),
        ("Plus rien ne bouge depuis dix minutes.", "C'est un bouchon : la circulation est très dense."),
        ("Un camion est arrêté hors des voies.", "Un véhicule est immobilisé sur l'accotement."),
        ("Rien ne bloque le tunnel ce matin.", "Aucune entrave à signaler dans le tunnel."),
        ("La voie de gauche rouvre à cinq heures.", "La voie de gauche est fermée jusqu'à cinq heures."),
    ], corrige=True,
       notes="Faire écrire d'abord, individuellement, puis comparer deux par deux avant "
             "d'afficher le corrigé. Les variantes correctes sont nombreuses : accepter "
             "tout ce qui contient le mot juste et un repère.")

    d.billet(
        "Écrivez ce que vous feriez demain matin si votre route était bloquée.",
        exemples=[
            "Avez-vous un autre chemin ? Lequel ?",
            "Qui faudrait-il prévenir, et à quelle heure ?",
        ],
        notes="Ramasser les billets : ils annoncent tout le défi 3 et disent qui, dans "
              "le groupe, a déjà eu à téléphoner pour annoncer un retard.")

    return d.save(dossier)
