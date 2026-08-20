# -*- coding: utf-8 -*-
"""C4 · Attention, c'est dangereux.
Bloc C « Défi 2 » · couleur acier · 60 min. Bilan du défi 2.
Source : dialogue `t2b`, mini-leçon et exercice `t2danger`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-epicerie/images/')


def build(dossier):
    d = Deck(
        code='C4', section='acier',
        titre="Attention, c'est dangereux",
        chapeau="Quatre dessins dans un losange, les mêmes partout au Canada. "
                "Ils disent : ça tue, ça brûle, ça prend feu, ça éclate. Et "
                "une règle qui ne tient à aucun dessin.",
        duree='60 minutes')

    d.titre(notes="Séance de sécurité autant que de langue. Apporter si possible deux "
                  "bouteilles de produits d'entretien avec des pictogrammes différents.")

    d.objectifs([
        "reconnaître les quatre pictogrammes de mise en garde ;",
        "dire ce qu'ils veulent dire, en une phrase ;",
        "savoir quoi faire et où ranger ;",
        "connaître la règle du non-mélange.",
    ])

    d.declencheur(
        'Observation', "Que veut dire ce dessin ?",
        image=IMG + 'pictogramme-poison.jpg',
        pistes=[
            "L'avez-vous déjà remarqué ?",
            "Sur quels produits se trouve-t-il ?",
            "Que faut-il faire quand on le voit ?",
            "Où rangez-vous ces produits chez vous ?",
        ],
        notes="La dernière question est la plus importante : beaucoup de gens rangent ces "
              "produits sous l'évier, à hauteur d'enfant.")

    d.dialogue('Dialogue · 1 de 2', "Regardez les dessins", [
        ("MARISOL", "Madame Ginette, je cherche un produit pour le plancher.", True),
        ("GINETTE", "C'est dans l'allée des produits d'entretien. Mais faites attention.", True),
        ("MARISOL", "Attention à quoi ?", False),
        ("GINETTE", "Regardez les petits dessins sur la bouteille. Celui-là veut dire « poison ».", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="« Attention à quoi ? » : Marisol demande une précision au lieu d'acquiescer. "
             "C'est le réflexe travaillé dans tout le module.")

    d.dialogue('Dialogue · 2 de 2', "Ce qu'il ne faut jamais faire", [
        ("MARISOL", "Alors je mets des gants ?", True),
        ("GINETTE", "Des gants, et vous ouvrez la fenêtre. Et surtout : vous ne mélangez jamais deux produits.", True),
        ("MARISOL", "Pourquoi ?", False),
        ("GINETTE", "Parce que ça peut faire un gaz dangereux. C'est écrit sur la bouteille, mais personne ne le lit.", True),
    ], notes="La dernière réplique est exacte : l'avertissement est imprimé sur presque "
             "toutes les bouteilles d'eau de Javel.")

    d.tableau('Analyse', "Les quatre dessins",
              ['Le dessin', "Ce qu'il veut dire"],
              [["une tête de mort", "poison — tue si on l'avale"],
               ["une main percée", "corrosif — brûle la peau et les yeux"],
               ["une flamme", "inflammable — prend feu"],
               ["une bombe qui éclate", "explosif — le contenant peut éclater"]],
              cle=0,
              note="Les mêmes dans tout le Canada, quelle que soit la marque.",
              notes="Diapo à photographier. Les faire chercher sur les bouteilles apportées "
                    "en classe.")

    d.regle("Ne jamais mélanger deux produits",
            "C'est la règle qui ne tient à aucun dessin.",
            precision="L'eau de Javel et un nettoyant à l'ammoniac produisent ensemble un "
                      "<b>gaz toxique</b> qui envoie des gens à l'hôpital chaque année. "
                      "Mélanger ne rend pas un produit « plus fort » : cela le rend "
                      "dangereux. L'avertissement est écrit sur la bouteille — et presque "
                      "personne ne le lit.",
            notes="Diapo à photographier. C'est l'information la plus importante de la "
                  "séance, et peut-être du module.")

    d.cartes("Trois gestes de sécurité", "À la maison", [
        ("Ranger en haut",
         "Hors de portée des enfants, dans une armoire fermée si possible. Jamais sous "
         "l'évier, qui est à hauteur d'enfant."),
        ("Garder le contenant d'origine",
         "Ne jamais transvider dans une bouteille d'eau ou de jus. C'est la cause "
         "d'empoisonnements chaque année."),
        ("Aérer",
         "Ouvrir une fenêtre quand on lave avec un produit fort, même sans mise en garde. "
         "Et des gants pour tout ce qui porte une main percée."),
    ], notes="Diapo à photographier. Ces trois gestes valent d'être répétés à voix haute "
             "par le groupe.")

    d.piege("Croire que « naturel » veut dire « sans danger »",
            "C'est du vinaigre, il n'y a pas de risque.",
            "Regarder le dessin, pas le mot.",
            "Un produit naturel peut être corrosif : le vinaigre concentré brûle les yeux, "
            "et mélangé à de l'eau de Javel il dégage du chlore. Le pictogramme dit la "
            "vérité ; le mot sur l'étiquette est du marketing.",
            notes="Nuance utile : ne pas opposer naturel et chimique, mais renvoyer au "
                  "pictogramme.")

    d.pratique('Pratique', "Que veut dire ce dessin ?",
               "Une phrase pour chacun.", [
        ("une tête de mort", "poison — ne pas avaler"),
        ("une main percée", "ça brûle la peau — mettre des gants"),
        ("une flamme", "ça prend feu — loin de la cuisinière"),
        ("une bombe qui éclate", "ça peut éclater — jamais dans l'auto l'été"),
        ("aucun dessin", "moins dangereux, mais on aère quand même"),
    ], corrige=True, cols=1,
       notes="Utiliser l'exercice 4 du module. Enchaîner avec le Vrai ou Faux de "
             "l'exercice 5.")

    d.billet(
        "Regardez trois produits d'entretien chez vous.",
        exemples=[
            "Quels dessins portent-ils ?",
            "Où sont-ils rangés ? Faut-il les déplacer ?",
        ],
        notes="Fin du bloc C. Devoir concret, et qui peut réellement éviter un accident.")

    return d.save(dossier)
