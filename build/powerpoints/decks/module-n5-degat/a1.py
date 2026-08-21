# -*- coding: utf-8 -*-
"""A1 · La tache au plafond.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-degat/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="La tache au plafond",
        chapeau="Un matin de novembre, l'eau tombe du plafond d'une chambre. "
                "Ce qui se passe dans les six premières heures décide de tout "
                "le reste.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Demander d'abord qui, dans le groupe, a "
                  "déjà eu de l'eau chez lui — un dégât, une infiltration, un dégel de "
                  "tuyau. Presque toujours, deux ou trois mains se lèvent, et l'une des "
                  "histoires servira de fil toute la semaine.")

    d.objectifs([
        "reconnaître les signes d'un dégât d'eau ;",
        "nommer ce qu'on voit : un cerne, un plancher qui gondole ;",
        "connaître les quatre gestes des premières heures ;",
        "savoir pourquoi on ne jette rien avant le constat.",
    ])

    d.declencheur(
        'Observation', "Vous vous levez et vous voyez ça au plafond de votre "
                       "chambre. Que faites-vous, dans quel ordre ?",
        image=IMG + 'cerne-plafond.jpg',
        pistes=[
            "Vous appelez qui, en premier ?",
            "Vous attendez de voir si ça s'arrête ?",
            "Vous essuyez tout de suite ?",
            "Vous prenez une photo ?",
        ],
        notes="La réponse la plus fréquente est « j'essuie et je regarde si ça continue ». "
              "C'est le réflexe qui coûte le plus cher : ce qui est nettoyé ne se prouve "
              "plus. Ne pas corriger tout de suite — le dialogue le fera.")

    d.dialogue('Dialogue · 1 de 3', "Est-ce que tu as eu de l'eau chez toi ?", [
        ("MARIAMA", "Kim ! Attends une minute avant de descendre. Est-ce que tu "
                    "as eu de l'eau chez toi cette nuit ?", True),
        ("KIM", "De l'eau ? Non… Pourquoi ? Qu'est-ce qui se passe ?", True),
        ("MARIAMA", "Viens voir. Regarde le plafond de ma chambre, dans le coin, "
                    "au-dessus du lit.", True),
        ("KIM", "Oh là là. C'est une grosse tache brune. Et le tour est plus "
                "foncé, on dirait un cerne.", False),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer que Mariama commence par le voisin du dessus, et non par "
             "le propriétaire. C'est le bon ordre : on cherche d'où ça vient avant "
             "d'appeler.")

    d.dialogue('Dialogue · 2 de 3', "D'où ça vient", [
        ("MARIAMA", "Ça coulait encore à six heures ce matin. J'ai mis une "
                    "chaudière par terre, et elle est déjà à moitié pleine.", True),
        ("KIM", "Le coin de ta chambre, c'est juste en dessous de ma salle de "
                "bain. Attends… mon chauffe-eau est dans le garde-robe, là.", True),
        ("MARIAMA", "Est-ce que tu peux aller voir tout de suite ? Moi, je "
                    "commence à sept heures et demie.", True),
        ("KIM", "J'y monte. Si c'est le chauffe-eau qui a lâché, ça expliquerait "
                "tout : il a quinze ans, ce réservoir-là.", True),
    ], notes="« Juste en dessous de ma salle de bain » : l'eau descend, toujours. Faire "
             "dessiner au tableau les trois étages de l'immeuble — c'est le schéma qui "
             "revient tout le module.")

    d.dialogue('Dialogue · 3 de 3', "Ne jette rien", [
        ("MARIAMA", "Et le plancher de ma chambre a commencé à gondoler. Les "
                    "lattes se soulèvent près du mur.", True),
        ("KIM", "Prends des photos. Tout de suite, avant que ça sèche, et avec "
                "la date.", True),
        ("MARIAMA", "Il y a aussi ma boîte de papiers qui était par terre, en "
                    "dessous. Elle est trempée.", True),
        ("KIM", "Prends-la en photo aussi, et ne jette rien. Rien du tout, même "
                "ce qui est fini. C'est ta preuve.", True),
    ], notes="Les deux dernières répliques sont le cœur de la séance. Les écrire au "
             "tableau et les y laisser jusqu'à la fin du bloc A.")

    d.regle("Ne rien jeter avant le constat",
            "Un bien jeté est un bien qui n'a jamais existé.",
            precision="C'est la première cause de refus d'une réclamation. Un matelas "
                      "trempé, une boîte de papiers, un tapis : on les sort de la pièce, "
                      "on ne les met pas au chemin. La photo datée du matin même vaut "
                      "plus que toutes les explications données trois semaines plus tard.",
            notes="Diapositive à photographier. Si les élèves ne retiennent qu'une chose "
                  "de la séance, c'est celle-là.")

    d.cartes("Les quatre gestes des premières heures", "Dans cet ordre", [
        ("Photographier",
         "Avant que ça sèche, avant de tasser quoi que ce soit. Avec la date."),
        ("Recueillir l'eau",
         "Une chaudière, une serviette. Limiter les dommages est votre part."),
        ("Ne rien jeter",
         "Même ce qui est manifestement fini. On le sort de la pièce, c'est tout."),
        ("Avertir sans attendre",
         "Le propriétaire d'abord, l'assureur ensuite. Pas à midi : tout de suite."),
    ], notes="Faire dire, pour chacun, ce qui se perd si on ne le fait pas. C'est plus "
             "efficace que de répéter la consigne.")

    d.tableau('Ce qu\'on voit, et le mot qui va avec', "Chaque surface a son verbe",
              ['La surface', 'Ce qu\'elle fait'],
              [["le plafond", "il coule, puis il cerne"],
               ["la peinture", "elle cloque, puis elle se décolle"],
               ["le plancher de bois", "il gonfle, puis il gondole"],
               ["le mur", "il s'assombrit, puis il moisit"]],
              cle=0,
              note="Ce sont les verbes qu'attendent le propriétaire et l'assureur.",
              notes="Faire mimer : « cloquer », « gondoler ». Le geste fixe le mot mieux "
                    "que la définition.")

    d.piege("Nettoyer avant de faire constater",
            "J'ai tout essuyé, c'était sale.",
            "J'ai tout photographié, puis j'ai essuyé.",
            "Personne ne demande de vivre dans l'eau. Mais entre le seau et la "
            "serpillière, il y a la photo — et elle prend dix secondes. Une pièce "
            "remise en état avant le passage de l'assureur est une pièce qu'on ne peut "
            "plus indemniser.",
            notes="C'est le piège le plus coûteux du module, et le plus naturel : on "
                  "range parce qu'on a été élevé à ranger.")

    d.pratique('Pratique · exercice pr1', "Vrai ou Faux — La tache au plafond",
               "Écoutez de nouveau le dialogue, puis répondez.",
               [("L'eau coulait encore à six heures du matin.", "VRAI"),
                ("La tache au plafond est petite et grise.", "FAUX"),
                ("La chambre de Mariama est sous la salle de bain de Kim.", "VRAI"),
                ("Kim conseille de jeter tout de suite ce qui est trempé.", "FAUX"),
                ("Kim trouve qu'on peut attendre midi pour appeler.", "FAUX")],
               corrige=True,
               notes="Cinq des sept énoncés du module. Les deux autres se font dans "
                     "l'activité interactive.")

    d.billet(
        "Écrivez une phrase : qu'est-ce que vous feriez en premier ?",
        exemples=[
            "« Je prendrais une photo avec la date. »",
            "« J'irais voir le voisin du dessus. »",
        ],
        notes="Deux minutes. Les ramasser : elles disent qui a compris que la preuve "
              "vient avant le ménage.")

    return d.save(dossier)
