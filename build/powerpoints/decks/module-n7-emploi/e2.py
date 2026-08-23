# -*- coding: utf-8 -*-
"""E2 · Écrivez la note de service
Bloc E « Je me lance » · couleur framboise · 75 min. Dernière séance.
Source du module : production écrite de « Je me lance », section
« Je retiens des mots » et son autoévaluation.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Écrivez la note de service",
        chapeau="La présentation est faite ; il faut maintenant l'annoncer à "
                "l'équipe. Huit à douze phrases, six parties, et pas une "
                "formule de politesse à la fin.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Trois temps : l'écriture de la note, la "
                  "correction par l'IA puis l'envoi, et le bilan. Garder vingt minutes "
                  "pour le bilan : c'est là que l'élève mesure ce qu'il sait faire.")

    d.objectifs([
        "écrire une note de service complète, avec ses six parties ;",
        "employer au moins un connecteur et une phrase passive ;",
        "relire ses verbes en -rai et en -rais avant d'envoyer ;",
        "évaluer ce qu'on est maintenant capable de faire.",
    ], notes="Le troisième objectif est une consigne de relecture, pas un savoir. "
             "L'écrire au tableau et l'y laisser pendant toute la séance.")

    d.declencheur(
        'Rappel', "Avant d'écrire : à qui écrivez-vous ?",
        pistes=[
            "À des collègues que vous croisez tous les jours.",
            "Donc : « vous », pas « Monsieur ». Pas de vedette, pas de salutation.",
            "Six parties, huit à douze phrases.",
            "Et une demande : qu'est-ce que le lecteur doit faire ?",
        ],
        notes="Cinq minutes, pas plus. La séance D1 a déjà tout donné ; il s'agit de "
              "réactiver, pas de réenseigner.")

    d.tableau('Analyse', "Ce que votre note doit contenir",
              ['L\'exigence', 'Comment la remplir'],
              [["L'en-tête", "destinataires, expéditeur, date, objet"],
               ["Un objet sans verbe", "six à dix mots, un groupe du nom"],
               ["Une date de début", "et une durée, si c'est un essai"],
               ["Une demande datée", "ce que le lecteur fait, et avant quand"],
               ["Une signature", "prénom, nom, fonction. Rien après."]],
              cle=0,
              note="Et dans le texte : au moins un connecteur, et une phrase passive du genre « il vous est demandé de... ».",
              notes="Diapositive à photographier, et à laisser projetée pendant "
                    "l'écriture. C'est la liste que le module affiche aussi, dans la "
                    "carte de production écrite.")

    d.regle("Relisez vos verbes en -rai et en -rais",
            "L'un annonce, l'autre demande. Le -s change tout.",
            precision="« Je demanderai » dit ce que vous ferez. « Je demanderais » "
                      "demande poliment. À l'oral, la différence s'entend à peine ; à "
                      "l'écrit, elle décide du sens. C'est la faute la plus fréquente "
                      "des écrits de travail, et la seule qui se corrige en trente "
                      "secondes de relecture ciblée.",
            notes="Diapositive à photographier. Faire faire la relecture ciblée à voix "
                  "basse : chercher uniquement les verbes en -rai et -rais, ne rien "
                  "lire d'autre. C'est une technique, et elle s'apprend.")

    d.cartes('Production écrite', "Trois temps, dans cet ordre", [
        ("1 · Écrire", "Huit à douze phrases dans le module, section « Je me lance ». Le compteur de phrases vous suit."),
        ("2 · Faire vérifier", "« Vérifier mon texte » : l'IA vous répond à l'écran. Cette correction reste privée, personne d'autre ne la voit."),
        ("3 · Corriger, puis envoyer", "Le bouton d'envoi n'apparaît qu'après la vérification : on ne dépose pas un texte non relu."),
        ("Et si vous allez plus vite", "Écrivez ensuite la lettre d'affaires au fournisseur, avec ses sept parties. Demande de soumission, jamais commande."),
    ], notes="Insister sur le deuxième point : plusieurs élèves n'osent pas demander "
             "la correction parce qu'ils croient qu'elle sera vue. Elle ne l'est pas.")

    d.pratique('Relecture', "Six vérifications avant d'envoyer",
               "Passez votre note à travers cette liste.", [
        ("L'objet n'a aucun verbe conjugué.", ""),
        ("La date est en toutes lettres.", ""),
        ("Il y a une date de début et une durée.", ""),
        ("On sait ce que le lecteur doit faire, et avant quand.", ""),
        ("Il y a au moins un connecteur.", ""),
        ("La note finit sur une fonction, pas sur « veuillez agréer ».", ""),
    ], notes="Faire échanger les cahiers : chacun relit la note de son voisin avec "
             "cette liste. Six vérifications mécaniques se font mieux à deux, et "
             "l'erreur des autres s'attrape plus facilement que la sienne.")

    d.tableau('Bilan', "Ce que vous savez faire maintenant",
              ['Le savoir-faire', 'Où vous l\'avez travaillé'],
              [["Suivre une présentation longue", "Défi 1, la réunion de production"],
               ["Présenter en cinq parties", "Défi 2, le poste 4"],
               ["Écrire une note de service", "Défi 3, et aujourd'hui"],
               ["Écrire une lettre d'affaires", "Défi 3, en variante"],
               ["Connaître vos droits en SST", "Défi 2, programme et droit de refus"]],
              cle=0,
              note="Le seul de ces cinq qui serve hors du travail est le dernier - et c'est peut-être le plus important.",
              notes="Diapositive à photographier. Ouvrir ensuite « Je retiens des "
                    "mots » dans le module : l'autoévaluation en seize énoncés, que "
                    "chacun remplit seul.")

    d.piege('Bilan',
            "croire qu'un projet refusé est un projet perdu",
            "un projet refusé est un projet daté",
            "Un projet présenté correctement laisse une trace : une date à l'ordre du "
            "jour, un compte rendu, une note de service. Six mois plus tard, quand la "
            "situation aura empiré ou que le budget se sera libéré, cette trace "
            "existera encore - et c'est votre nom qui sera dessus. Aïcha n'a rien "
            "obtenu le premier jour : elle a obtenu quinze minutes le 15 septembre.",
            notes="Bonne dernière diapositive de contenu. Beaucoup d'élèves n'osent "
                  "pas présenter par peur du refus ; c'est ce qu'il faut désamorcer en "
                  "terminant.")

    d.billet(
        "Une chose que vous allez faire cette semaine, à votre travail.",
        exemples=[
            "Regarder s'il y a un programme de prévention.",
            "Demander une place à l'ordre du jour.",
            "Écrire une note de service, ou juste son objet.",
        ],
        notes="Dernier billet du module. Ramasser et lire à voix haute deux ou trois "
              "réponses, sans nommer les auteurs : c'est ce qui donne au groupe l'idée "
              "que la chose est possible.")

    return d.save(dossier)
