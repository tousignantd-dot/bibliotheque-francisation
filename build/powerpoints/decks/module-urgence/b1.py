# -*- coding: utf-8 -*-
"""B1 · À l'urgence : raconter ce qui est arrivé.
Bloc B · couleur acier (compréhension orale) · 75 min.
Source : dialogue `t1` et exercice `t1vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="À l'urgence : raconter ce qui est arrivé",
        chapeau="« Racontez-moi ce qui s'est passé. » Sept répliques pour répondre, et "
                "une phrase qui change tout : « Vous avez bien réagi. »",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Rappeler la chronologie : l'accident à onze "
                  "heures, quinze minutes d'eau froide, l'appel au 811, puis l'urgence.")

    d.objectifs([
        "raconter un accident dans l'ordre où il est arrivé ;",
        "dire l'heure et la durée d'un événement passé ;",
        "expliquer les premiers soins déjà donnés ;",
        "comprendre ce que le médecin vérifie en écoutant le récit.",
    ])

    d.dialogue('Dialogue · 1 de 2', "Racontez-moi ce qui s'est passé", [
        ("L'URGENTOLOGUE", "Bonjour. Racontez-moi ce qui s'est passé.", False),
        ("FATOU", "Je travaillais en cuisine. L'huile a éclaboussé et je me suis brûlé "
                  "l'avant-bras droit.", True),
        ("L'URGENTOLOGUE", "À quelle heure est-ce arrivé ?", False),
        ("FATOU", "Vers onze heures. J'ai mis mon bras sous l'eau froide pendant quinze "
                  "minutes.", True),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="Passer l'audio du défi 1. Faire remarquer que Fatou répond à la question de "
             "l'heure ET ajoute ce qu'elle a fait. La deuxième information n'était pas "
             "demandée, et c'est celle qui compte le plus.")

    d.dialogue('Dialogue · 2 de 2', "Vous avez bien réagi", [
        ("L'URGENTOLOGUE", "Vous avez bien réagi. Est-ce que vous avez percé les "
                           "cloques ?", True),
        ("FATOU", "Non, l'infirmière d'Info-Santé m'a dit de ne pas y toucher.", True),
        ("L'URGENTOLOGUE", "Parfait. Je vais nettoyer la plaie et poser un pansement.",
         False),
    ], notes="« Vous avez bien réagi » n'est pas une politesse : c'est une information "
             "médicale. Les quinze minutes d'eau froide ont limité la profondeur de la "
             "brûlure. Le dire au groupe.")

    d.tableau('Analyse', "Le récit de Fatou, en quatre temps",
              ['Le moment', 'Ce qu\'elle dit'],
              [["ce que je faisais", "Je travaillais en cuisine."],
               ["ce qui est arrivé", "L'huile a éclaboussé."],
               ["ce que ça m'a fait", "Je me suis brûlé l'avant-bras droit."],
               ["ce que j'ai fait", "J'ai mis mon bras sous l'eau froide."]],
              cle=0,
              note="Quatre phrases, dans l'ordre du temps. C'est la structure de tout "
                   "récit d'accident, au travail comme à l'hôpital.",
              notes="Faire copier les quatre étiquettes de gauche dans le cahier. Elles "
                    "servent de plan pour l'exercice de production, en B4.")

    d.regle('La règle du récit',
            "On raconte dans l'ordre où c'est arrivé, pas dans l'ordre d'importance.",
            precision="Ce que je faisais, ce qui est arrivé, ce que ça m'a fait, ce que "
                      "j'ai fait ensuite. Un récit dans le désordre oblige l'auditeur à "
                      "reconstruire, et il se trompera.",
            notes="Faire raconter volontairement dans le désordre par un élève, puis dans "
                  "l'ordre. Le groupe entendra la différence tout seul.")

    d.cartes('Analyse', "Quatre informations que le médecin cherche", [
        ("Le mécanisme",
         "Comment l'accident s'est produit : de l'huile, de l'eau bouillante, une "
         "flamme. Chaque cause donne une brûlure différente."),
        ("L'heure",
         "Une brûlure évolue pendant les premières heures. Savoir quand elle est "
         "arrivée dit à quel stade elle en est."),
        ("Les premiers soins",
         "Ce qui a été fait — et pendant combien de temps. Quinze minutes d'eau froide "
         "et trois minutes ne donnent pas le même résultat."),
        ("Ce qui n'a pas été fait",
         "Avoir percé une cloque, mis du beurre ou de la glace change le traitement. "
         "Il faut le dire, même si on sait maintenant que c'était une erreur."),
    ], notes="La quatrième carte demande du courage : on avoue une erreur. Le dire "
             "clairement — un médecin n'est pas là pour juger, il a besoin de savoir.")

    d.pratique('Pratique · 1 de 3', "Vrai ou faux — à l'urgence",
               "Répondez sans relire le dialogue.", [
        ("Fatou travaillait en cuisine au moment de l'accident.", "VRAI"),
        ("Elle s'est brûlé l'avant-bras gauche.", "FAUX — le droit"),
        ("L'accident est arrivé vers onze heures.", "VRAI"),
        ("Elle a mis son bras sous l'eau froide quinze minutes.", "VRAI"),
        ("Le médecin trouve qu'elle a mal réagi.", "FAUX — il dit qu'elle a bien réagi"),
        ("Fatou a percé les cloques elle-même.", "FAUX — elle n'y a pas touché"),
        ("Le médecin va nettoyer la plaie et poser un pansement.", "VRAI"),
    ], corrige=True,
       notes="La deuxième est celle qui trompe : le côté est dit une seule fois, au "
             "milieu d'une longue phrase.")

    d.pratique('Pratique · 2 de 3', "Remettez le récit dans l'ordre",
               "Numérotez de 1 à 5 selon l'ordre où c'est arrivé.", [
        ("Elle a mis son bras sous l'eau froide.", "3"),
        ("Elle travaillait en cuisine.", "1"),
        ("Mathieu a appelé Info-Santé.", "4"),
        ("L'huile a éclaboussé son avant-bras.", "2"),
        ("Elle est arrivée à l'urgence.", "5"),
    ], corrige=True,
       notes="Faire justifier chaque position par un mot du dialogue. C'est un exercice "
             "de compréhension fine, pas de mémoire.")

    d.piege("Le piège du récit trop court",
            "Je me suis brûlée.",
            "Je travaillais en cuisine, l'huile a éclaboussé et je me suis brûlé l'avant-bras droit vers onze heures.",
            "« Je me suis brûlée » ne dit ni comment, ni où sur le corps, ni quand. Le "
            "médecin devra poser quatre questions. Une phrase préparée d'avance en fait "
            "gagner cinq, et personne n'oublie l'essentiel dans la panique.",
            notes="Faire produire cette phrase longue par trois ou quatre élèves, à voix "
                  "haute. Ne corriger que l'ordre et le contenu, pas encore les temps "
                  "verbaux — ce sera l'objet de B2.")

    d.pratique('Pratique · 3 de 3', "Racontez l'accident",
               "Quatre phrases : ce que je faisais, ce qui est arrivé, ce que ça m'a "
               "fait, ce que j'ai fait.", [
        ("Une coupure en préparant des légumes",
         "Je préparais des légumes. Le couteau a glissé. Je me suis coupé le doigt. "
         "J'ai comprimé avec un linge propre."),
        ("Une chute dans un escalier",
         "Je descendais l'escalier. J'ai glissé sur une marche mouillée. Je me suis "
         "tordu la cheville. J'ai mis de la glace."),
        ("Une brûlure avec de l'eau bouillante",
         "Je vidais une casserole. L'eau bouillante a débordé. Je me suis brûlé la main. "
         "J'ai mis la main sous l'eau froide quinze minutes."),
    ], corrige=True,
       notes="Les corrigés sont des modèles, pas des réponses uniques. Ce qu'on évalue "
             "est la présence des quatre étapes, dans l'ordre.")

    d.billet(
        "Racontez en quatre phrases un petit accident qui vous est déjà arrivé.",
        exemples=[
            "Ce que vous faisiez · ce qui est arrivé · ce que ça vous a fait · ce que "
            "vous avez fait.",
            "Si rien ne vous vient, inventez : la structure compte plus que la vérité.",
        ],
        notes="Ces billets serviront de matière première en B2, où l'on travaillera les "
              "temps du passé sur les phrases produites par le groupe lui-même.")

    return d.save(dossier)
