# -*- coding: utf-8 -*-
"""A3 · Le corps, les sens et la douleur.
Bloc A · couleur foret (vocabulaire) · 50 min.
Source : exercice `prSens`, cartes mémoire du corps, vocabulaire de la douleur.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='foret',
        titre='Le corps, les sens et la douleur',
        chapeau="Pour se faire soigner, il faut d'abord pouvoir nommer. Les parties du "
                "corps, les cinq sens, et surtout les quatre mots qui disent comment "
                "une douleur se comporte.",
        duree='50 minutes')

    d.titre(notes="Séance de vocabulaire pur. Prévoir beaucoup d'oral : chaque mot doit "
                  "sortir de la bouche des élèves, pas seulement de la vôtre.")

    d.objectifs([
        "nommer les parties du corps utiles en consultation ;",
        "associer chacun des cinq sens à son organe ;",
        "choisir le bon verbe pour dire comment la douleur se comporte ;",
        "situer une douleur à droite, à gauche, en haut, en bas.",
    ])

    d.vocabulaire('Vocabulaire · 1 de 3', "Les parties du corps qu'on montre au médecin", [
        ("le genou", "L'articulation au milieu de la jambe."),
        ("la cheville", "L'articulation entre la jambe et le pied."),
        ("le poignet", "L'articulation entre le bras et la main."),
        ("l'épaule", "Le haut du bras, là où il s'attache au corps."),
        ("le dos", "L'arrière du corps, de la nuque aux hanches."),
        ("la poitrine", "L'avant du haut du corps, où sont le cœur et les poumons."),
    ], notes="Faire montrer chaque partie sur soi pendant qu'on la nomme. Le geste fixe "
             "le mot bien mieux que la traduction.")

    d.vocabulaire('Vocabulaire · 2 de 3', "Ce qu'il y a sous la peau", [
        ("un muscle", "Ce qui se contracte pour faire bouger le corps."),
        ("un tendon", "La partie qui attache un muscle à un os."),
        ("un os", "La partie dure du squelette."),
        ("une articulation", "L'endroit où deux os se rejoignent et se plient."),
        ("un ligament", "Ce qui tient deux os ensemble à une articulation."),
    ], notes="Ces cinq mots reviennent dans tout le module : « inflammation du tendon » "
             "en C1, « les ligaments sont étirés » en E1. Ne pas les sauter.")

    d.tableau('Analyse', "Les cinq sens et leur organe",
              ['Le sens', "L'organe"],
              [["la vue", "les yeux"],
               ["l'ouïe", "les oreilles"],
               ["l'odorat", "le nez"],
               ["le goût", "la langue"],
               ["le toucher", "la peau"]],
              cle=0,
              note="Les noms des sens sont difficiles ; les organes sont connus. On part "
                   "donc de l'organe pour retrouver le sens, pas l'inverse.",
              notes="« L'ouïe » et « l'odorat » sont les deux mots que personne ne "
                    "connaît. Les faire répéter cinq fois chacun.")

    d.regle('Le mot clé de la séance',
            "Une douleur ne fait pas seulement « mal » : elle élance, elle brûle, elle tire ou elle pique.",
            precision="Le verbe que vous choisissez oriente le diagnostic. Une douleur "
                      "qui élance et une douleur qui brûle ne viennent pas du même "
                      "problème, et le médecin le sait avant même de vous examiner.",
            notes="Diapo centrale de la séance. La laisser affichée pendant tout "
                  "l'exercice qui suit.")

    d.cartes('Analyse', "Quatre façons dont une douleur se comporte", [
        ("Ça élance",
         "Une douleur vive qui revient par à-coups, comme des vagues. C'est celle de "
         "Yannick : « ça élance dès que je plie la jambe »."),
        ("Ça brûle",
         "Une douleur chaude et continue, comme une brûlure. Souvent la peau, un nerf, "
         "ou l'estomac."),
        ("Ça tire",
         "Une douleur d'étirement quand on bouge dans une direction. Souvent un muscle "
         "ou un tendon."),
        ("Ça pique",
         "Une douleur fine et courte, comme une aiguille. Souvent la peau ou une piqûre."),
    ], notes="Faire mimer chacune des quatre par un élève différent. Le groupe devine "
             "le verbe avant de le lire.")

    d.tableau('Analyse', "Situer la douleur en trois mots",
              ['On précise', 'Les mots', 'Exemple'],
              [["le côté", "droit, gauche", "le genou droit"],
               ["la hauteur", "en haut, en bas", "le bas du dos"],
               ["la face", "devant, derrière", "derrière la cuisse"]],
              cle=1,
              note="Sans le côté, le soignant doit examiner les deux. Dites-le toujours.",
              notes="Faire remarquer que Yannick dit « le genou droit » dès la première "
                    "phrase du triage. Ce n'est pas un détail, c'est une habitude à "
                    "prendre.")

    d.pratique('Pratique · 1 de 3', 'Le sens et son organe',
               "Reliez chaque sens à la partie du corps qui lui correspond.", [
        ("la vue", "les yeux"),
        ("l'ouïe", "les oreilles"),
        ("l'odorat", "le nez"),
        ("le goût", "la langue"),
        ("le toucher", "la peau"),
    ], corrige=True, cols=2,
       notes="Exercice rapide, deux minutes. S'il prend plus de temps, c'est le "
             "vocabulaire des sens qui n'est pas installé : y revenir.")

    d.pratique('Pratique · 2 de 3', 'Quel verbe pour quelle douleur ?',
               "Choisissez : élancer, brûler, tirer ou piquer.", [
        ("Une douleur vive qui revient par à-coups.", "ça élance"),
        ("Une sensation de chaleur continue sur la peau.", "ça brûle"),
        ("Une douleur quand on étire le muscle.", "ça tire"),
        ("Une douleur fine, comme une aiguille.", "ça pique"),
        ("Le genou de Yannick quand il plie la jambe.", "ça élance"),
    ], corrige=True,
       notes="La dernière relie l'exercice au dialogue de A1. Faire retrouver la phrase "
             "exacte du dialogue.")

    d.pratique('Pratique · 3 de 3', 'Décrivez la douleur en une phrase',
               "Utilisez : la partie du corps, le côté, le verbe de douleur.", [
        ("Le genou, à droite, une douleur par à-coups.",
         "J'ai le genou droit qui élance."),
        ("L'épaule, à gauche, une douleur quand on lève le bras.",
         "Ça tire dans l'épaule gauche quand je lève le bras."),
        ("Le bas du dos, une douleur continue et chaude.",
         "Ça brûle dans le bas du dos."),
        ("La cheville, à droite, enflée depuis hier.",
         "Ma cheville droite est enflée depuis hier."),
    ], corrige=True,
       notes="Accepter toute phrase qui contient les trois éléments. La formulation "
             "exacte importe moins que la présence du côté et du verbe.")

    d.piege('Le piège du corps',
            "J'ai mal au pied.",
            "J'ai mal à la cheville droite.",
            "« Le pied » couvre tout, de la cheville aux orteils. Plus la zone nommée "
            "est large, plus le soignant devra chercher. Le mot précis existe en "
            "français, et c'est celui de la séance : cheville, poignet, épaule, genou.",
            notes="Faire retrouver, pour chaque mot vague donné par le groupe, le mot "
                  "précis correspondant. « La jambe » → le genou, la cheville, la cuisse.")

    d.billet(
        "Nommez trois parties de votre corps et dites, pour chacune, comment une douleur "
        "s'y comporterait.",
        exemples=[
            "Utilisez un des quatre verbes : élancer, brûler, tirer, piquer.",
            "Exemple : « Le bas du dos — ça tire quand je me penche. »",
        ],
        notes="Les billets serviront en B1 : chacun décrira sa propre douleur à "
              "l'infirmière du triage.")

    return d.save(dossier)
