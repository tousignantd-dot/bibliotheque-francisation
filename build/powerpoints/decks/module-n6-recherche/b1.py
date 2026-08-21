# -*- coding: utf-8 -*-
"""B1 · Lisons l'offre au complet.
Bloc B « Défi 1 · L'offre d'emploi » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n6-recherche/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Lisons l'offre au complet",
        chapeau="Une offre détaillée n'est pas un titre suivi de trois "
                "paragraphes en désordre : c'est quatre parties, toujours les "
                "mêmes. Savoir où regarder fait décider en deux minutes.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 1. Chacun devrait avoir apporté une offre "
                  "réelle, trouvée en devoir. Ceux qui n'en ont pas travaillent sur "
                  "celle de Boisverte, projetée.")

    d.objectifs([
        "reconnaître les quatre parties d'une offre d'emploi détaillée ;",
        "trouver les tâches et les reconnaître comme des infinitifs ;",
        "distinguer ce qui est requis de ce qui est un atout ;",
        "lire les conditions sans les sauter.",
    ], notes="Le quatrième objectif est celui qu'on saute toujours. Insister : les "
             "conditions disent l'horaire, le statut et les avantages.")

    d.declencheur(
        'Observation', "Trois paragraphes. Par où commencer ?",
        image=IMG + 'offre-ecran.jpg',
        pistes=[
            "Lisez-vous une offre du début à la fin ?",
            "Ou cherchez-vous d'abord quelque chose de précis ?",
            "Que cherchez-vous en premier ?",
            "Qu'est-ce qui vous ferait renoncer tout de suite ?",
        ],
        notes="Beaucoup répondent « le salaire ». Il n'y est pas toujours. Ce qui y est "
              "toujours : les tâches et les exigences.")

    d.dialogue('Dialogue · 1 de 3', "L'entreprise, puis les tâches", [
        ("DJAMILA", "Regardez celle-ci. Boisverte, à Longueuil. Ils cherchent un commis à l'inventaire.", True),
        ("MARISOL", "J'ai lu le titre, mais après, il y a trois paragraphes. Je me perds.", True),
        ("DJAMILA", "Une offre détaillée a toujours les mêmes parties. La première, c'est l'entreprise : qui elle est, ce qu'elle fabrique.", True),
        ("MARISOL", "« Boisverte fabrique des meubles en bois massif depuis 1998. Quarante employés. » D'accord, ça je comprends.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Marisol dit « je me perds » — c'est la phrase d'un lecteur qui n'a pas de "
             "plan. Le module lui en donne un.")

    d.dialogue('Dialogue · 2 de 3', "Requis, ou atout ?", [
        ("DJAMILA", "Les exigences. Attention ici : il y a ce qui est requis et ce qui est un atout. Ce n'est pas pareil.", True),
        ("MARISOL", "« Requis : deux ans d'expérience en entrepôt, français fonctionnel. Atout : connaissance d'un logiciel d'inventaire. »", True),
        ("DJAMILA", "Le requis, il vous le faut. L'atout, c'est un plus. Si vous n'avez que l'atout qui manque, vous postulez quand même.", True),
        ("MARISOL", "Le logiciel, je l'ai utilisé six ans. Ce n'était pas le même, mais je sais comment ça marche.", True),
    ], notes="C'est le point le plus utile de la séance : un atout manquant n'empêche "
             "pas de postuler. Beaucoup de candidats se retirent eux-mêmes pour rien.")

    d.dialogue('Dialogue · 3 de 3', "Les conditions", [
        ("DJAMILA", "Et la dernière partie, les conditions : trente-sept heures et demie, poste permanent, assurance collective après trois mois.", True),
        ("MARISOL", "Permanent… ça veut dire que ça ne finit pas ?", True),
        ("DJAMILA", "Ça veut dire qu'il n'y a pas de date de fin prévue. Ce n'est pas un contrat de six mois. C'est exactement ce que vous cherchiez.", True),
    ], notes="Reprendre les quatre mots de la séance A1 : temps plein, temps partiel, "
             "permanent, contrat. Ils reviennent ici dans un texte réel.")

    d.tableau('Analyse', "Les quatre parties, dans l'ordre",
              ['La partie', 'Ce qu\'on y trouve'],
              [["1. L'entreprise", "Ce qu'elle fait, depuis quand, combien d'employés."],
               ["2. Les tâches", "Ce que vous ferez tous les jours, écrit à l'infinitif."],
               ["3. Les exigences", "Ce qui est requis, et ce qui est un atout."],
               ["4. Les conditions", "Heures, statut, salaire, avantages."]],
              cle=0,
              note="L'ordre varie un peu d'une offre à l'autre. Les quatre parties, elles, y sont toujours.",
              notes="Diapositive à photographier. C'est la grille de lecture du bloc B "
                    "entier.")

    d.regle("Les tâches sont à l'infinitif",
            "Tenir, recevoir, préparer, signaler.",
            precision="Une offre écrit les tâches à l'infinitif parce qu'elle ne parle "
                      "encore de personne. Cela donne un repère de lecture très fiable : "
                      "la liste de verbes à l'infinitif, c'est la liste des tâches. Et au "
                      "moment de répondre, on reprend ces mêmes verbes, conjugués.",
            notes="Diapositive à photographier. Le lien avec la lettre de motivation du "
                  "bloc C se fait ici.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue et l'offre projetée.", [
        ("Boisverte fabrique des meubles depuis 1998.", "vrai"),
        ("« Signaler les écarts » est une des tâches.", "vrai"),
        ("Connaître le logiciel est obligatoire.", "faux — c'est un atout"),
        ("Deux ans d'expérience sont requis.", "vrai"),
        ("Un poste permanent est un contrat de six mois.", "faux — sans date de fin"),
        ("Marisol devrait postuler malgré l'atout manquant.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la ligne exacte de l'offre.")

    d.billet(
        "Découpez votre offre en quatre parties.",
        exemples=[
            "Écrivez 1, 2, 3, 4 dans la marge, en face de chaque bloc.",
            "S'il manque une partie, notez laquelle : c'est une question à poser en entrevue.",
        ],
        notes="Une offre sans conditions écrites est fréquente. Ce n'est pas suspect, "
              "mais c'est une question à préparer.")

    return d.save(dossier)
