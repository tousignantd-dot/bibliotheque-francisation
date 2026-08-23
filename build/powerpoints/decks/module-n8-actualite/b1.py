# -*- coding: utf-8 -*-
"""B1 · Le même conseil, raconté deux fois
Bloc B « Défi 1 · Deux versions du même fait » · couleur acier · 75 min.
Source : reportage `t1`, exercice `t11` et son bandeau « Comparer deux
comptes rendus d'un même fait ».
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n8-actualite' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Deux personnes, une soirée, deux récits",
        chapeau="Wilfrid Chamberland et Régine Sauvé étaient dans la même "
                "salle, le même lundi. Ils ne racontent pas la même chose et "
                "ils ne se contredisent jamais. C'est ça qu'il faut "
                "apprendre à entendre.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc B. Annoncer tout de suite la difficulté du défi : "
                  "ici, personne ne ment. Les élèves cherchent spontanément qui a "
                  "tort, et il n'y a pas de réponse à cette question-là.")

    d.objectifs([
        "suivre un reportage radio à trois voix, sans transcription ;",
        "distinguer ce que chaque personne choisit de raconter ;",
        "repérer un désaccord chiffré et dire sur quoi il porte vraiment ;",
        "nommer la source d'un renseignement entendu.",
    ], notes="Le troisième objectif est le coeur de la séance et il revient dans les "
             "trois suivantes. Le quatrième est préparé ici et travaillé en B4.")

    d.declencheur(
        'Discussion', "Deux amis vous racontent la même soirée. Que faites-vous ?",
        image=IMG + 'studio-radio.jpg',
        pistes=[
            "Est-ce que vous cherchez lequel des deux se trompe ?",
            "Est-ce qu'il est possible que les deux disent vrai ?",
            "Qu'est-ce que chacun a jugé important de garder ?",
            "Qu'est-ce que vous apprenez du récit, et qu'est-ce que vous apprenez de celui qui raconte ?",
        ],
        notes="Laisser venir les réponses. La quatrième question est celle qui ouvre "
              "le module : un récit renseigne toujours deux fois, sur le fait et sur "
              "la personne qui le rapporte.")

    d.dialogue('Reportage 1 de 4', "Ce que dit l'animateur au départ", [
        ("GRÉGOIRE", "Retour ce matin sur la séance de lundi soir à l'hôtel de ville de Rivière-aux-Cèdres.", True),
        ("GRÉGOIRE", "Le règlement numéro douze cent quatre a été adopté par quatre voix contre trois. Il autorise la cession du boisé Sainte-Perpétue à Habitations Verchères-Nord pour un dollar symbolique.", True),
        ("GRÉGOIRE", "En échange : quarante-cinq logements à loyer abordable sur les cent quatre-vingts prévus.", True),
        ("GRÉGOIRE", "Nous avons demandé à deux personnes de nous raconter la même soirée.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire relever les cinq chiffres de ce début : quatre contre trois, un "
             "dollar, quarante-cinq, cent quatre-vingts, douze cent quatre. Aucun des "
             "deux invités ne les contestera : c'est le socle commun.")

    d.dialogue('Reportage 2 de 4', "La même minute, deux fois", [
        ("WILFRID", "Il s'est passé qu'une ville de vingt-quatre mille habitants s'est donné quarante-cinq logements abordables sans dépenser un sou.", True),
        ("WILFRID", "Le terrain ne rapportait rien, il coûtait onze mille dollars par année en entretien, et il va maintenant produire du logement et des taxes.", True),
        ("RÉGINE", "Il s'est passé qu'un conseil a cédé un bien public pour un dollar, quatre jours après avoir reçu l'évaluation, et sans avoir regardé le seul autre terrain disponible.", True),
        ("RÉGINE", "Le vote a été pris à vingt-deux heures cinquante, devant onze personnes.", True),
    ], notes="Le passage central de la séance. Faire chercher une seule phrase de "
             "l'un que l'autre pourrait déclarer fausse : il n'y en a pas. Puis "
             "demander ce que chacun a laissé de côté.")

    d.dialogue('Reportage 3 de 4', "Le terrain derrière l'aréna", [
        ("GRÉGOIRE", "Monsieur Chamberland, le terrain derrière l'aréna, il existe ?", True),
        ("WILFRID", "Il existe, et il appartient à la Ville, c'est exact. Mais il est zoné industriel et il faudrait vingt et un mois pour le rezoner.", True),
        ("RÉGINE", "Vingt et un mois, c'est le délai que la Ville avance. Elle ne l'a écrit nulle part. Et c'est une estimation du service de l'urbanisme, pas une règle de loi.", True),
        ("WILFRID", "C'est une estimation, oui. Ça reste vingt et un mois pendant lesquels personne ne se loge.", True),
    ], notes="Deux gestes à faire remarquer : Wilfrid concède le fait avant "
             "d'objecter, et Régine ne nie pas le chiffre, elle en discute le statut. "
             "Ce sont les deux gestes que le module fait travailler jusqu'à la fin.")

    d.dialogue('Reportage 4 de 4', "Quatre-vingt-dix ou trois cent quarante-deux", [
        ("WILFRID", "Le promoteur parle de quatre-vingt-dix arbres sur les quatre hectares boisés, avec replantation à deux pour un.", True),
        ("RÉGINE", "Le comité en a compté trois cent quarante-deux, un samedi, à six personnes. Nous avons remis nos feuilles à la Ville.", True),
        ("WILFRID", "On ne compte peut-être pas la même chose. Un arbre de quinze centimètres de diamètre, est-ce que c'est un arbre ?", True),
        ("GRÉGOIRE", "Vous voyez, chers auditeurs : le désaccord n'est pas sur le chiffre, il est sur la définition. Retenez ça, c'est souvent le cas.", True),
    ], notes="La dernière réplique est la phrase à retenir de tout le bloc. L'écrire "
             "au tableau et l'y laisser jusqu'à la fin de la séance.")

    d.regle("Le désaccord n'est pas toujours là où on le voit",
            "Quatre-vingt-dix contre trois cent quarante-deux : l'écart a "
            "l'air d'un mensonge. Il vient d'une définition. À partir de quel "
            "diamètre un jeune érable devient-il un arbre ?",
            precision="Avant de choisir entre deux chiffres qui s'opposent, cherchez "
                      "ce que chacun a compté. Très souvent, les deux comptages sont "
                      "exacts et portent sur deux ensembles différents. La question "
                      "utile n'est pas « qui ment ? », c'est « qu'avez-vous compté ? ».",
            notes="Diapositive à photographier. Donner un exemple hors du dossier : "
                  "deux personnes comptent les logements d'un immeuble, l'une compte "
                  "les portes, l'autre les baux.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le reportage.", [
        ("Le terrain est cédé au promoteur pour un dollar symbolique.", "vrai"),
        ("Régine Sauvé conteste le nombre de logements abordables prévus.", "faux - elle conteste la façon de décider"),
        ("Le vote a été pris devant une salle comble.", "faux - devant onze personnes"),
        ("Le terrain derrière l'aréna appartient bien à la Ville.", "vrai"),
        ("Le délai de vingt et un mois est inscrit dans une loi.", "faux - c'est une estimation de l'urbanisme"),
        ("Le promoteur et le comité donnent le même nombre d'arbres abattus.", "faux - quatre-vingt-dix contre trois cent quarante-deux"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la réplique entendue, pas par une "
             "impression. Le deuxième énoncé est celui qui piège : Régine est contre "
             "l'endroit et contre la manière, jamais contre le logement abordable.")

    d.tableau('Analyse', "Ce que chacun a gardé de la même soirée",
              ['Wilfrid Chamberland', 'Régine Sauvé'],
              [["quarante-cinq logements abordables",
                "un bien public cédé pour un dollar"],
               ["onze mille dollars d'entretien par année",
                "quatre jours entre l'évaluation et le vote"],
               ["un terrain qui produira des taxes",
                "un vote à vingt-deux heures cinquante devant onze personnes"]],
              cle=0,
              note="Aucune des six phrases n'est fausse. Ce que chacun a choisi de dire est déjà une prise de position.",
              notes="Diapositive à photographier. Faire ajouter par le groupe une "
                    "septième ligne à partir de ce qu'ils ont retenu : les propositions "
                    "se rangent presque toujours d'un côté ou de l'autre sans hésiter.")

    d.billet(
        "Racontez en trois phrases une décision prise chez vous ou au travail, comme si vous étiez pour.",
        exemples=[
            "Puis les trois mêmes phrases comme si vous étiez contre.",
            "Interdiction d'écrire quoi que ce soit de faux dans les deux versions.",
        ],
        notes="Devoir. La contrainte est tout l'exercice : dire deux choses opposées "
              "sans mentir une seule fois. Deux ou trois billets seront lus en début "
              "de B2, avant les articles.")

    return d.save(dossier)
