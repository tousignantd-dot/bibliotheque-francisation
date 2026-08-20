# -*- coding: utf-8 -*-
"""C1 · À l'arrêt d'autobus.
Bloc C « Défi 2 · L'autobus et l'horaire » · couleur acier · 75 min.
Source : dialogue `t2`, exercices `t2vf`, `t2horaire`, mini-leçon `t2horaire`.

Trois questions font tout le défi : est-ce le bon arrêt, à quelle heure passe
le prochain, et à quelle heure passe le dernier. La troisième est celle qu'on
oublie, et c'est celle qui coûte le plus cher.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-autobus/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="À l'arrêt d'autobus",
        chapeau="Trois questions suffisent : est-ce le bon arrêt, à quelle "
                "heure passe le prochain, et à quelle heure passe le dernier.",
        duree='75 minutes')

    d.titre(notes="Demander au groupe qui prend l'autobus pour venir au centre. Les faire "
                  "dire le numéro de leur ligne : ce sont ces numéros-là qu'on emploiera "
                  "dans les exercices.")

    d.objectifs([
        "vérifier qu'on est au bon arrêt ;",
        "demander l'heure du prochain passage ;",
        "comprendre « aux quinze minutes » ;",
        "demander l'heure du dernier autobus.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'on voit à un arrêt ?",
        image=IMG + 'arret-autobus.jpg',
        pistes=[
            "Qu'est-ce qui est affiché sur le poteau ?",
            "Comment sait-on quel autobus passe ici ?",
            "Comment sait-on dans quelle direction il va ?",
            "Que fait-on si on n'est pas sûr ?",
        ],
        notes="Amener l'idée qu'un arrêt porte deux informations : le numéro de la ligne "
              "et la direction. Le deuxième est celui qu'on oublie de vérifier.")

    d.dialogue('Dialogue · 1 de 2', "Le prochain autobus", [
        ("HASSAN", "Bonjour. Est-ce que le 51 passe ici ?", True),
        ("CLAUDE", "Oui, c'est bien l'arrêt du 51.", True),
        ("HASSAN", "Il passe à quelle heure ?", True),
        ("CLAUDE", "Aux quinze minutes. Le prochain est à huit heures dix.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire remarquer que Hassan vérifie d'abord l'arrêt, ensuite l'heure. L'ordre "
             "compte : demander l'heure d'un autobus qui ne passe pas là ne sert à rien.")

    d.dialogue('Dialogue · 2 de 2', "Et le dernier ?", [
        ("HASSAN", "Huit heures dix… ou huit heures et demie ?", True),
        ("CLAUDE", "Huit heures dix. Dans cinq minutes.", True),
        ("HASSAN", "Merci. Et le dernier, le soir ?", True),
        ("CLAUDE", "Onze heures et quart. Après, il n'y en a plus.", True),
    ], notes="Deux choses à souligner : Hassan fait répéter l'heure quand il hésite, et il "
             "pense à demander le dernier passage. Les deux sont des réflexes à installer.")

    d.tableau('Analyse', "Les trois questions",
              ['La question', 'Pourquoi'],
              [["Est-ce que le 51 passe ici ?", "pour vérifier l'arrêt"],
               ["Il passe à quelle heure ?", "pour savoir combien attendre"],
               ["Et le dernier, le soir ?", "pour ne pas rentrer à pied"]],
              cle=2,
              note="La troisième est celle qu'on oublie. C'est aussi celle qui coûte le "
                   "plus cher quand on l'oublie.",
              notes="Diapositive à photographier. Faire dire les trois questions par chaque "
                    "élève, dans l'ordre.")

    d.regle("Aux quinze minutes",
            "Une expression d'ici, à connaître.",
            precision="« Il passe <b>aux quinze minutes</b> » veut dire : toutes les "
                      "quinze minutes — 8 h, 8 h 15, 8 h 30, 8 h 45…",
            notes="Diapositive à photographier. Écrire la suite des heures au tableau : "
                  "c'est en la voyant écrite que l'expression devient claire.")

    d.piege('Piège', "« dans cinq minutes » = « à cinq heures »",
            "« dans » compte à partir de maintenant",
            "<b>Dans</b> cinq minutes : à partir du moment où on parle. <b>À</b> cinq "
            "heures : une heure fixe sur l'horloge. Les deux ne se confondent jamais.",
            notes="Reprise du piège de A2, dans un vrai contexte. Trois minutes suffisent.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("C'est bien l'arrêt du 51.", "vrai"),
        ("Le 51 passe aux trente minutes.", "faux — aux quinze minutes"),
        ("Le prochain passe dans cinq minutes.", "vrai"),
        ("Le dernier passe à minuit.", "faux — à onze heures et quart"),
    ], corrige=True, cols=1,
       notes="Faire d'abord à l'oral, sans le texte du dialogue sous les yeux.")

    d.pratique('Pratique · à deux', "À l'arrêt",
               "Deux par deux. L'un attend, l'autre connaît la ligne.", [
        ("Étape 1", "Vérifiez que c'est le bon arrêt."),
        ("Étape 2", "Demandez l'heure du prochain passage."),
        ("Étape 3", "Faites répéter l'heure pour être sûr."),
        ("Étape 4", "Demandez l'heure du dernier autobus, puis remerciez."),
    ], cols=1,
       notes="Vingt-cinq minutes. Donner à chaque paire un numéro de ligne réel du "
             "quartier et une heure de départ : la contrainte rend l'échange concret.")

    d.billet(
        "Trouvez l'heure du dernier autobus de votre ligne.",
        exemples=[
            "Regardez l'horaire à l'arrêt, ou demandez à quelqu'un.",
            "Écrivez le numéro de la ligne et l'heure.",
        ],
        notes="Devoir de terrain. Plusieurs découvriront que leur ligne s'arrête plus tôt "
              "qu'ils ne le croyaient.")

    return d.save(dossier)
