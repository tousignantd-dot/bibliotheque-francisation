# -*- coding: utf-8 -*-
"""A3 · Les couleurs et les motifs.
Bloc A « Je découvre » · couleur teal · 60 min.
Source : exercices `prCouleurs` et `prImg`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-vetements/images/')


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre='Les couleurs et les motifs',
        chapeau="Une couleur ne suffit pas : « bleu » peut désigner le ciel "
                "ou la nuit. Deux mots de plus — pâle, foncé — et la "
                "conseillère sait exactement quoi aller chercher.",
        duree='60 minutes')

    d.titre(notes="Séance de vocabulaire. Apporter si possible deux vêtements réels, un "
                  "pâle et un foncé, un uni et un rayé : la démonstration vaut mieux que "
                  "la définition.")

    d.objectifs([
        "distinguer pâle et foncé ;",
        "nommer quatre motifs : uni, rayé, à pois, à carreaux ;",
        "nommer trois matières : le coton, la laine, le nylon ;",
        "reconnaître les lieux et les objets d'un magasin de vêtements.",
    ])

    d.declencheur(
        'Observation', "Comment décririez-vous ce vêtement ?",
        image=IMG + 'manteaux-suspendus.jpg',
        pistes=[
            "Quelle couleur ?",
            "Clair ou sombre ?",
            "Avec un dessin, ou sans ?",
            "En quelle matière, à votre avis ?",
        ],
        notes="Laisser décrire librement. Noter au tableau les mots qui manquent : ce sont "
              "ceux de la séance.")

    d.tableau('Analyse', "Deux mots qui précisent la couleur",
              ['On dit', 'Ça veut dire'],
              [["bleu pâle", "clair, proche du blanc — comme le ciel"],
               ["bleu foncé", "sombre, presque noir"],
               ["uni", "une seule couleur, sans dessin"],
               ["rayé", "des lignes droites de deux couleurs"]],
              cle=0,
              note="Pâle salit vite ; foncé ne se voit pas le soir. Les deux ont un défaut.",
              notes="Diapo à photographier. Faire donner un exemple de vêtement pâle et un "
                    "de vêtement foncé par chaque élève.")

    d.cartes("Les quatre motifs", "Ce qu'on voit sur le tissu", [
        ("Uni",
         "Une seule couleur, aucun dessin. C'est le plus courant pour un manteau d'hiver, "
         "et le plus facile à agencer."),
        ("Rayé",
         "Des lignes droites de deux couleurs. Souvent sur les chandails et les bas."),
        ("À pois",
         "Des petits ronds répétés sur le tissu. Surtout sur les blouses et les robes."),
        ("À carreaux",
         "Des lignes qui se croisent et forment des carrés. Très fréquent sur les chemises "
         "d'automne, ici."),
    ], notes="Faire chercher un exemple de chacun dans la classe : quelqu'un porte "
             "toujours au moins deux de ces motifs.")

    d.regle("La matière se dit avec « en » ou « de »",
            "un chandail <b>en</b> laine, un chandail <b>de</b> laine",
            precision="Les deux se disent et veulent dire la même chose. Les trois matières "
                      "à connaître pour l'hiver : le <b>coton</b>, léger, qui ne réchauffe "
                      "pas ; la <b>laine</b>, chaude mais qui pique un peu ; le "
                      "<b>nylon</b>, qui coupe le vent et laisse passer le froid s'il n'est "
                      "pas doublé.",
            notes="Diapo à photographier. Insister sur « doublé » : c'est le mot qui "
                  "distingue un manteau utile d'un manteau décoratif.")

    d.piege("Dire seulement la couleur",
            "Je cherche un manteau bleu.",
            "Je cherche un manteau bleu foncé, uni.",
            "« Bleu » couvre vingt teintes. La conseillère apportera trois manteaux, dont "
            "aucun ne conviendra. Deux mots de plus — la nuance et le motif — font gagner "
            "dix minutes à tout le monde.",
            notes="Faire reformuler par les élèves leurs propres demandes du billet de "
                  "sortie de A1, en ajoutant nuance et motif.")

    d.pratique('Pratique · 1 de 2', "Que veut dire ce mot ?",
               "Associez chaque mot à sa définition.", [
        ("pâle", "une couleur claire, proche du blanc"),
        ("foncé", "une couleur sombre, proche du noir"),
        ("uni", "une seule couleur, sans dessin"),
        ("rayé", "des lignes droites de deux couleurs"),
        ("à pois", "des petits ronds répétés"),
        ("à carreaux", "des lignes qui se croisent"),
    ], corrige=True,
       notes="Utiliser l'exercice 4 du module. Faire dire à voix haute avant de glisser.")

    d.pratique('Pratique · 2 de 2', "Dans le magasin",
               "Nommez ce que montre chaque photo.", [
        ("Une rangée de vêtements accrochés", "des cintres"),
        ("La pièce fermée par un rideau", "la cabine d'essayage"),
        ("La petite étiquette du col", "la taille"),
        ("Le carton attaché à la manche", "l'étiquette de prix"),
        ("Les dessins dans le col", "l'étiquette d'entretien"),
        ("La machine chaude de la buanderie", "la sécheuse"),
    ], corrige=True,
       notes="Utiliser l'exercice 3 du module, à glisser-déposer. Projeter les images une "
             "à une si le groupe travaille sans ordinateur.")

    d.billet(
        "Décrivez trois vêtements que vous portez aujourd'hui.",
        exemples=[
            "Le vêtement, la couleur, la nuance, le motif.",
            "Ex. : « un chandail vert foncé, uni, en laine ».",
        ],
        notes="Devoir très court, à faire en classe s'il reste du temps. Il prépare "
              "directement l'exercice d'accord de B2.")

    return d.save(dossier)
