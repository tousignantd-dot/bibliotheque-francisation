# -*- coding: utf-8 -*-
"""C1 · La question courte.
Bloc C « Défi 2 · L'étiquette et l'affichette » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2combien`, mini-leçon `t2combien`.

La séance orale du module. Le programme du niveau 2 demande des phrases
interrogatives partielles sans inversion, avec le mot interrogatif en fin de
phrase : « c'est combien ? », « c'est où ? ». C'est exactement ce qu'on dit
dans un magasin, et c'est déjà suffisant.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-panier/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="La question courte",
        chapeau="Quatre questions de trois mots suffisent pour tout trouver "
                "dans un magasin.",
        duree='75 minutes')

    d.titre(notes="Séance de parole. Rassurer d'entrée : on ne demande pas de faire de "
                  "longues phrases. Trois mots bien placés valent mieux qu'une phrase "
                  "hésitante de dix.")

    d.objectifs([
        "demander le prix d'un produit ;",
        "demander dans quelle allée il se trouve ;",
        "demander le format ;",
        "faire répéter plus lentement.",
    ])

    d.declencheur(
        'Observation', "À qui demander, et quoi ?",
        image=IMG + 'produits-entretien.jpg',
        pistes=[
            "Que voit-on sur cette tablette ?",
            "Comment savoir lequel prendre ?",
            "À qui demande-t-on dans un magasin ?",
            "Quelle question posez-vous en premier ?",
        ],
        notes="Amener le mot « commis ». Beaucoup d'élèves n'osent pas demander : dire "
              "clairement que c'est le travail du commis de répondre.")

    d.dialogue('Dialogue · 1 de 2', "Je cherche le savon à vaisselle", [
        ("AMINATA", "Bonjour. Je cherche le savon à vaisselle.", True),
        ("DENIS", "Allée 7, madame. Au fond, à droite.", True),
        ("AMINATA", "Allée 7. C'est loin ?", True),
        ("DENIS", "Non, tout droit. Sur la tablette du milieu.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire remarquer la deuxième réplique d'Aminata : elle répète « allée 7 » "
             "avant de poser sa question suivante. C'est ce qui l'empêche d'oublier.")

    d.dialogue('Dialogue · 2 de 2', "Et c'est combien ?", [
        ("AMINATA", "Merci. Et c'est combien ?", True),
        ("DENIS", "Quatre dollars vingt-neuf pour le grand format.", True),
        ("AMINATA", "Quatre dollars vingt-neuf. Merci beaucoup.", True),
    ], notes="Trois répliques, deux informations, un merci. C'est la longueur réelle d'un "
             "échange dans un magasin — le dire au groupe rassure beaucoup.")

    d.tableau('Analyse', "Quatre questions, et on trouve tout",
              ['Ce qu\'on veut savoir', 'Ce qu\'on dit'],
              [["le prix", "C'est combien ? · Ça coûte combien ?"],
               ["le rayon", "C'est où ? · C'est dans quelle allée ?"],
               ["le format", "C'est quel format ? · C'est le kilo ou le sac ?"],
               ["on n'a pas compris", "Pouvez-vous répéter, s'il vous plaît ?"]],
              cle=2,
              note="Aucune de ces questions ne dépasse cinq mots.",
              notes="Diapositive à photographier. La faire recopier telle quelle : c'est "
                    "une fiche de survie, pas un exercice.")

    d.regle("Le mot interrogatif va à la fin",
            "« Ça coûte combien ? », et non « combien ça coûte ? ».",
            precision="C'est la forme la plus simple du français parlé, et elle est tout à "
                      "fait correcte : « C'est <b>combien</b> ? », « C'est <b>où</b> ? », "
                      "« C'est <b>quel format</b> ? ». Personne ne la corrigera.",
            notes="Diapositive à photographier. Insister : les élèves croient souvent que "
                  "la forme courte est fautive. Elle ne l'est pas.")

    d.piege('Le piège', "parler plus fort", "parler plus lentement",
            "Quand on n'est pas compris, le réflexe est de hausser la voix. Ce n'est "
            "presque jamais le volume qui manque : c'est la vitesse. La bonne phrase est "
            "« <b>plus lentement, s'il vous plaît</b> », et elle vaut dans les deux sens.",
            notes="Faire répéter la phrase en chœur, trois fois. C'est celle qui sauve le "
                  "plus de conversations, dans ce module comme ailleurs.")

    d.pratique('Production orale', "Que dites-vous ?",
               "Une question courte pour chaque situation.", [
        ("Vous voulez savoir le prix.", "C'est combien ?"),
        ("Vous cherchez le rayon d'un produit.", "C'est dans quelle allée ?"),
        ("Vous voulez savoir si c'est le kilo ou le sac.", "C'est quel format ?"),
        ("Vous n'avez pas compris le prix.", "Pouvez-vous répéter, s'il vous plaît ?"),
        ("Vous voulez savoir si le spécial est encore bon.", "C'est encore le spécial ?"),
    ], corrige=True, cols=1,
       notes="Tout à l'oral d'abord, chacun son tour, debout si possible. L'écrit vient "
             "après, et seulement pour ceux qui en ont besoin.")

    d.pratique('Pratique · à deux', "Le commis et le client",
               "Deux par deux. Trois échanges chacun, puis on change.", [
        ("Étape 1", "Dites bonjour et nommez le produit que vous cherchez."),
        ("Étape 2", "Demandez l'allée. Répétez le numéro."),
        ("Étape 3", "Demandez le prix. Répétez le prix."),
        ("Étape 4", "Remerciez."),
    ], cols=1,
       notes="Vingt-cinq minutes. Le commis a le droit d'inventer les allées et les prix. "
             "Ce qui compte, c'est la répétition à l'étape 2 et à l'étape 3.")

    d.billet(
        "Apprenez ces quatre questions par cœur.",
        exemples=[
            "C'est combien ?",
            "C'est dans quelle allée ?",
            "C'est quel format ?",
            "Pouvez-vous répéter, s'il vous plaît ?",
        ],
        notes="Devoir de mémoire, sans écriture. Leur dire qu'ils peuvent les essayer "
              "pour vrai avant le prochain cours : c'est le but.")

    return d.save(dossier)
