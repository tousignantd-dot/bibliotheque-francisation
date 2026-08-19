#!/usr/bin/env python3
"""Classe de présentation : quinze élèves, quatre modules, toutes les traces.

Sert à montrer l'espace enseignant tel qu'il est en fin d'étape — la
progression du groupe, le dossier d'un élève, ce qui bloque, l'aide que les
modules ont proposée, les productions orales et écrites déposées. Rien ici
n'est un vrai élève : les quinze portent un pseudo, comme le veut le portail.

    python3 build/demo_classe.py --install   # pose la classe
    python3 build/demo_classe.py --purge     # enlève tout ce qu'elle a écrit

La classe occupe les identifiants 201 à 215 : --purge ne retire que ceux-là,
et la petite démonstration de six élèves (101-106, build/demo_traces.py) est
retirée à l'installation parce qu'elle occupe le même groupe.

Les voix des dépôts oraux se fabriquent à part, une seule fois, par
build/demo_classe_audio.py : une réinstallation ne repaie pas la synthèse.
"""

import argparse
import json
import shutil
from datetime import date, timedelta
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
DATA = RACINE / "data"
SAUVEGARDE = DATA / "_sauvegarde-avant-demo-classe"
AUDIO_DEPOTS = RACINE / "assets" / "oral-submissions"
AUDIO_VOIX = RACINE / "build" / "demo-voix-classe"

GROUPE = 1
IDS_ANCIENNE_DEMO = {101, 102, 103, 104, 105, 106}

FICHIERS = [
    "students.json", "schedule.json", "access_log.json", "progress.json",
    "vocab_progress.json", "corrige_moi.json", "oral_submissions.json",
    "written_submissions.json", "analyses_erreurs.json", "signaux_aide.json",
]

# ── Le calendrier ───────────────────────────────────────────────────────────
# Les décalages sont comptés en jours de classe : le 15 et le 16 août 2026
# tombent une fin de semaine, et une trace datée d'un dimanche se remarque.
AUJ = date.today()
OUVRABLES = [0, 1, 4, 5, 6, 7, 8, 11, 12, 13]


def horodatage(jours, heure):
    return f"{(AUJ - timedelta(days=jours)).isoformat()}T{heure}"


# ── Les quatre modules à l'horaire ──────────────────────────────────────────
# Un module terminé, un module en cours, un module ouvert ce matin, un module
# encore à venir : c'est ce contraste qui rend le tableau de bord lisible en
# présentation. `zones` est le nombre de zones à remplir dans le module.
MODULES = {
    35: {"titre": "Module 1 — Consulter au bon endroit", "dossier": "module-consultation",
         "zones": 123, "ouverture": -13, "theme": "Santé"},
    36: {"titre": "Module 2 — Une urgence au travail", "dossier": "module-urgence",
         "zones": 146, "ouverture": -6, "theme": "Santé"},
    34: {"titre": "Module 3 — Prendre rendez-vous et aller à la pharmacie",
         "dossier": "module-sante", "zones": 88, "ouverture": 0, "theme": "Santé"},
    39: {"titre": "Module 4 — Absent ou en retard : que faire ?", "dossier": "module-travail",
         "zones": 152, "ouverture": 6, "theme": "Monde du travail"},
}

# Les autres modules du programme restent au calendrier du groupe, mais plus
# loin dans la session. Sans cela, ils s'ouvriraient tous le même jour et le
# tableau des modules afficherait sept lignes « personne encore » — qui se
# lisent comme un retard alors qu'elles ne sont qu'une planification à plat.
A_VENIR = {40: 13, 41: 20, 42: 27, 43: 34, 44: 41, 45: 48, 46: 55}

# Les consignes des deux cartes « Je me lance », telles que les modules les
# envoient avec le dépôt. Elles s'affichent au-dessus de chaque production
# dans la fiche de l'élève : sans elles, on lit une réponse sans sa question.
PO = {
    35: {"label": "Production orale — décrire une douleur",
         "question": "Décrire une douleur à un professionnel de la santé"},
    36: {"label": "Production orale — décrire une urgence",
         "question": "Décrire une situation d urgence et les premiers soins donnés"},
    34: {"label": "Production orale — prendre un rendez-vous",
         "question": "Appeler une clinique pour obtenir un rendez-vous"},
    39: {"label": "Production orale — message vocal",
         "question": "Laisser un message vocal pour justifier un retard ou une absence"},
}
PE = {
    35: {"label": "Écris pour demander un rendez-vous",
         "question": "Ta douleur ne passe pas. Écris à la clinique sans rendez-vous pour "
                     "obtenir un rendez-vous cette semaine."},
    36: {"label": "Écris un message de réconfort",
         "question": "Ton collègue s'est blessé au travail et reste à la maison pour deux "
                     "semaines. Écris-lui un court message."},
    34: {"label": "Écris pour faire renouveler une ordonnance",
         "question": "Il te reste deux comprimés et ton ordonnance est terminée. Écris à ta "
                     "pharmacie pour demander un renouvellement."},
    39: {"label": "Écris pour justifier un abandon",
         "question": "Tu étudies en comptabilité à Trois-Rivières. Ta famille vient d'obtenir "
                     "un logement à Gatineau et vous déménagez dans trois semaines. Écris à la "
                     "responsable de la formation."},
}

# ── Les quinze élèves ───────────────────────────────────────────────────────
ELEVES = [
    {"id": 201, "code": "ALOU31", "nom": "Alouette"},
    {"id": 202, "code": "BAMB19", "nom": "Bambou"},
    {"id": 203, "code": "CACT62", "nom": "Cactus"},
    {"id": 204, "code": "COLI38", "nom": "Colibri"},
    {"id": 205, "code": "EPIN18", "nom": "Épinette"},
    {"id": 206, "code": "ERAB71", "nom": "Érable"},
    {"id": 207, "code": "ETOI06", "nom": "Étoile"},
    {"id": 208, "code": "FOUG65", "nom": "Fougère"},
    {"id": 209, "code": "GENE77", "nom": "Genévrier"},
    {"id": 210, "code": "HERO52", "nom": "Héron"},
    {"id": 211, "code": "IRIS09", "nom": "Iris"},
    {"id": 212, "code": "LUPI36", "nom": "Lupin"},
    {"id": 213, "code": "MARG74", "nom": "Marguerite"},
    {"id": 214, "code": "NENU28", "nom": "Nénuphar"},
    {"id": 215, "code": "ORIG61", "nom": "Orignal"},
]
IDS_DEMO = {e["id"] for e in ELEVES}

