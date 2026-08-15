# -*- coding: utf-8 -*-
"""E1 · À toi : le message et le courriel.
Bloc E · couleur teal (je me lance) · 90 min.
Source : section `appli`, exercice `aSecretaire` et production écrite d'abandon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='À toi : le message et le courriel',
        chapeau="Tout le module en une séance. Écouter un message de la secrétaire, "
                "y répondre au téléphone, puis écrire le courriel le plus difficile "
                "du module : celui d'un abandon.",
        duree='90 minutes')

    d.titre(notes="Séance d'application. Aucun contenu nouveau. Un tiers d'écoute, un "
                  "tiers d'oral, un tiers d'écrit — et tenir l'horaire.")

    d.objectifs([
        "comprendre un message d'information laissé par une secrétaire ;",
        "laisser un message de réponse complet ;",
        "écrire un courriel pour justifier un abandon ;",
        "relire son courriel avant de l'envoyer.",
    ])

    # ── premier temps · l'écoute ───────────────────────────────────
    d.pratique('Pratique · 1 de 4', "Le message de la secrétaire",
               "Un message est laissé à monsieur Diallo au sujet d'une inscription.", [
        ("Quel est le but de l'appel ?",
         "l'informer des dates et des documents pour l'inscription"),
        ("Quand les inscriptions commencent-elles ?", "la semaine prochaine"),
        ("Pourquoi doit-il se rendre au centre ?", "pour confirmer son inscription"),
        ("Quels documents faut-il apporter ?", "une pièce d'identité et une preuve de résidence"),
    ], corrige=True,
       notes="Lire le message deux fois à voix haute avant d'afficher les questions. "
             "Programme visé : soutien informatique. Faire prendre des notes sur la "
             "grille des cinq informations vue en A4.")

    d.regle("La grille de prise de notes",
            "Qui appelle · pourquoi · quelle date · quels documents · quel numéro.",
            precision="Cinq lignes tracées à l'avance sur un papier. On les remplit "
                      "pendant l'écoute, dans le désordre s'il le faut. C'est ce qui "
                      "évite de tout retenir de tête.",
            notes="Faire tracer la grille dans le cahier avant la deuxième écoute. La "
                  "différence de performance est immédiate.")

    # ── deuxième temps · la production orale ───────────────────────
    d.cartes('À l\'oral', "Le message de réponse", [
        ("Se nommer et rappeler pourquoi",
         "« Bonjour, ici Amadou Diallo. Je vous rappelle au sujet de mon inscription au "
         "programme en soutien informatique. »"),
        ("Confirmer ce qu'on a compris",
         "« Vous m'avez dit que les inscriptions commencent la semaine prochaine, et "
         "qu'il faut apporter une pièce d'identité et une preuve de résidence. »"),
        ("Poser sa question",
         "« Est-ce qu'un bail peut servir de preuve de résidence ? » Une question "
         "précise, pas « j'ai des questions »."),
        ("Donner son numéro, deux fois",
         "« Vous pouvez me rappeler au 514 555-0198. Je répète : 514 555-0198. » "
         "Lentement, à la fin."),
    ], notes="Faire remarquer la deuxième carte : reformuler ce qu'on a compris est à la "
             "fois une vérification et une politesse.")

    d.pratique('Pratique · 2 de 4', "Enregistrez votre message de réponse",
               "Quatre parties, quarante secondes. Puis réécoutez-vous.", [
        ("Vous vous nommez", "et rappelez le sujet"),
        ("Vous confirmez", "ce que vous avez compris du message"),
        ("Vous posez une question", "précise, une seule"),
        ("Vous donnez votre numéro", "deux fois, lentement"),
    ], corrige=False,
       notes="Vingt minutes. Chacun écrit puis enregistre. Circuler et écouter deux ou "
             "trois enregistrements.")

    # ── troisième temps · le courriel ──────────────────────────────
    d.regle("Le courriel d'abandon",
            "On dit qu'on part, pourquoi, depuis quand on le sait, et ce qu'on demande.",
            precision="C'est le courriel le plus difficile du module, parce qu'on "
                      "annonce une mauvaise nouvelle. Il se règle en quatre phrases, et "
                      "il vaut mieux l'écrire que de disparaître sans rien dire.",
            notes="Le dire clairement : partir sans prévenir empêche d'obtenir une "
                  "attestation et ferme la porte pour un retour plus tard.")

    d.tableau('Analyse', "Le courriel d'abandon, en quatre phrases",
              ['La phrase', 'Un exemple'],
              [["le but", "Je vous écris pour vous informer que je dois abandonner le cours."],
               ["la raison", "Ma famille déménage à Trois-Rivières le mois prochain."],
               ["la date", "Mon dernier jour de cours sera le 28 mars."],
               ["la demande", "Pourriez-vous me remettre une attestation des cours suivis ?"]],
              cle=0, props=[0.28, 0.72],
              notes="La quatrième phrase est celle que personne n'écrit et qui compte le "
                    "plus : l'attestation peut valoir pour une inscription future.")

    d.cartes('Écrire', "Quatre choses à ne pas oublier", [
        ("L'objet nomme l'abandon",
         "« Abandon du cours — Karim Haddad ». Le mot « abandon » doit y être : c'est "
         "une démarche administrative, pas une absence."),
        ("Le registre reste officiel",
         "Même si vous connaissez bien l'enseignante. Un abandon passe par la "
         "direction : le courriel sera transmis."),
        ("Une seule phrase de regret",
         "« Je regrette de devoir interrompre le cours. » Une fois, pas trois."),
        ("Demander l'attestation",
         "Elle prouve les heures suivies. Elle peut être exigée pour une inscription "
         "ailleurs, ou pour un employeur."),
    ], notes="Insister sur la quatrième carte. C'est un droit que peu de gens "
             "connaissent, et il se perd si on ne le demande pas.")

    d.pratique('Pratique · 3 de 4', "Écrivez le courriel d'abandon",
               "Cinq parties, quatre phrases dans le corps.", [
        ("La situation",
         "Vous déménagez dans une autre ville le mois prochain et devez abandonner le "
         "cours."),
        ("Ce que vous annoncez", "la date de votre dernier jour de cours"),
        ("Ce que vous demandez", "une attestation des cours suivis"),
    ], corrige=False,
       notes="Vingt-cinq minutes d'écriture. Ramasser : c'est l'évaluation écrite du "
             "module.")

    d.pratique('Pratique · 4 de 4', "Relisez avant d'envoyer",
               "Six vérifications, dans l'ordre.", [
        ("L'objet dit-il de quoi il s'agit ?", "en trois ou quatre mots"),
        ("Le but est-il dans la première phrase ?", "pas à la fin"),
        ("L'appel et la salutation sont-ils du même registre ?", "officiel avec officiel"),
        ("Ai-je écrit mon nom complet ?", "prénom et nom de famille"),
        ("Ai-je donné une date précise ?", "le dernier jour de cours"),
        ("Ai-je demandé quelque chose ?", "une attestation, un rappel"),
    ], corrige=True,
       notes="Faire faire la relecture par le voisin. Une relecture croisée trouve deux "
             "fois plus d'oublis qu'une relecture par l'auteur.")

    d.billet(
        "En une phrase : qu'est-ce que vous ferez différemment la prochaine fois que vous serez en retard ?",
        exemples=[
            "Pensez à la première séance : prévenir avant de partir, pas après.",
            "Une seule phrase, honnête. Elle n'est pas notée.",
        ],
        notes="Lire quelques billets à voix haute, sans nommer les auteurs. C'est la "
              "meilleure préparation à la séance de bilan.")

    return d.save(dossier)
