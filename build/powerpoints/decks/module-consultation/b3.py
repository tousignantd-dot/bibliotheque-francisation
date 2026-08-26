# -*- coding: utf-8 -*-
"""B3 · Poser une question.
Bloc B · couleur ambre (écriture) · 75 min.
Source : exercice `t1quest` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre='Poser une question',
        chapeau="L'infirmière pose sept questions à Yannick, et il n'en pose aucune. "
                "Pourtant c'est le patient qui repart avec ses doutes. Trois "
                "constructions suffisent pour les poser toutes.",
        duree='75 minutes')

    d.titre(notes="Ouvrir en demandant au groupe : quelle question auriez-vous posée à "
                  "l'infirmière ? Noter les questions au tableau, même mal formées. On "
                  "les corrigera ensemble à la fin.")

    d.objectifs([
        "poser une question avec « est-ce que » ;",
        "poser une question avec un mot interrogatif : où, quand, combien, comment ;",
        "reconnaître l'inversion, que les professionnels emploient ;",
        "choisir la construction selon la personne à qui on parle.",
    ])

    d.tableau('Analyse', "Trois façons de poser une question",
              ['La construction', 'Un exemple', 'Quand'],
              [["Est-ce que", "Est-ce que vous avez mal ?", "toujours, à l'oral"],
               ["Mot interrogatif", "Où est la douleur ?", "pour un détail précis"],
               ["Inversion", "Avez-vous de la fièvre ?", "poli, plutôt à l'écrit"]],
              cle=0,
              note="Les trois sont correctes. La première fonctionne partout : c'est "
                   "celle à maîtriser d'abord.",
              notes="Insister : personne n'a besoin des trois pour se faire comprendre. "
                    "Mais il faut comprendre les trois, parce que le personnel les "
                    "utilise toutes.")

    d.regle('La construction la plus sûre',
            "Est-ce que + une phrase normale, sans rien changer d'autre.",
            precision="« Vous avez mal » devient « Est-ce que vous avez mal ? ». Le sujet reste devant "
                      "le verbe, l'ordre des mots ne bouge pas. C'est la seule "
                      "construction qui ne demande aucune transformation.",
            notes="Faire fabriquer cinq questions par le groupe à partir de cinq phrases "
                  "affirmatives, en ajoutant simplement « est-ce que ».")

    d.tableau('Analyse', "Les mots interrogatifs utiles en consultation",
              ['Le mot', 'Il cherche', 'Exemple'],
              [["où", "un lieu", "Où est la douleur ?"],
               ["depuis quand", "un moment de départ", "Depuis quand avez-vous mal ?"],
               ["combien de temps", "une durée", "Combien de temps dure la douleur ?"],
               ["comment", "une manière", "Comment se comporte la douleur ?"],
               ["pourquoi", "une cause", "Pourquoi faut-il de la glace ?"]],
              cle=0,
              notes="Ces cinq mots couvrent presque toutes les questions d'un patient. "
                    "Les faire copier dans le cahier avec un exemple chacun.")

    d.regle("La règle de place",
            "Le mot interrogatif se met au début, jamais à la fin.",
            precision="« Où avez-vous mal ? » et non « Vous avez mal où ? ». La seconde "
                      "s'entend entre amis, mais devant un professionnel de la santé, le "
                      "mot interrogatif ouvre la question.",
            notes="Faire corriger oralement cinq questions mal placées. C'est une erreur "
                  "d'ordre, pas de vocabulaire : elle se corrige vite.")

    d.cartes('Ouvrir la mini-leçon', "Ce qu'il faut savoir en plus", [
        ("L'inversion : à comprendre, pas à produire",
         "« Avez-vous mal ? » — le sujet passe après le verbe, avec un trait d'union. "
         "Le personnel l'emploie souvent. Vous n'êtes pas obligé de l'employer."),
        ("La question par le ton",
         "« Vous avez mal ? » avec la voix qui monte à la fin. Correct entre proches ; "
         "à éviter avec un professionnel, qui l'entendra comme familier."),
        ("Répondre à une question fermée",
         "Une question en « est-ce que » attend oui ou non. Mais ajoutez toujours une "
         "précision : « Non, mais j'ai eu froid toute la nuit »."),
        ("Poser sa question à la fin",
         "Le meilleur moment pour poser ses questions est juste avant de sortir, quand "
         "le médecin demande « avez-vous des questions ? ». Préparez-les d'avance."),
    ], notes="La quatrième carte est un conseil pratique : faire écrire ses questions "
             "avant le rendez-vous, sur papier ou dans le téléphone.")

    d.pratique('Pratique · 1 de 3', 'Écrivez la question',
               "La réponse est donnée. Quelle question a été posée ?", [
        ("« J'ai mal depuis cette nuit. »", "Depuis quand avez-vous mal ?"),
        ("« La douleur est au genou droit. »", "Où est la douleur ?"),
        ("« Non, je n'ai pas de fièvre. »", "Est-ce que vous avez de la fièvre ?"),
        ("« Environ six sur dix. »", "Sur une échelle de un à dix, où se situe la douleur ?"),
        ("« Trois fois par jour, vingt minutes. »", "Combien de fois faut-il mettre de la glace ?"),
    ], corrige=True,
       notes="Accepter toute question correcte qui appelle cette réponse. Faire remarquer "
             "que les réponses en oui/non appellent « est-ce que », les autres un mot "
             "interrogatif.")

    d.pratique('Pratique · 2 de 3', "Transformez en question avec « est-ce que »",
               "N'ajoutez rien d'autre, ne changez pas l'ordre des mots.", [
        ("Vous avez de la fièvre.", "Est-ce que vous avez de la fièvre ?"),
        ("Je peux retourner travailler demain.", "Est-ce que je peux retourner travailler demain ?"),
        ("La clinique ouvre à sept heures.", "Est-ce que la clinique ouvre à sept heures ?"),
        ("Il faut apporter la carte d'assurance maladie.",
         "Est-ce qu'il faut apporter la carte d'assurance maladie ?"),
    ], corrige=True,
       notes="La quatrième introduit « est-ce qu' » devant une voyelle. Le signaler sans "
             "en faire une règle nouvelle : c'est la même élision que « je n'ai pas ».")

    d.piege('Le piège du mélange',
            "Est-ce que avez-vous mal ?",
            "Est-ce que vous avez mal ? OU Avez-vous mal ?",
            "On ne combine jamais les deux constructions. « Est-ce que » exige l'ordre "
            "normal — sujet puis verbe. L'inversion se fait seule. Choisir l'une des "
            "deux, jamais les deux ensemble.",
            notes="Erreur très fréquente chez les élèves qui viennent d'apprendre "
                  "l'inversion. La montrer, puis passer vite : c'est une erreur qui "
                  "disparaît d'elle-même une fois vue.")

    d.pratique('Pratique · 3 de 3', "Cinq questions à poser au médecin",
               "Écrivez chaque question. Utilisez la construction de votre choix.", [
        ("Vous voulez savoir si vous pouvez travailler.",
         "Est-ce que je peux retourner travailler ?"),
        ("Vous voulez savoir combien de temps ça va durer.",
         "Combien de temps est-ce que ça va durer ?"),
        ("Vous voulez savoir quand revenir.",
         "Quand est-ce que je dois revenir vous voir ?"),
        ("Vous voulez savoir si le médicament se prend avec de la nourriture.",
         "Est-ce que je dois prendre le médicament avec de la nourriture ?"),
        ("Vous voulez savoir ce qu'il faut éviter de faire.",
         "Qu'est-ce que je dois éviter de faire ?"),
    ], corrige=True,
       notes="Ces cinq questions sont celles qu'un patient devrait toujours poser. Les "
             "faire copier dans le cahier : elles servent en E1 et hors du cours.")

    d.billet(
        "Écrivez trois questions que vous poseriez à un médecin.",
        exemples=[
            "Une avec « est-ce que », une avec un mot interrogatif, une au choix.",
            "Elles doivent porter sur une vraie situation, la vôtre ou une inventée.",
        ],
        notes="Relire les questions notées au tableau en début de séance et les corriger "
              "avec le groupe : c'est la meilleure fin possible pour cette séance.")

    return d.save(dossier)
