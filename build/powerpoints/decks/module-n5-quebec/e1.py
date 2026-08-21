# -*- coding: utf-8 -*-
"""E1 · Réserver, et laisser un message
Bloc E « Je me lance » · couleur teal · 75 min. Production orale.
Source : bloc « Je me lance » de l'activité interactive — jeu de rôle
`regions` et production orale (message sur la boîte vocale d'un gîte).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Réserver, et laisser un message",
        chapeau="C'est à vous. Vous exposez votre demande à un préposé au "
                "comptoir des autocars ou à quelqu'un de la région ; puis "
                "vous laissez un message sur la boîte vocale d'un gîte pour "
                "réserver une chambre et poser vos questions.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Elle se fait presque entièrement debout et à "
                  "deux. Prévoir des postes avec écouteurs pour le jeu de rôle avec "
                  "l'assistant, et un coin calme pour l'enregistrement. L'enseignante "
                  "circule et écoute ; elle ne corrige pas pendant.")

    d.objectifs([
        "exposer une demande complète sans attendre qu'on vous questionne ;",
        "poser trois questions polies de suite, avec trois formules différentes ;",
        "laisser un message de trente à quarante-cinq secondes qui n'oublie rien ;",
        "tenir le vouvoiement du début à la fin des deux productions.",
    ], notes="Le premier objectif est le critère principal : si l'assistant doit "
             "demander « quand ? », la demande n'était pas complète. Il le fait exprès, "
             "et c'est ainsi qu'il fait travailler le discours suivi du niveau 5.")

    d.regle("Six informations, dans l'ordre",
            "Où · quand · combien de temps · combien de personnes · les "
            "bagages · le retour.",
            precision="C'est la règle de B4, et c'est la grille du jeu de rôle "
                      "comme celle de la correction.",
            notes="Diapositive à photographier et à laisser projetée pendant tout "
                  "l'atelier. Rendre ici les billets de B1, B2 et B4 : chacun arrive "
                  "avec sa demande et ses trois questions déjà écrites.")

    d.tableau('Trois situations', "Choisissez la vôtre",
              ['La situation', 'Ce qui est en jeu'],
              [["Le comptoir de la gare", "Réserver un aller-retour"],
               ["Le salon du gîte", "Se faire conseiller ses journées"],
               ["Le sentier du parc", "Jaser avec un autre vacancier"]],
              cle=1,
              notes="Les trois cas sont ceux de l'activité interactive. Le premier est "
                    "le plus cadré et le troisième le plus libre : conseiller le "
                    "premier à ceux que la conversation spontanée effraie encore.")

    d.cartes("Ce que fait l'assistant", "Il ne devine rien à votre place", [
        ("Il attend votre demande complète",
         "Il ne vous arrache pas les informations une par une."),
        ("Il redemande le reste en une fois",
         "Si vous ne dites que la ville, il demande quand et combien de temps."),
        ("Il ne donne pas de prix inventé",
         "Il dit que ça dépend de la date, puis il annonce un montant."),
        ("Il vous vouvoie, et il attend la même chose",
         "Ce sont des inconnus, des deux côtés."),
    ], notes="Prévenir le groupe : l'assistant est exigeant exprès. Ce n'est ni une "
             "panne ni de la mauvaise volonté. Ceux qui l'ont compris travaillent "
             "beaucoup mieux dès le deuxième essai.")

    d.tableau('Le message au gîte', "Six morceaux, dans l\'ordre",
              ['Le morceau', "Ce qu'on y met"],
              [["1", "Qui parle, et d'où l'on appelle"],
               ["2", "Les dates, et combien de nuits"],
               ["3", "Combien de personnes"],
               ["4", "Deux questions, posées poliment"],
               ["5", "Comment on arrivera, et à quelle heure"],
               ["6", "Un numéro de téléphone, dit lentement"]],
              cle=1,
              notes="Faire écrire les six lignes avant d'enregistrer. Un message "
                    "improvisé dure quatre-vingt-dix secondes et oublie le numéro ; un "
                    "message écrit d'abord en dure quarante et n'oublie rien.")

    d.piege("Enregistrer sans avoir écrit",
            "Je vais improviser, c'est plus naturel.",
            "J'écris mes six lignes, je les lis une fois, puis j'enregistre.",
            "Un message improvisé oublie presque toujours deux choses : le nombre "
            "de nuits et le numéro de téléphone. Ce sont justement les deux qui "
            "rendent le rappel possible.",
            notes="Insister : lire ses notes n'a rien d'artificiel au téléphone. Tout le "
                  "monde le fait, y compris les gens dont c'est la langue maternelle.")

    d.pratique('Autoévaluation', "Réécoutez-vous comme si vous teniez le gîte",
               "Répondez honnêtement avant d'envoyer.", [
        ("Sait-on qui appelle, et comment vous rappeler ?", "sinon, le message ne sert à rien"),
        ("Peut-on noter les dates et le nombre de nuits ?", "des chiffres, pas « bientôt »"),
        ("Vos questions sont-elles posées poliment ?", "trois formules différentes"),
        ("Le message dure-t-il moins de quarante-cinq secondes ?", "sinon, coupez les excuses"),
        ("Le vouvoiement est-il tenu du début à la fin ?", "sinon, reprenez le début"),
        ("Le numéro est-il dit assez lentement ?", "faites-le vérifier par un voisin"),
    ], corrige=True,
       notes="Faire faire cette autoévaluation avant l'envoi à l'enseignante, pas après. "
             "Les élèves recommencent d'eux-mêmes une fois sur deux, et c'est le but.")

    d.billet(
        "Après votre enregistrement : notez la chose que vous referiez autrement.",
        exemples=[
            "Une seule chose, la plus importante.",
            "Notez aussi ce qui a bien marché : ça se garde pour la prochaine fois.",
        ],
        notes="Ramasser les billets et les rendre en E2 avec la production écrite. La "
              "comparaison entre ce que l'élève a repéré lui-même et ce que dit la "
              "rétroaction vaut mieux qu'une note.")

    return d.save(dossier)
