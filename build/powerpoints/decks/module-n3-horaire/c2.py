# -*- coding: utf-8 -*-
"""C2 · Pouvoir, devoir, falloir.
Bloc C « Défi 2 · Est-ce que je peux vous demander ? » · couleur ambre · 60 min.
Source : exercice `t2modal`, mini-leçon `t2modal`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Pouvoir, devoir, falloir",
        chapeau="« Je peux partir à midi », « je dois partir à midi », « il "
                "faut partir à midi » : trois phrases, trois situations "
                "complètement différentes. Un chef d'équipe entend la "
                "différence tout de suite.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture, la plus grammaticale du module. Partir des demandes "
                  "ramassées au billet de C1 : plusieurs contiendront déjà l'un des trois "
                  "verbes, correctement ou non.")

    d.objectifs([
        "employer « pouvoir » pour la permission et la capacité ;",
        "employer « devoir » pour l'obligation qui vient de quelqu'un ;",
        "employer « il faut » pour la règle de la place ;",
        "laisser le verbe qui suit à l'infinitif.",
    ])

    d.tableau('Analyse', "Trois verbes, trois sens",
              ["Le verbe", "Ce qu'il dit"],
              [["pouvoir", "la permission, ou la capacité : « je peux partir ? »"],
               ["devoir", "l'obligation qui vient de ma vie : « je dois y aller »"],
               ["falloir", "la règle de la place : « il faut aviser »"]],
              cle=1,
              note="« Il faut » ne nomme personne : c'est la règle pour "
                   "tout le monde. Ce verbe n'existe qu'avec « il ».",
              notes="Diapo à photographier. La distinction devoir / falloir est celle qui "
                    "manque le plus : « je dois » explique ma situation, « il faut » "
                    "rappelle la règle. Les deux se disent au travail, jamais au même "
                    "moment.")

    d.regle("Le verbe qui suit ne change jamais",
            "Je peux partir. Je dois finir. Il faut aviser.",
            precision="Après ces trois-là, l'autre verbe reste à "
                      "l'infinitif — la forme du dictionnaire. On ne dit "
                      "jamais « je peux je pars ».",
            notes="Diapo à photographier. C'est la règle la plus rentable du module : "
                  "elle s'applique aussi à « aller », « vouloir » et « savoir », donc "
                  "à presque toutes les phrases utiles au travail.")

    d.pratique('Écriture', "Peux, pouvez, dois, doit ou faut",
               "Complétez chaque phrase.", [
        ("Est-ce que je ___ vous parler deux minutes ?", "peux"),
        ("Monsieur Roy, est-ce que vous ___ m'aider ?", "pouvez"),
        ("Jeudi, je ___ aller à la clinique avec mon garçon.", "dois"),
        ("Il ___ aviser le chef d'équipe trois jours avant.", "faut"),
        ("Miguel ___ me remplacer jeudi matin.", "peut — ou : doit"),
        ("Chaque employé ___ poinçonner en arrivant.", "doit"),
    ], corrige=True,
       notes="C'est l'exercice `t2modal` du module interactif, mot pour mot. La cinquième "
             "ligne accepte deux réponses, et la différence vaut d'être discutée : "
             "« peut » dit qu'il est libre, « doit » dit que c'est décidé.")

    d.regle("On dit vous au chef d'équipe",
            "Est-ce que vous pouvez m'aider, monsieur Roy ?",
            precision="Au travail, on vouvoie la personne responsable et on "
                      "tutoie souvent les collègues. Miguel tutoie Fabiola ; "
                      "tous deux vouvoient Gaétan. Dans le doute, on "
                      "vouvoie : c'est l'erreur qui ne coûte rien.",
            notes="Diapo à photographier. Ne pas en faire une règle absolue — beaucoup de "
                  "milieux tutoient tout le monde. Ce qui compte, c'est de savoir "
                  "observer ce que font les autres pendant la première semaine.")

    d.pratique('Écriture', "Permission, obligation ou règle ?",
               "Écrivez la phrase avec le bon verbe.", [
        ("Vous demandez à sortir plus tôt vendredi.", "Est-ce que je peux partir à midi vendredi ?"),
        ("Vous expliquez pourquoi : votre fille est malade.", "Je dois aller la chercher à l'école."),
        ("Vous rappelez la règle de la place à un nouveau.", "Il faut poinçonner avant d'entrer."),
        ("Vous demandez de l'aide pour porter des boîtes.", "Est-ce que vous pouvez m'aider ?"),
        ("Vous dites qu'un collègue est libre jeudi.", "Miguel peut me remplacer."),
    ], corrige=True, cols=1,
       notes="Corriger le choix du verbe d'abord, la forme ensuite. Un élève qui écrit "
             "« il faut » là où il devait dire « je dois » a un problème de sens, pas de "
             "conjugaison.")

    d.piege("Dire « je veux » à la place de « je peux »",
            "Je veux partir à midi.",
            "Est-ce que je peux partir à midi ?",
            "« Je veux » annonce une décision déjà prise : devant un chef "
            "d'équipe, il sonne comme un ordre. Les deux mots se ressemblent "
            "à l'oreille, et l'erreur coûte cher pour une seule lettre.",
            notes="Faire dire la paire « je veux / je peux » à voix haute, plusieurs fois. "
                  "La différence est une voyelle, et elle change tout le rapport entre "
                  "les deux personnes.")

    d.billet(
        "Réécrivez votre demande de C1 avec le bon verbe.",
        exemples=[
            "La demande avec « est-ce que je peux », la raison avec « je dois ».",
            "« Est-ce que je peux partir à midi ? Je dois aller à la clinique. »",
        ],
        notes="Devoir court. Deux phrases, dans cet ordre : la demande, puis la raison. "
              "C'est la structure exacte de la production orale de E1.")

    return d.save(dossier)
