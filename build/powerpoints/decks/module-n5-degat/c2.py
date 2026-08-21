# -*- coding: utf-8 -*-
"""C2 · La formule officielle et ce qu'elle veut dire.
Bloc C « Défi 2 · L'avis » · couleur teal · 75 min. Compréhension écrite.
Source : exercice `t2sens`, mini-leçon `t2sens`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='teal',
        titre="La formule officielle et ce qu'elle veut dire",
        chapeau="La langue administrative n'est celle de personne — ni parlée, "
                "ni littéraire. Elle revient pourtant à l'école, à la ville et "
                "chez l'assureur.",
        duree='75 minutes')

    d.titre(notes="Séance de traduction, au sens propre : du français administratif vers "
                  "le français de tous les jours. C'est un exercice que les élèves "
                  "réclament souvent sans savoir le nommer.")

    d.objectifs([
        "reconnaître les formules courantes d'un document officiel ;",
        "les redire en français ordinaire, sans rien perdre ;",
        "repérer ce qui vous engage dans un paragraphe ;",
        "savoir qu'une formule vague n'est pas un délai.",
    ])

    d.regle("Traduire dans ses mots, à la première personne",
            "« Il est nécessaire que les occupants libèrent l'accès » "
            "devient « je dois tasser mes meubles ».",
            precision="C'est le geste à faire devant chaque avis, et il ne prend que "
                      "quelques secondes. Tant que la phrase reste à la troisième "
                      "personne et au passif, elle ne vous atteint pas vraiment ; "
                      "traduite à la première personne, elle devient une tâche datée.",
            notes="Faire faire l'opération à voix haute sur deux ou trois phrases avant "
                  "l'exercice. C'est la compétence de la séance, pas la reconnaissance "
                  "des formules.")

    d.tableau('Formules · 1 de 2', "Du document au réel",
              ['La formule', 'Ce qu\'elle dit'],
              [["Veuillez prévoir un accès.", "Quelqu'un doit pouvoir ouvrir."],
               ["À défaut, nous aviserons le propriétaire.",
                "Sinon, il appellera le propriétaire."],
               ["Il est nécessaire de libérer l'accès.", "Tassez vos meubles."],
               ["Les travaux seront effectués.", "On fera les travaux."]],
              cle=1,
              note="La version ordinaire n'est pas plus longue.",
              notes="Faire lire la colonne de gauche par un élève et celle de droite par "
                    "un autre : entendre les deux à la suite installe la paire.")

    d.tableau('Formules · 2 de 2', "Celles qui trompent le plus",
              ['La formule', 'Ce qu\'elle dit'],
              [["Le cas échéant…", "Si ça arrive…"],
               ["dans les meilleurs délais", "vite, mais sans date"],
               ["Aucune interruption n'est prévue.", "On ne devrait pas couper l'eau."],
               ["Le bruit est important et continu.", "Du bruit jour et nuit."]],
              cle=1,
              note="« N'est prévue » et « devrait » ne sont pas des garanties.",
              notes="La dernière ligne fonde la demande du défi 3. La signaler sans "
                    "encore l'expliquer.")

    d.cartes("Trois signaux à repérer d'un coup d'œil", "Ils marquent le paragraphe qui engage", [
        ("À défaut",
         "Si vous ne le faites pas. La suite dit ce que l'autre fera à votre place."),
        ("Faute de quoi",
         "Sinon. La formule la plus directe des trois."),
        ("Le cas échéant",
         "Si le cas se présente. Elle annonce une éventualité, pas une certitude."),
    ], cols=1,
       notes="Les faire surligner dans l'avis affiché en C1. Trouver ces trois mots-là, "
             "c'est trouver l'obligation en dix secondes.")

    d.pratique('Pratique · exercice t2sens', "Redites-le en français ordinaire",
               "Une phrase par formule. À la première personne quand c'est possible.",
               [("Veuillez prévoir un accès au logement.",
                 "Il faut que quelqu'un puisse ouvrir."),
                ("À défaut, l'entrepreneur communiquera avec le propriétaire.",
                 "Sinon, il appellera le propriétaire."),
                ("Il est nécessaire que les occupants libèrent l'accès.",
                 "Je dois tasser mes meubles."),
                ("Le cas échéant, un second passage sera planifié.",
                 "Si ça arrive, ils reviendront."),
                ("Nous vous prions de nous aviser dans les meilleurs délais.",
                 "Je dois répondre vite."),
                ("Le bruit des appareils est important et continu.",
                 "Ça va faire du bruit jour et nuit.")],
               corrige=True, cols=1,
               notes="Accepter toute reformulation exacte : il n'y a pas une seule bonne "
                     "réponse. Refuser seulement ce qui perd une information.")

    d.piege("Prendre « dans les meilleurs délais » pour un délai",
            "Ils vont s'en occuper bientôt.",
            "Je demande une date, par écrit.",
            "« Dans les meilleurs délais », « prochainement », « sous peu » ne veulent "
            "rien dire de précis, et n'engagent personne. Si le délai compte pour vous — "
            "et après un dégât, il compte —, demandez une date et gardez la réponse. "
            "Ce n'est pas de la méfiance : c'est ce que fait toute personne qui gère un "
            "chantier.",
            notes="Faire chercher au groupe d'autres formules floues rencontrées ailleurs. "
                  "Il y en a toujours : « selon la disponibilité », « à confirmer ».")

    d.regle("Un avis lu sans réponse est un avis accepté",
            "Si quelque chose ne convient pas, écrivez-le le jour même.",
            precision="Vous n'avez rien signé, et c'est justement le point : le silence "
                      "vaut acceptation dans presque toutes les démarches de logement. "
                      "Répondre ne veut pas dire refuser — ça peut être « je serai là », "
                      "« laissez-moi une clé chez la voisine », ou « je note que je "
                      "n'aurai pas de chambre pendant trois jours ». Cette dernière "
                      "phrase-là vaut de l'or trois semaines plus tard.",
            notes="Diapositive à photographier. Elle prépare directement le défi 3.")

    d.billet(
        "Traduisez une formule dans vos mots, à la première personne.",
        exemples=[
            "« Il est nécessaire que les occupants libèrent l'accès. »",
            "devient « Je dois tasser mon lit et ma commode avant mercredi. »",
        ],
        notes="Deux minutes. Vérifier une chose : la traduction contient-elle la date ?")

    return d.save(dossier)
