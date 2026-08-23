# -*- coding: utf-8 -*-
"""B5 · Lire un sommaire de police, et faire clarifier
Bloc B « Défi 1 · Ce qui est couvert » · couleur teal · 75 min.
Écoute et réponds. Source du module : les exercices `t1prop` et `t1clar`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B5', section='teal',
        titre="Lire un sommaire de police, et faire clarifier",
        chapeau="Deux pages qui résument soixante. On y trouve ses plafonds "
                "en trois minutes — et pour tout le reste, il faut savoir "
                "poser la question.",
        duree='75 minutes')

    d.titre(notes="Séance en deux temps : la lecture d'un document, puis les "
                  "phrases qui servent à le faire expliquer. Les deux "
                  "exercices du module correspondants sont `t1prop` (type "
                  "texte) et `t1clar`.")

    d.objectifs([
        "prélever un plafond, une franchise et un mode d'indemnisation ;",
        "repérer une sous-limite et savoir ce qu'elle impose ;",
        "faire clarifier un mot une seule fois, sur le mot qui décide ;",
        "résumer avec ses propres mots pour vérifier.",
    ], notes="Les deux derniers objectifs sont des savoirs du programme : "
             "« phrases clés pour résumer et faire le point » et « phrases "
             "clés pour faire clarifier les points équivoques ».")

    d.declencheur(
        'Pour commencer', "Dans une explication de dix minutes, combien de "
                          "mots décident vraiment de quelque chose ?",
        pistes=[
            "Un ? Deux ? Tous ?",
            "Que faites-vous quand un mot vous échappe : vous arrêtez, ou vous continuez ?",
            "Qu'est-ce que ça coûte de faire semblant d'avoir compris ?",
        ],
        notes="La bonne réponse à la première piste est « un ou deux ». C'est "
              "ce qui rend la demande de clarification gérable : on ne "
              "s'arrête pas dix fois, on s'arrête une fois au bon endroit.")

    d.tableau('Analyse', "Ce qu'on cherche dans un sommaire",
              ['Où regarder', 'Ce qu\'on note'],
              [["Section A — vos biens", "le plafond, la franchise, le mode d'indemnisation"],
               ["Les sous-limites", "bijoux, argent, vélos, instruments"],
               ["Section B — responsabilité civile", "le montant par événement, et l'absence de franchise"],
               ["Les avenants", "ce qu'ils ajoutent, et leur franchise propre, souvent différente"],
               ["Le pied de page", "le délai de déclaration, la prime, le nombre de versements"]],
              cle=0,
              note="Trois minutes par année, au renouvellement. Le meilleur rapport effort-résultat du module.",
              notes="Diapositive à photographier. Insister sur la franchise "
                    "des avenants : elle est souvent plus élevée que la "
                    "principale, et rien ne le signale.")

    d.regle("Le sommaire donne les plafonds ; le contrat donne les exclusions",
            "Le sommaire est exact, mais il ne contient aucune exclusion détaillée.",
            precision="Les trois quarts des refus s'appuient sur une "
                      "exclusion. Lire les exclusions du contrat en premier, "
                      "avant même les protections.",
            notes="Diapositive à photographier. Contre-intuitif, et c'est "
                  "l'ordre utile : les protections décrivent un monde "
                  "généreux, les exclusions décrivent le vrai contrat.")

    d.cartes('Analyse', "Six phrases clés, six moments", [
        ("Qu'entendez-vous exactement par… ?", "dès qu'un mot technique décide de quelque chose"),
        ("Sur quelle clause vous appuyez-vous ?", "dès qu'une décision vous est annoncée"),
        ("Ce montant est avant ou après la franchise ?", "avant d'accepter un chiffre, jamais après"),
        ("Reprenons les trois points l'un après l'autre.", "au début d'une conversation qui en contient plusieurs"),
        ("Je résume, pour être certaine : …", "au milieu, puis à la fin"),
        ("Je vous envoie les pièces aujourd'hui.", "en raccrochant, toujours"),
    ], cols=2,
       notes="Faire dire les six à voix haute, une personne chacune. Elles "
             "ne servent que si elles viennent sans réfléchir.")

    d.piege('Attention',
            "« Je n'ai rien compris. »",
            "« Le mot “subrogation”, vous l'entendez comment ? »",
            "La première phrase oblige l'autre à tout recommencer et donne "
            "l'impression d'un mur. La seconde désigne le point exact et se "
            "règle en une phrase — et elle vous fait passer pour rigoureux "
            "plutôt que pour perdu, ce qui est l'inverse de ce qu'on craint.",
            notes="Beaucoup d'élèves croient que demander une précision les "
                  "dessert. Le dire explicitement : c'est le contraire, et "
                  "les professionnels le remarquent.")

    d.pratique('Pratique', "Que fait cette phrase dans la conversation ?",
               "Reliez chaque phrase à son travail.", [
        ("Qu'entendez-vous exactement par « valeur à neuf » ?", "faire clarifier un mot du métier"),
        ("Sur quelle clause vous appuyez-vous ?", "faire préciser le fondement écrit"),
        ("Je résume : je déclare, je monte un inventaire, j'attends l'expert.", "reformuler pour vérifier"),
        ("Reprenons les trois points l'un après l'autre.", "structurer une conversation longue"),
        ("Ce montant est avant ou après la franchise ?", "lever une ambiguïté sur un chiffre"),
        ("Je vous envoie les quatre pièces aujourd'hui.", "terminer sur une action datée"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t1clar` du module, dans sa version projetée. "
             "Après correction, faire jouer un mini-échange de deux répliques "
             "avec chacune des six.")

    d.billet(
        "Résume en une phrase, avec tes propres mots, ce qu'est une franchise.",
        exemples=[
            "N'emploie ni le mot « franchise » ni le mot « soustraire ».",
            "Une seule phrase, adressée à quelqu'un qui ne connaît rien à l'assurance.",
        ],
        notes="Cinq minutes. C'est l'exercice de reformulation lui-même : "
              "répéter les mots de l'autre ne prouve rien, et l'interdiction "
              "des deux mots force la vraie reformulation.")

    return d.save(dossier)
