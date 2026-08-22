# -*- coding: utf-8 -*-
"""A2 · « Un incendie, une inondation »
Bloc A « Je découvre » · couleur indigo · 75 min. Graphie-phonie.
Source : exercice `prPhon`, mini-leçon `prPhon`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="« Un incendie, une inondation »",
        chapeau="Deux voyelles du nez portent la moitié des mots du fait "
                "divers. Celle de « in » — incendie, témoin, voisin, matin. "
                "Celle de « on » — inondation, cabanon, prévention, "
                "déclaration. Les confondre, c'est faire répéter la "
                "personne en face.",
        duree='75 minutes')

    d.titre(notes="Séance de phonétique, et elle n'est pas décorative : les deux sons "
                  "travaillés ici sont ceux des mots du module. Commencer en disant "
                  "« un incendie » puis « une inondation » deux fois, sans rien "
                  "expliquer, et demander ce qui change dans la bouche.")

    d.objectifs([
        "entendre la différence entre la voyelle de « in » et celle de « on » ;",
        "placer les lèvres correctement pour chacune des deux ;",
        "reconnaître les graphies qui donnent chaque son ;",
        "dire sans hésiter les mots qui contiennent les deux.",
    ], notes="Le troisième objectif est celui qui sert à l'écrit : « in », « ain », "
             "« ein », « im » donnent tous le même son, et l'élève qui l'ignore "
             "écrit « incendie » avec un o.")

    d.regle("Le son de « in » : les lèvres étirées",
            "Les lèvres s'écartent sur les côtés, presque comme pour "
            "sourire, et l'air passe par le nez.",
            precision="fin · main · plein · voisin · matin · témoin · incendie. "
                      "On l'écrit in, ain, ein, im : la graphie change, le son ne "
                      "change pas. Mettez la main devant la bouche : vous sentez "
                      "une fente large et plate.",
            notes="Faire dire les sept mots par toute la classe, la main devant la "
                  "bouche. Le geste installe le son mieux que l'explication, et il "
                  "reste disponible quand l'élève doute, seul, dans la rue.")

    d.regle("Le son de « on » : les lèvres en rond",
            "Les lèvres se ferment en petit rond, la langue recule, et "
            "l'air passe encore par le nez.",
            precision="bon · son · long · pont · cabanon · inondation · "
                      "prévention. On l'écrit on ou om. La main devant la bouche "
                      "sent un petit rond serré, pas une fente.",
            notes="Diapositive à photographier avec la précédente. Les deux règles se "
                  "lisent ensemble : c'est le contraste qui s'apprend, pas chaque son "
                  "isolé.")

    d.tableau('À l\'oreille', "La même graphie, deux sons différents",
              ['On lit', 'On entend'],
              [["incendie", "« in » étiré, puis « an »"],
               ["inondation", "« i-non » : le n se dit, puis « on » rond"],
               ["témoin", "« in » à la fin, lèvres étirées"],
               ["cabanon", "« on » à la fin, lèvres en rond"],
               ["important", "« in » étiré, puis « an »"],
               ["prévention", "« an », puis « on » rond"]],
              cle=1,
              notes="La comparaison « incendie » / « inondation » est le point le plus "
                    "difficile de la séance. La faire dire lentement, syllabe par "
                    "syllabe, avant de l'accélérer.")

    d.cartes("Quatre graphies pour un seul son", "Le son de « in » à l'écrit", [
        ("in",
         "incendie · voisin · matin · quinze. La graphie la plus fréquente."),
        ("ain / aim",
         "main · demain · plainte · faim. Le a ne s'entend pas du tout."),
        ("ein / eim",
         "plein · peintre · frein. Rare, mais elle revient dans « peinture »."),
        ("en après i",
         "bien · rien · combien · chien. Le son de « in » se cache derrière un e."),
    ], notes="La quatrième carte est la surprise de la séance : « bien » et « vin » "
             "riment. Le faire entendre plutôt que l'expliquer.")

    d.pratique('Écoute', "« in » ou « on » ?",
               "Écoutez le mot et dites quelle voyelle du nez vous entendez.", [
        ("un incendie", "le son de « in »"),
        ("une inondation", "le son de « on »"),
        ("un témoin", "le son de « in »"),
        ("un cabanon", "le son de « on »"),
        ("le matin", "le son de « in »"),
        ("la prévention", "le son de « on »"),
        ("un voisin", "le son de « in »"),
        ("une déclaration", "le son de « on »"),
        ("la fin de la rue", "le son de « in »"),
        ("un soupçon", "le son de « on »"),
    ], corrige=True,
       notes="Exercice prPhon de l'activité, en cartes écoutables. Chaque mot peut être "
             "réécouté autant de fois qu'il le faut : c'est un exercice qui se refait "
             "seul, à la maison, et il faut le dire au groupe.")

    d.piege("Confondre les deux voyelles du nez",
            "un bon voisin dit avec un seul son pour les deux",
            "un bon (rond) voisin (étiré)",
            "« Un bain » et « un bon » ne veulent pas dire la même chose. Quand le "
            "doute vient, regardez les lèvres de la personne qui parle : la moitié "
            "de l'écoute passe par les yeux, et personne ne le dit jamais.",
            notes="Faire pratiquer en binôme, dos à dos puis face à face. La différence "
                  "de réussite entre les deux positions frappe le groupe et justifie "
                  "tout le conseil.")

    d.piege("Faire sonner la voyelle du nez devant une autre voyelle",
            "une i-non-dation dite « un-ondation »",
            "i-non-da-tion",
            "Quand le n est suivi d'une voyelle, il se prononce et la voyelle du nez "
            "disparaît : inondation, inutile, initial. C'est la règle qui explique "
            "pourquoi « incendie » et « inondation » ne commencent pas pareil.",
            notes="Trois exemples suffisent. Ne pas transformer la séance en cours de "
                  "phonétique théorique : l'objectif est que les seize mots du module "
                  "se disent bien, pas que la règle soit récitée.")

    d.billet(
        "Écrivez une phrase qui contient les deux sons, et dites-la à voix haute.",
        exemples=[
            "Par exemple : Un incendie important dans le cabanon du voisin.",
            "Soulignez les mots où vous entendez la voyelle du nez.",
        ],
        notes="Écouter trois ou quatre phrases avant la sortie. Corriger la mélodie et "
              "les lèvres, jamais le contenu de la phrase.")

    return d.save(dossier)
