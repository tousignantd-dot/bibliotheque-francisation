# -*- coding: utf-8 -*-
"""C4 · Il faut que, je souhaite que - et le choix entre « de » et « que »
Bloc C « Défi 2 · L'entrevue et le documentaire » · couleur ambre · 75 min.
Source : exercices `t2subj`, `t2dequ` et `t2idees`, avec leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="Il faut que, je souhaite que",
        chapeau="Ce que Myriam Vaugeois demande n'existe pas encore : c'est "
                "pour ça qu'elle dit « il faut que les pièces existent ». Un "
                "souhait n'est pas un fait, et le français le marque dans le "
                "verbe.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 2, et la plus chargée : le subjonctif, le "
                  "choix de la construction, et l'idée principale. Prévoir de reporter "
                  "l'idée principale en D1 si le subjonctif prend tout le temps - c'est "
                  "fréquent et ce n'est pas grave.")

    d.objectifs([
        "employer le subjonctif après il faut que, je veux que, je "
        "souhaite que ;",
        "former le subjonctif à partir de la troisième personne du "
        "pluriel ;",
        "choisir entre « de » et un infinitif, ou « que » et un "
        "subjonctif ;",
        "distinguer une idée principale d'une idée secondaire.",
    ], notes="Le troisième objectif est le plus rentable à l'écrit : c'est lui qui "
             "évite la faute la plus visible dans les lettres du Défi 3.")

    d.declencheur(
        'Observation', "Est-ce que c'est un fait ?",
        pistes=[
            "« Il faut que les pièces existent. » - est-ce qu'elles existent ?",
            "« Je souhaite qu'ils appellent. » - est-ce qu'ils appellent ?",
            "« Je sais qu'ils appellent. » - et ici ?",
            "Qu'est-ce qui change dans le verbe, chaque fois ?",
        ],
        notes="Les deux premières phrases ne rapportent aucun fait, la troisième oui. "
              "C'est toute la différence entre le subjonctif et l'indicatif, et le "
              "groupe la trouve seul en deux minutes.")

    d.tableau('Analyse', "Ce qui demande le subjonctif, ce qui ne le demande pas",
              ['La formule', 'Le verbe qui suit'],
              [["il faut que, je veux que", "subjonctif : ce n'est pas un fait"],
               ["je souhaite que, j'aimerais que", "subjonctif : c'est un souhait"],
               ["je demande que, j'ai peur que", "subjonctif : exigence ou crainte"],
               ["je pense que, je crois que", "indicatif : on présente un fait"],
               ["je sais que, j'espère que", "indicatif : j'espère qu'il rappellera"]],
              cle=0,
              note="Les deux dernières lignes sont les pièges : espérer ne prend jamais le subjonctif.",
              notes="Diapositive à photographier. « J'espère qu'il rappelle » est "
                    "l'erreur attendue chez presque tout le monde. La corriger une fois "
                    "ici et la reprendre chaque fois qu'elle revient.")

    d.regle("Comment le former, à l'oral",
            "Prends la troisième personne du pluriel du présent et enlève la finale.",
            precision="Ils écrivent, donc que j'écrive. Ils appellent, donc qu'ils "
                      "appellent. Pour beaucoup de verbes, le subjonctif s'entend "
                      "exactement comme le présent : il n'y a donc rien de nouveau à "
                      "prononcer. Six irréguliers seulement reviennent partout : que je "
                      "sois, que j'aie, que j'aille, que je fasse, que je puisse, que "
                      "je sache.",
            notes="Diapositive à photographier. Faire fabriquer trois subjonctifs par la "
                  "méthode, au tableau, avant d'aborder les irréguliers. La méthode "
                  "rassure ; la liste, non.")

    d.pratique('Grammaire', "Mettez le verbe au subjonctif présent",
               "Après il faut que, je souhaite que, j'ai peur que.", [
        ("Il faut que les pièces ... (exister) et qu'on puisse les commander.", "existent"),
        ("Je souhaite qu'ils ... (appeler) avant de jeter.", "appellent"),
        ("Elle veut que la personne ... (garder) ses preuves.", "garde"),
        ("Il faut que la personne ... (avoir) gardé sa facture.", "ait"),
        ("Le journal demande que chaque lettre ... (être) signée.", "soit"),
        ("Il faut que tu ... (savoir) ce que tu demandes avant d'écrire.", "saches"),
    ], corrige=True, cols=2,
       notes="Les trois premiers s'entendent comme le présent : le faire remarquer, ça "
             "démystifie. Les trois derniers sont des irréguliers ; les faire répéter à "
             "voix haute plutôt que les expliquer.")

    d.regle("Un seul sujet, ou deux sujets",
            "Même sujet : « de » et un infinitif. Deux sujets : « que » et un subjonctif.",
            precision="Je vous demande d'être prudent - c'est moi qui demande, et c'est "
                      "vous qui devez l'être, mais un seul verbe se conjugue. Je demande "
                      "que les pièces soient disponibles - moi je demande, les pièces "
                      "sont : deux sujets, donc « que ». Vouloir et espérer se passent "
                      "de « de » : je veux partir, j'espère gagner.",
            notes="Diapositive à photographier. C'est la règle la plus rentable de la "
                  "séance : elle supprime d'un coup les « je veux que je comprenne » qui "
                  "reviennent à toutes les productions.")

    d.pratique('Grammaire', "« de » ou « que » ?",
               "Le verbe qui suit vous indique lequel.", [
        ("Je vous demande ... être prudent avec cette expression.", "d' - un seul sujet"),
        ("Je demande ... les pièces soient disponibles.", "que - deux sujets"),
        ("Elle souhaite ... les gens appellent avant de jeter.", "que - deux sujets"),
        ("Il a refusé ... réparer l'appareil.", "de - un seul sujet"),
        ("Il faut éviter ... jeter l'appareil trop vite.", "de - un seul sujet"),
        ("J'ai peur ... perdre mes soirées.", "de - un seul sujet"),
    ], corrige=True, cols=2,
       notes="Poser chaque fois la même question avant de répondre : qui fait le premier "
             "verbe, qui fait le second ? Si c'est la même personne, c'est « de ». "
             "L'automatisme se prend en six phrases.")

    d.pratique('Compréhension', "Idée principale ou idée secondaire ?",
               "Une idée principale se retient seule ; une idée secondaire dépend d'une autre.", [
        ("Trois problèmes se cachent derrière l'expression « obsolescence programmée ».", "idée principale"),
        ("Nos lignes sonnent pendant trois jours.", "idée secondaire - trois jours après quoi ?"),
        ("Un appareil qu'on ne peut pas réparer est jetable, même bien fait.", "idée principale"),
        ("L'entente sur les ampoules a duré seize ans.", "idée secondaire"),
        ("L'Office ne prend pas le dossier en main : il dit ce qu'on peut faire.", "idée principale"),
        ("Les documents ont été retrouvés dans des archives d'entreprise.", "idée secondaire"),
    ], corrige=True,
       notes="Test à donner au groupe : redis l'énoncé à quelqu'un qui n'a rien "
             "entendu. S'il se comprend seul, c'est une idée principale. Sinon, c'est "
             "une idée secondaire. L'idée principale d'une entrevue se cache presque "
             "toujours dans la réponse à la question la plus courte.")

    d.billet(
        "Écris une phrase avec « il faut que » sur le sujet de ton choix.",
        exemples=[
            "Une seule phrase, avec le subjonctif.",
            "Elle servira dans ton courriel de la dernière séance.",
        ],
        notes="Deux minutes. Le courriel de E2 exige un « il faut que » suivi du "
              "subjonctif : ce billet est littéralement une phrase de leur production "
              "finale. Le dire.")

    return d.save(dossier)
