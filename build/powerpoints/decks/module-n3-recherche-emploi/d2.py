# -*- coding: utf-8 -*-
"""D2 · Écrivez, cochez, signez, datez.
Bloc D « Défi 3 » · couleur teal · 75 min. Écoute et écriture.
Source du module : exercices `t3imper` et `t3annonce`, mini-leçon `t3imper`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='teal',
        titre='Écrivez, cochez, signez, datez',
        chapeau="Six verbes, et tous les formulaires du Québec s'ouvrent : "
                "ceux de l'emploi, de la clinique, de l'école, de la "
                "bibliothèque. Ils s'écrivent tous de la même façon.",
        duree='75 minutes')

    d.titre(notes="Deuxième séance du défi 3. Distribuer un formulaire vierge à chacun "
                  "et le faire remplir pour de vrai pendant la séance : c'est ce qui "
                  "reste.")

    d.objectifs([
        "reconnaître les six verbes de consigne d'un formulaire ;",
        "comprendre que l'impératif n'est pas impoli ;",
        "remplir un formulaire au complet ;",
        "lire une petite annonce et en repérer les parties.",
    ])

    d.tableau('Analyse', "Les six verbes des formulaires",
              ['Le verbe', 'Ce qu\'il demande'],
              [["Écrivez", "mettre des mots dans une case, en lettres moulées"],
               ["Remplissez", "faire toutes les cases, sans en sauter"],
               ["Cochez", "faire un crochet dans un petit carré : oui ou non"],
               ["Signez", "écrire son nom à la main, en bas"],
               ["Datez", "mettre le jour, le mois et l'année"],
               ["Joignez", "ajouter un papier : une copie, jamais l'original"]],
              cle=0,
              notes="Diapo à photographier, la plus réutilisable du module. Faire "
                    "chercher ces six verbes dans le formulaire distribué.")

    d.regle("L'impératif des formulaires n'est pas impoli",
            "Écrivez. Cochez. Signez.",
            precision="Il n'y a pas de « vous » devant, et ce n'est pas sec : c'est la "
                      "langue des papiers officiels, la même pour tout le monde. Un "
                      "formulaire ne s'adresse à personne en particulier.",
            notes="Diapo à photographier. Plusieurs élèves lisent ces consignes comme "
                  "un ordre brutal : le dire une fois suffit à les rassurer.")

    d.cartes("Deux règles qui évitent des ennuis", "À retenir absolument", [
        ("Aucune case vide",
         "Une case vide ne veut pas dire « non » : elle veut dire que la question n'a "
         "pas été lue. Cochez « non », ou écrivez « aucun ». La personne qui lit ne "
         "devine pas à votre place."),
        ("Une copie, jamais l'original",
         "Carte d'assurance maladie, permis, passeport : on joint une photocopie et "
         "on garde l'original sur soi. Un original remis ne revient pas toujours, et "
         "il est long à remplacer."),
        ("La signature",
         "C'est votre nom écrit à la main, toujours de la même façon. Elle n'a pas "
         "besoin d'être lisible : elle doit être la vôtre, et la même chaque fois."),
        ("La date au Québec",
         "On écrit souvent 2026-08-22 : l'année, le mois, le jour. On peut aussi "
         "écrire 22 août 2026. Les deux se comprennent."),
    ], notes="Faire signer et dater le formulaire distribué avant la fin de la séance : "
             "c'est le geste qu'on oublie le plus souvent.")

    d.piege("Laisser une case vide",
            "Avez-vous un permis de conduire ? (rien de coché)",
            "Cochez « non ».",
            "Celui qui lit ne sait pas si vous avez répondu non ou si vous n'avez pas "
            "compris la question. Dans le doute, il met le formulaire de côté. Une "
            "seconde pour cocher, et le formulaire reste dans la pile.",
            notes="Faire vérifier au voisin, à la fin de la séance, qu'aucune case du "
                  "formulaire n'est restée vide. La vérification croisée marche mieux "
                  "que la relecture par soi-même.")

    d.pratique('Écriture', "Quel verbe manque ?",
               "Complétez avec : écrivez, cochez, signez, datez, remplissez, joignez.", [
        ("___ votre nom en lettres moulées.", "Écrivez"),
        ("___ la case « non » si vous n'avez pas de permis.", "Cochez"),
        ("___ au bas de la page, dans le rectangle.", "Signez"),
        ("___ le formulaire : le jour, le mois et l'année.", "Datez"),
        ("___ toutes les cases : n'en laissez aucune vide.", "Remplissez"),
        ("___ une copie de votre carte d'assurance maladie.", "Joignez"),
    ], corrige=True,
       notes="Même exercice que t3imper dans le module. Faire relire chaque consigne "
             "complète à voix haute, sur le ton neutre d'un formulaire.")

    d.pratique('Lecture', "La petite annonce de Fanta",
               "Lisez l'annonce, puis répondez par vrai ou faux.", [
        ("L'annonce dit ce que Fanta sait faire.", "vrai"),
        ("Elle dit dans quel quartier elle habite.", "vrai"),
        ("Elle est libre le soir et la fin de semaine.", "faux — le matin, en semaine"),
        ("Elle dit combien elle demande de l'heure.", "vrai"),
        ("Elle donne son adresse complète.", "faux — seulement son quartier"),
        ("On peut la joindre par téléphone.", "vrai"),
    ], corrige=True,
       notes="Mêmes énoncés que t3annonce dans le module. Lire l'annonce entière à "
             "voix haute avant : c'est le modèle de la production écrite de E2.")

    d.pratique('Production', "Remplissez le formulaire au complet",
               "Chacun remplit le formulaire distribué. Le voisin vérifie.", [
        ("Les cases d'identité", "nom, prénom, adresse, téléphone, en lettres moulées"),
        ("Le poste demandé", "recopié d'une vraie annonce, mot pour mot"),
        ("Les disponibilités", "des jours et des heures, comme en B4"),
        ("Le bas", "cases cochées, signature, date"),
    ], notes="Vingt-cinq minutes. Passer dans les rangées. La consigne au voisin est "
             "simple : vérifier qu'aucune case n'est vide, rien d'autre.")

    d.billet(
        "Quelle case du formulaire vous a demandé le plus de temps ?",
        exemples=[
            "Le nom de la case, et pourquoi.",
            "Une phrase suffit.",
        ],
        notes="Deux minutes. Les réponses disent où porter l'aide à la prochaine "
              "séance de la session.")

    return d.save(dossier)
