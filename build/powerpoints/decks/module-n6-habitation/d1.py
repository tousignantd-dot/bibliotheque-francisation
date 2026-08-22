# -*- coding: utf-8 -*-
"""D1 · La rencontre du 8 avril
Bloc D « Défi 3 · Quand le plan change » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3choix`, cartes de FC_CARDS de la
section t3. Savoir du programme : saisir les rapports entre des interlocutrices
ou des interlocuteurs.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="La rencontre du 8 avril",
        chapeau="Le plancher est ouvert, et ce qu'on trouve n'était pas dans "
                "le prix. Quatre personnes parlent, chacune de son point de "
                "vue, et c'est la propriétaire qui doit décider.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc D, et c'est la séance la plus dense du module : "
                  "quatre locuteurs, deux solutions chiffrées, un permis. Prévoir "
                  "trois écoutes du dialogue, avec une consigne différente chaque "
                  "fois.")

    d.objectifs([
        "suivre une conversation à quatre voix ;",
        "dire qui parle au nom de quoi ;",
        "comparer deux solutions par leur prix et leur délai ;",
        "nommer ce qu'on trouve en ouvrant un plancher.",
    ], notes="Le deuxième objectif est le savoir que le programme n'introduit qu'au "
             "niveau 6 : saisir les rapports entre les interlocuteurs. Le nommer au "
             "groupe.")

    d.declencheur(
        'Observation', "Trois personnes vous conseillent en même temps. Comment décidez-vous ?",
        pistes=[
            "Qui a un intérêt dans votre décision, et qui n'en a pas ?",
            "Laquelle des trois paiera si vous vous trompez ?",
            "Comment demander à quelqu'un de parler un à la fois ?",
        ],
        notes="La dernière question s'exerce pour vrai : « Allez-y. Une à la fois, "
              "s'il vous plaît. » C'est la phrase de Doïna dans le dialogue, et elle "
              "vaut d'être apprise telle quelle.")

    d.dialogue('Dialogue · 1 de 3', "Ce qu'on a trouvé", [
        ("FERNAND", "Tout le monde est là. Madame Alcindor, et monsieur Toupin est au téléphone. On a ouvert le plancher hier matin.", True),
        ("FERNAND", "On a trouvé deux choses. Un : il n'y a aucune membrane sous la dalle. En 1961, ça ne se faisait pas. Deux : il y a un vieux puisard, sous le coin, qui avait été condamné par quelqu'un avant vous.", True),
        ("KETTLY", "Rempli de pierre et coulé par-dessus. Ça se voyait nulle part : c'est exactement la « condition non visible » dont on parlait la semaine passée.", True),
        ("DOÏNA", "Donc ce n'est pas dans le prix.", True),
    ], consigne="Première écoute : qui parle, et au nom de quoi ?",
       notes="Faire relever les quatre voix et leur rôle avant d'aller plus loin. "
             "L'entrepreneur exécute, l'inspectrice constate, la ville autorise, la "
             "propriétaire décide et paie.")

    d.dialogue('Dialogue · 2 de 3', "Deux solutions, deux prix", [
        ("FERNAND", "Première solution : on casse la dalle, on pose une membrane et un drain neuf, on recoule. Six mille huit cents dollars, neuf jours ouvrables de plus.", True),
        ("FERNAND", "Deuxième : on laisse la dalle, on pose une membrane par-dessus, puis un plancher flottant. Mille neuf cents dollars, deux jours.", True),
        ("DOÏNA", "Quelle est la différence, dans dix ans ?", True),
        ("KETTLY", "La deuxième tolère l'humidité, elle ne l'arrête pas. Si l'eau revient, vous refaites tout, et vous payez le premier prix en plus du deuxième.", True),
    ], consigne="Deuxième écoute : notez les deux prix et les deux délais.",
       notes="La question de Doïna — « quelle est la différence, dans dix ans ? » — "
             "est la meilleure du module. La faire remarquer : elle contient un "
             "« quelle » et une échéance, et c'est elle qui obtient la vraie réponse.")

    d.dialogue('Dialogue · 3 de 3', "Le permis, et la décision", [
        ("RÉJEAN", "Si vous refaites la dalle, vous touchez à la structure, et je veux voir le plan modifié. Si vous posez un plancher flottant, c'est du revêtement, et je n'ai rien à voir là-dedans.", True),
        ("DOÏNA", "Et si je vous envoie le plan modifié, ça prend combien de temps ?", True),
        ("RÉJEAN", "Dix jours ouvrables. Et ne vous fiez pas à ce que votre voisin a vécu : chaque municipalité a ses propres exigences.", True),
        ("DOÏNA", "Je prends la première solution, parce que je ne veux pas payer deux fois. Vous m'écrivez les deux prix aujourd'hui, et je signe demain matin.", True),
    ], consigne="Troisième écoute : qu'est-ce que Doïna décide, et pourquoi ?",
       notes="La dernière réplique est le modèle de la production orale de E1 et du "
             "courriel de E2. La faire relire deux fois : une décision, une raison, "
             "une demande écrite, une date.")

    d.tableau('Analyse', "Qui parle au nom de quoi",
              ['La personne', 'Ce qu\'elle apporte'],
              [["l'entrepreneur", "ce qui est possible, à quel prix, en combien de jours"],
               ["l'inspectrice", "ce qui est, et ce que ça donnera dans dix ans"],
               ["le service des permis", "ce que la ville autorise, et le délai"],
               ["la propriétaire", "la décision, et l'argent"]],
              cle=0,
              note="Une seule des quatre paiera si la décision est mauvaise.",
              notes="Diapositive à photographier. C'est le tableau du bloc D. La note "
                    "est ce qui remet la propriétaire au centre : personne ne décide "
                    "à sa place, et personne ne pose ses questions.")

    d.tableau('Analyse', "Ce qu'on trouve en ouvrant",
              ['Le mot', 'Ce que c\'est'],
              [["la dalle", "le béton coulé à plat qui sert de plancher"],
               ["une membrane", "la feuille étanche qui arrête l'humidité du sol"],
               ["un imprévu", "une condition qui n'était pas visible à la visite"],
               ["un acompte", "la part du prix versée d'avance, contre reçu"]],
              cle=0,
              note="« Imprévu » a ici un sens précis, et il coûte cher.",
              notes="Diapositive à photographier. Insister sur le sens contractuel "
                    "d'« imprévu » : ce n'est pas une surprise désagréable, c'est ce "
                    "que la soumission a exclu par écrit.")

    d.pratique('Compréhension', "De quelle solution s'agit-il ?",
               "Dites s'il s'agit de casser la dalle, du plancher flottant, ou des deux.", [
        ("6 800 $ et neuf jours ouvrables de plus", "casser la dalle"),
        ("1 900 $ et deux jours", "le plancher flottant"),
        ("il faut poser une membrane", "les deux"),
        ("le service des permis veut voir le plan modifié", "casser la dalle"),
        ("la solution tolère l'humidité au lieu de l'arrêter", "le plancher flottant"),
        ("un drain neuf est posé sous la dalle", "casser la dalle"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la réplique. La troisième est celle "
             "qu'on manque : les deux solutions posent une membrane, seule sa place "
             "change.")

    d.billet(
        "Laquelle des deux solutions choisirais-tu, et pourquoi ?",
        exemples=[
            "Deux phrases : la décision, et la raison.",
            "Il n'y a pas de bonne réponse.",
        ],
        notes="Trois minutes. Faire un tour de table rapide des deux camps : les deux "
              "choix se défendent, et c'est ce qui rend l'exercice honnête. Ce que "
              "le module évalue, c'est la raison donnée, pas le choix.")

    return d.save(dossier)
