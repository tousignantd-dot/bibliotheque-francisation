# -*- coding: utf-8 -*-
"""D1 · Ce qu'il y a dans l'enveloppe
Bloc D « Défi 3 · Ce qui s'écrit après » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3feuillet` et `t3compte`, trois mots de FC_CARDS.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Ce qu'il y a dans l'enveloppe",
        chapeau="Trois feuilles, trois usages. La première explique comment "
                "ça marche ici, la deuxième est une lettre d'une médecin à "
                "une autre, et vous n'en êtes que la copie.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 3. Le module n'a que deux séances pour ce défi : "
                  "celle-ci porte les deux textes, la suivante porte la langue. Ne "
                  "pas déborder sur la grammaire aujourd'hui.")

    d.objectifs([
        "distinguer les trois papiers d'une enveloppe de sortie ;",
        "trouver dans un feuillet ce qu'on demande d'apporter et qui appeler ;",
        "repérer les sept parties d'un compte rendu de consultation ;",
        "trouver le paragraphe qui vous demande quelque chose.",
    ], notes="Le quatrième objectif est le seul qui compte vraiment hors de la "
             "classe. Le dire au groupe : sur une page entière, un seul paragraphe "
             "attend quelque chose de vous.")

    d.declencheur(
        'Observation', "Qu'est-ce que vous faites d'un papier reçu d'un bureau ?",
        pistes=[
            "Vous le lisez tout de suite, ou plus tard ?",
            "Où le rangez-vous ?",
            "Est-ce que vous écrivez dessus ?",
            "Est-ce qu'il vous est déjà arrivé de ne pas le relire du tout ?",
        ],
        notes="Cinq minutes. La réponse la plus fréquente est « je le range ». C'est "
              "précisément ce que la séance vient corriger : un papier bien rangé est "
              "un papier introuvable.")

    d.dialogue('Dialogue · 1 de 3', "Trois papiers, trois usages", [
        ("PIERRE-LUC", "Pierre-Luc Nadeau, infirmier de liaison. Mariette m'a dit que vous aviez des questions.", True),
        ("LEYLA", "J'ai trois feuilles et je n'en comprends qu'une.", True),
        ("PIERRE-LUC", "C'est déjà une de plus que la moyenne. Le feuillet bleu, le compte rendu, et la demande de prélèvements.", True),
        ("PIERRE-LUC", "Le bleu, gardez-le sur le frigidaire. Il ne parle pas de vous : il explique comment ça marche ici.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Insister sur « il ne parle pas de vous ». C'est ce qui distingue un "
             "feuillet d'un compte rendu, et c'est la distinction que les élèves "
             "manquent le plus souvent.")

    d.dialogue('Dialogue · 2 de 3', "Elle n'a rien ajouté : elle a traduit", [
        ("LEYLA", "Ici, elle écrit « fatigue persistante d'apparition progressive ». Moi, je lui ai dit que j'étais fatiguée depuis février.", True),
        ("PIERRE-LUC", "C'est la même chose, dite dans l'autre langue. Elle n'a rien ajouté : elle a traduit.", True),
        ("LEYLA", "Et « anémie légère, étiologie à préciser » ?", True),
        ("PIERRE-LUC", "L'étiologie, c'est la cause. À préciser, ça veut dire qu'on la cherche encore.", True),
    ], notes="Écrire les deux formules au tableau. Elles seront reprises en D2, où "
             "les élèves les traduiront dans les deux sens.")

    d.dialogue('Dialogue · 3 de 3', "Écrivez votre nom à côté des tirets", [
        ("LEYLA", "Il y a un paragraphe avec des tirets, en bas.", True),
        ("PIERRE-LUC", "C'est le plan. Si vous ne lisez qu'une partie de la lettre, lisez celle-là.", True),
        ("PIERRE-LUC", "Écrivez votre nom au crayon à côté des tirets qui sont à vous, tout de suite, pendant que c'est frais.", True),
        ("LEYLA", "Je peux écrire sur un papier officiel ?", True),
    ], notes="Faire deviner la réponse au groupe avant de la donner. La plupart "
             "répondront non. C'est votre copie, et un papier qu'on n'annote jamais "
             "est un papier qu'on ne relit jamais.")

    d.tableau('Analyse', "Trois papiers, trois usages",
              ['Le papier', 'Ce qu\'il fait'],
              [["Le feuillet", "explique comment ça marche ici, jamais votre cas"],
               ["Le compte rendu", "une lettre d'une médecin à une autre, dont vous avez la copie"],
               ["La demande d'examens", "ce que vous apportez au laboratoire"]],
              cle=0,
              note="Le feuillet se garde des années ; le compte rendu se lit une fois et se classe.",
              notes="Diapositive à photographier. C'est le tableau de référence du "
                    "défi. Faire nommer par le groupe lequel des trois se garde à la "
                    "vue.")

    d.tableau('Analyse', "Sur un feuillet, trois endroits à trouver",
              ['L\'endroit', 'Ce qu\'on y cherche'],
              [["Avant", "ce qu'il faut apporter et préparer, la veille"],
               ["Après", "ce qu'on vous remet, et ce que vous en faites"],
               ["Le numéro", "qui appeler, et à quelles heures"]],
              cle=0,
              note="Le reste est là pour rassurer. Ce n'est pas inutile, mais ça ne vous demande rien.",
              notes="Diapositive à photographier. Faire chronométrer : le groupe doit "
                    "trouver les trois endroits en moins de trente secondes sur le "
                    "texte de l'exercice.")

    d.tableau('Analyse', "Un compte rendu, toujours le même ordre",
              ['La partie', 'Ce qu\'elle contient'],
              [["L'en-tête", "d'où vient la lettre, la date, à qui elle est adressée"],
               ["Le motif", "qui est vu, et pourquoi"],
               ["Ce qui est rapporté", "vos mots à vous, traduits"],
               ["La conduite proposée", "le plan, souvent à tirets"],
               ["Ce qui reste à décider", "ce qu'on ne sait pas encore"]],
              cle=0,
              note="Une seule de ces cinq parties vous demande quelque chose : la conduite proposée.",
              notes="Diapositive à photographier. Compter les tirets du paragraphe de "
                    "la conduite proposée avec le groupe : trois tirets, trois choses "
                    "attendues.")

    d.vocabulaire('Vocabulaire', "Les trois mots de l'écrit qui reste", [
        ("un feuillet d'information", "La feuille remise en sortant, qui explique la marche à suivre."),
        ("les effets secondaires", "Ce qu'un traitement fait en plus de ce qu'on lui demande."),
        ("un suivi", "Ce qui est prévu après : qui rappelle, quand, et ce qu'il faut avoir fait."),
    ], notes="« Un suivi » est le mot du module qu'on emploiera le plus longtemps. "
             "Faire produire la phrase : « Est-ce qu'il y a un suivi de prévu ? »")

    d.pratique('Lecture', "Où trouve-t-on la réponse ?",
               "Dites dans quel papier et dans quelle partie.", [
        ("Ce qu'il faut apporter la prochaine fois.", "le feuillet, partie « avant »"),
        ("Le numéro de téléphone de la liaison.", "le feuillet, l'encadré du bas"),
        ("Depuis quand la fatigue est apparue.", "le compte rendu, le motif"),
        ("Ce que la patiente a raconté.", "le compte rendu, « la patiente rapporte »"),
        ("Les trois choses à faire d'ici janvier.", "le compte rendu, la conduite proposée"),
        ("Ce qu'on ne sait pas encore.", "le compte rendu, la dernière ligne"),
    ], corrige=True,
       notes="Faire chercher dans le texte projeté avant de corriger. Le but n'est "
             "pas la bonne réponse : c'est de voir que chaque question a un endroit, "
             "et un seul.")

    d.billet(
        "Quel mot d'un papier officiel n'avez-vous jamais osé faire traduire ?",
        exemples=[
            "Un mot, écrit comme vous l'avez vu.",
            "On le traduira ensemble à la prochaine séance.",
        ],
        notes="Deux minutes. Les billets ouvrent directement D2. Traduire ces mots-là "
              "fait partie du travail de quelqu'un, quelque part : le redire en "
              "ramassant les feuilles.")

    return d.save(dossier)
