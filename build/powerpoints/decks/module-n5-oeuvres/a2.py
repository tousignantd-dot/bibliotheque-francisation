# -*- coding: utf-8 -*-
"""A2 · Le son de « j » et le son de « ch »
Bloc A « Je découvre » · couleur indigo · graphie-phonie · 75 min.
Source : exercice `prPhon`, mini-leçon `prPhon`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Le son de « j » et le son de « ch »",
        chapeau="Un personnage, un passage, une image d'un côté ; un "
                "chapitre, une planche, une chanson de l'autre. Deux sons "
                "faits au même endroit dans la bouche, que rien ne "
                "distingue sur le visage de la personne qui parle — et un "
                "seul geste pour passer de l'un à l'autre.",
        duree='75 minutes')

    d.titre(notes="Séance de graphie-phonie. Commencer la main sur la gorge, tout le "
                  "groupe en même temps : dire « jjjj », puis « chhhh ». La différence se "
                  "sent avant de s'entendre. C'est l'exercice le plus rentable de la "
                  "séance et il prend dix secondes.")

    d.objectifs([
        "sentir la différence entre le son de « j » et le son de « ch » ;",
        "reconnaître les quatre orthographes qui donnent le son de « j » ;",
        "prononcer les mots du module qui contiennent l'un ou l'autre ;",
        "ne pas éteindre la voix en fin de mot : image, page, passage, village.",
    ], notes="Le quatrième objectif est le plus difficile et le plus utile. En fin de mot, "
             "la voix a tendance à s'éteindre avant le son : « personnache » au lieu de "
             "« personnage ». Y revenir à chaque séance du module.")

    d.declencheur(
        'Écoute', "Les gens, les champs. J'ai, chez. Qu'est-ce qui change "
                  "entre les deux mots ?",
        pistes=[
            "Est-ce que les lèvres bougent différemment ? Regardez-vous l'un l'autre.",
            "Est-ce que la langue change de place ?",
            "Posez deux doigts sur votre gorge et redites les deux mots.",
            "Lequel des deux sons fait bourdonner la gorge ?",
        ],
        notes="Laisser le groupe chercher avant de donner la réponse. Les trois premières "
              "pistes mènent toutes à « rien ne change » — c'est voulu. Seule la quatrième "
              "donne la vraie différence, et elle ne se voit pas.")

    d.regle("Même bouche, même langue — seule la voix change",
            "« j » sans voix devient « ch » ; « ch » avec la voix devient « j ».",
            precision="Les lèvres avancent un peu, la langue monte vers l'avant du "
                      "palais, l'air passe par une fente étroite : identique pour les "
                      "deux. La gorge vibre pour « j », elle ne vibre pas pour « ch ». "
                      "C'est tout, et c'est la seule chose à retenir.",
            notes="Diapositive à photographier. Faire l'aller-retour dix fois, la main sur "
                  "la gorge, sans changer la position des lèvres : jjj-chhh-jjj-chhh. "
                  "C'est le seul exercice utile de la séance.")

    d.tableau('Comment ça s\'écrit', "Quatre façons pour un son, une seule pour l'autre",
              ['Le son de « j »', 'Le son de « ch »'],
              [["j — j'ai, déjà, toujours, jamais", "ch — un chapitre, chaque, chez"],
               ["g devant e — une page, une image", "ch — une planche, une chanson"],
               ["g devant i — la gigue, agir", "ch — chercher, toucher, marcher"],
               ["ge devant a, o — nous mangeons", "ch — une chaise, un chien"],
               ["Et jamais : l'intrigue, une guide", "Sauf : un chœur, une chorale (« k »)"]],
              cle=0,
              notes="La dernière rangée porte les deux exceptions à signaler. À gauche, le "
                    "g reste dur devant u : « intrigue » ne se dit pas « intrijue ». À "
                    "droite, quelques mots venus du grec disent « k » : un chœur, une "
                    "chorale, la technologie. Rares, mais « chœur » revient dès qu'on "
                    "parle de musique.")

    d.cartes("Les paires à sentir", "Deux mots, une seule différence", [
        ("les gens / les champs",
         "La gorge vibre, puis elle ne vibre plus. Rien d'autre ne change."),
        ("j'ai / chez",
         "Deux mots très courts : c'est là que la différence s'entend le mieux."),
        ("bouger / boucher",
         "La même consonne au milieu, deux fois. À dire lentement."),
        ("la cage / la cache",
         "En fin de mot : c'est le cas le plus difficile du français."),
    ], notes="Faire dire les quatre paires par tout le groupe, puis par des élèves seuls. "
             "Ceux dont la langue première n'a pas le son de « j » — plusieurs langues "
             "n'ont que « ch » — ont besoin de la main sur la gorge plus longtemps que "
             "les autres. Ne pas presser.")

    d.pratique('Écoute', "Vous entendez « j » ou « ch » ?",
               "Écoutez le mot et dites lequel des deux sons vous entendez.", [
        ("un personnage", "« j » — g devant e"),
        ("un chapitre", "« ch »"),
        ("une image", "« j » — g devant e"),
        ("une planche", "« ch »"),
        ("un passage", "« j » — g devant e"),
        ("une chanson", "« ch »"),
        ("déjà lu", "« j » — écrit avec j"),
        ("toucher", "« ch »"),
        ("l'intrigue est jolie", "« j » — mais le g de « intrigue » reste dur"),
        ("chercher un album", "« ch » deux fois"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice `prPhon` du module interactif, à cartes écoutables. Le "
             "faire d'abord ici, à la voix de l'enseignante, puis le laisser refaire à "
             "l'écran avec les enregistrements. La neuvième ligne est un piège utile : le "
             "mot contient le son de « j », mais pas là où on le croit.")

    d.piege("Éteindre la voix en fin de mot",
            "un personnache · une imache · un passache",
            "un personnage · une image · un passage",
            "En fin de mot, la voix s'arrête souvent avant le son, et « j » devient "
            "« ch ». Il faut tenir la voix jusqu'au bout : la dernière syllabe de "
            "« personnage » bourdonne encore quand elle s'arrête.",
            notes="Exercice de correction : faire dire « image, page, passage, village, "
                  "personnage » en tenant la main sur la gorge pendant toute la dernière "
                  "syllabe. Si la vibration s'arrête avant le mot, le mot est faux.")

    d.pratique('Phrases à répéter', "Les deux sons dans la même phrase",
               "Dites chaque phrase lentement, puis vite.", [
        ("J'ai lu ce roman en deux soirées.",),
        ("Chaque chapitre commence par une chanson.",),
        ("Ce personnage-là m'a touchée.",),
        ("La planche du milieu ne contient aucune image.",),
        ("Je cherche l'album que j'ai déjà lu.",),
        ("Quelle belle façon de le dire !",),
    ], notes="Les six phrases viennent du module. La dernière est un piège : le « ç » de "
             "« façon » n'est pas un « ch », c'est le son de « s ». Personne ne le "
             "remarque avant de l'avoir dit à voix haute une fois.")

    d.billet(
        "Écrivez trois mots de votre œuvre qui contiennent le son de « j » ou celui de « ch ».",
        exemples=[
            "Dites lequel des deux, et comment il s'écrit : j, g, ge ou ch.",
            "Choisissez-en un et dites-le à voix haute avant de sortir.",
        ],
        notes="Ramasser les billets : ils donnent la liste des mots à reprendre en A3 avec "
              "le vocabulaire. Un élève qui n'en trouve aucun peut prendre les mots du "
              "module — un personnage, un chapitre, une planche.")

    return d.save(dossier)
