# -*- coding: utf-8 -*-
"""D2 · Signaler un bris d'équipement.
Bloc D · couleur teal (lire et répondre) · 60 min.
Source : exercice `t3bris` — la directive de signalement.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='teal',
        titre="Signaler un bris d'équipement",
        chapeau="Quatre gestes et une interdiction. C'est la directive la plus courte du "
                "module, et la seule dont le non-respect peut blesser quelqu'un.",
        duree='60 minutes')

    d.titre(notes="Séance de lecture de consigne de sécurité. Le ton compte : ce n'est "
                  "plus une question de remboursement, mais d'intégrité physique.")

    d.objectifs([
        "connaître les quatre gestes du signalement, dans l'ordre ;",
        "comprendre pourquoi on ne répare pas soi-même ;",
        "expliquer le mot « signaler » dans ses propres mots ;",
        "trouver un synonyme de « bris ».",
    ])

    d.regle('La directive, en une phrase',
            "Arrêtez · photographiez · avertissez · remplissez. Et ne réparez jamais.",
            precision="Quatre gestes dans cet ordre, puis une interdiction absolue. "
                      "L'ordre compte : photographier avant d'arrêter la machine serait "
                      "dangereux, et avertir avant de photographier fait perdre la "
                      "preuve.",
            notes="Écrire les quatre verbes à l'impératif au tableau. C'est exactement "
                  "la forme travaillée en C4.")

    d.tableau('Analyse', "Les quatre gestes et leur raison",
              ['Le geste', 'Pourquoi'],
              [["arrêter la machine", "éviter que le bris s'aggrave ou blesse"],
               ["prendre une photo", "garder la preuve de l'état au moment du bris"],
               ["avertir le superviseur", "il décide de la suite et prévient la maintenance"],
               ["remplir le formulaire", "le signalement devient officiel et daté"]],
              cle=0, props=[0.35, 0.65],
              notes="Faire remarquer que chaque geste a une raison différente. Ce n'est "
                    "pas une liste arbitraire.")

    d.cartes('Analyse', "Pourquoi ne jamais réparer soi-même", [
        ("La sécurité",
         "Un équipement mal remis en marche peut blesser la personne suivante. Vous ne "
         "serez peut-être pas là quand cela arrivera."),
        ("La garantie",
         "Une réparation faite par un employé annule souvent la garantie du fabricant. "
         "L'entreprise paie alors le remplacement complet."),
        ("La responsabilité",
         "Si un accident survient après une réparation non autorisée, la responsabilité "
         "peut retomber sur la personne qui a réparé."),
        ("Ce qu'on peut faire",
         "Signaler vite et précisément. Une bonne photo et une description exacte "
         "accélèrent la vraie réparation."),
    ], notes="Ces quatre raisons répondent à l'objection la plus fréquente : « mais je "
             "sais réparer ça ». Les donner toutes les quatre.")

    d.pratique('Pratique · 1 de 4', "La directive, cinq questions",
               "Répondez d'après le texte.", [
        ("Que faut-il faire en premier si une machine se brise ?", "l'arrêter immédiatement"),
        ("Qu'est-ce qu'il faut faire avant d'avertir le superviseur ?",
         "prendre une photo du bris"),
        ("Est-ce qu'on peut réparer l'équipement soi-même ?", "non, jamais"),
        ("Où doit-on remplir le formulaire de signalement ?", "dans l'application"),
        ("Qui décide de la suite ?", "le superviseur"),
    ], corrige=True,
       notes="La deuxième question porte sur l'ordre, pas sur le contenu. C'est la plus "
             "difficile, et la plus utile.")

    d.pratique('Pratique · 2 de 4', "Expliquez le mot",
               "Dans vos propres mots, sans employer le mot lui-même.", [
        ("signaler", "faire savoir, informer quelqu'un d'un problème"),
        ("un bris", "un équipement qui casse ou cesse de fonctionner"),
        ("un synonyme de « bris »", "une panne, un dommage, un bris de service"),
        ("un formulaire de signalement", "le document où on déclare officiellement un bris"),
    ], corrige=True,
       notes="Expliquer un mot sans l'employer est un exercice de reformulation. C'est "
             "aussi ce qu'on fait quand on cherche un mot qui manque.")

    d.pratique('Pratique · 3 de 4', "Écrivez la directive à l'impératif",
               "Deuxième personne du pluriel. Une consigne par ligne.", [
        ("arrêter la machine", "Arrêtez immédiatement la machine."),
        ("prendre une photo", "Prenez une photo du bris."),
        ("avertir le superviseur", "Avertissez votre superviseur."),
        ("remplir le formulaire", "Remplissez le formulaire de signalement."),
        ("ne pas réparer soi-même", "Ne tentez jamais de réparer l'équipement vous-même."),
    ], corrige=True,
       notes="C'est exactement l'exercice de C4, appliqué à une vraie directive. Le "
             "signaler : le savoir de grammaire devient un document de travail.")

    d.piege("Le piège de la photo prise trop tard",
            "J'arrête la machine, j'avertis, puis je prends une photo.",
            "J'arrête la machine, je prends la photo, puis j'avertis.",
            "Entre le moment où on avertit et celui où on revient, quelqu'un peut avoir "
            "déplacé la pièce, nettoyé, ou tenté quelque chose. La photo prise tout de "
            "suite montre l'état réel au moment du bris — et c'est elle qui compte.",
            notes="L'ordre d'une directive n'est presque jamais arbitraire. Faire "
                  "chercher, pour chacun des quatre gestes, ce qui se passerait s'il "
                  "était fait plus tard.")

    d.piege("Le piège du bris « pas grave »",
            "Ce n'est qu'un petit bruit, je le signalerai demain.",
            "Je signale tout de suite, même un petit bruit.",
            "Un bris mineur signalé le jour même se répare en une heure. Le même bris "
            "ignoré trois jours immobilise la machine une semaine. Signaler ne coûte "
            "que deux minutes et ne met personne en cause.",
            notes="Insister : signaler n'est pas dénoncer. Beaucoup d'élèves hésitent par "
                  "crainte d'être tenus responsables du bris.")

    d.pratique('Pratique · 4 de 4', "Écrivez le signalement",
               "Quatre phrases, une par élément.", [
        ("La situation",
         "Un chariot élévateur fait un bruit anormal et s'arrête par moments."),
        ("Ce que vous avez fait", "les quatre gestes de la directive, dans l'ordre"),
        ("Ce que vous joignez", "une photo, et l'heure du bris"),
        ("Ce que vous demandez", "une vérification avant la reprise du travail"),
    ], corrige=False,
       notes="Vingt minutes. Ramasser : ces signalements montrent si la directive est "
             "vraiment comprise, ordre compris.")

    d.billet(
        "Écrivez les quatre gestes du signalement, à l'impératif, plus l'interdiction.",
        exemples=[
            "Une ligne par geste, dans l'ordre.",
            "Ajoutez, pour chacun, la raison en trois mots.",
        ],
        notes="Ce billet peut être affiché en classe. C'est une vraie fiche de sécurité, "
              "écrite par les élèves.")

    return d.save(dossier)
