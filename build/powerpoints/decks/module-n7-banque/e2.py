# -*- coding: utf-8 -*-
"""E2 · La lettre qui laisse une trace
Bloc E « Je me lance » · couleur framboise · 90 min. Bilan du module.
Source : production écrite de « Je me lance » et exercice `t3lettre`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre='La lettre qui laisse une trace',
        chapeau="Trente jours ont passé, le montant est toujours au relevé. "
                "Un appel ne laisse rien derrière lui ; une lettre datée, si.",
        duree='90 minutes')

    d.titre(notes="Dernière séance. Elle se termine par l'autoévaluation du module : "
                  "prévoir vingt minutes pour elle, elle n'est pas décorative.")

    d.objectifs([
        "écrire une lettre de réclamation en trois paragraphes ;",
        "choisir un objet qui trie la lettre sur la bonne pile ;",
        "tenir un ton ferme et neutre du premier mot au dernier ;",
        "demander une date de réponse plutôt que de l'espérer.",
    ], notes="Le troisième objectif vient du programme : « choisir et maintenir un ton "
             "approprié ». Le mot qui compte est « maintenir ».")

    d.declencheur(
        'Observation', "Pourquoi écrire, quand on a déjà téléphoné ?",
        pistes=[
            "Que reste-t-il d'un appel, six mois plus tard ?",
            "Qui se souvient de ce qui a été dit ?",
            "Qu'est-ce qu'une lettre datée prouve ?",
            "Combien de temps ça prend, écrire douze phrases ?",
        ],
        notes="La dernière question ramène tout le monde sur terre : vingt minutes. "
              "C'est le meilleur argument de la séance.")

    d.regle("Une lettre de réclamation n'est pas une lettre de colère",
            "Elle a un seul but : obtenir une réponse écrite.",
            precision="Tout ce qui n'y contribue pas l'affaiblit. Le récit de votre "
                      "journée, ce que vous pensez du service, le nombre de fois où "
                      "vous avez rappelé : rien de cela n'aide. Le lecteur traite "
                      "quarante dossiers par jour. Écrivez pour lui.",
            notes="Diapositive à photographier. Le dire sans moraliser : ce n'est pas "
                  "une question de politesse, c'est une question d'efficacité.")

    d.tableau('Analyse', "Ce qu'on écrit, ce qui marche",
              ['Ce qui vient à l\'esprit', 'Ce qui fonctionne'],
              [['Problème avec ma carte', 'Contestation, dossier, 780 $'],
               ["Je suis désolée de vous déranger", "(rien : on entre dans le sujet)"],
               ["C'est inadmissible", 'Je constate que le montant y figure'],
               ["J'ai rappelé quatre fois", "J'ai signalé le 15 mars à 11 h 20"],
               ["J'espère une réponse rapide", "Je vous demande de répondre d'ici le 30"]],
              cle=0,
              notes="Diapositive à photographier. La cinquième ligne est celle qui "
                    "change le plus la réponse obtenue.")

    d.regle("Une date se demande, elle ne se souhaite pas",
            "« Je vous demande de me répondre par écrit d'ici le 30 avril. »",
            precision="Une date crée une échéance ; un souhait n'en crée aucune. Et la "
                      "version ferme n'est pas plus agressive que l'autre : elle est "
                      "plus précise. C'est la précision qui fait le travail, pas le "
                      "ton.",
            notes="Diapositive à photographier. Faire écrire la phrase telle quelle "
                  "dans le cahier, avec une vraie date.")

    d.tableau('Le plan', "Trois paragraphes, un par idée",
              ['Le paragraphe', 'Ce qu\'il contient'],
              [['premier', "l'opération, sa date, la date de l'appel"],
               ['deuxième', 'la carte en ma possession, le commerçant inconnu'],
               ['troisième', 'ce que je demande, et pour quand']],
              cle=0,
              note="Le lecteur pressé lit le premier et le dernier. Mettez-y l'essentiel.",
              notes="Diapositive à laisser affichée pendant l'écriture. Elle suffit : "
                    "aucun modèle de lettre n'est distribué, et c'est voulu.")

    d.pratique('Vérification', "Avant d'envoyer, relisez",
               "Cochez ce que votre lettre contient vraiment.", [
        ("Un objet court, avec le numéro de dossier et le montant.", "objet"),
        ("Trois paragraphes séparés, un par idée.", "plan"),
        ("La date de l'opération et celle de l'appel.", "faits"),
        ("Une phrase emphatique : « Ce que je conteste, c'est... »", "mise en relief"),
        ("Une demande au subjonctif : « je demande que... soit... »", "subjonctif"),
        ("Une date de réponse demandée, pas espérée.", "échéance"),
        ("Une salutation fermée, sans remerciement d'avance.", "salutation"),
    ], corrige=False,
       notes="Faire cocher avant de demander la correction par l'assistant. Ceux qui "
             "cochent tout obtiennent une rétroaction beaucoup plus courte.")

    d.piege('Le piège', "écrire pendant qu'on est fâché",
            "écrire, laisser dormir une nuit, relire",
            "La phrase qui soulage à l'écriture est presque toujours celle qui "
            "affaiblit à la lecture. Elle donne à l'autre quelque chose à quoi "
            "répondre, et ce n'est jamais votre demande.",
            notes="Vrai pour toutes les lettres formelles du programme, pas seulement "
                  "pour celle-ci. Le dire ainsi.")

    d.tableau('Bilan du module', "Ce que vous savez faire maintenant",
              ['Le bloc', 'Ce qui reste'],
              [['Je découvre', 'lire les quatre chiffres du relevé'],
               ['Défi 1', 'comparer trois façons d\'emprunter'],
               ['Défi 2', "distinguer un abri d'un placement"],
               ['Défi 3', 'contester une opération, et par écrit'],
               ['partout', "dire ce qu'on n'a pas compris"]],
              cle=0,
              notes="Diapositive de fermeture. La dernière ligne est celle que les "
                    "élèves emporteront le plus loin : la nommer en dernier.")

    d.billet("En deux phrases : qu'est-ce que tu feras autrement, la prochaine fois "
             "que tu iras à la caisse ?",
             exemples=["Je demanderai le taux et s'il est fixe.",
                       "Je ne signerai rien pendant le rendez-vous."],
             notes="Cinq minutes, et lire quelques billets à voix haute avant de "
                   "fermer le module. C'est la meilleure fin possible pour ce "
                   "contenu-là.")

    return d.save(dossier)
