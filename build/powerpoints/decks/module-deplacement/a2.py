# -*- coding: utf-8 -*-
"""A2 · Les consonnes qui tombent.
Bloc A « Je découvre » · couleur teal · 60 min.
Source : mini-leçon `prPhon`, exercice `prPhon` (cartes à écouter).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='teal',
        titre='Les consonnes qui tombent',
        chapeau="Vous connaissez le mot « quelque », mais vous entendez « quek ». "
                "Vous connaissez « plus », mais vous entendez « pu ». Ce n'est "
                "pas votre oreille : c'est le français parlé.",
        duree='60 minutes')

    d.titre(notes="Séance d'écoute. Prévoir le son et l'essayer avant l'arrivée du groupe. "
                  "Elle explique une frustration que beaucoup d'élèves traînent depuis des "
                  "mois.")

    d.objectifs([
        "savoir que la dernière consonne d'un groupe tombe souvent à l'oral ;",
        "rendre à un mot incomplet sa consonne manquante ;",
        "reconnaître quelque, plus, quatre, autre et notre dans une phrase rapide ;",
        "savoir que rien de tout cela ne change à l'écrit.",
    ])

    d.declencheur(
        'Écoute', "Quel mot entendez-vous ?",
        pistes=[
            "« Il y a quek chose devant la porte. »",
            "« On se voit pu tard. »",
            "« Ça prend quat minutes. »",
            "Ces mots existent-ils ? Que manque-t-il ?",
        ],
        notes="Faire écouter les trois phrases du module avant toute explication. Laisser "
              "le groupe chercher. Quelqu'un finira par dire « quelque » — c'est le moment "
              "de la séance.")

    d.tableau('Analyse', "La même consonne, deux sorts",
              ['Ce qui suit', 'Ce qui arrive'],
              [["une consonne", "la dernière consonne tombe"],
               ["une voyelle", "on l'entend, et elle se lie"],
               ["une pause", "on l'entend"]],
              cle=0,
              note="C'est le mot SUIVANT qui décide, pas le mot lui-même.",
              notes="Diapo centrale. Faire recopier. Elle explique pourquoi le même mot "
                    "sonne différemment d'une phrase à l'autre.")

    d.cartes('Les cinq mots les plus touchés', "Ce qu'on écrit, ce qu'on entend", [
        ("quelque",
         "« quek chose » devant une consonne. C'est le mot le plus déformé du français "
         "parlé courant."),
        ("plus",
         "« pu tard » devant une consonne. Attention : « plus » tout seul, en fin de "
         "phrase, garde son son."),
        ("quatre",
         "« quat minutes ». Le « r » final tombe devant toutes les consonnes."),
        ("autre et notre",
         "« aut chose », « not voisin ». Mais « notre arrêt » se dit en entier — le mot "
         "suivant commence par une voyelle."),
    ], notes="Faire produire les deux versions de « notre » par le groupe : « not voisin » "
             "puis « notre arrêt ». C'est le meilleur exemple du tableau précédent.")

    d.regle("Ce que vous devez faire",
            "Quand un mot semble incomplet, rendez-lui sa dernière consonne.",
            precision="« Quek » n'existe pas ; « quelque » existe. Ne cherchez pas un mot "
                      "inconnu : cherchez un mot connu auquel il manque la fin. Dans neuf "
                      "cas sur dix, le mot réapparaît immédiatement.",
            notes="C'est une stratégie d'écoute, pas une règle de grammaire. Le dire "
                  "clairement : on travaille la compréhension.")

    d.piege("Écrire ce qu'on entend",
            "Ça prend quat minutes.",
            "Ça prend quatre minutes.",
            "Cette chute n'existe qu'à l'oral. À l'écrit, absolument rien ne change : "
            "on écrit toujours le mot en entier. L'erreur vient d'élèves qui apprennent "
            "beaucoup à l'oreille — c'est une qualité, mais il faut faire la correction.",
            notes="Rassurer : entendre cette chute est le signe d'une bonne oreille.")

    d.pratique('Pratique', "Elle tombe, ou on l'entend ?",
               "Écoutez chaque groupe de mots.", [
        ("quelque chose", "elle tombe — consonne après"),
        ("quel âge", "on l'entend — voyelle après"),
        ("plus tard", "elle tombe — consonne après"),
        ("quatre minutes", "elle tombe — consonne après"),
        ("notre arrêt", "on l'entend — voyelle après"),
        ("notre voisin", "elle tombe — consonne après"),
    ], corrige=True,
       notes="Utiliser l'exercice 2 du module. Deux écoutes avant de donner la réponse. "
             "Les élèves peuvent le refaire seuls après le cours.")

    d.cartes('Pourquoi ça compte ici', "Les annonces du transport", [
        ("Elles sont rapides",
         "Une annonce de métro dure trois secondes. Toutes les consonnes qui peuvent "
         "tomber tombent."),
        ("Elles sont souvent mal audibles",
         "Haut-parleur, bruit de foule, tunnel. Vous n'entendrez jamais tout : il faut "
         "reconstituer."),
        ("Elles suivent toujours la même forme",
         "C'est ce qui sauve. On travaillera cette forme au bloc D — et connaître la forme "
         "vaut mieux qu'entendre chaque syllabe."),
    ], notes="Annoncer le bloc D dès maintenant : les élèves comprennent mieux l'utilité de "
             "cette séance quand ils savent où elle mène.")

    d.billet(
        "Notez trois mots que vous entendez souvent sans les reconnaître.",
        exemples=[
            "À la radio, au travail, dans l'autobus.",
            "Écrivez-les comme vous les entendez : on les identifiera ensemble.",
        ],
        notes="Excellent départ pour la séance suivante. Écrire les relevés au tableau et "
              "les décoder en groupe : c'est souvent spectaculaire.")

    return d.save(dossier)
