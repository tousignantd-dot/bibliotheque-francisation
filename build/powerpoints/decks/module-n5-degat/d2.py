# -*- coding: utf-8 -*-
"""D2 · Mettre en avant, dire la cause.
Bloc D « Défi 3 · La réclamation » · couleur ambre · 75 min. Grammaire et écriture.
Source : exercices `t3emph`, `t3conn` et `t3lettre`, mini-leçons du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Mettre en avant, dire la cause",
        chapeau="Une demande qui aboutit dit trois choses : ce qu'on a perdu, "
                "pourquoi c'est arrivé, ce qu'on veut. Deux points de langue "
                "suffisent à les relier.",
        duree='75 minutes')

    d.titre(notes="Séance dense : deux points de grammaire et une lettre. Prévoir de "
                  "commencer la lettre en classe et de la finir dans le module "
                  "interactif — c'est la production écrite de E2.")

    d.objectifs([
        "mettre en avant un élément avec « c'est… qui », « c'est… que » ;",
        "employer « ce qui / ce que…, c'est » pour ouvrir une demande ;",
        "relier une cause et une conséquence ;",
        "employer le deux-points qui explique.",
    ])

    d.regle("À l'oral la voix, à l'écrit une tournure",
            "L'emphase encadre le mot important pour qu'on ne puisse pas le manquer.",
            precision="Quand vous parlez, vous appuyez sur le mot qui compte et tout le "
                      "monde comprend. À l'écrit, la voix ne passe pas : il faut une "
                      "construction. Dans une lettre de réclamation, c'est l'outil le "
                      "plus utile que vous ayez — il dit ce qui compte sans hausser le "
                      "ton.",
            notes="Faire lire une phrase à plat, puis la même en insistant à l'oral, puis "
                  "sa version emphatique écrite. Les trois à la suite.")

    d.tableau('Les trois tournures emphatiques', "Une seule par phrase",
              ['La tournure', 'Un exemple du module'],
              [["c'est … qui", "C'est le chauffe-eau du dessus qui a lâché."],
               ["c'est … que", "C'est pendant la nuit que le dégât est arrivé."],
               ["ce qui …, c'est", "Ce qui m'inquiète, c'est l'humidité du matelas."],
               ["ce que …, c'est", "Ce que je demande, c'est une réduction de loyer."]],
              cle=0,
              note="« qui » si le mot encadré fait l'action ; « que » dans tous les autres cas.",
              notes="La note est la seule chose à retenir pour choisir. Un seul test, une "
                    "seule question.")

    d.pratique('Pratique · exercice t3emph', "Mettez en avant la partie soulignée",
               "Employez la tournure qui convient.",
               [("<Le chauffe-eau du dessus> a lâché.",
                 "C'est le chauffe-eau du dessus qui a lâché."),
                ("Le dégât est arrivé <pendant la nuit>.",
                 "C'est pendant la nuit que le dégât est arrivé."),
                ("<L'humidité dans le matelas> m'inquiète.",
                 "Ce qui m'inquiète, c'est l'humidité dans le matelas."),
                ("Je demande <une réduction de loyer>.",
                 "Ce que je demande, c'est une réduction de loyer."),
                ("<J'>ai appelé le propriétaire à six heures et demie.",
                 "C'est moi qui ai appelé le propriétaire.")],
               corrige=True, cols=1,
               notes="La dernière porte l'accord : « c'est moi qui ai appelé », jamais "
                     "« qui a appelé ». C'est l'erreur la plus fréquente du point.")

    d.tableau('Cause et conséquence', "Les mots qui font tenir une demande",
              ['Le connecteur', 'Ce qu\'il fait'],
              [["puisque · étant donné que · comme",
                "rappelle une cause que le lecteur connaît déjà"],
               ["parce que · car",
                "apporte une cause comme une information nouvelle"],
               ["c'est pourquoi · par conséquent · donc",
                "annonce la demande : sa place est juste avant"],
               ["le deux-points",
                "remplace « parce que », en plus net"]],
              cle=0,
              note="Une cause, une conséquence, puis on change de phrase.",
              notes="La différence entre les deux premières lignes est fine mais utile : "
                    "« puisque » rappelle, « parce que » apprend.")

    d.regle("Le deux-points qui explique",
            "Je n'ai rien jeté : je voulais tout faire constater.",
            precision="Ce deux-points-là annonce une cause ou une explication, pas une "
                      "énumération. C'est précisément celui que le programme du niveau 5 "
                      "attend, avec la virgule qui ferme une subordonnée placée en tête "
                      "de phrase : « Comme la fuite venait d'en haut, j'ai averti ma "
                      "voisine. »",
            notes="Deux points de ponctuation nommés explicitement dans les attentes de "
                  "fin de cours. Le dire : ça motive.")

    d.pratique('Pratique · exercice t3conn', "Le bon connecteur",
               "Chacun ne s'emploie qu'une fois.",
               [("___ la fuite venait du logement du dessus, je ne suis pas responsable.",
                 "Étant donné que"),
                ("Je n'ai pas pu dormir dans ma chambre ___ le matelas était humide.",
                 "parce que"),
                ("Le logement était inutilisable ; ___ , je demande une réduction.",
                 "par conséquent"),
                ("Je n'ai rien jeté ___ je voulais tout faire constater.",
                 "un deux-points"),
                ("___ vous m'aviez confirmé une intervention, j'ai attendu.", "Comme")],
               corrige=True, cols=1,
               notes="Faire justifier le choix de la première : pourquoi « étant donné "
                     "que » plutôt que « parce que » ? Parce que le propriétaire le sait "
                     "déjà.")

    d.cartes("Les cinq parties d'une demande écrite", "Cinq lignes suffisent", [
        ("Les faits, datés",
         "« Le 10 novembre au matin, un dégât d'eau est survenu dans ma chambre. »"),
        ("Ce que vous avez perdu, chiffré",
         "« Les travaux ont duré trois jours, pendant lesquels je n'ai pas pu occuper ma chambre. »"),
        ("La cause, sans accusation",
         "« Étant donné que la cause se trouvait dans un autre logement… »"),
        ("La demande, avec un montant",
         "« Par conséquent, je demande une réduction équivalant à trois jours, soit 90 $. »"),
    ], notes="Il y a une cinquième partie : le délai. Elle est sur la diapositive "
             "suivante, parce que c'est celle qu'on oublie.")

    d.regle("Une demande sans chiffre se répond par « on verra »",
            "Le loyer mensuel divisé par 30, multiplié par le nombre de jours.",
            precision="900 $ par mois, trois jours sans chambre : 900 ÷ 30 × 3 = 90 $. Le "
                      "calcul est simple et vérifiable par l'autre partie, ce qui est "
                      "exactement le but. Ajoutez la date limite — « je vous saurais gré "
                      "de me répondre avant le 30 novembre » — et votre lettre est "
                      "complète.",
            notes="Faire faire le calcul avec le loyer réel de deux ou trois élèves qui "
                  "acceptent. Le montant devient concret d'un coup.")

    d.piege("Menacer dès la première lettre",
            "Sinon j'irai au Tribunal.",
            "Je vous saurais gré de me répondre avant le 30 novembre.",
            "Chaque étape a son ton, et on ne brûle pas la première. La menace a sa "
            "place — dans la mise en demeure, qui vient après une lettre restée sans "
            "réponse. Annoncée trop tôt, elle durcit une discussion qui pouvait se "
            "régler en deux courriels.",
            notes="Point de stratégie. Le dire clairement : ce n'est pas une question de "
                  "politesse, c'est une question d'efficacité.")

    d.billet(
        "Écrivez les deux phrases centrales de votre lettre.",
        exemples=[
            "La cause : « Étant donné que… »",
            "La demande : « Par conséquent, je demande… , soit … $. »",
        ],
        notes="Cinq minutes. Ces deux phrases forment le cœur de la production écrite de "
              "E2 : les garder.")

    return d.save(dossier)
