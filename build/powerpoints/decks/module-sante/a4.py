# -*- coding: utf-8 -*-
"""A4 · Dire comment on se sent.
Bloc A « Je découvre » · couleur teal (écoute et réponds) · 55 min.
Source du module : dialogue `prep` (« Je me sens fatiguée depuis deux semaines »),
savoirs `l2` et `l4` en avant-goût, cartes mémoire « se sentir ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre='Dire comment on se sent',
        chapeau="Deux symptômes et une durée : c'est tout ce que la réceptionniste "
                "attend. Trop en dire fait perdre le rendez-vous, pas trop peu.",
        duree='55 minutes')

    d.titre(notes="Séance charnière : elle prépare l'appel enregistré de E1. Les phrases "
                  "écrites ici seront réutilisées telles quelles.")

    d.objectifs([
        "décrire un symptôme en une phrase courte ;",
        "dire depuis quand ça dure ;",
        "doser l'intensité : un peu, assez, très, trop ;",
        "distinguer « j'ai mal à » et « je me sens ».",
    ])

    d.regle('La règle du symptôme',
            "Ce que je ressens · depuis quand.",
            precision="« Je me sens fatiguée depuis deux semaines. » Deux informations, "
                      "une phrase. Le médecin posera les autres questions.",
            notes="La diapositive à photographier. La comparer à ce que les élèves "
                  "diraient spontanément — souvent un récit de trois minutes.")

    d.tableau('Analyse', "Deux façons de dire, à ne pas mélanger",
              ['La structure', 'Quand on l\'emploie'],
              [["j'ai mal à + endroit", "une douleur localisée : à la tête, au dos, "
                                        "au ventre, à la gorge"],
               ["je me sens + adjectif", "un état général : fatiguée, faible, "
                                         "nerveuse, mieux"],
               ["j'ai + nom", "un symptôme qui a un nom : de la fièvre, la nausée, "
                              "des étourdissements"]],
              cle=0,
              note="Lina emploie les deux premières dans la même phrase.",
              notes="L'erreur la plus fréquente est « je me sens mal à la tête ». La "
                    "traiter ici, avant qu'elle s'installe.")

    d.piege("Le piège du mélange",
            "Je me sens mal à la tête depuis deux semaines.",
            "J'ai mal à la tête depuis deux semaines.",
            "« Se sentir » demande un adjectif : je me sens fatiguée, je me sens mieux. "
            "Pour une douleur à un endroit précis, c'est « avoir mal à ».",
            notes="Faire dire les deux phrases correctes à voix haute, deux fois "
                  "chacune. C'est une erreur d'oreille, elle se corrige par l'oreille.")

    d.cartes('Analyse', "Doser, sans exagérer", [
        ("un peu",
         "« J'ai un peu mal à la tête. » Le cran le plus bas. Ça va."),
        ("assez",
         "« Ce médicament est assez efficace. » C'est réel, sans être fort."),
        ("très",
         "« Je suis très fatiguée. » C'est fort, et ça se dit sans dramatiser."),
        ("trop",
         "« Je suis trop fatiguée pour travailler. » Attention : trop veut dire plus "
         "qu'il ne faut. C'est un signal, pas un superlatif."),
    ], notes="La quatrième carte est le point à retenir. Elle est reprise en détail en "
             "C4 ; ici on ne fait que l'installer.")

    d.pratique('Pratique · 1 de 3', "Mal à, ou se sentir ?",
               "Complétez avec la bonne structure.", [
        ("___ la gorge depuis hier.", "J'ai mal à la gorge depuis hier."),
        ("___ fatiguée le matin.", "Je me sens fatiguée le matin."),
        ("___ au dos quand je travaille.", "J'ai mal au dos quand je travaille."),
        ("___ mieux depuis deux jours.", "Je me sens mieux depuis deux jours."),
        ("___ de la fièvre depuis ce matin.", "J'ai de la fièvre depuis ce matin."),
    ], corrige=True,
       notes="Faire justifier chaque choix par la question : est-ce un endroit, un "
             "adjectif, ou un nom ?")

    d.pratique('Pratique · 2 de 3', "Depuis quand ?",
               "Ajoutez la durée. Une phrase complète à chaque fois.", [
        ("Fatigue · deux semaines", "Je me sens fatiguée depuis deux semaines."),
        ("Mal de tête · trois jours", "J'ai mal à la tête depuis trois jours."),
        ("Toux · une semaine", "Je tousse depuis une semaine."),
        ("Mal au dos · un mois", "J'ai mal au dos depuis un mois."),
    ], corrige=True,
       notes="« Depuis » + durée, toujours. C'est l'information que la réceptionniste "
             "note et qui décide de l'urgence du rendez-vous.")

    d.pratique('Pratique · 3 de 3', "Votre phrase, la vraie",
               "Écrivez la phrase que vous diriez au téléphone, aujourd'hui.", [
        ("Ce que vous ressentez", "un symptôme, pas trois"),
        ("Depuis quand", "hier, trois jours, deux semaines"),
        ("L'intensité, si elle compte", "un peu, assez, très"),
        ("Rien d'autre", "le médecin posera les autres questions"),
    ], corrige=False,
       notes="Dix minutes. Circuler et couper ce qui dépasse : la phrase doit tenir en "
             "une respiration. C'est le critère.")

    d.billet(
        "Écrivez votre phrase de symptôme, prête à dire au téléphone.",
        exemples=[
            "Ce que je ressens, depuis quand.",
            "Vous la relirez avant de vous enregistrer, en E1.",
        ],
        notes="Ramasser et garder : ces billets sont redistribués au début de E1. Les "
              "élèves n'auront pas à réinventer leur phrase le jour de l'enregistrement.")

    return d.save(dossier)
