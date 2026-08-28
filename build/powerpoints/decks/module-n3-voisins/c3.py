# -*- coding: utf-8 -*-
"""C3 · Ce qui va arriver, et ce qui aura lieu.
Bloc C « Défi 2 · Venez prendre un café » · couleur ambre (écriture) · 60 min.
Source : exercice `t2futur`, mini-leçon `t2futur`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Ce qui va arriver, et ce qui aura lieu",
        chapeau="Deux futurs, et ils ne servent pas au même endroit. L'un "
                "se dit sur le palier, l'autre s'écrit sur le carton qu'on "
                "glisse sous les portes.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture, la plus grammaticale du module. Elle se justifie "
                  "par le carton de E1 : sans le futur simple, l'élève écrit son "
                  "invitation comme il la dirait, et le carton sonne faux.")

    d.objectifs([
        "employer le futur proche à l'oral : « je vais apporter » ;",
        "employer le futur simple à l'écrit : « la fête aura lieu » ;",
        "connaître par cœur « il y aura », « ce sera », « nous serons » ;",
        "écrire « confirmez SVP » au bon endroit.",
    ])

    d.regle("Le futur de tous les jours",
            "Je vais apporter mes biscuits.",
            precision="Le verbe « aller », puis le verbe qui ne change pas. "
                      "C'est le futur qu'on entend partout, à l'oral, pour "
                      "ce qui est décidé et proche.",
            notes="Diapo à photographier. Faire produire cinq phrases avec le groupe, à "
                  "partir de ce que chacun fera ce soir. Le futur proche s'installe vite "
                  "parce qu'il n'a qu'une forme à retenir.")

    d.tableau('Analyse', "Deux futurs, deux endroits",
              ["On dit, sur le palier", "On écrit, sur le carton"],
              [["Je vais apporter des gâteaux.", "Il y aura du café et des gâteaux."],
               ["On va se voir samedi.", "La rencontre aura lieu samedi."],
               ["Ça va être chez nous.", "Ce sera chez nous, au 3A."],
               ["On va être une dizaine.", "Nous serons une dizaine."]],
              cle=1,
              note="Même sens des deux côtés. Ce qui change, c'est le canal : "
                   "l'oral prend le futur proche, l'écrit prend le simple.",
              notes="Diapo à photographier. Faire lire les deux colonnes à voix haute, "
                    "l'une après l'autre. La colonne de droite sonne « écrit » même "
                    "prononcée — c'est ce qu'il faut entendre.")

    d.cartes("Trois formes à savoir par cœur", "Elles reviennent dans tous les cartons", [
        ("Il y aura",
         "« Il y aura du café, du thé et des gâteaux. » C'est la forme qui annonce ce "
         "qu'on trouvera sur place."),
        ("Ce sera",
         "« Ce sera chez nous, au 3A. » Elle donne l'endroit sans répéter le verbe "
         "« avoir lieu »."),
        ("Nous serons",
         "« Nous serons une dizaine. » Elle rassure : l'invité sait dans quoi il entre."),
        ("Aura lieu",
         "« La rencontre aura lieu le samedi 14, à 14 h. » C'est la formule des affiches "
         "et des cartons. On ne la dit jamais à voix haute."),
    ], notes="Ces quatre formes suffisent pour écrire n'importe quel carton d'invitation. "
             "Les faire copier telles quelles dans le cahier.")

    d.pratique('Écriture', "Futur proche ou futur simple ?",
               "Écrivez le verbe entre parenthèses à la forme qui convient.", [
        ("Je ___ (apporter) mes biscuits, j'insiste.", "vais apporter — on le dit"),
        ("Ma sœur ___ (faire) des gâteaux pour samedi.", "va faire — on le dit"),
        ("Sur le carton, j'écris : la fête ___ (avoir) lieu samedi.", "aura — on l'écrit"),
        ("Ce ___ (être) chez nous, au 3A.", "sera — on l'écrit"),
        ("Il y ___ (avoir) du café et des gâteaux.", "aura — on l'écrit"),
        ("On ___ (se voir) samedi, alors !", "va se voir — on le dit"),
    ], corrige=True,
       notes="C'est l'exercice `t2futur` du module interactif, mot pour mot. La question à "
             "poser avant chaque réponse n'est pas « quel temps ? » mais « est-ce que je "
             "le dis ou est-ce que je l'écris ? ». C'est ça qui décide.")

    d.piege("Écrire le carton comme on parle",
            "Samedi on va faire un café pis ça va être chez nous.",
            "La rencontre aura lieu samedi 14, à 14 h, chez nous, au 3A.",
            "Le carton se lit sans la voix, par des gens qu'on ne connaît "
            "pas encore. Ce qui passe très bien sur le palier — « on va "
            "faire », « pis » — donne à l'écrit un mot glissé à la va-vite.",
            notes="Ne pas dévaloriser l'oral au passage : la colonne de gauche est du bon "
                  "français d'ici, et c'est celle qu'il faut employer en parlant. Deux "
                  "canaux, deux registres.")

    d.regle("Confirmez SVP",
            "Confirmez SVP en glissant un mot sous notre porte.",
            precision="C'est la phrase qui demande une réponse. On l'écrit "
                      "à la fin du carton ; on ne la dit jamais de vive "
                      "voix — en personne, on demande simplement « vous "
                      "pensez pouvoir venir ? ».",
            notes="Diapo à photographier. Faire remarquer qu'on dit aussi comment "
                  "répondre : sans ça, l'invité ne sait pas quoi faire de la demande.")

    d.billet(
        "Écrivez trois phrases de votre carton, au futur simple.",
        exemples=[
            "Une pour l'endroit, une pour ce qu'il y aura, une pour la réponse.",
            "« La rencontre aura lieu… Il y aura… Confirmez SVP… »",
        ],
        notes="Devoir court. Ces trois phrases entrent telles quelles dans le carton de "
              "E1. Ramasser et corriger seulement les formes du futur simple.")

    return d.save(dossier)
