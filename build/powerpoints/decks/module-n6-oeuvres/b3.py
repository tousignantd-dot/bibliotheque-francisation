# -*- coding: utf-8 -*-
"""B3 · Le plus-que-parfait : reculer d'un cran
Bloc B « Défi 1 · Le déroulement du film » · couleur ambre · 75 min.
Source : exercice `t1pqp` et sa mini-leçon « Le plus-que-parfait : reculer
d'un cran ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Le plus-que-parfait : reculer d'un cran",
        chapeau="Un film montre les images ; un texte, lui, n'a que ce "
                "temps-là pour dire au lecteur qu'il vient de reculer de "
                "quarante ans.",
        duree='75 minutes')

    d.titre(notes="Troisième séance du Défi 1, et la plus grammaticale du bloc. Faire "
                  "le lien avec B2 : ce que les trois signaux font au cinéma, le "
                  "plus-que-parfait le fait à l'écrit.")

    d.objectifs([
        "reconnaître un plus-que-parfait à l'écoute et à la lecture ;",
        "le fabriquer avec l'auxiliaire à l'imparfait et le participe ;",
        "accorder le participe quand l'auxiliaire est « être » ;",
        "l'employer pour placer un retour en arrière dans un récit.",
    ], notes="Le quatrième objectif est celui de la production écrite de E2 : un "
             "résumé de ce film sans plus-que-parfait sera confus, forcément.")

    d.declencheur(
        'Observation', "Ces deux phrases racontent-elles la même chose ?",
        pistes=[
            "« Elle a lu la lettre. »",
            "« La lettre avait été écrite en 1978. »",
            "Laquelle des deux actions vient en premier ?",
            "Comment le sais-tu, sans qu'aucune date ne soit donnée ?",
        ],
        notes="Laisser chercher. La réponse — c'est le verbe qui le dit — est le cœur "
              "de la séance, et elle vient presque toujours du groupe.")

    d.tableau('Analyse', "Trois moments, trois temps",
              ['Le temps', 'Ce qu\'il place'],
              [["présent", "Elle lit la lettre. - maintenant"],
               ["passé composé", "Elle a lu la lettre samedi. - un moment du passé"],
               ["plus-que-parfait", "La lettre avait été écrite en 1978. - avant ce moment"],
               ["comment le faire", "auxiliaire à l'imparfait + participe passé"]],
              cle=0,
              note="Le plus-que-parfait recule toujours d'un cran, jamais de deux.",
              notes="Diapositive à photographier. Écrire les trois phrases au tableau "
                    "l'une sous l'autre : la progression se voit mieux à la verticale.")

    d.regle("Comment il se fabrique",
            "L'auxiliaire à l'imparfait, puis le participe passé. Rien de plus.",
            precision="Elle avait pris. Il était parti. Elles s'étaient vues. Si vous "
                      "savez faire le passé composé, vous savez déjà faire le "
                      "plus-que-parfait : c'est le même participe, avec « avait » ou "
                      "« était » à la place de « a » et « est ».",
            notes="Diapositive à photographier. Cette phrase rassure : les élèves "
                  "croient souvent découvrir un temps nouveau, alors qu'ils n'en "
                  "apprennent qu'une moitié.")

    d.regle("L'accord avec « être »",
            "Avec « était », le participe s'accorde avec le sujet - comme au passé composé.",
            precision="Il était parti. Elle était partie. Elles étaient venues. C'est "
                      "exactement la règle que vous connaissez déjà : rien de nouveau "
                      "ne s'ajoute ici. Avec « avait », pas d'accord avec le sujet.",
            notes="Diapositive à photographier. Ne pas ouvrir la question de l'accord "
                  "avec le COD placé avant : ce n'est pas au programme du niveau 6 et "
                  "ça noie la règle simple.")

    d.pratique('Grammaire', "Mettez au plus-que-parfait",
               "Complétez la deuxième phrase avec le verbe entre parenthèses.", [
        ("Estelle arrive le soir. Elle ... (prendre) l'autobus du matin.", "avait pris"),
        ("Elle trouve la lettre. Quelqu'un l' ... (écrire) en 1978.", "avait écrite"),
        ("Le film tient l'affiche onze semaines. Il y ... (être présenté) en premier.", "avait été présenté"),
        ("Réal n'apparaît jamais aujourd'hui. Il ... (partir) un matin de novembre.", "était parti"),
        ("La mère n'en parlait plus. Elle ... (ranger) toutes les photos.", "avait rangé"),
        ("Thérèse ne comprend pas la scène. Elle n' ... (entendre) la phrase.", "avait pas entendu"),
    ], corrige=True, cols=2,
       notes="Les items 2 et 4 sont les deux qui portent l'accord. Les corriger en "
             "dernier, ensemble, pour que la règle se voie deux fois de suite.")

    d.piege("Tout raconter au passé composé",
            "Elle a pris l'autobus du matin, mais elle arrive le soir.",
            "Elle avait pris l'autobus du matin, mais elle arrive le soir.",
            "Avec le passé composé, les deux actions paraissent au même moment, et le "
            "lecteur cherche pourquoi ça ne colle pas. À l'oral, le contexte fait le "
            "travail et personne ne s'en aperçoit ; à l'écrit, il n'y a pas de "
            "contexte, et c'est le verbe qui doit tout dire.",
            notes="C'est la faute la plus fréquente dans les résumés de E2, et la plus "
                  "invisible pour celui qui écrit. Le montrer maintenant coûte moins "
                  "cher que de le corriger dans vingt copies.")

    d.cartes("Où il sert vraiment", "Trois endroits du module", [
        ("Dans la bande-annonce",
         "« le village où elle avait grandi » : le passé du personnage."),
        ("Dans le film",
         "les quatre retours en arrière, que l'image montre et que le texte dit."),
        ("Dans la biographie",
         "« où il avait été présenté en premier » : une date avant une autre."),
        ("Dans ton résumé",
         "chaque fois que tu racontes un retour en arrière, en E2."),
    ], notes="Quatre emplois, tous dans le dossier. Faire chercher la phrase exacte "
             "dans la transcription pour les deux premiers.")

    d.billet(
        "Écris deux phrases : une au passé composé, une au plus-que-parfait.",
        exemples=[
            "Par exemple : « J'ai déménagé en juin. J'avais visité l'appartement en mars. »",
            "Les deux phrases doivent se suivre.",
        ],
        notes="Deux minutes. Les billets où les deux phrases ne se suivent pas "
              "montrent que la notion d'antériorité n'est pas passée : reprendre ces "
              "élèves en B4.")

    return d.save(dossier)
