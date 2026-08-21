# -*- coding: utf-8 -*-
"""C1 · À gauche ou à droite ?
Bloc C « Défi 2 · Demander son chemin » · couleur acier · 75 min.
Source : dialogue `t2`, exercices `t2vf` et `t2prep`, mini-leçon `t2prep`.

L'étage est acquis ; reste le corridor. Cinq expressions suffisent à situer
n'importe quelle porte du bâtiment : à côté de, en face de, au bout du, au
milieu du, entre… et…

Ce sont des prépositions et des groupes prépositionnels, le savoir le plus
fourni du niveau 2 - dix points à lui seul. On en prend cinq, celles qui
servent dans un corridor, et on les fait toutes passer par le geste avant de
les faire passer par l'écrit.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-couloirs/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="À gauche ou à droite ?",
        chapeau="Comprendre une indication dans un corridor et dire "
                "exactement où se trouve une porte.",
        duree='75 minutes')

    d.titre(notes="Troisième bloc. Séance très gestuelle : chaque expression se dit "
                  "avec la main avant de s'écrire.")

    d.objectifs([
        "comprendre à gauche, à droite et tout droit ;",
        "situer une porte avec à côté de et en face de ;",
        "situer une porte avec au bout du et au milieu du ;",
        "redire une indication pour la vérifier.",
    ])

    d.declencheur(
        'Observation', "Comment est-ce qu'on décrit cet endroit ?",
        image=IMG + 'salle-casiers.jpg',
        pistes=[
            "Qu'est-ce qu'il y a le long du mur ?",
            "Est-ce que c'est au début ou au bout du corridor ?",
            "Qu'est-ce qu'il y a en face ?",
            "Comment vous diriez à quelqu'un où c'est ?",
        ],
        notes="Laisser essayer les formules approximatives avant de donner les bonnes. "
              "Noter au tableau ce que le groupe produit : on y reviendra à la fin.")

    d.dialogue('Dialogue', "Soraya cherche les toilettes", [
        ("SORAYA", "Excusez-moi, où sont les toilettes ?", True),
        ("GILLES", "Au bout du corridor, en face de l'ascenseur.", True),
        ("SORAYA", "À gauche ou à droite ?", True),
        ("GILLES", "À droite. Tout droit, puis à droite.", True),
        ("SORAYA", "Merci. Et la salle des casiers ?", True),
        ("GILLES", "Au rez-de-chaussée, à côté de la cafétéria.", True),
    ], consigne="Écoutez deux fois, puis montrez la direction avec la main.",
       notes="Faire écouter les yeux fermés la première fois, puis avec le geste la "
             "seconde. La troisième réplique est la clé : Soraya n'a pas tout compris, "
             "et elle le dit en une question de quatre mots.")

    d.tableau('Analyse', "Cinq façons de dire où c'est",
              ["On dit", "Ça veut dire"],
              [["à côté de la cafétéria", "la porte voisine, du même côté"],
               ["en face de l'ascenseur", "de l'autre côté du corridor"],
               ["au bout du corridor", "tout au fond, la dernière porte"],
               ["au milieu du corridor", "ni au début, ni au fond"],
               ["entre l'escalier et l'ascenseur", "avec un repère de chaque côté"]],
              cle=1,
              note="On dit toujours « du » corridor : « de le corridor » n'existe pas.",
              notes="Diapositive à photographier. Dessiner le corridor du vrai centre au "
                    "tableau et placer les cinq expressions dessus, une par une.")

    d.regle("À côté, ou en face ?",
            "La différence tient à un seul geste.",
            precision="<b>À côté</b>, c'est le même côté du corridor : les deux portes "
                      "se touchent. <b>En face</b>, c'est l'autre côté : il faut "
                      "traverser. Montrez-le avec les deux mains, et la classe entière "
                      "comprend en trois secondes.",
            notes="Diapositive à photographier. Le geste d'abord, le mot ensuite. Faire "
                  "refaire le geste par tout le groupe, deux fois.")

    d.piege('Le piège du jour',
            "« à côté la cafétéria »",
            "à côté de la cafétéria",
            "Le petit mot <b>de</b> n'est pas facultatif : sans lui, la phrase s'arrête "
            "au milieu et l'interlocuteur ne sait pas de quoi on parle. Même chose pour "
            "« en face <b>de</b> l'ascenseur ».",
            notes="Faire entendre les deux versions. Puis faire répéter cinq phrases "
                  "avec le « de » bien détaché.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Les toilettes sont au bout du corridor.", "vrai"),
        ("Il faut tourner à gauche.", "faux - à droite"),
        ("La salle des casiers est au rez-de-chaussée.", "vrai"),
        ("La salle des casiers est à côté de la cafétéria.", "vrai"),
        ("La salle des casiers ferme le midi.", "faux - elle est ouverte toute la journée"),
    ], corrige=True, cols=1,
       notes="Cinq énoncés. Les faire d'abord à l'oral, en groupe, puis à l'écrit.")

    d.cartes("Trois gestes à ne pas confondre", "À faire en même temps qu'on parle", [
        ("À droite",
         "Du côté de la main droite. On tourne."),
        ("À gauche",
         "Du côté de la main gauche. On tourne aussi."),
        ("Tout droit",
         "Devant soi, sans tourner du tout."),
    ], cols=3, notes="« À droite » et « tout droit » se ressemblent et se confondent tout "
                     "le temps. Le geste est la seule chose qui les sépare vraiment "
                     "pour un débutant.")

    d.pratique('Pratique · dans le corridor', "Situez cinq portes",
               "Debout, dans le vrai corridor du centre.", [
        ("Étape 1", "Le groupe se place au milieu du corridor."),
        ("Étape 2", "Chacun situe une porte avec à côté de ou en face de."),
        ("Étape 3", "Chacun situe une porte avec au bout du corridor."),
        ("Étape 4", "Chacun dit où est sa propre classe, avec deux repères."),
    ], cols=1,
       notes="Vingt minutes hors de la classe. Prévenir le secrétariat. L'étape 4 est "
             "l'évaluation formative de la séance : elle se note d'un coup d'œil.")

    d.billet(
        "Écrivez où sont les toilettes de votre étage, avec deux repères.",
        exemples=[
            "Les toilettes sont au bout du corridor.",
            "Elles sont en face de l'ascenseur.",
            "Elles sont à côté de l'escalier.",
        ],
        notes="Devoir court. Vérifier le « de » : c'est le piège de la séance, et il "
              "se corrige en une seconde.")

    return d.save(dossier)
