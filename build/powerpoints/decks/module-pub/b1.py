# -*- coding: utf-8 -*-
"""B1 · Deux capsules à comparer.
Bloc B · couleur acier (compréhension orale) · 60 min.
Source : dialogue `t1` et exercice `t1capsules`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Deux capsules à comparer',
        chapeau="Vingt secondes contre quarante. La plus courte n'est pas la plus "
                "claire — et c'est ce qui surprend Solange avant d'enregistrer la "
                "sienne.",
        duree='60 minutes')

    d.titre(notes="Ouverture du défi 1. Faire écouter, si possible, deux vraies capsules "
                  "de radio communautaire avant le dialogue. La comparaison devient "
                  "concrète.")

    d.objectifs([
        "comparer deux enregistrements sur trois critères ;",
        "reconnaître ce qui nuit à la clarté d'une capsule ;",
        "comprendre des conseils techniques donnés à l'oral ;",
        "employer le vocabulaire de la comparaison.",
    ])

    d.dialogue('Dialogue · 1 de 3', "Vingt secondes et quarante secondes", [
        ("OMAR", "Avant d'enregistrer, écoute les deux capsules du mois passé. Celle de "
                 "la friperie dure vingt secondes ; celle de la cuisine collective, "
                 "quarante.", True),
        ("SOLANGE", "À la friperie, on parle plus vite que sur l'autre capsule. On "
                    "comprend moins bien, je trouve.", True),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="Passer l'audio du défi 1. Faire relever la comparaison de Solange : « plus "
             "vite que ». C'est la construction de la séance B2.")

    d.dialogue('Dialogue · 2 de 3', "Plus longue, mais plus claire", [
        ("OMAR", "Tu as raison. La capsule de la cuisine collective est plus longue, "
                 "mais elle est aussi plus claire que celle de la friperie.", True),
        ("SOLANGE", "Et la musique ? Celle de la friperie est plus forte que la musique "
                    "de la cuisine collective. Elle couvre la voix.", True),
    ], notes="Faire remarquer le « mais » : plus longue ET plus claire. La longueur n'est "
             "pas le problème, la vitesse l'est.")

    d.dialogue('Dialogue · 3 de 3', "Insiste sur un seul mot", [
        ("OMAR", "Alors baisse la musique, ralentis un peu, et insiste sur un seul mot : "
                 "gratuit. C'est celui-là que les gens vont retenir.", True),
    ], notes="Trois conseils en une réplique : la musique, le rythme, l'accent "
             "d'insistance. Ce dernier renvoie à la séance A2.")

    d.tableau('Analyse', "Les deux capsules, comparées",
              ['Le critère', 'La friperie', 'La cuisine collective'],
              [["la durée", "vingt secondes", "quarante secondes"],
               ["le rythme", "on parle vite", "on parle plus lentement"],
               ["la clarté", "on comprend moins bien", "plus claire"],
               ["la musique", "trop forte, couvre la voix", "au bon niveau"]],
              cle=0, props=[0.24, 0.38, 0.38],
              notes="Quatre critères. Faire remarquer que la plus courte perd sur trois "
                    "d'entre eux : la brièveté n'est pas une qualité en soi.")

    d.regle('La règle du défi 1',
            "Une capsule courte n'est pas une capsule rapide.",
            precision="Trente secondes, c'est court : il faut donc dire moins de choses, "
                      "pas les dire plus vite. Parler vite fait perdre l'auditeur, et "
                      "une capsule qu'on ne comprend pas ne sert à rien, même en vingt "
                      "secondes.",
            notes="Diapo centrale du défi. C'est la leçon que Solange retient, et c'est "
                  "celle qui vaut pour toute prise de parole.")

    d.cartes('Analyse', "Trois choses qui nuisent à une capsule", [
        ("Le débit trop rapide",
         "On croit gagner du temps ; on perd l'auditeur. La solution n'est pas de "
         "ralentir, mais de couper du texte."),
        ("La musique trop forte",
         "Elle couvre la voix. Une musique de fond doit s'entendre sans qu'on ait à "
         "faire un effort pour comprendre la parole."),
        ("Trop d'informations",
         "Six objets nommés, trois adresses, deux heures : personne ne retient. Une "
         "capsule porte une idée et trois faits."),
        ("Ce qui aide",
         "Un mot mis en avant, un slogan court, et une seule information par phrase."),
    ], notes="La quatrième carte donne la solution positive. Ne pas finir sur les trois "
             "problèmes : les élèves doivent repartir avec la méthode.")

    d.pratique('Pratique · 1 de 4', "Sept questions sur le dialogue",
               "Répondez sans relire.", [
        ("Combien de temps dure la capsule de la friperie ?", "vingt secondes"),
        ("Et celle de la cuisine collective ?", "quarante secondes"),
        ("Quelle capsule est la plus claire, selon Omar ?", "celle de la cuisine collective"),
        ("Qu'est-ce que Solange reproche à la capsule de la friperie ?",
         "on y parle trop vite, alors on comprend moins bien"),
        ("Quel problème pose la musique de la friperie ?",
         "elle est trop forte et elle couvre la voix"),
        ("Sur quel mot Solange devra-t-elle insister ?", "sur le mot « gratuit »"),
    ], corrige=True,
       notes="Six questions, six réponses courtes. Faire répondre sans notes : le "
             "dialogue est court et dense.")

    d.pratique('Pratique · 2 de 4', "Les trois conseils d'Omar",
               "Que doit faire Solange avant d'enregistrer ?", [
        ("Premier conseil", "baisser la musique"),
        ("Deuxième conseil", "ralentir un peu"),
        ("Troisième conseil", "insister sur un seul mot"),
        ("Le mot choisi", "gratuit"),
    ], corrige=True,
       notes="Faire remarquer que les trois conseils sont concrets et applicables tout "
             "de suite. C'est ce qui fait un bon conseil.")

    d.piege("Le piège du « je vais parler plus vite »",
            "Mon texte est trop long, je vais le lire plus vite.",
            "Mon texte est trop long, je vais le couper.",
            "Accélérer ne raccourcit presque rien et détruit la compréhension. Couper une "
            "phrase gagne quatre secondes sans rien perdre — parce que la phrase coupée "
            "était celle que personne n'écoutait.",
            notes="Faire l'expérience : lire un texte de quarante secondes en trente. "
                  "Puis le couper. Le groupe entendra la différence.")

    d.piege("Le piège de la musique",
            "Une musique forte rend la capsule dynamique.",
            "Une musique forte couvre la voix.",
            "La musique de fond doit rester en dessous de la parole. À la radio, "
            "l'auditeur est souvent en voiture ou dans le bruit : ce qui est déjà "
            "difficile à comprendre devient impossible.",
            notes="Point technique simple mais souvent ignoré. Le relier à l'écoute "
                  "réelle : personne n'écoute la radio dans le silence.")

    d.pratique('Pratique · 3 de 4', "Qu'est-ce qui ne va pas ?",
               "Un problème par capsule.", [
        ("On y nomme six sortes d'objets en vingt secondes.", "trop d'informations"),
        ("La musique est au même volume que la voix.", "musique trop forte"),
        ("Le texte de quarante secondes est lu en vingt.", "débit trop rapide"),
        ("On insiste sur quatre mots différents.", "aucun mot ne ressort"),
    ], corrige=True,
       notes="Faire proposer une correction pour chaque problème. C'est la partie utile "
             "de l'exercice.")

    d.pratique('Pratique · 4 de 4', "Comparez deux annonces",
               "Sur trois critères : durée, clarté, ce qu'on retient.", [
        ("Annonce A", "vingt secondes, six informations, débit rapide"),
        ("Annonce B", "trente secondes, trois informations, un mot mis en avant"),
        ("Laquelle est la plus claire ?", "B — moins d'informations, plus de temps"),
        ("Qu'est-ce qu'on retient de chacune ?", "de A, rien ; de B, le mot mis en avant"),
    ], corrige=True,
       notes="Cette comparaison prépare directement B2, où l'on apprendra à la formuler "
             "avec « plus… que » et « moins… que ».")

    d.billet(
        "Écoutez une publicité à la radio et notez trois choses.",
        exemples=[
            "Sa durée approximative, le mot mis en avant, ce que vous avez retenu.",
            "N'importe quelle radio, n'importe quelle publicité.",
        ],
        notes="Devoir court et concret. Il installe une écoute active de la publicité, "
              "qui est l'objectif du module.")

    return d.save(dossier)