# ── Le travail fait, module par module ──────────────────────────────────────
# (élève, zones réussies, réussies du premier coup, erreurs, jours, heure)
# `zones` à None : l'élève n'a rien ouvert. Un élève absent du tableau d'un
# module n'y a pas de trace du tout.
TRAVAIL = {
    35: [  # Module 1 — terminé pour presque tout le monde
        (201, 123, 111, 14, 11, "10:22:41"),
        (202, 123,  96, 31, 11, "10:31:08"),
        (203, 123,  74, 68,  8, "11:04:52"),
        (204,  61,  44, 39,  8, "09:58:17"),
        (205, 123, 118,  9, 12, "09:47:33"),
        (206, 123,  88, 42, 11, "13:15:26"),
        (207, 123, 115, 12, 12, "10:09:04"),
        (208, 104,  71, 55,  8, "14:02:39"),
        (209, 123,  81, 57,  7, "11:36:12"),
        (210,  38,  22, 44, 12, "09:12:55"),
        (211, 123, 102, 22, 11, "15:20:31"),
        (212, 123,  93, 35,  8, "10:47:19"),
        (213, 118,  60, 88,  7, "13:41:47"),
        (215,  76,  49, 51,  7, "09:33:22"),
    ],
    36: [  # Module 2 — en cours depuis six jours
        (201, 146, 128, 21, 1, "10:15:09"),
        (202, 121,  92, 39, 1, "10:44:37"),
        (203,  84,  51, 62, 0, "11:12:48"),
        (204,  22,  12, 27, 4, "09:41:15"),
        (205, 146, 137, 11, 1, "09:52:26"),
        (206, 109,  74, 48, 0, "13:26:03"),
        (207, 146, 131, 16, 0, "10:05:58"),
        (208,  63,  38, 55, 1, "14:18:44"),
        (209,  97,  62, 61, 0, "11:48:21"),
        (211, 132, 108, 27, 1, "15:02:12"),
        (212, 118,  84, 44, 0, "10:53:36"),
        (213,  71,  33, 79, 1, "13:57:29"),
        (215,  44,  26, 38, 4, "09:26:07"),
    ],
    34: [  # Module 3 — ouvert ce matin
        (201, 32, 29, 4, 0, "11:07:14"),
        (202, 18, 13, 8, 0, "11:22:51"),
        (205, 41, 39, 3, 0, "10:58:32"),
        (206, 11,  7, 6, 0, "11:40:09"),
        (207, 36, 33, 5, 0, "11:14:47"),
        (211, 24, 19, 7, 0, "11:31:20"),
        (203, None, None, None, 0, "11:45:38"),   # ouvert, rien fait encore
        (212, None, None, None, 0, "11:49:02"),
    ],
}

# Ateliers de l'après-midi. Sans eux, la série de jours consécutifs du portail
# élève retomberait à un seul jour : elle compte des dates, pas des exercices.
ATELIERS = [
    (201, 31, "Vocabulaire — Cartes mémoire", 4, "14:35:12", None, None, None, None),
    (201, 37, "Vocabulaire Santé — Cartes illustrées", 5, "14:12:44", None, None, None, None),
    (201,  4, "À la clinique", 12, "14:48:03", 21, 22, 18, 6),
    (202, 31, "Vocabulaire — Cartes mémoire", 5, "15:02:27", None, None, None, None),
    (202, 29, "Corrige-moi ! (assistant oral)", 4, "14:26:51", None, None, None, None),
    (203, 28, "Détective des temps", 6, "14:55:38", 14, 24, 6, 29),
    (205, 37, "Vocabulaire Santé — Cartes illustrées", 4, "14:08:19", None, None, None, None),
    (205, 28, "Détective des temps", 5, "15:11:06", 24, 24, 21, 4),
    (206, 29, "Corrige-moi ! (assistant oral)", 5, "14:44:33", None, None, None, None),
    (207, 31, "Vocabulaire — Cartes mémoire", 1, "14:19:57", None, None, None, None),
    (207,  8, "Chez le Docteur", 11, "14:37:22", 19, 20, 17, 5),
    (208, 31, "Vocabulaire — Cartes mémoire", 6, "15:08:41", None, None, None, None),
    (209, 29, "Corrige-moi ! (assistant oral)", 4, "14:52:15", None, None, None, None),
    (211, 37, "Vocabulaire Santé — Cartes illustrées", 1, "14:23:48", None, None, None, None),
    (211, 28, "Détective des temps", 7, "15:04:29", 20, 24, 15, 12),
    (212, 31, "Vocabulaire — Cartes mémoire", 5, "14:41:36", None, None, None, None),
    (213, 29, "Corrige-moi ! (assistant oral)", 4, "14:58:52", None, None, None, None),
    (215, 31, "Vocabulaire — Cartes mémoire", 7, "14:15:11", None, None, None, None),
]

# ── Les fichiers de séance ouverts depuis le portail ────────────────────────
# (élève, module, jours, heure, fichier)
CONSULTATIONS = [
    (201, 35, 12, "10:04:21", "assets/documents/module-consultation-a1-le-genou-de-yannick.html"),
    (201, 35, 11, "09:58:44", "assets/documents/module-consultation-c2-le-present-de-l-indicatif.html"),
    (201, 36,  5, "10:02:17", "assets/documents/module-urgence-a1-une-brulure-en-cuisine.html"),
    (201, 36,  1, "09:47:33", "assets/powerpoints/module-urgence/B1-a-l-urgence-raconter-ce-qui-est-arrive.pptx"),
    (202, 35, 12, "10:12:09", "assets/documents/module-consultation-a1-le-genou-de-yannick.html"),
    (202, 35,  8, "11:22:48", "assets/documents/module-consultation-c3-la-phrase-negative.html"),
    (202, 36,  4, "10:31:55", "assets/documents/module-urgence-a1-une-brulure-en-cuisine.html"),
    (203, 35,  8, "10:48:26", "assets/documents/module-consultation-c2-le-present-de-l-indicatif.html"),
    (203, 36,  0, "10:57:13", "assets/documents/module-urgence-b2-le-passe-compose.html"),
    (204, 35,  8, "09:44:02", "assets/documents/module-consultation-a1-le-genou-de-yannick.html"),
    (205, 35, 13, "09:31:47", "assets/documents/module-consultation-a1-le-genou-de-yannick.html"),
    (205, 35, 12, "09:39:28", "assets/powerpoints/module-consultation/A4-qui-soigne-quoi-et-ou-aller.pptx"),
    (205, 36,  5, "09:41:11", "assets/documents/module-urgence-a1-une-brulure-en-cuisine.html"),
    (205, 34,  0, "10:44:36", "assets/documents/module-sante-a1-lina-appelle-la-clinique.html"),
    (206, 35, 11, "13:02:19", "assets/documents/module-consultation-c2-le-present-de-l-indicatif.html"),
    (206, 36,  0, "13:11:47", "assets/documents/module-urgence-b2-le-passe-compose.html"),
    (207, 35, 13, "09:52:33", "assets/documents/module-consultation-a1-le-genou-de-yannick.html"),
    (207, 35, 12, "09:56:41", "assets/documents/module-consultation-e2-je-retiens-des-mots.html"),
    (207, 36,  1, "09:48:55", "assets/documents/module-urgence-a1-une-brulure-en-cuisine.html"),
    (207, 34,  0, "10:51:02", "assets/documents/module-sante-a1-lina-appelle-la-clinique.html"),
    (208, 35,  8, "13:47:16", "assets/documents/module-consultation-a1-le-genou-de-yannick.html"),
    (209, 35,  7, "11:18:39", "assets/documents/module-consultation-c3-la-phrase-negative.html"),
    (209, 36,  0, "11:32:24", "assets/documents/module-urgence-b2-le-passe-compose.html"),
    (210, 35, 12, "09:02:48", "assets/documents/module-consultation-a1-le-genou-de-yannick.html"),
    (211, 35, 11, "15:04:12", "assets/documents/module-consultation-c2-le-present-de-l-indicatif.html"),
    (211, 36,  1, "14:51:37", "assets/powerpoints/module-urgence/B1-a-l-urgence-raconter-ce-qui-est-arrive.pptx"),
    (212, 35,  8, "10:29:53", "assets/documents/module-consultation-a1-le-genou-de-yannick.html"),
    (212, 36,  0, "10:38:21", "assets/documents/module-urgence-a1-une-brulure-en-cuisine.html"),
    (213, 35,  7, "13:22:44", "assets/documents/module-consultation-c2-le-present-de-l-indicatif.html"),
    (213, 36,  1, "13:39:08", "assets/documents/module-urgence-b2-le-passe-compose.html"),
    (215, 35,  7, "09:14:36", "assets/documents/module-consultation-a1-le-genou-de-yannick.html"),
]


