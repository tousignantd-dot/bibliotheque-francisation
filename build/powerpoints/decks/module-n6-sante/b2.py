# -*- coding: utf-8 -*-
"""B2 · Le parler d'ici : être après, passer proche
Bloc B « Défi 1 » · couleur teal · 75 min. Écoute et réponse.
Source : exercices `t1aspect` et `t1chiffres`, mini-leçon `t1aspect`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='teal',
        titre="Le parler d'ici : être après, passer proche",
        chapeau="Gilles ouvre la conversation par « vous êtes après "
                "attendre ». Aucun cours n'y prépare, et c'est parfaitement "
                "ordinaire ici.",
        duree='75 minutes')

    d.titre(notes="Séance d'écoute. Elle porte sur quatre tournures que le programme "
                  "demande de comprendre, jamais de produire. Le dire au groupe dès "
                  "le début : personne ne sera évalué sur leur emploi.")

    d.objectifs([
        "comprendre « être après » suivi d'un verbe à l'infinitif ;",
        "comprendre « être pour » et « être sur le bord de » ;",
        "comprendre « passer proche de », et ce qu'il dit du résultat ;",
        "relever des chiffres à la deuxième écoute d'une conversation.",
    ], notes="Le troisième objectif corrige un contresens réel : « on a passé proche "
             "d'annuler » veut dire qu'on n'a pas annulé, et beaucoup comprennent le "
             "contraire.")

    d.declencheur(
        'Observation', "Quelle phrase d'ici ne comprenez-vous toujours pas ?",
        pistes=[
            "Une phrase entendue au travail, à l'épicerie, chez le voisin.",
            "Est-ce que vous avez osé demander ce qu'elle voulait dire ?",
            "Qu'est-ce que vous avez répondu, en attendant de comprendre ?",
        ],
        notes="Cinq minutes. Noter les phrases au tableau. Il y en aura d'autres que "
              "les quatre de la séance : les traiter au passage, elles valent leur "
              "temps.")

    d.tableau('Analyse', "Quatre tournures, quatre moments de l'action",
              ['On entend', 'Ça veut dire'],
              [["être après", "c'est en train de se faire"],
               ["être pour", "c'est sur le point d'arriver"],
               ["être sur le bord de", "à un cheveu, et retenu de justesse"],
               ["passer proche de", "ça a failli arriver, et ce n'est pas arrivé"]],
              cle=0,
              note="Le programme demande de les comprendre. Personne n'est obligé de les employer.",
              notes="Diapositive à photographier. C'est le tableau de référence du "
                    "défi. Faire lire les quatre lignes à voix haute avant tout "
                    "exemple.")

    d.cartes('Exemples', "Les mêmes phrases, en français d'ailleurs", [
        ("Je suis après attendre.", "Je suis en train d'attendre. L'action est commencée et pas finie."),
        ("Il est après remplir sa feuille.", "Il est en train de la remplir, en ce moment même."),
        ("J'étais pour partir.", "J'allais partir, et quelque chose est arrivé avant."),
        ("Je suis sur le bord de pleurer.", "Je me retiens de justesse, et ça se voit."),
        ("On a passé proche d'annuler.", "On a failli annuler. Donc on n'a pas annulé."),
        ("Ça fait deux heures que je suis là.", "J'attends depuis deux heures, et j'attends encore."),
    ], cols=2,
       notes="Une carte à la fois. Faire lire la colonne de gauche par un élève et "
             "celle de droite par un autre : l'écart entre les deux registres "
             "s'entend mieux à deux voix.")

    d.piege('Compréhension',
            "on a passé proche d'annuler, donc on a annulé",
            "on a passé proche d'annuler, donc on n'a pas annulé",
            "C'est le contresens exact, et il est très fréquent. La tournure "
            "dit qu'une chose a failli arriver — et le fait qu'on en parle "
            "signifie précisément qu'elle n'est pas arrivée. Même piège avec "
            "« il s'en est fallu de peu » et « à un cheveu près ».",
            notes="Faire reformuler par trois élèves différents. Ce piège coûte des "
                  "malentendus réels au travail, où l'on entend souvent « j'ai passé "
                  "proche de manquer mon quart ».")

    d.piege('Compréhension',
            "je suis après manger, donc j'ai fini",
            "je suis après manger, donc je mange en ce moment",
            "« Après » ne parle pas du tout de temps dans cette tournure. Ne "
            "cherchez pas de logique : elle est ancienne, elle est venue de "
            "France avant de s'y perdre, et elle se reconnaît plus qu'elle ne "
            "se comprend.",
            notes="Rassurer : cette tournure n'a aucune logique repérable. Ce qui "
                  "s'apprend ici est un réflexe de reconnaissance, pas une règle.")

    d.regle("À l'écrit, on écrit les équivalents",
            "Ces quatre tournures sont justes à l'oral et déplacées dans un écrit.",
            precision="Dans un courriel au secrétariat ou sur un formulaire, on écrit "
                      "« être en train de », « aller », « faillir ». Écrire « j'étais "
                      "pour annuler mon rendez-vous » détonne, sans être faux.",
            notes="Diapositive à photographier. Le dire évite qu'un élève enthousiaste "
                  "les réemploie dans la production écrite de E2, où elles seraient "
                  "corrigées.")

    d.pratique('Écoute', "Qu'est-ce que ça veut dire ?",
               "Écoutez la phrase, puis donnez son équivalent.", [
        ("Je suis après attendre.", "je suis en train d'attendre"),
        ("Il est après remplir sa feuille.", "il est en train de la remplir"),
        ("J'étais pour partir.", "j'allais partir"),
        ("Je suis sur le bord de pleurer.", "je me retiens de justesse"),
        ("On a passé proche d'annuler.", "on a failli annuler, et on ne l'a pas fait"),
        ("Je viens de sortir de son bureau.", "j'en suis sorti il y a une minute"),
    ], corrige=True,
       notes="Lire les phrases soi-même, avec l'intonation d'ici. L'audio du module "
             "servira à la reprise individuelle.")

    d.pratique('Écoute', "Les chiffres, à la deuxième écoute",
               "Réécoutez la conversation et complétez.", [
        ("Gilles attend depuis combien de temps ?", "deux heures"),
        ("Leyla est au Québec depuis combien d'années ?", "cinq ans"),
        ("Depuis combien d'années à Rimouski ?", "trois ans"),
        ("Combien de jours travaille-t-elle sur quatorze ?", "sept"),
        ("Depuis combien de mois est-elle fatiguée ?", "huit mois"),
    ], corrige=True,
       notes="Faire écouter deux fois, sans arrêt entre les deux. Les chiffres sont "
             "ce qui se perd le plus vite dans un débit normal, et c'est exactement "
             "ce que le niveau demande de tenir.")

    d.billet(
        "Notez une phrase d'ici que vous voudriez comprendre.",
        exemples=[
            "Écrivez-la comme vous l'avez entendue.",
            "Dites où vous l'avez entendue, si vous vous en souvenez.",
        ],
        notes="Deux minutes. Garder les billets : ils font une banque de tournures "
              "qui servira à toute la session, bien au-delà de ce module.")

    return d.save(dossier)
