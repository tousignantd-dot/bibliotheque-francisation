# -*- coding: utf-8 -*-
"""E2 · La lettre, et le bilan du module.
Bloc E « Je me lance » · couleur framboise · 75 min. Production écrite et bilan.
Source : production écrite du module, révision des quatre blocs.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="La lettre, et le bilan du module",
        chapeau="Cinq lignes bien choisies valent trois pages. Puis on ferme "
                "le module en reprenant ce qu'on sait faire — et ce qu'on a "
                "le droit de demander.",
        duree='75 minutes')

    d.titre(notes="Dernière séance. Prévoir une bonne moitié du temps pour l'écriture et "
                  "la correction dans le module. Le bilan vient à la fin, quand les "
                  "lettres sont envoyées.")

    d.objectifs([
        "écrire une demande de réduction de loyer complète ;",
        "chiffrer sa demande et fixer un délai ;",
        "reprendre les points de langue des quatre blocs ;",
        "savoir ce qu'on a le droit de demander à un propriétaire.",
    ])

    d.regle("Une demande facile à traiter obtient une réponse",
            "Le destinataire doit pouvoir dire oui en trente secondes.",
            precision="Vous avez raison, et ça ne suffit pas. Ce qui décide, c'est la "
                      "facilité de traitement : des faits datés, un montant, une date "
                      "limite. Tout ce qui oblige le destinataire à chercher, à "
                      "reconstituer ou à se défendre travaille contre vous.",
            notes="Ouvrir la séance là-dessus. C'est l'idée qui organise toute la lettre "
                  "et qui vaut bien au-delà du logement.")

    d.tableau('La lettre · 1 de 2', "Ce qui s'est passé",
              ['La partie', 'La phrase modèle'],
              [["les faits, datés",
                "Le 10 novembre, un dégât d'eau est survenu dans ma chambre."],
               ["ce que j'ai perdu",
                "Les travaux ont duré trois jours, pendant lesquels je n'ai pas pu occuper ma chambre."]],
              cle=0,
              note="Deux phrases, pas trois.",
              notes="Faire remarquer la date en tête : c'est la première chose que "
                    "cherche celui qui lit.")

    d.tableau('La lettre · 2 de 2', "Ce que je demande",
              ['La partie', 'La phrase modèle'],
              [["la cause",
                "Étant donné que la cause était dans un autre logement, je ne suis pas responsable."],
               ["la demande",
                "Par conséquent, je demande une réduction de trois jours, soit 90 $."],
               ["le délai",
                "Je vous saurais gré de me répondre avant le 30 novembre."]],
              cle=0,
              note="Lues à la suite, les cinq font une lettre complète.",
              notes="Faire lire les cinq d'un trait par un élève. Entendre la lettre "
                    "entière en vingt secondes convainc mieux que n'importe quel "
                    "commentaire sur la concision.")

    d.cartes("Ce qu'il faut vérifier avant d'envoyer", "Quatre contrôles", [
        ("Une date dans la première phrase",
         "C'est la première chose que cherche celui qui lit."),
        ("Un chiffre dans la demande",
         "Loyer ÷ 30 × nombre de jours. Sans chiffre : « on verra »."),
        ("Une date limite de réponse",
         "Elle vous donne le droit de relancer sans avoir l'air pressant."),
        ("Aucune accusation",
         "« La cause se trouvait ailleurs », pas « vous avez négligé »."),
    ], notes="Les faire cocher un à un sur la lettre écrite dans le module, avant de "
             "demander la correction.")

    d.tableau('Les points de langue · 1 de 2', "Raconter et décrire",
              ['Le point', 'En une phrase'],
              [["le son o", "eau à la fin des mots longs, au devant d, t, s, o dans les mots courts"],
               ["imparfait / passé composé", "le décor dure, l'événement fait avancer"],
               ["le gérondif", "en + le radical de nous + -ant, même sujet pour les deux"]],
              cle=0,
              note="Les trois points des blocs A et B.",
              notes="Faire reformuler chaque ligne par un élève différent avant d'afficher "
                    "la colonne de droite.")

    d.tableau('Les points de langue · 2 de 2', "Lire un avis et demander",
              ['Le point', 'En une phrase'],
              [["les tournures d'avis", "un « il » qui ne désigne personne, un passif, « veuillez »"],
               ["le subjonctif", "après il faut que, il est nécessaire que, pour que, avant que"],
               ["l'emphase et les connecteurs", "c'est … qui, ce que …, c'est ; étant donné que, par conséquent"]],
              cle=0,
              note="Les trois points des blocs C et D.",
              notes="C'est la révision la plus efficace de la séance : reformuler avant "
                    "de lire.")

    d.vocabulaire('Bilan du vocabulaire', "Les mots à garder",
                  [("un cerne · gondoler · cloquer", "ce qu'on voit, avec le verbe juste"),
                   ("une fuite · une infiltration", "d'où ça vient, et par où ça passe"),
                   ("l'assèchement · un asséchateur", "ce qui répare, et ce qui fait du bruit"),
                   ("un avis · à défaut", "ce qu'on lit, et le mot qui vous engage"),
                   ("une réclamation · une franchise", "ce qu'on demande à son assureur"),
                   ("une réduction de loyer", "ce qu'on demande à son propriétaire")],
                  notes="Six lignes, dix-sept mots. Faire réviser les cartes mémoire dans "
                        "le module avant l'autoévaluation.")

    d.piege("Croire qu'on n'a rien à demander",
            "Il a fait réparer, c'est déjà ça.",
            "Le logement était inutilisable trois jours : je demande une réduction.",
            "C'est le fil de tout le module. Faire réparer est l'obligation du "
            "propriétaire, pas une faveur. Une pièce dont on ne peut pas se servir "
            "pendant trois jours est un loyer payé pour rien, et le demander n'est ni "
            "impoli ni exagéré : c'est une démarche ordinaire, prévue, que des milliers "
            "de locataires font chaque année.",
            notes="Fermer le module là-dessus. Pour beaucoup d'élèves, c'est le vrai "
                  "apprentissage — plus que la grammaire.")

    d.billet(
        "Gardez la fiche des cinq lignes d'une demande écrite.",
        exemples=[
            "Elle sert pour un logement, une école, une compagnie d'assurance.",
            "Les faits, la perte, la cause, la demande, le délai.",
        ],
        notes="Dernier billet du module. Faire l'autoévaluation dans le module interactif "
              "avant de partir : dix énoncés, trois choix.")

    return d.save(dossier)
