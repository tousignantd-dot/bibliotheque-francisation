# -*- coding: utf-8 -*-
"""C4 · Le subjonctif de l'opinion et du doute
Bloc C « Défi 2 · L'éditorial et sa thèse » · couleur ambre · 75 min.
Source : exercice `t2subj` et sa mini-leçon. Savoir du niveau 8 : le
subjonctif après les verbes d'opinion niés, les verbes de sentiment, les
tournures impersonnelles d'appréciation et les connecteurs qui l'imposent.
Dernière séance du bloc : le billet de sortie prépare le bloc D.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="Je pense que c'est, je ne pense pas que ce soit",
        chapeau="Le subjonctif dit que ce qui suit n'est pas posé comme "
                "réel : souhaité, craint, apprécié, douteux. L'indicatif dit "
                "l'inverse. Tous les cas particuliers découlent de là.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc C, et la plus dense. La couper en deux "
                  "moitiés nettes avec une pause : les déclencheurs d'abord, les "
                  "formes irrégulières ensuite. Ne pas mélanger.")

    d.objectifs([
        "expliquer la règle unique derrière tous les cas du subjonctif ;",
        "faire basculer un verbe d'opinion en le niant ou en le questionnant ;",
        "employer le subjonctif après un sentiment ou une appréciation ;",
        "garder l'indicatif après les tournures de certitude.",
    ], notes="Le quatrième objectif est celui qu'on oublie. Un texte truffé de "
             "subjonctifs inutiles se lit aussi mal qu'un texte qui n'en a aucun.")

    d.declencheur(
        'Observation', "Qu'est-ce qui change entre ces deux phrases ?",
        pistes=[
            "« Je pense que le projet est bon. »",
            "« Je ne pense pas que le projet soit bon. »",
            "Un seul mot a été ajouté. Pourquoi le verbe change-t-il aussi ?",
            "Et « Croyez-vous que ce soit suffisant ? » — même mécanisme ?",
        ],
        notes="C'est le point le plus utile de la séance et il tient en une "
              "observation. Laisser le groupe formuler la règle avant de la donner : "
              "quand j'affirme ce que je pense, je le pose comme réel, donc "
              "indicatif ; quand je le nie, je ne le pose plus.")

    d.regle("Le subjonctif dit ce qui n'est pas posé comme réel",
            "Souhaité, craint, apprécié, douteux, ou seulement envisagé. "
            "L'indicatif dit ce qui est posé comme un fait, même s'il est "
            "faux.",
            precision="C'est pour cette raison que « je pense que » prend "
                      "l'indicatif : j'affirme. Le test à appliquer devant chaque "
                      "tournure impersonnelle : est-ce que je pose ce fait comme "
                      "réel ? « Il est certain que » : oui, indicatif. « Il est "
                      "souhaitable que » : non, subjonctif.",
            notes="Diapositive à photographier. Y ramener chaque item de la pratique "
                  "plutôt que de faire réciter une liste de déclencheurs : la liste "
                  "s'oublie, la règle reste.")

    d.cartes('Analyse', "Quatre déclencheurs, dans l'ordre d'utilité", [
        ("Les verbes d'opinion, niés ou questionnés",
         "Je pense que le projet est bon. Je ne pense pas que le projet soit "
         "bon. Croyez-vous que ce soit suffisant ? Même chose pour croire, "
         "trouver, être sûr, être certain, il me semble."),
        ("Les verbes de sentiment, toujours",
         "craindre que · regretter que · s'étonner que · être content que · "
         "trouver dommage que. « Je regrette que l'évaluation n'ait pas été "
         "publiée. » Ce qui suit n'est pas donné comme un fait : il est "
         "donné comme ce qui me touche."),
        ("Les tournures d'appréciation",
         "il faut que · il est important que · il vaut mieux que · il est "
         "regrettable que. Mais il est évident que, il est certain que et il "
         "paraît que demandent l'indicatif : ils posent un fait."),
        ("Les connecteurs qui l'imposent",
         "bien que · quoique · pour que · afin que · à moins que · avant "
         "que · sans que · pourvu que. Il n'y a rien à décider, seulement à "
         "retenir. « Pour que chacun puisse se prononcer. »"),
    ], notes="Faire produire une phrase par carte sur le dossier du boisé. La "
             "quatrième carte reprend le « bien que » de C3 : le faire remarquer, "
             "c'est le même savoir vu par l'autre bout.")

    d.tableau('Analyse', "Les formes irrégulières qui couvrent presque tout",
              ['Infinitif', 'Subjonctif présent'],
              [["être", "que je sois · qu'il soit · que nous soyons · qu'ils soient"],
               ["avoir", "que j'aie · qu'il ait · que nous ayons · qu'ils aient"],
               ["aller", "que j'aille · que nous allions · qu'ils aillent"],
               ["faire", "que je fasse · que nous fassions"],
               ["pouvoir", "que je puisse · que nous puissions"],
               ["savoir", "que je sache · que nous sachions"],
               ["les verbes réguliers", "sur la 3e personne du pluriel : ils publient, que je publie"]],
              cle=0,
              notes="Diapositive à photographier. Ces six verbes couvrent la grande "
                    "majorité des cas réels d'un débat. Faire noter la dernière "
                    "ligne : c'est la fabrique du subjonctif régulier, et elle "
                    "dispense d'apprendre le reste.")

    d.pratique('Pratique 1 de 2', "Subjonctif ou indicatif ?",
               "Mettez le verbe entre parenthèses au mode que le début de phrase commande.", [
        ("Je ne pense pas que ce projet (être) ___ la seule solution.", "soit - opinion niée"),
        ("Je pense que le taux d'inoccupation (être) ___ le vrai problème.", "est - opinion affirmée"),
        ("Il est important que la Ville (publier) ___ l'évaluation.", "publie - appréciation"),
        ("Il est évident que la population (vouloir) ___ des logements.", "veut - certitude"),
        ("Je regrette que le conseil (prendre) ___ sa décision aussi vite.", "prenne - sentiment"),
        ("Bien que le comité (avoir) ___ raison, je signerai contre lui.", "ait - bien que"),
        ("Nous demandons un report pour que chacun (pouvoir) ___ se prononcer.", "puisse - but"),
        ("Il est certain que le financement (expirer) ___ en mars.", "expire - certitude"),
    ], corrige=True,
       notes="Faire dire le déclencheur à voix haute avant de répondre : « je ne "
             "pense pas que », donc opinion niée, donc subjonctif. C'est le "
             "raisonnement qu'on veut installer, pas la bonne réponse.")

    d.pratique('Pratique 2 de 2', "Les cas plus fins",
               "Même consigne. Regardez d'abord ce qui précède le verbe.", [
        ("Je crains que ce débat ne (finir) ___ devant les tribunaux.", "finisse - le ne n'est pas une négation"),
        ("À moins que la Ville ne (faire) ___ un geste, le registre passera.", "fasse - à moins que"),
        ("Croyez-vous que trente jours de plus (changer) ___ quelque chose ?", "changent - question"),
        ("Il vaut mieux que nous (aller) ___ à l'assemblée avant de signer.", "allions - appréciation"),
        ("Après qu'il (avoir) ___ parlé, la salle s'est vidée.", "a parlé - indicatif, l'action a eu lieu"),
    ], corrige=True,
       notes="Le premier item mérite un arrêt : « je crains qu'il ne vienne » veut "
             "dire qu'il vient, et que c'est ce que je crains. Ce « ne » est "
             "explétif, il ne nie rien, et on peut l'omettre à l'oral. Le dernier "
             "item est l'exception que tout le monde rate.")

    d.piege('Piège', "Je ne crois pas que c'est vrai",
            "Je ne crois pas que ce soit vrai",
            "La négation d'un verbe d'opinion entraîne le subjonctif. C'est "
            "la construction la plus fréquente d'une discussion, donc la "
            "faute la plus souvent entendue. À l'inverse, ne mettez pas du "
            "subjonctif partout par prudence : quand vous affirmez, "
            "affirmez. L'indicatif est la forme normale du français.",
            notes="Les deux moitiés comptent autant. Un élève qui sort de cette "
                  "séance en subjonctivant tout n'a pas mieux appris que celui qui "
                  "n'en met jamais.")

    d.billet(
        "Écrivez trois phrases : votre position sur le boisé, un doute, une demande.",
        exemples=[
            "Le doute avec un verbe d'opinion nié : je ne pense pas que...",
            "La demande avec une appréciation : il est important que la Ville...",
        ],
        notes="Devoir, et c'est l'entrée du bloc D. Ces trois phrases sont exactement "
              "la matière d'une intervention à la tribune : une position, une "
              "réserve, une demande précise. Les faire garder, on les reprend en D1.")

    return d.save(dossier)
