# -*- coding: utf-8 -*-
"""C4 · Écrire une affiche.
Bloc C · couleur teal (production écrite) · 75 min.
Source : les deux affiches du défi 2, mises en pratique.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='teal',
        titre='Écrire une affiche',
        chapeau="Une affiche se lit en trois secondes, debout, dans un corridor. Tout "
                "doit y être — et tout doit se voir d'un coup d'œil.",
        duree='75 minutes')

    d.titre(notes="Séance de production écrite. Apporter du papier grand format si "
                  "possible : une affiche s'écrit à la bonne taille, pas sur une feuille "
                  "de cahier.")

    d.objectifs([
        "écrire une affiche qui contient les six informations obligatoires ;",
        "hiérarchiser : ce qui se lit en premier, en deuxième, en dernier ;",
        "terminer par un slogan ou une promesse ;",
        "relire une affiche du point de vue de celui qui passe.",
    ])

    d.tableau('Analyse', "Les six informations obligatoires",
              ["L'information", 'Un exemple'],
              [["quoi", "un atelier de réparation"],
               ["qui organise", "le centre Sainte-Odile"],
               ["quand", "samedi 12 avril, de 9 h à 16 h"],
               ["où", "au sous-sol du centre"],
               ["combien", "gratuit"],
               ["quoi apporter", "votre grille-pain, votre lampe"]],
              cle=0, props=[0.3, 0.7],
              notes="Six informations. Une affiche à laquelle il en manque une oblige "
                    "les gens à téléphoner — et la plupart ne téléphonent pas.")

    d.regle('La règle de la hiérarchie',
            "Trois niveaux : ce qu'on voit de loin, ce qu'on lit en s'approchant, ce qu'on retient en partant.",
            precision="De loin : le titre et la date, en gros. En s'approchant : "
                      "l'adresse, l'heure, le prix. En partant : le slogan. Une affiche "
                      "sans hiérarchie se lit comme une lettre, et personne ne lit une "
                      "lettre sur un babillard.",
            notes="Faire dessiner les trois niveaux au tableau, en trois tailles de "
                  "lettres. La démonstration visuelle est immédiate.")

    d.cartes('Analyse', "Quatre erreurs d'affiche fréquentes", [
        ("Tout de la même taille",
         "Rien ne ressort, donc rien ne se lit. Il faut un titre trois fois plus gros "
         "que le reste."),
        ("La date en petit",
         "C'est l'information qu'on cherche en premier. Elle doit être visible de trois "
         "mètres."),
        ("Trop de texte",
         "Une affiche n'est pas un dépliant. Au-delà de soixante mots, personne ne lit "
         "jusqu'au bout."),
        ("Pas de « quoi apporter »",
         "« Apportez votre vélo » change tout : sans cette phrase, les gens viennent "
         "les mains vides et repartent déçus."),
    ], notes="La quatrième erreur est la plus coûteuse et la moins connue. La souligner.")

    d.pratique('Pratique · 1 de 4', "Trouvez ce qui manque",
               "Six informations obligatoires. Lesquelles manquent ?", [
        ("« Atelier de réparation, samedi, au centre Sainte-Odile. Gratuit. »",
         "l'heure et quoi apporter"),
        ("« La Nuit des ateliers, vendredi 7 novembre, de 18 h à 21 h. 5 $. »",
         "où, et quoi apporter"),
        ("« Apportez votre vélo au stationnement de l'école Saint-Fidèle, entrée libre. »",
         "quand, et qui organise"),
        ("« Réparation gratuite d'appareils. Rien ne se jette, tout se répare. »",
         "quand, où, quoi apporter, qui organise"),
    ], corrige=True,
       notes="Le quatrième exemple n'a qu'un slogan et une promesse. Faire remarquer "
             "qu'il ne permet à personne de venir.")

    d.pratique('Pratique · 2 de 4', "Classez par niveau",
               "De loin, en s'approchant, en partant.", [
        ("La Grande Réparation", "de loin — c'est le titre"),
        ("Samedi 12 avril", "de loin — la date"),
        ("De 9 h à 16 h, sous-sol du centre Sainte-Odile", "en s'approchant"),
        ("Apportez votre grille-pain, votre lampe ou votre chaise", "en s'approchant"),
        ("Rien ne se jette, tout se répare !", "en partant — le slogan"),
    ], corrige=True,
       notes="Faire dessiner l'affiche au tableau, à main levée, avec les trois tailles. "
             "Cela prend deux minutes et cela clarifie tout.")

    d.piege("Le piège de l'affiche écrite comme une lettre",
            "Bonjour, nous avons le plaisir de vous inviter à notre atelier…",
            "LA GRANDE RÉPARATION — samedi 12 avril",
            "Une affiche n'a ni salutation, ni formule de politesse, ni phrase "
            "d'introduction. Elle commence par ce qu'elle annonce. Les formules polies "
            "appartiennent au courriel, pas au babillard.",
            notes="Relier au module 3, où l'on apprend justement les formules du "
                  "courriel. Chaque support a ses codes.")

    d.piege("Le piège du texte qui déborde",
            "Quatre-vingts mots serrés sur une feuille.",
            "Quarante mots, avec de l'espace autour.",
            "L'espace vide fait partie de l'affiche : c'est lui qui met en valeur ce qui "
            "est écrit. Une feuille pleine de texte se lit comme un règlement, et "
            "personne ne s'arrête devant un règlement.",
            notes="Montrer deux affiches côte à côte : une chargée, une aérée. Le choix "
                  "du groupe est immédiat.")

    d.pratique('Pratique · 3 de 4', "Écrivez votre affiche",
               "Six informations, trois niveaux, un slogan à la fin.", [
        ("L'événement", "celui de votre billet de A1"),
        ("Le titre", "gros, court, avec la date"),
        ("Les informations pratiques", "heure, adresse, prix, quoi apporter"),
        ("La fin", "un slogan ou une promesse"),
    ], corrige=False,
       notes="Trente minutes. Sur papier grand format si possible. Circuler et vérifier "
             "les six informations, pas le dessin.")

    d.pratique('Pratique · 4 de 4', "Le test du corridor",
               "Affichez les affiches au mur. Passez devant en trois secondes.", [
        ("Qu'est-ce que vous avez vu de loin ?", "le titre et la date, normalement"),
        ("Qu'est-ce qui manquait ?", "notez-le sur un papier"),
        ("Est-ce que vous savez quoi apporter ?", "sinon, l'affiche a raté"),
        ("Est-ce que vous vous souvenez du slogan ?", "cinq minutes plus tard"),
    ], corrige=False,
       notes="C'est l'exercice le plus formateur de la séance. Le faire vraiment : "
             "afficher, faire circuler le groupe, puis interroger de mémoire.")

    d.billet(
        "Après le test du corridor : qu'est-ce que vous changeriez dans votre affiche ?",
        exemples=[
            "Une seule chose, précise.",
            "Exemple : « la date était trop petite ».",
        ],
        notes="Les corrections proposées par le groupe valent mieux que les vôtres. "
              "Ramasser et faire refaire l'affiche pour E1 si le temps le permet.")

    return d.save(dossier)
