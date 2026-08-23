# -*- coding: utf-8 -*-
"""B4 · Restreindre et comparer
Bloc B « Défi 1 » · couleur ambre · écriture · 75 min.
Source : exercices `t1que` et `t1comp`, mini-leçons du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Restreindre et comparer",
        chapeau="« Je n'ai reçu que onze candidatures. » Cette phrase est "
                "positive, et beaucoup d'élèves la lisent à l'envers pendant "
                "des années. Après elle : comparer deux régions avec des "
                "chiffres.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 1, et la plus dense : deux points de "
                  "grammaire. Prévoir quarante minutes pour « ne… que », le reste "
                  "pour les comparatifs, qui sont plus familiers.")

    d.objectifs([
        "comprendre que « ne… que » veut dire « seulement » ;",
        "placer le « que » devant ce qu'on limite ;",
        "employer plus de, moins de, autant de avec un nom ;",
        "former un superlatif, et connaître meilleur et mieux.",
    ], notes="Le deuxième objectif est le seul qui demande vraiment du travail : la "
             "place du « que » décide du sens de la phrase.")

    d.declencheur(
        'Observation', "Cette phrase est-elle positive ou négative ?",
        pistes=[
            "« Je n'ai que dix dollars. »",
            "Est-ce que la personne a de l'argent, oui ou non ?",
            "Et « je n'ai pas dix dollars » ?",
            "Qu'est-ce qui change entre les deux ?",
        ],
        notes="Faire voter à main levée avant d'expliquer. Le groupe se partage "
              "presque toujours en deux, et c'est ce partage qui installe la règle.")

    d.regle("« ne… que » veut dire « seulement »",
            "La phrase reste positive. « Je n'ai reçu que onze "
            "candidatures » veut dire que l'employeur en a reçu onze.",
            precision="Le « ne » trompe l'œil : il n'y a aucune négation. Le sens "
                      "est porté par le « que », qui se place juste devant ce qu'on "
                      "limite — et c'est sa place qui fait tout. « Il ne travaille "
                      "que le jour » n'est pas « il ne travaille qu'à Jonquière ».",
            notes="Diapositive à photographier. Astuce à donner : remplacer "
                  "mentalement « ne… que » par « seulement » et relire. Si le sens "
                  "tient, c'est bon.")

    d.cartes('Analyse', "La place du « que » fait le sens", [
        ("Il ne travaille que le jour.", "pas le soir, pas la nuit"),
        ("Il ne travaille qu'à Jonquière.", "pas ailleurs"),
        ("Il n'y a que lui qui travaille.", "les autres ne travaillent pas"),
        ("Elle n'a envoyé que trois lettres.", "temps composé : ne devant l'auxiliaire"),
        ("Il ne fait pas que produire.", "attention : il produit, et il fait autre chose"),
        ("J'en ai reçu que onze.", "à l'oral au Québec, le « ne » tombe"),
    ], cols=1,
       notes="La cinquième carte inverse le sens : « pas que » veut dire « pas "
             "seulement ». Une syllabe, et le paragraphe se retourne. La faire "
             "relire deux fois.")

    d.pratique('Grammaire', "Récrivez avec « ne… que »",
               "Écrivez la phrase entière.", [
        ("Il a reçu seulement onze candidatures.", "Il n'a reçu que onze candidatures."),
        ("Le laboratoire compte seulement sept personnes.", "Le laboratoire ne compte que sept personnes."),
        ("Elle a visité seulement deux régions.", "Elle n'a visité que deux régions."),
        ("Le poste est offert seulement sur le quart de jour.", "Le poste n'est offert que sur le quart de jour."),
        ("Je connais seulement le marché de Montréal.", "Je ne connais que le marché de Montréal."),
        ("L'appel a duré seulement dix minutes.", "L'appel n'a duré que dix minutes."),
    ], corrige=True,
       notes="Exercice `t1que` du module interactif. Vérifier la place du « que » à "
             "chaque correction : c'est là que se fait ou se défait la réponse.")

    d.regle("Comparer une quantité : « de », et jamais d'article",
            "plus de, moins de, autant de, toujours suivis d'un nom. "
            "« Plus des usines » n'existe pas.",
            precision="Après un verbe, le « de » disparaît : « cette région embauche "
                      "plus que la moyenne ». Le superlatif ajoute l'article devant, "
                      "accordé avec le nom : le secteur le plus important, la région "
                      "la plus jeune. Et deux irréguliers, deux seulement : bon donne "
                      "meilleur, bien donne mieux.",
            notes="Diapositive à photographier. « Plus bon » et « plus bien » sont les "
                  "deux fautes qui reviennent le plus dans les lettres du bloc D.")

    d.pratique('Grammaire', "Comparer deux régions",
               "Complétez.", [
        ("Le primaire y occupe deux fois ___ emplois que dans le reste du Québec.", "plus d'"),
        ("À Montréal, il y a ___ postes ouverts et plus de candidats.", "moins de"),
        ("La construction y pèse ___ que la moyenne : 8,9 contre 7,0 %.", "plus"),
        ("Les services y occupent ___ place qu'ailleurs.", "autant de"),
        ("C'est le secteur ___ important en valeur des ventes.", "le plus"),
        ("C'est la région ___ touchée par le manque de relève.", "la plus"),
        ("Pour un technicien, les perspectives y sont ___ qu'à Montréal.", "meilleures"),
        ("Avec neuf ans d'expérience, elle se placerait ___ qu'un diplômé de l'an dernier.", "mieux"),
    ], corrige=True,
       notes="Exercice `t1comp` du module interactif. Les deux derniers sont les "
             "irréguliers : les faire répéter à voix haute.")

    d.billet(
        "Comparez votre région actuelle à une autre, en deux phrases avec des chiffres.",
        exemples=[
            "Une phrase avec « plus de » ou « moins de ».",
            "Une phrase avec un superlatif.",
        ],
        notes="Premier brouillon de l'exposé oral du bloc E. Garder les billets : "
              "les élèves les reprendront en E1.")

    return d.save(dossier)
