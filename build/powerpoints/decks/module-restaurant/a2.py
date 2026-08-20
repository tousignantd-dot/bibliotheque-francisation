# -*- coding: utf-8 -*-
"""A2 · Le « e » qui tombe.
Bloc A « Je découvre » · couleur teal · 60 min.
Source : mini-leçon `prPhon`, exercice `prPhon` (cartes à écouter).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='teal',
        titre='Le « e » qui tombe',
        chapeau="« Qu'est-ce que vous prenez ? » devient « qu'est-c'que vous "
                "prenez ? ». Ce n'est pas de la négligence : en français "
                "parlé, beaucoup de « e » disparaissent.",
        duree='60 minutes')

    d.titre(notes="Séance d'écoute. Prévoir le son. Commencer par dire la phrase du chapeau "
                  "à vitesse normale, puis lentement. L'écart frappe.")

    d.objectifs([
        "reconnaître les petits mots dont le « e » tombe ;",
        "réinsérer le « e » pour retrouver la phrase écrite ;",
        "savoir que rien de tout cela ne s'écrit ;",
        "comprendre un serveur qui parle vite.",
    ])

    d.declencheur(
        'Écoute', "Qu'est-ce que vous entendez ?",
        pistes=[
            "« J'vais prendre la table d'hôte. »",
            "« Kesskvouprené ? »",
            "Combien de mots y a-t-il dans la deuxième phrase ?",
            "Que manque-t-il, à votre avis ?",
        ],
        notes="Faire écouter les deux phrases avant toute explication. La deuxième "
              "ressemble à un seul mot long : c'est exactement l'effet à faire vivre.")

    d.tableau('Analyse', "Les petits mots qui perdent leur e",
              ['On écrit', 'On entend souvent'],
              [["je vais prendre", "j'vais prendre"],
               ["qu'est-ce que vous prenez", "qu'est-c'que vous prenez"],
               ["je ne sais pas", "j'sais pas"],
               ["s'il vous plaît", "s'y vous plaît"]],
              cle=1,
              note="je, ce, de, le, que, ne, te : ce sont eux qui perdent leur voyelle.",
              notes="Diapo centrale. Faire recopier. La liste des mots concernés est courte "
                    "et ce sont les plus fréquents du français.")

    d.regle("Le réflexe qui débloque",
            "Quand un groupe semble être un mot inconnu, réinsérez un « e ».",
            precision="« Kesskvouprené » redevient « qu'est-ce que vous prenez ». « J'sais "
                      "pas » redevient « je ne sais pas ». Dans presque tous les cas, la "
                      "phrase réapparaît d'un coup.",
            notes="Diapo à photographier. C'est une stratégie d'écoute, pas une règle de "
                  "grammaire.")

    d.regle("Vous n'avez pas à parler comme ça",
            "Parler lentement et complètement est parfaitement correct.",
            precision="Un serveur préfère largement une phrase claire à une imitation "
                      "approximative. Ce qu'il faut, c'est <b>reconnaître</b> la forme "
                      "resserrée — parce que c'est celle que vous entendrez.",
            notes="Le dire clairement : plusieurs élèves croient devoir imiter ce parler "
                  "rapide pour être acceptés. Ce n'est pas le cas.")

    d.piege("Écrire ce qu'on entend",
            "J'vais prendre le poulet.",
            "Je vais prendre le poulet.",
            "Cette chute n'existe qu'à l'oral. À l'écrit, tous les « e » sont là, sans "
            "exception. « J'vais » ne s'écrit que dans les dialogues de roman, pour imiter "
            "la parole.",
            notes="Rassurer : entendre cette chute est le signe d'une bonne oreille, pas "
                  "d'une mauvaise mémoire.")

    d.pratique('Pratique · 1 de 2', "Le e tombe, ou pas ?",
               "Écoutez chaque phrase.", [
        ("Je vais prendre la table d'hôte.", "il tombe — j'vais"),
        ("Je regarde le menu.", "on l'entend"),
        ("Qu'est-ce que vous prenez ?", "il tombe — deux fois"),
        ("Vous avez fait votre choix ?", "on l'entend"),
        ("Je ne sais pas encore.", "il tombe — et le « ne » disparaît"),
        ("Ce serait possible ?", "on l'entend"),
    ], corrige=True,
       notes="Utiliser l'exercice 2 du module. Deux écoutes avant de corriger.")

    d.pratique('Pratique · 2 de 2', "Réinsérez le e",
               "Écrivez la phrase complète.", [
        ("« J'vais prendre le poulet. »", "Je vais prendre le poulet."),
        ("« Qu'est-c'que vous prenez ? »", "Qu'est-ce que vous prenez ?"),
        ("« J'sais pas encore. »", "Je ne sais pas encore."),
        ("« C'pas grave. »", "Ce n'est pas grave."),
    ], corrige=True, cols=1,
       notes="La dernière est la plus resserrée : deux mots entiers ont disparu. Elle "
             "s'entend pourtant tous les jours.")

    d.cartes("Pourquoi ça compte au restaurant", "Trois raisons", [
        ("Le serveur répète les mêmes phrases",
         "Vingt fois par soir. À force, elles se resserrent — ce n'est pas contre vous."),
        ("La salle est bruyante",
         "Une phrase resserrée dans le bruit devient presque inaudible. Demander de "
         "répéter est normal, y compris pour les gens d'ici."),
        ("Vous savez déjà ce qu'il va dire",
         "« Vous avez fait votre choix ? », « quelque chose à boire ? », « ensemble ou "
         "séparé ? ». Connaître les questions d'avance vaut mieux que tout entendre."),
    ], notes="La troisième carte est la vraie stratégie du module : anticiper les questions "
             "plutôt que déchiffrer chaque syllabe.")

    d.billet(
        "Notez trois phrases entendues cette semaine que vous n'avez pas comprises du premier coup.",
        exemples=[
            "Écrivez-les comme vous les avez entendues.",
            "Essayez de réinsérer les « e » : la phrase réapparaît-elle ?",
        ],
        notes="Les relevés font une excellente ouverture de la séance suivante. Les décoder "
              "en groupe est souvent spectaculaire.")

    return d.save(dossier)
