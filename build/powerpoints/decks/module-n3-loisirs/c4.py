# -*- coding: utf-8 -*-
"""C4 · L'adjectif qui décrit le film.
Bloc C « Défi 2 · Le ciné-club du vendredi » · ambre · 60 min.
Source du module : exercice `t2adj`, mini-leçon `t2adj`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="L'adjectif qui décrit le film",
        chapeau="Dans une description de film, presque tout tient en deux ou "
                "trois adjectifs : court, drôle, triste, vrai. Ce sont eux "
                "qui aident à choisir — et ils changent de forme selon le mot "
                "qu'ils décrivent.",
        duree='60 minutes')

    d.titre(notes="Dernière séance du défi 2. Point de langue court : garder vingt "
                  "minutes pour l'écriture, où l'accord se joue vraiment.")

    d.objectifs([
        "accorder un adjectif au féminin et au pluriel ;",
        "reconnaître les adjectifs qui ne changent pas au féminin ;",
        "placer l'adjectif après le nom, comme le fait le français ;",
        "employer les adjectifs du feuillet pour décrire un film.",
    ])

    d.regle("La règle en une phrase",
            "L'adjectif s'accorde avec le nom qu'il décrit.",
            precision="Au féminin, on ajoute un e. Au pluriel, un s. Aux deux, "
                      "e puis s, dans cet ordre. Et si l'adjectif finit déjà par un e, "
                      "on ne touche à rien au féminin.",
            notes="Diapo à photographier. Toute la séance tient dans ces quatre lignes ; "
                  "le reste n'est que de l'entraînement.")

    d.tableau('Analyse', "Quatre cas, quatre formes",
              ["Le cas", "Exemple", "Ce qu'on ajoute"],
              [["masculin singulier", "un film court", "rien"],
               ["féminin singulier", "une séance courte", "un e"],
               ["masculin pluriel", "des films courts", "un s"],
               ["féminin pluriel", "des séances courtes", "un e, puis un s"]],
              cle=1,
              note="Le s ne s'entend jamais. Le e s'entend parfois : il fait sonner la consonne d'avant.",
              notes="Diapo à photographier. Faire dire « court » et « courte » à voix "
                    "haute : le t se met à sonner. C'est l'indice le plus utile à "
                    "l'oreille, et il marche pour gratuit, petit, grand, vrai.")

    d.cartes("Deux familles à part", "Elles se comportent autrement", [
        ("drôle · triste · libre · propre",
         "Ils finissent déjà par un e : on n'ajoute rien au féminin. « Un film drôle », "
         "« une histoire drôle ». Au pluriel, le s revient quand même : des films "
         "drôles."),
        ("gratuit · gros · beau",
         "Ils changent plus que d'un e : gratuite, grosse, belle. Il n'y en a pas "
         "beaucoup, et ce sont les plus employés — donc on les apprend un par un, "
         "comme des mots."),
    ], cols=1,
       notes="La deuxième carte est celle qu'on relit. « Belle » surprend toujours : "
             "signaler aussi « un bel automne », devant une voyelle.")

    d.piege('Le piège', "un court film, une drôlee histoire",
            "un film court, une histoire drôle",
            "Deux fautes différentes. La place, d'abord : en français, l'adjectif se met "
            "presque toujours APRÈS le nom, contrairement à l'anglais. Et le e ensuite : "
            "un adjectif qui en a déjà un n'en prend pas un second au féminin.",
            notes="La question de la place revient à chaque niveau. La règle pratique : "
                  "après le nom, sauf une petite série de mots courts et très courants "
                  "— grand, gros, petit, beau, jeune, vieux.")

    d.pratique('Écriture · 1 de 2', "Accordez l'adjectif",
               "Complétez avec la bonne forme de l'adjectif entre parenthèses.", [
        ("Le documentaire est un film ___ . (court)", "court"),
        ("La séance du samedi est ___ pour les enfants. (gratuit)", "gratuite"),
        ("C'est une histoire ___ , tirée de la vie de vrais pêcheurs. (vrai)", "vraie"),
        ("Les deux comédies de la session sont très ___ . (drôle)", "drôles"),
        ("Le drame du 3 octobre est une histoire ___ . (triste)", "triste"),
        ("Les places sont ___ dans la salle 2 : personne n'est venu. (libre)", "libres"),
    ], corrige=True,
       notes="C'est l'exercice t2adj du module. Faire dire, avant chaque réponse, si le "
             "nom est masculin ou féminin, singulier ou pluriel : c'est le raisonnement "
             "qu'on veut installer, pas la bonne case.")

    d.pratique('Écriture · 2 de 2', "Décrivez un film en une phrase",
               "Écrivez une phrase avec au moins deux adjectifs accordés.", [
        ("un documentaire de 1 h 10 sur les rivières",
         "C'est un documentaire court et vrai, sur les rivières du Québec."),
        ("une comédie de 1 h 34 sur deux voisins",
         "C'est une comédie drôle, avec deux voisins jamais d'accord."),
        ("un drame de 1 h 52 sur une famille",
         "C'est une longue histoire triste, sur une famille qui déménage."),
        ("un film d'animation pour les familles",
         "C'est un film d'animation court, gratuit pour les enfants."),
    ], corrige=True,
       notes="Accepter toute phrase juste : le corrigé donne un exemple, pas la réponse. "
             "Relever au tableau deux ou trois phrases d'élèves, mieux tournées que "
             "celles-là.")

    d.billet(
        "Écrivez trois phrases sur un film que vous avez aimé.",
        exemples=[
            "Employez au moins deux adjectifs, accordés.",
            "Dites le genre et la durée, comme dans le feuillet.",
        ],
        notes="Devoir court. C'est la dernière écriture avant le défi 3 : ramasser et "
              "relever ce qui reviendra dans la production écrite du bloc E.")

    return d.save(dossier)
