# -*- coding: utf-8 -*-
"""D1 · Il est comment, votre chat ?
Bloc D « Défi 3 · Il est comment ? » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3ordre`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-voisins/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Il est comment, votre chat ?",
        chapeau="Quand quelque chose se perd dans un immeuble, tout se joue "
                "sur la description. D'abord ce qui se voit de loin, ensuite "
                "le détail qui ne trompe pas.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 3. C'est le défi le plus utile hors de l'immeuble : "
                  "décrire une personne ou un objet sert au poste de police, à l'hôpital, "
                  "au bureau des objets perdus. Le dire en ouverture.")

    d.objectifs([
        "comprendre une description dite à l'oral ;",
        "relever la couleur, la taille et le détail ;",
        "reconnaître ce que chaque mot fait connaître ;",
        "poser la question « il est comment ? ».",
    ])

    d.declencheur(
        'Observation', "Comment décrire ce qu'on a perdu ?",
        image=IMG + 'affiche-entree.jpg',
        pistes=[
            "Qu'est-ce qu'on écrit sur une affiche comme celle-là ?",
            "Par quoi commence-t-on : la couleur, ou le nom ?",
            "Qu'est-ce qui permet de reconnaître à coup sûr ?",
            "Avez-vous déjà perdu quelque chose ici ?",
        ],
        notes="La troisième question est celle du défi : la couleur ne suffit jamais, il "
              "faut un détail. Laisser le groupe trouver l'idée avant de la nommer.")

    d.dialogue('Dialogue · 1 de 3', "Il est parti quand ?", [
        ("MANON", "Monsieur Belkacem ! Vous avez vu mon affiche dans l'entrée ?", True),
        ("RACHID", "L'affiche pour le chat ? Oui, ce matin. Il est parti quand ?", True),
        ("MANON", "Avant-hier soir. Il n'est jamais parti aussi longtemps.", True),
        ("RACHID", "Il est comment ? J'ai vu un chat dans la ruelle hier.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Deux questions à retenir, et elles sont dans les répliques de Rachid : "
             "« il est parti quand ? » et « il est comment ? ». Ce sont les deux "
             "questions qu'on pose toujours devant une affiche.")

    d.dialogue('Dialogue · 2 de 3', "Roux, assez gros, une tache blanche", [
        ("MANON", "Il est roux, assez gros, avec une tache blanche sous le menton.", True),
        ("RACHID", "Le chat d'hier était roux, oui. Il avait un collier.", True),
        ("MANON", "Un collier bleu ? Caramel porte un collier bleu, sans médaille.", True),
        ("RACHID", "Bleu, je pense. Il était un peu peureux, il s'est sauvé.", True),
    ], notes="La description de Manon suit exactement l'ordre du défi : la couleur, la "
             "taille, le détail. Faire compter les trois éléments dans sa première "
             "réplique — ils y sont tous, en une seule phrase.")

    d.dialogue('Dialogue · 3 de 3', "Ces clés-là, dans l'escalier", [
        ("RACHID", "Attendez, j'ai trouvé autre chose. Ces clés-là, dans l'escalier.", True),
        ("MANON", "Montrez-moi. Un trousseau avec trois clés et un petit ourson ?", True),
        ("RACHID", "Oui, un ourson en tissu, un peu usé. Elles sont à qui ?", True),
        ("MANON", "À la dame du premier. Grande, cheveux gris courts, lunettes rouges.", True),
    ], notes="Deuxième description, celle d'une personne cette fois — et le même ordre : "
             "la taille, puis les cheveux, puis le détail des lunettes. Faire remarquer "
             "que trois mots suffisent à reconnaître quelqu'un.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le chat de Manon est parti avant-hier soir.", "vrai"),
        ("Caramel est noir avec des pattes blanches.", "faux — roux, avec une tache blanche sous le menton"),
        ("Caramel porte un collier bleu, sans médaille.", "vrai"),
        ("Rachid a vu le chat derrière le garage vert.", "vrai — au bout de la ruelle"),
        ("Rachid a trouvé un trousseau de clés dans la cour.", "faux — dans l'escalier"),
        ("Les clés appartiennent à la dame du premier étage.", "vrai"),
    ], corrige=True,
       notes="C'est l'exercice `t3vf` du module interactif, mot pour mot. La cinquième "
             "ligne se joue sur un seul mot — cour ou escalier : c'est exactement le "
             "genre de détail qui compte quand on rapporte un objet trouvé.")

    d.pratique('Compréhension', "Chaque mot dit une chose précise",
               "Qu'est-ce que ce bout de description fait connaître ?", [
        ("« roux », « bleu », « gris »", "la couleur — ce qui se voit de plus loin"),
        ("« assez gros », « grande », « petit »", "la taille"),
        ("« une tache blanche sous le menton »", "le détail qui ne trompe pas"),
        ("« très peureux », « toujours de bonne humeur »", "le caractère"),
        ("« des lunettes rouges », « un collier »", "ce que la personne ou l'animal porte"),
        ("« vu lundi soir dans la ruelle »", "le moment et l'endroit de la dernière fois"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t3ordre` du module interactif. Faire ressortir l'ordre "
             "utile : couleur et taille d'abord — elles se voient de loin —, détail "
             "ensuite. C'est la grille de l'affiche de D2.")

    d.billet(
        "Décrivez en trois lignes un objet que vous avez sur vous.",
        exemples=[
            "La couleur, la taille, puis le détail.",
            "« Un sac noir, assez grand, avec une fermeture cassée. »",
        ],
        notes="Devoir court. Les ramasser sans les nommer : en D2, on les lira à voix "
              "haute et le groupe devra retrouver l'objet dans la classe. Une description "
              "qui échoue au test est une description à reprendre.")

    return d.save(dossier)
