# -*- coding: utf-8 -*-
"""A2 · Le son « é » et le son « è »
Bloc A « Je découvre » · couleur indigo · 75 min. Graphie-phonie.
Source du module : exercice `prPhon` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Le son « é » et le son « è »",
        chapeau="Deux façons de dire la lettre « e », et tout le vocabulaire "
                "du bureau les porte : un relevé, le secrétariat, annoncer "
                "d'un côté ; une conseillère, une pièce, après de l'autre. "
                "Surtout, c'est le seul son qui sépare « je voudrais » de "
                "« je voudrai ».",
        duree='75 minutes')

    d.titre(notes="Séance de prononciation, la seule du module. Elle vient tôt exprès : "
                  "les mots travaillés ici reviennent dans les trois défis, et la "
                  "distinction « je voudrais » contre « je voudrai » sert dès la séance "
                  "B2. Prévoir de faire répéter beaucoup, et à voix haute.")

    d.objectifs([
        "entendre la différence entre le « é » fermé et le « è » ouvert ;",
        "produire les deux sons en sentant la mâchoire descendre sur le second ;",
        "reconnaître les orthographes qui donnent l'un ou l'autre ;",
        "dire « je voudrais » avec un « è », et non « je voudrai ».",
    ], notes="Le quatrième objectif est le seul qui change le sens d'une phrase. Le "
             "garder pour la fin de la séance, mais l'annoncer dès le début : c'est ce "
             "qui donne envie de travailler les trois premiers.")

    d.regle("La mâchoire, et rien d'autre",
            "Sur « é », la mâchoire reste haute et le son est bref. Sur "
            "« è », elle descend d'un doigt et le son dure plus longtemps.",
            precision="Posez deux doigts sous le menton et dites « les, lait ». "
                      "Vous sentez la mâchoire descendre sur le second.",
            notes="Diapositive à photographier. Le truc des deux doigts sous le menton "
                  "donne le résultat en une tentative chez la plupart des élèves : la "
                  "différence devient tactile au lieu d'être seulement auditive.")

    d.cartes("Quatre paires", "Un seul son les sépare", [
        ("les · lait",
         "Les dates de l'avis. Un café au lait."),
        ("fée · fait",
         "Un conte de fées. C'est déjà fait."),
        ("thé · taie",
         "Une tasse de thé. Une taie d'oreiller."),
        ("je voudrai · je voudrais",
         "Le premier est un futur. Le second est une demande polie."),
    ], notes="Faire écouter les quatre paires deux fois avant de les projeter, puis "
             "demander de lever la main gauche pour « é » et la droite pour « è ». On "
             "voit immédiatement qui entend et qui devine.")

    d.tableau('Les mots du bureau', "Où est le « é », où est le « è »",
              ['Le son « é »', 'Le son « è »'],
              [["un relevé", "une conseillère"],
               ["le secrétariat", "une pièce"],
               ["annoncer", "après"],
               ["vous devez", "une matière"]],
              cle=1,
              notes="Ce sont les mots du module, pas des mots d'exercice. Faire compléter "
                    "la colonne de droite par le groupe. « Une conseillère » et « un "
                    "relevé » reviennent dès le bloc D.")

    d.pratique('Discrimination', "Lequel entendez-vous ?",
               "L'enseignante lit un mot de chaque paire, sans le montrer.", [
        ("les ou lait ?", "faire lever la main, puis dire lequel"),
        ("fée ou fait ?", "les deux existent : le contexte ne suffit pas"),
        ("thé ou taie ?", "la mâchoire descend sur le second"),
        ("je voudrai ou je voudrais ?", "la paire qui sert au comptoir"),
        ("signé ou signait ?", "un participe et un imparfait"),
        ("dé ou dais ?", "piège : peu d'élèves connaissent le second mot"),
    ], corrige=True,
       notes="La dernière ligne est un piège volontaire : le mot « dais » est rare. Elle "
             "apprend au groupe qu'on peut entendre juste un son sans connaître le mot — "
             "et que c'est déjà une réussite.")

    d.piege("Dire un seul son entre les deux",
            "Je fais un « e » qui n'est ni fermé ni ouvert : ça passe.",
            "J'exagère les deux pendant une semaine, puis je relâche.",
            "Personne ne vous corrige, mais on vous fait répéter. C'est le défaut le "
            "plus discret du français parlé et le plus long à sortir. En exagérant "
            "quelques jours, il en reste juste assez.",
            notes="Le dire sans dramatiser. Un élève qui comprend que la difficulté est "
                  "normale y travaille ; un élève qui croit mal entendre abandonne.")

    d.pratique('Production', "Lisez à voix haute, une phrase chacun",
               "Le voisin dit si le son est juste, sans corriger la phrase.", [
        ("Je voudrais savoir si je garde ma place.", "deux « è » : voudrais, place"),
        ("Le relevé arrive après la fin du cours.", "« é » puis « è » dans la même phrase"),
        ("La conseillère reçoit sur rendez-vous.", "« è » au milieu et à la fin"),
        ("Vous devez signer cet avis et le rapporter.", "trois « é » de suite"),
        ("L'échéance est écrite en gras, tout en haut.", "deux « é », puis un « è »"),
    ], corrige=True,
       notes="Faire lire debout et lentement. Le rôle du voisin est important : il "
             "écoute un seul point, le son, et pas la grammaire. C'est ce qui rend la "
             "correction supportable et utile.")

    d.regle("La lettre ne décide pas toujours",
            "« ai », « ei », « -et » et « -ère » donnent tous un « è », sans "
            "le moindre accent écrit.",
            precision="« Une semaine » n'a aucun accent et se dit avec un « è ». "
                      "C'est l'oreille qui commande, l'orthographe suit.",
            notes="Cette diapositive répond à la question que le groupe pose toujours "
                  "vers la fin : « comment je sais, si c'est pas écrit ? ». La réponse "
                  "honnête est qu'on l'apprend mot par mot, et que la liste est courte.")

    d.billet(
        "Écrivez deux mots du module : un avec le son « é », un avec le son « è ».",
        exemples=[
            "Prenez des mots que vous aurez à dire au comptoir, pas des mots de dictionnaire.",
            "Entraînez-vous à les dire l'un après l'autre, trois fois.",
        ],
        notes="Ramasser les billets. Ceux qui écrivent deux mots du même son n'entendent "
              "pas encore la différence : ce sont eux qu'il faut reprendre en A3, "
              "individuellement, pendant que le reste travaille le vocabulaire.")

    return d.save(dossier)
