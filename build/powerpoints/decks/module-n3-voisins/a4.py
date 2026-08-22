# -*- coding: utf-8 -*-
"""A4 · Je m'appelle, je vous présente.
Bloc A « Je découvre » · couleur ambre (écriture) · 60 min.
Source : exercice `prPresente`, mini-leçon `prPresente`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-voisins/images/')


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Je m'appelle, je vous présente",
        chapeau="Se présenter, c'est donner son propre nom. Présenter "
                "quelqu'un, c'est en donner un troisième. Dans un escalier, "
                "les deux arrivent dans la même minute.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture et de formules. Prévoir de faire écrire au tableau : "
                  "« je m'appelle » avec son apostrophe est une orthographe qui se "
                  "photographie mieux qu'elle ne s'explique.")

    d.objectifs([
        "donner son nom, son étage et depuis quand on habite là ;",
        "présenter quelqu'un poliment ou simplement ;",
        "nommer le lien familial de la personne présentée ;",
        "répondre « enchanté » ou « enchantée » selon le cas.",
    ])

    d.regle("Le verbe s'appeler porte un petit mot",
            "« Je m'appelle Rachid Belkacem. »",
            precision="Le « m' » fait partie du verbe : je m'appelle, tu "
                      "t'appelles, il s'appelle. Sans lui, la phrase n'existe "
                      "pas. Et on ne dit pas « mon nom est » : ça se comprend, "
                      "mais personne ne le dit.",
            notes="Diapo à photographier. Écrire les trois personnes au tableau et faire "
                  "recopier. C'est la faute la plus fréquente de tout le module.")

    d.tableau('Analyse', "Se présenter : trois renseignements",
              ["Ce qu'on donne", "Comment on le dit"],
              [["le nom", "Je m'appelle Rachid Belkacem."],
               ["l'étage", "J'habite au troisième, au 3A."],
               ["depuis quand", "Nous sommes arrivés il y a trois semaines."],
               ["le métier, si ça vient", "Je suis électricien."]],
              cle=1,
              note="Dans un immeuble, l'étage vaut presque autant que le nom.",
              notes="Diapo à photographier. Faire remarquer « j'habite » : le H ne se "
                    "prononce pas, d'où l'apostrophe.")

    d.tableau('Analyse', "Présenter quelqu'un : trois formules",
              ["La formule", "Quand l'employer"],
              [["Je vous présente ma sœur.", "avec quelqu'un qu'on vouvoie — la plus polie"],
               ["Je te présente ma sœur.", "avec quelqu'un qu'on tutoie"],
               ["Voici ma sœur.", "tous les jours, plus court"],
               ["C'est ma sœur.", "encore plus court, tout aussi correct"]],
              cle=1,
              note="On commence toujours par nommer la personne à qui on parle : "
                   "« Madame Lachapelle, je vous présente… »",
              notes="Diapo à photographier. Faire pratiquer l'ordre en tour de table, "
                    "deux par deux, avec une troisième personne imaginaire.")

    d.vocabulaire('Vocabulaire', "Les liens familiaux", [
        ("ma femme, mon mari", "la personne avec qui on vit"),
        ("mon garçon, ma fille", "ses enfants — on dit aussi mon fils, ma fille"),
        ("mon frère, ma sœur", "les enfants des mêmes parents que soi"),
        ("mon père, ma mère", "ses parents"),
        ("mon oncle, ma tante", "le frère ou la sœur d'un parent"),
        ("mon voisin, ma voisine", "pas un lien familial — un lien de porte"),
    ], notes="La dernière ligne est là exprès : dans beaucoup de cultures on présente un "
             "voisin comme un cousin. Ici, on nomme le vrai lien, et c'est tout.")

    d.regle("Enchanté ou enchantée ?",
            "Le son est le même. Seule l'écriture change.",
            precision="Un homme écrit « enchanté », une femme écrit "
                      "« enchantée ». À l'oral, rien ne se distingue — c'est "
                      "une règle d'écriture, pas de prononciation.",
            notes="Diapo à photographier. Le dire clairement évite six mois d'hésitation "
                  "inutile à l'oral.")

    d.pratique('Écriture', "Complétez la présentation",
               "Employez « je m'appelle », « je vous présente », « c'est », "
               "« voici » ou « enchantée ».", [
        ("Bonjour, ___ Rachid Belkacem, du troisième.", "je m'appelle"),
        ("Madame Lachapelle, ___ ma sœur, Leïla.", "je vous présente"),
        ("___ ma sœur. Elle habite à Longueuil.", "C'est / Voici"),
        ("— Bonjour ! — Bonjour, ___ .", "enchantée / enchanté"),
        ("___ mon petit garçon. Il a quatre ans.", "Voici / C'est"),
        ("— Comment ___ , déjà ? — Manon Lachapelle.", "vous appelez-vous"),
    ], corrige=True,
       notes="C'est l'exercice `prPresente` du module interactif. Le faire par écrit ici, "
             "puis à l'écran : la deuxième fois va deux fois plus vite.")

    d.piege("Oublier le petit mot du verbe",
            "Je appelle Rachid.",
            "Je m'appelle Rachid.",
            "Le verbe est « s'appeler » : le petit mot devant n'est jamais "
            "facultatif. Il change avec la personne — je m'appelle, tu t'appelles, "
            "il s'appelle — et l'apostrophe le colle au verbe.",
            notes="Faire écrire les trois personnes au tableau par trois élèves "
                  "différents. C'est plus efficace qu'une explication.")

    d.pratique('Production', "Deux par deux, en tour de table",
               "Présentez-vous, puis présentez votre voisin de table au groupe.", [
        ("Votre nom et votre étage.", "Je m'appelle… J'habite au…"),
        ("Depuis quand vous habitez là.", "Je suis arrivé il y a…"),
        ("Le nom de votre voisin de table.", "Je vous présente…"),
        ("Le lien, si vous en avez un.", "C'est mon frère / mon amie / mon voisin."),
        ("La réponse de la personne présentée.", "Bonjour, enchanté / enchantée."),
    ], corrige=False,
       notes="Dix minutes, tout le monde parle deux fois. Ne corriger que les « je "
             "appelle » — le reste s'installera au défi 1.")

    d.billet(
        "Écrivez la présentation d'une personne de chez vous.",
        exemples=[
            "« Je vous présente ma sœur, Leïla. Elle habite à Longueuil. »",
            "Le lien d'abord, le prénom ensuite.",
        ],
        notes="Devoir court. Il ferme le bloc A et donne à chacun une phrase prête pour "
              "le jeu de rôle de E1.")

    return d.save(dossier)
