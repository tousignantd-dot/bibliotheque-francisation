# -*- coding: utf-8 -*-
"""A2 · Les trois sons du nez : on, an, in
Bloc A « Je découvre » · couleur indigo · 75 min. Graphie-phonie.
Source du module : exercice `prPhon` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Les trois sons du nez : on, an, in",
        chapeau="Au téléphone, personne ne voit vos lèvres et personne ne "
                "peut vous faire répéter. Trois sons décident si votre nom, "
                "votre date et votre numéro seront écrits correctement : "
                "celui de bonjour, celui d'absence et celui de matin.",
        duree='75 minutes')

    d.titre(notes="Séance de phonétique, à faire debout la première demi-heure si la "
                  "salle le permet. Ces trois sons se travaillent avec les lèvres avant "
                  "de se travailler avec l'oreille : le geste vient d'abord, le son "
                  "suit. Prévoir une petite glace ou faire utiliser l'écran éteint d'un "
                  "téléphone.")

    d.objectifs([
        "produire les trois voyelles nasales du niveau : on, an, in ;",
        "les distinguer à l'écoute dans des mots du module ;",
        "ne plus prononcer le « n » qui les suit ;",
        "dire les nombres du numéro de téléphone sans les mélanger.",
    ], notes="Le troisième objectif est le plus tenace. Ajouter un « n » entendu au "
             "milieu du mot est le défaut le plus fréquent et le plus discret : "
             "personne ne corrige, mais on fait répéter.")

    d.regle("Le « n » ne se prononce pas",
            "Dans bonjour, absence et matin, la lettre « n » ne s'entend "
            "pas : elle fait seulement passer la voyelle par le nez.",
            precision="Si vous entendez un « n » au milieu du mot, il y en a "
                      "trop.",
            notes="Diapositive à photographier. Faire dire « bo-njour » puis "
                  "« bonjour » pour que la différence s'entende. Beaucoup d'élèves "
                  "découvrent ici qu'ils ajoutaient une consonne.")

    d.tableau('Les trois lèvres', "Un geste par son",
              ['Le son', 'Ce que font les lèvres'],
              [["on", "Elles avancent et se ferment presque, en rond."],
               ["an", "La mâchoire descend, la bouche s'ouvre large."],
               ["in", "Elles s'étirent sur les côtés, comme un sourire."]],
              note="Rond, ouvert, étiré. Trois gestes, dans cet ordre.",
              notes="Faire faire les trois gestes sans son, puis avec. Passer dans les "
                    "rangées : c'est le seul moment du module où l'on corrige une "
                    "bouche et non une phrase.")

    d.cartes("Comment ça s'écrit", "Un son, plusieurs orthographes", [
        ("Le son de bonjour",
         "on, om : bonjour, un répondeur, composer, le nom, un abandon."),
        ("Le son d'absence",
         "an, am, en, em : avant, une absence, un empêchement, un enfant."),
        ("Le son de matin",
         "in, im, ain, ein : le matin, la main, demain, cinq, impossible."),
        ("Le piège de « en »",
         "Il donne le son d'absence dans absence, mais celui de matin dans examen."),
    ], notes="La quatrième carte explique pourquoi il n'y a pas de règle courte. Ne pas "
             "chercher à en donner une : ces mots s'apprennent avec leur son, pas avec "
             "leurs lettres.")

    d.pratique('Écoute', "Quel son entendez-vous ?",
               "Dites bonjour, absence ou matin.", [
        ("bonjour", "le son de bonjour"),
        ("une absence", "le son d'absence"),
        ("le matin", "le son de matin"),
        ("un répondeur", "le son de bonjour"),
        ("un empêchement", "le son d'absence"),
        ("la main", "le son de matin"),
    ], corrige=True,
       notes="Lire chaque mot deux fois, sans le montrer. Faire répondre par le geste "
             "des lèvres plutôt qu'à voix haute : on voit d'un coup d'œil qui suit et "
             "qui devine.")

    d.pratique('Écoute · suite', "Six mots de plus",
               "Même consigne, un peu plus vite.", [
        ("un abandon", "le son de bonjour"),
        ("avant", "le son d'absence"),
        ("cinq", "le son de matin"),
        ("composer", "le son de bonjour"),
        ("un enfant", "le son d'absence"),
        ("impossible", "le son de matin"),
    ], corrige=True,
       notes="« Cinq » et « impossible » sont ceux qu'on manque : le son de matin y est "
             "court et suivi d'une consonne. Les redire seuls, puis dans « cinq cent "
             "cinquante-cinq ».")

    d.tableau('Trois mots, une consonne', "La série qui sépare tout",
              ['Le son', 'La série'],
              [["on", "bon  ·  son  ·  ton  ·  long"],
               ["an", "banc  ·  sans  ·  temps  ·  lent"],
               ["in", "bain  ·  saint  ·  teint  ·  lin"]],
              cle=1,
              notes="Faire lire les colonnes de haut en bas, puis les lignes de gauche à "
                    "droite. C'est en lisant les lignes que la différence s'entend : "
                    "bon, banc, bain, trois fois de suite.")

    d.regle("Les nombres passent tous par le nez",
            "un, cinq, onze, vingt, cent, cinquante : cinq des six portent "
            "une voyelle nasale.",
            precision="Un numéro de téléphone mal nasalisé est un numéro "
                      "qu'on ne rappellera pas.",
            notes="Faire dire le numéro du centre, 450 555-0180, par groupes de trois "
                  "et quatre chiffres, lentement. Puis le faire écrire par le voisin "
                  "sous la dictée : c'est le vrai test.")

    d.piege("Ajouter un « n » qu'on entend",
            "Bonn-jour, madame. Je serai ab-senn-ce demain.",
            "Bonjour, madame. Je serai absente demain.",
            "La lettre « n » n'est pas une consonne ici : elle indique que la "
            "voyelle sort par le nez. Un « n » entendu au milieu fait sonner le "
            "français comme une autre langue, et c'est le défaut qui résiste le "
            "plus longtemps.",
            notes="Exagérer les deux versions au tableau. Puis proposer un exercice "
                  "d'une semaine : bouche fermée sur « on », mâchoire tombée sur "
                  "« an », lèvres étirées sur « in ». Après, on relâche.")

    d.pratique('Répétition', "Six phrases du module",
               "À dire à voix haute, deux fois chacune.", [
        ("Bonjour, ici Nourhane Ouazzani, groupe 6.", "le son de bonjour, deux fois"),
        ("Je vous appelle pour signaler mon absence.", "le son d'absence, deux fois"),
        ("Je serai en classe demain matin.", "le son de matin, deux fois"),
        ("Composez le poste deux cent vingt-quatre.", "les trois sons dans un nombre"),
        ("J'ai un empêchement ce matin, mais je viendrai demain.", "ouvert, étiré, étiré"),
        ("Un abandon annoncé n'est pas un échec.", "rond au début, ouvert à la fin"),
    ], notes="Faire enregistrer la deuxième et la sixième avec le téléphone de l'élève, "
             "puis réécouter. S'entendre soi-même fait plus que dix corrections.")

    d.billet(
        "Écrivez trois mots du module : un avec le son de bonjour, un avec "
        "celui d'absence, un avec celui de matin.",
        exemples=[
            "Des mots vus aujourd'hui, pas des mots inventés.",
            "Soulignez les lettres qui donnent le son.",
        ],
        notes="Ramasser les billets. Ceux qui écrivent trois mots du même son n'ont pas "
              "encore la distinction : les revoir individuellement au début de A3.")

    return d.save(dossier)
