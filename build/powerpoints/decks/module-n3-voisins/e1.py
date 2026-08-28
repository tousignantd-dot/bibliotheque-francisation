# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 75 min.
Source : jeu de rôle, production orale et production écrite du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='Je me lance',
        chapeau="Les trois défis se rassemblent en une seule visite : on "
                "frappe, on demande sa permission, on invite, on décrit, on "
                "remercie. Une production orale, un carton à écrire.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Prévoir des écouteurs : la production orale se "
                  "fait à l'ordinateur, chacun de son côté, et c'est ce qui permet à un "
                  "élève timide de se reprendre dix fois sans témoin.")

    d.objectifs([
        "tenir une conversation complète avec une voisine ;",
        "employer les trois défis dans une même production ;",
        "écrire le carton qu'on glisse sous les portes ;",
        "recevoir une correction et la relire.",
    ])

    d.cartes('Les trois défis, réunis', "Ce qui doit apparaître", [
        ("Défi 1 · demander",
         "S'annoncer, dire la raison, demander la permission poliment, et comprendre la "
         "réponse — oui, oui mais, ou non."),
        ("Défi 2 · inviter",
         "Donner le jour, l'heure et l'endroit. Répondre à « est-ce que j'apporte quelque "
         "chose ? ». Faire un compliment."),
        ("Défi 3 · décrire",
         "Dire la couleur, la taille, puis le détail — pour un objet trouvé, un animal, "
         "ou une personne qu'on cherche."),
    ], notes="Diapo à photographier. C'est la grille de la production orale, et c'est "
             "aussi celle avec laquelle l'enseignante écoute.")

    d.regle("Le jeu de rôle vient en premier",
            "Trois situations, deux rôles, autant de reprises qu'on veut.",
            precision="Dans l'activité : la <b>remise de la cour</b> "
                      "(demander une permission), le <b>café de samedi</b> "
                      "(inviter), l'<b>affiche dans l'entrée</b> (décrire un "
                      "chat perdu). L'assistant joue la voisine — et il ne "
                      "dit rien qu'on ne lui demande pas.",
            notes="Insister sur la dernière phrase : la permission, le nom du concierge, "
                  "la couleur du chat, tout se demande. Un élève qui attend que "
                  "l'assistant parle n'obtient rien, et c'est exactement la leçon.")

    d.pratique('Production orale', "Ce qui est demandé",
               "Environ 45 secondes, à l'ordinateur.", [
        ("Temps 1 · saluer", "dire bonjour et donner en une phrase la raison de la visite"),
        ("Temps 2 · demander", "poser la permission : « est-ce que je pourrais… ? »"),
        ("Temps 3 · inviter", "le jour, l'heure et l'endroit — les trois"),
        ("Temps 4 · remercier", "« merci, c'est gentil » avant de partir"),
    ], cols=1,
       notes="On s'enregistre, on s'écoute, on recommence autant de fois qu'on veut. Rien "
             "ne part avant que l'élève appuie sur envoyer : le rappeler avant de "
             "commencer enlève la moitié de la peur.")

    d.piege("Réciter le dialogue au lieu de parler",
            "Apprendre les répliques de Rachid par cœur et les redire.",
            "Employer les structures avec ses propres mots et sa propre situation.",
            "Une voisine réelle ne donnera pas la réplique attendue. Ce qui se "
            "réemploie, ce sont les structures — « excusez-moi de vous "
            "déranger », « est-ce que je pourrais », « c'est samedi, à deux "
            "heures » — jamais les phrases entières.",
            notes="Rassurer : hésiter, se reprendre et chercher un mot est normal et "
                  "n'est pas pénalisé. C'est même le signe qu'on parle au lieu de "
                  "réciter.")

    d.pratique('Production écrite', "Ce qui est demandé",
               "Le carton glissé sous les portes, de 5 à 8 phrases.", [
        ("L'occasion", "pourquoi vous invitez — une phrase suffit"),
        ("Les trois", "le jour, l'heure et l'endroit, avec le numéro de porte"),
        ("Ce qu'il y aura", "et ce qu'on apporte, ou pas"),
        ("Le futur simple", "« La rencontre aura lieu… », « Il y aura… »"),
        ("La réponse", "« Confirmez SVP », et comment répondre"),
        ("La signature", "votre nom et votre numéro de porte"),
    ], cols=1,
       notes="Les billets de C2, C3 et C4 contiennent déjà presque tout : le faire "
             "remarquer avant de commencer. L'élève assemble plutôt qu'il n'invente, et "
             "c'est ce qui rend l'exercice tenable en une séance.")

    d.regle("Deux détails d'écriture qui se voient",
            "samedi le 14, à 14 h",
            precision="Les noms de jours ne prennent pas de majuscule — on "
                      "écrit « samedi », jamais « Samedi ». Et l'heure "
                      "s'écrit avec une espace avant le h : « 14 h », pas "
                      "« 14h ».",
            notes="Diapo à photographier. Ce sont les deux erreurs que la correction "
                  "signale le plus souvent sur cette tâche. Les dire avant, plutôt que "
                  "de les corriger vingt fois après.")

    d.tableau('Analyse', "Ce qui est regardé",
              ['Le critère', 'Ce qui compte'],
              [["La tâche", "les quatre temps sont là"],
               ["Le vocabulaire", "les mots du module sont employés"],
               ["La langue", "la demande polie, les trois renseignements"],
               ["La clarté", "on comprend du premier coup"]],
              cle=3,
              note="La clarté passe avant la perfection : une phrase simple "
                   "et juste vaut mieux qu'une phrase compliquée et fausse.",
              notes="Diapo à photographier. Le dire avant que les élèves commencent, pas "
                    "au moment de rendre les corrections.")

    d.billet(
        "Notez ce que la correction vous a signalé.",
        exemples=[
            "Deux choses réussies, deux choses à travailler.",
            "Gardez la note : elle sert à la séance E2.",
        ],
        notes="La correction n'est pas conservée par le système : elle s'affiche et elle "
              "disparaît. Cette note est la seule trace qu'il en restera, et il faut le "
              "dire clairement pour que les élèves la prennent.")

    return d.save(dossier)
