# -*- coding: utf-8 -*-
"""E1 · Décris quelqu'un pour qu'on le reconnaisse
Bloc E « Je me lance » · couleur teal · production orale · 75 min.
Source : bloc `appli` de `custom.js` — le jeu de rôle « reconnaitre » et la
production orale en trois temps, corrigée par l'assistant puis déposée.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Décris quelqu'un pour qu'on le reconnaisse",
        chapeau="Quatre-vingt-dix secondes, quatre temps, et un inconnu qui "
                "doit repartir du terminus avec la bonne personne.",
        duree='75 minutes')

    d.titre(notes="Première séance de production. Rappeler le tableau des quatre temps "
                  "de C1 avant tout : silhouette, vêtements, visage, signe "
                  "particulier. C'est la grille de correction.")

    d.objectifs([
        "décrire une personne en quatre-vingt-dix secondes, dans l'ordre ;",
        "répondre à une demande de précision sans se contredire ;",
        "corriger soi-même une phrase ambiguë ;",
        "employer deux adjectifs accordés et une relative avec qui ou où.",
    ], notes="Le troisième objectif est celui que l'assistant provoque : il "
             "redemande, il confond exprès, et l'élève doit reprendre.")

    d.declencheur(
        'Préparation', "Qui vas-tu décrire ?",
        pistes=[
            "Kadiatou, si tu préfères t'appuyer sur le dossier.",
            "Quelqu'un de ta famille que tu attends.",
            "Quelqu'un de la classe, sans dire son nom.",
            "Note trois détails qui se voient de loin.",
        ],
        notes="Cinq minutes de préparation écrite, en silence, avant tout le reste. "
              "Sans ces trois détails notés, la production part dans le désordre.")

    d.tableau('Plan', "Quatre-vingt-dix secondes, trois temps",
              ['Le temps', 'Ce que tu dis'],
              [["Temps 1", "la silhouette et l'âge : une femme de taille moyenne, dans la trentaine"],
               ["Temps 2", "les vêtements et le bagage : un foulard vert, une grosse valise rouge"],
               ["Temps 3", "le visage, les cheveux, puis le signe particulier"]],
              cle=0,
              note="Le signe particulier en dernier : il sert à être sûr, pas à chercher.",
              notes="Diapositive à photographier. Chronométrer une première fois à "
                    "vide : quatre-vingt-dix secondes, c'est long, et les élèves "
                    "s'arrêtent souvent à quarante.")

    d.cartes('Jeu de rôle', "L'assistant joue celui qui va au terminus", [
        ("Il n'a jamais vu la personne",
         "Il n'a pas de photo. Tout ce qu'il saura vient de toi, et il partira avec ça."),
        ("Il redemande ce qui est vague",
         "Attachés comment ? Grande, elle ou la valise ? Réponds sans changer ce que tu as déjà dit."),
        ("Il répète ce qu'il a compris",
         "Écoute bien : s'il a compris autre chose, c'est à toi de corriger."),
        ("Il demande où se placer",
         "Le terminus a deux portes. Emploie où : près du banc où les gens attendent."),
    ], notes="Les trois situations du module sont Kadiatou, Ousmane et le "
             "rendez-vous. On peut aussi jouer l'autre rôle : celui qui va chercher.")

    d.regle("Ce qui dépend de celui qui regarde ne se cherche pas",
            "Elle est jolie et gentille ne permet de trouver personne.",
            precision="Dans une salle d'attente, on cherche une taille, une couleur, "
                      "un objet, une forme de cheveux. Tout le reste est vrai mais "
                      "inutilisable. C'est la différence entre décrire pour raconter "
                      "et décrire pour retrouver.",
            notes="Diapositive à photographier. L'assistant refuse poliment ces "
                  "descriptions et en redemande une autre : prévenir le groupe.")

    d.pratique('Langue', "Trois phrases à réutiliser",
               "Préparez-les à l'avance : elles serviront pendant l'enregistrement.", [
        ("Une relative", "une femme de taille moyenne qui tire une grosse valise rouge"),
        ("Un où de lieu", "près du banc où les gens attendent, en face du guichet"),
        ("Une correction", "je me suis mal exprimée : c'est la valise qui est grosse"),
        ("Deux adjectifs accordés", "une longue veste grise et des lunettes rondes"),
        ("Un signe particulier", "une petite cicatrice au-dessus du sourcil gauche"),
    ], corrige=True,
       notes="Faire écrire ces cinq phrases dans le cahier avant l'enregistrement. "
             "Les élèves qui les ont préparées parlent deux fois plus longtemps.")

    d.tableau('Démarche', "Trois étapes, dans le module",
              ['L\'étape', 'Ce que tu fais'],
              [["Je m'enregistre", "quatre-vingt-dix secondes, autant de fois que tu veux"],
               ["Je m'écoute", "tu lis la transcription et tu la corriges"],
               ["J'envoie", "l'assistant te répond, puis tu déposes pour ton enseignant"]],
              cle=0,
              notes="Montrer la démarche au projecteur une fois, avec un enregistrement "
                    "de l'enseignant. Voir quelqu'un se reprendre trois fois "
                    "dédramatise plus que n'importe quelle consigne.")

    d.billet(
        "Quel détail as-tu oublié, et que tu ajouterais maintenant ?",
        exemples=[
            "Une phrase.",
            "Écoute ton enregistrement avant de répondre.",
        ],
        notes="Deux minutes. Les billets préparent E2 : ce qui manque à l'oral manque "
              "souvent aussi à l'écrit.")

    return d.save(dossier)
