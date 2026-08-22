# -*- coding: utf-8 -*-
"""D1 · Vingt-deux personnes à la cafétéria
Bloc D « Défi 3 · Le compte rendu » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3parties`, mini-leçon
`t3parties`. Intention du programme : lire un compte rendu.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Vingt-deux personnes à la cafétéria",
        chapeau="Quarante minutes de rencontre, et deux pages le vendredi. "
                "Un compte rendu ne raconte pas : il rapporte, et il est "
                "fait pour ceux qui n'étaient pas là.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 3. Le bloc n'a que deux séances : celle-ci porte "
                  "l'écoute et la structure, D2 porte la langue. Ne pas déborder.")

    d.objectifs([
        "suivre une rencontre d'information à plusieurs voix ;",
        "reconnaître les six parties d'un compte rendu ;",
        "aller droit aux décisions quand on manque de temps ;",
        "employer les trois mots de la rencontre.",
    ], notes="Le troisième objectif est un geste de lecteur pressé, et c'est celui qui "
             "servira le plus : la plupart des gens ne lisent qu'un compte rendu sur "
             "trois, et seulement ses décisions.")

    d.declencheur(
        'Observation', "Es-tu déjà arrivé après une réunion importante ?",
        pistes=[
            "Comment as-tu su ce qui s'y était dit ?",
            "Par un papier, par un collègue, ou pas du tout ?",
            "Qu'est-ce qui manque quand on l'apprend de bouche à oreille ?",
        ],
        notes="Le quart de soir n'assiste presque jamais aux rencontres. C'est le vrai "
              "public d'un compte rendu, et beaucoup d'élèves travaillent le soir : la "
              "question les touche directement.")

    d.dialogue('Dialogue · 1 de 3', "L'ouverture et l'ordre du jour", [
        ("PATRICE", "Il est deux heures et demie, on commence. Nous sommes vingt-deux.", True),
        ("PATRICE", "Trois points à l'ordre du jour : le poste affiché, la démarche pour se présenter, et vos questions.", True),
        ("PATRICE", "Marie-Soleil prend des notes ; il y aura un compte rendu au babillard vendredi.", True),
        ("MARIE-SOLEIL", "Et il sera aussi dans le réseau interne, pour ceux du quart de soir qui ne sont pas là.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Faire relever les quatre éléments de l'en-tête : l'heure, le nombre de "
             "personnes, l'ordre du jour, le suivi annoncé. Tout est dit dans les "
             "quarante premières secondes.")

    d.dialogue('Dialogue · 2 de 3', "Une question, une réponse", [
        ("YANETH", "Si deux personnes se présentent et qu'elles ont les mêmes compétences, qu'est-ce qui décide ?", True),
        ("MARIE-SOLEIL", "L'ancienneté, à ce moment-là seulement. Mais je veux être claire : c'est un départage, ce n'est pas le critère.", True),
        ("GHISLAIN", "Une question de mon monde à l'expédition : est-ce qu'on perd son ancienneté en changeant de poste ?", True),
        ("MARIE-SOLEIL", "Non. L'ancienneté est celle de l'entreprise, pas celle du poste. Vous la gardez au complet.", True),
    ], notes="Ces deux échanges deviendront deux lignes du compte rendu. Le dire tout "
             "de suite : c'est ce que la séance va faire faire.")

    d.dialogue('Dialogue · 3 de 3', "Le taux, et se présenter deux fois", [
        ("YANETH", "Et pendant la période d'essai, on est payé à quel taux ?", True),
        ("PATRICE", "Au taux du nouveau poste, dès le premier jour. Un dollar quarante de plus l'heure.", True),
        ("YANETH", "Si je me présente et que je ne l'ai pas, est-ce que ça me nuit la prochaine fois ?", True),
        ("PATRICE", "Au contraire. Les trois derniers vérificateurs s'étaient tous présentés une fois avant.", True),
    ], notes="La dernière réplique porte un plus-que-parfait — « s'étaient présentés » "
             "— et une hypothèse en « si ». Les deux se travaillent en D2 : les "
             "signaler sans les expliquer maintenant.")

    d.tableau('Analyse', "Les six parties d'un compte rendu",
              ['La partie', 'Ce qu\'on y trouve'],
              [["L'en-tête", "la date, l'heure, le lieu, le nombre de présents"],
               ["L'ordre du jour", "les sujets annoncés, numérotés"],
               ["Les points", "ce qui a été dit sur chacun"],
               ["Les questions", "ce qui a été demandé, et la réponse donnée"],
               ["Les décisions", "ce qui est acquis — la partie la plus lue"],
               ["Le suivi", "qui fait quoi, et pour quand"]],
              cle=0,
              notes="Diapositive à photographier. Six rangées sans note : c'est le "
                    "tableau de tout le bloc D. Faire dire au groupe laquelle des six "
                    "il lirait s'il n'avait que deux minutes.")

    d.regle("Il ne dit jamais « je »",
            "Celui qui écrit disparaît — et ce n'est pas de la modestie.",
            precision="On n'écrit pas « j'ai demandé si l'ancienneté comptait » mais "
                      "« une question est posée sur l'ancienneté ». Le compte rendu "
                      "doit valoir pour tous ceux qui le liront, y compris ceux qui "
                      "arriveront dans six mois. Le passif est chez lui ici : il "
                      "rapporte sans mettre personne en cause.",
            notes="Diapositive à photographier. Rappeler C3 : c'est la même langue que "
                  "la politique, pour la même raison. Le groupe l'a déjà rencontrée.")

    d.vocabulaire('Vocabulaire', "Trois mots de la rencontre", [
        ("un compte rendu", "Le texte qui rapporte ce qui s'est dit et ce qui a été décidé."),
        ("un ordre du jour", "La liste des sujets qu'une rencontre va traiter, dans l'ordre."),
        ("les qualifications", "Les diplômes, les formations et les habiletés qu'on peut prouver."),
    ], notes="Distinguer « qualifications » et « qualités » : les premières se "
             "prouvent, les secondes se racontent. C'est la nuance qui sert en "
             "entrevue.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la rencontre du mercredi.", [
        ("Vingt-deux personnes assistaient à la rencontre.", "vrai"),
        ("L'ordre du jour comptait trois points.", "vrai"),
        ("Une personne mutée perd l'ancienneté qu'elle avait.", "faux - elle la garde au complet"),
        ("Pendant l'essai, on est payé au taux de l'ancien poste.", "faux - au nouveau taux dès le premier jour"),
        ("Si personne à l'interne ne convient, le poste sort à l'externe.", "vrai"),
        ("Se présenter sans être choisi nuit à la candidature suivante.", "faux - au contraire"),
    ], corrige=True,
       notes="Le dernier item est le plus important du module : il décide qui osera "
             "une deuxième fois. Faire relire la réplique de Patrice mot pour mot.")

    d.billet(
        "Écris en une ligne la décision la plus utile de la rencontre.",
        exemples=[
            "Commence par le mot « Décision : ».",
            "Une seule phrase, sans « je ».",
        ],
        notes="Trois minutes. C'est l'entrée dans D2 : nommer au lieu de raconter. "
              "Relire deux ou trois billets à voix haute pour montrer la forme.")

    return d.save(dossier)
