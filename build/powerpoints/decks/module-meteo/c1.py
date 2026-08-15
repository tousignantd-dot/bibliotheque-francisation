# -*- coding: utf-8 -*-
"""C1 · Prisca et Mado avant le départ.
Bloc C · couleur acier (compréhension orale) · 60 min.
Source : dialogue `t2`, exercices `t2vf` et `t2accli`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Prisca et Mado avant le départ',
        chapeau="La route est ouverte, mais la visibilité tombe sous deux cents mètres. "
                "Ouverte ne veut pas dire sûre — et c'est toute la différence entre "
                "partir et attendre.",
        duree='60 minutes')

    d.titre(notes="Ouverture du défi 2. Demander : est-ce qu'une route ouverte est "
                  "forcément praticable ? Beaucoup répondront oui. C'est la leçon.")

    d.objectifs([
        "comprendre un échange sur l'état d'une route ;",
        "distinguer « ouverte » de « praticable » ;",
        "savoir à qui demander avant de partir ;",
        "proposer une solution en attendant.",
    ])

    d.dialogue('Dialogue · 1 de 3', "Est-ce que l'autoroute 10 est praticable ?", [
        ("PRISCA", "Mado, je pars pour le chantier de Granby. Est-ce que l'autoroute 10 "
                   "est praticable ?", True),
        ("MADO", "Attends, je regarde le site du ministère des Transports… Il y a un "
                 "avertissement de poudrerie entre Sainte-Julie et Marieville.", True),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="Passer l'audio du défi 2. Faire remarquer le mot « praticable » : Prisca ne "
             "demande pas si la route est ouverte, mais si on peut y rouler.")

    d.dialogue('Dialogue · 2 de 3', "Est-ce qu'on ferme la route ?", [
        ("PRISCA", "Est-ce qu'on ferme la route ?", True),
        ("MADO", "Non, elle reste ouverte, mais la visibilité tombe à moins de deux "
                 "cents mètres.", True),
        ("PRISCA", "Je devrais peut-être attendre que le vent faiblisse.", True),
    ], notes="La réponse de Mado contient un « mais » : la route est ouverte ET "
             "dangereuse. Les deux à la fois. C'est le cœur de la séance.")

    d.dialogue('Dialogue · 3 de 3', "Je leur envoie un message", [
        ("MADO", "C'est ce que je conseille à tout le monde ce matin. Je leur envoie un "
                 "message dès que l'avertissement sera levé.", True),
        ("PRISCA", "Parfait. Je vais préparer les feuilles de temps pendant ce temps-là.",
         True),
    ], notes="Deux choses : Mado emploie « leur » (séance C3) et Prisca propose une tâche "
             "de remplacement (séance B5). Le module se referme sur lui-même.")

    d.regle('La règle du défi 2',
            "Ouverte ne veut pas dire praticable.",
            precision="Une route reste ouverte tant qu'elle n'est pas physiquement "
                      "bloquée. La visibilité, la glace et le vent peuvent la rendre "
                      "dangereuse sans qu'elle soit fermée. La décision revient au "
                      "conducteur.",
            notes="Écrire la règle au tableau. C'est un savoir de sécurité routière "
                  "autant que de langue.")

    d.tableau('Analyse', "Trois mots à ne pas confondre",
              ['Le mot', 'Ce qu\'il dit'],
              [["fermée", "on ne peut pas y aller, c'est bloqué"],
               ["ouverte", "on peut y aller, rien ne bloque"],
               ["praticable", "on peut y rouler en sécurité"]],
              cle=0,
              note="Une route peut être ouverte sans être praticable. L'inverse "
                   "n'existe pas.",
              notes="Faire produire trois phrases avec les trois mots. La distinction "
                    "devient claire tout de suite.")

    d.cartes('Analyse', "Quatre choses à vérifier avant de partir", [
        ("L'avertissement routier",
         "Le site du ministère des Transports le publie par tronçon d'autoroute. C'est "
         "plus précis que le bulletin météo général."),
        ("La visibilité annoncée",
         "Sous cinq cents mètres, on ralentit. Sous deux cents mètres, on ne devrait "
         "pas partir."),
        ("L'état de la chaussée",
         "Sèche, mouillée, enneigée, glacée. Les sites d'information routière emploient "
         "ces quatre mots."),
        ("Qui prévenir",
         "Le répartiteur ou le superviseur, avant de partir et en cas de changement. "
         "Personne ne devrait rouler sans que quelqu'un le sache."),
    ], notes="La quatrième carte est un réflexe de sécurité au travail : prévenir avant "
             "de prendre la route en conditions difficiles.")

    d.pratique('Pratique · 1 de 4', "Vrai ou faux",
               "D'après le dialogue.", [
        ("L'autoroute 10 est fermée à la circulation.", "FAUX — elle reste ouverte"),
        ("Un avertissement de poudrerie touche le secteur de Marieville.", "VRAI"),
        ("Mado consulte le site du ministère des Transports.", "VRAI"),
        ("La visibilité reste excellente sur tout le trajet.",
         "FAUX — moins de deux cents mètres"),
        ("Prisca part tout de suite, malgré l'avertissement.", "FAUX — elle attend"),
        ("Mado préviendra l'équipe quand l'avertissement sera levé.", "VRAI"),
    ], corrige=True,
       notes="Le premier énoncé est le piège : « ouverte » et « fermée » sont dits dans "
             "la même réplique. Faire réécouter.")

    d.pratique('Pratique · 2 de 4', "Cinq questions",
               "Répondez par une phrase complète.", [
        ("Pourquoi Prisca parle-t-elle à Mado avant de partir ?",
         "Pour savoir si l'autoroute 10 est praticable."),
        ("Que signifie le mot « poudrerie » ?",
         "De la neige déjà tombée que le vent soulève."),
        ("Pourquoi une route ouverte peut-elle rester dangereuse ?",
         "Parce que la visibilité peut tomber sous deux cents mètres."),
        ("Que fera Mado dès que l'avertissement sera levé ?",
         "Elle enverra un message à toute l'équipe."),
        ("Que fera Prisca en attendant ?", "Elle préparera les feuilles de temps."),
    ], corrige=True,
       notes="La cinquième réponse reprend l'idée de la solution de rechange, vue en B5. "
             "Le faire remarquer.")

    d.piege("Le piège de la route ouverte",
            "La route est ouverte, donc je peux partir.",
            "La route est ouverte, mais la visibilité est à deux cents mètres.",
            "Le ministère ferme rarement une autoroute : il avertit. C'est au conducteur "
            "de décider, et l'avertissement existe précisément pour qu'il décide en "
            "connaissance de cause.",
            notes="Point de sécurité important. Beaucoup d'élèves croient qu'une route "
                  "dangereuse serait fermée.")

    d.piege("Le piège du départ sans prévenir",
            "Je pars, ils le sauront bien.",
            "Je préviens le répartiteur avant de partir.",
            "En conditions difficiles, quelqu'un doit savoir que vous êtes sur la route "
            "et à quelle heure vous devriez arriver. Si vous n'arrivez pas, c'est cette "
            "information qui déclenche les recherches.",
            notes="Le dire simplement, sans dramatiser. C'est une pratique courante dans "
                  "les métiers du transport et de la construction.")

    d.pratique('Pratique · 3 de 4', "Partir ou attendre ?",
               "Donnez la décision et la raison.", [
        ("Route ouverte, visibilité à 800 mètres, chaussée sèche.", "partir — conditions normales"),
        ("Route ouverte, visibilité à 200 mètres, poudrerie.", "attendre — visibilité trop faible"),
        ("Route ouverte, chaussée glacée, pas de vent.", "attendre ou rouler très lentement"),
        ("Route fermée entre deux sorties.", "attendre — pas le choix"),
        ("Avertissement levé, chaussée enneigée.", "partir, en prévoyant plus de temps"),
    ], corrige=True,
       notes="Faire justifier chaque décision par un chiffre ou un mot de l'avertissement. "
             "Ne jamais accepter « parce que ça a l'air correct ».")

    d.pratique('Pratique · 4 de 4', "Que faites-vous en attendant ?",
               "Une tâche utile par situation.", [
        ("Vous êtes au bureau", "préparer les documents, les feuilles de temps"),
        ("Vous êtes à la maison", "prévenir le client, replanifier la journée"),
        ("Vous êtes à l'atelier", "entretenir les outils, préparer le matériel"),
        ("Vous êtes déjà en route", "vous arrêter à une halte et prévenir"),
    ], corrige=True,
       notes="Le quatrième cas est celui qu'on oublie : que faire quand on est déjà "
             "parti ? S'arrêter et prévenir, jamais continuer par entêtement.")

    d.billet(
        "Écrivez ce que vous diriez à un collègue qui veut partir malgré l'avertissement.",
        exemples=[
            "Trois phrases : le fait, le risque, la proposition.",
            "Sans lui donner d'ordre — vous n'êtes pas son superviseur.",
        ],
        notes="Situation délicate et réaliste. Lire quelques billets : les formulations "
              "varient beaucoup et méritent d'être comparées.")

    return d.save(dossier)
