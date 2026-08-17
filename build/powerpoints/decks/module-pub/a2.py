# -*- coding: utf-8 -*-
"""A2 · L'accent d'insistance.
Bloc A · couleur violet (graphie-phonie) · 60 min.
Source : exercice `prAccent` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='violet',
        titre="L'accent d'insistance",
        chapeau="« Cet atelier est complètement gratuit. » Un mot est dit plus long et "
                "plus haut que les autres : c'est celui qu'on retiendra. En publicité, "
                "ce choix vaut la moitié du message.",
        duree='60 minutes')

    d.titre(notes="Dire la phrase du chapeau trois fois, en insistant chaque fois sur un "
                  "mot différent. Demander au groupe ce qui change. Tout change.")

    d.objectifs([
        "reconnaître le mot sur lequel on insiste dans une phrase ;",
        "produire un accent d'insistance : syllabe allongée, ton qui monte ;",
        "choisir le mot à mettre en avant dans une annonce ;",
        "employer l'intonation d'une phrase exclamative ;",
        "distinguer le son « ch » du son « j » dans le vocabulaire de la publicité.",
    ])

    d.regle('La règle',
            "On allonge la dernière syllabe du mot et on fait monter le ton.",
            precision="« C'est gra-TUIT. » La syllabe dure plus longtemps et la voix "
                      "monte. Le reste de la phrase reste au même niveau : c'est le "
                      "contraste qui fait entendre l'insistance.",
            notes="Faire produire l'accent sur un seul mot par tout le groupe, en même "
                  "temps. C'est bruyant et cela fonctionne.")

    d.tableau('Analyse', "Le même énoncé, trois insistances",
              ['On insiste sur', 'Ce que ça veut dire'],
              [["gratuit", "ce qui compte, c'est que ça ne coûte rien"],
               ["cet atelier", "celui-là, pas un autre"],
               ["complètement", "il n'y a aucun frais caché"]],
              cle=0,
              note="La phrase ne change pas d'un mot. Seule l'insistance change — et le "
                   "sens avec elle.",
              notes="Faire dire les trois versions par trois élèves différents. Le groupe "
                    "devine à chaque fois sur quel mot on a insisté.")

    d.cartes('Analyse', "Où placer l'insistance dans une annonce", [
        ("Sur le prix, s'il est avantageux",
         "« C'est gratuit. » « C'est cinq dollars. » Si le prix est un argument, c'est "
         "lui qu'on met en avant."),
        ("Sur la date, si elle approche",
         "« C'est samedi. » « C'est la dernière occasion avant l'été. » L'urgence fait "
         "agir."),
        ("Sur le résultat, s'il est concret",
         "« Vous repartirez avec un grille-pain qui fonctionne. » Ce qu'on obtient est "
         "plus fort que ce qu'on propose."),
        ("Un seul mot par annonce",
         "Insister sur trois mots revient à n'insister sur aucun. Omar le dit à "
         "Solange : un seul mot, et c'est « gratuit »."),
    ], notes="La quatrième carte est la règle pratique. C'est ce qu'Omar conseille en "
             "B1 : « insiste sur un seul mot ».")

    d.pratique('Pratique · 1 de 6', "Sur quel mot insiste-t-on ?",
               "Écoutez la phrase, écrivez le mot allongé.", [
        ("Cet atelier est complètement gratuit.", "gratuit"),
        ("Nos bénévoles réparent absolument tout.", "absolument"),
        ("C'est la dernière occasion avant l'été.", "dernière"),
        ("Vous repartirez avec un grille-pain qui fonctionne.", "fonctionne"),
        ("Quelle belle idée de quartier !", "belle"),
    ], corrige=True,
       notes="Dire chaque phrase deux fois, sans montrer le texte. C'est un exercice "
             "d'oreille avant d'être un exercice d'analyse.")

    d.regle("La phrase exclamative",
            "Le ton monte à la fin, sans qu'un mot soit allongé.",
            precision="« Quelle belle idée de quartier ! » L'intonation monte sur toute "
                      "la fin de la phrase. C'est différent de l'accent d'insistance, "
                      "qui porte sur un seul mot.",
            notes="Faire dire la même phrase deux fois : une fois avec l'accent sur "
                  "« belle », une fois en exclamative. La différence s'entend.")

    d.pratique('Pratique · 2 de 6', "Insistance ou exclamation ?",
               "Un mot allongé, ou tout le ton qui monte ?", [
        ("C'est complètement gratuit.", "insistance sur « gratuit »"),
        ("Quelle belle idée !", "exclamation — le ton monte à la fin"),
        ("C'est la dernière occasion.", "insistance sur « dernière »"),
        ("Comme c'est bien organisé !", "exclamation"),
        ("Nos bénévoles réparent tout.", "insistance sur « tout »"),
    ], corrige=True,
       notes="Faire produire chaque phrase avant de la classer. C'est en la disant qu'on "
             "sait ce qu'elle est.")

    d.piege("Le piège des trois insistances",
            "C'est COMPLÈTEMENT GRATUIT, SAMEDI, au CENTRE SAINTE-ODILE.",
            "C'est complètement GRATUIT, samedi, au centre Sainte-Odile.",
            "Insister sur tout revient à n'insister sur rien : l'auditeur ne sait plus "
            "quoi retenir. Une capsule de trente secondes a droit à un mot mis en avant, "
            "un seul.",
            notes="Faire l'expérience : dire une annonce avec trois insistances, puis "
                  "avec une seule. Demander au groupe ce qu'il a retenu.")

    d.piege("Le piège du volume",
            "Vous criez le mot au lieu de l'allonger.",
            "Vous allongez la syllabe et vous montez le ton.",
            "L'accent d'insistance n'est pas une question de volume. Crier fatigue "
            "l'auditeur et sonne agressif à la radio. C'est la durée et la hauteur qui "
            "font le travail, pas la force.",
            notes="Faire essayer les deux : crier, puis allonger. La deuxième version "
                  "est plus efficace et plus agréable.")

    d.pratique('Pratique · 3 de 6', "Choisissez le mot à mettre en avant",
               "Un seul mot par annonce. Lequel, et pourquoi ?", [
        ("Atelier de réparation, samedi, gratuit, au centre Sainte-Odile.",
         "gratuit — c'est l'argument le plus fort"),
        ("Dernière soirée de couture avant l'été, vendredi, cinq dollars.",
         "dernière — l'urgence fait agir"),
        ("Vous repartez avec votre vélo réglé, dimanche, à l'école Saint-Fidèle.",
         "réglé — le résultat concret"),
        ("Trente artisans vous ouvrent leur atelier, du 3 au 5 octobre.",
         "trente — la quantité impressionne"),
    ], corrige=True,
       notes="Faire justifier chaque choix. Plusieurs réponses se défendent : c'est la "
             "justification qu'on évalue.")

    d.pratique('Pratique · 4 de 6', "Dites l'annonce",
               "À voix haute, avec un seul accent d'insistance.", [
        ("Annonce 1", "L'atelier de réparation, c'est samedi, et c'est GRATUIT."),
        ("Annonce 2", "C'est la DERNIÈRE soirée de couture avant l'été."),
        ("Annonce 3", "Vous repartirez avec un vélo qui ROULE."),
    ], corrige=True,
       notes="Faire dire chaque annonce par trois élèves. Le groupe devine sur quel mot "
             "l'accent a été mis : si personne ne devine, c'est raté.")


    d.regle("Deux sons proches de la capsule",
            "Le son « ch » souffle sans voix ; le son « j » fait vibrer la gorge.",
            precision="« Affiche » et « message » sont les deux supports du module. "
                      "Leurs deux sons se font au même endroit de la bouche : seule "
                      "la vibration les sépare.",
            notes="Faire poser la main sur la gorge. « ch » ne vibre pas, « j » vibre. "
                  "C'est le seul critère fiable, et il se sent au doigt.")

    d.tableau('Analyse', "Les deux sons dans les mots de la publicité",
              ['Le son', "Il s'écrit", 'Mots du module'],
              [["le son « ch »", "ch", "affiche, choisis, chaîne, déchirés"],
               ["le son « j »", "j, ou g devant e, i, y", "gens, justement, message, rejoindre"]],
              cle=0,
              note="Devant a, o et u, le g ne fait pas le son « j » mais le son « g » : "
                   "gratuit, garde, légume.",
              notes="Faire classer trois mots supplémentaires trouvés par le groupe "
                    "avant de montrer la note du bas.")

    d.piege('Le piège du g de « gratuit »',
            "jratuit, avec le son « j »",
            "gratuit — le son « g », parce que le g précède un r",
            "Le g ne se ramollit qu'avant e, i ou y : gens, agence, budget. Partout "
            "ailleurs il reste dur : gratuit, garde, légume. Dans une publicité, "
            "« gratuit » est le mot qu'on répète le plus : il vaut la peine d'être juste.",
            notes="Faire lire à voix haute « les gens profitent d'un atelier gratuit » : "
                  "les deux valeurs du g sont dans la même phrase.")

    d.pratique('Pratique · 5 de 6', 'Quel son entendez-vous ?',
               "Écoutez le mot, écrivez « ch » ou « j ».", [
        ("affiche", "le son « ch »"),
        ("message", "le son « j »"),
        ("choisis", "le son « ch »"),
        ("gens", "le son « j »"),
        ("chaîne", "le son « ch »"),
        ("justement", "le son « j »"),
        ("déchirés", "le son « ch »"),
        ("rejoindre", "le son « j »"),
    ], corrige=True, cols=2,
       notes="Les huit mots de l'exercice de sons du module en ligne, dans le même "
             "ordre. Faire garder la main sur la gorge pendant l'écoute.")

    d.pratique('Pratique · 6 de 6', 'Trois phrases de capsule à lire à voix haute',
               "Chacun lit une phrase. Le groupe ne corrige que les « ch » et les « j ».", [
        ("Choisis une seule idée par capsule.", "ch"),
        ("Le message doit rejoindre les gens du quartier.", "j · j · j"),
        ("L'affiche annonce un atelier gratuit.", "ch · g dur"),
    ], corrige=True,
       notes="La troisième phrase est la plus utile : elle oppose le son « ch », le "
             "son « j » et le g dur en une seule ligne.")

    d.billet(
        "Écrivez une annonce de deux phrases et soulignez le mot sur lequel vous insisterez.",
        exemples=[
            "Un seul mot souligné.",
            "Écrivez à côté pourquoi vous avez choisi celui-là.",
        ],
        notes="La justification est le vrai contenu du billet. Un choix expliqué vaut "
              "mieux qu'un bon choix inexpliqué.")

    return d.save(dossier)
