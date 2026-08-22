# -*- coding: utf-8 -*-
"""A1 · « Il faut que tu ailles au secrétariat »
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source du module : dialogue `prep`, exercice `pr1`.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-ecole/images/')


def img(nom):
    """Le chemin d'une illustration, ou None si elle n'a pas encore été
    produite. Les séances se construisent sans les images et les reprennent
    d'elles-mêmes à la reconstruction."""
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="« Il faut que tu ailles au secrétariat »",
        chapeau="Amelia Dumitrescu est arrivée de Roumanie il y a deux ans. "
                "Sa mère sera opérée à Bucarest au mois de mars, et il "
                "faudra qu'elle parte trois semaines. Elle le sait depuis "
                "trois jours et elle n'a encore rien dit à personne : elle "
                "ne sait pas à quelle porte frapper.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir en demandant à main levée qui, dans "
                  "le groupe, a déjà eu à régler une affaire au bureau du centre — une "
                  "absence, un changement d'horaire, un papier à obtenir. Puis demander "
                  "qui a hésité plusieurs jours avant d'y aller. Les deux mains montent "
                  "presque autant l'une que l'autre, et c'est là qu'est le module.")

    d.objectifs([
        "savoir à qui s'adresser dans un centre selon la question qu'on a ;",
        "nommer les lieux et les personnes : le secrétariat, la conseillère, un local ;",
        "comprendre une conversation entre deux élèves sur une démarche à faire ;",
        "distinguer ce qu'on tutoie de ce qu'on vouvoie dans un établissement.",
    ], notes="Le premier objectif est le vrai contenu de la séance. Les trois autres le "
             "servent. Un élève qui sait que l'enseignante ne décide pas des absences a "
             "déjà gagné une semaine.")

    d.declencheur(
        'Observation', "Un comptoir, une file au sol, une vitre. "
                       "Qu'est-ce qu'on vient y faire ?",
        image=img('comptoir-secretariat.jpg'),
        pistes=[
            "Qu'est-ce qu'on peut demander à ce comptoir, et qu'est-ce qu'on ne peut pas ?",
            "Est-ce qu'on tutoie ou est-ce qu'on vouvoie la personne derrière la vitre ?",
            "Combien de temps avez-vous, à votre avis, quand il y a du monde derrière vous ?",
            "Qu'est-ce que vous apportez avec vous quand vous y allez ?",
        ],
        notes="La troisième piste est la plus utile. Personne n'a jamais dit aux élèves "
              "qu'un comptoir donne environ deux minutes. Le savoir change complètement "
              "la façon dont on prépare ce qu'on va dire.")

    d.dialogue('Dialogue · 1 de 3', "Je ne sais pas à qui parler", [
        ("AMELIA", "Koffi, je ne sais pas à qui parler. J'ai un problème et "
                   "il dure.", True),
        ("KOFFI", "Un problème de cours ou un problème de papiers ?", True),
        ("AMELIA", "De papiers. Je dois m'absenter trois semaines au mois de "
                   "mars.", True),
        ("KOFFI", "Trois semaines ! Alors ce n'est pas ton enseignante qu'il "
                  "faut voir.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer la première question de Koffi : il trie avant de "
             "conseiller. « Un problème de cours ou un problème de papiers ? » est la "
             "question que chaque élève devrait se poser à lui-même en premier.")

    d.dialogue('Dialogue · 2 de 3', "Le secrétariat, en avant, à droite", [
        ("AMELIA", "C'est qui, d'abord ? Je n'ose pas déranger le monde.", True),
        ("KOFFI", "Le secrétariat, en avant, à droite en entrant. C'est "
                  "madame Paradis.", True),
        ("AMELIA", "Elle s'occupe de quoi, exactement ?", True),
        ("KOFFI", "Des dossiers. Les absences, les inscriptions, les "
                  "attestations.", True),
    ], notes="« Je n'ose pas déranger le monde » est la phrase à relever. Beaucoup "
             "d'élèves la portent. Répondre franchement : le secrétariat est là pour "
             "ça, et ne rien dire coûte plus cher à tout le monde qu'une question.")

    d.dialogue('Dialogue · 3 de 3', "Vouvoie-les", [
        ("AMELIA", "Et si c'est plus compliqué que ça ?", True),
        ("KOFFI", "Là, elle te renvoie à monsieur Gauthier, le conseiller en "
                  "formation. Il touche à ton horaire et à ton groupe.", True),
        ("AMELIA", "Et je perds ma place, si je m'absente si longtemps ?", True),
        ("KOFFI", "Pas si tu préviens avant. C'est de ne rien dire qui coûte "
                  "cher. Et vouvoie-les : ici, on se tutoie entre nous, pas "
                  "avec le bureau.", False),
    ], notes="La dernière réplique porte deux choses : la règle du module — prévenir "
             "d'avance conserve la place — et la bascule du tutoiement au vouvoiement. "
             "C'est le seul dialogue du module où l'on tutoie. Le dire au groupe.")

    d.regle("Trois portes, trois questions",
            "L'enseignante pour le cours. Le secrétariat pour le dossier. "
            "La conseillère pour le parcours.",
            precision="Frapper à la mauvaise porte ne fâche personne — mais on "
                      "vous renvoie, et vous perdez une journée.",
            notes="Diapositive à photographier. Elle revient en B1 et en D1. Faire "
                  "donner par le groupe trois exemples de questions pour chaque porte.")

    d.cartes("Le centre et ses gens", "Quatre mots à savoir avant tout le reste", [
        ("Le secrétariat",
         "Le bureau de l'entrée, où l'on règle tout ce qui touche au dossier."),
        ("Une conseillère",
         "La personne qui décide du groupe, de l'horaire, de la suite des cours."),
        ("Un local",
         "La salle où se donne un cours, désignée par son numéro."),
        ("Une session",
         "La période de plusieurs mois pendant laquelle un cours se donne."),
    ], notes="Faire répéter avec l'article. « Un local » surprend : beaucoup d'élèves "
             "disent « une classe ». Les deux se comprennent, mais c'est « local 118 » "
             "qui est écrit sur l'avis qu'ils recevront en bloc C.")

    d.tableau('Deux façons de parler', "Entre nous, et avec le bureau",
              ['Avec un camarade', 'Au comptoir'],
              [["Tu sais où c'est ?", "Pourriez-vous me dire où c'est ?"],
               ["Je peux-tu m'absenter ?", "Je voudrais savoir si je peux m'absenter."],
               ["J'ai un problème.", "Je viens vous annoncer une absence prévue."],
               ["Merci, là.", "Je vous remercie, bonne journée."]],
              cle=1,
              notes="Faire compléter la colonne de droite avant de l'afficher. Ne pas "
                    "présenter la colonne de gauche comme fautive : elle est juste, et "
                    "elle est ce qu'on dit entre soi. C'est l'endroit qui change.")

    d.piege("Croire qu'il faut d'abord en parler à son enseignante",
            "Je vais le dire à mon enseignante, elle va s'en occuper.",
            "Je vais au secrétariat, et j'en informe mon enseignante ensuite.",
            "L'enseignante peut vous écouter et vous conseiller, mais rien de ce que "
            "vous lui dites n'entre dans votre dossier. Une absence annoncée "
            "seulement en classe reste une absence non motivée.",
            notes="Ce piège-là est le vrai obstacle du module. Il n'est pas dû à un "
                  "manque de vocabulaire : il vient de ce que l'enseignante est la seule "
                  "personne que l'élève connaît dans l'établissement.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Amelia doit s'absenter trois semaines au mois de mars.", "vrai"),
        ("Koffi lui conseille d'en parler d'abord à son enseignante.",
         "faux — au secrétariat"),
        ("Le secrétariat est à droite en entrant.", "vrai"),
        ("Madame Paradis décide des changements de groupe.",
         "faux — c'est monsieur Gauthier"),
        ("Une absence annoncée d'avance fait perdre sa place.",
         "faux — c'est le contraire"),
        ("Koffi conseille de vouvoyer le personnel du bureau.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la réplique exacte. La quatrième est "
             "celle que le groupe manque : on retient « madame Paradis » parce que c'est "
             "le premier nom entendu.")

    d.billet(
        "Écrivez une affaire que vous auriez à régler au centre, et à qui vous iriez.",
        exemples=[
            "Une seule affaire, et une seule porte.",
            "Si vous n'êtes pas sûr de la porte, écrivez la question que vous poseriez.",
        ],
        notes="Ramasser les billets : ils servent en A4, où chacun écrira sa première "
              "phrase de comptoir à partir de sa propre affaire.")

    return d.save(dossier)
