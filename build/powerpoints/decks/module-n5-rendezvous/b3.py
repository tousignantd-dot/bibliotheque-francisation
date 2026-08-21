# -*- coding: utf-8 -*-
"""B3 · « Je serai là » — le futur simple.
Bloc B « Défi 1 » · couleur ambre · 75 min. Écriture.
Source : exercice `t1futur` et sa mini-leçon.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-rendezvous/images/')


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="« Je serai là » — le futur simple",
        chapeau="« Je vais venir » raconte une intention. « Je viendrai » "
                "prend un engagement. Dans un appel à une clinique, des "
                "deux côtés, on prend des engagements.",
        duree='75 minutes')

    d.titre(notes="Rendre les billets de B2. Écrire les deux phrases au tableau — « je "
                  "vais venir jeudi » et « je viendrai jeudi » — et demander laquelle on "
                  "croirait davantage. La discussion ouvre la séance mieux qu'une règle.")

    d.objectifs([
        "former le futur simple des verbes réguliers ;",
        "employer les huit irréguliers de l'appel ;",
        "reconnaître le futur simple dans ce que dit la clinique ;",
        "distinguer « je serai » de « je serais » à l'écrit.",
    ])

    d.declencheur(
        'Écoute', "« Vous recevrez un rappel automatisé la veille. » Qu'est-ce que ça "
                  "vous demande de faire ?",
        image=IMG + 'telephone-message.jpg',
        pistes=[
            "Qui parle : vous ou la clinique ?",
            "Est-ce une information ou une consigne ?",
            "Que se passe-t-il si vous ne répondez pas au rappel ?",
            "Qu'est-ce qu'il faut noter dans cette phrase ?",
        ],
        notes="Point important : chaque futur simple qu'on vous adresse est une consigne "
              "déguisée. Le faire découvrir plutôt que de l'annoncer.")

    d.regle("Le radical du futur finit toujours par un r",
            "arrive-R-ai · finir-ai · attend-R-ai · ser-ai · aur-ai · ir-ai",
            precision="C'est le son qui signale le futur à l'oreille. Les terminaisons, "
                      "elles, ne changent jamais : -ai, -as, -a, -ons, -ez, -ont, pour "
                      "tous les verbes, sans exception.",
            notes="Diapositive à photographier. Faire dire six verbes à la file en "
                  "écoutant le r : c'est ce qui rend le repérage automatique.")

    d.cartes("La formation, en deux temps", "Un radical, six terminaisons", [
        ("Les verbes en -er et -ir",
         "L'infinitif entier, puis la terminaison. arriver donne j'arriverai · finir donne je finirai"),
        ("Les verbes en -re",
         "Le e tombe avant la terminaison. attendre donne j'attendrai · prendre donne je prendrai"),
        ("Les six irréguliers de l'appel",
         "être donne je serai · avoir donne j'aurai · aller donne j'irai · faire donne je ferai"),
        ("Et deux de plus",
         "falloir donne il faudra · pouvoir donne je pourrai · venir donne je viendrai · recevoir donne vous recevrez"),
    ], notes="Apprendre « je serai, j'aurai, j'irai, il faudra » couvre la moitié de ce "
             "qui se dit dans un appel. Le dire aux élèves : l'effort est court.")

    d.tableau('Qui emploie le futur, et pour dire quoi',
              "Écoutez qui parle",
              ['La phrase', 'Ce que ça veut dire'],
              [["Vous recevrez un rappel la veille.", "attendez-le, et répondez"],
               ["Il faudra être à jeun.", "une consigne, pas une information"],
               ["Ce sera un autre rendez-vous.", "il faudra rappeler"],
               ["Je serai là à seize heures quarante-cinq.", "c'est vous qui vous engagez"]],
              cle=0,
              notes="Les trois premières sont dites par la clinique, la dernière par le "
                    "patient. Faire trouver la différence au groupe.")

    d.piege("Employer le futur après « si » de condition",
            "« Si je serai libre, je viendrai. »",
            "« Si je suis libre, je viendrai. »",
            "Après « si » de condition, on met le présent. Le futur va dans l'autre "
            "moitié de la phrase. C'est une des rares règles du français qui ne souffre "
            "aucune exception.",
            notes="Faire produire trois phrases en « si… je… » à l'oral, rapidement, en "
                  "tour de table. L'erreur disparaît en une dizaine d'essais.")

    d.pratique('Écriture', "Mettez au futur simple",
               "Le verbe est entre parenthèses.", [
        ("Je ___ (être) à la clinique quinze minutes avant.", "serai"),
        ("Vous ___ (recevoir) un rappel automatisé la veille.", "recevrez"),
        ("Ce ___ (être) un autre rendez-vous pour la prise de sang.", "sera"),
        ("Il ___ (falloir) être à jeun douze heures avant.", "faudra"),
        ("J'___ (apporter) ma carte et la liste de mes médicaments.", "apporterai"),
        ("Je vous ___ (rappeler) dès que j'aurai mon horaire.", "rappellerai"),
        ("La docteure ___ (avoir) les résultats jeudi matin.", "aura"),
        ("Si ça continue, nous ___ (aller) plus loin.", "irons"),
    ], corrige=True, cols=2,
       notes="« Rappellerai » prend deux l : le faire remarquer, c'est la seule "
             "difficulté orthographique de la liste.")

    d.pratique('Production', "Trois engagements",
               "Écrivez trois phrases au futur simple, à propos d'un rendez-vous.", [
        ("Ce que vous ferez avant.", "J'apporterai ma carte et je noterai mes questions."),
        ("À quelle heure vous serez là.", "Je serai là à seize heures quarante-cinq."),
        ("Ce que vous ferez si vous ne pouvez pas venir.", "Je vous rappellerai avant jeudi."),
    ], corrige=True,
       notes="Les trois phrases resserviront telles quelles dans la production écrite de "
             "E2. Le dire : ça change l'attention qu'on y met.")

    d.billet(
        "Écrivez ce que vous ferez demain, en trois phrases au futur simple.",
        exemples=[
            "Pas au futur proche : « je ferai », et non « je vais faire ».",
            "Soulignez le r de chaque verbe.",
        ],
        notes="Souligner le r est l'astuce qui fait le plus pour l'orthographe du futur. "
              "Insister dessus.")

    return d.save(dossier)
