# -*- coding: utf-8 -*-
"""A2 · Le son de « é » et le son de « è »
Bloc A « Je découvre » · couleur indigo · 75 min. Graphie-phonie.
Source : exercice `prPhon` et sa mini-leçon du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Le son de « é » et le son de « è »",
        chapeau="Météo, prévisions, éclaircie, été d'un côté ; tempête, "
                "averse, neige, veille de l'autre. Deux voyelles voisines qui "
                "portent la moitié des mots du temps qu'il fait — et qui "
                "séparent « je reporterai » de « je reporterais ».",
        duree='75 minutes')

    d.titre(notes="Séance de prononciation. Elle se fait debout, à voix haute, et le "
                  "groupe doit s'entendre. Prévoir un miroir de poche par personne si "
                  "possible : la différence entre les deux sons est visible sur la "
                  "mâchoire avant d'être audible à l'oreille.")

    d.objectifs([
        "entendre la différence entre le son de « é » et celui de « è » ;",
        "produire les deux en surveillant l'ouverture de la mâchoire ;",
        "savoir que « er » à la fin d'un infinitif se dit « é » ;",
        "distinguer « je reporterai » de « je reporterais ».",
    ], notes="Le quatrième objectif n'est pas un raffinement : devant un groupe qui "
             "attend une décision, il sépare ce qui est décidé de ce qui ne l'est pas. "
             "Y consacrer la dernière demi-heure, sans se presser.")

    d.declencheur(
        'Écoute', "« L'été. La tempête. » Qu'est-ce qui change dans votre "
                  "bouche entre les deux ?",
        pistes=[
            "Est-ce que la bouche s'ouvre plus, ou moins ?",
            "Où sont les lèvres : étirées, ou détendues ?",
            "Est-ce que le son est court et tendu, ou plus large ?",
            "Dans quelle langue que vous connaissez ces deux sons existent-ils ?",
        ],
        notes="La dernière piste est importante : beaucoup de langues n'ont qu'un seul "
              "son entre les deux. Si c'est le cas d'un élève, son oreille entend "
              "« la même voyelle deux fois » — c'est normal, et ça se corrige par le "
              "geste, pas par l'écoute.")

    d.regle("Le son de « é » : la bouche presque fermée",
            "Les lèvres s'étirent sur les côtés, la mâchoire reste haute, le "
            "son est tendu et clair.",
            precision="Quatre orthographes, un seul son : é, er à la fin d'un "
                      "verbe, ez, et parfois es. Reporter se dit « report-é ».",
            notes="Faire produire le son en série : météo, prévisions, éclaircie, été, "
                  "gelée. Puis les infinitifs : reporter, annuler, apporter — le r final "
                  "ne s'entend jamais, et c'est déroutant pour qui vient d'une langue où "
                  "toutes les lettres se prononcent.")

    d.regle("Le son de « è » : la mâchoire descend",
            "La bouche s'ouvre franchement, la langue est plus basse, le son "
            "est plus grave et plus long.",
            precision="On l'écrit è, ê, ai, ei, ou simplement e devant deux "
                      "consonnes : neige, veille, verglas, avertissement.",
            notes="Insister sur « avertissement » : c'est le mot le plus important du "
                  "module et il commence par un « è » sans accent écrit. A-VER-tis-se-"
                  "ment, comme dans « hiver ». Le faire répéter dix fois, sans rire.")

    d.tableau('Deux colonnes', "Où va chaque mot du bulletin ?",
              ['Le son de « é »', 'Le son de « è »'],
              [["la météo", "la tempête"],
               ["les prévisions", "une averse"],
               ["une éclaircie", "la neige"],
               ["l'été · une gelée", "la grêle · la veille"]],
              cle=1,
              notes="Faire trier au tableau, mot par mot, avant d'afficher la colonne de "
                    "droite. Les élèves se corrigent entre eux : c'est l'exercice le plus "
                    "efficace de la séance.")

    d.cartes("La paire qui décide", "Futur ou conditionnel ?", [
        ("Je reporterai",
         "Son de « é » à la fin. C'est décidé : je le ferai."),
        ("Je reporterais",
         "Son de « è » à la fin. Ce n'est pas décidé : je le ferais peut-être."),
        ("Je confirmerai",
         "Décidé. « Je vous confirmerai vendredi à midi. »"),
        ("Je confirmerais",
         "Pas décidé. « Je confirmerais bien, mais je ne sais pas encore. »"),
    ], notes="Faire dire les quatre en boucle, deux par deux. Beaucoup de francophones "
             "ne font plus cette différence ; la faire quand même, elle rend service. "
             "Écouter chaque élève individuellement au moins une fois.")

    d.piege("Dire le r final d'un infinitif",
            "Je vais reportèr la sortie.",
            "Je vais reporté la sortie.",
            "Le « er » final d'un verbe se dit « é » et le r ne s'entend jamais : "
            "reporter, annuler, apporter, prévenir est une autre famille.",
            notes="C'est la faute la plus fréquente de la séance, et la plus vite "
                  "corrigée : dix infinitifs à la file suffisent souvent.")

    d.piege("Chercher l'accent écrit pour décider du son",
            "Neige, veille, verglas : il n'y a pas d'accent, donc c'est « é ».",
            "Neige, veille, verglas, avertissement : tous avec le son « è ».",
            "Beaucoup de « è » ne portent aucun accent. C'est l'oreille qui "
            "commande, pas l'orthographe — et la règle du e devant deux consonnes.",
            notes="Faire relever dans le dialogue prep tous les mots à « è » sans accent "
                  "écrit. Il y en a plus que le groupe ne l'imagine.")

    d.pratique('Écoute', "Quel son entendez-vous ?",
               "L'enseignante dit le mot ; le groupe lève une main pour « é », "
               "deux pour « è ».", [
        ("la météo", "é"),
        ("la tempête", "è"),
        ("les prévisions", "é"),
        ("la neige", "è"),
        ("une éclaircie", "é"),
        ("une averse", "è"),
        ("l'été", "é"),
        ("la grêle", "è"),
        ("une gelée", "é"),
        ("la veille", "è"),
    ], corrige=True,
       notes="Ce sont exactement les dix cartes de l'exercice prPhon du module. Les faire "
             "d'abord ici, à la voix, puis renvoyer au module pour les réécouter seul : "
             "la reprise à la maison est ce qui fait entrer la différence.")

    d.billet(
        "Écrivez trois mots du temps avec le son « é » et trois avec le son « è ».",
        exemples=[
            "Vous pouvez les prendre dans le dialogue ou en chercher d'autres.",
            "Dites-les à voix haute avant de les écrire : c'est l'oreille qui tranche.",
        ],
        notes="Relever les billets et repérer les erreurs de tri : elles disent quels "
              "mots reprendre en A3, pendant le travail sur le vocabulaire.")

    return d.save(dossier)
