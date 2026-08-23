# -*- coding: utf-8 -*-
"""E2 · Écris ta mise en demeure
Bloc E « Je me lance » · couleur framboise · production écrite et bilan ·
75 min.
Source : bloc `appli` de `custom.js` — production écrite et ses neuf
exigences —, banc FC_CARDS, autoévaluation en seize énoncés.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Écris ta mise en demeure",
        chapeau="Dernière séance : douze à seize phrases, en cinq "
                "paragraphes courts. Les faits, le droit, la demande, le "
                "délai, les pièces.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Rendre les billets de D2 : la demande et "
                  "le délai y sont déjà écrits. Prévoir quarante minutes d'écriture "
                  "réelle et garder le bilan pour la fin.")

    d.objectifs([
        "rédiger une lettre formelle de douze à seize phrases ;",
        "découper le texte en cinq paragraphes, un par fonction ;",
        "employer deux connecteurs en tête de paragraphe et un subjonctif ;",
        "évaluer ce qu'on est maintenant capable de faire.",
    ], notes="C'est l'intention de production écrite de la situation, telle que le "
             "programme la nomme : rédiger une lettre de réclamation. Aucun détour par "
             "les attentes de fin de cours n'est nécessaire ici.")

    d.declencheur(
        'Mise en situation', "Pourquoi écrire, puisqu'on s'est déjà déplacé au comptoir ?",
        pistes=[
            "Que reste-t-il d'une conversation, trois semaines plus tard ?",
            "Qui lira la lettre, et que fera-t-il de plus que la personne au comptoir ?",
            "Qu'est-ce qui commence le jour où la lettre arrive ?",
            "Que faut-il garder, une fois la lettre partie ?",
        ],
        notes="La troisième question est la bonne : un délai commence. C'est ce qui "
              "distingue une mise en demeure d'une lettre de plainte, et c'est ce qui "
              "la rend efficace.")

    d.tableau('Analyse', "Cinq paragraphes, cinq travaux",
              ['Le paragraphe', 'Ce qu\'on y met'],
              [["1 · L'achat", "la date, le bien, le prix"],
               ["2 · La panne", "la chronologie, une date par phrase"],
               ["3 · Le droit", "la garantie, et la preuve qu'on était dedans"],
               ["4 · La demande", "une seule, avec « à vos frais »"],
               ["5 · Le délai", "dix jours, et la suite annoncée"],
               ["Les pièces", "énumérées à la fin, sans commentaire"]],
              cle=0,
              notes="Diapositive à photographier, et à laisser affichée pendant "
                    "l'écriture. Elle remplace toute autre consigne, et l'objet se "
                    "rédige en dernier.")

    d.cartes('Production écrite', "Quatre phrases outils du module", [
        ("Le connecteur d'ajout", "« Je vous rappelle en outre que la garantie légale s'applique. »"),
        ("Le connecteur de conclusion", "« En conséquence, je vous demande de procéder, à vos frais, à… »"),
        ("Le délai", "« Vous disposez d'un délai de dix jours à compter de la réception de la présente. »"),
        ("La suite annoncée", "« À défaut, je m'adresserai à la Division des petites créances. »"),
    ], notes="Ce sont des modèles de forme, pas de contenu : chacun écrit les siennes "
             "avec ses propres dates. Le dire explicitement, sinon quinze lettres "
             "identiques arrivent à la correction.")

    d.regle("Écrivez ce qui s'est passé, pas ce que vous ressentez",
            "Une lettre qui donne des dates, un montant et un délai obtient une réparation.",
            precision="« J'ai été très déçue » devient « le véhicule a servi "
                      "vingt-quatre jours ». Le second dit la même chose et se prouve. "
                      "Et « vous le regretterez » devient « je m'adresserai aux petites "
                      "créances » : un fait annoncé au futur pèse plus qu'une menace, "
                      "et il ne peut pas se retourner contre son auteur.",
            notes="Diapositive à photographier. C'est le critère principal de la "
                  "correction : on évalue ce que la lettre demande et ce qu'elle "
                  "prouve, pas ce qu'elle ressent.")

    d.piege('Piège', "glisser une deuxième demande",
            "garder l'autre pour la lettre suivante",
            "Réparation et remboursement de la garantie prolongée sont deux dossiers. "
            "Ensemble dans la même lettre, ils se négocient l'un contre l'autre, et le "
            "commerçant accordera le moins cher des deux. Une demande, une lettre.",
            notes="Repasser dans les rangs à mi-parcours en ne cherchant que cela : "
                  "c'est l'erreur la plus fréquente, et elle se corrige en biffant deux "
                  "lignes.")

    d.pratique('Vocabulaire', "Les seize mots du module, un dernier tour",
               "Donnez la définition de mémoire, puis vérifiez avec les cartes.", [
        ("une auto d'occasion · l'odomètre", "le bien, et le chiffre du compteur"),
        ("les frais de crédit · l'obligation totale", "ce que le crédit coûte, et le vrai total"),
        ("la transmission · un cognement", "la pièce, et le bruit qu'elle fait"),
        ("un diagnostic · un témoin lumineux", "ce que le garage établit, et ce qui s'allume"),
        ("la garantie légale · l'usure normale", "ce que la loi donne, et ce qu'on vous répond"),
        ("une mise en demeure · un délai raisonnable", "la lettre, et le temps qu'elle accorde"),
    ], corrige=True,
       notes="Par paires, cinq minutes. Les seize mots regroupés deux à deux par le "
             "lien qui les unit : c'est ainsi qu'ils se retiennent, et c'est ainsi "
             "qu'ils reviennent dans les cartes mémoire.")

    d.billet(
        "Qu'est-ce que tu es capable de faire aujourd'hui, que tu ne faisais pas avant ce module ?",
        exemples=[
            "Une phrase, sur un achat ou ailleurs.",
            "L'autoévaluation en seize énoncés est dans le module.",
        ],
        notes="Cinq minutes, à la toute fin. Faire lire trois billets à voix haute. "
              "Rappeler que l'autoévaluation reste ouverte à la maison, et que "
              "l'étiquette d'une auto d'occasion se demande avant de signer.")

    return d.save(dossier)
