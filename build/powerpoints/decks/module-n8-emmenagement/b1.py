# -*- coding: utf-8 -*-
"""B1 · L'appel au courtier
Bloc B « Défi 1 · Ce qui est couvert » · couleur acier · 75 min.
Compréhension orale. Source du module : le dialogue `t1` et l'exercice `t11`.

L'extrait de ce défi contient un **exposé de quatorze répliques d'affilée** du
même locuteur, coupé par deux questions : la forme que le programme du niveau 8
appelle « suivre le déroulement d'exposés bien structurés ». Toute la séance
est bâtie là-dessus, en trois écoutes à consigne différente.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="L'appel au courtier",
        chapeau="Trente-six répliques, dont quatorze d'affilée par la même "
                "personne. On n'écoute pas un exposé comme on écoute une "
                "conversation.",
        duree='75 minutes')

    d.titre(notes="Séance d'écoute longue, la plus exigeante du module. "
                  "Prévoir trois écoutes complètes de l'extrait : le module "
                  "ne fonctionne pas avec une seule.")

    d.objectifs([
        "suivre un exposé de quatorze répliques sans perdre le fil ;",
        "prélever un fait à la première écoute, des chiffres à la deuxième ;",
        "repérer ce qui est dit deux fois — c'est ce qui compte ;",
        "reformuler à la fin, comme Amira le fait.",
    ], notes="Les trois écoutes ont trois consignes différentes. C'est la "
             "méthode que le niveau 8 demande, et elle s'enseigne : dire "
             "avant chaque écoute ce qu'on cherche.")

    d.declencheur(
        'Avant d\'écouter', "Qu'est-ce que votre assurance habitation couvre, "
                            "exactement ?",
        pistes=[
            "Vos meubles ? Le logement ? Les dommages que vous causez aux autres ?",
            "Combien payez-vous de franchise, et savez-vous ce que c'est ?",
            "Qui, dans la classe, a déjà lu son contrat en entier ?",
        ],
        notes="La troisième question ne reçoit presque jamais de main levée, "
              "et c'est le meilleur début possible pour cette séance. Ne pas "
              "corriger les réponses fausses maintenant : l'extrait le fera.")

    d.tableau('Analyse', "Trois écoutes, trois consignes",
              ['L\'écoute', 'Ce qu\'on cherche'],
              [["Première", "de quoi parle-t-on, et qui sont les deux personnes"],
               ["Deuxième", "les chiffres : plafonds, franchise, millions"],
               ["Troisième", "ce que le courtier dit deux fois"]],
              cle=0,
              note="Annoncer la consigne AVANT chaque écoute, jamais après.",
              notes="Diapositive à photographier. Ce qui est dit deux fois "
                    "dans l'extrait : qu'un refus sans clause n'est pas un "
                    "refus, et qu'il ne faut rien accepter du déménageur "
                    "avant la décision.")

    d.dialogue('Écoute', "Ce que ma police couvre vraiment", [
        ("AMIRA", "J'ai eu des dommages. Avant de réclamer, j'aimerais comprendre ce que j'ai acheté.", True),
        ("GHISLAIN", "C'est la meilleure question que vous puissiez me poser, et la plupart des gens la posent après le sinistre.", False),
        ("GHISLAIN", "Trois choses qui n'ont rien à voir entre elles : vos biens, votre responsabilité civile, vos frais de subsistance.", True),
        ("AMIRA", "Attendez. « Valeur à neuf », « franchise » — pouvez-vous me redire ça autrement ?", True),
        ("GHISLAIN", "Un refus sans clause n'est pas un refus, c'est une opinion.", True),
        ("AMIRA", "Je résume, pour être certaine : je déclare, je monte un inventaire, j'attends l'expert.", True),
    ], consigne="Six répliques sur trente-six. Cinq sont en couleur : ce sont "
                "celles qu'on redemandera.",
       notes="Faire écouter l'extrait entier avant d'afficher. Les deux "
             "répliques d'Amira en évidence sont des gestes de langue, pas "
             "des renseignements : faire clarifier, puis résumer. C'est ce "
             "que la séance B5 travaillera pour lui-même.")

    d.regle("Déclarer, ce n'est pas réclamer",
            "La déclaration dit qu'il s'est passé quelque chose. Elle n'engage à rien, et elle se fait le jour même.",
            precision="La réclamation vient après, avec un inventaire et des "
                      "preuves. Attendre d'avoir tout chiffré pour appeler "
                      "fait perdre trois semaines et affaiblit le dossier.",
            notes="Diapositive à photographier. C'est le renseignement le "
                  "plus utile de l'extrait, et celui que les élèves "
                  "retiennent le moins spontanément.")

    d.pratique('Pratique', "Vrai ou faux",
               "Écoutez de nouveau, puis répondez.", [
        ("Amira appelle son courtier avant d'avoir déclaré son sinistre.", "VRAI"),
        ("La franchise s'applique une fois par objet endommagé.", "FAUX"),
        ("Elle est indemnisée à la valeur au jour du sinistre.", "FAUX"),
        ("Selon le courtier, un refus doit toujours s'appuyer sur une clause.", "VRAI"),
        ("Une preuve d'achat doit obligatoirement être une facture.", "FAUX"),
        ("Le courtier conseille de s'entendre d'abord avec le déménageur.", "FAUX"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t11` du module, dans sa version projetée. "
             "Quatre « faux » sur six : c'est voulu, chacun corrige une idée "
             "reçue que la classe a exprimée au déclencheur.")

    d.billet(
        "Écris la question que tu poserais à ton courtier demain matin.",
        exemples=[
            "Une seule question, et elle doit appeler un chiffre ou un mot précis.",
            "Pas « est-ce que je suis bien couvert ? » — trop large.",
        ],
        notes="Cinq minutes. Ramasser et trier en deux piles : les questions "
              "qui appellent un chiffre, et les autres. Rendre les secondes à "
              "reformuler — c'est l'objet de la séance B5.")

    return d.save(dossier)
