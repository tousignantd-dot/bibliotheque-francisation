# -*- coding: utf-8 -*-
"""B4 · Décrire sa douleur à voix haute.
Bloc B · couleur teal (écoute et réponds) · 60 min.
Source : dialogue `t1`, vocabulaire de la douleur (A3), production orale du défi 1.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='teal',
        titre='Décrire sa douleur à voix haute',
        chapeau="Tout ce qui a été écrit depuis A1 doit maintenant sortir de la bouche, "
                "en trente secondes, devant quelqu'un qui attend. C'est la séance où le "
                "module devient utile.",
        duree='60 minutes')

    d.titre(notes="Séance de production orale. Prévoir la disposition en dyades dès le "
                  "début : deux chaises face à face, une personne joue l'infirmière.")

    d.objectifs([
        "dire son problème en une phrase complète, sans préparation écrite ;",
        "répondre aux quatre questions du triage sans hésiter ;",
        "demander de répéter quand on n'a pas compris ;",
        "tenir trente secondes de parole utile.",
    ])

    d.regle('La phrase de trente secondes',
            "L'endroit avec le côté · depuis quand · ce qui aggrave · le chiffre sur dix.",
            precision="Quatre informations, dans cet ordre. C'est ce que Yannick dit au "
                      "triage, et c'est ce que tout patient devrait pouvoir dire. Rien "
                      "de plus n'est nécessaire au premier contact.",
            notes="Écrire les quatre au tableau, en colonne, et les y laisser toute la "
                  "séance. Les élèves y jetteront un œil pendant les jeux de rôle.")

    d.cartes('Le modèle', "La phrase de Yannick, découpée", [
        ("L'endroit et le côté",
         "« J'ai le genou droit… » — Jamais « la jambe » : le mot précis existe et il "
         "évite un examen inutile."),
        ("L'état et le moment",
         "« …enflé depuis cette nuit. » — Un mot d'état (enflé, raide, bloqué) et un "
         "point de départ dans le temps."),
        ("Ce qui aggrave",
         "« Ça élance dès que je plie la jambe. » — Le geste qui déclenche vaut plus "
         "qu'une longue description."),
        ("Le chiffre",
         "« Six quand je marche, deux quand je reste assis. » — Deux chiffres, pour le "
         "mouvement et le repos."),
    ], notes="Faire lire les quatre cartes à voix haute, une par élève, dans l'ordre. "
             "Puis les faire dire d'un seul trait par un seul élève : c'est le modèle.")

    d.tableau('Analyse', "Les mots d'état les plus utiles",
              ['Le mot', 'Ce qu\'il décrit'],
              [["enflé", "le volume a augmenté"],
               ["raide", "ça ne plie plus comme avant"],
               ["bloqué", "ça ne bouge plus du tout"],
               ["engourdi", "on ne sent presque plus"],
               ["chaud", "la peau est plus chaude qu'ailleurs"]],
              cle=0,
              note="Un seul de ces mots remplace trois phrases d'explication.",
              notes="Faire montrer sur soi ce que chacun veut dire. « Engourdi » est le "
                    "plus difficile : le faire mimer.")

    d.cartes('Quand on ne comprend pas', "Quatre phrases à savoir par cœur", [
        ("Demander de répéter",
         "« Pardon, est-ce que vous pouvez répéter, s'il vous plaît ? » — Toujours "
         "correct, jamais impoli."),
        ("Demander plus lentement",
         "« Est-ce que vous pouvez parler plus lentement ? » — Personne ne le prend "
         "mal, et tout le monde ralentit."),
        ("Demander le sens d'un mot",
         "« Qu'est-ce que ça veut dire, une ordonnance ? » — Nommer le mot exact qu'on "
         "n'a pas compris fait gagner du temps."),
        ("Vérifier qu'on a compris",
         "« Donc je dois revenir dans une semaine, c'est bien ça ? » — Reformuler ce "
         "qu'on a compris est la meilleure vérification."),
    ], notes="Ces quatre phrases valent plus que tout le vocabulaire médical du module. "
             "Les faire répéter en chœur, puis individuellement.")

    d.pratique('Pratique · 1 de 3', 'Construisez la phrase',
               "Assemblez les quatre informations en une seule phrase orale.", [
        ("Cheville droite · enflée · depuis hier soir · mal quand on marche",
         "J'ai la cheville droite enflée depuis hier soir, ça fait mal quand je marche."),
        ("Bas du dos · bloqué · depuis trois jours · mal quand on se penche",
         "J'ai le bas du dos bloqué depuis trois jours, ça élance quand je me penche."),
        ("Épaule gauche · raide · depuis une semaine · mal quand on lève le bras",
         "J'ai l'épaule gauche raide depuis une semaine, ça tire quand je lève le bras."),
        ("Poignet droit · engourdi · depuis ce matin · mal quand on tape au clavier",
         "J'ai le poignet droit engourdi depuis ce matin, ça pique quand je tape."),
    ], corrige=True,
       notes="Faire dire chaque phrase debout, à voix haute, sans lire. La lecture "
             "silencieuse ne prépare pas au triage.")

    d.pratique('Pratique · 2 de 3', "Jeu de rôle · au triage",
               "À deux. L'un pose les quatre questions, l'autre répond. Puis on échange.", [
        ("Question 1", "Qu'est-ce qui vous amène aujourd'hui ?"),
        ("Question 2", "Est-ce que vous vous êtes cogné ou tordu quelque chose ?"),
        ("Question 3", "Depuis quand avez-vous mal ?"),
        ("Question 4", "Sur une échelle de un à dix, où se situe votre douleur ?"),
    ], corrige=False,
       notes="Dix minutes par personne. Circuler et n'intervenir que si la personne "
             "bloque plus de cinq secondes. Noter deux erreurs récurrentes pour la "
             "correction collective, pas plus.")

    d.piege("Le piège du silence",
            "…",
            "Pardon, est-ce que vous pouvez répéter ?",
            "Beaucoup d'élèves se taisent quand ils n'ont pas compris, par gêne. Le "
            "silence est interprété comme un accord : l'infirmière passe à la suite et "
            "l'information est perdue. Demander de répéter n'est pas un aveu de "
            "faiblesse, c'est la seule façon d'obtenir la bonne information.",
            notes="Point à traiter sérieusement. Demander qui, dans le groupe, s'est déjà "
                  "tu en consultation. La discussion vaut la leçon.")

    d.pratique('Pratique · 3 de 3', "Jeu de rôle · je ne comprends pas",
               "L'infirmière parle vite et emploie un mot difficile. Réagissez.", [
        ("« Vous avez une tendinite, je vous réfère en physio. »",
         "Qu'est-ce que ça veut dire, une tendinite ?"),
        ("« Prenez ça deux fois par jour, à jeun. »",
         "Pardon, qu'est-ce que ça veut dire, à jeun ?"),
        ("« Revenez si ça ne s'améliore pas d'ici quarante-huit heures. »",
         "Donc je reviens dans deux jours si c'est pareil, c'est bien ça ?"),
        ("« Vous avez besoin d'une ordonnance renouvelée. »",
         "Est-ce que vous pouvez parler plus lentement, s'il vous plaît ?"),
    ], corrige=True,
       notes="Le troisième item est le plus important : reformuler pour vérifier. C'est "
             "l'habitude qui évite le plus d'erreurs, ici comme au travail.")

    d.billet(
        "Enregistrez-vous ou dites à votre voisin votre phrase de trente secondes.",
        exemples=[
            "Les quatre informations : endroit et côté, depuis quand, ce qui aggrave, "
            "le chiffre.",
            "Écrivez ensuite sur le billet celle des quatre que vous avez oubliée.",
        ],
        notes="C'est l'oubli qui est instructif, pas la réussite. Relever quelle "
              "information manque le plus souvent dans le groupe et y revenir en E1.")

    return d.save(dossier)
