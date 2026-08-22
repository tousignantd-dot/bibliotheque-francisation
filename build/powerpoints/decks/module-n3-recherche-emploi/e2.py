# -*- coding: utf-8 -*-
"""E2 · Ma petite annonce.
Bloc E « Je me lance » · couleur framboise · 75 min. Production écrite et bilan.
Source du module : exercices `t3annparts` et `aComp`, section « Je retiens des mots ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre='Ma petite annonce',
        chapeau="Six lignes sur un carton, un numéro en gros en bas, et le "
                "quartier sait ce que vous savez faire. C'est le dernier "
                "geste du module, et le seul qui travaille pendant que vous "
                "dormez.",
        duree='75 minutes')

    d.titre(notes="Dernière séance. Prévoir du carton et des crayons feutres : "
                  "l'annonce se termine à la main, et elle repart avec l'élève.")

    d.objectifs([
        "écrire une petite annonce en six lignes ;",
        "protéger ses renseignements personnels ;",
        "réviser le vocabulaire du module ;",
        "évaluer ce qu'on est maintenant capable de faire.",
    ])

    d.tableau('Le plan · 1 de 2', "Les trois premières lignes",
              ['La ligne', 'Ce qu\'elle contient'],
              [["1. Le titre", "MÉNAGE ET GARDE D'ENFANTS, en gros"],
               ["2. Qui je suis", "Je m'appelle… et j'habite dans…"],
               ["3. Ce que je sais faire", "J'ai six ans d'expérience en…"]],
              cle=0,
              note="Le titre nomme le service, jamais la personne.",
              notes="Diapo à photographier, et à laisser affichée pendant l'écriture.")

    d.tableau('Le plan · 2 de 2', "Les trois dernières lignes",
              ['La ligne', 'Ce qu\'elle contient'],
              [["4. Quand je suis libre", "Du lundi au vendredi, de 8 h à 13 h"],
               ["5. Mon prix", "Je demande 20 $ de l'heure"],
               ["6. Mon numéro", "Appelez-moi au 438 555-0192"]],
              cle=0,
              note="Le numéro va toujours en dernier, et plus gros que le reste.",
              notes="Diapo à photographier. Faire vérifier deux fois le numéro : un "
                    "chiffre de travers, et l'annonce ne sert à rien.")

    d.regle("Jamais son adresse complète sur un babillard",
            "Le quartier suffit.",
            precision="Un babillard est public : tout le monde y lit. « J'habite dans "
                      "Saint-Michel » dit que vous êtes proche sans dire où vous "
                      "habitez. Le numéro de téléphone suffit pour vous joindre.",
            notes="Diapo à photographier. Point de sécurité : le dire clairement, une "
                  "fois, sans dramatiser, et vérifier chaque annonce à la fin.")

    d.cartes("Trois choses qui font la différence", "Avant de punaiser", [
        ("Le titre, pas le nom",
         "Celui qui cherche quelqu'un pour son ménage cherche le mot « ménage », pas "
         "votre prénom. Le titre nomme le service, en gros, tout en haut."),
        ("Un prix, même approximatif",
         "Sans montant, on vous appelle pour demander le prix — ou on ne vous appelle "
         "pas. Écrivez un montant, quitte à ajouter « à discuter »."),
        ("Les languettes",
         "Découpez le bas en languettes, avec votre numéro sur chacune. Celui qui "
         "passe en arrache une et l'emporte : il n'a rien à noter."),
        ("Où la punaiser",
         "Épicerie, buanderie, pharmacie, centre communautaire, entrée d'immeuble. "
         "Quatre ou cinq endroits valent mieux qu'un seul très bien choisi."),
    ], notes="Faire nommer par le groupe cinq babillards du quartier, avec les rues. "
             "La liste vaut plus que l'annonce elle-même.")

    d.pratique('Écriture', "Complétez le plan de l'annonce",
               "Complétez avec : titre, nom, expérience, libre, demande, numéro.", [
        ("En haut, on écrit un ___ en grosses lettres.", "titre"),
        ("Ensuite, je donne mon ___ et mon quartier.", "nom"),
        ("J'écris que j'ai six ans d'___ en garde d'enfants.", "expérience"),
        ("Je dis que je suis ___ du lundi au vendredi.", "libre"),
        ("Je ___ 20 $ de l'heure.", "demande"),
        ("Tout en bas, mon ___ de téléphone, en gros.", "numéro"),
    ], corrige=True,
       notes="Même exercice que t3annparts dans le module. Il sert de plan à l'écriture "
             "qui suit : ne pas s'y attarder plus de dix minutes.")

    d.pratique('Production écrite', "Écrivez votre annonce",
               "Six lignes, de 5 à 8 phrases. Puis recopiez-la sur le carton.", [
        ("Le titre", "Le service que vous offrez, en majuscules."),
        ("Vous", "Prénom et quartier. Jamais l'adresse."),
        ("Votre expérience", "Ce que vous savez faire, et depuis combien de temps."),
        ("Vos disponibilités", "Des jours et des heures, comme en B4."),
        ("Votre prix et votre numéro", "Un montant, puis le numéro en gros."),
    ], notes="Trente minutes. Faire vérifier par l'assistant avant de recopier au "
             "propre : la correction reste privée, et seul ce que l'élève envoie "
             "arrive à l'enseignante.")

    d.pratique('Vocabulaire', "Le mot juste, pour finir",
               "Complétez avec un mot du module.", [
        ("Une ___ « On embauche » est collée dans la vitrine.", "affiche"),
        ("J'ai pris deux annonces sur le ___ de l'épicerie.", "babillard"),
        ("Le ___ est de 16,50 $ de l'heure.", "salaire"),
        ("Mon ___ va de 9 h à 13 h, du mardi au samedi.", "horaire"),
        ("Hugo me donne un ___ de demande d'emploi.", "formulaire"),
        ("J'ai punaisé ma petite ___ à côté de la caisse.", "annonce"),
    ], corrige=True,
       notes="Même exercice que aComp dans le module. Enchaîner avec les cartes "
             "mémoire du rail « Mes outils » si le temps le permet.")

    d.billet(
        "Qu'est-ce que vous êtes maintenant capable de faire que vous ne saviez pas faire il y a quatre semaines ?",
        exemples=[
            "Une phrase, la vôtre.",
            "Puis remplissez l'autoévaluation du module.",
        ],
        notes="Cinq minutes. Lire deux ou trois billets à voix haute, sans nommer "
              "personne : c'est la meilleure fin possible pour ce module-là.")

    return d.save(dossier)
