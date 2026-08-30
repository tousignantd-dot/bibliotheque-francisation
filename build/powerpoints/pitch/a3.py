# -*- coding: utf-8 -*-
"""A3 · Les fiches de l'élève — ce qu'on lui met dans les mains, sur papier.

Section ambre · l'annexe qui répond à « et l'élève, il repart avec quoi ? ».
La réponse tient en un fait : une fiche par séance, imprimable, en noir et
blanc, et le manuel qui les relie toutes.

Les chiffres viennent de `chiffres.py`, comptés sur le dépôt — jamais écrits en
dur : un chiffre périmé annoncé devant une direction coûte plus cher que pas de
chiffre du tout.

Source : `assets/presentations/fiches-eleve.html`.
"""
from theme import Deck
from chiffres import CH, n
from vues import ecran, poser


def build(dossier):
    d = Deck(
        code='A3', section='ambre',
        titre="Les fiches de l'élève",
        chapeau="Une fiche par séance, format lettre, en noir et blanc — %s fiches. "
                "Elles s'impriment sur la photocopieuse de l'école, elles se rangent "
                "dans un cartable, et elles ne demandent aucun appareil."
                % n(CH['fiches']),
        duree='5 minutes')

    d.titre(surtitre="ANNEXE  ·  LE PAPIER",
            notes="Annexe. Elle sert surtout devant une direction qui doute que le "
                  "numérique convienne à son public : la réponse est qu'on n'a jamais "
                  "retiré le papier.")

    d.regle("La règle qui tient tout",
            "Une séance, c'est une fiche pour l'élève et un diaporama pour vous.",
            precision="Les deux sortent du même fichier de contenu. Corriger une règle "
                      "la corrige des deux côtés : il n'existe pas de version à jour et "
                      "de version oubliée.",
            notes="C'est la même diapositive que dans P1. La répéter est voulu : c'est "
                  "la seule idée que la salle doit emporter des deux.")

    ecran(d, "Une séance", "La fiche que l'élève reçoit",
          poser('mat', '01-fiche-seance'),
          "Nom, date, l'objectif de la séance, les exercices. Noir et blanc : la "
          "hiérarchie passe par la graisse et les filets, jamais par la couleur.",
          notes="Le noir et blanc n'est pas une économie de style : c'est la seule "
                "façon qu'une fiche sorte juste d'une photocopieuse d'école.")

    ecran(d, "Une séance", "Le dialogue, écrit",
          poser('mat', '02-fiche-dialogue'),
          "Ce que l'élève a entendu dans le module, il le retrouve écrit. Il peut "
          "le relire chez lui sans rouvrir un écran.",
          notes="Point à faire : l'audio est dans le module, le texte est sur la "
                "fiche. Un élève sans données mobiles travaille quand même.")

    ecran(d, "Un module", "Le sommaire de ses séances",
          poser('mat', '03-sommaire-module'),
          "Les seize séances d'un module en une page. C'est ce que l'enseignant "
          "imprime en premier, pour savoir où il va.",
          notes="Seize séances par module aux niveaux 3 à 8 ; huit aux niveaux 1 et 2. "
                "Le dire seulement si on le demande.")

    ecran(d, "Toutes ensemble", "Le manuel de l'élève",
          poser('mat', '06-manuel-couverture'),
          "Les %s séances d'un niveau reliées en un manuel, avec sa table des "
          "matières. Il se fabrique en une commande." % n(CH['par_niveau'].get(
              'Niveau 4', 0)),
          notes="C'est le document qui impressionne le plus en salle, et c'est le "
                "moins cher à produire : il est assemblé à partir des fiches qui "
                "existent déjà.")

    d.cartes("Ce que le papier permet", "Quatre situations, toutes réelles",
             [("Un élève sans appareil", "Il fait la séance sur sa fiche, et rattrape "
               "l'écoute en classe. Rien ne l'exclut du cours."),
              ("Une panne de réseau", "La séance se donne quand même : "
               "l'enseignant a son diaporama, l'élève a sa fiche."),
              ("Un cartable qui reste", "À la fin du niveau, l'élève repart avec un "
               "manuel. C'est ce qu'il montre chez lui."),
              ("Une correction à la main", "L'enseignant qui préfère corriger sur "
               "papier le peut. Le module n'oblige personne.")],
             notes="Ces quatre-là viennent de vraies objections. Ne pas les inventer "
                   "en salle : les lire.")

    d.billet("Le papier n'est pas la version dégradée du cours. C'est la moitié qui "
             "reste quand tout le reste tombe.",
             exemples=["%s fiches, une par séance." % n(CH['fiches']),
                       "Le document « Les fiches de l'élève » tient sur neuf pages."],
             notes="Fermer là-dessus. C'est la phrase qui désamorce l'objection du "
                   "tout-numérique.")

    return d.save(dossier)
