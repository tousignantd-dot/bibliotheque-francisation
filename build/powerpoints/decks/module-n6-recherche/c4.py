# -*- coding: utf-8 -*-
"""C4 · La lettre de motivation.
Bloc C « Défi 2 · La demande » · couleur ambre · 75 min. Fin du Défi 2.
Source : exercices `t2lettre` et `t2form`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n6-recherche/')


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="La lettre de motivation",
        chapeau="Trois paragraphes, une demi-page, et des formules qui ne "
                "s'inventent pas. Ce qui est figé se recopie : le français ne "
                "se dépense que dans le deuxième paragraphe.",
        duree='75 minutes')

    d.titre(notes="Séance d'écriture. Prévoir du temps réel pour rédiger : la lettre "
                  "doit sortir de cette séance, au moins en brouillon.")

    d.objectifs([
        "écrire l'appel et la salutation d'une lettre professionnelle ;",
        "organiser la lettre en trois paragraphes ;",
        "reprendre les mots exacts de l'offre ;",
        "remplir la rubrique d'expérience de la demande d'emploi.",
    ])

    d.declencheur(
        'Observation', "Comment commence-t-on une lettre à un employeur ?",
        image=IMG + 'vocab/lettre-motivation.jpg',
        pistes=[
            "« Bonjour » ?",
            "« Salut » ?",
            "« À qui de droit » ?",
            "Et si on connaît le nom de la personne ?",
        ],
        notes="« Bonjour » vient toujours en premier — c'est ce qu'on écrit dans un "
              "courriel entre collègues. Le distinguer d'une candidature.")

    d.tableau('Structure', "Trois paragraphes, et rien de plus",
              ['Le paragraphe', 'Ce qu\'il contient'],
              [["1. Pourquoi j'écris", "Le titre exact du poste et où vous l'avez vu."],
               ["2. Ce que j'apporte", "Deux phrases, avec un chiffre. C'est le seul endroit qui vous appartient."],
               ["3. Ce que je demande", "Vous restez disponible pour une rencontre, et vous remerciez."]],
              cle=0,
              note="Une demi-page. Un employeur qui reçoit quarante candidatures donne trente secondes à chacune.",
              notes="Diapositive à photographier. Le fait que seul le paragraphe 2 change "
                    "d'une lettre à l'autre est ce qui rend l'exercice tenable.")

    d.cartes("Les formules figées", "À recopier telles quelles", [
        ("Madame, Monsieur,",
         "L'appel, quand on ne connaît pas le nom. Avec le nom : « Madame Toubaï, »."),
        ("Je vous soumets ma candidature au poste de…",
         "La première phrase. Le titre du poste se recopie mot pour mot depuis l'offre."),
        ("Je demeure disponible pour vous rencontrer.",
         "Ce que vous demandez, sans insister."),
        ("Veuillez agréer, Madame, Monsieur, mes salutations distinguées.",
         "La sortie. Elle reprend exactement l'appel du début."),
    ], notes="Faire écrire les quatre formules au propre dans le cahier. Elles serviront "
             "toute la vie professionnelle, pas seulement dans ce module.")

    d.pratique('Application', "Complétez la formule",
               "Ce sont des expressions figées.", [
        ("On ne connaît pas le nom : « ___ , Monsieur, »", "Madame"),
        ("« Je vous ___ ma candidature au poste de… »", "soumets"),
        ("« Je demeure ___ pour vous rencontrer. »", "disponible"),
        ("« Je vous ___ de l'attention portée à ma demande. »", "remercie"),
        ("« Veuillez ___ , Madame, Monsieur, mes salutations distinguées. »", "agréer"),
    ], corrige=True,
       notes="« Agréer » ne s'emploie nulle part ailleurs. Le dire : c'est un mot de "
             "formule, pas un mot de langue courante.")

    d.regle("Reprendre les mots de l'offre",
            "L'employeur reconnaît son propre vocabulaire.",
            precision="Si l'offre dit « tenir l'inventaire à jour », écrivez « j'ai tenu "
                      "l'inventaire à jour ». Deux ou trois expressions reprises "
                      "suffisent : la lecture devient facile, et le lien entre votre "
                      "expérience et le besoin se fait tout seul. Ce n'est pas de la "
                      "copie, c'est de la correspondance.",
            notes="Diapositive à photographier. Faire souligner, dans l'offre de chacun, "
                  "les trois expressions à reprendre.")

    d.pratique('Rédaction', "Le paragraphe 2, celui qui vous appartient",
               "Deux phrases, avec un chiffre et deux mots repris de l'offre.", [
        ("Votre durée d'expérience", "J'ai ___ ans d'expérience en…"),
        ("Une preuve chiffrée", "…dont l'inventaire de 800 références."),
        ("Un mot repris de l'offre", "…tenir l'inventaire à jour, comme le demande votre offre."),
    ], corrige=True,
       notes="Circuler et corriger individuellement. C'est le passage où le niveau de "
             "chacun se voit, et où l'aide vaut le plus.")

    d.piege("Raconter toute sa vie",
            "Une lettre de deux pages, avec tout le parcours.",
            "Une demi-page, trois paragraphes, un chiffre.",
            "Une lettre longue n'est pas lue jusqu'au bout, et ce qui compte s'y perd. "
            "Le curriculum vitæ porte déjà les faits ; la lettre dit seulement ce qu'ils "
            "veulent dire pour ce poste-ci.",
            notes="Rassurer ceux qui trouvent leur lettre trop courte : c'est le format "
                  "attendu.")

    d.billet(
        "Écrivez votre lettre de motivation au complet.",
        exemples=[
            "Trois paragraphes, l'appel et la salutation.",
            "Relisez à voix haute avant de la remettre : une lettre courte et juste vaut mieux qu'une longue avec des fautes.",
        ],
        notes="La lettre se corrige à la séance suivante ou dans « Je me lance », où "
              "l'assistant donne une rétroaction immédiate.")

    return d.save(dossier)
