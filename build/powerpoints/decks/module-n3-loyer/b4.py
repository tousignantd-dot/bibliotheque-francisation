# -*- coding: utf-8 -*-
"""B4 · L'adjectif qui suit le nom.
Bloc B « Défi 1 · Lire la petite annonce » · couleur indigo · 75 min.
Source : exercice `t1adj` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='indigo',
        titre="L'adjectif qui suit le nom",
        chapeau="Chauffé, chauffée, chauffés, chauffées : un seul mot, quatre "
                "écritures. C'est le nom d'à côté qui décide, et c'est pour "
                "cela qu'on a appris les articles.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc B, et la seule de grammaire. Ouvrir en "
                  "reprenant les billets de la séance A4 : ceux qui hésitaient encore "
                  "sur « un » et « une » vont hésiter ici aussi. Le lien est direct.")

    d.objectifs([
        "accorder un adjectif avec le nom qu'il accompagne ;",
        "ajouter un e au féminin et un s au pluriel ;",
        "reconnaître les adjectifs qui ne changent pas au féminin ;",
        "entendre la différence entre compris et comprise.",
    ])

    d.regle("Un adjectif ne vit pas tout seul",
            "Il prend le genre et le nombre de son nom",
            precision="Un logement chauffé, une cuisine chauffée, des "
                      "logements chauffés, des chambres chauffées. Le mot est "
                      "le même ; c'est sa fin qui bouge. Deux gestes, toujours "
                      "dans cet ordre : un e au féminin, un s au pluriel.",
            notes="Diapositive à photographier. Écrire les quatre formes au tableau, "
                  "l'une sous l'autre, et souligner seulement la fin. Le mot ne change "
                  "pas : c'est ce qu'il faut voir.")

    d.tableau('Analyse', "Les quatre formes d'un adjectif",
              ["Le nom", "L'adjectif"],
              [["un logement", "chauffé"],
               ["une cuisine", "chauffée"],
               ["des logements", "chauffés"],
               ["des chambres", "chauffées"]],
              cle=1,
              note="Les quatre se disent exactement pareil. Seule l'écriture change.",
              notes="Diapositive à photographier. Le dire clairement : ici, on n'entend "
                    "rien. C'est une règle d'écriture, et c'est justement pour cela "
                    "qu'elle s'oublie.")

    d.tableau('Analyse', "Les adjectifs qui ne changent pas au féminin",
              ["Masculin", "Féminin"],
              [["un balcon arrière", "une porte arrière"],
               ["un sous-sol propre", "une chambre propre"],
               ["un logement libre", "une place libre"],
               ["un immeuble moderne", "une cuisine moderne"]],
              cle=0,
              note="Ils finissent déjà par un e : il n'y a rien à ajouter.",
              notes="Diapositive à photographier. C'est un soulagement pour le groupe : "
                    "une bonne partie des adjectifs du logement sont dans ce cas.")

    d.tableau('Analyse', "Deux adjectifs où le féminin s'entend",
              ["Masculin", "Féminin"],
              [["le chauffage est compris", "l'électricité est comprise"],
               ["le stationnement est inclus", "la place est incluse"],
               ["un grand salon", "une grande cuisine"],
               ["un petit balcon", "une petite chambre"]],
              cle=0,
              note="Au masculin, la dernière lettre se tait. Le e du féminin la réveille.",
              notes="Diapositive à photographier. Faire écouter la différence : "
                    "« compris » et « comprise » ne se disent pas pareil. C'est le seul "
                    "endroit du module où l'accord s'entend.")

    d.piege('Orthographe',
            "« la cuisine est chauffé »",
            "« la cuisine est chauffée »",
            "On ne l'entend pas, mais il s'écrit. Cherchez toujours le nom "
            "auquel l'adjectif se rapporte, puis regardez son article : une "
            "cuisine, donc un e.",
            notes="Donner la méthode en trois temps : quel nom ? quel article ? quelle "
                  "fin ? Faire appliquer à voix haute sur deux ou trois phrases.")

    d.piege('Orthographe',
            "« une porte arrièree »",
            "« une porte arrière »",
            "Un adjectif qui finit déjà par un e ne change pas au féminin. "
            "Propre, arrière, libre, moderne, rouge : rien à ajouter.",
            notes="Erreur de sur-application, fréquente chez les élèves qui viennent de "
                  "comprendre la règle. La signaler comme une bonne nouvelle : c'est "
                  "moins de travail.")

    d.pratique('Grammaire', "Complétez l'adjectif",
               "Chauffé ou chauffée ? Compris ou comprise ?", [
        ("Le logement est ___ : je ne paie pas le chauffage.", "chauffé"),
        ("La cuisine est ___ , elle aussi.", "chauffée"),
        ("L'électricité est ___ dans le loyer.", "comprise"),
        ("Le chauffage est ___ dans le loyer.", "compris"),
        ("Les deux chambres sont ___ , avec une porte.", "fermées"),
        ("Le balcon ___ donne sur la cour.", "arrière"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice 4 du Défi 1. Faire justifier chaque réponse par le nom, "
             "jamais par l'oreille : dans quatre cas sur six, l'oreille ne dit rien.")

    d.pratique('Répétition', "Compris ou comprise ?",
               "Écoutez la fin du mot, puis répétez.", [
        ("Le chauffage est compris.", "on n'entend pas la fin"),
        ("L'électricité est comprise.", "on entend le z"),
        ("Le stationnement est inclus.", "on n'entend pas la fin"),
        ("La place est incluse.", "on entend le z"),
        ("Le logement est grand.", "on n'entend pas le d"),
        ("La cuisine est grande.", "on entend le d"),
    ], corrige=True,
       notes="Répétition par paires : masculin, puis féminin, deux fois chaque. C'est le "
             "seul accord du module qui s'entend, et l'entendre aide à l'écrire.")

    d.billet(
        "Décrivez votre logement en trois phrases, avec trois adjectifs.",
        exemples=[
            "Mon logement est ___ .",
            "Ma cuisine est ___ . Mes chambres sont ___ .",
        ],
        notes="Devoir court. Les trois phrases obligent à passer par le masculin, le "
              "féminin et le pluriel. Corriger seulement les accords, pas le reste : "
              "c'est le point de la séance.")

    return d.save(dossier)