# ── Ce que les élèves ont dit (« Je me lance », carte orale) ────────────────
# La transcription est ce que la reconnaissance vocale a entendu ; la
# rétroaction, ce que la correction lui a rendu à l'écran. L'audio est
# fabriqué à part par build/demo_classe_audio.py, une voix par élève.
ORAUX = [
    {"eleve": 205, "module": 35, "jours": 12, "heure": "10:03:47",
     "transcription": "Bonjour, j'ai mal à l'épaule droite depuis une semaine. La douleur "
                      "augmente quand je lève le bras et je dors mal à cause de ça.",
     "feedback": "Phrase correcte : Bonjour, j'ai mal à l'épaule droite depuis une semaine. "
                 "La douleur augmente quand je lève le bras et je dors mal à cause de ça."},
    {"eleve": 207, "module": 35, "jours": 12, "heure": "10:16:29",
     "transcription": "J'ai mal au dos depuis trois jours. Ça fait mal quand je me penche pour "
                      "ramasser quelque chose. J'ai pas pris de médicament.",
     "feedback": "Correction : J'ai mal au dos depuis trois jours. Ça fait mal quand je me "
                 "penche pour ramasser quelque chose. Je n'ai pas pris de médicament. | Devant "
                 "un professionnel, on garde le « ne » de la négation : « je n'ai pas pris »."},
    {"eleve": 201, "module": 35, "jours": 11, "heure": "10:29:12",
     "transcription": "Bonjour, ma gorge est très irritée depuis lundi et j'ai de la difficulté "
                      "à avaler. Je fais un peu de fièvre le soir.",
     "feedback": "Phrase correcte : Bonjour, ma gorge est très irritée depuis lundi et j'ai de "
                 "la difficulté à avaler. Je fais un peu de fièvre le soir."},
    {"eleve": 213, "module": 35, "jours": 7, "heure": "13:36:58",
     "transcription": "Moi j'ai mal la tête depuis deux semaine. Je prend des pilule mais ça "
                      "marche pas beaucoup.",
     "feedback": "Correction : J'ai mal à la tête depuis deux semaines. Je prends des pilules, "
                 "mais ça ne fonctionne pas beaucoup. | Trois choses : on dit « avoir mal à la "
                 "tête » ; après « deux », le nom se met au pluriel (« deux semaines », « des "
                 "pilules ») ; et le verbe « prendre » à la première personne s'écrit « je prends »."},
    {"eleve": 202, "module": 36, "jours": 1, "heure": "10:39:24",
     "transcription": "Hier au travail, mon collègue il a tombé de l'escabeau. Il a se blessé au "
                      "poignet. J'ai mis de la glace tout de suite.",
     "feedback": "Correction : Hier au travail, mon collègue est tombé de l'escabeau. Il s'est "
                 "blessé au poignet. J'ai mis de la glace tout de suite. | « Tomber » se conjugue "
                 "avec « être » au passé composé : « il est tombé ». Un verbe pronominal aussi : "
                 "« il s'est blessé », jamais « il a se blessé »."},
    {"eleve": 205, "module": 36, "jours": 1, "heure": "09:44:51",
     "transcription": "Ce matin, je me suis brûlé la main sur la plaque de cuisson. J'ai mis la "
                      "main sous l'eau froide pendant dix minutes, puis j'ai appelé Info-Santé.",
     "feedback": "Phrase correcte : Ce matin, je me suis brûlé la main sur la plaque de cuisson. "
                 "J'ai mis la main sous l'eau froide pendant dix minutes, puis j'ai appelé "
                 "Info-Santé."},
    {"eleve": 211, "module": 36, "jours": 1, "heure": "14:57:33",
     "transcription": "Une cliente a glissé sur le plancher mouillé. Elle s'est fait mal au genou. "
                      "On a appelé l'ambulance et j'ai resté avec elle.",
     "feedback": "Correction : Une cliente a glissé sur le plancher mouillé. Elle s'est fait mal "
                 "au genou. On a appelé l'ambulance et je suis resté avec elle. | « Rester » se "
                 "conjugue avec « être » : « je suis resté »."},
    {"eleve": 209, "module": 36, "jours": 0, "heure": "11:41:16",
     "transcription": "Mon fils il a se coupé le doigt avec un couteau. Le sang il a arrêté après "
                      "dix minute. On a pas allé à l'hôpital.",
     "feedback": "Correction : Mon fils s'est coupé le doigt avec un couteau. Le sang a arrêté de "
                 "couler après dix minutes. Nous ne sommes pas allés à l'hôpital. | On ne répète "
                 "pas le sujet (« mon fils s'est coupé »). Les verbes pronominaux prennent « être » "
                 "au passé composé, « aller » aussi : « nous sommes allés »."},
    {"eleve": 203, "module": 36, "jours": 0, "heure": "11:06:42",
     "transcription": "Il y a un accident. Le monsieur a tombé. Moi j'ai appeler le 911 et après "
                      "j'ai attendre.",
     "feedback": "Correction : Il y a eu un accident. Le monsieur est tombé. J'ai appelé le 911, "
                 "puis j'ai attendu. | Au passé composé, le deuxième verbe est un participe passé, "
                 "pas un infinitif : « j'ai appelé », « j'ai attendu »."},
    {"eleve": 207, "module": 34, "jours": 0, "heure": "11:19:38",
     "transcription": "Bonjour, je m'appelle Étoile. Je voudrais un rendez-vous parce que je "
                      "tousse depuis cinq jours. Est-ce que vous avez une place jeudi matin ?",
     "feedback": "Phrase correcte : Bonjour, je m'appelle Étoile. Je voudrais un rendez-vous "
                 "parce que je tousse depuis cinq jours. Est-ce que vous avez une place jeudi "
                 "matin ?"},
]

