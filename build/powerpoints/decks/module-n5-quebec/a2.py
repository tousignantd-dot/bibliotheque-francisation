# -*- coding: utf-8 -*-
"""A2 · Le son de « ou » et le son de « u »
Bloc A « Je découvre » · couleur indigo · 75 min. Graphie-phonie.
Source : exercice `prPhon` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Le son de « ou » et le son de « u »",
        chapeau="Deux sons que beaucoup de langues ne distinguent pas, et "
                "qui séparent pourtant « la roue » de « la rue », « tout » "
                "de « tu », « le cou » de « le cul ». Le vocabulaire du "
                "voyage en est plein : la soute, le tour, la durée, le sud.",
        duree='75 minutes')

    d.titre(notes="Séance de prononciation, la seule du module. Elle vient tôt exprès : "
                  "les mots travaillés ici — la soute, la durée, le sud, le tour — "
                  "reviennent dans les trois défis. Prévoir de faire beaucoup répéter, "
                  "et à voix haute : cette séance ne s'apprend pas en silence.")

    d.objectifs([
        "entendre la différence entre le son de « ou » et le son de « u » ;",
        "produire les deux sons en tenant les lèvres et la langue en place ;",
        "distinguer deux mots qui ne diffèrent que par ce son ;",
        "prononcer les mots du voyage qui contiennent l'un ou l'autre.",
    ], notes="Le premier objectif précède le deuxième et ne se saute pas : on ne produit "
             "pas une différence qu'on n'entend pas encore. Consacrer la première demie "
             "à l'écoute seule, sans demander de répéter.")

    d.regle("Les deux sons se font au même endroit",
            "Les lèvres sont arrondies dans les deux cas. C'est la langue "
            "qui bouge : en avant pour « u », en arrière pour « ou ».",
            precision="Pour « u », dites « i » puis arrondissez les lèvres sans "
                      "bouger la langue. Le son arrive tout seul.",
            notes="Diapositive à photographier. Le truc du « i » arrondi est le plus "
                  "efficace qu'on connaisse pour cette paire : il donne le résultat en "
                  "une tentative chez la plupart des élèves. Le faire faire devant un "
                  "miroir ou face à un voisin.")

    d.cartes("Quatre paires", "Un seul son les sépare", [
        ("la roue · la rue",
         "La roue de l'autocar. La rue Berri."),
        ("tout · tu",
         "Tout le trajet. Tu pars lundi."),
        ("le tour · la tour",
         "Faire le tour du parc. La tour du phare."),
        ("sourd · sûr",
         "Il est sourd de cette oreille. Je suis sûre de l'heure."),
    ], notes="Faire écouter les quatre paires deux fois avant de les projeter, puis "
             "demander au groupe de lever la main gauche pour « ou » et la droite pour "
             "« u ». On voit immédiatement qui entend et qui devine.")

    d.tableau('Les mots du voyage', "Où est le son « ou », où est le son « u »",
              ['Le son « ou »', 'Le son « u »'],
              [["la soute", "la durée"],
               ["le tour", "le sud"],
               ["nous partons", "une minute"],
               ["le jour", "la nature"]],
              cle=1,
              notes="Ce sont les mots du module, pas des mots d'exercice. Faire "
                    "compléter la colonne de droite par le groupe. « La durée » et « le "
                    "sud » reviennent dès la séance B2.")

    d.pratique('Discrimination', "Lequel entendez-vous ?",
               "L'enseignante lit un mot de chaque paire, sans le montrer.", [
        ("la roue ou la rue ?", "faire lever la main, puis dire lequel"),
        ("le tour ou la tour ?", "l'article aide : ne pas s'en priver"),
        ("nous ou nu ?", "le premier est un pronom, le second un adjectif"),
        ("la boue ou le bus ?", "le second finit par une consonne qu'on entend"),
        ("la soute ou la chute ?", "les deux existent dans le module"),
        ("douze ou douce ?", "piège : les deux ont le son « ou »"),
    ], corrige=True,
       notes="La dernière ligne est un piège volontaire : les deux mots ont le même son. "
             "Il apprend au groupe qu'on peut répondre « les deux pareils », ce qui est "
             "souvent la bonne réponse et que personne n'ose donner.")

    d.piege("Croire que le « u » français existe déjà dans sa langue",
            "C'est comme le « ou », je le dis pareil.",
            "J'écoute d'abord, je répète après, et j'accepte que ce soit nouveau.",
            "Beaucoup de langues n'ont pas ce son du tout. Ce n'est pas un défaut "
            "d'oreille : c'est un son qu'on n'a jamais eu à distinguer, et qui "
            "s'apprend en quelques semaines quand on sait qu'il existe.",
            notes="Le dire sans détour et sans dramatiser. Un élève qui comprend que la "
                  "difficulté est normale y travaille ; un élève qui croit mal entendre "
                  "abandonne. C'est le seul piège de la séance et il est décisif.")

    d.pratique('Production', "Lisez à voix haute, une phrase chacun",
               "Le voisin dit si le son est juste, sans corriger la phrase.", [
        ("La soute est sous le plancher de l'autocar.", "trois fois le son « ou »"),
        ("La durée du trajet est de huit heures.", "« durée » : la langue en avant"),
        ("Nous partons du quai numéro douze.", "« nous », « douze » : son « ou »"),
        ("Rimouski est sur la rive sud du fleuve.", "« sud » : son « u »"),
        ("Le tour de l'île prend une heure.", "« tour » puis « une » : les deux sons"),
    ], corrige=True,
       notes="Faire lire debout et lentement. Le rôle du voisin est important : il "
             "écoute un seul point, le son, et pas la grammaire. C'est ce qui rend la "
             "correction supportable et utile.")

    d.billet(
        "Écrivez deux mots du module : un avec le son « ou », un avec le son « u ».",
        exemples=[
            "Prenez des mots que vous aurez à dire, pas des mots de dictionnaire.",
            "Entraînez-vous à les dire l'un après l'autre, trois fois.",
        ],
        notes="Ramasser les billets. Les mots choisis disent où en est chaque élève : "
              "ceux qui écrivent deux mots du même son n'entendent pas encore la "
              "différence, et ce sont eux qu'il faut reprendre en A3.")

    return d.save(dossier)
