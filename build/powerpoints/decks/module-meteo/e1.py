# -*- coding: utf-8 -*-
"""E1 · À toi : planifier et écrire un bulletin.
Bloc E · couleur teal (je me lance) · 90 min.
Source : section `appli` — planifier une journée, puis rédiger un bulletin météo.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='À toi : planifier et écrire',
        chapeau="Tout le module en une séance. Expliquer une décision à un collègue, "
                "puis rédiger le bulletin qu'on voudrait entendre : celui qui dit quoi "
                "faire, pas seulement quel temps il fera.",
        duree='90 minutes')

    d.titre(notes="Séance d'application. Aucun contenu nouveau. Un tiers d'oral, un "
                  "tiers d'écrit, un tiers de relecture croisée.")

    d.objectifs([
        "expliquer une décision prise à cause de la météo ;",
        "rédiger un bulletin météo au futur simple ;",
        "écrire un message d'équipe avec une condition ;",
        "relire un texte en vérifiant les temps et les pronoms.",
    ])

    # ── premier temps · l'oral ─────────────────────────────────────
    d.regle("À l'oral · les quatre phrases",
            "La décision · la raison · la règle · la solution de rechange.",
            precision="C'est la structure de B5, et elle vaut pour toute annulation. La "
                      "quatrième phrase est celle qui distingue une annulation d'une "
                      "journée perdue.",
            notes="Écrire les quatre au tableau avant de lancer les dyades.")

    d.pratique('Pratique · 1 de 4', "Jeu de rôle · annoncer et convaincre",
               "À deux. L'un annonce, l'autre insiste. Puis on échange.", [
        ("Vous annoncez", "la décision, avec la raison chiffrée"),
        ("Le collègue insiste", "« on a du retard », « j'ai l'équipement »"),
        ("Vous reconnaissez son point", "puis vous revenez à la règle"),
        ("Vous refermez", "sur ce qu'on fait à la place"),
    ], corrige=False,
       notes="Vingt minutes. Circuler et vérifier une seule chose : la règle chiffrée "
             "est-elle citée ? C'est le critère du module.")

    # ── deuxième temps · le bulletin ───────────────────────────────
    d.tableau('Écrire', "Un bulletin, en cinq phrases",
              ['La phrase', 'Le temps'],
              [["ce qui se passe maintenant", "présent"],
               ["ce qui est prévu en avant-midi", "futur simple"],
               ["ce qui est prévu en après-midi", "futur simple"],
               ["les accumulations attendues", "futur simple"],
               ["ce qui est prévu demain", "futur simple"]],
              cle=1, props=[0.65, 0.35],
              note="Une seule phrase au présent : celle qui décrit maintenant. Tout le "
                   "reste est au futur.",
              notes="C'est le squelette du bulletin de B1. Le faire retrouver dans le "
                    "texte avant de rédiger.")

    d.cartes('Écrire', "Quatre choses à mettre dans un bulletin", [
        ("Les chiffres avec leurs unités",
         "Degrés, kilomètres à l'heure, centimètres. Un bulletin sans chiffres ne sert "
         "à rien : personne ne peut décider."),
        ("Les moments de la journée",
         "Avant-midi, après-midi, en soirée, demain. Une prévision sans moment est "
         "inutilisable."),
        ("Ce que ça change concrètement",
         "« La chaussée restera glissante », « une journée idéale pour les travaux en "
         "hauteur ». C'est ce qu'on retient."),
        ("La zone visée",
         "« Pour la Montérégie », « sur la Rive-Sud ». La météo n'est jamais la même "
         "partout."),
    ], notes="La troisième carte est ce qui distingue un bon bulletin : il traduit les "
             "chiffres en conséquences.")

    d.pratique('Pratique · 2 de 4', "Rédigez le bulletin",
               "Cinq phrases, au futur simple sauf la première.", [
        ("Ce qui se passe maintenant", "au présent, avec « déjà » si c'est en cours"),
        ("L'avant-midi et l'après-midi", "au futur, avec les chiffres et les heures"),
        ("Les accumulations", "au futur, avec une fourchette : deux à quatre centimètres"),
        ("Demain", "au futur, avec une conséquence pratique"),
    ], corrige=False,
       notes="Vingt minutes d'écriture individuelle. Choisir la vraie météo du jour "
             "plutôt qu'une situation inventée.")

    # ── troisième temps · le message ───────────────────────────────
    d.regle("Le message à l'équipe",
            "La décision · la condition · ce qu'on fait en attendant.",
            precision="« On ne monte pas ce matin. Si l'avertissement est levé avant "
                      "midi, je vous envoie un message. En attendant, on prépare le "
                      "bardeau à l'atelier. » Trois phrases, et toute l'équipe sait "
                      "quoi faire.",
            notes="Faire remarquer le « si » de la deuxième phrase et le « vous » de la "
                  "troisième : c'est C4 et C3 réunis.")

    d.pratique('Pratique · 3 de 4', "Écrivez le message d'équipe",
               "Trois phrases. Une condition, un pronom complément.", [
        ("La décision", "ce qui est annulé, et pourquoi"),
        ("La condition", "avec « si », au présent puis au futur"),
        ("En attendant", "la tâche de remplacement"),
    ], corrige=False,
       notes="Quinze minutes. Ramasser : ces messages sont l'évaluation écrite du "
             "module.")

    d.piege("Le piège du bulletin sans conséquence",
            "Rafales de 60 km/h, mercure à moins six.",
            "Rafales de 60 km/h : aucun travail en hauteur aujourd'hui.",
            "Des chiffres seuls obligent chacun à faire le calcul. Un bulletin qui dit ce "
            "que ça change — la chaussée restera glissante, la journée conviendra aux "
            "toitures — est celui qu'on écoute vraiment.",
            notes="Faire ajouter une conséquence à chaque phrase des bulletins écrits. "
                  "La différence est immédiate.")

    d.pratique('Pratique · 4 de 4', "Relecture croisée",
               "Échangez les textes. Six vérifications.", [
        ("Les chiffres ont-ils tous une unité ?", "degrés, km/h, cm"),
        ("Les moments de la journée sont-ils nommés ?", "avant-midi, après-midi, demain"),
        ("Les verbes de prévision sont-ils au futur ?", "cherchez le son r"),
        ("Y a-t-il un futur après « si » ?", "s'il y en a un, le corriger"),
        ("Les pronoms sont-ils bien placés ?", "lui et leur devant le verbe"),
        ("Est-ce qu'on sait quoi faire de sa journée ?", "sinon, ajouter une conséquence"),
    ], corrige=True,
       notes="Une relecture croisée trouve deux fois plus d'erreurs qu'une relecture par "
             "l'auteur. Ramasser les versions corrigées.")

    d.billet(
        "En une phrase : qu'est-ce que vous comprenez mieux dans un bulletin qu'au début du module ?",
        exemples=[
            "Une seule chose, précise.",
            "Exemple : « je sais maintenant que le vent qui tombe, c'est bon signe ».",
        ],
        notes="Lire quelques billets à voix haute, sans nommer les auteurs. C'est la "
              "meilleure préparation à la séance de bilan.")

    return d.save(dossier)
