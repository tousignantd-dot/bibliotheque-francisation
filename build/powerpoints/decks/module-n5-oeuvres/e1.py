# -*- coding: utf-8 -*-
"""E1 · Vos deux minutes au club du jeudi
Bloc E « Je me lance » · couleur teal · 75 min. Production orale.
Source : bloc « Je me lance » de l'activité interactive — dialogue `appli`,
jeu de rôle `oeuvres` (trois situations) et présentation enregistrée.
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
        code='E1', section='teal',
        titre="Vos deux minutes au club du jeudi",
        chapeau="C'est votre tour. Dix personnes vous écoutent, personne ne "
                "vous coupe, et personne ne connaît l'œuvre dont vous "
                "parlez. Vous l'avez lue, vue ou écoutée dans n'importe "
                "quelle langue : vous la présentez en français.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Elle se fait presque entièrement debout et à "
                  "deux. Prévoir des postes avec écouteurs pour le jeu de rôle et un "
                  "coin calme pour l'enregistrement. Rendre au début les billets de D1 "
                  "et de D2 : chacun arrive avec son avis et sa réserve déjà écrits.")

    d.objectifs([
        "présenter une œuvre pendant deux minutes sans s'arrêter ;",
        "raconter au présent et s'arrêter avant le dénouement ;",
        "donner un avis précis et le justifier ;",
        "tenir son avis devant quelqu'un qui pense autrement.",
    ], notes="Le premier objectif est le critère du niveau 5 à l'oral : un discours "
             "suivi, pas cinq réponses à cinq questions. Si l'assistant doit demander "
             "« et ça se passe où ? », la présentation n'était pas complète.")

    d.dialogue('Dialogue', "Vous avez trouvé vos mots", [
        ("GILBERTE", "Vous avez trouvé vos mots, Mai. Ça s'entend.", True),
        ("MAI", "Je fais toujours pareil, maintenant : le titre, le genre, où ça se passe.", True),
        ("GILBERTE", "Puis l'histoire, au présent, sans le dénouement.", True),
        ("MAI", "Et je m'arrête au moment où le personnage doit choisir.", True),
    ], consigne="Écoutez, puis dites ce que Mai fait « toujours pareil ».",
       notes="Faire remarquer le renversement : à la séance A1, Mai relisait trois "
             "fois une affiche sans oser entrer. Le dire au groupe en toutes lettres — "
             "c'est le moment de la séance qui reste.")

    d.dialogue('Dialogue · la suite', "Et si quelqu'un n'est pas d'accord ?", [
        ("GILBERTE", "Et l'avis ?", True),
        ("MAI", "Un adjectif précis, jamais « c'est bon ». Et une raison derrière.", True),
        ("GILBERTE", "Et si quelqu'un n'est pas d'accord ?", True),
        ("MAI", "Je lui accorde ce qu'il a de juste, puis je dis pourquoi je pense autrement.", True),
    ], notes="Ces deux dernières répliques sont la méthode du module en entier. Les "
             "laisser affichées pendant que le groupe prépare sa présentation.")

    d.cartes("Trois situations pour le jeu de rôle", "Choisissez la vôtre", [
        ("Devant le cinéma, un mardi soir",
         "La personne n'a pas vu le film et hésite. Elle ne veut surtout pas savoir "
         "comment ça finit — et elle n'aime pas les histoires au passé."),
        ("Au comptoir de la bibliothèque",
         "Vous voulez une autre bande dessinée. On vous en conseillera une si vous "
         "dites ce que vous avez lu et ce que vous cherchez."),
        ("Le club du jeudi, salle du fond",
         "Deux minutes devant une dizaine de chaises en cercle. Quelqu'un dans le "
         "groupe ne sera pas d'accord avec vous."),
    ], cols=3, notes="Ce sont les trois situations de l'activité interactive. "
                     "L'assistant ne connaît pas votre œuvre et il vous fera préciser. "
                     "Ce n'est ni une panne ni de la mauvaise volonté : c'est ainsi "
                     "qu'il fait travailler le discours suivi.")

    d.tableau('Le jeu de rôle', "Ce que la grille vérifie",
              ["Le sujet", "Ce qu'on attend"],
              [["L'œuvre", "le titre, le genre et le support"],
               ["Le cadre", "où et quand, en une phrase"],
               ["Le personnage", "ce qu'il veut, avec « qui » ou « que »"],
               ["L'arrêt", "au moment du choix, jamais le dénouement"],
               ["L'avis", "un adjectif précis, mis en avant"],
               ["La recommandation", "à qui, et pourquoi à cette personne-là"]],
              cle=1,
              notes="Six des onze sujets de la grille en ligne. Les cinq autres — la "
                    "reprise de l'œuvre par un autre mot, la justification, "
                    "l'accord donné à l'autre — sont ceux du Défi 2 et du Défi 3 : les "
                    "écrire au tableau à côté.")

    d.regle("On ne raconte pas la fin",
            "On s'arrête au moment où le personnage doit choisir.",
            precision="C'est la règle du club, et c'est aussi ce qui donne envie. Une "
                      "histoire résumée jusqu'au bout n'a plus besoin d'être lue ; une "
                      "histoire arrêtée au bon endroit se fait emprunter le soir même.",
            notes="Diapositive à photographier et à laisser projetée pendant tout "
                  "l'atelier. C'est le seul manquement que le jeu de rôle sanctionne "
                  "vraiment.")

    d.pratique('Production orale', "Vos deux minutes, en cinq temps",
               "Écrivez d'abord, lisez à voix haute, puis enregistrez. De "
               "cent à cent trente secondes.", [
        ("TEMPS 1", "Bonsoir. Je vous apporte un roman, une histoire de famille, à peu près trois cents pages."),
        ("TEMPS 2", "Ça se passe aujourd'hui, dans un village au bord de la mer. C'est une femme qui revient dans le village qu'elle a quitté il y a vingt ans."),
        ("TEMPS 3", "Elle vient vendre la maison de sa mère. Mais elle ouvre la maison et elle trouve une boîte de lettres. Je m'arrête ici."),
        ("TEMPS 4", "Moi, ce qui m'a touchée, c'est le silence entre les deux sœurs : elles ne se disent presque rien, et on comprend tout quand même."),
        ("TEMPS 5", "Ce que j'ai le moins aimé, c'est la longueur du début. Par contre, je le recommande à quelqu'un qui a quitté un pays."),
    ], cols=1,
       notes="Les cinq temps sont ceux du module en ligne. Insister : l'œuvre doit "
             "être une vraie œuvre, lue ou vue pour de bon, dans n'importe quelle "
             "langue. Une présentation sur un livre inventé s'entend en dix secondes.")

    d.piege("Enregistrer sans avoir écrit",
            "J'improvise, ça fera plus naturel.",
            "J'écris mes cinq temps, je les lis une fois, puis j'enregistre.",
            "Une présentation improvisée dure quarante secondes ou quatre minutes, "
            "et elle oublie presque toujours deux choses : le genre de l'œuvre, et "
            "la raison derrière l'avis. Ce sont les deux qui donnent envie.",
            notes="Lire ses notes n'a rien d'artificiel devant un groupe : les gens "
                  "qui présentent des livres à la radio le font tous. Le dire.")

    d.pratique('Autoévaluation', "Réécoutez-vous comme quelqu'un qui ne connaît pas l'œuvre",
               "Répondez honnêtement avant d'envoyer.", [
        ("Sait-on le titre, le genre et le support ?", "les trois, dès la première phrase"),
        ("L'histoire est-elle racontée au présent ?", "elle arrive, elle ouvre, elle trouve"),
        ("Vous êtes-vous arrêté avant la fin ?", "au moment du choix"),
        ("L'avis a-t-il un adjectif précis et une raison ?", "jamais « c'est bon »"),
        ("Avez-vous dit une chose moins aimée ?", "sans démolir l'œuvre"),
        ("Dit-on à qui vous la recommandez ?", "à quelqu'un de précis"),
    ], corrige=True,
       notes="Faire faire l'autoévaluation avant l'envoi à l'enseignante, jamais "
             "après. Les élèves recommencent d'eux-mêmes une fois sur deux, et c'est "
             "exactement le but.")

    d.billet(
        "Après votre enregistrement : notez la chose que vous referiez autrement.",
        exemples=[
            "Une seule chose, la plus importante.",
            "Notez aussi ce qui a bien marché : ça se garde pour la prochaine fois.",
        ],
        notes="Ramasser les billets et les rendre en E2 avec la rétroaction de la "
              "production orale. La comparaison entre ce que l'élève a repéré "
              "lui-même et ce que dit la correction vaut mieux qu'une note.")

    return d.save(dossier)
