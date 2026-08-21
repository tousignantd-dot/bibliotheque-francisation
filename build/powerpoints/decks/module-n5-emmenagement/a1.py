# -*- coding: utf-8 -*-
"""A1 · Les clés du 4.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-emmenagement/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Les clés du 4",
        chapeau="Le bail est signé, les clés sont dans la main. Tout ce qui "
                "vient ensuite — le camion, l'adresse, les voisins — n'est "
                "écrit nulle part.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Demander d'abord qui, dans le groupe, a "
                  "déjà déménagé au Québec, et ce qui a été le plus difficile. Les "
                  "réponses annoncent presque toujours les trois défis du module : le "
                  "camion, l'adresse, les voisins.")

    d.objectifs([
        "dire ce qu'on fait le jour où on reçoit les clés ;",
        "comprendre ce qu'est un état des lieux et à quoi il sert ;",
        "nommer les défauts courants d'un logement ;",
        "situer le module : entre le bail signé et la vie dans l'immeuble.",
    ])

    d.declencheur(
        'Observation', "Vous entrez pour la première fois dans un logement vide. "
                       "Vous regardez quoi ?",
        image=IMG + 'logement-vide.jpg',
        pistes=[
            "Les planchers et les murs ?",
            "Les fenêtres et les serrures ?",
            "Le poêle et le réfrigérateur ?",
            "Est-ce que vous écrivez quelque chose ?",
        ],
        notes="Presque personne ne répond « j'écris ». C'est exactement le point de "
              "départ. Laisser le dialogue amener l'état des lieux plutôt que de le "
              "donner tout de suite.")

    d.dialogue('Dialogue · 1 de 3', "Le nouveau du 4", [
        ("AMADOU", "Bonjour, madame. Excusez-moi, je bloque l'escalier avec ma "
                   "boîte.", True),
        ("THÉRÈSE", "Prenez votre temps, je ne suis pas pressée. Vous êtes le "
                    "nouveau du 4 ?", True),
        ("AMADOU", "Oui. Amadou Sow. Monsieur Rondeau vient de me remettre les "
                   "clés, il y a dix minutes.", True),
        ("THÉRÈSE", "Thérèse Guillemette, le 3, juste en dessous de vous. Ça fait "
                    "vingt-six ans que je suis dans l'immeuble.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer comment on se présente entre voisins : le nom, le numéro "
             "du logement, et rien de plus. C'est le modèle de la production orale du "
             "bloc E.")

    d.dialogue('Dialogue · 2 de 3', "Finissez le tour, et écrivez tout", [
        ("THÉRÈSE", "Vous avez fait le tour du logement avec lui, avant de signer "
                    "le papier ?", True),
        ("AMADOU", "On a commencé. Il m'a montré la cuisine, la chambre, le "
                   "balcon. On n'a pas fini.", True),
        ("THÉRÈSE", "Finissez-le, et écrivez tout. C'est ça, l'état des lieux : la "
                    "liste de ce qui est déjà abîmé quand vous entrez.", True),
        ("AMADOU", "Il y a une égratignure sur le plancher du salon, et la porte "
                   "de l'armoire ferme mal.", True),
    ], notes="Deux mots à écrire au tableau : « état des lieux » et « égratignure ». "
             "Ils reviennent dans toute la séance A4.")

    d.dialogue('Dialogue · 3 de 3', "Le premier juillet", [
        ("THÉRÈSE", "Notez-les. Prenez des photos aussi. Sinon, dans trois ans, ce "
                    "sera vous qui aurez fait l'égratignure.", True),
        ("AMADOU", "Je n'y avais pas pensé. Merci, madame Guillemette.", True),
        ("THÉRÈSE", "Appelez-moi Thérèse. Et le vrai déménagement, c'est quand ?", True),
        ("AMADOU", "Le premier juillet. Il faut encore que je trouve un camion.", True),
    ], notes="La dernière réplique annonce le plan du module : le camion, puis "
             "l'adresse, puis les voisins. Le dire au groupe.")

    d.regle("L'état des lieux se fait dans un logement vide",
            "Une fois les meubles entrés, il est trop tard : ils cachent tout.",
            precision="Au Québec, l'état des lieux n'est pas obligatoire. C'est "
                      "justement pour cela qu'il faut le faire : personne ne vous le "
                      "demandera, et personne ne le fera à votre place.",
            notes="Diapositive à photographier. Si les élèves ne retiennent qu'une chose "
                  "de la séance, c'est celle-là.")

    d.cartes("Quatre gestes du jour des clés", "Dans cet ordre", [
        ("Faire le tour au complet",
         "Chaque pièce, avec le propriétaire, avant d'entrer le premier meuble."),
        ("Écrire l'état des lieux",
         "La liste de ce qui est déjà abîmé. Deux signatures et une date."),
        ("Prendre des photos",
         "Une photo datée vaut mille explications : planchers, murs, salle de bain."),
        ("Vérifier ce qui fonctionne",
         "Robinets, ronds du poêle, fenêtres, serrures. Ce qui ne marche pas se "
         "signale la première semaine."),
    ], notes="Faire dire, pour chacun, combien de temps ça prend. La réponse totale est "
             "d'environ trente minutes — à mettre en regard des trois ans du bail.")

    d.piege("Croire qu'un logement neuf pour soi est un logement neuf",
            "C'est propre, donc il n'y a rien à noter.",
            "C'est propre, mais l'égratignure du salon était déjà là.",
            "Un logement fraîchement nettoyé paraît sans défaut. Les marques se voient "
            "de biais, à la lumière rasante, et près des plinthes. C'est là qu'il faut "
            "regarder, pas au milieu de la pièce.",
            notes="Faire l'expérience en classe : demander aux élèves de repérer les "
                  "marques du plancher du local. Elles apparaissent dès qu'on se baisse.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Amadou vient de recevoir les clés de monsieur Rondeau.", "vrai"),
        ("Thérèse habite l'immeuble depuis six mois.", "faux — depuis vingt-six ans"),
        ("Thérèse habite le logement du dessous.", "vrai — le 3"),
        ("Amadou a terminé le tour du logement avec le propriétaire.",
         "faux — ils ont commencé seulement"),
        ("Il y a une égratignure sur le plancher du salon.", "vrai"),
        ("Le déménagement d'Amadou a lieu au mois de juin.", "faux — le premier juillet"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte du dialogue.")

    d.billet(
        "Dans votre logement d'aujourd'hui, nommez trois choses qui étaient déjà "
        "abîmées quand vous êtes entré.",
        exemples=[
            "Écrivez-les avec l'endroit : « une tache au plafond de la salle de bain ».",
            "Si vous ne vous en souvenez pas, c'est déjà une réponse à la question.",
        ],
        notes="Devoir concret qui prépare A4. Prévoir que plusieurs élèves n'auront rien "
              "noté en entrant : le dire sans jugement, c'est le sens du module.")

    return d.save(dossier)
