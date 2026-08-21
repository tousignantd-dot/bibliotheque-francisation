# -*- coding: utf-8 -*-
"""A3 · De quelle couleur ?
Bloc A « Je découvre » · couleur teal · 75 min. Fin du bloc de découverte.
Source : exercices `prImg` et `prCouleur`, mini-leçon `prCouleur`.

Les cinq couleurs du programme — rouge, bleu, jaune, vert, noir — plus le
blanc, qui manque à la liste mais qu'aucune classe ne peut éviter : les
feuilles sont blanches.

Ici on ne fait que **nommer** les couleurs. L'accord et la place viennent au
Défi 1, en B2, et la séance s'arrête volontairement avant.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-classe/images/')


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre="De quelle couleur ?",
        chapeau="Six couleurs suffisent pour demander n'importe quel objet "
                "d'une salle de classe.",
        duree='75 minutes')

    d.titre(notes="Séance légère, très visuelle. Apporter des objets de couleurs "
                  "différentes : crayons, cahiers, feuilles, sacs. On nomme ce qu'on "
                  "touche.")

    d.objectifs([
        "nommer six couleurs ;",
        "désigner un objet par sa couleur ;",
        "reconnaître les lieux et les objets de la classe sur une photo ;",
        "demander un objet précis à l'enseignante.",
    ])

    d.declencheur(
        'Observation', "Combien de couleurs voyez-vous ?",
        image=IMG + 'boite-crayons.jpg',
        pistes=[
            "Nommez une couleur que vous voyez.",
            "Quelle est la couleur de votre crayon ?",
            "Et celle de votre cahier ?",
            "Quelle couleur manque dans la boîte ?",
        ],
        notes="Laisser nommer dans le désordre, y compris dans la langue maternelle : on "
              "reprend ensuite en français, sans corriger la première fois.")

    d.vocabulaire('Vocabulaire', "Les six couleurs de la classe", [
        ("rouge", "La couleur d'une tomate."),
        ("bleu", "La couleur du ciel."),
        ("jaune", "La couleur du soleil."),
        ("vert", "La couleur de l'herbe."),
        ("noir", "La couleur de la nuit."),
        ("blanc", "La couleur de la neige."),
    ], notes="Diapositive à photographier. Montrer un objet de chaque couleur en la "
             "disant : le mot se retient avec la chose, pas avec la traduction.")

    d.tableau('Analyse', "L'objet, puis la couleur",
              ["On dit", "On ne dit pas"],
              [["un crayon rouge", "un rouge crayon"],
               ["une feuille blanche", "une blanche feuille"],
               ["le tableau noir", "le noir tableau"],
               ["un sac vert", "un vert sac"]],
              cle=1,
              note="En français, la couleur vient toujours après l'objet.",
              notes="Diapositive à photographier. Beaucoup de langues font l'inverse : "
                    "le dire explicitement, et demander au groupe comment ça se dit chez "
                    "eux. La comparaison fait retenir la règle.")

    d.regle("Désigner un objet par sa couleur",
            "Quand on ne connaît pas le nom, la couleur suffit.",
            precision="« Le <b>rouge</b>, s'il vous plaît. » « Le grand <b>bleu</b>, "
                      "là. » On montre du doigt et on dit la couleur : l'enseignante "
                      "comprend, et donne le nom de l'objet en même temps.",
            notes="Diapositive à photographier. C'est une stratégie de survie, pas une "
                  "faute : la nommer comme telle donne confiance aux plus timides.")

    d.pratique('Vocabulaire', "Quelle couleur ?",
               "Associez chaque objet à sa couleur.", [
        ("Le crayon de Myriam, comme une tomate.", "rouge"),
        ("Les cinq mots au tableau, comme le ciel.", "bleu"),
        ("La feuille neuve, comme la neige.", "blanche"),
        ("Le tableau du fond, comme la nuit.", "noir"),
        ("Le sac de Tariq, comme l'herbe du parc.", "vert"),
        ("La gomme à effacer, comme le soleil.", "jaune"),
    ], corrige=True, cols=1,
       notes="Ces six énoncés sont ceux de l'exercice 4 du module en ligne. Les faire à "
             "l'oral ici, pour que l'écran ne serve qu'à confirmer.")

    d.pratique('Pratique · en groupe', "Donnez-moi le rouge",
               "Debout, autour d'une table où tout est mélangé.", [
        ("Étape 1", "L'enseignante demande un objet par sa couleur."),
        ("Étape 2", "Un élève le trouve et le rapporte."),
        ("Étape 3", "Il dit à son tour : « Donnez-moi le… »"),
        ("Étape 4", "On complique : « le petit rouge », « la grande blanche »."),
    ], cols=1,
       notes="Vingt minutes. L'étape 4 introduit sans le dire la place de l'adjectif "
             "avant le nom — « petit », « grand » — qui, elle, se met devant. Ne pas "
             "l'expliquer : le faire entendre.")

    d.billet(
        "Écrivez la couleur de quatre choses qui sont dans votre classe.",
        exemples=[
            "Mon cahier est bleu.",
            "La porte est brune.",
            "Le tableau est blanc.",
            "Ma chaise est noire.",
        ],
        notes="Devoir court. Ne pas corriger l'accord cette semaine : il est enseigné en "
              "B2. Noter seulement ce qui reviendra là.")

    return d.save(dossier)
