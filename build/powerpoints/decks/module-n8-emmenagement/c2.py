# -*- coding: utf-8 -*-
"""C2 · Lire une lettre de décision
Bloc C « Défi 2 · Faire valoir sa réclamation » · couleur teal · 75 min.
Écoute et réponds. Source du module : l'exercice `t2refus` (type texte).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='teal',
        titre="Lire une lettre de décision",
        chapeau="Cinq blocs, toujours les mêmes, dans toutes les compagnies. "
                "Une lettre à laquelle il en manque un est incomplète — et "
                "vous pouvez le dire.",
        duree='75 minutes')

    d.titre(notes="Séance de compréhension écrite. La situation du programme "
                  "n'a que des intentions orales : cette lecture vient des "
                  "attentes de fin de cours du niveau 8, qui demandent de "
                  "résumer les propos de son interlocuteur et de négocier la "
                  "solution d'un problème.")

    d.objectifs([
        "retrouver les cinq blocs d'une lettre de décision ;",
        "recalculer soi-même le montant réellement versé ;",
        "repérer les passifs qui cachent leur auteur ;",
        "noter le délai de contestation le jour de la réception.",
    ], notes="Le deuxième objectif est celui qui évite la plus grande "
             "déception : le chiffre du corps de la lettre est presque "
             "toujours avant franchise.")

    d.declencheur(
        'Pour commencer', "Une lettre annonce « le dommage retenu s'établit à "
                          "940 $ ». Combien recevez-vous ?",
        pistes=[
            "Où trouve-t-on la franchise dans une lettre ?",
            "Pourquoi les deux chiffres ne sont-ils jamais côte à côte ?",
            "Que veut dire « retenu » ?",
        ],
        notes="« Retenu » est le mot à faire chercher : il annonce toujours "
              "un montant avant franchise. Une fois repéré, il ne s'oublie "
              "plus.")

    d.tableau('Analyse', "Les cinq blocs d'une lettre de décision",
              ['Le bloc', 'Ce qu\'on y cherche'],
              [["L'objet", "le numéro de dossier, à reprendre dans tous vos courriels"],
               ["Le rappel des faits", "ce que l'assureur a compris de votre déclaration"],
               ["Ce qui est accepté", "le dommage retenu, puis la franchise, ailleurs"],
               ["Ce qui est refusé", "le motif, et surtout la clause citée entre guillemets"],
               ["Le recours", "le délai, la forme, et l'organisme après l'assureur"]],
              cle=0,
              note="Cherchez ces cinq blocs à la première lecture. Un manquant se signale.",
              notes="Diapositive à photographier. Une décision qui ne cite "
                    "aucune clause ne se défend pas devant un réviseur, et "
                    "elle se retire souvent dès qu'on la demande.")

    d.cartes('Analyse', "Cinq formules, et ce qu'elles annoncent", [
        ("« le dommage retenu s'établit à… »", "un montant avant franchise, à recalculer soi-même."),
        ("« il a été établi que… »", "personne n'est nommé : demandez par qui, et sur quelle pièce."),
        ("« la clause X se lit comme suit »", "le point d'appui du refus — donc de votre contestation."),
        ("« la responsabilité est régie par… »", "on vous renvoie à un autre contrat, souvent celui d'un tiers."),
    ], cols=2,
       notes="Les quatre sont dans la lettre du module. Faire retrouver "
             "chacune dans le texte de l'exercice `t2refus` avant de "
             "commenter.")

    d.regle("La clause citée est votre point d'appui",
            "Elle est reproduite entre guillemets parce que l'assureur y est tenu : c'est le seul endroit de la lettre où l'on vous donne un texte plutôt qu'un jugement.",
            precision="Un mot du contrat qui ne recouvre pas exactement votre "
                      "situation est une brèche. « Pendant leur transport » "
                      "ne veut pas dire « pendant le service ».",
            notes="Diapositive à photographier. Faire relire la clause 7.3 "
                  "lentement, mot par mot, à voix haute. C'est en la lisant "
                  "ainsi qu'on trouve la distinction, pas en la survolant.")

    d.piege('Attention',
            "lire « refusé » et ranger la lettre",
            "lire jusqu'au paragraphe de la révision",
            "Toute lettre de décision contient une voie de recours et un "
            "délai — souvent soixante jours. Beaucoup de dossiers se ferment "
            "simplement parce que personne n'a lu ce paragraphe-là. Notez la "
            "date le jour de la réception, et envoyez une semaine d'avance : "
            "une pièce manquante ne se remplace pas en vingt-quatre heures.",
            notes="Faire calculer la date limite à partir d'une date de "
                  "réception donnée. L'exercice paraît trivial et il ne "
                  "l'est pas.")

    d.pratique('Pratique', "Où trouve-t-on cela dans la lettre ?",
               "Reliez chaque question au bloc qui y répond.", [
        ("Quel est le numéro du dossier ?", "l'objet"),
        ("À combien le dommage accepté est-il établi ?", "premier élément — accepté"),
        ("Quelle somme sera réellement versée ?", "la ligne de la franchise"),
        ("Quels sont les mots exacts de la clause invoquée ?", "troisième élément — refusé"),
        ("Dans quel délai peut-on demander une révision ?", "le paragraphe du recours"),
        ("À quel organisme s'adresser s'il n'y a pas d'entente ?", "la fin du paragraphe du recours"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t2refus` du module, dans sa version projetée. "
             "Le module fait cliquer dans le texte ; ici, on fait nommer le "
             "bloc. La compétence est la même.")

    d.billet(
        "Réécris « il a été établi que l'entreprise avait la garde du bien » en nommant qui a établi.",
        exemples=[
            "Une seule phrase, à la voix active.",
            "Puis écris la question que tu poserais à l'experte.",
        ],
        notes="Cinq minutes. Le lien avec la séance A4 est direct : le passif "
              "cache l'auteur, et la question « par qui ? » est celle qui "
              "débloque le dossier.")

    return d.save(dossier)
