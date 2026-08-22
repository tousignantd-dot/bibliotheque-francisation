# -*- coding: utf-8 -*-
"""A4 · Quatre papiers qu'on confond tout le temps
Bloc A « Je découvre » · couleur ambre · 75 min. Écriture.
Source du module : exercice `prMot` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Quatre papiers qu'on confond tout le temps",
        chapeau="L'avis vient du centre vers vous. Le formulaire va de vous "
                "vers le centre. L'attestation prouve où vous êtes "
                "aujourd'hui, le relevé prouve ce que vous avez réussi "
                "hier. Se tromper de nom, c'est repartir sans ce qu'on "
                "était venu chercher.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. Elle transforme le vocabulaire de A3 en "
                  "gestes : quel papier pour quelle situation, et qui peut l'imprimer. "
                  "Terminer par la première phrase écrite du module.")

    d.objectifs([
        "distinguer les quatre documents par leur sens de circulation ;",
        "savoir lequel s'imprime au comptoir et lequel vient du ministère ;",
        "demander le bon document avec la bonne phrase ;",
        "écrire une première phrase de comptoir, complète et vouvoyée.",
    ], notes="Le troisième objectif est le pont entre le bloc A et le bloc B. Le "
             "quatrième prépare la production écrite de E2 : on commence à écrire dès "
             "la quatrième séance, pas à la quatorzième.")

    d.tableau('Le sens de circulation', "Qui écrit à qui",
              ['Du centre vers vous', 'De vous vers le centre'],
              [["Un avis", "Un formulaire"],
               ["Il annonce une décision prise", "Il fait entrer une demande"],
               ["Il porte des dates et une échéance", "Il porte des cases à remplir"],
               ["On le signe et on le rapporte", "On le signe et on le remet"]],
              cle=1,
              notes="Faire compléter la colonne de droite avant de l'afficher. Le "
                    "tableau tient tout le bloc C d'avance : un avis s'annonce, il ne "
                    "se discute pas.")

    d.tableau('Deux preuves, deux moments', "Ce qu'on est, ce qu'on a réussi",
              ['Une attestation', 'Un relevé'],
              [["Vous êtes inscrit ici, en ce moment", "Vous avez réussi tel cours"],
               ["Le secrétariat l'imprime sur-le-champ", "Le ministère l'envoie"],
               ["Pour un employeur, un propriétaire", "Pour une équivalence, un dossier"],
               ["Disponible aujourd'hui", "Après la fin du cours"]],
              cle=1,
              notes="C'est la confusion la plus fréquente du module. La question qui "
                    "départage est celle de madame Paradis : « C'est pour prouver que "
                    "vous êtes inscrite, ou pour prouver ce que vous avez réussi ? »")

    d.regle("Une conversation ne laisse aucune trace",
            "Le formulaire, lui, en laisse une, datée.",
            precision="C'est pour ça qu'on vous le fait remplir même quand vous "
                      "venez de tout expliquer de vive voix.",
            notes="Diapositive à photographier. Elle revient en D2 et en E2. Beaucoup "
                  "d'élèves vivent le formulaire comme une méfiance à leur égard : "
                  "expliquer que c'est ce qui les protège, eux, quand deux versions "
                  "ne concordent pas.")

    d.cartes("La phrase qui demande le bon papier", "Quatre demandes, quatre formules", [
        ("L'avis",
         "J'ai reçu un avis et je viens le rapporter signé."),
        ("Le formulaire",
         "Je viens vous remettre mon formulaire d'absence signé."),
        ("L'attestation",
         "Je voudrais une attestation de fréquentation, s'il vous plaît."),
        ("Le relevé",
         "Est-ce que mon relevé des apprentissages est déjà parti ?"),
    ], notes="Faire répéter les quatre à voix haute, debout. Elles sont courtes exprès : "
             "au comptoir, on a environ deux minutes et la première phrase décide de "
             "tout le reste.")

    d.piege("Répondre à un avis par un courriel d'explication",
            "Bonjour, je voulais expliquer pourquoi je n'ai pas pu venir.",
            "Je signe l'avis, je le rapporte, et je demande un rendez-vous.",
            "Un avis annonce une décision déjà prise. Un courriel d'explication "
            "n'ouvre aucun dossier et n'arrête aucune échéance. Si la décision pose "
            "un problème, c'est un rendez-vous qu'il faut, pas une lettre.",
            notes="Beaucoup d'élèves écrivent ce courriel-là, croyant bien faire, et "
                  "attendent ensuite une réponse qui ne vient pas. Le dire clairement.")

    d.pratique('Compréhension', "Quel papier, dans quelle situation ?",
               "Répondez oralement, puis justifiez.", [
        ("Votre employeur veut une preuve que vous étudiez ici.", "une attestation"),
        ("Vous voulez annoncer une absence de trois semaines.", "un formulaire"),
        ("Le centre vous confirme les dates de votre absence.", "un avis"),
        ("Vous demandez une équivalence dans un autre programme.", "un relevé"),
        ("Vous revenez de l'étranger avec un billet d'hôpital.",
         "une pièce justificative"),
        ("Vous voulez changer de groupe.", "un formulaire, puis une demande écrite"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par le sens de circulation. La dernière a "
             "deux réponses : c'est voulu, et elle annonce le bloc D.")

    d.pratique('Écriture', "Votre première phrase de comptoir",
               "Écrivez-la, puis lisez-la à voix haute à votre voisin.", [
        ("Le bonjour, votre nom complet, votre groupe.", "une seule phrase"),
        ("Ce que vous venez faire, au présent.", "sans dates ni raison encore"),
        ("Le document que vous demandez, avec son article.", "le bon mot, pas « papier »"),
        ("Un remerciement pour terminer.", "deux mots suffisent"),
    ], corrige=False,
       notes="Passer dans les rangées. Deux erreurs reviennent : on oublie le groupe, et "
             "on commence par la raison. Corriger sur place, à voix basse, sans reprendre "
             "le groupe entier.")

    d.billet(
        "Écrivez la phrase que vous direz en arrivant au comptoir, en entier.",
        exemples=[
            "Nom complet, groupe, et ce que vous venez faire.",
            "Vouvoyez. Relisez-la à voix haute avant de la remettre.",
        ],
        notes="Ramasser les billets et les garder : ils reviennent en B1, où la même "
              "phrase servira d'ouverture au dialogue du comptoir.")

    return d.save(dossier)
