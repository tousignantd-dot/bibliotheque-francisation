# -*- coding: utf-8 -*-
"""A2 · Le « u » de jupe et le « ou » de rouge.
Bloc A « Je découvre » · couleur indigo (graphie-phonie) · 60 min.
Source : mini-leçon `prPhon`, exercice `prPhon` (cartes à écouter).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre='Le « u » de jupe et le « ou » de rouge',
        chapeau="Deux sons très proches à l'oreille, très différents dans la "
                "bouche. Beaucoup de langues n'ont que le second — et « tu » "
                "devient « tout » sans qu'on s'en aperçoive.",
        duree='60 minutes')

    d.titre(notes="Séance d'écoute. Prévoir le son. Commencer en disant « jupe » puis "
                  "« joupe » sans prévenir, et demander au groupe si les deux existent.")

    d.objectifs([
        "entendre la différence entre le son u et le son ou ;",
        "savoir que c'est la langue, et non les lèvres, qui décide ;",
        "produire le son u à partir du son i ;",
        "employer les deux sons dans les mots du magasin.",
    ])

    d.declencheur(
        'Écoute', "Ces deux mots sont-ils différents ?",
        pistes=[
            "« une jupe » et « une joue »",
            "« un pull » et « une poule »",
            "Qu'est-ce qui change ?",
            "Les lèvres, ou la langue ?",
        ],
        notes="Faire écouter les paires avant toute explication. Le groupe entend qu'il y a "
              "une différence bien avant de pouvoir la nommer.")

    d.tableau('Analyse', "Deux sons, deux positions de langue",
              ['On entend « u »', 'On entend « ou »'],
              [["une jupe", "rouge"],
               ["un pull", "un blouson"],
               ["le tissu", "un foulard"],
               ["uni", "un bouton"]],
              cle=0,
              note="À gauche, la langue est en avant. À droite, elle est au fond.",
              notes="Diapo centrale, à photographier. Faire lire la colonne de gauche, puis "
                    "celle de droite, puis en alternance.")

    d.regle("Le truc du « i »",
            "Dites « i » longuement, puis arrondissez les lèvres.",
            precision="Sans bouger la langue. Le son qui sort est le <b>u</b> de « jupe ». "
                      "C'est la seule méthode qui fonctionne à coup sûr, parce qu'elle "
                      "part d'un son que presque toutes les langues possèdent — le i — au "
                      "lieu de partir du ou, qui entraîne la langue au fond.",
            notes="Diapo à photographier. Faire faire l'exercice en même temps par tout le "
                  "groupe, un doigt sous le menton pour sentir la langue bouger.")

    d.cartes("Où ces deux sons apparaissent", "Trois endroits du module", [
        ("Les vêtements",
         "une j<b>u</b>pe, un p<b>u</b>ll, le tiss<b>u</b> — et un f<b>ou</b>lard, un "
         "bl<b>ou</b>son, un b<b>ou</b>ton."),
        ("Les motifs et les matières",
         "<b>u</b>ni se dit avec le u ; d<b>ou</b>x, d<b>ou</b>blé et l'<b>ou</b>verture "
         "du magasin se disent avec le ou."),
        ("Deux mots que tout change",
         "« t<b>u</b> » et « t<b>ou</b>t » ne veulent pas dire la même chose. Là, la "
         "confusion change vraiment la phrase."),
    ], notes="Le troisième cas justifie tout le travail : ce n'est pas un détail d'accent.")

    d.piege("Écouter les lèvres",
            "Les deux sons se ressemblent, donc c'est pareil.",
            "La différence est dans la langue.",
            "Les lèvres sont presque identiques pour les deux sons : rondes dans les deux "
            "cas. C'est la langue qui bouge — en avant pour le u, au fond pour le ou. Un "
            "doigt sous le menton permet de le sentir.",
            notes="Faire vérifier par le toucher. Beaucoup d'élèves ne croient à la "
                  "différence que lorsqu'ils la sentent.")

    d.pratique('Pratique · 1 de 2', "Quel son entendez-vous ?",
               "Écoutez chaque mot.", [
        ("une jupe", "u"),
        ("rouge", "ou"),
        ("un pull", "u"),
        ("un blouson", "ou"),
        ("le tissu", "u"),
        ("un foulard", "ou"),
        ("uni", "u"),
        ("un bouton", "ou"),
    ], corrige=True,
       notes="Utiliser l'exercice 2 du module, à cartes écoutables. Deux écoutes avant de "
             "corriger.")

    d.pratique('Pratique · 2 de 2', "Dans une phrase",
               "Écoutez, puis répétez.", [
        ("Je cherche une jupe unie.", "trois fois le son u"),
        ("Le foulard rouge est en rabais.", "deux fois le son ou"),
        ("Ce tissu est doux.", "u, puis ou"),
        ("Le blouson a un capuchon.", "trois fois le son ou"),
        ("Il manque un bouton au pull.", "ou, puis u"),
    ], corrige=True, cols=1,
       notes="Plus difficile : les deux sons se suivent dans la même phrase. Faire répéter "
             "lentement d'abord, à vitesse normale ensuite.")

    d.billet(
        "Trouvez cinq mots avec le son u et cinq mots avec le son ou.",
        exemples=[
            "Dans le vocabulaire du module, ou ailleurs.",
            "Lisez-les à voix haute avant de les écrire.",
        ],
        notes="Rendre à la séance suivante. Corriger surtout la lecture à voix haute.")

    return d.save(dossier)