# ── Ce que les élèves ont écrit (« Je me lance », carte écrite) ─────────────
ECRITS = [
    {"eleve": 205, "module": 35, "jours": 12, "heure": "10:21:55",
     "texte": "Bonjour,\nJe vous écris pour obtenir un rendez-vous cette semaine. J'ai mal à "
              "l'épaule droite depuis sept jours et la douleur ne diminue pas. Je suis "
              "disponible mardi et jeudi, toute la journée.\nMerci de votre attention,\nÉpinette",
     "feedback": "Phrase correcte : Bonjour, Je vous écris pour obtenir un rendez-vous cette "
                 "semaine. J'ai mal à l'épaule droite depuis sept jours et la douleur ne diminue "
                 "pas. Je suis disponible mardi et jeudi, toute la journée. Merci de votre "
                 "attention, Épinette"},
    {"eleve": 207, "module": 35, "jours": 12, "heure": "10:34:07",
     "texte": "Bonjour,\nJ'ai mal au dos depuis trois jours. Je voudrais voir un médecin cette "
              "semaine. Est-ce que vous avez une place le matin ? Je travaille l'après-midi.\n"
              "Merci beaucoup,\nÉtoile",
     "feedback": "Correction : Bonjour, J'ai mal au dos depuis trois jours. Je voudrais voir un "
                 "médecin cette semaine. Auriez-vous une place le matin ? Je travaille "
                 "l'après-midi. Merci beaucoup, Étoile | « Est-ce que vous avez » est correct ; "
                 "« auriez-vous » est plus poli dans un courriel à une clinique."},
    {"eleve": 201, "module": 35, "jours": 11, "heure": "10:41:33",
     "texte": "Bonjour,\nMa gorge est irritée depuis lundi et j'ai de la fièvre le soir. Je "
              "voudrais un rendez-vous avant vendredi si c'est possible. Je peux venir n'importe "
              "quand.\nMerci,\nAlouette",
     "feedback": "Phrase correcte : Bonjour, Ma gorge est irritée depuis lundi et j'ai de la "
                 "fièvre le soir. Je voudrais un rendez-vous avant vendredi si c'est possible. "
                 "Je peux venir n'importe quand. Merci, Alouette"},
    {"eleve": 212, "module": 35, "jours": 8, "heure": "11:02:19",
     "texte": "Bonjour,\nJe veux un rendez-vous. J'ai mal au ventre depuis quatre jour. Je peut "
              "venir le matin ou l'après-midi. Merci.",
     "feedback": "Correction : Bonjour, Je voudrais un rendez-vous. J'ai mal au ventre depuis "
                 "quatre jours. Je peux venir le matin ou l'après-midi. Merci. | « Je veux » est "
                 "trop direct dans un courriel : on écrit « je voudrais ». Après « quatre », le "
                 "nom se met au pluriel. Le verbe « pouvoir » s'écrit « je peux »."},
    {"eleve": 213, "module": 35, "jours": 7, "heure": "13:52:41",
     "texte": "Bonjour madame,\nJ'ai mal la tête et je dors pas. Ça fait deux semaine. Je veux "
              "voir le docteur vite. Je suis libre tout les jours.\nMerci\nMarguerite",
     "feedback": "Correction : Bonjour madame, J'ai mal à la tête et je ne dors pas. Ça fait deux "
                 "semaines. Je voudrais voir le médecin rapidement. Je suis libre tous les jours. "
                 "Merci, Marguerite | Trois points à revoir : « avoir mal à la tête » ; la "
                 "négation complète (« je ne dors pas ») ; le pluriel après « deux » et dans "
                 "« tous les jours »."},
    {"eleve": 205, "module": 36, "jours": 1, "heure": "10:02:14",
     "texte": "Salut Karim,\nJ'ai appris que tu t'es blessé au dos hier. J'espère que la douleur "
              "diminue. Ne t'inquiète pas pour l'horaire : on s'occupe de tes tâches jusqu'à ton "
              "retour. Repose-toi bien.\nÉpinette",
     "feedback": "Phrase correcte : Salut Karim, J'ai appris que tu t'es blessé au dos hier. "
                 "J'espère que la douleur diminue. Ne t'inquiète pas pour l'horaire : on s'occupe "
                 "de tes tâches jusqu'à ton retour. Repose-toi bien. Épinette"},
    {"eleve": 211, "module": 36, "jours": 1, "heure": "15:11:28",
     "texte": "Bonjour Karim,\nJ'ai su que tu es tombé au travail. J'espère que ton genou va "
              "mieux. Si tu as besoin de quelque chose, tu me appelles. On pense à toi.\nIris",
     "feedback": "Correction : Bonjour Karim, J'ai su que tu es tombé au travail. J'espère que "
                 "ton genou va mieux. Si tu as besoin de quelque chose, tu m'appelles. On pense "
                 "à toi. Iris | Devant une voyelle, « me » devient « m' » : « tu m'appelles »."},
    {"eleve": 202, "module": 36, "jours": 1, "heure": "10:58:36",
     "texte": "Bonjour Karim,\nJe suis désolé pour ton accident. Tu a été très courageux. Repose "
              "toi bien et reviens quand tu es guéri. Nous manque toi.\nBambou",
     "feedback": "Correction : Bonjour Karim, Je suis désolé pour ton accident. Tu as été très "
                 "courageux. Repose-toi bien et reviens quand tu seras guéri. Tu nous manques. "
                 "Bambou | « Tu as » prend un s. À l'impératif, le pronom se rattache par un "
                 "trait d'union : « repose-toi ». Et l'on dit « tu nous manques »."},
    {"eleve": 206, "module": 36, "jours": 0, "heure": "13:44:52",
     "texte": "Bonjour,\nJ'espère que tu va mieux. C'est plate que tu reste à maison deux "
              "semaine. Si tu veux, je passe chez toi samedi.\nÉrable",
     "feedback": "Correction : Bonjour, J'espère que tu vas mieux. C'est dommage que tu restes à "
                 "la maison deux semaines. Si tu veux, je passe chez toi samedi. Érable | « Tu "
                 "vas », « tu restes » : le s de la deuxième personne. On dit « à la maison », et "
                 "« deux semaines » au pluriel."},
    {"eleve": 209, "module": 36, "jours": 0, "heure": "11:57:09",
     "texte": "Salut,\nJ'ai entendu que tu a eu un accident. Prend soin de toi. Le travaille "
              "attend, ta santé non.\nGenévrier",
     "feedback": "Correction : Salut, J'ai entendu que tu as eu un accident. Prends soin de toi. "
                 "Le travail attend, ta santé non. Genévrier | « Tu as » et « prends » prennent "
                 "un s. Le nom s'écrit « le travail » ; « travaille » est le verbe."},
]

