# -*- coding: utf-8 -*-
"""A2 · La liaison des quantités.
Bloc A « Je découvre » · couleur teal · 60 min.
Source : mini-leçon `prPhon`, exercice `prPhon` (cartes à écouter).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='teal',
        titre='La liaison des quantités',
        chapeau="« Deux œufs » se dit « deu-zeu ». Ce n'est pas du français "
                "rapide : c'est la prononciation normale. Et c'est ce qui rend "
                "les quantités méconnaissables.",
        duree='60 minutes')

    d.titre(notes="Séance d'écoute. Prévoir le son. Commencer par dicter « deux œufs, trois "
                  "oranges, six oignons » et faire écrire : la surprise est immédiate.")

    d.objectifs([
        "reconnaître une liaison entre un nombre et un nom ;",
        "savoir que c'est le mot suivant qui décide ;",
        "prononcer six et dix de leurs trois façons ;",
        "couper un groupe de mots avant la voyelle pour retrouver le nombre.",
    ])

    d.tableau('Analyse', "Le mot suivant décide",
              ['Ce qui suit', 'Ce qui arrive'],
              [["une voyelle", "la consonne se réveille et se lie"],
               ["une consonne", "la consonne finale reste muette"],
               ["rien (fin de phrase)", "on prononce la forme pleine"]],
              cle=0,
              note="Le même nombre se prononce de deux ou trois façons.",
              notes="Diapo centrale. Faire recopier. C'est exactement la même logique que "
                    "la chute des consonnes, vue dans le module des déplacements.")

    d.cartes('Les liaisons obligatoires', "Devant une voyelle", [
        ("deux œufs",
         "Se dit « deu-zeufs ». Le x de « deux » devient un son [z]."),
        ("trois oranges",
         "Se dit « troi-zoranges ». Même mécanique."),
        ("un ananas",
         "Se dit « u-nananas ». Le n de « un » se prononce avec le mot suivant."),
        ("cent euros",
         "Se dit « cen-teuros ». Le t de « cent » se réveille."),
    ], notes="Faire dire chaque paire par le groupe, deux fois. L'exagération aide ici : "
             "elle installe le réflexe.")

    d.regle('Le cas de six et dix',
            "Ces deux nombres se prononcent de trois façons.",
            precision="Seuls, en fin de phrase : « siss », « diss ». Devant une consonne : "
                      "« si », « di ». Devant une voyelle : « siz », « diz ». « J'en veux "
                      "six » · « six citrons » · « six oignons ».",
            notes="Faire dire les trois formes à voix haute par tout le groupe. C'est la "
                  "diapo la plus utile de la séance.")

    d.piege("Chercher un mot inconnu",
            "« Deuzeufs » ? Je ne connais pas ce mot.",
            "Coupez avant la voyelle : deux — œufs.",
            "Un groupe de mots lié sonne comme un seul mot long et inconnu. Le réflexe qui "
            "sauve : couper avant la voyelle et rendre au nombre sa forme habituelle. "
            "Dans presque tous les cas, le nombre réapparaît.",
            notes="C'est une stratégie d'écoute. Le dire clairement : on travaille la "
                  "compréhension, pas la prononciation.")

    d.pratique('Pratique · 1 de 2', "Liaison ou pas ?",
               "Écoutez chaque groupe.", [
        ("deux œufs", "liaison — voyelle après"),
        ("deux poires", "pas de liaison"),
        ("trois oranges", "liaison"),
        ("trois tomates", "pas de liaison"),
        ("six oignons", "liaison — « siz »"),
        ("six citrons", "pas de liaison — « si »"),
    ], corrige=True,
       notes="Utiliser l'exercice 2 du module. Deux écoutes avant de corriger. Les élèves "
             "peuvent le refaire seuls.")

    d.pratique('Pratique · 2 de 2', "Dites-le à voix haute",
               "Prononcez chaque quantité, puis vérifiez avec l'enregistrement.", [
        ("2 œufs", "deu-zeufs"),
        ("3 ananas", "troi-zananas"),
        ("6 oranges", "si-zoranges"),
        ("10 œufs", "di-zeufs"),
        ("100 grammes", "cent grammes — aucune liaison"),
    ], corrige=True, cols=1,
       notes="Faire dire par toute la classe en même temps : l'effet de groupe lève la "
             "gêne. Puis deux ou trois élèves seuls.")

    d.cartes("Pourquoi ça compte ici", "Les quantités sont partout", [
        ("Au comptoir",
         "« Quatre poitrines », « deux cents grammes », « une livre et demie ». Chaque "
         "commande contient un nombre suivi d'un nom."),
        ("À la caisse",
         "Le montant est dit à voix haute et rarement répété. « Cent euros » et « cent "
         "grammes » ne se prononcent pas pareil."),
        ("Dans une recette",
         "« Deux œufs », « trois oignons », « huit onces ». Les liaisons y sont partout, "
         "et une recette mal entendue se rate."),
    ], notes="Annoncer le bloc C : la commande au comptoir est exactement l'endroit où "
             "cette séance servira.")

    d.billet(
        "Écrivez cinq quantités que vous achetez souvent, et dites-les à voix haute.",
        exemples=[
            "Marquez d'un trait celles qui demandent une liaison.",
            "Exemple : 2 œufs (liaison) · 3 tomates (pas de liaison).",
        ],
        notes="Corriger surtout le repérage : c'est la compétence visée, pas la "
              "prononciation parfaite.")

    return d.save(dossier)
