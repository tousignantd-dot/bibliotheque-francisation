# -*- coding: utf-8 -*-
"""C2 · Avant de, après avoir.
Bloc C · couleur ambre (écriture) · 75 min.
Source : mini-leçon `t2avant`, exercices `t2avant` et `t2ordre`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Avant de, après avoir',
        chapeau="Quand vous racontez ce que vous avez fait — au téléphone, dans un "
                "courriel, devant le tribunal — vous devez placer deux actions dans "
                "l'ordre. Ces deux marqueurs servent exactement à ça, et ils "
                "fonctionnent en miroir l'un de l'autre.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire exigeante. Le piège n'est pas la forme, c'est "
                  "l'ordre : ce qui suit « avant de » arrive en deuxième. Prévoir du "
                  "temps sur ce seul point.")

    d.objectifs([
        "placer deux actions dans l'ordre à l'intérieur d'une seule phrase ;",
        "employer avant de suivi de l'infinitif présent ;",
        "employer après suivi de l'infinitif passé ;",
        "accorder le participe passé quand le verbe se construit avec être.",
    ])

    d.regle('Le piège, avant tout le reste',
            "Ce qui suit « avant de » arrive en deuxième. Ce qui suit « après » arrive en premier.",
            precision="C'est l'inverse de l'ordre de lecture, et c'est la seule vraie "
                      "difficulté de la séance. « Je vérifie le panneau avant d'appeler » : "
                      "je vérifie d'abord. « Après avoir vérifié le panneau, j'appelle » : "
                      "je vérifie d'abord aussi. Même ordre réel, deux phrases inversées.",
            notes="Commencer par là. Faire mimer avec deux objets posés sur la table : "
                  "on déplace physiquement l'ordre des actions.")

    d.tableau('Analyse · 1 de 2', "avant de + infinitif présent",
              ['Élément', 'Exemple', 'Rang'],
              [["1re action", "Je vérifie le panneau", "elle a lieu d'abord"],
               ["Le marqueur", "avant d'", "devant une voyelle"],
               ["2e action, à l'infinitif", "appeler la propriétaire", "pas encore faite"]],
              cle=1,
              note="Avant de devient avant d' devant une voyelle ou un h muet : avant "
                   "d'appeler, avant d'utiliser, avant d'habiter. La phrase complète : "
                   "« Je vérifie le panneau avant d'appeler la propriétaire. »",
              notes="Faire produire cinq phrases orales avec avant de avant de passer à "
                    "la suite.")

    d.tableau('Analyse · 2 de 2', "après + infinitif passé",
              ['Élément', 'Exemple', 'Rang'],
              [["1re action, à l'infinitif passé", "Après avoir descendu les vélos,", "déjà terminée"],
               ["2e action", "vous lavez le plancher", "elle suit"]],
              cle=1,
              note="On ne dit jamais « après descendre ». Après le mot après, le verbe est "
                   "obligatoirement à l'infinitif passé — donc avoir ou être suivi du "
                   "participe passé.",
              notes="C'est la forme la plus difficile à produire spontanément. Y consacrer "
                    "le plus de temps.")

    d.cartes('La forme', "Fabriquer un infinitif passé", [
        ("La formule",
         "Deux morceaux : avoir ou être à l'infinitif, puis le participe passé du verbe. "
         "Avoir lavé. Être monté."),
        ("Avec avoir — la grande majorité",
         "avoir lavé, avoir vu, avoir pris, avoir fini, avoir écrit. C'est le cas par "
         "défaut : en cas de doute, c'est probablement avoir."),
        ("Avec être — les déplacements",
         "aller, venir, monter, descendre, entrer, sortir, rentrer, partir, arriver, "
         "rester, tomber. Et tous les verbes pronominaux : s'être levé."),
        ("Les terminaisons du participe passé",
         "-é : parlé, tombé · -t : fait, écrit · -u : reçu, vendu, vu · -i : fini, "
         "réussi · -s : mis, pris."),
    ], notes="Faire copier la liste des verbes avec être. C'est une liste à mémoriser, "
             "il n'y a pas de raccourci.")

    d.regle("L'accord",
            "Être regarde le sujet. Avoir ne le regarde pas.",
            precision="Avec être, le participe s'accorde : après être monté (lui), après "
                      "être montée (elle), après être montés (eux), après être montées "
                      "(elles). Avec avoir, aucun accord avec le sujet : après avoir monté "
                      "ne change jamais, quel que soit le sujet.",
            notes="Formule à faire répéter telle quelle : « être regarde le sujet, avoir "
                  "ne le regarde pas ».")

    d.pratique('Pratique', "Quelle action vient en premier ?",
               "Lisez la phrase et dites laquelle des deux actions a lieu d'abord.", [
        ("Oksana prend une photo avant d'envoyer son courriel.", "la photo, puis le courriel"),
        ("Après avoir terminé leur installation, l'électricien montera au quatrième.", "terminer, puis monter"),
        ("Il faut couper le courant avant de toucher au panneau.", "couper, puis toucher"),
        ("Après avoir descendu ses vélos, Jean-Philippe a lavé le plancher.", "descendre, puis laver"),
        ("Lisez bien votre bail avant de le signer.", "lire, puis signer"),
    ], corrige=True,
       notes="Exercice de compréhension pure, avant toute production. Ne pas laisser passer "
             "une seule erreur d'ordre ici : la production échouera sinon.")

    d.pratique('Pratique', 'Complétez',
               "Avec avant de, avant d', après avoir ou après être.", [
        ("Oksana prend une photo ___ envoyer un courriel à sa propriétaire.", "avant d'"),
        ("___ terminé leur installation, l'électricien montera au quatrième.", "Après avoir"),
        ("Il faut couper le courant ___ toucher au panneau électrique.", "avant de"),
        ("___ descendu ses vélos, Jean-Philippe a lavé le plancher.", "Après avoir"),
        ("___ monté au troisième, Samir a constaté l'ampleur du désordre.", "Après être"),
        ("Lisez bien votre bail ___ le signer.", "avant de"),
    ], corrige=True,
       notes="Le cinquième est le seul avec être : monter est un verbe de déplacement. "
             "Faire justifier.")

    d.piege('La forme après « après »',
            "Après descendre les vélos, je lave le plancher.",
            "Après avoir descendu les vélos, je lave le plancher.",
            "Après le mot après, on ne met jamais un infinitif présent seul. Il faut "
            "l'infinitif passé : avoir ou être, suivi du participe passé. C'est l'erreur "
            "la plus fréquente, et elle s'entend tout de suite.",
            notes="Faire corriger oralement cinq phrases fautives inventées sur place.")

    d.piege('Le sujet unique',
            "Avant d'appeler la propriétaire, elle a vérifié le panneau.",
            "Avant d'appeler la propriétaire, j'ai vérifié le panneau.",
            "Les deux actions doivent avoir le même sujet. Si les sujets diffèrent, on "
            "abandonne l'infinitif et on emploie une phrase complète : « avant que la "
            "propriétaire appelle… ». C'est une condition, pas une préférence de style.",
            notes="Condition souvent passée sous silence, et pourtant elle explique la "
                  "moitié des phrases bancales produites par le groupe.")

    d.pratique('Vérification', 'Cinq questions rapides',
               "Répondez sans regarder vos notes.", [
        ("« Avant de signer, lisez votre bail. » Quelle action vient en premier ?", "lire"),
        ("« Après avoir payé, il a reçu un reçu. » Quelle action vient en premier ?", "payer"),
        ("Après avoir fini, ou après finir ?", "après avoir fini"),
        ("Elle est rentrée, puis elle a soupé. On dit…", "Après être rentrée chez elle, elle a soupé."),
        ("« Avant d' » s'emploie devant…", "une voyelle ou un h muet"),
    ], corrige=True,
       notes="La quatrième réunit les deux difficultés : être, et l'accord au féminin. "
             "Si le groupe la réussit, la séance est acquise.")

    d.billet(
        "Racontez en une phrase deux choses que vous avez faites hier, dans l'ordre.",
        exemples=[
            "Utilisez avant de dans une phrase, puis récrivez la même idée avec après avoir.",
            "Exemple : « J'ai lavé la vaisselle avant de sortir. » / « Après avoir lavé la vaisselle, je suis sorti. »",
        ],
        notes="La reformulation est l'exercice clé : produire les deux formes pour la même "
              "idée prouve que l'ordre est compris.")

    return d.save(dossier)
