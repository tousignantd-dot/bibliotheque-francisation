# -*- coding: utf-8 -*-
"""A2 · Le son « ch » et le son « j ».
Bloc A « Je découvre » · couleur indigo · 60 min. Graphie-phonie.
Source du module : exercice `prPhon`, mini-leçon `prPhon`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Le son « ch » et le son « j »",
        chapeau="Deux sons voisins, faits au même endroit de la bouche. Une "
                "seule chose les sépare : pour « ch », la gorge est "
                "tranquille ; pour « j », elle vibre. Deux mots repères — "
                "chaudron, gymnase — et tout le module s'entend.",
        duree='60 minutes')

    d.titre(notes="Séance de graphie-phonie. Prévoir que chacun pose deux doigts sur sa "
                  "propre gorge : c'est la seule façon de faire sentir la différence, et "
                  "elle marche du premier coup.")

    d.objectifs([
        "entendre la différence entre le son « ch » et le son « j » ;",
        "produire les deux sons en contrôlant la vibration de ma gorge ;",
        "savoir que le son « j » s'écrit j, mais aussi g devant e, i et y ;",
        "reconnaître les mots du module qui portent l'un ou l'autre.",
    ])

    d.regle("La seule différence",
            "Pour « ch », la gorge est tranquille. Pour « j », elle vibre.",
            precision="La langue est au même endroit, les lèvres sont un peu avancées "
                      "dans les deux cas. Rien ne bouge, sauf la gorge. Posez deux "
                      "doigts dessus et dites « chhh », puis « jjj » : au deuxième, "
                      "vous sentez quelque chose bouger sous vos doigts.",
            notes="Diapo à photographier. Le faire faire à tout le groupe en même temps, "
                  "debout si possible. Passer entre les rangées : ceux qui ne sentent "
                  "rien serrent trop la gorge ou soufflent trop fort.")

    d.tableau('Analyse', "Deux sons, deux graphies",
              ["Le son", "Comment il s'écrit", "Exemples du module"],
              [["ch · comme chaudron", "ch", "chaudron · chercher · chaque"],
               ["j · comme gymnase", "j", "jeudi · je · journée"],
               ["j · comme gymnase", "g devant e, i, y", "gymnase · gens · gigot"],
               ["gu · pas le son j", "g devant a, o, u", "gâteau · gomme · légume"]],
              cle=0,
              note="Le son « j » a deux orthographes ; le son « ch » n'en a qu'une.",
              notes="Diapo à photographier. Insister sur la troisième ligne : c'est celle "
                    "qui manque à presque tout le monde, et c'est elle qui explique "
                    "pourquoi « gymnase » ne se lit pas « guymnase ».")

    d.pratique('Discrimination', "Quel son entendez-vous ?",
               "Écoutez, puis dites : le son de « chaudron » ou celui de « gymnase » ?", [
        ("un chaudron", "ch — la gorge est tranquille"),
        ("un gymnase", "j — écrit avec un g devant y"),
        ("jeudi", "j — écrit avec un j"),
        ("chercher", "ch — deux fois dans le même mot"),
        ("une séance", "ch — mais attention, il s'écrit c ici"),
        ("je voudrais", "j — le mot le plus utile du module"),
        ("la cuisine collective", "ch — dans « collective », pas dans « cuisine »"),
        ("le congé", "j — écrit avec un g devant e"),
    ], corrige=True,
       notes="C'est l'exercice prPhon du module, avec les mêmes mots : les élèves le "
             "retrouveront à l'écran avec l'audio. Faire répéter chaque mot après la "
             "correction, doigts sur la gorge.")

    d.piege('Le piège', "chymnase, guymnase", "gymnase",
            "Deux fautes pour un seul mot, et elles n'ont pas la même cause. « Chymnase » "
            "vient de la gorge qui ne vibre pas ; « guymnase » vient de la lettre g, lue "
            "comme dans « gâteau ». Devant e, i et y, le g se dit toujours « j ».",
            notes="Demander qui a déjà dit l'un ou l'autre. Dédramatiser : le mot est "
                  "long et il porte les deux difficultés en même temps.")

    d.cartes("Trois paires à écouter", "Le sens change", [
        ("le chou / la joue",
         "Le chou est un légume ; la joue est une partie du visage. Deux mots courants "
         "qu'on entend tous les jours, et qui ne se ressemblent que pour l'oreille "
         "qui n'a pas encore fait la différence."),
        ("chaque / la gêne",
         "« Chaque séance » et « la gêne de téléphoner » : les deux reviennent dans ce "
         "module-ci. Le premier a la gorge tranquille, le second la fait vibrer."),
        ("chercher / gérer",
         "Deux verbes de la vie courante. Dites-les l'un après l'autre, lentement, "
         "avec les doigts sur la gorge : la différence se voit avant de s'entendre."),
    ], notes="Faire dire chaque paire deux fois : la première pour comprendre, la seconde "
             "les yeux fermés, pour n'écouter que le son.")

    d.pratique('Production', "À lire à voix haute",
               "Six phrases du centre de quartier. Deux doigts sur la gorge.", [
        ("Le chaudron est dans la cuisine collective.", "ch deux fois"),
        ("Jeudi, il y a de la danse au gymnase.", "j deux fois"),
        ("Je cherche le babillard de l'entrée.", "j, puis ch"),
        ("Chaque séance coûte trois dollars.", "ch au début"),
        ("J'aimerais changer de journée.", "j, ch, j"),
        ("Le congé du dimanche change tout.", "j, puis ch"),
    ], notes="Faire lire par toute la classe ensemble, puis un élève à la fois. Ne "
             "corriger que le son travaillé : le reste attendra.")

    d.billet(
        "Écrivez trois mots de votre journée qui portent le son « j ».",
        exemples=[
            "Pensez aussi aux mots écrits avec un g : gens, gymnase, congé.",
            "Vérifiez avec vos doigts sur la gorge avant d'écrire.",
        ],
        notes="Devoir court. Les mots trouvés serviront d'exemples à la séance A3, où "
              "le vocabulaire du centre se met en place.")

    return d.save(dossier)
