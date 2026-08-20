# -*- coding: utf-8 -*-
"""A4 · Ce qu'on apporte, ce qu'on trouve.
Bloc A « Je découvre » · couleur teal · 50 min.
Source : exercice `prImg`, cartes mémoire.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-activite/images/')


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre="Ce qu'on apporte, ce qu'on trouve",
        chapeau="Huit lieux et objets d'un centre de loisirs. Les nommer, "
                "c'est pouvoir demander où ils sont — et savoir ce qu'on doit "
                "mettre dans son sac.",
        duree='50 minutes')

    d.titre(notes="Séance visuelle et courte. Elle clôt le bloc A : à la fin, chacun doit "
                  "pouvoir dire ce qu'il faut apporter à une activité.")

    d.objectifs([
        "nommer huit lieux et objets d'un centre de loisirs ;",
        "distinguer ce qui est obligatoire de ce qui est recommandé ;",
        "employer l'article juste : un maillot, le bonnet, la piscine ;",
        "faire la liste de ce que je dois mettre dans mon sac.",
    ])

    d.declencheur(
        'Observation', "Que faut-il mettre dans ce sac ?",
        image=IMG + 'sac-piscine.jpg',
        pistes=[
            "Nommez chaque objet que vous voyez.",
            "Lequel est obligatoire dans les piscines d'ici ?",
            "Qu'est-ce qui manque, selon vous ?",
            "Avez-vous déjà été refusé quelque part faute d'un objet ?",
        ],
        notes="La deuxième piste amène le bonnet de bain. La quatrième amène souvent des "
              "histoires vécues : les laisser sortir, elles installent le vocabulaire.")

    d.cartes('Les quatre objets', "Ce qu'on apporte", [
        ("un maillot de bain",
         "Se dit « maillot » tout court dans la conversation. Au Québec, on entend aussi "
         "« costume de bain »."),
        ("un bonnet de bain",
         "Obligatoire dans beaucoup de piscines publiques d'ici. Il se vend au comptoir, "
         "quelques dollars."),
        ("une serviette",
         "Grande, pour se sécher. À ne pas confondre avec la serviette de table."),
        ("des sandales",
         "Pour le bord de la piscine et la douche. Souvent recommandées plutôt "
         "qu'obligatoires."),
    ], notes="Insister sur la différence obligatoire / recommandé : elle décide si on peut "
             "entrer dans l'eau ou non.")

    d.cartes('Les quatre lieux', "Ce qu'on trouve sur place", [
        ("le comptoir",
         "L'endroit où on s'inscrit, où on paie et où on pose ses questions."),
        ("le vestiaire",
         "Où on se change et où on laisse ses affaires. Souvent avec des casiers à cadenas."),
        ("la piscine",
         "Le bassin lui-même. « Aller à la piscine » désigne aussi tout l'édifice."),
        ("le gymnase",
         "La grande salle des sports d'équipe et des cours de groupe."),
    ], notes="Faire situer chaque lieu par rapport aux autres : « le vestiaire est entre le "
             "comptoir et la piscine ». Cela réutilise les repères du module précédent.")

    d.tableau('Analyse', "Obligatoire ou recommandé ?",
              ['Ce qu\'on entend', 'Ce que ça veut dire'],
              [["Le bonnet est obligatoire.", "sans lui, pas d'accès à l'eau"],
               ["Des sandales sont recommandées.", "c'est un conseil, pas une condition"],
               ["Il faut une preuve de résidence.", "sans elle, je paie le tarif élevé"],
               ["Les partitions sont fournies.", "je n'ai rien à acheter"]],
              cle=0,
              note="Écoutez le mot exact : obligatoire, recommandé, fourni. Chacun décide "
                   "d'une dépense ou d'un refus.",
              notes="Diapo à photographier. Ces quatre formules reviennent partout, bien "
                    "au-delà des loisirs.")

    d.piege('Confondre obligatoire et recommandé',
            "On m'a dit d'apporter des sandales, alors j'ai pensé que le bonnet aussi, c'était juste conseillé.",
            "Le bonnet est obligatoire. Les sandales sont recommandées.",
            "Un objet obligatoire vous empêche de participer si vous ne l'avez pas. Un "
            "objet recommandé, non. La différence tient à un mot, et elle décide si votre "
            "enfant entre dans l'eau ce samedi-là.",
            notes="Faire répéter les deux adjectifs. Ce sont deux mots administratifs que "
                  "les élèves rencontreront dans tous les contextes.")

    d.pratique('Pratique', "Le mot juste",
               "Complétez avec le mot du vocabulaire.", [
        ("Le ___ de bain est obligatoire dans cette piscine.", "bonnet"),
        ("Les enfants se changent au ___ avant le cours.", "vestiaire"),
        ("C'est au ___ qu'on s'inscrit et qu'on paie.", "comptoir"),
        ("Apportez un ___ , une serviette et des sandales.", "maillot"),
        ("Le cours de groupe a lieu dans le ___ .", "gymnase"),
        ("Il faut une ___ de résidence pour le tarif réduit.", "preuve"),
    ], corrige=True,
       notes="Ces six mots sont dans le banc de vocabulaire. Les élèves peuvent les réviser "
             "seuls avec les cartes mémoire.")

    d.billet(
        "Faites la liste de ce qu'il faut apporter à une activité que vous connaissez.",
        exemples=[
            "Séparez ce qui est obligatoire de ce qui est recommandé.",
            "Si vous ne pratiquez aucune activité, faites la liste pour le cours de natation de Mateo.",
        ],
        notes="Bilan du bloc A. Les listes servent à la production orale de E1 — expliquer "
              "une activité qu'on connaît.")

    return d.save(dossier)
