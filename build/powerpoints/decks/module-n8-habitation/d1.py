# -*- coding: utf-8 -*-
"""D1 · Suivre un exposé, et non une conversation
Bloc D « Défi 3 · Porter la décision plus haut » · couleur acier · 75 min.
Source : dialogue `t3` (le monologue), exercices `t31` et `t3etapes`.

C'est la séance bâtie sur le **monologue long** que le niveau 8 réclame :
quinze répliques d'un seul locuteur, coupées par deux questions. Le programme
l'appelle « suivre le déroulement d'exposés bien structurés », et aucun module
des niveaux inférieurs n'en a. Elle se travaille en **trois écoutes à consigne
différente** : le fait récent, puis les chiffres, puis ce qui est dit deux
fois.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Quinze minutes, un seul homme, quatre temps",
        chapeau="Ce n'est pas une conversation : c'est un exposé, et il "
                "s'écoute autrement. Il annonce son plan, il marque ses "
                "étapes, et il répète à la fin ce qu'il faut retenir.",
        duree='75 minutes')

    d.titre(notes="Séance d'écoute longue, la seule du module et la seule du niveau. "
                  "Prévoir de passer la capsule TROIS fois, avec une consigne "
                  "différente chaque fois. Ne pas la passer une quatrième : la "
                  "quatrième écoute n'apprend plus rien.")

    d.objectifs([
        "noter le plan annoncé par l'orateur, avant qu'il ne commence ;",
        "repérer les marqueurs d'étape d'un exposé ;",
        "relever trois délais sans les confondre ;",
        "entendre ce que l'orateur dit ne pas pouvoir faire.",
    ], notes="Le quatrième objectif est le plus utile : la partie qui délimite évite "
             "d'attendre des mois une chose qui n'arrivera jamais.")

    d.declencheur(
        'Écoute 1 de 3', "Première écoute : combien de temps l'orateur annonce-t-il ?",
        pistes=[
            "En combien de temps dit-il qu'il va procéder ?",
            "Écrivez les quatre titres avant que le premier ne commence.",
            "Ne notez rien d'autre pour l'instant.",
            "Quel est le fait le plus récent qu'il mentionne ?",
        ],
        notes="Première écoute : le plan et rien d'autre. Insister pour que personne "
              "ne prenne de notes détaillées — c'est ce qui fait perdre le fil. Les "
              "quatre titres tiennent en quatre mots.")

    d.regle("Un exposé annonce son plan : notez-le en premier",
            "« Je vais procéder en quatre temps. » Cette phrase-là vaut la "
            "moitié de l'écoute : elle vous donne des tiroirs où ranger la "
            "suite.",
            precision="Les marqueurs d'étape sont vos repères : d'abord · premier "
                      "temps · ensuite · j'en viens à · enfin · je répète donc. Ils "
                      "ne portent aucune information et sont pourtant ce qu'il faut "
                      "entendre : ils disent où vous en êtes.",
            notes="Diapositive à photographier. Faire écrire les marqueurs au tableau "
                  "avant la deuxième écoute : le groupe les entendra passer.")

    d.pratique('Écoute 2 de 3', "Les chiffres, et à quoi ils se rapportent",
               "Deuxième écoute. Notez seulement les nombres et ce qu'ils comptent.", [
        ("Le délai normal d'une réponse finale", "soixante jours de la réception"),
        ("Le délai en circonstances exceptionnelles", "quatre-vingt-dix jours, avec une raison"),
        ("Le délai pour contester une décision du Tribunal administratif du logement",
         "trente jours"),
        ("Le nombre de temps annoncés par l'orateur", "quatre"),
        ("Ce qui doit accompagner un courriel de plainte", "la date d'envoi et une copie"),
    ], corrige=True,
       notes="Trois nombres dans quinze minutes, et deux d'entre eux appartiennent à "
             "deux systèmes différents. C'est la confusion la plus coûteuse du "
             "module : soixante jours pour l'assureur, trente pour le Tribunal.")

    d.cartes('Analyse', "Ce qu'une plainte est, au sens de la loi", [
        ("Trois éléments, pas un de moins",
         "C'est écrit, ça vise l'entreprise, et ça demande une mesure "
         "correctrice précise. Un appel où l'on exprime son mécontentement "
         "n'est pas une plainte."),
        ("Tant que rien n'est écrit, rien n'a commencé",
         "Vos délais ne courent pas, votre dossier n'est pas ouvert, et "
         "personne n'est tenu de vous répondre dans un temps donné. C'est "
         "l'écrit qui déclenche tout."),
        ("Un courriel suffit",
         "Ce qui compte est d'avoir une trace de la date d'envoi et une "
         "copie de ce qu'on a écrit. Gardez les deux, toujours."),
        ("« Réponse finale » ne veut pas dire « définitive pour vous »",
         "C'est la dernière position de l'entreprise. Ce que vous en faites "
         "ensuite ne dépend que de vous."),
    ], notes="La deuxième carte est celle qui change une vie administrative. Beaucoup "
             "d'élèves ont téléphoné pendant des mois en croyant que leur dossier "
             "avançait.")

    d.pratique('Écoute 3 de 3', "Vrai ou faux ?",
               "Troisième écoute : repérez ce qui est dit deux fois, puis répondez.", [
        ("Un appel téléphonique fait courir les délais de traitement.", "faux - seul l'écrit"),
        ("Le délai de quatre-vingt-dix jours n'a pas à être justifié.", "faux - il faut une raison"),
        ("Le transfert se demande après la réponse finale, ou le délai écoulé.", "vrai"),
        ("L'Autorité peut ordonner à l'assureur d'indemniser.", "faux - elle n'est pas un tribunal"),
        ("Une conciliation exige le consentement des deux parties.", "vrai"),
        ("Un différend avec un locataire relève du Tribunal administratif du logement.", "vrai"),
    ], corrige=True,
       notes="Faire remarquer que la réponse aux quatre premières est dans le résumé "
             "final de l'orateur : ce qui est dit deux fois est ce qu'il faut "
             "retenir, et c'est un résumé gratuit et vérifié.")

    # `capture` n'existe que dans theme.Deck : les présentations la portent,
    # les fiches imprimées non (build/powerpoints/fiche.py n'a pas la
    # méthode). Une fiche noir et blanc n'a de toute façon rien à faire
    # d'une capture d'écran.
    if hasattr(d, 'capture'):
        d.capture('t3etapes', "L'exercice tel que les élèves le verront",
                  consigne="Chaque porte, et ce qu'on y obtient.",
                  notes="Ouvrir le module après la troisième écoute, pas avant : "
                        "l'exercice sert de vérification, il ne remplace pas l'écoute.")

    d.regle("Ne confondez pas les portes",
            "Un différend avec votre assureur relève de l'Autorité des "
            "marchés financiers. Un différend avec votre locataire ou votre "
            "propriétaire relève du Tribunal administratif du logement.",
            precision="Deux systèmes distincts, deux séries de délais. Frapper à la "
                      "mauvaise porte fait perdre des semaines, et parfois un droit. "
                      "C'est l'erreur la plus coûteuse de tout le module.",
            notes="Diapositive à photographier. Teodora est propriétaire ET "
                  "propriétaire-bailleresse : c'est exactement le genre de situation "
                  "où l'on se trompe de porte.")

    d.billet(
        "Écrivez les quatre portes du recours, dans l'ordre, et ce qu'on obtient à chacune.",
        exemples=[
            "Une ligne par porte.",
            "À côté de chaque porte, le document qu'on en rapporte.",
        ],
        notes="Le tableau se refait de mémoire à la fin de la séance. Ceux qui "
                "inversent les deux dernières ont encore le temps : on y revient en "
                "D2 et en E2.")

    return d.save(dossier)
