# -*- coding: utf-8 -*-
"""C2 · Lire une fiche sans la lire au complet
Bloc C « Défi 2 » · couleur teal · 75 min.
Source : exercice `t2fiche`, mini-leçon `t2garde` (première moitié).
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-classe' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='C2', section='teal',
        titre="Lire une fiche sans la lire au complet",
        chapeau="Une fiche d'information est faite de sections titrées. On "
                "lit les titres, on choisit la section qui touche sa "
                "question, et on ne lit que celle-là. Lire du début à la fin, "
                "c'est se donner du travail que la mise en page voulait "
                "éviter.",
        duree='75 minutes')

    d.titre(notes="Séance de compréhension écrite. Projeter la fiche de la Ville de "
                  "Rivière-Noire, telle qu'elle est dans le module, et travailler "
                  "dessus toute la séance.")

    d.objectifs([
        "entrer dans une fiche par ses titres de section ;",
        "repérer un chiffre et l'année qui va avec ;",
        "reconnaître les mots par lesquels une source se montre prudente ;",
        "savoir ce qu'une fiche ne dit pas, et pourquoi.",
    ], notes="Le quatrième objectif est une leçon de méthode : la ville qui plante "
             "les arbres est la ville qui écrit la fiche. Ce qu'elle dit est vrai ; "
             "ce qu'elle choisit de taire est un choix.")

    d.declencheur(
        'Observation', "Combien de temps pour trouver un chiffre ?",
        image=IMG + 'cour-ecole.jpg',
        pistes=[
            "Une page de neuf sections, une seule question.",
            "Par où commencez-vous : le début, ou les titres ?",
            "Combien de sections faut-il vraiment lire ?",
            "Qu'est-ce qui vous fait perdre le plus de temps ?",
        ],
        notes="Chronométrer : donner la fiche et une question, trente secondes. Ceux "
              "qui lisent les titres trouvent, les autres non. La démonstration vaut "
              "mieux que la consigne.")

    d.tableau('Analyse', "Quatre gestes de lecture",
              ['Le geste', 'Ce qu\'il donne'],
              [["Lire les titres",
                "la carte de la page, en dix secondes"],
               ["Chercher les chiffres",
                "les seuls endroits où l'organisme s'engage"],
               ["Chercher l'année",
                "ce qui rend le chiffre citable dans un travail"],
               ["Chercher les mots prudents",
                "environ, de l'ordre de, on estime que, pourrait"]],
              cle=0,
              note="Un chiffre sans son année ne vaut rien dans un travail.",
              notes="Diapositive à photographier. Le quatrième geste renvoie à B4 : "
                    "les marqueurs d'estimation se lisent comme ils s'entendent.")

    d.pratique('Lecture', "Retrouvez le passage qui répond",
               "Une question, un passage de la fiche. Réponse en montrant la ligne.", [
        ("Pourquoi un secteur devient-il un îlot de chaleur ?", "les surfaces sombres absorbent le rayonnement du jour"),
        ("Quels secteurs sont les plus touchés ?", "le centre commercial et le parc industriel est"),
        ("Quel chiffre peut-on citer, avec son année ?", "17 % de canopée, relevé de l'an dernier"),
        ("Où la ville se montre-t-elle prudente ?", "les comparaisons entre villes demandent de la prudence"),
        ("Quelles sont les deux façons dont un arbre rafraîchit ?", "l'ombre, et l'eau rejetée en vapeur"),
        ("Que demande-t-on aux résidents ?", "arroser chaque semaine pendant trois étés"),
    ], corrige=True,
       notes="Le module fait cliquer dans le texte ; en classe, projeter et faire "
             "surligner au tableau. Chronométrer encore : la deuxième moitié va "
             "deux fois plus vite que la première.")

    d.regle("Une fiche est un point de départ",
            "Elle est écrite par quelqu'un qui a un intérêt dans le sujet. "
            "Ce qu'elle dit est vrai ; ce qu'elle choisit de ne pas dire est "
            "un choix, lui aussi.",
            precision="Ici, la ville qui plante les arbres est la ville qui écrit "
                      "la fiche. C'est une bonne source, et ce n'est pas une preuve. "
                      "Un travail sérieux en consulte une deuxième.",
            notes="Diapositive à photographier. Ne pas verser dans la méfiance : le "
                  "point est de croiser, pas de douter.")

    d.tableau('Analyse', "Dans le résumé, ou dehors ?",
              ['La décision', 'Le renseignement'],
              [["On garde", "les surfaces sombres absorbent la chaleur du jour"],
               ["On garde", "17 % de canopée, relevé de l'an dernier"],
               ["On garde", "un arbre de deux ans rafraîchit très peu"],
               ["On garde", "la ville avertit que la comparaison est délicate"],
               ["On enlève", "le programme est financé par les travaux publics"],
               ["On enlève", "à qui téléphoner pour signaler un arbre"]],
              cle=0,
              notes="Diapositive à photographier. Demander la raison de chaque "
                    "décision avant de la montrer : c'est l'exercice, pas la liste.")

    d.piege('Lecture',
            "« C'est intéressant, je le garde. »",
            "« Est-ce que ça répond à ma question ? »",
            "Le budget est un gros chiffre, l'histoire de l'organisme est "
            "une jolie page. Ces phrases-là ne mentent pas : elles occupent "
            "la place de celles qui répondaient. Un résumé de dix lignes "
            "n'a pas de place à donner.",
            notes="Le piège de tout le bloc C, et il revient à chaque séance. Le "
                  "nommer une fois par jour suffit à le faire reculer.")

    d.billet(
        "Trouvez dans votre source une phrase prudente, et recopiez-la.",
        exemples=[
            "Une phrase avec environ, on estime, ou un conditionnel.",
            "Dites ce que cette prudence vous apprend.",
        ],
        notes="Devoir concret. Les phrases prudentes d'une source sont les plus "
              "utiles d'un travail : elles disent ce qu'on ne sait pas encore, et "
              "c'est souvent l'angle qui manque.")

    return d.save(dossier)
