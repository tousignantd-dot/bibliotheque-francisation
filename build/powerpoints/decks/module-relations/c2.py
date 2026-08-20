# -*- coding: utf-8 -*-
"""C2 · Le décor et les évènements.
Bloc C · couleur ambre (écriture) · 90 min.
Source : mini-leçon `t2temps`, exercices `t2temps` et `t2decor`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Le décor et les évènements',
        chapeau="« Je portais des sandales » et « je suis arrivée le douze "
                "janvier » sont tous les deux au passé. Ils ne font pas le même "
                "travail : l'un peint le décor, l'autre fait avancer l'histoire.",
        duree='90 minutes')

    d.titre(notes="La séance la plus longue du module, et la plus rentable. Reprendre les "
                  "billets de C1 : les mots de temps relevés décident du temps de verbe.")

    d.objectifs([
        "employer l'imparfait pour décrire une situation qui durait ;",
        "employer le passé composé pour raconter ce qui est arrivé ;",
        "trancher avec la question « est-ce que je peux compter combien de fois ? » ;",
        "accorder le participe passé avec l'auxiliaire être.",
    ])

    d.declencheur(
        'Le problème', "Pourquoi ces deux phrases ne sont-elles pas au même temps ?",
        pistes=[
            "« À l'aéroport, je portais une veste et des sandales. »",
            "« Je suis arrivée le douze janvier. »",
            "Laquelle décrit ? Laquelle raconte un moment ?",
            "Laquelle pourriez-vous dater précisément ?",
        ],
        notes="Laisser le groupe chercher cinq minutes. Plusieurs sentent la différence sans "
              "savoir la nommer : c'est le bon point de départ.")

    d.tableau('Analyse', "Deux temps, deux rôles",
              ['', 'Imparfait', 'Passé composé'],
              [["Ce que ça dit", "comment c'était", "ce qui est arrivé"],
               ["Ça dure ?", "oui, longtemps ou souvent", "non, c'est un moment"],
               ["On peut compter ?", "non", "oui, une fois, ce jour-là"],
               ["Dans le récit", "le décor", "l'histoire avance"]],
              cle=2,
              note="La ligne du milieu est le test à retenir : peut-on répondre à « combien "
                   "de fois ? »",
              notes="Diapo centrale de la séance. La faire recopier avant de continuer.")

    d.regle("Le test qui tranche",
            "Demandez-vous : est-ce que je peux compter combien de fois ?",
            precision="« Une fois, le douze janvier » — on peut compter, donc passé composé. "
                      "« Tous les jours pendant trois mois » — on ne peut pas compter, donc "
                      "imparfait. Le test marche dans presque tous les cas du niveau.",
            notes="Faire appliquer le test à voix haute sur cinq phrases du dialogue de C1.")

    d.cartes("Le récit de Mariama, décortiqué", "Ce qui alterne", [
        ("Décor · imparfait",
         "« Je portais une veste et des sandales. » · « Il faisait trente degrés. » · "
         "« Mon cousin m'attendait. » · « Je regardais la neige. »"),
        ("Évènement · passé composé",
         "« Je suis arrivée le douze janvier. » · « J'ai eu mal aux oreilles. » · "
         "« Une voisine m'a emmenée glisser. » · « J'ai compris ce jour-là. »"),
        ("Ce que ça donne à l'oreille",
         "Un récit tout au passé composé se comprend, mais sonne comme une liste. "
         "L'imparfait donne au récit de quoi respirer."),
    ], notes="Lire les deux premières cartes à voix haute, l'une après l'autre. La "
             "différence de rythme s'entend.")

    d.regle("L'accord avec être",
            "Avec l'auxiliaire être, le participe s'accorde avec le sujet.",
            precision="Une femme écrit « je suis arrivée ». Plusieurs personnes écrivent "
                      "« on est partis ». Avec avoir, rien ne bouge : « j'ai eu », "
                      "« on a fait », « elle a compris ».",
            notes="C'est la faute la plus visible à l'écrit. Écrire les quatre formes au "
                  "tableau et les y laisser jusqu'à la fin du bloc.")

    d.piege('Tout raconter au passé composé',
            "Il a fait froid et je n'ai pas eu de manteau.",
            "Il faisait froid et je n'avais pas de manteau.",
            "La colonne de gauche n'est pas fausse grammaticalement, mais elle transforme "
            "un décor en série d'évènements. Le lecteur attend qu'il se passe quelque "
            "chose, et rien ne vient. C'est la maladresse la plus fréquente des récits "
            "d'élèves à ce niveau.",
            notes="Ne pas présenter la gauche comme une faute de langue. Le mot juste est "
                  "« maladroit », pas « incorrect ».")

    d.pratique('Pratique · 1 de 2', "Imparfait ou passé composé ?",
               "Mettez le verbe au temps qui convient.", [
        ("Je (arriver) ___ le douze janvier.", "suis arrivée"),
        ("À l'aéroport, je (porter) ___ une veste.", "portais"),
        ("Chez moi, il (faire) ___ trente degrés.", "faisait"),
        ("J'(avoir) ___ mal aux oreilles.", "ai eu"),
        ("Les trois premiers mois, je ne (sortir) ___ pas.", "sortais"),
        ("Un jour, une voisine m'(emmener) ___ glisser.", "a emmenée"),
    ], corrige=True,
       notes="Faire dire le test à voix haute avant chaque réponse : « est-ce que je peux "
             "compter ? ». Le raisonnement compte plus que la forme.")

    d.pratique('Pratique · 2 de 2', "Décor ou évènement ?",
               "Dites si la phrase plante le décor ou raconte un évènement.", [
        ("Mon cousin m'attendait avec un manteau.", "décor"),
        ("J'ai compris ce jour-là.", "évènement"),
        ("Il pleuvait et on n'avait pas de camion.", "décor"),
        ("On a fait onze voyages en voiture.", "évènement"),
        ("Je comptais les jours devant la fenêtre.", "décor"),
    ], corrige=True, cols=1,
       notes="Cet exercice vérifie la compréhension du rôle, pas la conjugaison. Un élève "
             "qui classe bien mais conjugue mal a compris l'essentiel.")

    d.billet(
        "Racontez en cinq phrases un souvenir : deux phrases de décor, trois d'évènement.",
        exemples=[
            "Soulignez les verbes à l'imparfait d'un trait, ceux au passé composé de deux.",
            "Vérifiez l'accord du participe si vous employez être.",
        ],
        notes="Corriger individuellement. Ces billets sont le brouillon de la production "
              "orale de E1 — les rendre avant cette séance.")

    return d.save(dossier)
