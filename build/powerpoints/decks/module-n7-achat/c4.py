# -*- coding: utf-8 -*-
"""C4 · Mettre en avant, et demander sans sommer
Bloc C « Défi 2 · La réclamation au comptoir » · couleur ambre · grammaire ·
75 min.
Source : exercices `t2emph` et `t2cond` et leurs mini-leçons ; savoirs
« phrases emphatiques » (cinq points) et « indicatif conditionnel présent »
(cinq points) du niveau 7.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="Mettre en avant, et demander sans sommer",
        chapeau="La personne au comptoir retient la première moitié de "
                "votre phrase. Deux procédés décident vous-même de ce "
                "qu'elle emportera.",
        duree='75 minutes')

    d.titre(notes="Deux points de grammaire dans la même séance, et c'est voulu : ils "
                  "se combinent dans la même phrase. « Ce que je demande, c'est que "
                  "vous acceptiez de réparer » contient les deux.")

    d.objectifs([
        "mettre un mot en relief avec « c'est… qui » et « c'est… que » ;",
        "mettre une idée en relief avec « ce que… c'est » ;",
        "former le conditionnel présent à partir du radical du futur ;",
        "savoir quand passer du conditionnel à l'indicatif.",
    ], notes="Le quatrième objectif est celui qui relie le bloc C au bloc D : "
             "conditionnel au comptoir, indicatif dans la lettre. C'est la progression "
             "qui rend une mise en demeure méritée.")

    d.declencheur(
        'Observation', "Ces deux phrases disent-elles la même chose ?",
        pistes=[
            "« La garantie légale s'applique. »",
            "« C'est la garantie légale qui s'applique, pas la prolongée. »",
            "Laquelle des deux retiendra la personne au comptoir ?",
            "Qu'est-ce qui a changé dans la deuxième, exactement ?",
        ],
        notes="Rien n'a changé sur le fond : les mêmes mots, dans un autre ordre. "
              "C'est le point de départ de la séance, et il rassure ceux qui croient "
              "qu'on va leur demander du vocabulaire nouveau.")

    d.tableau('Analyse', "Deux procédés de mise en relief",
              ['La forme', 'Quand l\'employer'],
              [["c'est… qui", "l'élément mis en avant est le sujet"],
               ["c'est… que", "dans tous les autres cas"],
               ["ce que… c'est", "pour une idée entière"],
               ["ce n'est pas… c'est", "la plus forte : elle écarte et elle pose"],
               ["moi, je… ; l'auto, elle…", "à l'oral seulement, jamais dans la lettre"]],
              cle=0,
              notes="Diapositive à photographier. La dernière rangée est celle qu'on "
                    "oublie de dire : la reprise pronominale est excellente en parlant "
                    "et refusée à l'écrit formel.")

    d.regle("« Ce que je demande, c'est… » annonce qu'il n'y a qu'une demande",
            "C'est la phrase la plus rentable du module.",
            precision="Elle coupe court à la négociation : une seule chose est sur la "
                      "table, et l'autre doit répondre à celle-là. Deux demandes dans "
                      "le même échange en font un marchandage, et le commerçant "
                      "accordera la moins chère. Cette règle vaut aussi pour la lettre "
                      "du bloc D.",
            notes="Diapositive à photographier. Faire formuler à chacun sa phrase, "
                  "avec sa vraie demande. Deux minutes, et on la retrouve en E1.")

    d.pratique('Grammaire', "Mettez en relief",
               "Refaites la phrase avec le procédé indiqué.", [
        ("La garantie légale s'applique. (c'est… qui)", "C'est la garantie légale qui s'applique."),
        ("Je demande la réparation. (ce que… c'est)", "Ce que je demande, c'est la réparation."),
        ("Je conteste l'exclusion. (forme négative)", "Ce n'est pas le prix que je conteste, c'est l'exclusion."),
        ("J'ai posé la question deux fois. (c'est… qui)", "C'est moi qui ai posé la question deux fois."),
        ("Vous devez réparer avant vendredi. (c'est… que)", "C'est avant vendredi que vous devez réparer."),
        ("Le rapport établit la fuite. (c'est… qui)", "C'est le rapport qui établit la fuite."),
    ], corrige=True,
       notes="Le quatrième item porte le piège de l'accord : « c'est moi qui ai », "
             "jamais « qui a ». Le verbe suit le pronom mis en relief. Corriger tout "
             "de suite et à voix haute.")

    d.tableau('Analyse', "Le conditionnel présent",
              ['La pièce', 'Où on la prend'],
              [["Le radical", "celui du futur, sans exception"],
               ["Les terminaisons", "celles de l'imparfait"],
               ["Les irréguliers", "les mêmes qu'au futur"],
               ["Le s à « je »", "toujours : je voudrais, pas je voudrai"],
               ["Ce qu'il change", "le ton, jamais le contenu"]],
              cle=0,
              notes="Diapositive à photographier. La quatrième rangée mérite un arrêt : "
                    "à l'oral la différence ne s'entend presque pas, à l'écrit elle "
                    "transforme une demande en annonce.")

    d.pratique('Grammaire', "Mettez au conditionnel présent",
               "Le verbe entre parenthèses.", [
        ("(accepter) ___ -vous de faire réparer la transmission sans frais ?", "Accepteriez"),
        ("Je (vouloir) ___ savoir à quelle catégorie appartient mon véhicule.", "voudrais"),
        ("Me (passer) ___ -vous une autre voiture en attendant ?", "passeriez"),
        ("Il me (falloir) ___ une copie du rapport.", "faudrait"),
        ("J'(aimer) ___ que la réponse me soit donnée par écrit.", "aimerais"),
        ("Ce (être) ___ possible de faire le travail chez mon garage ?", "serait"),
    ], corrige=True,
       notes="Le troisième item est l'exemple que donne le programme lui-même pour "
             "cette situation. Le signaler : ce n'est pas une phrase inventée par le "
             "module.")

    d.piege('Piège', "rester au conditionnel dans la lettre",
            "passer à l'indicatif une fois le délai posé",
            "« Je vous demanderais de procéder » n'est pas une mise en demeure : c'est "
            "encore une demande. Dans la lettre, on écrit « je vous demande de "
            "procéder ». Le conditionnel au comptoir, l'indicatif dans la lettre — "
            "c'est cette progression qui rend l'écrit crédible.",
            notes="Annoncer que le bloc D repose là-dessus. Les élèves qui écriront "
                  "leur lettre au conditionnel auront été prévenus deux séances "
                  "d'avance.")

    d.billet(
        "Écris ta demande au comptoir : une phrase emphatique et une demande au conditionnel.",
        exemples=[
            "« Ce que je demande, c'est… »",
            "« Accepteriez-vous de… ? »",
        ],
        notes="Cinq minutes. Ces deux phrases sont celles que chacun dira en E1 : les "
              "faire écrire maintenant évite de les improviser le jour du jeu de rôle.")

    return d.save(dossier)
