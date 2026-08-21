# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots.
Bloc E « Je me lance » · couleur framboise · 60 min.
Source : banc `FC_CARDS`, cartes mémoire et autoévaluation du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre='Je retiens des mots',
        chapeau="Seize mots, quatre familles, et une question : qu'est-ce que "
                "je suis maintenant capable de faire au comptoir d'un bureau "
                "de poste ?",
        duree='60 minutes')

    d.titre(notes="Dernière séance du module. Prévoir les cartes mémoire du module "
                  "interactif : la révision se fait à l'écran, en paires.")

    d.objectifs([
        "revoir les seize mots du module, par familles ;",
        "employer chaque mot dans une phrase ;",
        "évaluer ce qu'on est capable de faire ;",
        "nommer ce qui reste à travailler.",
    ])

    d.cartes("L'endroit et l'envoi", "Six mots", [
        ("un bureau de poste, un préposé",
         "L'endroit et la personne. Ce sont les deux mots qui nomment la situation "
         "entière du module."),
        ("un timbre, affranchir",
         "Le petit papier collant, et le verbe qui dit qu'on a payé le voyage. Une "
         "lettre sans timbre n'est pas affranchie : elle revient."),
        ("un envoi, un colis",
         "Tout ce qu'on confie à la poste, et la boîte en particulier. Le premier "
         "mot contient le second."),
        ("une balance, un reçu",
         "L'appareil qui décide d'une partie du prix, et le papier qu'on garde. Le "
         "numéro de repérage est écrit sur le reçu."),
    ], notes="Faire dire chaque mot avec son article, puis dans une phrase complète. "
             "« Affranchir » est le seul verbe : le faire conjuguer une fois au présent.")

    d.cartes("L'adresse et les services", "Six mots", [
        ("l'expéditeur, le destinataire",
         "Celui qui envoie, celui qui reçoit. En haut à gauche pour le premier, au "
         "milieu et en plus gros pour le second."),
        ("le code postal, le repérage",
         "Les six caractères qui disent où livrer, et le numéro qui permet de suivre "
         "la boîte sur Internet. Le repérage est compris, il ne se paie pas."),
        ("un avis de livraison",
         "Le carton laissé dans la boîte aux lettres quand un colis attend. Quinze "
         "jours, puis il repart à l'expéditeur."),
        ("le courrier recommandé, un mandat-poste",
         "Le service avec signature, pour les papiers importants, et le papier qui "
         "vaut de l'argent, pour ne pas envoyer de comptant."),
    ], notes="Les quatre paires se répondent deux à deux. Faire chercher au groupe une "
             "situation réelle pour chacune des huit entrées.")

    d.vocabulaire('Les mots qui restent', "Deux mots et une phrase", [
        ("fragile", "Qui casse facilement : du verre, une assiette, un cadre."),
        ("un jour ouvrable", "Du lundi au vendredi, sans les jours fériés."),
        ("rien de fragile", "La réponse aux trois questions de sécurité du comptoir."),
        ("Je vais le prendre.", "L'annonce du choix, en trois mots."),
        ("Est-ce que vous pouvez répéter ?", "La phrase qui sauve tout le reste."),
    ], notes="Les trois dernières lignes ne sont pas des mots mais des phrases toutes "
             "faites : c'est ce que le programme appelle des énoncés-types, et elles "
             "valent autant que le vocabulaire.")

    d.tableau('Autoévaluation', "Ce que je suis capable de faire",
              ['La tâche', 'Le défi'],
              [["Demander le prix et le délai avant de choisir", "défi 1"],
               ["Dire ce qu'il y a dans une boîte", "défi 2"],
               ["Annoncer mon choix et demander autre chose", "défi 2"],
               ["Lire un avis de livraison", "défi 3"],
               ["Demander un service au comptoir", "défi 3"]],
              cle=0, props=[0.74, 0.26],
              note="Cochez ce que vous savez faire, et entourez ce qui reste à travailler.",
              notes="Diapo à photographier. Faire remplir individuellement, en silence, "
                    "cinq minutes. Ramasser : c'est la trace la plus utile pour la "
                    "suite du parcours de chaque élève.")

    d.pratique('Révision', "Le mot juste",
               "Complétez avec un mot du bureau de poste.", [
        ("La personne qui envoie le colis est l' ___ .", "expéditeur"),
        ("La personne qui reçoit le colis est le ___ .", "destinataire"),
        ("Les six caractères comme G1J 3K7 forment le code ___ .", "postal"),
        ("Le petit carton laissé dans la boîte aux lettres est un ___ de livraison.", "avis"),
        ("Le numéro qui permet de suivre le colis sur Internet est le ___ .", "repérage"),
        ("Coller un timbre ou payer au comptoir, c'est ___ son envoi.", "affranchir"),
    ], corrige=True,
       notes="C'est l'exercice `aComp` du module, revu une dernière fois. Les élèves "
             "l'ont déjà vu en A3 : comparer les deux résultats est un bon indicateur "
             "de progrès, et ça se dit au groupe.")

    d.piege(
        "Le dernier rappel",
        "jeter le carton avec les circulaires",
        "le garder et aller au comptoir dans les quinze jours",
        "C'est l'erreur la plus coûteuse du module, et elle n'a rien à voir avec la "
        "langue : le carton ressemble à de la publicité. Une fois qu'on sait ce que "
        "c'est, on ne se trompe plus jamais.",
        notes="Terminer là-dessus. C'est l'information que les élèves rapporteront chez "
              "eux et qu'ils diront à leurs voisins, ce qui est exactement l'effet "
              "recherché.")

    d.billet(
        "Écrivez une chose que vous irez faire au bureau de poste cette année.",
        exemples=[
            "Envoyer, ramasser, acheter, demander un service ?",
            "Quels mots du module allez-vous employer ?",
        ],
        notes="Dernier billet du module. Le lire à voix haute pour ceux qui le veulent : "
              "c'est une bonne façon de fermer les seize séances.")

    return d.save(dossier)
