# -*- coding: utf-8 -*-
"""A3 · Les lieux qu'on partage.
Bloc A « Je découvre » · couleur teal · 60 min.
Source : exercice `prImg`, banc `FC_CARDS`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-voisins/images/')


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre="Les lieux qu'on partage",
        chapeau="Dans un immeuble, sept endroits n'appartiennent à personne "
                "et servent à tout le monde. Savoir les nommer, c'est pouvoir "
                "demander quelque chose sans montrer du doigt.",
        duree='60 minutes')

    d.titre(notes="Séance de vocabulaire et de lecture d'images. Prévoir de projeter les "
                  "sept photos de l'exercice interactif : elles sont faites pour être "
                  "vues grandes.")

    d.objectifs([
        "nommer les sept lieux communs d'un immeuble ;",
        "associer une photo et sa description ;",
        "employer chaque mot avec son article ;",
        "dire à quoi sert chaque endroit.",
    ])

    d.declencheur(
        'Observation', "À qui appartient la cour ?",
        image=IMG + 'remise-cour.jpg',
        pistes=[
            "Qui a le droit d'utiliser la cour d'un immeuble ?",
            "Et la remise, au fond : à qui est-elle ?",
            "Est-ce qu'on peut y laisser ses affaires ?",
            "Qui décide, quand deux voisins veulent la même place ?",
        ],
        notes="La question n'a pas de réponse simple, et c'est voulu : elle prépare tout "
              "le défi 1. Laisser le désaccord s'installer, puis le nommer — c'est "
              "exactement pour ça qu'on demande la permission.")

    d.vocabulaire('Vocabulaire', "Les lieux de l'immeuble", [
        ("un immeuble", "un bâtiment qui contient plusieurs logements, les uns au-dessus des autres"),
        ("le palier", "le petit espace plat devant les portes, entre deux escaliers"),
        ("l'entrée", "la pièce du bas, où arrivent le courrier et les visiteurs"),
        ("la cour", "l'espace en arrière, entre l'immeuble et la clôture"),
        ("une remise", "une petite construction fermée, dans la cour, où on range des choses"),
        ("la ruelle", "le petit chemin qui passe en arrière des immeubles"),
    ], notes="Faire répéter chaque mot avec son article. « Un immeuble » et « une "
             "remise » : les deux genres, dans les deux premiers mots, et personne ne "
             "peut deviner lequel est lequel.")

    d.pratique('Association', "Quelle photo pour quelle phrase ?",
               "Lisez la phrase, puis nommez la photo.", [
        ("L'escalier de métal qui monte en tournant, en avant du bâtiment.", "l'escalier extérieur"),
        ("Le petit espace plat où donnent deux portes de logement.", "le palier"),
        ("Le mur de petites portes où arrive le courrier de tout le monde.", "les boîtes aux lettres"),
        ("La petite construction de bois, au fond de la cour.", "la remise"),
        ("La corde tendue entre deux poteaux, pour faire sécher le linge.", "la corde à linge"),
        ("Le petit chemin qui passe en arrière des immeubles.", "la ruelle"),
        ("Une feuille punaisée dans l'entrée, que tout le monde peut lire.", "l'affiche"),
    ], corrige=True,
       notes="C'est l'exercice `prImg` du module interactif, en texte. Le faire d'abord à "
             "l'oral, photos projetées : le glisser-déposer viendra ensuite à l'écran.")

    d.tableau('Analyse', "Les gens de l'immeuble",
              ["Le mot", "Qui c'est"],
              [["un voisin, une voisine", "la personne qui habite à côté ou dans le même immeuble"],
               ["le concierge", "celui qui s'occupe de l'immeuble et a les clés des portes communes"],
               ["le propriétaire", "celui à qui appartient l'immeuble et à qui on paie le loyer"],
               ["faire connaissance", "se parler pour la première fois et apprendre qui est l'autre"]],
              cle=1,
              note="Le concierge n'est pas le propriétaire : c'est lui qu'on voit tous "
                   "les jours, et c'est lui qui a les clés.",
              notes="Diapo à photographier. Demander qui, dans le groupe, sait à qui "
                    "s'adresser chez lui pour une clé ou une réparation.")

    d.cartes("Trois mots qui reviennent tout le module", "À installer aujourd'hui", [
        ("le palier",
         "C'est là que se passent les trois quarts des conversations de voisinage : deux "
         "portes, un espace de deux mètres, et trente secondes."),
        ("la remise",
         "L'endroit du défi 1. Fermée, dans la cour, avec une clé chez le concierge — "
         "d'où la permission à demander."),
        ("l'affiche",
         "L'endroit du défi 3. Punaisée dans l'entrée, elle décrit ce qui manque pour "
         "que les voisins le reconnaissent."),
        ("Pourquoi ces trois-là",
         "Chacun ouvre un défi du module. Les revoir aujourd'hui, c'est gagner dix "
         "minutes trois fois cette semaine."),
    ], notes="Faire écrire les trois mots dans le cahier, avec un dessin plutôt qu'une "
             "traduction : le dessin se retient mieux et se refait de mémoire.")

    d.pratique('Production', "Où est-ce que ça se passe ?",
               "Complétez avec un lieu de l'immeuble.", [
        ("On prend son courrier dans ___ .", "l'entrée, aux boîtes aux lettres"),
        ("Le vélo passe l'hiver dans ___ .", "la remise"),
        ("On s'est parlé cinq minutes sur ___ du deuxième.", "le palier"),
        ("Le chat s'est sauvé dans ___ , en arrière.", "la ruelle"),
        ("Elle étend ses draps sur ___ dès qu'il fait beau.", "la corde à linge"),
        ("L'affiche du chat perdu est punaisée dans ___ .", "l'entrée"),
    ], corrige=True,
       notes="Faire relire chaque phrase complète à voix haute. C'est la première fois "
             "que les mots sortent dans une phrase, et c'est ce qui compte.")

    d.billet(
        "Faites la liste des lieux communs de votre immeuble.",
        exemples=[
            "Ceux qui existent chez vous, et ceux qui n'existent pas.",
            "Marquez celui que vous utilisez le plus souvent.",
        ],
        notes="Devoir court. Les listes serviront d'exemples réels au défi 1 : chacun "
              "demandera sa permission pour un endroit de son propre immeuble.")

    return d.save(dossier)
