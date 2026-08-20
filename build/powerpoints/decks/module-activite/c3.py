# -*- coding: utf-8 -*-
"""C3 · Chaque, plusieurs, quelques.
Bloc C · couleur ambre (écriture) · 60 min.
Source : mini-leçon `t2quant`, exercice `t2quant`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre='Chaque, plusieurs, quelques',
        chapeau="« Chaque cours », « plusieurs parents », « quelques places ». "
                "Ces mots disent une quantité sans la compter — et chacun "
                "impose sa propre forme au nom qui suit.",
        duree='60 minutes')

    d.titre(notes="Écrire les trois mots au tableau et demander lequel est suivi d'un "
                  "singulier. Le vote est toujours partagé : c'est le point de la séance.")

    d.objectifs([
        "employer chaque avec un nom singulier ;",
        "employer plusieurs et quelques avec un nom pluriel ;",
        "distinguer quelques (peu) de plusieurs (un bon nombre) ;",
        "savoir que tous les et chaque veulent dire la même chose.",
    ])

    d.tableau('Analyse', "Le nom qui suit",
              ['Le mot', 'Le nom qui suit', 'Ce que ça dit'],
              [["chaque", "singulier", "un par un"],
               ["plusieurs", "pluriel", "un bon nombre"],
               ["quelques", "pluriel", "un petit nombre"],
               ["tous les", "pluriel", "sans exception"]],
              cle=0,
              note="Un seul demande le singulier : chaque.",
              notes="Diapo centrale. Faire recopier. La note résume toute la difficulté.")

    d.regle('chaque — jamais de s',
            "« chaque cours », jamais « chaques cours ».",
            precision="<b>chaque</b> ne prend jamais de s, et le nom qui suit reste au "
                      "singulier — même si on parle de douze cours. C'est le contraire de "
                      "ce que l'intuition suggère : on les prend un à la fois.",
            notes="C'est la faute la plus fréquente de la séance. Écrire la forme juste au "
                  "tableau et l'y laisser.")

    d.regle('plusieurs — invariable',
            "La même forme au masculin et au féminin.",
            precision="« plusieurs parents », « plusieurs activités », « plusieurs "
                      "places ». Jamais de « plusieures ». Ce mot ne change jamais.",
            notes="Rassurer : c'est un des rares mots français qui ne s'accorde pas du "
                  "tout.")

    d.piege('Confondre quelques et quelque chose',
            "Il reste quelque chose de places.",
            "Il reste quelques places.",
            "<b>quelques</b> (avec s) annonce un petit nombre et se met devant un nom "
            "pluriel. <b>quelque chose</b> est un mot différent, qui désigne une chose "
            "indéterminée et reste toujours au singulier. Les deux n'ont rien à voir.",
            notes="Donner deux exemples de chaque. La confusion vient de la ressemblance, "
                  "pas du sens.")

    d.pratique('Pratique · 1 de 2', "Quel déterminant ?",
               "Complétez.", [
        ("___ cours reprend ce qui a été vu la semaine d'avant.", "Chaque"),
        ("___ parents s'installent devant la vitre.", "Plusieurs"),
        ("Il reste ___ places dans la chorale.", "quelques"),
        ("Le cours a lieu ___ samedis, de neuf à dix heures.", "tous les"),
        ("___ enfant doit avoir son propre bonnet de bain.", "Chaque"),
        ("Le dépliant présente ___ activités : une trentaine en tout.", "plusieurs"),
    ], corrige=True,
       notes="Faire dire à voix haute si le nom qui suit est singulier ou pluriel avant de "
             "répondre. C'est le raisonnement qui compte.")

    d.pratique('Pratique · 2 de 2', "Corrigez la phrase",
               "Chaque phrase contient une faute d'accord.", [
        ("Chaques cours dure une heure.", "Chaque cours dure une heure."),
        ("Chaque enfants doit avoir son bonnet.", "Chaque enfant doit avoir son bonnet."),
        ("Plusieures activités sont offertes.", "Plusieurs activités sont offertes."),
        ("Il reste quelque place.", "Il reste quelques places."),
    ], corrige=True, cols=1,
       notes="Faire nommer la faute avant de corriger : accord du déterminant, ou accord "
             "du nom ?")

    d.cartes('À l\'oral, au Québec', "Deux formes très employées", [
        ("« bien des »",
         "Veut dire « beaucoup de ». « Bien des parents arrivent en retard. » Très "
         "fréquent à l'oral, plus rare à l'écrit."),
        ("« tous les »",
         "« Tous les samedis » et « chaque samedi » veulent exactement la même chose. "
         "« Tous les » est plus courant dans la conversation."),
        ("Ce qu'on écrit",
         "Dans un texte, <b>chaque</b> et <b>plusieurs</b> passent partout. Gardez « bien "
         "des » pour l'oral."),
    ], notes="Distinguer l'oral de l'écrit est un fil du module — il sera repris en D2 "
             "avec le registre.")

    d.billet(
        "Écrivez quatre phrases sur une activité, une par déterminant.",
        exemples=[
            "chaque, plusieurs, quelques, tous les.",
            "Soulignez le nom qui suit et indiquez s'il est au singulier ou au pluriel.",
        ],
        notes="Corriger surtout le singulier après chaque. Rendre à la séance suivante.")

    return d.save(dossier)
