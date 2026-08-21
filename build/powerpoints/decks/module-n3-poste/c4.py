# -*- coding: utf-8 -*-
"""C4 · L'adresse sur la boîte, et l'ordre de l'envoi.
Bloc C « Défi 2 · Dire ce qu'il y a dedans, et payer » · couleur ambre · 75 min.
Source : mini-leçon `t2adresse`, exercices `t2adresse` et `t2etapes`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-poste/images/')


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="L'adresse sur la boîte, et l'ordre de l'envoi",
        chapeau="Deux adresses sur la même boîte, jamais au même endroit : la "
                "vôtre en haut à gauche, celle de l'autre au milieu. Et six "
                "étapes qui reviennent toujours dans le même ordre.",
        duree='75 minutes')

    d.titre(notes="Séance d'écriture. Apporter une vraie boîte de carton si possible : "
                  "les deux adresses se placent avec la main, pas sur une diapositive.")

    d.objectifs([
        "placer l'adresse de l'expéditeur et celle du destinataire ;",
        "écrire une adresse québécoise complète, avec le code postal ;",
        "épeler un nom quand on le demande ;",
        "remettre les six étapes d'un envoi dans l'ordre.",
    ])

    d.declencheur(
        'Observation', "Où va chaque adresse sur cette boîte-là ?",
        image=IMG + 'ruban-boite.jpg',
        pistes=[
            "Combien d'adresses faut-il écrire ?",
            "Laquelle doit être la plus grosse ?",
            "Qu'est-ce qui arrive si la boîte ne se rend pas ?",
            "Où écrit-on « fragile » ou « ne pas plier » ?",
        ],
        notes="La troisième piste amène la raison d'être de l'adresse de l'expéditeur : "
              "sans elle, une boîte perdue est perdue pour de bon.")

    d.tableau('Analyse', "Ce qui est écrit sur la boîte de Yassine",
              ['Où', 'Ce qui est écrit'],
              [["En haut à gauche", "Yassine Berrada — 2145, 8e Avenue, app. 3"],
               ["La suite", "Québec (Québec) G1J 3K7"],
               ["Au milieu, en plus gros", "Karim Berrada — 780, 14e Rue Nord-Ouest"],
               ["La suite", "Calgary (Alberta) T2M 3P4"],
               ["À la main, sur le côté", "Ne pas plier — deux kilos cent"]],
              cle=0,
              note="En haut à gauche : celui qui envoie. Au milieu : celui qui reçoit.",
              notes="Diapo à photographier. C'est le document de l'exercice `t2adresse` "
                    "du module. Le faire recopier tel quel sur la fiche : la mise en "
                    "page s'apprend en la reproduisant.")

    d.regle("L'ordre des lignes, toujours le même",
            "le nom, le numéro et la rue, la ville, la province, le code postal",
            precision="Cinq lignes, jamais dans un autre ordre. Le numéro d'appartement "
                      "se met après la rue, avec « app. ». La province s'écrit entre "
                      "parenthèses après la ville : Québec (Québec), Calgary (Alberta).",
            notes="Diapo à photographier. Beaucoup de pays écrivent l'adresse dans "
                  "l'ordre inverse, du pays vers la personne. Le dire, et faire "
                  "comparer avec ce que les élèves connaissent.")

    d.regle("Le code postal",
            "G1J 3K7",
            precision="Six caractères : une lettre, un chiffre, une lettre, une "
                      "espace, un chiffre, une lettre, un chiffre. Il dit "
                      "exactement où livrer. Sans lui, la boîte part quand même, "
                      "mais elle met plus de temps.",
            notes="Diapo à photographier. Faire écrire son propre code postal à chaque "
                  "élève, puis le faire épeler à voix haute au voisin : c'est "
                  "l'entraînement de la diapositive suivante.")

    d.cartes("Épeler quand on vous le demande", "Quatre choses à savoir", [
        ("« Vous épelez, s'il vous plaît ? »",
         "La préposée demande souvent d'épeler un nom de famille. Ce n'est pas une "
         "marque de méfiance : elle doit l'écrire sans faute."),
        ("Dire la lettre, puis un mot",
         "« B comme dans Boston. » C'est ce qu'on fait au téléphone et au comptoir "
         "quand deux lettres se ressemblent."),
        ("Les lettres qui se confondent",
         "B et P, D et T, M et N, G et J. Ce sont les quatre paires qui posent "
         "problème en français : les préparer d'avance."),
        ("Écrire en lettres détachées",
         "Sur une boîte, on n'écrit pas en lettres attachées : chaque lettre "
         "séparée, en majuscules si possible. La machine doit pouvoir lire."),
    ], notes="Faire épeler son nom de famille à chaque élève devant le groupe. "
             "Cinq minutes, et c'est la compétence la plus transférable de la séance.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Regardez le tableau de la boîte, puis répondez.", [
        ("Yassine est l'expéditeur du colis.", "vrai — son adresse est en haut à gauche"),
        ("Karim habite en Alberta.", "vrai"),
        ("L'adresse de l'expéditeur est écrite au milieu.", "faux — en haut à gauche"),
        ("Le code postal du destinataire est T2M 3P4.", "vrai"),
        ("Le colis est parti par Xpresspost.", "faux — colis standard"),
        ("Il y a un numéro de repérage sur le reçu.", "vrai"),
    ], corrige=True,
       notes="C'est l'exercice `t2adresse` du module interactif. Le document de "
             "référence est le tableau projeté deux diapositives plus haut : y revenir "
             "à chaque réponse.")

    d.pratique('Compréhension', "Les six étapes, dans l'ordre",
               "Qu'est-ce qui se passe à chaque étape ?", [
        ("Tu arrives au comptoir avec ta boîte.", "tu dis en une phrase où elle va"),
        ("La préposée pose la boîte sur la balance.", "le poids décide d'une partie du prix"),
        ("Elle demande ce qu'il y a dedans.", "tu nommes le contenu et tu dis si c'est fragile"),
        ("Elle nomme deux vitesses et deux prix.", "tu demandes le délai, puis tu choisis"),
        ("Tu paies au comptoir.", "tu reçois un reçu avec le numéro de repérage"),
        ("Tu rentres à la maison.", "tu suis ton colis sur Internet avec ce numéro"),
    ], corrige=True,
       notes="C'est l'exercice `t2etapes` du module. Il résume les blocs B et C en six "
             "lignes : le projeter à la fin et le faire raconter par un élève, de "
             "mémoire, comme une histoire.")

    d.billet(
        "Écrivez votre adresse complète, dans le bon ordre, avec le code postal.",
        exemples=[
            "Cinq lignes : le nom, le numéro et la rue, la ville, la province, le code postal.",
            "En lettres détachées, comme sur une boîte.",
        ],
        notes="Ramasser et corriger. C'est un billet qui sert bien au-delà du module : "
              "beaucoup d'élèves n'ont jamais écrit leur adresse dans l'ordre d'ici.")

    return d.save(dossier)
