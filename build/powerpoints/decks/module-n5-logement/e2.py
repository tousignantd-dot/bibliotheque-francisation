# -*- coding: utf-8 -*-
"""E2 · Le courriel de notes, et le bilan.
Bloc E « Je me lance » · couleur framboise · 60 min.
Source : production écrite, banc de vocabulaire et autoévaluation du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Le courriel de notes, et le bilan",
        chapeau="Seize mots, sept points de langue, dix questions. Dernière "
                "séance : on écrit, on rassemble, et chacun fait le point.",
        duree='60 minutes')

    d.titre(notes="Séance de bilan. Rendre tous les billets corrigés du module avant de "
                  "commencer, et prévoir du temps pour la production écrite : c'est elle "
                  "qui compte.")

    d.objectifs([
        "écrire un courriel qui rapporte les renseignements d'un appel ;",
        "employer deux phrases rapportées dans un texte suivi ;",
        "rassembler le vocabulaire du module en quatre familles ;",
        "évaluer ce que je suis maintenant capable de faire.",
    ])

    d.tableau('La production écrite', "Ce que le courriel doit contenir",
              ['L\'élément', 'Ce qu\'on écrit'],
              [["Le loyer et la date", "1 050 $ par mois, libre le 1er juillet"],
               ["Ce qui est inclus", "et surtout ce qui ne l'est pas"],
               ["Deux phrases rapportées", "« Elle me dit que… », « Je lui ai demandé si… »"],
               ["Ce qui reste à vérifier", "le bruit, les fenêtres, le loyer d'avant"],
               ["Le rendez-vous", "jeudi 18 h, 412 rue Bowen, appartement 3"]],
              cle=0,
              note="De 6 à 10 phrases. Rapportez, ne recopiez pas.",
              notes="Diapositive à photographier. C'est la consigne et la grille de "
                    "correction. Insister sur la dernière ligne de la note : « Elle me dit "
                    "que le chauffage n'est pas inclus », et non « Le chauffage n'est pas "
                    "inclus. »")

    d.pratique('Écriture', "Écrivez le courriel",
               "À la personne qui déménagera avec vous, après votre appel.", [
        ("L'ouverture", "Bonjour, j'ai appelé pour le quatre et demie de la rue Bowen."),
        ("Ce qu'on vous a dit", "Elle me dit que le logement est libre le premier juillet."),
        ("La question que vous avez posée", "Je lui ai demandé si le chauffage était inclus."),
        ("La réponse", "Il ne l'est pas : il faut compter environ cent dollars par mois."),
        ("Ce qui reste", "Il reste à vérifier le bruit et l'état des fenêtres."),
        ("Le rendez-vous", "La visite est jeudi à dix-huit heures."),
    ], corrige=False,
       notes="Quarante minutes d'écriture au propre. Circuler et corriger les phrases "
             "rapportées en priorité : c'est le point de langue évalué. Le dépôt se fait "
             "dans le module.")

    d.vocabulaire('Famille · 1 de 4', "Le logement et l'annonce", [
        ("un quatre et demie", "Deux chambres, un salon, une cuisine, plus la salle de bain."),
        ("chauffé et éclairé", "Le loyer comprend le chauffage et l'électricité."),
        ("un plancher de bois franc", "De vraies planches de bois dur."),
        ("ensoleillé", "Le soleil entre une bonne partie de la journée."),
        ("insonorisé", "On n'entend pas les voisins."),
    ], notes="« Chauffé et éclairé » s'écrit C/E dans les annonces : le rappeler une "
             "dernière fois.")

    d.vocabulaire('Famille · 2 de 4', "L'appel et la visite", [
        ("la date d'occupation", "Le jour où le bail commence."),
        ("les électroménagers", "Poêle, réfrigérateur, laveuse, sécheuse."),
        ("une buanderie", "Le local commun où les locataires lavent leur linge."),
        ("une case de stationnement", "L'espace réservé où un locataire gare son auto."),
        ("une remise", "Un petit espace fermé pour ranger vélos et pneus."),
    ], notes="Ces cinq mots sont exactement les cinq renseignements qu'on va chercher au "
             "téléphone.")

    d.vocabulaire('Famille · 3 de 4', "Le bail", [
        ("un bail", "Le contrat écrit, sur le formulaire officiel du Québec."),
        ("le loyer", "La somme payée chaque mois."),
        ("un avis de modification", "Ce que le propriétaire veut changer l'an prochain."),
        ("le renouvellement", "Le bail recommence sans qu'on le resigne."),
    ], notes="Faire redire la règle du silence : il coûte cher devant un avis de "
             "modification, et il protège à la fin d'un bail.")

    d.vocabulaire('Famille · 4 de 4', "Mes droits", [
        ("sous-louer", "Laisser quelqu'un habiter chez soi en gardant son bail."),
        ("le Tribunal administratif du logement",
         "L'organisme qui tranche entre locataire et propriétaire."),
    ], notes="Rappeler l'ancien nom, la Régie du logement : les élèves l'entendront encore "
             "longtemps autour d'eux.")

    d.tableau('Les points de langue · 1 de 2', "Écouter et rapporter",
              ['Le point', 'En une phrase'],
              [["sur le, dans la, à la", "à l'oral, les deux mots se collent"],
               ["le discours indirect", "« est-ce que » devient « si », et les pronoms changent"],
               ["qui, que, où", "on regarde ce qui suit le petit mot"]],
              cle=0,
              note="Les trois points des défis 1 et 2.",
              notes="Faire reformuler chaque ligne par un élève différent avant d'afficher "
                    "la colonne de droite.")

    d.tableau('Les points de langue · 2 de 2', "Décrire et lire un contrat",
              ['Le point', 'En une phrase'],
              [["le gérondif", "en + le verbe en -ant, même sujet pour les deux"],
               ["le futur simple", "l'infinitif plus les terminaisons d'avoir"],
               ["les impersonnelles", "un « il » qui ne désigne personne"]],
              cle=0,
              note="Six lignes, six séances de grammaire.",
              notes="C'est la révision la plus efficace de la séance : reformuler avant de "
                    "lire.")

    d.piege("Croire qu'on ne peut rien dire à un propriétaire",
            "C'est lui qui décide, je n'ai rien à dire.",
            "J'ai un mois pour répondre, et le droit de refuser.",
            "C'est le fil de tout le module. Poser huit questions au téléphone, demander "
            "le loyer de l'ancien locataire, lire le bail avant de signer, refuser une "
            "hausse par écrit : ce sont quatre gestes ordinaires, et ils sont tous permis.",
            notes="Fermer le module là-dessus. Pour beaucoup d'élèves, c'est le vrai "
                  "apprentissage — plus que la grammaire.")

    d.billet(
        "Gardez la feuille des huit questions dans vos papiers.",
        exemples=[
            "Vous en aurez besoin le jour où vous chercherez un logement.",
            "Et le 1er juillet arrive vite.",
        ],
        notes="Dernier billet du module. Faire l'autoévaluation dans le module interactif "
              "avant de partir : dix énoncés, trois choix.")

    return d.save(dossier)