# ── Ce qui bloque : les analyses d'erreurs demandées par les élèves ─────────
# (élève, module, exercice, notion, items, erreurs, jours, heure, patron,
#  explication, conseil). Trois notions reviennent chez trois élèves ou plus :
# c'est là que le tableau de bord affiche « À reprendre en groupe ».
ANALYSES = [
    (203, 35, "Le présent de l'indicatif", "Le présent de l'indicatif", 8, 6, 8, "10:52:31",
     "Les terminaisons du singulier",
     "Les six réponses fautives sont des verbes en -er à la deuxième et à la troisième personne du singulier : le s de « tu » et le t muet de « il » manquent chaque fois.",
     "Avant de valider, dis le pronom à voix haute : « tu » demande un s, « il » demande un t muet."),
    (206, 35, "Le présent de l'indicatif", "Le présent de l'indicatif", 8, 5, 11, "13:08:44",
     "Les verbes irréguliers du présent",
     "Les erreurs portent toutes sur « prendre », « venir » et « pouvoir » : les formes régulières en -e ont été appliquées à des verbes qui changent de radical.",
     "Retiens les trois radicaux : je prends, je viens, je peux. Ils reviennent dans presque tous les dialogues du module."),
    (213, 35, "Le présent de l'indicatif", "Le présent de l'indicatif", 8, 7, 7, "13:29:18",
     "Le verbe et son sujet",
     "Le verbe est écrit à l'infinitif dans cinq réponses sur sept : « je prendre », « il aller ». Le lien entre le sujet et la terminaison n'est pas encore fait.",
     "Écris d'abord le pronom, puis demande-toi : qu'est-ce qu'il fait ? La terminaison suit le pronom, jamais l'infinitif."),
    (215, 35, "Le présent de l'indicatif", "Le présent de l'indicatif", 8, 5, 7, "09:21:07",
     "Les terminaisons du singulier",
     "Comme souvent au début, le s de la deuxième personne est oublié quand le verbe est long : « tu explique », « tu commence ».",
     "La longueur du verbe ne change rien : avec « tu », il y a toujours un s à la fin."),
    (202, 35, "La phrase négative", "Pour construire une phrase négative", 6, 4, 8, "11:14:52",
     "Le « ne » de la négation",
     "Le « pas » est bien placé, mais le « ne » manque dans les quatre phrases : c'est la négation de l'oral familier, transportée à l'écrit.",
     "À l'écrit, la négation a toujours deux morceaux : ne … pas. Encadre le verbe avec les deux."),
    (209, 35, "La phrase négative", "Pour construire une phrase négative", 6, 5, 7, "11:27:39",
     "Le « ne » et l'élision",
     "Deux erreurs sont un « ne » oublié ; trois autres sont un « ne » gardé devant une voyelle : « ne ai pas » au lieu de « n'ai pas ».",
     "Devant a, e, i, o, u et h, « ne » devient « n' » : je n'ai pas, il n'est pas."),
    (212, 35, "La phrase négative", "Pour construire une phrase négative", 6, 4, 8, "10:39:14",
     "Le « ne » de la négation",
     "Les quatre phrases fautives sont construites sans « ne ». La place du « pas » après le verbe est juste.",
     "Ajoute le « ne » avant le verbe et relis : ne … pas encadre toujours le verbe conjugué."),
    (208, 35, "Écris la question", "La phrase interrogative", 5, 4, 8, "13:54:26",
     "L'ordre des mots dans la question",
     "Les questions sont écrites dans l'ordre de la phrase affirmative avec un point d'interrogation au bout : « Vous avez une place ? » là où la consigne demandait l'inversion.",
     "Trois façons de poser la question ; celle qu'on te demande ici est l'inversion : Avez-vous une place ?"),
    (204, 35, "Écris la question", "La phrase interrogative", 5, 4, 8, "09:47:58",
     "Le mot interrogatif",
     "Le mot interrogatif manque dans trois réponses : la question porte sur le moment ou le lieu, mais commence directement par le verbe.",
     "Repère d'abord ce que tu veux savoir : quand, où, pourquoi, combien. Le mot interrogatif se place au début."),
    (203, 36, "Le passé composé", "Le passé composé", 10, 7, 0, "11:02:47",
     "L'infinitif à la place du participe",
     "Sept réponses gardent l'infinitif après l'auxiliaire : « j'ai appeler », « j'ai attendre ». Le choix de l'auxiliaire, lui, est juste.",
     "Après « avoir » ou « être », le verbe se termine en -é, -i ou -u : j'ai appelé, j'ai fini, j'ai attendu."),
    (213, 36, "Le passé composé", "Le passé composé", 10, 8, 1, "13:48:12",
     "Le choix de l'auxiliaire",
     "Huit erreurs sur dix sont un « avoir » là où il fallait « être » : tomber, aller, rester, arriver et partir sont tous passés à l'auxiliaire avoir.",
     "Une petite liste de verbes de déplacement va avec « être ». Apprends-les ensemble : aller, venir, arriver, partir, tomber, rester."),
    (209, 36, "Le passé composé", "Le passé composé", 10, 6, 0, "11:36:03",
     "Le choix de l'auxiliaire",
     "Les six erreurs mêlent deux choses : « avoir » avec un verbe de déplacement, et un sujet répété (« mon fils il a »).",
     "Deux réflexes : les verbes de déplacement prennent « être », et le sujet ne se dit qu'une fois."),
    (208, 36, "Le passé composé", "Le passé composé", 10, 6, 1, "14:09:37",
     "Le participe des verbes en -ir et -re",
     "Les verbes en -er sont bien accordés ; les erreurs se concentrent sur « finir », « attendre » et « prendre », dont le participe a été formé en -é.",
     "Trois familles de participes : -é pour les verbes en -er, -i pour ceux en -ir, -u pour beaucoup de verbes en -re."),
    (215, 36, "Le passé composé", "Le passé composé", 10, 6, 4, "09:18:44",
     "L'auxiliaire manquant",
     "Dans cinq réponses, seul le participe est écrit : « je tombé », « il parti ». L'auxiliaire n'a pas été posé.",
     "Le passé composé se fait toujours à deux : l'auxiliaire, puis le participe. Vérifie que ta réponse a bien deux mots."),
    (202, 36, "Les verbes pronominaux au passé composé", "Les verbes pronominaux au passé composé", 6, 4, 1, "10:31:19",
     "La place du pronom",
     "Le pronom est placé après l'auxiliaire dans les quatre réponses : « il a se blessé » au lieu de « il s'est blessé ».",
     "Le pronom vient avant l'auxiliaire, et l'auxiliaire est toujours « être » : il s'est blessé, je me suis brûlé."),
    (206, 36, "Les verbes pronominaux au passé composé", "Les verbes pronominaux au passé composé", 6, 4, 0, "13:19:51",
     "L'auxiliaire des pronominaux",
     "Les quatre erreurs utilisent « avoir » : « je me suis » a été remplacé par « je me ai ».",
     "Un verbe pronominal ne prend jamais « avoir » : je me suis, tu t'es, il s'est."),
    (203, 36, "Répondre avec un pronom complément", "Les pronoms compléments", 7, 5, 0, "11:19:26",
     "Le choix entre le, lui et y",
     "Le pronom direct est mis là où il faut un pronom indirect : « je le téléphone » au lieu de « je lui téléphone ».",
     "Demande-toi si le verbe est suivi de « à » : téléphoner à quelqu'un → lui. Voir quelqu'un → le, la."),
    (212, 36, "Répondre avec un pronom complément", "Les pronoms compléments", 7, 4, 0, "10:47:08",
     "La place du pronom",
     "Le pronom est placé après le verbe dans quatre réponses : « je donne lui » au lieu de « je lui donne ».",
     "En français, le pronom complément passe devant le verbe : je lui donne, je le vois."),
    (208, 36, "Répondre avec un pronom complément", "Les pronoms compléments", 7, 5, 1, "14:22:15",
     "Le choix entre le, lui et y",
     "Cinq réponses reprennent le nom au complet au lieu du pronom : la consigne demandait de remplacer, elle a été lue comme une recopie.",
     "Relis la question : ce qu'on te demande, c'est de ne pas répéter le nom. Le pronom prend sa place."),
    (206, 34, "Le futur proche", "Le futur proche (aller + infinitif)", 6, 4, 0, "11:36:42",
     "Le verbe aller au présent",
     "La construction est comprise, mais « aller » est mal conjugué : « je va prendre », « nous allons prend ».",
     "Le futur proche, c'est aller au présent + l'infinitif : je vais prendre, nous allons prendre."),
    (202, 34, "Le futur proche", "Le futur proche (aller + infinitif)", 6, 3, 0, "11:19:07",
     "L'infinitif après aller",
     "Le deuxième verbe est conjugué au lieu de rester à l'infinitif : « je vais prends ».",
     "Après « aller », le verbe ne bouge plus : il reste à l'infinitif."),
]


