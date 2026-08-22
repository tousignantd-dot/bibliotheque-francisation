# -*- coding: utf-8 -*-
"""C1 · Deux papiers sur la table
Bloc C « Défi 2 · Les papiers du chantier » · couleur acier · 75 min.
Source : dialogue `t2`, exercices `t2vf` et `t2mise`, mini-leçon `t2mise`,
cartes de FC_CARDS de la section t2.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Deux papiers sur la table",
        chapeau="Le rapport décrit ce qui est ; la soumission décrit ce qui "
                "sera fait. Ils ne se contredisent pas : ils ne font pas le "
                "même travail.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc C. Apporter, si possible, un vrai document "
                  "technique — un relevé, une facture détaillée, un avis — et le "
                  "faire circuler avant de commencer. Voir la mise en page vaut "
                  "mieux que l'entendre décrire.")

    d.objectifs([
        "dire lequel des deux papiers porte quel renseignement ;",
        "nommer les mots des papiers du chantier ;",
        "trouver la section des limites d'un rapport ;",
        "trouver la ligne des exclusions d'une soumission.",
    ], notes="Les deux derniers objectifs sont les seuls qui comptent vraiment. Le "
             "reste de la lecture s'improvise ; ces deux endroits-là, non.")

    d.declencheur(
        'Observation', "Vous recevez deux documents la même semaine sur la même maison. Lequel ouvrez-vous en premier ?",
        pistes=[
            "Lequel a coûté de l'argent ? Lequel était gratuit ?",
            "Lequel a été écrit par quelqu'un qui fera les travaux ?",
            "Est-ce que ça change quelque chose à la façon de le lire ?",
        ],
        notes="La deuxième question donne la réponse à la troisième. Un document "
              "écrit par celui qui exécutera n'a pas le même statut qu'un document "
              "écrit par quelqu'un qui n'a rien à vendre.")

    d.dialogue('Dialogue · 1 de 3', "Deux papiers, deux métiers", [
        ("DOÏNA", "J'ai votre rapport devant moi et la soumission de monsieur Trudelle à côté. Je n'arrive pas à les faire concorder.", True),
        ("KETTLY", "C'est normal, et c'est même sain. Ces deux papiers ne servent pas à la même chose. Le mien décrit ce qui est ; le sien décrit ce qui sera fait.", True),
        ("DOÏNA", "Il y a une section que je ne comprends pas du tout, à la page deux. Elle s'appelle « Historique du bâtiment ».", True),
        ("KETTLY", "Celle-là, je la rédige au passé des documents, parce que je recopie ce que disent les archives de la ville.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="La deuxième réplique est la phrase du bloc entier. L'écrire au tableau "
             "et l'y laisser quatre séances.")

    d.dialogue('Dialogue · 2 de 3', "Dix-neuf pour cent", [
        ("DOÏNA", "Vous écrivez : « Le mur nord, où la fissure a été relevée, présente un taux d'humidité de dix-neuf pour cent. » Dix-neuf, c'est beaucoup ?", True),
        ("KETTLY", "C'est trop pour refermer un mur par-dessus. En bas de quinze, je vous dirais d'y aller. À dix-neuf, il faut que vous laissiez sécher.", True),
        ("DOÏNA", "Monsieur Trudelle m'a dit la même chose. Trois ou quatre semaines.", True),
        ("KETTLY", "Alors vous avez deux avis qui concordent. Notez-le : c'est rare, et ça vaut la peine d'être noté.", True),
    ], notes="La première réplique contient la relative en « où » de C4 et la seconde "
             "un subjonctif après « il faut que ». Les signaler sans les expliquer.")

    d.dialogue('Dialogue · 3 de 3', "Pourquoi écrire ce qu'on ne fait pas", [
        ("DOÏNA", "Sa soumission a une colonne « exclusions ». Pourquoi une entreprise écrirait-elle ce qu'elle ne fait pas ?", True),
        ("KETTLY", "Parce que c'est là que se trouvent les mauvaises surprises. Lisez-moi les exclusions.", True),
        ("DOÏNA", "« Le permis, la peinture, les luminaires, la disposition des matériaux, et tout travail découlant d'une condition non visible au moment de la visite. »", True),
        ("KETTLY", "Arrêtez-vous sur la dernière. Si on ouvre le plancher et qu'on trouve quelque chose que personne ne pouvait voir, ce n'est pas dans le prix.", True),
    ], notes="La dernière réplique annonce tout le bloc D. Le dire au groupe : ce "
             "qu'ils viennent d'entendre va arriver dans deux semaines.")

    d.tableau('Analyse', "Les mots des papiers",
              ['Le mot', 'Ce que c\'est'],
              [["le rapport", "un document qui décrit l'état réel, sans prix"],
               ["le taux", "un chiffre mesuré, en pourcentage"],
               ["les exclusions", "ce qui n'est pas compris dans le prix"],
               ["l'échéancier", "le calendrier des travaux, séchage compris"]],
              cle=0,
              note="Deux de ces quatre mots décident de la facture finale.",
              notes="Diapositive à photographier. Faire deviner lesquels : les "
                    "exclusions et l'échéancier. Le taux d'humidité, lui, décide de "
                    "la date, ce qui revient au même.")

    d.regle("Savoir dans lequel des deux chercher",
            "Un état est dans le rapport ; une intention est dans la soumission.",
            precision="Chercher un prix dans un rapport, c'est perdre dix minutes : il "
                      "n'en donne pas, exprès. Croire une soumission sur l'état d'un "
                      "mur, c'est plus grave : elle décrit ce qu'elle fera, pas ce "
                      "qui est. Quand les deux papiers ne s'accordent pas sur l'état "
                      "du bâtiment, c'est le rapport qui l'emporte.",
            notes="Diapositive à photographier. C'est la règle du bloc C.")

    d.pratique('Pratique', "Dans lequel des deux ?",
               "Dites où se trouve chaque renseignement, et à quel endroit.", [
        ("le taux d'humidité du mur nord", "le rapport, section 2"),
        ("le montant à verser à la signature", "la soumission, sous le total"),
        ("l'année de construction", "le rapport, section 1"),
        ("ce qui n'est pas compris dans le prix", "la soumission, tout en bas"),
        ("ce que l'inspectrice n'a pas pu voir", "le rapport, section 4"),
        ("la durée de validité du prix", "la soumission, première ligne"),
    ], corrige=True,
       notes="Exercice central de la séance. Demander chaque fois : est-ce un état ou "
             "une intention ? C'est le raisonnement, la réponse vient ensuite.")

    d.billet(
        "Quel document as-tu déjà reçu sans savoir ce qu'il fallait y chercher ?",
        exemples=[
            "Un bail, une assurance, un avis de la ville, un relevé.",
            "Dis ce que tu aurais voulu y trouver.",
        ],
        notes="Trois minutes. Les documents nommés servent en C2 et C3 : la plupart "
              "ont une section de limites ou d'exclusions que personne n'a lue.")

    return d.save(dossier)
