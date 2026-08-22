# -*- coding: utf-8 -*-
"""D1 · Deux lettres, deux points de vue - et quinze lignes de fait divers
Bloc D « Défi 3 · Le courrier des lecteurs » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf`, `t3fd` et `t3appui`, cartes
FC_CARDS de la tâche `t3`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Deux lettres, deux points de vue",
        chapeau="Dans la même double page, le journal met ce qu'il y a de "
                "plus sec et ce qu'il y a de plus personnel : quinze lignes "
                "de fait divers d'un côté, des lettres signées de l'autre.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 3. Apporter un vrai journal ouvert à la page "
                  "des lettres : le contraste entre les deux genres se voit avant de se "
                  "lire, et c'est la meilleure entrée en matière.")

    d.objectifs([
        "comprendre deux lettres de lecteurs qui s'opposent ;",
        "lire un fait divers et ne pas y ajouter ce qui n'y est pas ;",
        "distinguer une opinion appuyée d'une opinion nue ;",
        "employer les mots de l'opinion publiée.",
    ], notes="Le deuxième objectif est le plus mal réussi du module : le groupe complète "
             "spontanément le fait divers avec ce qu'il imagine. C'est là qu'il faut "
             "mettre le temps.")

    d.declencheur(
        'Observation', "Pourquoi écrire à un journal ?",
        pistes=[
            "As-tu déjà eu envie d'écrire à un journal, ou à la radio ?",
            "Qu'est-ce qui te ferait écrire : une colère, une bonne nouvelle ?",
            "Qui lit ces lettres, à ton avis ?",
            "Est-ce que le journal dit s'il est d'accord ?",
        ],
        notes="La dernière question annonce l'encadré du journal, à la fin du dialogue. "
              "Laisser le groupe deviner : la réponse le surprend toujours.")

    d.dialogue('Lecture · 1 de 3', "La lettre de Gaëtan Provencher", [
        ("RAPHAËL", "Nadège, le Courrier de la Batture est arrivé. Il y a deux lettres sur ta laveuse.", True),
        ("NADÈGE", "Sur ma laveuse ? Personne ne sait que j'ai une laveuse brisée !", True),
        ("RAPHAËL", "Sur le sujet, je veux dire. « Monsieur le rédacteur en chef, j'ai écouté avec intérêt la chronique du 12 août. À mon avis, on demande beaucoup trop aux consommateurs. »", True),
        ("RAPHAËL", "« Si je dois écrire une mise en demeure chaque fois qu'un appareil brise, je vais y passer mes soirées. Ce n'est pas au client de faire le travail du commerçant. »", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire relever la formule d'appel et la signature : ce sont deux des huit "
             "exigences du courriel de E2. Le dire maintenant, et le rappeler à chaque "
             "lettre lue.")

    d.dialogue('Lecture · 2 de 3', "La lettre de Louise Berthiaume", [
        ("RAPHAËL", "« Pour ma part, je ne partage pas l'avis exprimé la semaine dernière. J'ai suivi les trois étapes en février dernier, pour un lave-vaisselle. »", True),
        ("RAPHAËL", "« Le commerçant avait d'abord refusé ; il a rappelé six jours après avoir reçu ma lettre. Si les gens savaient que ça marche, ils écriraient. »", True),
        ("NADÈGE", "Six jours. Elle donne une date, un appareil et un résultat.", True),
        ("RAPHAËL", "C'est ce qui fait la différence entre les deux. Ils écrivent tous les deux ce qu'ils pensent, mais elle appuie son point de vue sur un cas qu'elle a vécu.", True),
    ], notes="« Le commerçant avait d'abord refusé » : un plus-que-parfait, revu en C2. "
             "Le faire repérer par le groupe, c'est la meilleure preuve que la "
             "grammaire du module sert à lire.")

    d.dialogue('Lecture · 3 de 3', "L'encadré du journal", [
        ("NADÈGE", "Il y a une troisième lettre en dessous ?", True),
        ("RAPHAËL", "Un encadré du journal, plutôt. « Le Courrier publie les lettres signées de leur auteur et n'en corrige que l'orthographe. Les opinions exprimées n'engagent que ceux qui les signent. »", True),
        ("NADÈGE", "Autrement dit, le journal ne dit pas s'il est d'accord.", True),
        ("RAPHAËL", "Il ne le dit jamais dans cette page-là. C'est justement pour ça qu'elle existe.", True),
    ], notes="Le conseil de Raphaël à la fin du dialogue - expliquer d'abord, donner son "
             "avis ensuite - est le plan exact du courriel de E2. Le noter au tableau et "
             "le laisser jusqu'à la fin du module.")

    d.tableau('Analyse', "Le fait divers de la page cinq",
              ['Ce que le texte dit', 'Ce qu\'il ne dit pas'],
              [["Deux logements détruits", "la cause certaine de l'incendie"],
               ["Quatorze occupants évacués", "s'il y a un responsable"],
               ["Aucune blessure rapportée", "ce que le journal en pense"],
               ["Dommages de cent quarante mille dollars", "si l'enquête est terminée"]],
              cle=0,
              note="« Le feu se serait déclaré » : ce conditionnel dit que l'enquête n'est pas finie.",
              notes="Diapositive à photographier. Le conditionnel est la signature du "
                    "fait divers, comme le « je » est celle de la lettre. Le faire "
                    "entourer dans le texte.")

    d.regle("Le fait divers ne dit que ce qu'il dit",
            "Si tu y lis un avis, c'est que tu l'y as mis toi-même.",
            precision="Cinq phrases, aucun « je », aucun adjectif de jugement, et un "
                      "conditionnel. Il ne cherche pas de coupable, il ne tire aucune "
                      "leçon, et il ne dit pas ce que le journal en pense. C'est le "
                      "genre le plus court du journal, et c'est aussi celui qu'on "
                      "complète le plus spontanément dans sa tête.",
            notes="Diapositive à photographier. Faire l'expérience : demander au groupe "
                  "ce qui a causé l'incendie. Plusieurs répondront « la sécheuse » - qui "
                  "n'est nulle part dans le texte.")

    d.vocabulaire('Vocabulaire', "Les mots de l'opinion publiée", [
        ("une lettre ouverte", "Un texte qu'on écrit à un journal pour être lu de tout le monde."),
        ("un point de vue", "La façon dont une personne voit une question, qu'une autre voit autrement."),
        ("un avis appuyé", "Une opinion accompagnée d'une raison qu'on peut vérifier."),
        ("un avis nu", "Une opinion donnée sans raison vérifiable. C'est permis, mais ça ne se discute pas."),
    ], notes="Les deux premiers sont des cartes mémoire de l'activité ; les deux "
             "derniers sont des expressions de travail, à écrire au tableau. Faire "
             "classer les deux lettres du dialogue dans ces deux cases.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après les deux lettres et l'encadré.", [
        ("Louise Berthiaume raconte une démarche qu'elle a faite elle-même.", "vrai"),
        ("Son commerçant avait accepté dès le premier jour.", "faux - il avait d'abord refusé"),
        ("Il a rappelé six jours après avoir reçu la lettre.", "vrai"),
        ("L'appareil de madame Berthiaume était une laveuse.", "faux - un lave-vaisselle"),
        ("Le journal indique dans cette page s'il est d'accord.", "faux - jamais"),
        ("Raphaël conseille de donner son avis avant d'expliquer la chronique.", "faux - l'inverse"),
    ], corrige=True,
       notes="Le dernier compte double : c'est le plan du courriel de E2. Si le groupe "
             "se trompe, reprendre la réplique de Raphaël mot pour mot.")

    d.pratique('Analyse', "Un avis appuyé, ou un avis nu ?",
               "Une seule question : est-ce qu'on donne une raison vérifiable ?", [
        ("« J'ai suivi les trois étapes en février dernier, pour un lave-vaisselle. »", "appuyé"),
        ("« Ce n'est pas au client de faire le travail du commerçant. »", "non appuyé"),
        ("« La laveuse m'a coûté 780 dollars et elle a tenu trois ans. »", "appuyé"),
        ("« Tout le monde sait que les appareils ne durent plus. »", "non appuyé"),
        ("« Le technicien attend une pièce depuis cinq semaines : j'ai les courriels. »", "appuyé"),
        ("« Franchement, c'est décourageant. »", "non appuyé"),
    ], corrige=True,
       notes="Insister : les deux sont permis dans le courrier des lecteurs. On ne juge "
             "pas la personne, on observe si l'avis se discute. C'est aussi le critère "
             "de la production écrite.")

    d.billet(
        "Choisis une des deux lettres et dis laquelle t'a convaincu, et pourquoi.",
        exemples=[
            "Il n'y a pas de bonne réponse.",
            "Dis surtout ce qui, dans la lettre, t'a fait pencher.",
        ],
        notes="Trois minutes. Les réponses partagent presque toujours le groupe en "
              "deux : c'est le meilleur départ possible pour la discussion de D2.")

    return d.save(dossier)
