# -*- coding: utf-8 -*-
"""D2 · Avant de partir.
Bloc D « Défi 3 · Quand on doit arrêter » · couleur ambre (écriture) · 75 min.
Source : exercices `t3avant`, `t3demande` et `t3b` ; mini-leçons du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre='Avant de partir',
        chapeau="Une attestation demandée avant le départ se prépare en trois "
                "jours. Demandée après, le dossier est fermé. Toute la séance "
                "tient dans cet ordre-là.",
        duree='75 minutes')

    d.titre(notes="Séance d'écriture et de langue. Le point de grammaire et le conseil "
                  "pratique disent ici exactement la même chose : c'est rare, et ça se "
                  "signale au groupe.")

    d.objectifs([
        "employer avant de devant un verbe ;",
        "employer avant et après devant un nom ou une heure ;",
        "formuler quatre demandes polies ;",
        "lire un formulaire de demande d'attestation.",
    ])

    d.tableau('Analyse', "Avant de, avant, après",
              ["On dit", "Ce qui suit"],
              [["avant de partir", "un verbe qui ne change jamais"],
               ["avant d'arrêter", "un verbe qui commence par une voyelle"],
               ["avant le cours", "un nom : pas de « de »"],
               ["avant 9 heures", "une heure : pas de « de »"],
               ["après le cours", "un nom : jamais de « de » non plus"]],
              cle=1,
              note="Comment choisir : si le mot qui suit est une action, il "
                   "faut « de ». Si c'est une chose, une heure ou un jour, non.",
              notes="Diapo à photographier. Faire produire cinq phrases, une par ligne, "
                    "avec de vraies démarches des élèves.")

    d.regle("Le papier se demande avant",
            "« Avant de partir, je demande mon attestation. »",
            precision="Ce n'est pas une faute de français, c'est la seule "
                      "erreur du module qui coûte vraiment quelque chose. "
                      "Après le départ, le dossier est fermé et tout devient "
                      "plus long.",
            notes="Diapo à photographier. C'est la phrase à emporter du module. La faire "
                  "répéter par tout le groupe, deux fois.")

    d.pratique('Écriture', "Avant de, avant ou après ?",
               "Complétez chaque phrase.", [
        ("___ partir, je demande mon attestation.", "Avant de"),
        ("Je passe au secrétariat ___ le cours, à sept heures cinquante.", "avant"),
        ("___ signer le formulaire, lisez-le au complet.", "Avant de"),
        ("___ le cours, l'enseignante reste dix minutes dans la classe.", "Après"),
        ("Il faut téléphoner ___ neuf heures du matin.", "avant"),
        ("___ arrêter le cours, parlez-en à votre enseignante.", "Avant d'"),
    ], corrige=True,
       notes="La dernière ligne est le cas de la voyelle. Faire lire à voix haute : on "
             "entend pourquoi « de » devient « d' ».")

    d.cartes("Quatre demandes qui ouvrent le comptoir", "À apprendre par cœur", [
        ("Demander une chose",
         "« J'aimerais une attestation de fréquentation, s'il vous plaît. » Plus doux "
         "que « je veux », aussi clair."),
        ("Demander la permission",
         "« Est-ce que je peux garder l'original ? » Une réponse par oui ou par non : "
         "facile à comprendre, facile à donner."),
        ("Demander un service",
         "« Pourriez-vous faire une photocopie, s'il vous plaît ? » Le conditionnel "
         "rend la demande polie sans l'allonger."),
        ("Demander une explication",
         "« Qu'est-ce que je dois apporter ? » · « Quand est-ce que ce sera prêt ? » On "
         "demande ce qu'on n'a pas compris."),
    ], notes="Les quatre servent bien au-delà du centre : à la clinique, à la banque, au "
             "bureau de la garderie. Le dire au groupe.")

    d.pratique('Production orale', "La bonne demande",
               "Une phrase par situation, à voix haute.", [
        ("Vous voulez le papier qui prouve votre fréquentation.", "j'aimerais une attestation, s'il vous plaît"),
        ("Vous voulez garder votre billet d'origine.", "est-ce que je peux garder l'original ?"),
        ("Vous voulez une copie du papier.", "pourriez-vous faire une photocopie ?"),
        ("Vous ne savez pas quel papier apporter.", "qu'est-ce que je dois apporter ?"),
        ("La secrétaire a parlé trop vite.", "pouvez-vous répéter plus lentement ?"),
    ], corrige=True,
       notes="Tour de table. Faire remarquer que la dernière n'est jamais impolie : ce "
             "qui pose problème, c'est de repartir sans avoir compris.")

    d.tableau('Lecture', "Formulaire — Demande d'attestation",
              ["Ligne", "Ce qu'on y écrit"],
              [["Élève", "Nawel Belkacem, groupe 12"],
               ["Motif du départ", "abandon, emploi à temps plein"],
               ["Dernier jour de cours", "vendredi 28 mars"],
               ["Demandée le", "mardi 25 mars"],
               ["Prête le", "vendredi 28 mars, au comptoir"],
               ["Remise", "en main propre, sur signature"]],
              cle=1,
              note="Trois jours entre la demande et le papier : c'est pour ça "
                   "qu'on la fait avant.",
              notes="Diapo à photographier. Faire remplir le même formulaire avec des "
                    "données inventées, en cinq minutes : c'est la meilleure "
                    "préparation à « Je me lance ».")

    d.piege("Demander le papier après être parti",
            "téléphoner deux semaines plus tard",
            "le demander au comptoir, avant le dernier jour",
            "Le dossier fermé, la demande passe par un autre chemin et prend beaucoup "
            "plus de temps. Cinq minutes au comptoir avant de partir remplacent "
            "plusieurs appels.",
            notes="Ne pas en faire une menace : c'est un renseignement pratique. Le "
                  "répéter une fois, calmement, et passer à la suite.")

    d.billet(
        "Remplissez le formulaire de demande avec vos données.",
        exemples=[
            "Votre nom, votre groupe, une date de dernier jour au choix.",
            "Puis écrivez la phrase : « Avant de partir, je… »",
        ],
        notes="Fin du défi 3. Le formulaire rempli sert d'appui direct au jeu de rôle "
              "de E1, cas « le travail à temps plein ».")

    return d.save(dossier)
