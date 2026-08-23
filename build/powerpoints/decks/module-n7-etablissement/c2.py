# -*- coding: utf-8 -*-
"""C2 · Demander sans exiger
Bloc C « Défi 2 · L'entrevue de sélection » · couleur ambre · 75 min.
Source : exercice `t2cond` et sa mini-leçon (conditionnel présent).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Demander sans exiger',
        chapeau="« Vous pouvez me dire la date ? » et « pourriez-vous me dire "
                "la date ? » demandent la même chose. La seconde obtient une "
                "réponse plus souvent.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire orale. Faire dire les phrases plutôt que les "
                  "écrire : le conditionnel de politesse est une affaire de bouche.")

    d.objectifs([
        "former le conditionnel présent de six verbes courants ;",
        "poser une question au conditionnel de politesse ;",
        "employer l'imparfait après « si » et le conditionnel ensuite ;",
        "distinguer « je serai » et « je serais » à l'écrit.",
    ], notes="Le quatrième objectif est celui de la lettre : « je serai disponible » "
             "engage, « je serais disponible » n'engage à rien.")

    d.declencheur(
        'Écoute', "Laquelle des deux obtient une réponse ?",
        pistes=[
            "« Donnez-moi la date de la décision. »",
            "« Vous pouvez me dire la date ? »",
            "« Pourriez-vous me dire à quel moment la décision sera prise ? »",
            "Pourquoi la troisième, alors qu'elle est plus longue ?",
        ],
        notes="Réponse attendue : parce qu'elle laisse à l'autre la possibilité de "
              "dire non. C'est exactement pour cela qu'il dit oui.")

    d.regle("Radical du futur, terminaisons de l'imparfait",
            "pouvoir : je pourrais · vouloir : je voudrais · être : ce serait · "
            "avoir : j'aurais",
            precision="Il n'y a rien d'autre à savoir : tout verbe irrégulier au futur "
                      "l'est au conditionnel, de la même façon. Les terminaisons sont "
                      "celles de l'imparfait : -ais, -ais, -ait, -ions, -iez, -aient.",
            notes="Diapositive à photographier. Faire conjuguer « pouvoir » en entier "
                  "à voix haute, et rappeler le « e » de « nous pourrions » vu en A2.")

    d.tableau('Analyse', "Les six verbes de l'entrevue",
              ['Le verbe', 'Ce qu\'on dit'],
              [['pouvoir', "pourriez-vous me préciser la date ?"],
               ['vouloir', "je voudrais savoir si les cours sont le jour"],
               ['avoir', "j'aurais deux ou trois questions"],
               ['savoir', "sauriez-vous s'il reste des places ?"],
               ['être', "ce serait ma deuxième demande"],
               ['devoir', "je devrais d'abord régler mon horaire"]],
              cle=0,
              notes="Six rangées, aucune note : la densité tient. Faire répéter chaque "
                    "ligne en chœur, puis par un élève seul.")

    d.regle("Après « si », jamais de conditionnel",
            "Si j'étais admise en janvier, je garderais mes deux quarts.",
            precision="L'imparfait va après « si », le conditionnel dans l'autre "
                      "moitié de la phrase. C'est l'erreur la plus repérée du niveau, "
                      "et elle s'entend tout de suite.",
            notes="Diapositive à photographier. Écrire la forme fautive au tableau, la "
                  "faire corriger par le groupe, puis l'effacer — ne pas la laisser "
                  "sous les yeux.")

    d.pratique('Grammaire', "Mettez le verbe à la bonne forme",
               "Conditionnel présent, ou imparfait après « si ».", [
        ("(Pouvoir) ___-vous me préciser quand la décision sera communiquée ?", "Pourriez"),
        ("Je (vouloir) ___ savoir si les cours du premier bloc sont le jour.", "voudrais"),
        ("Si j'(être) ___ admise en janvier, je garderais mes deux quarts.", "étais"),
        ("J'(avoir) ___ deux ou trois questions à vous poser avant de partir.", "aurais"),
        ("(Savoir) ___-vous s'il reste des places pour l'entrée de janvier ?", "Sauriez"),
        ("Si je faisais la mise à niveau, mon dossier (être) ___ plus fort.", "serait"),
    ], corrige=True,
       notes="Faire lire chaque phrase corrigée à voix haute, en vouvoyant. Ce sont "
             "les questions qu'ils poseront au bloc E.")

    d.piege('Piège', "Je serais disponible dès le mois de septembre.",
            "Je serai disponible dès le mois de septembre.",
            "Le conditionnel sert à demander, jamais à s'engager. Quand la chose est "
            "réglée, on dit « je serai » : une lettre qui écrit « je serais » laisse "
            "penser qu'il reste une condition.",
            notes="Faute très fréquente chez ceux qui viennent d'apprendre le "
                  "conditionnel : ils le mettent partout. Le nommer explicitement.")

    d.billet("Écris les deux questions que tu poserais à la fin d'une entrevue.",
             exemples=["Pourriez-vous me dire quand la décision sera communiquée ?",
                       "Sauriez-vous s'il y a une entrée en janvier ?"],
             notes="Ramasser les billets. Les meilleures questions serviront de banque "
                   "commune au jeu de rôle du bloc E.")

    return d.save(dossier)
