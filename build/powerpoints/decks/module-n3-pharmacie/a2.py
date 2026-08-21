# -*- coding: utf-8 -*-
"""A2 · Le son AN et le son ON.
Bloc A « Je découvre » · couleur indigo (graphie-phonie) · 60 min.
Source : mini-leçon `prPhon`, exercice `prPhon` (cartes à écouter).

Les sons sont nommés par leurs lettres et par un mot repère — « le son AN,
comme dans ordonnance ». L'alphabet phonétique reste dans le module
interactif : sur une diapositive projetée, il ne servirait à personne.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre='Le son AN et le son ON',
        chapeau="Ordonnance, pendant, médicament ; comprimé, comptoir, mon "
                "nom. Deux sons qui passent par le nez, et qui séparent "
                "« sans » de « son ».",
        duree='60 minutes')

    d.titre(notes="Séance de phonétique. Prévoir les haut-parleurs : tout se joue à "
                  "l'oreille. Les deux mots repères sont les deux mots les plus "
                  "fréquents du module — on ne pouvait pas mieux tomber.")

    d.objectifs([
        "entendre la différence entre le son AN et le son ON ;",
        "savoir que ces sons passent en partie par le nez ;",
        "reconnaître les deux écritures du son AN : an et en ;",
        "prononcer les mots du module sans les confondre.",
    ])

    d.declencheur(
        'Écoute', "« Sans ordonnance » ou « son médicament » ?",
        pistes=[
            "Est-ce que ces deux phrases se ressemblent ?",
            "Qu'est-ce qui change : la bouche, la langue, ou le nez ?",
            "Dans votre langue, est-ce qu'il y a des sons qui passent par le nez ?",
        ],
        notes="Dire les deux phrases trois fois chacune, sans les écrire. Faire lever la "
              "main quand le groupe entend « sans ». Écrire seulement après.")

    d.regle("Le son AN",
            "« une ordonnance »",
            precision="La bouche est bien ouverte, la langue à plat, et l'air "
                      "passe en partie par le nez. Il s'écrit de deux façons : "
                      "an comme dans « pendant », et en comme dans "
                      "« médicament ». Deux écritures, un seul son.",
            notes="Diapositive à photographier. Faire répéter « ordonnance » lentement, "
                  "puis « pendant », « avant », « médicament ».")

    d.regle("Le son ON",
            "« un comprimé »",
            precision="La bouche est en rond, presque fermée, et l'air passe "
                      "aussi par le nez. Il s'écrit on ou om. Devant un p ou un "
                      "b, c'est toujours om : comprimé, comptoir.",
            notes="Diapositive à photographier. Le passage de « ordonnance » à "
                  "« comprimé » se voit sur les lèvres : les faire regarder de face.")

    d.tableau('Analyse', "Trois paires qui changent le sens",
              ["On entend AN", "On entend ON"],
              [["dans le sac", "un don de sang"],
               ["sans ordonnance", "son médicament"],
               ["combien de temps", "un sandwich au thon"],
               ["pendant sept jours", "on prend le comprimé"]],
              cle=0,
              note="Dans le doute, dis le mot à côté de « ordonnance », puis de « comprimé ».",
              notes="Faire lire chaque ligne à deux voix : un élève la colonne de gauche, "
                    "un autre celle de droite. Le contraste s'entend mieux ainsi.")

    d.piege('Prononciation',
            "« ordonnonce »",
            "« ordonnance »",
            "Remplacer le son AN par le son ON est le piège le plus fréquent chez les "
            "débutants. Le remède est mécanique : ouvrir grand la bouche. Le son AN "
            "demande de la place ; le son ON n'en demande presque pas.",
            notes="Faire exagérer l'ouverture de la bouche une première fois, puis "
                  "revenir à une prononciation normale. L'exagération sert de repère.")

    d.pratique('Discrimination', "AN ou ON ?",
               "Écoutez chaque mot, puis dites quel son vous entendez.", [
        ("une ordonnance", "AN"),
        ("un comprimé", "ON"),
        ("pendant sept jours", "AN"),
        ("le comptoir", "ON"),
        ("un médicament", "AN — écrit avec e-n"),
        ("mon nom", "ON, deux fois"),
        ("avant le repas", "AN"),
        ("ils sont prêts", "ON"),
    ], corrige=True,
       notes="Les huit items sont ceux de l'exercice interactif. Les dire deux fois "
             "chacun, à vitesse normale la seconde fois.")

    d.pratique('Production', "À dire à voix haute",
               "Chaque phrase contient les deux sons.", [
        ("Un comprimé pendant sept jours.", "ON puis AN"),
        ("Sans ordonnance, on ne peut pas.", "AN, AN, ON"),
        ("Mon nom est écrit sur le flacon.", "ON trois fois"),
        ("Combien de temps est-ce que ça prend ?", "ON puis AN"),
    ], corrige=False,
       notes="Faire dire chaque phrase par trois élèves différents. Corriger seulement "
             "les deux sons de la séance, rien d'autre.")

    d.billet(
        "Écrivez trois mots du module avec le son AN et trois avec le son ON.",
        exemples=[
            "Cherchez dans les mots de la séance A1.",
            "Soulignez les lettres qui font le son.",
        ],
        notes="Devoir court. Il sert de vérification : un élève qui range « comptoir » "
              "dans la colonne AN n'a pas encore entendu la différence.")

    return d.save(dossier)