# ── L'aide proposée, prise ou refusée ──────────────────────────────────────
# Chaque analyse d'erreur suppose une aide proposée puis acceptée : ces
# signaux-là se déduisent d'ANALYSES. Restent ceux qu'on ne peut pas déduire —
# les refus, et les mini-leçons rouvertes sans qu'il y ait eu d'erreur.
# L'exercice est nommé par son titre, comme le module l'envoie depuis la greffe
# build/greffe_titre_exercice.py — et comme l'analyse d'erreurs le fait déjà :
# les deux journaux doivent tomber sur la même ligne du tableau.
# (élève, module, exercice, proposée, acceptée, refusée, mini-leçons, erreurs, jours, heure)
SIGNAUX_EXTRA = [
    (204, 35, "Le présent de l'indicatif", 2, 0, 2, 0, 6, 8, "09:52:41"),
    (204, 35, "Associe le mot ou le groupe de mots à sa définition", 1, 0, 1, 0, 5, 8, "09:49:12"),
    (210, 35, "Vrai ou Faux — Le genou de Yannick", 2, 0, 2, 0, 7, 12, "09:07:33"),
    (210, 35, "Associe le mot ou le groupe de mots à sa définition", 1, 0, 1, 0, 4, 12, "09:04:18"),
    (213, 35, "Le pluriel des noms et des adjectifs", 2, 1, 1, 1, 6, 7, "13:33:57"),
    (215, 35, "La phrase négative", 1, 0, 1, 0, 4, 7, "09:26:44"),
    (204, 36, "Le passé composé", 2, 0, 2, 0, 8, 4, "09:36:22"),
    (215, 36, "Les verbes pronominaux au passé composé", 1, 0, 1, 0, 5, 4, "09:22:09"),
    (203, 36, "Poser une question polie", 1, 1, 0, 1, 4, 0, "11:23:51"),
    (213, 36, "Le lien d'appartenance", 2, 1, 1, 1, 7, 1, "13:52:36"),
    (208, 36, "Vrai ou Faux — À l'urgence", 1, 0, 1, 0, 4, 1, "14:04:19"),
    # Mini-leçons rouvertes d'elles-mêmes : aucune erreur, juste de la curiosité.
    (205, 35, "Le présent de l'indicatif", 0, 0, 0, 3, 0, 12, "09:58:07"),
    (207, 35, "La phrase négative", 0, 0, 0, 2, 0, 12, "10:12:44"),
    (201, 36, "Le passé composé", 0, 0, 0, 4, 0, 1, "10:08:26"),
    (211, 36, "Les verbes pronominaux au passé composé", 0, 0, 0, 2, 0, 1, "14:48:15"),
    (205, 36, "Répondre avec un pronom complément", 0, 0, 0, 3, 0, 1, "09:47:38"),
    (207, 34, "Le futur proche", 0, 0, 0, 2, 0, 0, "11:11:52"),
    (201, 34, "Les verbes pronominaux", 0, 0, 0, 1, 0, 0, "11:04:29"),
]

# ── « Corrige-moi ! », la pratique libre ────────────────────────────────────
# (élève, thème, réponses, justes du premier coup, jours, heure)
CORRIGE_MOI = [
    (201, "sante", "Santé", 42, 34, 4, "14:31:18"),
    (202, "sante", "Santé", 28, 15, 4, "14:29:47"),
    (203, "sante", "Santé", 19, 7,  6, "14:52:33"),
    (205, "sante", "Santé", 51, 46, 1, "14:06:22"),
    (206, "sante", "Santé", 24, 12, 5, "14:47:09"),
    (207, "sante", "Santé", 38, 31, 1, "14:22:51"),
    (209, "sante", "Santé", 22, 9,  4, "14:56:14"),
    (211, "sante", "Santé", 33, 25, 5, "14:18:36"),
    (213, "sante", "Santé", 17, 5,  4, "15:01:44"),
    (201, "travail", "Monde du travail", 16, 13, 1, "15:12:07"),
    (205, "travail", "Monde du travail", 21, 19, 0, "11:52:38"),
    (207, "travail", "Monde du travail", 14, 11, 1, "15:04:52"),
]

# ── Cartes mémoire ─────────────────────────────────────────────────────────
# box 0 = à revoir tout de suite, 5 = su. Les onze premiers mots sont ceux du
# domaine Santé ; les mots 26 à 30 sont ceux du monde du travail.
VOCABULAIRE = {
    201: {"sante": [5, 5, 4, 5, 4, 5, 4, 3, 4, 3, 3], "travail": [3, 2, 3, 2, 1]},
    202: {"sante": [4, 3, 3, 2, 3, 2, 4, 1, 2, 1, 1], "travail": [1, 1, 0]},
    203: {"sante": [2, 1, 2, 1, 1, 0, 1, 0], "travail": []},
    204: {"sante": [1, 1, 0, 0], "travail": []},
    205: {"sante": [5, 5, 5, 5, 4, 5, 5, 4, 4, 4, 3], "travail": [4, 3, 4, 3, 3]},
    206: {"sante": [3, 2, 3, 2, 2, 1, 3, 1, 2], "travail": [1, 0]},
    207: {"sante": [5, 4, 5, 4, 4, 4, 5, 3, 4, 3, 2], "travail": [3, 3, 2, 2, 1]},
    208: {"sante": [2, 2, 1, 1, 2, 0, 1], "travail": []},
    209: {"sante": [3, 2, 2, 1, 2, 1, 2, 1], "travail": [1]},
    211: {"sante": [4, 4, 3, 4, 3, 3, 4, 2, 3, 2], "travail": [2, 2, 1]},
    212: {"sante": [3, 3, 2, 2, 2, 1, 3, 1], "travail": [1, 1]},
    213: {"sante": [2, 1, 1, 1, 0, 0], "travail": []},
    215: {"sante": [2, 2, 1, 1, 1, 0, 1], "travail": []},
}
MOTS_SANTE = [f"w{i}" for i in range(1, 12)]
MOTS_TRAVAIL = [f"w{i}" for i in range(26, 31)]
INTERVALLES = [1, 2, 4, 8, 16, 32]


# ── Lecture et écriture des fichiers de données ─────────────────────────────

def charger(nom, defaut):
    chemin = DATA / nom
    if not chemin.exists():
        return defaut
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def ecrire(nom, contenu):
    DATA.mkdir(parents=True, exist_ok=True)
    with open(DATA / nom, "w", encoding="utf-8") as f:
        json.dump(contenu, f, ensure_ascii=False, indent=2)


