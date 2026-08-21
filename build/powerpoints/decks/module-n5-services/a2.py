# -*- coding: utf-8 -*-
"""A2 · Les trois voyelles nasales.
Bloc A « Je découvre » · couleur indigo · 75 min. Graphie-phonie.
Source : exercice `prPhon` et sa mini-leçon.

Les sons sont nommés par leurs lettres et un mot repère — jamais en alphabet
phonétique : Verdana n'a pas ces caractères et ils partiraient en carrés vides
chez l'enseignante. Le module interactif, lui, affiche bien les symboles.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Les trois voyelles nasales",
        chapeau="Au téléphone, personne ne voit votre bouche. Trois sons "
                "portent tout ce dont un préposé a besoin : votre nom, "
                "votre adresse, le moment. Ils s'apprennent en une séance.",
        duree='75 minutes')

    d.titre(notes="Séance de phonétique. Prévoir un miroir de poche, ou faire travailler "
                  "les élèves deux par deux face à face : la position des lèvres se "
                  "corrige à l'œil bien plus vite qu'à l'oreille.")

    d.objectifs([
        "distinguer les sons AN, ON et IN à l'écoute ;",
        "produire chacun avec la bonne position des lèvres ;",
        "reconnaître les lettres qui donnent chaque son ;",
        "savoir quand la nasale disparaît devant une voyelle.",
    ])

    d.declencheur(
        'Écoute', "Trois mots. Est-ce que vous entendez la même chose ?",
        pistes=[
            "attente — nom — matin",
            "Lequel a les lèvres en rond ?",
            "Lequel a les lèvres étirées ?",
            "Est-ce que votre langue en a autant ?",
        ],
        notes="Dire les trois mots lentement, deux fois, sans les écrire. Beaucoup "
              "d'élèves n'entendront d'abord aucune différence : c'est normal et il faut "
              "le dire tout de suite, sinon ils croient avoir un problème d'oreille.")

    d.regle("Une voyelle nasale, c'est de l'air qui passe par le nez",
            "Par le nez et par la bouche en même temps — et la consonne n ne se dit pas.",
            precision="« nom » est une seule voyelle, pas « no-mme ». La lettre n a fondu "
                      "dans la voyelle : elle ne s'entend plus comme consonne. C'est ce "
                      "qui déroute les élèves dont la langue prononce toutes les lettres.",
            notes="Diapositive à photographier. Faire pincer le nez et redire « nom » : "
                  "le son change, ce qui prouve que l'air y passait.")

    d.tableau('Les trois sons', "Position, lettres, exemples",
              ['Le son', 'La bouche', 'On écrit', 'Dans ce module'],
              [["le son AN, comme dans attente", "grande ouverte", "an am en em",
                "attente · résidence · en vigueur"],
               ["le son ON, comme dans nom", "lèvres en rond", "on om",
                "nom · réponse · information"],
               ["le son IN, comme dans matin", "lèvres étirées", "in im ain ein",
                "matin · certain · plein"]],
              cle=0,
              note="Après un i, les lettres « en » se lisent IN : bien, rien, combien.",
              notes="Diapositive à photographier. C'est le tableau de référence de toute "
                    "la séance ; le laisser affiché pendant les exercices.")

    d.cartes("Comment corriger un élève", "Quatre gestes qui marchent", [
        ("Pour le son ON",
         "« Arrondissez les lèvres comme pour siffler. » Le geste vaut mieux que l'explication."),
        ("Pour le son IN",
         "« Étirez comme au début d'un sourire. » Faire tenir la position avant de dire le mot."),
        ("Pour le son AN",
         "« Ouvrez comme chez le médecin. » La mâchoire descend franchement."),
        ("Toujours",
         "Faire d'abord la position sans son, puis ajouter la voix. Jamais l'inverse."),
    ], notes="La dernière carte est celle qui change tout : un élève qui cherche le son "
             "en même temps que la position n'obtient ni l'un ni l'autre.")

    d.pratique('Discrimination', "Quel son entendez-vous ?",
               "Dites AN, ON ou IN pour chaque mot.", [
        ("attente", "AN"),
        ("nom", "ON"),
        ("matin", "IN"),
        ("résidence", "AN"),
        ("réponse", "ON"),
        ("certain", "IN"),
        ("renseignement", "AN"),
        ("information", "ON"),
        ("plein", "IN"),
    ], corrige=True,
       notes="Dire chaque mot deux fois. Ne pas afficher l'orthographe pendant l'écoute : "
             "elle donne la réponse et vide l'exercice de son intérêt. Dans le module, le "
             "même exercice porte les symboles de l'alphabet phonétique.")

    d.regle("Devant une voyelle, la nasale disparaît",
            "« une année » se dit a-nnée, et non an-née.",
            precision="Quand le n ou le m est suivi d'une voyelle, il redevient une "
                      "consonne ordinaire et la voyelle d'avant se dénasalise : a-nnée, "
                      "bo-nne, ma-ti-née. C'est la règle qui manque le plus souvent aux "
                      "élèves qui nasalisent partout.",
            notes="Diapositive à photographier. Faire opposer : « an » et « année », "
                  "« bon » et « bonne », « certain » et « certaine ».")

    d.piege("Prononcer la consonne finale",
            "nom dit « nomme », matin dit « matine »",
            "Une seule voyelle, et rien après.",
            "La consonne nasale a fondu dans la voyelle. La redire annule le son et "
            "transforme souvent le mot en un autre : « certain » devient « certaine », "
            "donc féminin, ce qui n'était pas voulu.",
            notes="Faire l'opposition masculin/féminin au tableau : c'est le seul endroit "
                  "où l'erreur de nasale change vraiment le sens, et ça frappe.")

    d.pratique('Production', "Lisez à voix haute",
               "Une phrase par personne, en surveillant vos lèvres.", [
        ("Le temps d'attente est d'environ quatre minutes.", "le son AN, trois fois"),
        ("Je vous donne mon nom et mon code postal.", "le son ON, trois fois"),
        ("Le camion passe le mardi matin.", "le son ON, puis le son IN"),
        ("J'aimerais un renseignement sur les tarifs en vigueur.", "le son AN partout"),
        ("Je n'ai pas eu de réponse, et c'est certain.", "le son ON, puis le son IN"),
        ("Quatre visites gratuites par année.", "attention : a-nnée, pas de nasale"),
    ], corrige=False,
       notes="La dernière phrase est le piège de la séance. La garder pour la fin et "
             "laisser le groupe se corriger lui-même.")

    d.billet(
        "Enregistrez-vous en disant votre nom et votre adresse, comme au téléphone.",
        exemples=[
            "Réécoutez-vous : est-ce que vos lèvres étaient rondes sur « nom » ?",
            "Recommencez jusqu'à ce que vous soyez satisfait de la première phrase.",
        ],
        notes="Devoir court mais exigeant. Il prépare directement l'appel du défi 1, où "
              "donner son nom et son adresse est la première épreuve réelle.")

    return d.save(dossier)
