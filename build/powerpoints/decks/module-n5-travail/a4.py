# -*- coding: utf-8 -*-
"""A4 · Au téléphone, ou dans le corridor ?
Bloc A « Je découvre » · couleur ambre · 75 min. Registre de langue.
Source : exercice `prReg`, mini-leçon `prReg`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-travail/images/')


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Au téléphone, ou dans le corridor ?",
        chapeau="Entre collègues, on se tutoie et on parle vite. Dès qu'on "
                "décroche le téléphone, tout change. Ce n'est pas de la "
                "froideur : au bout du fil, ce n'est plus vous qui parlez, "
                "c'est l'organisation.",
        duree='75 minutes')

    d.titre(notes="Séance qui ferme le bloc A et prépare tout le défi 1. Commencer par "
                  "relire la dernière réplique de Ghislain en A1 : « Ce n'est pas Dorine "
                  "qui répond au poste vingt-deux, c'est la coopérative. » Toute la "
                  "séance en découle.")

    d.objectifs([
        "reconnaître ce qui se dit au téléphone et ce qui se dit entre collègues ;",
        "ouvrir un appel en nommant l'établissement, puis soi-même ;",
        "faire patienter, transférer et s'excuser avec les formules d'usage ;",
        "fermer un appel en disant ce qui va se passer ensuite.",
    ])

    d.declencheur(
        'Observation', "Un téléphone de bureau, un voyant rouge qui "
                       "clignote. Qu'est-ce qu'on dit en décrochant ?",
        image=IMG + 'telephone-poste.jpg',
        pistes=[
            "Est-ce qu'on dit « allô » ? Pourquoi pas ?",
            "Qu'est-ce que la personne au bout du fil veut savoir en premier ?",
            "Comment dit-on à quelqu'un d'attendre, poliment ?",
            "Qu'est-ce qu'on dit à la fin, pour que la personne sache ce qui suit ?",
        ],
        notes="La première piste étonne toujours : « allô » n'est pas impoli, il est "
              "personnel. La personne qui appelle croit s'être trompée de numéro. C'est "
              "l'exemple le plus clair de la différence de registre.")

    d.regle("Deux façons de parler dans le même immeuble",
            "Entre collègues, on se tutoie. Au téléphone et par écrit, on "
            "vouvoie tout le monde, même les gens qu'on connaît depuis un an.",
            precision="Vouvoyer ne veut pas dire allonger : les phrases restent "
                      "courtes, une idée à la fois. Un message poli et interminable "
                      "est un message raté.",
            notes="La précision compte autant que la règle. Beaucoup d'élèves croient "
                  "que la politesse tient dans la longueur, et produisent des phrases de "
                  "trente mots qu'ils ne maîtrisent pas.")

    d.tableau('La même chose, deux fois', "Dans le corridor, et au téléphone",
              ['Entre collègues', 'Au téléphone'],
              [["Attends deux secondes", "Un instant, je vous prie"],
               ["Hein ?", "Pourriez-vous répéter ?"],
               ["C'est quoi ton numéro ?", "Votre numéro, s'il vous plaît ?"],
               ["C'est beau, je m'en occupe", "Je m'en occupe aujourd'hui"],
               ["Bye, à demain", "Merci de votre appel, bonne journée"]],
              cle=1,
              notes="Faire lire la colonne de gauche par un élève et celle de droite par "
                    "un autre, en alternance. Ce n'est pas le vocabulaire qui change le "
                    "plus : c'est le début de la phrase.")

    d.cartes("Les quatre moments d'un appel", "Une formule pour chacun", [
        ("Ouvrir",
         "Coopérative d'aide à domicile de Rosemont, bonjour. Ici Dorine, à l'accueil."),
        ("Faire patienter",
         "Un instant, je vous prie. Ne quittez pas, je vérifie."),
        ("Transférer",
         "Je vous transfère au poste onze. Je vous passe le service technique."),
        ("Fermer",
         "Je transmets votre message aujourd'hui. Merci de votre appel, bonne journée."),
    ], notes="L'ordre de la première carte est important : l'établissement d'abord, "
             "soi-même ensuite. La personne veut d'abord savoir qu'elle a composé le bon "
             "numéro. Le faire remarquer, puis faire répéter.")

    d.piege("Tutoyer parce qu'on connaît la personne",
            "Salut madame Thériault, comment ça va ?",
            "Bonjour madame Thériault. Comment puis-je vous aider ?",
            "Au téléphone, on vouvoie même les gens qu'on croise depuis un an. Le "
            "tutoiement reprend dès qu'on se revoit en personne, dans le corridor.",
            notes="C'est exactement l'objection de Dorine en A1. Faire relire sa réplique : "
                  "« Même madame Thériault ? Je lui parle depuis un an. » Le groupe se "
                  "reconnaît dans l'objection.")

    d.pratique('Registre', "Où est-ce que ça se dit ?",
               "Pour chaque phrase, dites : au téléphone, ou entre collègues ?", [
        ("Coopérative d'aide à domicile de Rosemont, bonjour.", "au téléphone"),
        ("Attends deux secondes, je finis mon café.", "entre collègues"),
        ("Un instant, je vous prie, je vérifie au registre.", "au téléphone"),
        ("Ah pis, laisse faire, je vais le faire moi-même.", "entre collègues"),
        ("Je vous transfère au poste onze, ne quittez pas.", "au téléphone"),
        ("C'est beau, pas de trouble, je m'en occupe.", "entre collègues"),
        ("Merci de votre appel, bonne journée.", "au téléphone"),
        ("Pourriez-vous me répéter votre numéro, s'il vous plaît ?", "au téléphone"),
    ], cols=2, corrige=True,
       notes="Préciser après la correction qu'aucune phrase de la colonne « entre "
             "collègues » n'est impolie : elles sont hors contexte au téléphone, ce qui "
             "n'est pas la même chose. Les élèves entendent souvent un jugement.")

    d.pratique('Transformation', "Dites-le au téléphone",
               "Récrivez chaque phrase pour un appel de travail.", [
        ("Hein ? J'ai pas compris.", "Pourriez-vous répéter, s'il vous plaît ?"),
        ("Attends, je regarde.", "Un instant, je vérifie."),
        ("C'est quoi ton nom déjà ?", "Votre nom, s'il vous plaît ?"),
        ("Je te rappelle tantôt.", "Je vous rappelle dans les meilleurs délais."),
        ("Bye là.", "Merci de votre appel, bonne journée."),
        ("Il est pas là, rappelle demain.", "Il n'est pas disponible. Souhaitez-vous laisser un message ?"),
    ], corrige=True,
       notes="La dernière est la plus riche : la version polie ne se contente pas de "
             "vouvoyer, elle propose une solution. Faire remarquer que c'est ce qui "
             "distingue un service d'un mur.")

    d.billet(
        "Écrivez les quatre phrases avec lesquelles vous ouvririez, feriez patienter, "
        "transféreriez et fermeriez un appel à votre travail.",
        exemples=[
            "Employez le nom de votre vrai lieu de travail, ou d'un lieu que vous connaissez.",
            "Relisez-les à voix haute : est-ce qu'elles tiennent en une respiration ?",
        ],
        notes="Ces quatre phrases servent directement en B1, où les élèves écriront leur "
              "message d'accueil. Leur demander de garder le billet.")

    return d.save(dossier)