def sauvegarder():
    """Copie les fichiers réels une seule fois, avant la première pose."""
    if SAUVEGARDE.exists():
        return False
    SAUVEGARDE.mkdir(parents=True)
    for nom in FICHIERS:
        source = DATA / nom
        if source.exists():
            shutil.copy2(source, SAUVEGARDE / nom)
    return True


def sans_demo(entrees, cle="studentId"):
    """Retire les enregistrements de la classe de présentation — et ceux de la
    petite démonstration de six élèves, qui occupe le même groupe."""
    exclus = IDS_DEMO | IDS_ANCIENNE_DEMO
    return [e for e in entrees if e.get(cle) not in exclus]


PAR_ID = {e["id"]: e for e in ELEVES}


def base_trace(eleve_id, activite_id, titre):
    e = PAR_ID[eleve_id]
    return {
        "studentId": e["id"], "studentLabel": e["nom"], "groupId": GROUPE,
        "activityId": activite_id, "activityTitle": titre,
        "score": None, "zones": None, "zonesDone": None,
        "firstTry": None, "totalErrors": None,
    }


def poser_planification():
    """Ouvre les quatre modules à des dates différentes pour ce groupe.

    Le tableau de bord compare les traces à la date d'ouverture du module :
    quatre modules ouverts le même jour donneraient quatre colonnes
    identiques, et la période « depuis l'ouverture » ne dirait plus rien.
    """
    horaire = charger("schedule.json", [])
    for act_id, mod in MODULES.items():
        jour = (AUJ + timedelta(days=mod["ouverture"])).isoformat()
        entree = next((h for h in horaire
                       if h.get("groupId") == GROUPE and h.get("activityId") == act_id), None)
        if entree is None:
            entree = {"groupId": GROUPE, "activityId": act_id, "dateFin": ""}
            horaire.append(entree)
        entree["datePrevue"] = jour
        # Un module encore à venir n'a pas été vu : la case reste vide.
        entree["dateVue"] = jour if mod["ouverture"] <= 0 else ""
    for act_id, decalage in A_VENIR.items():
        entree = next((h for h in horaire
                       if h.get("groupId") == GROUPE and h.get("activityId") == act_id), None)
        if entree is None:
            entree = {"groupId": GROUPE, "activityId": act_id, "dateFin": ""}
            horaire.append(entree)
        entree["datePrevue"] = (AUJ + timedelta(days=decalage)).isoformat()
        entree["dateVue"] = ""
    ecrire("schedule.json", horaire)


