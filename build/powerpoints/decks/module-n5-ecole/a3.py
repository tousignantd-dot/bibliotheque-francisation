# -*- coding: utf-8 -*-
"""A3 · Les seize mots du dossier
Bloc A « Je découvre » · couleur framboise · 75 min. Vocabulaire.
Source du module : `FC_CARDS`, exercices `prVocab`, `prImg`.
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
        code='A3', section='framboise',
        titre="Les seize mots du dossier",
        chapeau="Un centre fonctionne au papier, même quand tout est en "
                "ligne. Seize mots suffisent à traverser tout le module : "
                "quatre pour l'établissement, quatre pour l'absence, quatre "
                "pour l'avis officiel, quatre pour la preuve et le "
                "changement.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Le programme ne fournit aucun lexique pour "
                  "cette situation : les seize mots ont été composés à partir des deux "
                  "intentions de communication. Ils sont donc tous utiles, aucun n'est "
                  "là pour faire nombre — le dire au groupe, ça change l'attention.")

    d.objectifs([
        "nommer les quatre familles de mots du module ;",
        "distinguer les documents entre eux : avis, formulaire, attestation, relevé ;",
        "employer chaque mot avec son article ;",
        "reconnaître un mot dans une phrase entendue au comptoir.",
    ], notes="Le deuxième objectif est celui qui coûte un voyage quand il manque. Un "
             "élève qui demande un relevé au secrétariat repart les mains vides, et "
             "il croit qu'on lui a refusé quelque chose.")

    d.vocabulaire('Famille 1', "Le centre et ses gens", [
        ("le secrétariat", "Le bureau, près de l'entrée, où l'on règle tout ce "
                           "qui touche à son dossier d'élève."),
        ("une conseillère", "La personne qui décide de votre parcours : votre "
                            "groupe, votre horaire, la suite de vos cours."),
        ("un local", "La salle où se donne un cours, désignée par son numéro."),
        ("une session", "La période de plusieurs mois pendant laquelle un cours "
                        "se donne, du début à la fin."),
    ], notes="Faire répéter avec l'article. Demander à quelqu'un de dire à voix haute le "
             "numéro du local où le groupe se trouve : c'est la première fois que "
             "beaucoup le disent en français.")

    d.vocabulaire('Famille 2', "L'absence et ce qui la justifie", [
        ("une absence", "Le fait de ne pas être en classe un jour où l'on "
                        "devrait y être."),
        ("un motif", "La raison qu'on donne officiellement pour expliquer une "
                     "demande ou une absence."),
        ("une pièce justificative", "Le papier qui prouve ce qu'on avance : un "
                                    "billet, une lettre, un reçu."),
        ("un rattrapage", "Les heures offertes après coup pour reprendre ce qui "
                          "a été manqué."),
    ], notes="« Motif » est le mot du formulaire ; « raison » est le mot de la "
             "conversation. Les deux se disent, mais c'est « motif » qui est écrit dans "
             "la case, et c'est celui-là qu'il faut reconnaître.")

    d.vocabulaire('Famille 3', "L'avis officiel et ses dates", [
        ("un avis", "Un court document officiel qui vous informe d'une décision "
                    "et de ce que vous devez faire."),
        ("une échéance", "La date à laquelle une chose doit être faite, et après "
                         "laquelle il est trop tard."),
        ("un formulaire", "Une feuille avec des cases à remplir, la même pour "
                          "tout le monde."),
        ("une prolongation", "Le fait de continuer plus longtemps que ce qui "
                             "avait été annoncé."),
    ], notes="« Échéance » est le mot le plus rentable des seize. Le faire répéter trois "
             "fois. Tout le bloc C consiste à la trouver dans une page qui contient "
             "trois dates.")

    d.vocabulaire('Famille 4', "Le changement et la preuve", [
        ("un transfert", "Le passage d'un groupe à un autre, sans quitter le cours."),
        ("une attestation", "Le papier que le centre imprime pour confirmer que "
                            "vous êtes bien inscrit chez lui."),
        ("un relevé", "Le document du ministère qui dit quels cours vous avez "
                      "réussis, et quand."),
        ("un délai", "Le temps qu'il faut attendre avant qu'une demande soit "
                     "traitée."),
    ], notes="Ces quatre-là servent au bloc D. Annoncer que l'attestation et le relevé "
             "seront comparés en A4 : ce n'est pas la même chose, et la confusion est la "
             "plus fréquente de tout le module.")

    d.declencheur(
        'Observation', "Un babillard couvert de feuilles. "
                       "Comment savez-vous laquelle vous concerne ?",
        image=img('babillard-avis.jpg'),
        pistes=[
            "Par quoi commencez-vous : le titre, la date, votre nom ?",
            "Qu'est-ce qui vous fait décrocher d'une feuille officielle ?",
            "Combien de feuilles lisez-vous vraiment, en passant dans un corridor ?",
            "Qu'est-ce qui vous aiderait à repérer la bonne du premier coup ?",
        ],
        notes="Laisser le groupe répondre honnêtement : la plupart n'en lisent aucune. "
              "C'est le point de départ du bloc C — un avis est écrit pour être exact, "
              "pas pour être lu, et il faut une méthode pour le prendre par le bon bout.")

    d.pratique('Vocabulaire', "Le mot juste",
               "Complétez à l'oral, puis à l'écrit.", [
        ("Le ___ est ouvert de huit heures à seize heures.", "secrétariat"),
        ("Le rattrapage se donne au ___ 118.", "local"),
        ("La ___ d'hiver se termine à la fin du mois de juin.", "session"),
        ("Elle a reçu un ___ officiel qui confirme les dates.", "avis"),
        ("Son employeur demande une ___ de fréquentation.", "attestation"),
        ("Le ___ des apprentissages arrive après la fin du cours.", "relevé"),
    ], corrige=True,
       notes="Faire dire la phrase entière, pas seulement le mot. Insister sur l'article : "
             "« un avis », « une attestation ». C'est là que se joue la moitié de la "
             "note en production écrite.")

    d.piege("Dire « papier » pour tout",
            "Je viens chercher mon papier, s'il vous plaît.",
            "Je viens chercher mon attestation de fréquentation.",
            "« Papier » ne fait de mal à personne dans une conversation, mais au "
            "comptoir la personne doit savoir quoi ouvrir dans le système. Sans le "
            "bon mot, elle pose trois questions et la file s'allonge derrière vous.",
            notes="Ne pas présenter « papier » comme fautif : il est juste, et tout le "
                  "monde l'emploie. Ce qui manque, c'est le second mot, celui qui suit.")

    d.billet(
        "Écrivez trois mots du module que vous ne connaissiez pas ce matin.",
        exemples=[
            "Avec leur article, et une courte définition dans vos mots à vous.",
            "Choisissez ceux dont vous aurez besoin, pas les plus difficiles.",
        ],
        notes="Ramasser les billets. Les mots choisis disent où en est chaque élève et "
              "servent à composer le rappel de A4.")

    return d.save(dossier)
