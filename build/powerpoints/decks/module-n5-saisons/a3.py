# -*- coding: utf-8 -*-
"""A3 · Les seize mots de la météo qui décide
Bloc A « Je découvre » · couleur framboise · 75 min. Vocabulaire.
Source : banc `FC_CARDS`, exercices `prVocab` et `prImg`.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-saisons/images/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Les seize mots de la météo qui décide",
        chapeau="Quatre mots pour l'avis lui-même, quatre pour l'hiver du "
                "Bas-Saint-Laurent, quatre pour le printemps qui fait "
                "décider, quatre pour l'équipement des quatre saisons. Seize "
                "mots, et une décision devient possible.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Elle se prépare en imprimant les seize mots sur "
                  "des cartons : le tri en groupes de quatre, sur une table, vaut mieux "
                  "que n'importe quelle liste projetée. Prévoir aussi les six photos de "
                  "l'exercice prImg, si elles sont produites.")

    d.objectifs([
        "nommer les quatre mots de l'avis : veille, avertissement, prévisions, éclaircie ;",
        "nommer les phénomènes de l'hiver d'ici, avec leur article ;",
        "opposer reporter et annuler, et dire ce qui les sépare ;",
        "nommer ce qu'on apporte par grand froid et par grande chaleur.",
    ], notes="Le troisième objectif est le seul qui ne soit pas du vocabulaire pur : "
             "reporter et annuler ne se distinguent pas par le sens des mots mais par "
             "l'existence d'une date de rechange. Le poser ici, le travailler en C2.")

    d.declencheur(
        'Observation', "De la neige qui traverse la route en traînées. "
                       "Comment appelle-t-on ça ici ?",
        image=img('poudrerie-route.jpg'),
        pistes=[
            "Est-ce qu'il neige, sur cette photo ?",
            "D'où vient la neige qu'on voit passer ?",
            "Qu'est-ce que ça change pour quelqu'un qui conduit ?",
            "Est-ce que ce mot existe dans votre première langue ?",
        ],
        notes="« Poudrerie » est un mot du français d'ici, et la deuxième piste est la "
              "clé : la neige ne tombe pas, elle est soulevée. Beaucoup d'élèves l'ont "
              "entendu vingt fois sans jamais savoir ce qu'il désignait.")

    d.vocabulaire("Groupe 1", "L'avis météo lui-même", [
        ("une veille", "L'avis qui dit que le phénomène est possible."),
        ("un avertissement", "L'avis qui dit qu'il est imminent ou commencé."),
        ("les prévisions", "Ce que la météo annonce pour les jours qui viennent."),
        ("une éclaircie", "Le moment où les nuages s'ouvrent un peu."),
    ], notes="Les quatre ont été vus en A1 ; ici on les fixe avec l'article et la "
             "prononciation. « Éclaircie » est le seul mot agréable du module : le faire "
             "remarquer, ça aide à le retenir.")

    d.vocabulaire("Groupe 2", "L'hiver du Bas-Saint-Laurent", [
        ("la pluie verglaçante", "La pluie qui gèle en touchant le sol."),
        ("la poudrerie", "La neige déjà tombée que le vent soulève."),
        ("le refroidissement éolien", "Le froid que la peau sent quand le vent s'ajoute."),
        ("une bordée de neige", "Une grosse quantité tombée d'un seul coup."),
    ], notes="Le refroidissement éolien est le plus difficile à dire et le plus utile à "
             "comprendre : c'est ce chiffre-là qui gèle les doigts, pas celui du "
             "thermomètre. Le faire répéter en quatre syllabes bien séparées.")

    d.vocabulaire("Groupe 3", "Le printemps, et la décision", [
        ("la crue printanière", "La montée de l'eau quand toute la neige fond."),
        ("le dégel", "Le moment où la température repasse au-dessus de zéro."),
        ("reporter", "Déplacer une activité à une autre date."),
        ("annuler", "Décider qu'elle n'aura pas lieu du tout."),
    ], notes="Faire dire la différence entre les deux verbes avec des exemples de la vie "
             "des élèves : un rendez-vous reporté, une commande annulée. Le mot juste "
             "évite un téléphone sur deux.")

    d.vocabulaire("Groupe 4", "L'été, le froid, et le sac", [
        ("la chaleur extrême", "Une chaleur assez forte et longue pour rendre malade."),
        ("l'indice UV", "Le chiffre qui dit à quel point le soleil peut brûler."),
        ("un coup de chaleur", "Le malaise grave quand le corps ne se refroidit plus."),
        ("des crampons", "Les pointes qu'on attache sous ses bottes sur la glace."),
    ], notes="« Indice UV » se dit lettre par lettre : u-vé. Beaucoup d'élèves le lisent "
             "« uv » d'un bloc. Les crampons méritent d'être montrés : la plupart des "
             "gens ne savent pas que ça existe et que ça coûte quinze dollars.")

    d.tableau('Deux verbes', "Reporter ou annuler : la question qui tranche",
              ['On reporte', 'On annule'],
              [["Une date de rechange existe", "Aucune date de rechange"],
               ["La promenade sera encore là", "Le spectacle passe une fois"],
               ["« reportée au samedi 22 »", "« elle n'aura pas lieu »"],
               ["Personne ne perd rien", "On le dit plus tôt, et on dit pourquoi"]],
              cle=1,
              notes="Reprendre les billets de A1 : pour chaque situation notée par un "
                    "élève, faire dire au groupe s'il fallait reporter ou annuler. C'est "
                    "l'exercice le plus vivant de la séance.")

    d.pratique('Vocabulaire', "Le mot juste",
               "Complétez avec un mot des quatre groupes.", [
        ("La ___ laissera trois millimètres de glace sur les trottoirs.", "pluie verglaçante"),
        ("La ___ réduira la visibilité à moins d'un kilomètre.", "poudrerie"),
        ("Moins douze, mais un ___ de moins vingt-deux.", "refroidissement éolien"),
        ("La ___ a inondé les sentiers du bas du parc.", "crue printanière"),
        ("Avec un ___ de neuf, une heure au soleil suffit à brûler.", "indice UV"),
        ("Avec des ___, un trottoir gelé redevient marchable.", "crampons"),
    ], corrige=True,
       notes="Faire relire chaque phrase à voix haute une fois complétée : les seize mots "
             "doivent sortir de la bouche des élèves au moins une fois dans la séance, "
             "pas seulement de leur crayon.")

    d.billet(
        "Choisissez quatre mots des seize et écrivez une phrase avec chacun.",
        exemples=[
            "Prenez au moins un mot de l'hiver et un mot de l'été.",
            "Les phrases peuvent parler de vous, pas seulement de Marisol.",
        ],
        notes="Ramasser les billets. Les phrases servent en A4 pour travailler la langue "
              "des avis, et elles disent quels mots ne sont pas encore compris.")

    return d.save(dossier)
