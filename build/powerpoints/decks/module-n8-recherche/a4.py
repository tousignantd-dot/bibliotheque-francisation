# -*- coding: utf-8 -*-
"""A4 · Reprendre sans répéter
Bloc A « Je découvre » · couleur ambre · 75 min.
Source : exercice `prRepr` et sa mini-leçon. Savoir du niveau 8 : employer
des procédés de substitution lexicale pour reprendre un groupe du nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Ce rachat, cette acquisition, cet isolement",
        chapeau="Le français ne répète pas : il reprend. C'est ce qui rend "
                "un texte d'entreprise élégant à écrire, et difficile à lire "
                "quand on ne reconnaît pas la reprise.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire du texte, la première du module. Annoncer "
                  "d'emblée qu'elle sert deux fois : à écrire mieux, et surtout à "
                  "lire les deux documents du bloc C.")

    d.objectifs([
        "reconnaître une reprise et retrouver ce qu'elle reprend ;",
        "employer les quatre procédés : nominalisation, synonyme, générique, expression synthétique ;",
        "repérer le démonstratif comme signal d'une reprise ;",
        "résumer une situation entière en un seul groupe du nom.",
    ], notes="Le quatrième objectif est le plus difficile et le plus payant : c'est "
             "celui qui servira en entrevue, au défi 3.")

    d.declencheur(
        'Observation', "Combien de fois « l'usine » est-elle nommée ?",
        pistes=[
            "« Le Groupe Landron a racheté l'usine en janvier. »",
            "« Ce rachat a été annoncé aux employés le même jour. »",
            "« Cette acquisition n'a entraîné aucune mise à pied. »",
            "Trois phrases, un seul événement. Comment le sait-on ?",
        ],
        notes="Laisser chercher. La réponse est dans les démonstratifs : « ce », "
              "« cette ». Ils disent « j'en ai déjà parlé », et c'est tout le savoir "
              "de la séance.")

    d.regle("Le démonstratif est le signal",
            "Presque toutes les reprises commencent par ce, cet, cette ou "
            "ces. Quand vous en voyez un devant un mot qui n'a jamais été "
            "écrit avant, remontez d'une phrase et cherchez le verbe.",
            precision="C'est une méthode de lecture, pas une règle de grammaire. Elle "
                      "vaut pour un profil d'entreprise, un contrat, une lettre de "
                      "refus : partout où une phrase résiste, le démonstratif dit où "
                      "chercher.",
            notes="Diapositive à photographier. Faire l'essai tout de suite sur les "
                  "trois phrases du déclencheur.")

    d.cartes('Analyse', "Les quatre procédés", [
        ("Par nominalisation",
         "Le verbe de la première phrase devient un nom. Le groupe a racheté "
         "l'usine, ce rachat. C'est la reprise la plus fréquente dans les "
         "écrits d'entreprise."),
        ("Par synonymie",
         "On remplace par un mot de sens voisin. Le rachat, cette "
         "acquisition. Attention : le mot choisi colore la phrase — un "
         "employeur écrit « acquisition », un syndicat écrit « rachat »."),
        ("Par un générique",
         "On remonte d'un cran : le tri, l'examen, l'entrevue de groupe, ces "
         "trois étapes. Souvent précédé d'un nombre."),
        ("Par une expression synthétique",
         "Toute une phrase se résume en un groupe du nom. Après dix-huit "
         "heures il n'y a plus personne, cet isolement. La plus difficile, "
         "et la plus utile en entrevue."),
    ], notes="Faire trouver un exemple de chaque procédé dans le dialogue de A1. Il y "
             "en a au moins un de chaque.")

    d.tableau('Analyse', "Les fabriques de noms",
              ['Suffixe', 'Du verbe au nom'],
              [["-tion, -sion",
                "réorganiser donne la réorganisation, décider donne la décision"],
               ["-ment",
                "recruter donne le recrutement, isoler donne l'isolement"],
               ["-ance, -ence",
                "croître donne la croissance, exiger donne l'exigence"],
               ["-ure",
                "fermer donne la fermeture, ouvrir donne l'ouverture"],
               ["aucun suffixe",
                "racheter donne le rachat, embaucher donne l'embauche"]],
              cle=0,
              notes="Diapositive à photographier. Les noms sans suffixe s'apprennent un "
                    "par un : il n'y a pas de règle, et c'est là que les élèves "
                    "avancés butent encore.")

    d.pratique('Pratique 1 de 2', "Le nom caché sous le verbe",
               "Écrivez le nom qui reprend le verbe souligné.", [
        ("Le Groupe Landron a racheté l'usine. Ce ___ date de janvier.", "rachat"),
        ("L'entreprise recrute neuf personnes. Ce ___ occupera le poste.", "recrutement"),
        ("La production a été réorganisée. Cette ___ a créé le quart de soir.", "réorganisation"),
        ("On a fermé une ligne onze jours. Cette ___ a coûté très cher.", "fermeture"),
        ("Le carnet a doublé en dix-huit mois. Cette ___ explique tout.", "croissance / hausse"),
    ], corrige=True,
       notes="La dernière accepte plusieurs réponses. Le dire avant de corriger, sinon "
             "les élèves qui ont écrit « hausse » se croient dans l'erreur.")

    d.pratique('Pratique 2 de 2', "Résumer une situation en un mot",
               "Trouvez le groupe du nom qui reprend toute la phrase.", [
        ("Après dix-huit heures, il n'y a plus personne sur place.", "cet isolement"),
        ("Onze ans de supervision là-bas, cinq ans d'exécution ici.", "cette situation / ce parcours"),
        ("Neuf personnes à recruter avant février.", "cette échéance"),
        ("Madame Éthier et monsieur Bourbonnais reçoivent la candidate.", "ces deux personnes"),
    ], corrige=True,
       notes="Le plus difficile de la séance. Accepter toute réponse défendable : le "
             "but est de nommer, pas de trouver LE mot. Nommer, c'est déjà commencer "
             "à répondre — et c'est ce que fera Shirin devant le comité.")

    d.piege('Piège', "reprendre par un mot qui change le sens",
            "choisir un synonyme vraiment voisin",
            "Écrire « ce problème » à la place de « cette réorganisation » "
            "n'est pas une reprise : c'est un jugement ajouté en cachette. "
            "Dans une lettre d'affaires ou en entrevue, ce genre de glissement "
            "se remarque, et il se retourne contre celui qui l'a écrit.",
            notes="Exemple à faire sentir : « ce rachat » et « cette prise de "
                  "contrôle » désignent le même fait et ne disent pas la même chose.")

    d.billet(
        "Prenez trois phrases d'une annonce ou d'un site d'entreprise, et écrivez la reprise de chacune.",
        exemples=[
            "Une par nominalisation, une par synonyme, une par expression synthétique.",
            "Chacune doit commencer par un démonstratif.",
        ],
        notes="Devoir écrit court. Les trois reprises se relisent en début de B1, en "
              "cinq minutes, avant d'entrer dans l'appel de présélection.")

    return d.save(dossier)
