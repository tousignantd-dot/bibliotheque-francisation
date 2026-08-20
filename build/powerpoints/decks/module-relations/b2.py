# -*- coding: utf-8 -*-
"""B2 · qui, que, où.
Bloc B · couleur ambre (écriture) · 90 min.
Source : mini-leçon `t1rel`, exercices `t1rel` et `t1relGN`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre='qui, que, où',
        chapeau="« L'autobus ___ je prends s'arrête loin. » Trois pronoms "
                "possibles, un seul juste. Le choix ne dépend pas de la "
                "personne ni de la chose : il dépend du mot qui suit.",
        duree='90 minutes')

    d.titre(notes="Séance de grammaire longue. Écrire la phrase du chapeau au tableau et "
                  "faire voter à main levée. Garder le résultat affiché jusqu'à la fin.")

    d.objectifs([
        "coller deux phrases ensemble sans répéter le même mot ;",
        "choisir entre qui, que et où en regardant ce qui suit le trou ;",
        "savoir que où reprend aussi un moment, pas seulement un lieu ;",
        "retrouver le mot que le pronom remplace dans une phrase entendue.",
    ])

    d.declencheur(
        'Le problème', "Comment dire ces deux phrases en une seule ?",
        pistes=[
            "« Je prends un autobus. Cet autobus s'arrête loin. »",
            "Qu'est-ce qui se répète ?",
            "Par quel petit mot pourrait-on remplacer la répétition ?",
            "Essayez à voix haute, même sans être sûr.",
        ],
        notes="Laisser essayer trois ou quatre élèves avant de donner la réponse. Plusieurs "
              "produiront la bonne phrase spontanément : le point à enseigner est le choix "
              "entre les trois, pas l'idée de relier.")

    d.tableau('Analyse', "Ce qui vient après le trou",
              ['Après le trou', 'Le pronom', 'Exemple'],
              [["un verbe", "qui", "une collègue qui m'a parlé"],
               ["un sujet", "que", "le trajet que je fais"],
               ["un lieu avant", "où", "le gymnase où on joue"],
               ["un moment avant", "où", "l'année où je suis arrivée"]],
              cle=0,
              note="Le test tient en une question : qu'est-ce qui vient juste après le trou ?",
              notes="C'est la diapo centrale de la séance. La faire recopier telle quelle "
                    "dans le cahier avant de continuer.")

    d.regle('qui — le sujet',
            "Après qui, le verbe arrive tout de suite. Il n'y a pas d'autre sujet.",
            precision="« C'est une collègue qui m'a parlé du centre. » Le pronom qui est "
                      "lui-même le sujet du verbe « a parlé ». Si vous voyez un sujet après "
                      "le trou — je, tu, elle, mon frère — ce n'est pas qui.",
            notes="Faire souligner le verbe qui suit, dans trois exemples au tableau.")

    d.regle('que — le complément',
            "Après que, il y a un autre sujet, puis le verbe.",
            precision="« C'est le trajet que je fais chaque semaine. » Après que vient « je », "
                      "un sujet. Le trajet est ce qu'on fait : le complément direct. "
                      "Devant une voyelle, que devient qu' — mais qui ne se raccourcit jamais.",
            notes="Insister sur la dernière phrase : « qu'il » pour « qui il » est une des "
                  "fautes les plus fréquentes à l'écrit.")

    d.regle('où — le lieu, et le moment',
            "où reprend un endroit, mais aussi un moment.",
            precision="« Le gymnase où on joue » et « l'année où je suis arrivée » sont tous "
                      "les deux corrects. C'est la partie que les élèves oublient : en "
                      "anglais on dirait when, en français c'est le même mot que pour le lieu.",
            notes="Donner trois exemples de temps : le jour où, l'année où, le moment où. "
                  "Les écrire au tableau et les y laisser.")

    d.piege('Le piège de la personne',
            "les gens qui je vois le jeudi",
            "les gens que je vois le jeudi",
            "qui et que ne dépendent pas du fait qu'on parle d'une personne ou d'une chose. "
            "Beaucoup d'élèves choisissent qui parce qu'il s'agit de gens — et se trompent "
            "à chaque fois. Ce qui décide, c'est ce qui suit : ici, « je », un sujet.",
            notes="C'est la faute numéro un sur cette notion. Y consacrer du temps : faire "
                  "produire cinq phrases avec « les gens que… » par cinq élèves différents.")

    d.pratique('Pratique · 1 de 2', "qui, que ou où ?",
               "Complétez chaque phrase. Regardez ce qui vient juste après le trou.", [
        ("L'autobus ___ je prends s'arrête à trois coins de rue.", "que"),
        ("C'est une collègue ___ m'a parlé du centre communautaire.", "qui"),
        ("Le gymnase ___ on joue est au sous-sol.", "où"),
        ("Les gens ___ je vois le jeudi sont presque ma famille.", "que"),
        ("Le tournoi ___ commence en avril dure deux jours.", "qui"),
        ("Le parc ___ mes enfants jouent est à côté de la maison.", "où"),
    ], corrige=True,
       notes="Faire dire à voix haute, pour chaque ligne, ce qui vient après le trou avant "
             "de donner la réponse. Le raisonnement compte plus que la bonne case.")

    d.pratique('Pratique · 2 de 2', "De quoi parle-t-on ?",
               "Dites quel mot le pronom remplace.", [
        ("« Le gymnase où on joue n'est pas facile à trouver. »", "le gymnase"),
        ("« C'est une collègue qui m'a parlé du centre. »", "une collègue"),
        ("« Les gens que je vois le jeudi sont ma famille. »", "les gens"),
        ("« L'année où je suis arrivée, il faisait froid. »", "l'année"),
        ("« Le manteau que mon cousin avait apporté était trop grand. »", "le manteau"),
    ], corrige=True, cols=1,
       notes="Cet exercice vérifie la compréhension, pas la production. Un élève qui "
             "retrouve l'antécédent comprend la phrase, même s'il hésite encore à écrire.")

    d.billet(
        "Écrivez trois phrases sur votre quartier : une avec qui, une avec que, une avec où.",
        exemples=[
            "Soulignez, dans chaque phrase, le mot que le pronom remplace.",
            "Exemple : « Le parc où mes enfants jouent est à côté de la maison. »",
        ],
        notes="Corriger individuellement et rendre à la séance suivante : cette notion "
              "demande une rétroaction personnelle, pas une correction collective.")

    return d.save(dossier)
