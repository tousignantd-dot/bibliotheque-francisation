# -*- coding: utf-8 -*-
"""E1 · L'appel au complet.
Bloc E « Je me lance » · couleur teal · 75 min.
Source : jeu de rôle `demenagement` et production orale de `custom.js`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="L'appel au complet",
        chapeau="Vous avez la situation ; l'autre a les tarifs. À vous d'aller "
                "les chercher.",
        duree='75 minutes')

    d.titre(notes="Première séance de production. Elle se fait aux postes : le jeu de rôle "
                  "avec l'assistant d'abord, la production orale ensuite. Prévoir des "
                  "écouteurs.")

    d.objectifs([
        "mener un appel de déménagement du début à la fin ;",
        "couvrir les sept sujets sans en oublier un ;",
        "tenir les deux rôles : demander et expliquer ;",
        "se présenter à voix haute à une nouvelle voisine.",
    ])

    d.tableau('Les sept sujets · 1 de 2', "La situation",
              ['Le sujet', 'Ce que ça veut dire'],
              [["La date et les adresses", "le jour, l'heure, d'où on part, où on va"],
               ["L'étage et l'escalier", "avec ou sans ascenseur, escalier intérieur ou non"],
               ["Ce qu'il y a de gros", "un piano, un congélateur, un divan qui ne passe pas"]],
              cle=0,
              note="Trois situations au choix : le 3 ½ du deuxième, le 4 ½ avec un piano, "
                   "le camion sans chauffeur.",
              notes="Projeter pendant tout le jeu de rôle. Les élèves cochent au fur et à "
                    "mesure — c'est la grille d'autoévaluation de l'exercice.")

    d.tableau('Les sept sujets · 2 de 2', "L'argent, et la vérification",
              ['Le sujet', 'Ce que ça veut dire'],
              [["Le tarif", "et surtout ce qui s'ajoute au tarif"],
               ["L'assurance", "ce que couvre la base, ce que coûte la protection complète"],
               ["Le dépôt", "combien, et jusqu'à quand on peut annuler"],
               ["La répétition", "redire la date et l'heure avant de raccrocher"]],
              cle=0,
              notes="Les quatre sujets que l'élève doit aller chercher lui-même : "
                    "l'assistant ne les donne jamais spontanément.")

    d.cartes("Ce que vous avez appris, et qui doit ressortir", "Cinq choses à replacer", [
        ("La question qui rapporte",
         "Est-ce qu'il y a autre chose qui s'ajoute au tarif ?"),
        ("Les pronoms",
         "Le camion ? Je le réserve aujourd'hui. Des boîtes, j'en ai quinze."),
        ("Les prépositions de temps",
         "Le logement est libre à partir du premier juillet."),
        ("La durée",
         "Ils ont tout monté en quatre heures, la dernière fois."),
        ("La vérification finale",
         "Donc le premier juillet, huit heures, cent dollars de dépôt. C'est bien ça ?"),
    ], notes="Écrire ces cinq phrases au tableau pendant l'activité. Les élèves y "
             "reviennent quand ils bloquent.")

    d.regle("L'assistant ne donne rien avant qu'on le lui demande",
            "Les tarifs sont de son côté. La question est du vôtre.",
            precision="C'est voulu : dans un vrai appel, personne ne récite ses "
                      "suppléments. Un appel où l'élève ne pose aucune question se "
                      "termine sans qu'il connaisse le prix réel.",
            notes="Le dire avant de commencer, sinon plusieurs attendent que l'information "
                  "vienne. Un premier appel raté est une bonne leçon : le refaire tout de "
                  "suite.")

    d.piege("Raccrocher sans répéter la date",
            "Bon, parfait, merci, au revoir.",
            "Donc le premier juillet, huit heures, au 340 avenue Royale. C'est bien ça ?",
            "C'est la dernière chose de l'appel et la première qu'on oublie. Une date mal "
            "comprise, c'est un camion qui arrive un autre jour — et le premier juillet, "
            "il n'y a pas de deuxième chance.",
            notes="Faire écouter deux appels d'élèves jusqu'au bout et compter combien "
                  "répètent la date. Le résultat est parlant.")

    d.pratique('Jeu de rôle', "Les deux rôles, l'un après l'autre",
               "Vingt minutes par élève : d'abord la personne qui déménage, puis la "
               "répartitrice.", [
        ("Rôle 1 · la personne qui déménage",
         "Vous expliquez votre situation et allez chercher les prix."),
        ("Rôle 2 · la répartitrice",
         "Vous expliquez les tarifs en phrases suivies, avec « parce que », « donc »."),
        ("Situation A · le 3 ½ du deuxième", "Escalier extérieur qui tourne, quinze boîtes."),
        ("Situation B · le 4 ½ avec un piano", "Un piano droit, un congélateur plein."),
        ("Situation C · le camion sans chauffeur", "Trois amis pour aider, aucune idée de la grandeur."),
        ("À la fin", "« J'ai fini — corrigez mes phrases » pour obtenir la rétroaction."),
    ], corrige=False,
       notes="Le deuxième rôle est le plus formateur : expliquer un tarif demande des "
             "phrases reliées, ce que le programme vise au niveau 5.")

    d.pratique('Production orale', "Le lendemain, dans l'escalier",
               "Une minute d'enregistrement, en quatre temps.", [
        ("Temps 1 · se présenter", "Bonjour, je m'appelle… je viens d'emménager dans le 4."),
        ("Temps 2 · s'excuser en racontant",
         "Excusez-nous pour hier : le camion est arrivé en retard, et il pleuvait."),
        ("Temps 3 · demander comment ça fonctionne",
         "La salle de lavage, ça marche comment ? Et le bac brun, c'est quel jour ?"),
        ("Temps 4 · répondre à l'invitation",
         "C'est gentil. Malheureusement je travaille dimanche. Par contre, dimanche prochain…"),
        ("Puis", "S'écouter, corriger, recommencer autant de fois qu'on veut."),
        ("Enfin", "Envoyer à l'enseignante quand on est satisfait de sa version."),
    ], corrige=False,
       notes="Le temps 2 réemploie le passé composé et l'imparfait de D2 ; le temps 4, "
             "l'acte de parole de la même séance. Le dire aux élèves : ils entendent mieux "
             "leur progrès quand on le nomme.")

    d.billet(
        "Après votre enregistrement : qu'est-ce que vous referiez autrement ?",
        exemples=[
            "Une chose que vous avez oubliée dans l'appel.",
            "Une phrase que vous avez cherchée trop longtemps.",
        ],
        notes="L'autoévaluation vaut plus que la correction quand elle est écrite tout de "
              "suite après l'écoute.")

    return d.save(dossier)
