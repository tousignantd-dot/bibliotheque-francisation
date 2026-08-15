# -*- coding: utf-8 -*-
"""D1 · Le questionnaire et la fiche-conseil.
Bloc D · couleur teal (lire et répondre) · 75 min.
Source : exercices `t3form`, `t3vf` et `t3q` — questionnaire de santé, tendinite.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='teal',
        titre='Le questionnaire et la fiche-conseil',
        chapeau="Avant la physiothérapie, Yannick doit remplir un formulaire et lire une "
                "fiche. Deux documents écrits qu'on remplit seul, sans personne pour "
                "expliquer les mots.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 3. Demander qui a déjà eu à remplir un formulaire "
                  "de santé en français. Les difficultés nommées par le groupe orientent "
                  "la séance.")

    d.objectifs([
        "comprendre les rubriques d'un questionnaire de santé ;",
        "y répondre brièvement, sans phrase complète ;",
        "lire une fiche-conseil et en tirer les gestes à faire ;",
        "reconnaître quand une fiche dit de consulter.",
    ])

    d.tableau('Analyse', "Les cinq rubriques du questionnaire",
              ['La rubrique', 'La réponse de Yannick'],
              [["Motif de la consultation", "Douleur et enflure au genou droit"],
               ["Depuis combien de temps ?", "Depuis la nuit dernière"],
               ["Allergies connues", "Aucune"],
               ["Médicaments pris actuellement", "Un anti-inflammatoire, au besoin"],
               ["Occupation", "Manutentionnaire dans un entrepôt"]],
              cle=0,
              note="Aucune réponse n'est une phrase complète. Un formulaire se remplit "
                   "en groupes de mots.",
              notes="C'est le point de la séance : on n'écrit pas « Je travaille dans un "
                    "entrepôt », on écrit « Manutentionnaire dans un entrepôt ».")

    d.regle('La règle du formulaire',
            "On répond par un groupe de mots, jamais par une phrase.",
            precision="Motif : douleur au genou droit. Pas : « Je viens parce que j'ai "
                      "mal au genou droit. » Le formulaire est lu vite, par quelqu'un "
                      "qui cherche une information précise à un endroit précis.",
            notes="Cette règle est l'inverse de celle des exercices oraux du module. "
                  "Le dire explicitement, sinon les élèves croient s'être trompés avant.")

    d.cartes('En apprendre plus', "Quatre pièges des formulaires de santé", [
        ("« Aucune » plutôt que le vide",
         "Une case laissée vide veut dire « je n'ai pas lu ». Écrivez « aucune » ou "
         "« non » : c'est une réponse, et elle compte."),
        ("Les allergies : tout compte",
         "Médicaments, aliments, latex, piqûres. Une allergie oubliée ici peut causer "
         "une réaction grave pendant un soin."),
        ("« Occupation » veut dire métier",
         "Ce n'est pas un loisir. Pour un problème musculaire, c'est souvent "
         "l'information la plus utile du formulaire."),
        ("Les médicaments : donnez le nom",
         "« Des pilules pour la pression » ne suffit pas. Prenez une photo de vos boîtes "
         "avec votre téléphone : c'est la solution la plus simple."),
    ], notes="La quatrième carte est un conseil pratique à donner en toutes lettres : "
             "photographier ses boîtes de médicaments. Beaucoup le feront le soir même.")

    d.tableau('Analyse', "La fiche-conseil sur la tendinite",
              ['La rubrique', 'Ce qu\'elle dit'],
              [["Ce que c'est", "une irritation du tendon"],
               ["Les signes", "douleur qui élance, enflure, raideur le matin"],
               ["Pour soulager", "glace 20 minutes, 3 fois par jour, repos"],
               ["Pour éviter", "plier les genoux, alterner les tâches, s'échauffer"],
               ["Quand consulter", "si ça dure plus d'une semaine"]],
              cle=0,
              note="Toute fiche-conseil suit ces cinq rubriques, quel que soit le "
                   "problème. Les connaître, c'est savoir lire n'importe laquelle.",
              notes="Faire chercher les cinq rubriques dans la fiche sur l'entorse, en "
                    "E1 : elles y sont, dans le même ordre.")

    d.regle("La rubrique qu'on lit en dernier et qui compte le plus",
            "« Quand consulter » dit à quel moment la fiche ne suffit plus.",
            precision="Une fiche-conseil couvre les cas ordinaires. La dernière rubrique "
                      "dit où s'arrête l'ordinaire : plus d'une semaine, impossible de "
                      "marcher, la cheville est déformée. Lisez-la en premier.",
            notes="Faire relire cette rubrique deux fois. C'est le seul endroit de la "
                  "fiche qui parle de danger.")

    d.pratique('Pratique · 1 de 3', 'Remplissez le formulaire',
               "Répondez par un groupe de mots, comme sur un vrai formulaire.", [
        ("Motif de la consultation", "Douleur au bas du dos"),
        ("Depuis combien de temps ?", "Trois jours"),
        ("Allergies connues", "Aucune / Pénicilline"),
        ("Médicaments pris actuellement", "Aucun / Un anti-inflammatoire, au besoin"),
        ("Occupation", "Préposée à l'entretien"),
    ], corrige=True,
       notes="Corriger uniquement la forme : est-ce un groupe de mots ou une phrase ? "
             "Le contenu appartient à chacun.")

    d.pratique('Pratique · 2 de 3', 'Vrai ou faux — la fiche-conseil',
               "D'après la fiche sur la tendinite.", [
        ("Une tendinite vient souvent de gestes répétés.", "VRAI"),
        ("Il faut appliquer de la glace une heure d'affilée.", "FAUX — vingt minutes"),
        ("La raideur du matin est un des signes.", "VRAI"),
        ("Pour soulever, il vaut mieux plier le dos que les genoux.", "FAUX — les genoux"),
        ("Il faut consulter si la douleur dure plus d'une semaine.", "VRAI"),
        ("S'échauffer avant le quart de travail aide à éviter la tendinite.", "VRAI"),
    ], corrige=True,
       notes="La quatrième est celle qui compte : c'est un geste de sécurité au travail, "
             "pas seulement une réponse d'exercice. Le faire mimer correctement.")

    d.piege("Le piège du « ça va passer »",
            "Ça dure depuis trois semaines, mais ça va finir par passer.",
            "Ça dure depuis plus d'une semaine, je consulte.",
            "Une tendinite non traitée s'installe et devient chronique. La fiche donne "
            "une limite claire — une semaine — précisément pour qu'on n'ait pas à juger "
            "soi-même. Passé cette limite, on consulte, même si la douleur est "
            "supportable.",
            notes="Relier au travail : une douleur ignorée devient un arrêt de travail "
                  "long. C'est un argument qui porte auprès d'un groupe d'adultes.")

    d.pratique('Pratique · 3 de 3', "Répondez avec une phrase complète",
               "Ici, contrairement au formulaire, on rédige.", [
        ("Combien de temps faut-il appliquer la glace, et combien de fois par jour ?",
         "Il faut appliquer de la glace vingt minutes, trois fois par jour."),
        ("Nommez deux façons d'éviter une tendinite au travail.",
         "Il faut plier les genoux pour soulever et alterner les tâches."),
        ("Dans quel cas faut-il consulter un professionnel ?",
         "Il faut consulter si la douleur dure plus d'une semaine ou empêche de marcher."),
        ("Quels sont les trois signes d'une tendinite ?",
         "Une douleur qui élance, de l'enflure et une raideur le matin."),
    ], corrige=True,
       notes="Faire remarquer le contraste avec le premier exercice : même information, "
             "deux formes d'écriture. C'est la compétence de la séance.")

    d.billet(
        "Choisissez un problème de santé courant et écrivez sa fiche-conseil en cinq lignes.",
        exemples=[
            "Une ligne par rubrique : ce que c'est, les signes, pour soulager, pour "
            "éviter, quand consulter.",
            "Exemple de sujet : le mal de dos, le rhume, une brûlure légère.",
        ],
        notes="Les meilleures fiches peuvent être affichées en classe. C'est un exercice "
              "d'écriture fonctionnelle qui donne un résultat utile.")

    return d.save(dossier)
