# -*- coding: utf-8 -*-
"""E2 · Le carton du babillard, et les seize mots
Bloc E « Je me lance » · couleur framboise · 75 min.
Production écrite, puis bilan du module.
Source : bloc « Je me lance » (le babillard des coups de cœur) et « Je
retiens des mots ».
"""
import pathlib

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-oeuvres/images/')


def photo(nom):
    """La photo si elle est sur le disque, None sinon — voir a1.py."""
    p = pathlib.Path(IMG + nom)
    return str(p) if p.exists() else None


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Le carton du babillard, et les seize mots",
        chapeau="Dernière séance. À l'entrée de la bibliothèque, un "
                "babillard porte les coups de cœur des membres du club. Vous "
                "écrivez le vôtre — pour des gens que vous ne connaissez "
                "pas, qui le liront debout, en attendant leur tour.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Prévoir quarante minutes d'écriture en "
                  "silence, puis le bilan. Rendre au début les billets de E1 et les "
                  "rétroactions des productions orales : la comparaison est le vrai "
                  "moment d'apprentissage de la séance.")

    d.objectifs([
        "écrire une recommandation de sept à dix phrases ;",
        "raconter le début au présent, sans la fin ;",
        "reprendre l'œuvre par un autre mot à chaque fois ;",
        "faire le point sur ce qu'on est maintenant capable de faire.",
    ], notes="Le carton porte la même œuvre que la présentation de E1 : c'est voulu. "
             "Écrire deux fois la même chose, une fois pour l'oreille et une fois "
             "pour l'œil, est ce qui fait sentir la différence entre les deux.")

    d.declencheur(
        'Observation', "Qui lit ce babillard, et comment ?",
        image=photo('comptoir-coups-de-coeur.jpg'),
        pistes=[
            "Combien de temps quelqu'un s'arrête-t-il devant un carton ?",
            "Est-ce qu'on lit debout comme on lit assis ?",
            "Qu'est-ce qui vous ferait prendre le livre ?",
            "À qui écrivez-vous, si vous ne savez pas qui lira ?",
        ],
        notes="La dernière question donne le vouvoiement : on ne connaît pas son "
              "lecteur, donc on le vouvoie. C'est aussi la réponse à la question du "
              "registre, qui revient à chaque production écrite du niveau 5.")

    d.regle("On écrit pour quelqu'un qui lit debout",
            "Sept à dix phrases, avec « vous ». La première dit de quoi il s'agit.",
            precision="Personne ne lit trois phrases de contexte devant un babillard. "
                      "Le support et le genre viennent dès la première phrase — un "
                      "roman, une bande dessinée, une série — et le reste suit.",
            notes="Diapositive à photographier. Faire écrire deux premières phrases au "
                  "tableau, une qui commence par le support et une qui commence par "
                  "l'histoire, et faire choisir. Le groupe choisit la première.")

    d.tableau('Le carton', "Sept exigences, annoncées d'avance",
              ["La partie", "Ce qu'on y met"],
              [["La première phrase", "le support et le genre"],
               ["Le début de l'histoire", "deux phrases au présent, sans la fin"],
               ["Une relative", "une phrase avec qui, que ou où"],
               ["Une reprise", "cette histoire, ce livre, cette œuvre"],
               ["L'avis mis en avant", "ce qui m'a touché, c'est… — avec sa raison"],
               ["La fin", "à qui vous le recommandez, et votre prénom"]],
              cle=1,
              notes="Six des sept points de la liste en ligne. Le septième est "
                    "l'exclamation avec quel, quelle, quels ou quelles : l'écrire au "
                    "tableau à côté, parce que c'est celui qu'on oublie. Annoncer les "
                    "critères avant l'écriture, jamais après.")

    d.cartes("Les quatre défis, dans un seul carton", "D'où vient chaque phrase", [
        ("Le support et le genre",
         "Bloc A — un roman, une série, une bande dessinée, une chanson."),
        ("Le présent et les relatives",
         "Défi 1 — elle arrive, elle ouvre ; une femme qui revient."),
        ("La reprise sans répétition",
         "Défi 2 — cet album, cette histoire, ce premier tome."),
        ("L'avis en avant, et l'exclamation",
         "Défi 3 — moi, ce qui m'a touchée, c'est… Quelle fin !"),
    ], notes="Diapositive à photographier. Le module entier tient dans ces quatre "
             "cartes, et le carton du babillard est le seul endroit où les quatre se "
             "rencontrent. Le dire au groupe avant l'écriture.")

    d.piege("Raconter jusqu'à la fin",
            "…et à la fin, elle décide de rester dans le village.",
            "Elle ouvre la maison et elle trouve une boîte de lettres. Je m'arrête ici.",
            "Un carton qui raconte tout n'est plus une recommandation : c'est un "
            "résumé, et le livre reste sur le rayon. La règle du club vaut aussi à "
            "l'écrit, et elle vaut même davantage — l'écrit se relit.",
            notes="C'est la faute la plus fréquente de cette production, et elle vient "
                  "d'une bonne intention : on veut être complet. Le nommer ainsi aide "
                  "les élèves à la voir.")

    d.vocabulaire('Bilan du vocabulaire', "Huit des seize mots, une dernière fois", [
        ("une œuvre", "Ce que quelqu'un a écrit, filmé, dessiné ou composé."),
        ("l'intrigue", "Ce qui arrive dans l'histoire, du début à la fin."),
        ("le dénouement", "La fin de l'histoire : ce qu'on ne raconte jamais au club."),
        ("un personnage", "Quelqu'un qui vit dans l'histoire."),
        ("une case", "Le petit carré dessiné d'une bande dessinée."),
        ("une bulle", "La forme où l'on met ce qu'un personnage dit."),
        ("émouvant", "Qui touche, qui serre le cœur sans être triste."),
        ("recommander", "Conseiller une œuvre à quelqu'un, en disant pourquoi à lui."),
    ], notes="Huit des seize, ceux que le relevé montre comme les moins sûrs. Faire "
             "dire chaque mot avec son article et une phrase. Les huit autres se "
             "révisent avec les cartes mémoire de l'activité.")

    d.pratique('Bilan', "Êtes-vous maintenant capable de… ?",
               "Répondez pour vous-même, honnêtement.", [
        ("Nommer une œuvre et son support ?", "un roman, une série, un album"),
        ("Raconter une histoire au présent, dans l'ordre ?", "elle arrive, elle ouvre"),
        ("Vous arrêter avant le dénouement ?", "au moment du choix"),
        ("Lire une planche de bande dessinée ?", "les cases, les bulles, les onomatopées"),
        ("Donner un avis avec un adjectif précis ?", "jamais « c'est bon »"),
        ("Répondre à quelqu'un qui pense autrement ?", "accorder, puis tourner"),
    ], corrige=True,
       notes="Faire cocher individuellement, sans ramasser. Proposer à ceux qui "
             "hésitent sur deux points ou plus de refaire le défi correspondant dans "
             "l'activité interactive : elle reste ouverte après la fin du module.")

    d.billet(
        "En une phrase : quelle œuvre apporteriez-vous au club jeudi prochain ?",
        exemples=[
            "Une vraie œuvre, dans n'importe quelle langue.",
            "Gardez ce billet : c'est le seul du module qui ne se corrige pas.",
        ],
        notes="Ne pas ramasser celui-ci. Le module a commencé par une femme qui "
              "relisait trois fois une affiche sans oser entrer ; il se termine par "
              "la même invitation, adressée à chacun.")

    return d.save(dossier)