def installer():
    neuve = sauvegarder()

    # ── Élèves ──────────────────────────────────────────────────────────
    eleves = sans_demo(charger("students.json", []), "id")
    inscription = (AUJ - timedelta(days=13)).isoformat()
    for e in ELEVES:
        eleves.append({
            "id": e["id"], "code": e["code"], "label": e["nom"],
            "prenom": e["nom"], "groupId": GROUPE, "createdAt": inscription,
        })
    ecrire("students.json", eleves)

    poser_planification()

    # ── Traces sur les modules et les ateliers ──────────────────────────
    progression = sans_demo(charger("progress.json", []))
    for act_id, lignes in TRAVAIL.items():
        mod = MODULES[act_id]
        for eleve_id, faites, premier, erreurs, jours, heure in lignes:
            base = base_trace(eleve_id, act_id, mod["titre"])
            moment = horodatage(jours, heure)
            progression.append(dict(base, event="file_opened", timestamp=moment))
            progression.append(dict(base, event="dialogue_listened", timestamp=moment))
            if faites is not None:
                progression.append(dict(
                    base, event="exercise_completed", zones=mod["zones"], zonesDone=faites,
                    firstTry=premier, totalErrors=erreurs, timestamp=moment,
                ))
    for eleve_id, act_id, titre, jours, heure, faites, total, premier, erreurs in ATELIERS:
        base = base_trace(eleve_id, act_id, titre)
        moment = horodatage(jours, heure)
        progression.append(dict(base, event="file_opened", timestamp=moment))
        if faites is not None:
            progression.append(dict(
                base, event="exercise_completed", zones=total, zonesDone=faites,
                firstTry=premier, totalErrors=erreurs, timestamp=moment,
            ))
    progression.sort(key=lambda p: p.get("timestamp", ""))
    ecrire("progress.json", progression)

    # ── Journal des fichiers ouverts ────────────────────────────────────
    journal = sans_demo(charger("access_log.json", []))
    for eleve_id, act_id, jours, heure, fichier in CONSULTATIONS:
        journal.append(dict(
            base_trace(eleve_id, act_id, MODULES[act_id]["titre"]),
            file=fichier, timestamp=horodatage(jours, heure),
        ))
    for entree in journal:
        for cle in ("score", "zones", "zonesDone", "firstTry", "totalErrors"):
            entree.pop(cle, None)
    journal.sort(key=lambda x: x.get("timestamp", ""))
    ecrire("access_log.json", journal)

    # ── Productions orales ──────────────────────────────────────────────
    AUDIO_DEPOTS.mkdir(parents=True, exist_ok=True)
    manquants = []
    depots = sans_demo(charger("oral_submissions.json", []))
    for i, o in enumerate(ORAUX, start=1):
        e = PAR_ID[o["eleve"]]
        mod = MODULES[o["module"]]
        nom_fichier = f"classe{i:02d}-{e['code'].lower()}.mp3"
        voix = AUDIO_VOIX / f"{i:02d}-{e['code'].lower()}.mp3"
        if voix.exists():
            shutil.copy2(voix, AUDIO_DEPOTS / nom_fichier)
        else:
            manquants.append(voix.name)
        depots.append({
            "id": f"classe-{i:02d}-{e['code'].lower()}",
            "studentId": e["id"], "studentCode": e["code"], "groupId": GROUPE,
            "prenom": e["nom"], "theme": mod["theme"],
            "taskId": f"{mod['dossier']}-po",
            "taskLabel": PO[o["module"]]["label"],
            "question": PO[o["module"]]["question"],
            "transcription": o["transcription"], "feedback": o["feedback"],
            "audioUrl": f"/assets/oral-submissions/{nom_fichier}",
            "createdAt": horodatage(o["jours"], o["heure"]),
        })
    ecrire("oral_submissions.json", depots)

    # ── Productions écrites ─────────────────────────────────────────────
    textes = sans_demo(charger("written_submissions.json", []))
    for i, w in enumerate(ECRITS, start=1):
        e = PAR_ID[w["eleve"]]
        mod = MODULES[w["module"]]
        textes.append({
            "id": f"classe-ecrit-{i:02d}-{e['code'].lower()}",
            "studentId": e["id"], "studentCode": e["code"], "groupId": GROUPE,
            "prenom": e["nom"], "theme": mod["theme"],
            "taskId": f"{mod['dossier']}-pe",
            "taskLabel": PE[w["module"]]["label"],
            "question": PE[w["module"]]["question"],
            "texte": w["texte"], "feedback": w["feedback"],
            "createdAt": horodatage(w["jours"], w["heure"]),
        })
    ecrire("written_submissions.json", textes)

    # ── Ce qui bloque : les analyses d'erreurs ──────────────────────────
    analyses = sans_demo(charger("analyses_erreurs.json", []))
    for (eleve_id, act_id, exercice, notion, items, erreurs, jours, heure,
         patron, explication, conseil) in ANALYSES:
        e = PAR_ID[eleve_id]
        analyses.append({
            "patron": patron, "explication": explication, "conseil": conseil,
            "studentId": e["id"], "studentLabel": e["nom"], "groupId": GROUPE,
            "activityId": act_id, "activityTitle": MODULES[act_id]["titre"],
            "exercice": exercice, "notion": notion,
            "items": items, "erreurs": erreurs,
            "timestamp": horodatage(jours, heure),
        })
    analyses.sort(key=lambda a: a.get("timestamp", ""))
    ecrire("analyses_erreurs.json", analyses)

    # ── L'aide proposée, prise ou refusée ───────────────────────────────
    # Une analyse d'erreur ne s'obtient qu'après une aide proposée puis
    # acceptée : ces trois signaux se déduisent d'ANALYSES plutôt que d'être
    # recopiés à la main, où ils finiraient par ne plus concorder.
    signaux = sans_demo(charger("signaux_aide.json", []))
    cumuls = {}

    def cumul(eleve_id, act_id, exercice):
        cle = (eleve_id, act_id, exercice)
        if cle not in cumuls:
            e = PAR_ID[eleve_id]
            cumuls[cle] = {
                "studentId": e["id"], "studentLabel": e["nom"], "groupId": GROUPE,
                "activityId": act_id, "activityTitle": MODULES[act_id]["titre"],
                "exercice": exercice, "lastSeen": "",
            }
            signaux.append(cumuls[cle])
        return cumuls[cle]

    def ajouter(entree, champ, n):
        if n:
            entree[champ] = entree.get(champ, 0) + n

    for (eleve_id, act_id, exercice, _notion, _items, erreurs, jours, heure,
         *_reste) in ANALYSES:
        entree = cumul(eleve_id, act_id, exercice)
        for champ in ("aide_proposee", "aide_acceptee", "aide_analysee"):
            ajouter(entree, champ, 1)
        entree["erreurs"] = erreurs
        entree["lastSeen"] = max(entree["lastSeen"], horodatage(jours, heure))

    for (eleve_id, act_id, exercice, proposee, acceptee, refusee, lecons,
         erreurs, jours, heure) in SIGNAUX_EXTRA:
        entree = cumul(eleve_id, act_id, exercice)
        ajouter(entree, "aide_proposee", proposee)
        ajouter(entree, "aide_acceptee", acceptee)
        ajouter(entree, "aide_refusee", refusee)
        ajouter(entree, "plus_open", lecons)
        if erreurs:
            entree["erreurs"] = max(entree.get("erreurs", 0), erreurs)
        entree["lastSeen"] = max(entree["lastSeen"], horodatage(jours, heure))

    signaux.sort(key=lambda s: s.get("lastSeen", ""))
    ecrire("signaux_aide.json", signaux)

    # ── « Corrige-moi ! » ───────────────────────────────────────────────
    pratique = sans_demo(charger("corrige_moi.json", []))
    for eleve_id, theme_id, theme, reponses, premier, jours, heure in CORRIGE_MOI:
        e = PAR_ID[eleve_id]
        pratique.append({
            "studentId": e["id"], "studentLabel": e["nom"], "groupId": GROUPE,
            "themeId": theme_id, "themeLabel": theme,
            "answers": reponses, "firstTryOk": premier,
            "lastSeen": horodatage(jours, heure),
        })
    ecrire("corrige_moi.json", pratique)

    # ── Cartes mémoire ──────────────────────────────────────────────────
    vocab = sans_demo(charger("vocab_progress.json", []))
    for eleve_id, domaines in VOCABULAIRE.items():
        for mots, boites in ((MOTS_SANTE, domaines["sante"]),
                             (MOTS_TRAVAIL, domaines["travail"])):
            for mot, boite in zip(mots, boites):
                revu = horodatage(OUVRABLES[(boite + 1) % len(OUVRABLES)], "12:00:00")
                vocab.append({
                    "studentId": eleve_id, "wordId": mot, "box": boite,
                    "dueDate": (date.fromisoformat(revu[:10])
                                + timedelta(days=INTERVALLES[boite])).isoformat(),
                    "lastReview": revu,
                })
    ecrire("vocab_progress.json", vocab)

    # ── Compte rendu ────────────────────────────────────────────────────
    print(f"Classe de présentation posée : {len(ELEVES)} élèves, "
          f"{len(MODULES)} modules à l'horaire du groupe {GROUPE}.")
    for act_id, mod in MODULES.items():
        jour = (AUJ + timedelta(days=mod["ouverture"])).isoformat()
        etat = ("à venir" if mod["ouverture"] > 0
                else "ouvert ce matin" if mod["ouverture"] == 0
                else f"ouvert depuis {-mod['ouverture']} jours")
        print(f"  {act_id}  {mod['titre']}  ({jour}, {etat})")
    print(f"\n{len(ORAUX)} productions orales · {len(ECRITS)} productions écrites · "
          f"{len(ANALYSES)} analyses d'erreurs · {len(CORRIGE_MOI)} séances de « Corrige-moi ! »")
    print("\nCodes d'accès :")
    for e in ELEVES:
        print(f"  {e['code']}  {e['nom']}")
    if manquants:
        print(f"\n[!] {len(manquants)} voix manquantes dans "
              f"{AUDIO_VOIX.relative_to(RACINE)}/ : les dépôts oraux n'auront pas d'audio.")
        print("    python3 build/demo_classe_audio.py")
    if neuve:
        print(f"\nDonnées réelles sauvegardées dans {SAUVEGARDE.relative_to(RACINE)}/")
    print("Retrait : python3 build/demo_classe.py --purge")


def purger():
    ecrire("students.json", sans_demo(charger("students.json", []), "id"))
    for nom in ("progress.json", "access_log.json", "corrige_moi.json",
                "vocab_progress.json", "oral_submissions.json",
                "written_submissions.json", "analyses_erreurs.json",
                "signaux_aide.json"):
        ecrire(nom, sans_demo(charger(nom, [])))
    for fichier in AUDIO_DEPOTS.glob("classe*-*.mp3"):
        fichier.unlink()
    # La planification, elle, appartient au groupe et non à la démonstration :
    # on la remet telle qu'elle était plutôt que de l'effacer.
    ancienne = SAUVEGARDE / "schedule.json"
    if ancienne.exists():
        shutil.copy2(ancienne, DATA / "schedule.json")
        print("Planification du groupe remise dans son état d'avant la démonstration.")
    print("Classe de présentation retirée. Les autres élèves et leurs traces sont intacts.")


if __name__ == "__main__":
    parseur = argparse.ArgumentParser(description=__doc__)
    parseur.add_argument("--install", action="store_true", help="poser la classe de présentation")
    parseur.add_argument("--purge", action="store_true", help="retirer la classe de présentation")
    args = parseur.parse_args()
    if args.purge:
        purger()
    elif args.install:
        installer()
    else:
        parseur.print_help()
