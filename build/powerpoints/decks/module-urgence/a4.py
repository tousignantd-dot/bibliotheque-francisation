# -*- coding: utf-8 -*-
"""A4 · La trousse de premiers soins et les groupes de mots.
Bloc A · couleur framboise (vocabulaire) · 60 min.
Source : exercices `prMat` et `prGrp`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='framboise',
        titre='La trousse de premiers soins',
        chapeau="Six objets qu'on trouve dans toute trousse, et une règle d'écriture : "
                "nommer précisément suppose d'accorder correctement. « Une compresse "
                "stérile », pas « un compresse stérile ».",
        duree='60 minutes')

    d.titre(notes="Apporter une vraie trousse de premiers soins si l'établissement en a "
                  "une. Faire nommer les objets avant d'ouvrir la présentation.")

    d.objectifs([
        "nommer six objets d'une trousse de premiers soins et dire à quoi ils servent ;",
        "construire un groupe du nom : déterminant, nom, adjectif ;",
        "accorder l'adjectif en genre et en nombre ;",
        "savoir où se place l'adjectif en français.",
    ])

    d.tableau('Analyse', "Six objets et leur usage",
              ['L\'objet', 'À quoi il sert'],
              [["une compresse stérile", "couvrir une plaie sans la contaminer"],
               ["un désinfectant", "éliminer les microbes sur la peau"],
               ["une pince à échardes", "retirer un petit corps étranger"],
               ["un bandage élastique", "maintenir une articulation foulée"],
               ["des gants jetables", "protéger la personne qui soigne"],
               ["une couverture de survie", "garder au chaud une personne en état de choc"]],
              cle=0, props=[0.42, 0.58],
              notes="Faire remarquer que cinq des six noms sont accompagnés d'un "
                    "adjectif : stérile, élastique, jetables, de survie. C'est le sujet "
                    "de la deuxième partie de la séance.")

    d.cartes('En apprendre plus', "Quatre choses à savoir sur les gants", [
        ("Ils protègent celui qui soigne",
         "Pas seulement le blessé. Le sang d'une autre personne peut transmettre des "
         "infections : les gants sont d'abord pour vous."),
        ("Un seul usage",
         "« Jetables » veut dire qu'on les jette après une seule utilisation, même "
         "s'ils paraissent propres."),
        ("À défaut de gants",
         "Un sac de plastique propre sur la main, ou faire comprimer la plaie par le "
         "blessé lui-même avec un linge propre."),
        ("Se laver les mains avant et après",
         "Même avec des gants. C'est le geste le plus efficace de tous les premiers "
         "soins, et le plus souvent oublié."),
    ], notes="La troisième carte est un savoir pratique : au travail, on n'a pas toujours "
             "de gants sous la main.")

    # ── seconde partie · le groupe du nom ──────────────────────────
    d.regle('Le groupe du nom',
            "Déterminant + nom + adjectif : une brûlure superficielle.",
            precision="Les trois mots vont ensemble et changent ensemble. Si le nom est "
                      "féminin, le déterminant et l'adjectif le sont aussi. S'il est "
                      "pluriel, les trois le sont.",
            notes="Écrire « une brûlure superficielle » au tableau et entourer les trois "
                  "marques du féminin. Elles sont visibles sur les trois mots.")

    d.tableau('Analyse', "L'accord en genre et en nombre",
              ['Le groupe', 'Genre', 'Nombre'],
              [["un pansement propre", "masculin", "singulier"],
               ["une plaie propre", "féminin", "singulier"],
               ["des pansements propres", "masculin", "pluriel"],
               ["des plaies propres", "féminin", "pluriel"]],
              cle=0,
              note="« Propre » finit déjà par un e : il ne change pas au féminin, mais il "
                   "prend le s au pluriel.",
              notes="Choisir un adjectif en -e est volontaire : il isole le pluriel du "
                    "féminin. Faire ensuite le même tableau avec « vif, vive ».")

    d.tableau('Analyse', "Où se place l'adjectif",
              ['La place', 'Les adjectifs', 'Exemple'],
              [["après le nom", "la grande majorité", "une douleur vive"],
               ["avant le nom", "petit, grand, beau, bon, nouveau", "une petite cloque"],
               ["les deux", "quelques-uns, avec un sens différent", "un ancien collègue"]],
              cle=0,
              note="En cas de doute, placez l'adjectif après le nom : c'est correct dans "
                   "la grande majorité des cas.",
              notes="Ne pas développer la troisième ligne à ce niveau. La mentionner et "
                    "passer : c'est une curiosité, pas une règle à retenir.")

    d.pratique('Pratique · 1 de 3', "L'objet et son usage",
               "Reliez chaque objet à ce qu'il sert à faire.", [
        ("une compresse stérile", "couvrir une plaie sans la contaminer"),
        ("un désinfectant", "éliminer les microbes sur la peau"),
        ("une pince à échardes", "retirer un petit corps étranger"),
        ("un bandage élastique", "maintenir une articulation foulée"),
        ("des gants jetables", "protéger la personne qui soigne"),
        ("une couverture de survie", "garder au chaud une personne en état de choc"),
    ], corrige=True, cols=2,
       notes="Exercice rapide. Enchaîner sur l'écriture, qui est le vrai objet de la "
             "séance.")

    d.pratique('Pratique · 2 de 3', 'Écrivez le groupe du nom',
               "Accordez le déterminant et l'adjectif avec le nom.", [
        ("(un) brûlure + (superficiel)", "une brûlure superficielle"),
        ("(des) cloque + (petit)", "des petites cloques"),
        ("(le) pansement + (propre)", "le pansement propre"),
        ("(des) douleur + (vif)", "des douleurs vives"),
        ("(un) plaie + (profond)", "une plaie profonde"),
        ("(des) gant + (jetable)", "des gants jetables"),
    ], corrige=True,
       notes="Les items 2 et 5 demandent de déplacer l'adjectif avant le nom. Le "
             "signaler seulement à la correction : c'est le piège utile de l'exercice.")

    d.piege("Le piège de l'adjectif oublié",
            "des plaies profond",
            "des plaies profondes",
            "L'adjectif s'accorde toujours avec le nom qu'il accompagne, même quand il "
            "en est séparé par d'autres mots. C'est l'erreur la plus visible à l'écrit, "
            "et elle ne s'entend presque jamais à l'oral : il faut donc la chercher en "
            "relisant.",
            notes="Faire relire les six réponses de l'exercice précédent en vérifiant "
                  "uniquement les terminaisons d'adjectif.")

    d.pratique('Pratique · 3 de 3', "Décrivez la blessure en un groupe du nom",
               "Déterminant, nom, adjectif — accordés.", [
        ("Une brûlure qui ne touche que le dessus de la peau.",
         "une brûlure superficielle"),
        ("Des coupures qui saignent beaucoup.", "des coupures profondes"),
        ("Un pansement qu'on vient de changer.", "un pansement propre"),
        ("Des douleurs qui reviennent par à-coups.", "des douleurs vives"),
    ], corrige=True,
       notes="Accepter tout adjectif juste, pas seulement celui du corrigé. Ce qui compte "
             "est l'accord, pas le choix du mot.")

    d.billet(
        "Nommez trois objets d'une trousse de premiers soins, avec leur adjectif.",
        exemples=[
            "Écrivez le groupe complet : déterminant, nom, adjectif.",
            "Exemple : « des gants jetables » — masculin, pluriel.",
        ],
        notes="Corriger uniquement les accords. Rendre à la séance suivante, avant le "
              "passé composé, où l'accord du participe reprendra la même logique.")

    return d.save(dossier)
