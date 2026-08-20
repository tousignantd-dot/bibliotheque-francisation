# -*- coding: utf-8 -*-
"""C3 · Un plat qui ne convient pas.
Bloc C · couleur ambre (écriture) · 60 min.
Source : dialogue `t2b`, exercices `t2b` et `t2signal`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre='Un plat qui ne convient pas',
        chapeau="Manon avait demandé le poulet sans sauce. Il y en a. Elle le "
                "dit — sans exiger qu'on le refasse. Il y a plusieurs façons "
                "de signaler quelque chose.",
        duree='60 minutes')

    d.titre(notes="Cette séance nuance la précédente : signaler ne veut pas dire exiger. "
                  "C'est une distinction que beaucoup d'élèves n'ont pas.")

    d.objectifs([
        "signaler une erreur sans exiger une correction ;",
        "accepter ou refuser la solution proposée ;",
        "comprendre pourquoi le restaurant préfère le savoir ;",
        "comparer les usages d'ici et d'ailleurs.",
    ])

    d.dialogue('Dialogue · 1 de 2', "Signaler sans exiger", [
        ("MANON", "J'avais demandé le poulet sans sauce. Il y en a beaucoup.", True),
        ("VINCENT", "Ah, je suis désolé. Je vous en rapporte un autre ?", True),
        ("MANON", "Ce n'est pas nécessaire, je vais l'enlever. Mais je préfère vous le dire.", True),
        ("VINCENT", "Vous faites bien. Je le note pour la cuisine.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Les quatre répliques sont teintées : c'est un modèle complet d'échange. « Je "
             "préfère vous le dire » est la phrase clé.")

    d.dialogue('Dialogue · 2 de 2', "Pourquoi le dire", [
        ("ANDRÉS", "Tu ne veux pas qu'ils le refassent ?", False),
        ("MANON", "Non, ça prendrait vingt minutes et tu aurais fini de manger.", True),
        ("ANDRÉS", "Chez moi, on ne dirait rien du tout.", True),
        ("MANON", "Ici non plus, beaucoup de gens ne disent rien. Mais ils préfèrent qu'on le dise.", True),
    ], notes="La réponse de Manon est honnête : ici non plus, tout le monde ne dit pas "
             "tout. C'est une nuance importante — il ne s'agit pas d'imposer un usage.")

    d.tableau('Analyse', "Trois façons de signaler",
              ['Ce que je dis', 'Ce que ça demande'],
              [["Je préfère vous le dire.", "rien — juste une information"],
               ["Est-ce que ce serait possible de…", "une correction"],
               ["Je ne peux pas manger ça.", "un remplacement"]],
              cle=0,
              note="La première est la plus employée, et la moins connue des élèves.",
              notes="Diapo à photographier. Signaler sans exiger est une possibilité que "
                    "beaucoup ignorent.")

    d.regle("Signaler sans exiger",
            "« Je préfère vous le dire. »",
            precision="Cette phrase informe sans rien demander. Le restaurant note "
                      "l'erreur, la cuisine en tient compte, et vous n'attendez pas vingt "
                      "minutes de plus. C'est souvent la meilleure solution quand le "
                      "problème est réel mais supportable.",
            notes="Faire répéter la phrase par le groupe. Elle est courte et très utile.")

    d.regle("Pourquoi le restaurant préfère le savoir",
            "Sinon, il ne peut rien corriger.",
            precision="Une erreur signalée est une erreur qui ne se reproduira pas. Une "
                      "erreur tue laisse le restaurant croire que tout va bien — et il ne "
                      "comprendra pas pourquoi vous n'êtes pas revenu. Le dire est un "
                      "service rendu, pas un reproche.",
            notes="C'est le raisonnement de Manon, et c'est celui qui convainc le mieux.")

    d.piege("Exiger quand on veut seulement informer",
            "Il y a de la sauce, refaites-le.",
            "J'avais demandé sans sauce. Ce n'est pas nécessaire de le refaire, mais je préfère vous le dire.",
            "Exiger un remplacement pour un détail supportable met tout le monde dans "
            "l'embarras — et vous fait attendre vingt minutes. Informer suffit souvent, et "
            "c'est mieux reçu.",
            notes="La nuance est fine mais très utile. Faire jouer les deux versions.")

    d.pratique('Pratique · 1 de 2', "Est-ce qu'on le dit ?",
               "Dans un restaurant d'ici.", [
        ("Mon plat est froid.", "oui"),
        ("J'avais demandé sans sauce.", "oui"),
        ("Je n'aime pas le goût.", "mieux vaut non"),
        ("Il manque un couvert.", "oui"),
        ("Mon verre est sale.", "oui"),
        ("Le prix me semble élevé.", "mieux vaut non"),
    ], corrige=True,
       notes="Reprendre la règle : le restaurant peut-il y faire quelque chose ?")

    d.pratique('Pratique · 2 de 2', "Informer, ou demander une correction ?",
               "Choisissez la bonne formulation.", [
        ("De la sauce que vous n'aviez pas demandée, mais mangeable", "Je préfère vous le dire."),
        ("Un plat franchement froid", "Est-ce que ce serait possible de le réchauffer ?"),
        ("Un plat qui n'est pas celui que vous avez commandé", "Ce n'est pas ce que j'avais commandé."),
        ("Un ingrédient auquel vous êtes allergique", "Je ne peux pas manger ça, je suis allergique."),
    ], corrige=True, cols=1,
       notes="La dernière ligne n'est pas négociable : une allergie demande un "
             "remplacement, pas une information.")

    d.cartes("Comparer les usages", "Sans hiérarchie", [
        ("Là où on ne dit rien",
         "Dans beaucoup de cultures, signaler un problème au restaurant est mal vu — cela "
         "fait perdre la face à la personne qui sert."),
        ("Ici",
         "On le dit, généralement sans conflit, et le personnel s'excuse. Mais beaucoup de "
         "gens d'ici ne disent rien non plus."),
        ("Ce qu'il faut retenir",
         "Vous avez le droit de le dire, et c'est bien reçu. Vous n'êtes pas obligé. "
         "Connaître l'usage, c'est pouvoir choisir."),
    ], notes="La troisième carte est la bonne façon de conclure : on donne un choix, pas "
             "une règle de comportement.")

    d.billet(
        "Racontez une fois où quelque chose n'allait pas, au restaurant ou ailleurs.",
        exemples=[
            "L'avez-vous dit ? Pourquoi ?",
            "Que feriez-vous maintenant ?",
        ],
        notes="Bilan du bloc C. Les récits sont souvent riches et alimentent la production "
              "orale de E1.")

    return d.save(dossier)
