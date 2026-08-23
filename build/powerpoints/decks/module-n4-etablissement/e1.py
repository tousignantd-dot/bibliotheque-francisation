# -*- coding: utf-8 -*-
"""E1 · L'appel, puis le message dans la boîte vocale
Bloc E « Je me lance » · couleur teal · 75 min. Production orale.
Source du module : jeu de rôle `repondeur` (trois situations) et message
laissé dans la boîte vocale du centre.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n4-etablissement/images/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="L'appel, puis le message dans la boîte vocale",
        chapeau="Deux productions orales, dans cet ordre. D'abord un appel "
                "où quelqu'un décroche et pose des questions ; ensuite un "
                "message où personne ne répond et où tout doit sortir du "
                "premier coup.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Elle se fait presque entièrement debout et "
                  "par paires, dos à dos : au téléphone, on ne se voit pas, et se voir "
                  "fausse tout. Prévoir de quoi enregistrer — le téléphone de chaque "
                  "élève suffit.")

    d.objectifs([
        "téléphoner au secrétariat et justifier un retard, une absence ou un abandon ;",
        "répondre aux questions du secrétariat sans perdre le fil ;",
        "laisser un message complet en cinquante secondes ;",
        "redire ce qu'on a compris avant de raccrocher.",
    ], notes="Les deux premiers objectifs se travaillent dans la première demi-heure, "
             "les deux derniers dans la seconde. Ne pas les mélanger : l'appel prépare "
             "le message, pas l'inverse.")

    d.regle("Au téléphone, quelqu'un décroche parfois",
            "L'assistant joue madame Sansregret, au secrétariat. Elle ne "
            "voit rien de vous tant que vous ne vous êtes pas nommé.",
            precision="Si vous dites seulement « je ne peux pas venir », "
                      "elle demandera si c'est un retard, une absence ou un "
                      "abandon, et pour quelle date.",
            notes="Présenter le jeu de rôle du module. Trois situations sont offertes : "
                  "l'enfant malade, l'autobus qui ne passe pas, le cours du soir qu'on "
                  "arrête. Chacun en choisit une, puis en essaie une deuxième.")

    d.cartes("Les trois appels", "Choisissez-en un, puis un autre", [
        ("L'enfant malade",
         "Otite, rendez-vous à neuf heures, absente toute la journée."),
        ("L'autobus qui ne passe pas",
         "Tempête depuis cinq heures, arrivée vers neuf heures et demie."),
        ("Le cours du soir qu'on arrête",
         "Horaires changés, abandon à partir du 1er octobre, francisation gardée."),
        ("Ce qui change d'un appel à l'autre",
         "Le mot de la case, la date, et ce que le secrétariat vous demandera ensuite."),
    ], notes="Faire choisir avant de commencer. Les élèves qui prennent le troisième "
             "sont souvent ceux que la situation concerne vraiment : leur laisser le "
             "temps, et ne pas les faire passer devant le groupe.")

    d.tableau('Les neuf choses à faire', "Avant de raccrocher",
              ['À quel moment', 'Ce que vous faites'],
              [["Dès le bonjour", "Votre nom et votre groupe."],
               ["Tout de suite après", "Le mot : retard, absence ou abandon."],
               ["Puis", "La date exacte, jamais « aujourd'hui » seul."],
               ["Puis", "Le motif en une phrase, avec parce que ou à cause de."],
               ["Vous demandez", "Quel papier apporter, et pour quand."],
               ["Vous promettez", "Au futur : je serai, je remettrai, je rattraperai."],
               ["Avant de raccrocher", "Vous redites ce que vous avez compris."]],
              cle=1,
              notes="Grille d'observation pour celui qui écoute dans la paire. Lui "
                    "donner la feuille et lui demander de cocher : c'est lui qui "
                    "corrige, pas l'enseignant.")

    d.declencheur(
        'Mise en situation', "Sept heures dix, la boîte vocale se déclenche. "
                             "Vous avez une minute.",
        image=img('appel-cage-escalier.jpg'),
        pistes=[
            "Vous avez votre texte sous les yeux : lisez-le une fois pour vous.",
            "Puis retournez la feuille et dites-le sans regarder.",
            "Enregistrez-vous avec votre téléphone.",
            "Réécoutez-vous : sauriez-vous écrire votre propre numéro ?",
        ],
        notes="La quatrième piste est le vrai critère. Faire écouter deux ou trois "
              "enregistrements au groupe, avec l'accord de l'élève, et demander à "
              "chaque fois d'écrire le nom et le numéro entendus.")

    d.regle("Cinquante secondes, cinq morceaux",
            "Qui vous êtes. Le mot et la date. Le motif. Ce que vous ferez. "
            "Votre numéro, deux fois.",
            precision="Si vous dépassez, coupez dans le motif — jamais dans "
                      "le numéro.",
            notes="C'est la règle de B1 et de B4, reprise une dernière fois comme grille "
                  "d'évaluation. La laisser affichée pendant tous les enregistrements.")

    d.pratique('Production orale', "Votre message, enregistré",
               "Cinq morceaux, entre quarante-cinq et soixante secondes.", [
        ("Morceau 1", "Bonjour, ici (nom complet), groupe (numéro), francisation."),
        ("Morceau 2", "Je vous appelle pour signaler (le mot), (la date exacte)."),
        ("Morceau 3", "Le motif, une seule phrase, avec parce que ou à cause de."),
        ("Morceau 4", "Ce que vous ferez, au futur simple."),
        ("Morceau 5", "Mon numéro est le (...). Je répète : (...). Merci, bonne journée."),
    ], notes="Faire enregistrer dans le module, où l'assistant rend une rétroaction "
             "immédiate. Les élèves qui le souhaitent envoient l'enregistrement à "
             "l'enseignant ; rien ne part sans leur geste.")

    d.piege("Lire son texte au lieu de le dire",
            "On entend le papier : la voix descend à chaque fin de ligne.",
            "Vous retournez la feuille et vous dites les cinq morceaux de mémoire.",
            "Un message lu s'entend tout de suite, et il est plus difficile à "
            "comprendre qu'un message dit : les phrases y sont plates et les "
            "chiffres passent trop vite. Retournez la feuille.",
            notes="Ne pas en faire un interdit : lire une fois pour se rassurer est "
                  "utile. C'est le deuxième enregistrement qui se fait sans papier.")

    d.pratique('Écoute croisée', "Ce que votre voisin a compris",
               "Écoutez l'enregistrement d'un camarade et écrivez trois choses.", [
        ("Le nom", "Écrivez-le. Pouviez-vous l'écrire du premier coup ?"),
        ("Le groupe", "Un chiffre. L'avez-vous entendu ?"),
        ("La date", "Le jour et le quantième, pas « aujourd'hui »."),
        ("Le motif", "En une phrase. Était-elle courte ?"),
        ("Le numéro", "Dix chiffres. Avez-vous pu les écrire ?"),
    ], notes="C'est le meilleur exercice de la séance et le plus court. Ce que le "
             "voisin n'a pas pu écrire est exactement ce qu'il faut redire plus "
             "lentement. Personne ne discute ce verdict-là.")

    d.billet(
        "Écrivez ce que vous changeriez dans votre message si vous le "
        "refaisiez maintenant.",
        exemples=[
            "Une seule chose, la plus importante.",
            "Le plus souvent : dire le nom et le numéro plus lentement.",
        ],
        notes="Ramasser. Ceux qui écrivent « rien » n'ont pas fait l'écoute croisée : "
              "les faire refaire avec un autre voisin au début de E2.")

    return d.save(dossier)
