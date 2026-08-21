# -*- coding: utf-8 -*-
"""A3 · Les mots du dégât.
Bloc A « Je découvre » · couleur framboise · 75 min. Vocabulaire.
Source : exercices `prVocab` et `prImg`, cartes FC_CARDS.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-degat/images/')


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Les mots du dégât",
        chapeau="Dix-sept mots, et ils ne servent pas seulement à décrire : "
                "ce sont eux qui font qu'on est pris au sérieux au bout du fil.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Prévenir le groupe dès le départ : ces mots-là "
                  "seront réutilisés dans les trois défis. Ce n'est pas une liste à "
                  "apprendre puis à oublier.")

    d.objectifs([
        "nommer ce qu'on voit après un dégât d'eau ;",
        "distinguer la cause, le dommage et la réparation ;",
        "employer le verbe qui va avec chaque surface ;",
        "reconnaître les mots de la démarche : réclamation, franchise, avis.",
    ])

    d.declencheur(
        'Observation', "Nommez ce que vous voyez. Le mot exact, pas « c'est brisé ».",
        image=IMG + 'plancher-gondole.jpg',
        pistes=[
            "Qu'est-ce qui a bougé, exactement ?",
            "Combien de lattes ?",
            "Est-ce que ça se voit ou est-ce que ça se sent sous le pied ?",
            "Quel verbe emploieriez-vous ?",
        ],
        notes="Personne ne dit « gondoler » spontanément. Laisser chercher, accepter "
              "« ça fait des vagues », puis donner le mot : il se retiendra mieux après "
              "l'effort.")

    d.vocabulaire('Vocabulaire · 1 de 3', "Le dégât et ce qu'on voit",
                  [("un dégât d'eau", "les dommages causés par de l'eau répandue"),
                   ("un cerne", "la marque ronde et foncée que l'eau laisse en séchant"),
                   ("le plafond", "ce qui ferme la pièce par le haut"),
                   ("une chaudière", "le seau posé par terre pour recueillir l'eau"),
                   ("gondoler", "se déformer en vagues, comme un plancher qui a bu")],
                  notes="Faire répéter chaque mot avec son article. « Une chaudière » est "
                        "un québécisme : le préciser, plusieurs élèves connaissent « un "
                        "seau ».")

    d.vocabulaire('Vocabulaire · 2 de 3', "La cause et les dommages",
                  [("un chauffe-eau", "le réservoir qui chauffe l'eau du logement"),
                   ("une fuite", "le trou par où l'eau sort d'un appareil ou d'un tuyau"),
                   ("une infiltration", "de l'eau qui passe lentement à travers un mur"),
                   ("les dommages", "tout ce qui a été abîmé, le logement et vos biens"),
                   ("un avis", "un papier officiel affiché ou remis pour annoncer")],
                  notes="Faire distinguer « fuite » et « infiltration » : la première est "
                        "l'endroit d'où ça sort, la seconde le chemin que l'eau prend.")

    d.vocabulaire('Vocabulaire · 3 de 3', "Les travaux et la démarche",
                  [("l'assèchement", "le travail qui fait partir toute l'eau d'un mur"),
                   ("un asséchateur", "l'appareil bruyant qui souffle de l'air sec"),
                   ("une réclamation", "la demande faite à son assureur"),
                   ("une franchise", "le montant qui reste toujours à votre charge"),
                   ("une mise en demeure", "la lettre ferme qui donne un délai précis")],
                  notes="Les trois derniers appartiennent au défi 3. Les nommer dès "
                        "maintenant : les entendre une première fois suffit à les "
                        "installer.")

    d.tableau('Trois familles, trois moments', "Ne pas les mélanger",
              ['La famille', 'Ce qu\'elle nomme'],
              [["la cause", "un chauffe-eau, une fuite, un tuyau — d'où ça vient"],
               ["le dommage", "un cerne, un plancher gondolé, un matelas humide"],
               ["la réparation", "l'assèchement, un asséchateur, des travaux"],
               ["la démarche", "un avis, une réclamation, une franchise"]],
              cle=0,
              note="Un appel bien mené suit exactement cet ordre.",
              notes="C'est le plan du module entier. Le laisser au tableau : il servira "
                    "de repère jusqu'à la séance E2.")

    d.pratique('Pratique · exercice prImg', "Glissez chaque photo sur sa description",
               "Nommez d'abord à voix haute, puis vérifiez dans le module interactif.",
               [("Une marque brune et ronde, plus foncée sur le pourtour.", "un cerne"),
                ("Des lattes de bois qui se soulèvent et font des vagues.",
                 "un plancher qui gondole"),
                ("Un seau de plastique posé par terre.", "une chaudière"),
                ("Le gros réservoir qui chauffe l'eau.", "un chauffe-eau"),
                ("De la peinture qui se décolle en petites bulles.",
                 "de la peinture qui cloque"),
                ("L'appareil bruyant qui souffle de l'air sec.", "un asséchateur")],
               corrige=True, cols=1,
               notes="Six des huit images de l'exercice. Les deux autres — l'avis affiché "
                     "et la boîte de documents — se font dans le module, au défi 2.")

    d.piege("Employer un mot approximatif au téléphone",
            "Il y a de l'eau, c'est tout mouillé.",
            "Un cerne d'un mètre au plafond, et le plancher gondole.",
            "Ce n'est pas une question de beau langage. La personne au bout du fil "
            "décide de l'urgence à partir de ce que vous dites. « C'est tout mouillé » "
            "peut vouloir dire une flaque ou une pièce inondée ; « un cerne d'un mètre » "
            "ne veut dire qu'une chose.",
            notes="Faire refaire la phrase par deux ou trois élèves, avec leurs propres "
                  "mesures. L'exercice de A4 part de là.")

    d.billet(
        "Choisissez trois mots de la séance et écrivez une phrase avec chacun.",
        exemples=[
            "« Le plafond de ma chambre a un cerne brun. »",
            "« Une chaudière est posée sous la fuite. »",
        ],
        notes="Deux minutes. Les phrases servent d'amorce à la description écrite de A4.")

    return d.save(dossier)
