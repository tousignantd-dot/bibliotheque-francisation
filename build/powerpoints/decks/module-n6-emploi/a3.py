# -*- coding: utf-8 -*-
"""A3 · Un mot en fabrique un autre
Bloc A « Je découvre » · couleur ambre · 75 min.
Source : exercice `prMots` et sa mini-leçon. Savoirs « Formation des mots » et
« Relations sémantiques » du niveau 6 — préfixes, suffixes, nominalisation.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='ambre',
        titre="Un mot en fabrique un autre",
        chapeau="Un document administratif emploie des noms là où l'on "
                "emploierait des verbes en parlant. Défaire cet habillage, "
                "c'est comprendre une phrase de politique en une seconde.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire, mais de vocabulaire qui se fabrique. Elle "
                  "prépare tout le bloc C — une politique interne est écrite en noms "
                  "d'action — et l'exercice t3nom du bloc D.")

    d.objectifs([
        "reconnaître le verbe caché dans un nom en -age, -ment, -tion, -ure ;",
        "former le nom à partir du verbe et lui donner le bon article ;",
        "comprendre un adjectif en -able : « qu'on peut » ;",
        "employer les préfixes re- et dé- pour refaire et défaire.",
    ], notes="Le premier objectif est le plus rentable : c'est celui qui rend lisible "
             "une phrase comme « le comblement des postes par voie interne ».")

    d.declencheur(
        'Observation', "« On affiche le poste » et « l'affichage du poste » : quelle différence ?",
        pistes=[
            "Laquelle des deux phrases dit qui fait l'action ?",
            "Laquelle des deux dit quand ça se passe ?",
            "Où as-tu déjà vu la deuxième forme ?",
        ],
        notes="Laisser le groupe chercher. La réponse — le nom fait disparaître la "
              "personne et le temps — est le cœur de la séance, et elle revient au "
              "bloc D. Ne pas la donner trop vite.")

    d.tableau('Analyse', "Quatre suffixes font des noms d'action",
              ['Le suffixe', 'Du verbe au nom'],
              [["-age (masculin)", "afficher donne un affichage · emballer donne un emballage"],
               ["-ment (masculin)", "remplacer donne un remplacement · classer donne un classement"],
               ["-tion (féminin)", "muter donne une mutation · former donne une formation"],
               ["-ure (féminin)", "ouvrir donne une ouverture · se porter candidat donne une candidature"]],
              cle=0,
              note="Le genre suit le suffixe : une règle qui ne se trompe presque jamais.",
              notes="Diapositive à photographier. Faire trouver au groupe d'autres "
                    "mots en -tion de leur métier : il y en a partout, et beaucoup se "
                    "ressemblent d'une langue à l'autre.")

    d.regle("Pourquoi les documents parlent en noms",
            "Un nom n'a ni personne, ni temps — et c'est exactement ce qu'un document cherche.",
            precision="« On a décidé » demande de savoir qui est « on ». « La "
                      "décision » ne demande rien et vaut pour tout le monde. C'est "
                      "pratique pour l'employeur, et c'est parfois gênant pour le "
                      "lecteur : en lisant, remettez le verbe et demandez-vous qui "
                      "fait l'action.",
            notes="Diapositive à photographier. Le second mouvement — remettre le "
                  "verbe — est une stratégie de lecture, pas une règle de grammaire. "
                  "L'écrire au tableau sous forme de question : « qui fait ça ? ».")

    d.tableau('Deux autres outils', "L'adjectif en -able, les préfixes re- et dé-",
              ['La forme', 'Ce qu\'elle veut dire'],
              [["-able", "« qu'on peut » — payable, réalisable, acceptable"],
               ["in- devant -able", "le contraire — inacceptable, invivable"],
               ["re-", "refaire — recommencer, relire, refaire"],
               ["dé-, dés-", "défaire — décharger, démonter, désapprouver"]],
              cle=0,
              note="Devant une voyelle, « dé- » devient « dés- » : c'est une question de son, pas de sens.",
              notes="« Rouvrir », pas « reouvrir » : le signaler si quelqu'un le "
                    "produit, sans en faire une leçon.")

    d.pratique('Pratique', "Trouve le nom de la même famille",
               "À l'oral d'abord, puis à l'écrit. Attention à l'article.", [
        ("On affiche le poste : c'est ___ du poste.", "l'affichage"),
        ("Elle est mutée à la qualité : elle obtient ___ .", "une mutation"),
        ("Il faut remplacer Ghislain : l'usine prévoit ___ .", "un remplacement"),
        ("L'usine a ouvert en 1961 : ___ remonte à 1961.", "l'ouverture"),
        ("On a décidé d'appliquer le taux : ___ est appliquée.", "la décision"),
        ("Elle a suivi une formation : ___ figure à son dossier.", "la formation"),
    ], corrige=True,
       notes="Faire dire l'article à voix haute avec le nom. C'est là que le genre "
             "s'installe, pas dans une règle apprise.")

    d.piege('Piège', "inventer « un vérifiage » parce que « affichage » existe",
            "garder le verbe quand aucun nom ne vient",
            "Tous les verbes n'ont pas de nom d'action courant. « Vérifier » donne "
            "« une vérification », pas « un vérifiage ». En cas de doute, écrivez la "
            "phrase avec le verbe : elle sera toujours correcte, et souvent plus "
            "claire que le nom.",
            notes="Le dire nettement : personne ne perd de points pour avoir écrit "
                  "une phrase simple. On perd à écrire un mot qui n'existe pas.")

    d.pratique('Lecture', "Défaire la phrase de document",
               "Récrivez chaque phrase avec un verbe, comme on le dirait à voix haute.", [
        ("Le comblement des postes se fait par voie interne.", "on comble les postes à l'interne"),
        ("La transmission de la réponse est faite par écrit.", "on transmet la réponse par écrit"),
        ("L'affichage du poste a eu lieu le 14 septembre.", "le poste a été affiché le 14 septembre"),
        ("La sélection s'est faite sur les compétences.", "le comité a choisi sur les compétences"),
        ("Le remplacement sera assuré par le quart de soir.", "le quart de soir remplacera"),
    ], corrige=True,
       notes="Exercice d'entrée dans le bloc C. Insister sur la question à se poser "
             "chaque fois : qui fait l'action ? Souvent, la réponse est « l'employeur », "
             "et le document ne le dit pas.")

    d.billet(
        "Écris trois noms en -tion que tu connais dans ton métier.",
        exemples=[
            "Avec leur article.",
            "Si le mot ressemble à celui de ta langue, écris les deux.",
        ],
        notes="Deux minutes. Cette liste sert en A4 et revient au bloc D : le "
              "vocabulaire technique d'un métier est déjà à moitié en -tion.")

    return d.save(dossier)
