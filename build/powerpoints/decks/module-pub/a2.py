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
        "employer l'intonation d'une phrase exclamative.",
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

    d.pratique('Pratique · 1 de 4', "Sur quel mot insiste-t-on ?",
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

    d.pratique('Pratique · 2 de 4', "Insistance ou exclamation ?",
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

    d.pratique('Pratique · 3 de 4', "Choisissez le mot à mettre en avant",
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

    d.pratique('Pratique · 4 de 4', "Dites l'annonce",
               "À voix haute, avec un seul accent d'insistance.", [
        ("Annonce 1", "L'atelier de réparation, c'est samedi, et c'est GRATUIT."),
        ("Annonce 2", "C'est la DERNIÈRE soirée de couture avant l'été."),
        ("Annonce 3", "Vous repartirez avec un vélo qui ROULE."),
    ], corrige=True,
       notes="Faire dire chaque annonce par trois élèves. Le groupe devine sur quel mot "
             "l'accent a été mis : si personne ne devine, c'est raté.")

    d.billet(
        "Écrivez une annonce de deux phrases et soulignez le mot sur lequel vous insisterez.",
        exemples=[
            "Un seul mot souligné.",
            "Écrivez à côté pourquoi vous avez choisi celui-là.",
        ],
        notes="La justification est le vrai contenu du billet. Un choix expliqué vaut "
              "mieux qu'un bon choix inexpliqué.")

    return d.save(dossier)
