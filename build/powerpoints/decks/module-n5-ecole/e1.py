# -*- coding: utf-8 -*-
"""E1 · Au comptoir, puis dans la boîte vocale
Bloc E « Je me lance » · couleur teal · 75 min. Production orale.
Source du module : dialogue `appli`, jeu de rôle `ecole` (trois
situations) et message laissé dans la boîte vocale du centre.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-ecole/images/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Au comptoir, puis dans la boîte vocale",
        chapeau="C'est à vous. Vous réglez d'abord votre affaire au comptoir "
                "avec l'assistant, qui joue le secrétariat ; puis vous "
                "laissez un message dans la boîte vocale du centre — une "
                "minute, et personne ne pourra vous poser de question.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Elle se fait presque entièrement debout et à "
                  "deux. Prévoir des postes avec écouteurs pour le jeu de rôle et un "
                  "coin calme pour l'enregistrement. Rendre au début les billets de D1 "
                  "et de D2 : chacun arrive avec sa demande à moitié écrite.")

    d.objectifs([
        "exposer une démarche complète sans qu'on ait à vous questionner ;",
        "donner les dates avant le motif ;",
        "glisser une question polie dans une phrase ;",
        "laisser un message d'une minute qui n'oublie ni la date ni le numéro.",
    ], notes="Le premier objectif est le critère principal. Si l'assistant doit "
             "demander « à partir de quand ? », la démarche n'était pas exposée en "
             "entier — c'est ce que le niveau 5 appelle un discours suivi.")

    d.dialogue('Dialogue', "Vous savez maintenant à qui parler", [
        ("JOCELYNE", "Madame Dumitrescu ! Vous êtes revenue. Votre mère va mieux ?", True),
        ("AMELIA", "Beaucoup mieux, merci. Je vous apporte le papier de l'hôpital.", True),
        ("JOCELYNE", "Parfait. Vous voyez, vous aviez prévenu : tout est resté en place.", True),
        ("AMELIA", "J'ai appris une chose : il faut dire les dates avant le reste.", True),
    ], consigne="Écoutez, puis dites ce qu'Amelia a appris.",
       notes="Faire remarquer le renversement : au début du module, Amelia gardait sa "
             "nouvelle depuis trois jours sans savoir à quelle porte frapper. Le dire "
             "au groupe en toutes lettres — c'est le moment de la séance qui reste.")

    d.dialogue('Dialogue · la suite', "Je garde une copie de tout", [
        ("JOCELYNE", "Et l'écrire. Un dossier ne se souvient pas d'une conversation.", True),
        ("AMELIA", "Je garde une copie de tout, maintenant. Même des courriels.", True),
        ("JOCELYNE", "Vous êtes mieux organisée que bien du monde, madame Dumitrescu.", True),
        ("AMELIA", "C'est que je ne veux plus jamais rester trois jours sans oser demander.", True),
    ], notes="La dernière réplique est celle du module entier. La lire à voix haute et "
             "s'arrêter là.")

    d.cartes("Trois situations pour le jeu de rôle", "Choisissez la vôtre", [
        ("L'absence de trois semaines",
         "Du 9 au 27 mars. Vous voulez garder votre place, savoir quel papier remplir "
         "et pour quand, et ce qui arrive à votre allocation."),
        ("Le passage au groupe du soir",
         "Votre emploi débute à sept heures. Vous voulez le transfert à partir du "
         "20 avril, et connaître le délai d'un changement de groupe."),
        ("La preuve pour l'employeur",
         "Il exige une preuve écrite avant vendredi, avec les heures par semaine. "
         "Attestation ou relevé ? Lequel le centre peut-il imprimer ?"),
    ], cols=3, notes="Ce sont les trois situations de l'activité interactive. "
                     "L'assistant joue le secrétariat : il répond à ce qu'on lui "
                     "demande, et à rien d'autre. Il ne devine pas les dates à votre "
                     "place — c'est ainsi qu'il fait travailler le discours suivi.")

    d.tableau('Le jeu de rôle', "Ce que la grille vérifie",
              ["Le sujet", "Ce qu'on attend"],
              [["Qui vous êtes", "le nom et le groupe, dès la première phrase"],
               ["Ce que vous venez faire", "en une phrase, avant toute explication"],
               ["Les dates", "à partir de quand, jusqu'à quand"],
               ["Le motif", "une phrase, après les dates"],
               ["Vos questions", "glissées, jamais jetées en vrac"],
               ["Le retour", "ce que vous ferez, et quand"]],
              cle=1,
              notes="Six des sujets de la grille en ligne. C'est l'ordre du Défi 1 : "
                    "les dates d'abord, le motif ensuite. Le rappeler avant d'ouvrir "
                    "les postes.")

    d.regle("Une question polie se glisse dans une phrase",
            "Je voudrais savoir si… Pourriez-vous me dire quand…",
            precision="Trois questions posées d'affilée ressemblent à un "
                      "interrogatoire ; les mêmes, glissées dans des phrases, se "
                      "répondent avec plaisir. C'est la règle du Défi 1, et le jeu de "
                      "rôle la vérifie du début à la fin.",
            notes="Diapositive à photographier et à laisser projetée pendant tout "
                  "l'atelier. Faire produire trois questions par élève, à l'écrit, "
                  "avant d'aller aux postes.")

    d.pratique('Production orale', "Le message dans la boîte vocale",
               "Cinq temps, dans l'ordre. Écrivez, lisez à voix haute, puis "
               "enregistrez.", [
        ("TEMPS 1", "Bonjour, ici Amelia Dumitrescu, groupe 4, en francisation, cours de niveau 5."),
        ("TEMPS 2", "Je vous appelle pour vous annoncer une absence prévue de trois semaines."),
        ("TEMPS 3", "Je serai absente à partir du 9 mars, jusqu'au 27 mars inclusivement. Ma mère est opérée à l'étranger."),
        ("TEMPS 4", "Je reviendrai en classe le lundi 30 mars et je vous apporterai la pièce justificative dès mon retour."),
        ("TEMPS 5", "Je voudrais savoir si je dois remplir un formulaire avant mon départ. Vous pouvez me rappeler au 819 555-0142."),
    ], cols=1,
       notes="De quarante-cinq à soixante secondes. Personne ne vous voit et personne "
             "ne pourra vous poser de question : c'est exactement pour cela que le "
             "message doit être écrit avant d'être dit.")

    d.piege("Enregistrer sans avoir écrit",
            "J'improvise, ce sera plus naturel.",
            "J'écris mes cinq temps, je les lis une fois, puis j'enregistre.",
            "Un message improvisé oublie presque toujours deux choses : la date de "
            "retour et le numéro de téléphone. Ce sont justement les deux qui "
            "permettent au centre de vous répondre.",
            notes="Lire ses notes au téléphone n'a rien d'artificiel : tout le monde "
                  "le fait, y compris les gens dont c'est la langue maternelle. Le "
                  "dire, parce que beaucoup d'élèves croient le contraire.")

    d.pratique('Autoévaluation', "Réécoutez-vous comme si vous teniez le secrétariat",
               "Répondez honnêtement avant d'envoyer.", [
        ("Sait-on qui appelle, et de quel groupe ?", "le nom complet, dès le début"),
        ("Sait-on ce que vous annoncez, dès la deuxième phrase ?", "en une phrase"),
        ("Les deux dates y sont-elles ?", "à partir de, jusqu'à — inclusivement"),
        ("Le motif tient-il en une phrase ?", "une seule, après les dates"),
        ("Dites-vous ce que vous ferez au retour ?", "au futur simple"),
        ("Le numéro est-il dit assez lentement ?", "faites-le vérifier par un voisin"),
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
