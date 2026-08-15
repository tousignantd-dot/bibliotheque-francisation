# -*- coding: utf-8 -*-
"""A1 · Des lunettes de sécurité — mise en situation.
Bloc A « Je découvre » · couleur teal · 75 min.
Source du module : dialogue `prep`, exercice `pr1`, cartes mémoire.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='teal',
        titre='Des lunettes de sécurité',
        chapeau="Samuel a payé quarante dollars de sa poche pour des lunettes de "
                "sécurité. L'entreprise rembourse — mais seulement si on suit la "
                "procédure, et personne ne la lui a expliquée.",
        duree='75 minutes')

    d.titre(notes="Ouverture du module 4. Écrire au tableau : UNE PROCÉDURE. Demander qui "
                  "a déjà renoncé à une demande parce qu'il ne savait pas comment faire. "
                  "Beaucoup de mains se lèvent.")

    d.objectifs([
        "comprendre ce qu'est une procédure et pourquoi elle existe ;",
        "repérer les étapes d'une demande dans une explication orale ;",
        "savoir qui approuve et combien de temps ça prend ;",
        "nommer les documents à garder.",
    ])

    d.declencheur(
        'Mise en situation', "Vous avez payé du matériel de travail de votre poche. Que faites-vous ?",
        pistes=[
            "À qui demandez-vous si c'est remboursable ?",
            "Qu'est-ce que vous gardez, et pendant combien de temps ?",
            "Combien de temps attendriez-vous avant de relancer ?",
            "Et si personne ne vous répond ?",
        ],
        notes="Cinq minutes en grand groupe. Noter les réponses. Beaucoup diront « je ne "
              "demande pas » : c'est exactement ce que la séance vise à changer.")

    d.cartes('La situation', "Ce qu'on sait de Samuel", [
        ("Ce qu'il a acheté",
         "Des lunettes de sécurité pour son nouveau poste à l'entrepôt. Quarante "
         "dollars, payés de sa poche."),
        ("Ce qu'il ne sait pas",
         "Que l'entreprise rembourse ce genre de dépense, et qu'il existe une "
         "application pour le demander."),
        ("À qui il en parle",
         "À Diane, une collègue. Elle connaît la procédure et la lui explique en "
         "quatre étapes."),
        ("Ce qu'il doit retenir",
         "L'application s'appelle Ressources+. Le superviseur approuve. Environ dix "
         "jours. Et on garde le reçu original."),
    ], notes="La deuxième carte est le vrai sujet du module : une procédure qu'on ignore "
             "revient à une procédure qui n'existe pas.")

    d.dialogue('Dialogue · 1 de 3', "Est-ce que l'entreprise rembourse ?", [
        ("SAMUEL", "Diane, j'ai dû acheter des lunettes de sécurité pour mon nouveau "
                   "poste à l'entrepôt. Ça m'a coûté quarante dollars. Est-ce que "
                   "l'entreprise rembourse ce genre de dépense ?", True),
        ("DIANE", "Oui, bien sûr ! Il y a une procédure à suivre. Tu dois remplir une "
                  "demande de remboursement sur l'application de l'entreprise.", True),
        ("SAMUEL", "Ah bon ? Je ne savais pas qu'on avait une application pour ça.",
         False),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="Passer l'audio de « Je découvre ». Faire remarquer la question de Samuel : "
             "elle est directe, polie, et elle obtient une réponse en dix secondes.")

    d.dialogue('Dialogue · 2 de 3', "Elle s'appelle Ressources+", [
        ("DIANE", "Oui, elle s'appelle Ressources+. Tu prends une photo de ton reçu, tu "
                  "entres le montant, puis tu envoies ta demande.", True),
        ("SAMUEL", "D'accord. Est-ce qu'il faut l'approbation de quelqu'un avant ?",
         True),
        ("DIANE", "Oui, ton superviseur doit approuver la demande avant que les finances "
                  "la traitent.", True),
    ], notes="Trois étapes dans la première réplique : photo, montant, envoi. Les faire "
             "compter par le groupe et les écrire au tableau.")

    d.dialogue('Dialogue · 3 de 3', "Garde ton reçu original", [
        ("SAMUEL", "Combien de temps ça prend, habituellement ?", True),
        ("DIANE", "En général, une dizaine de jours. Garde ton reçu original, au cas où.",
         True),
    ], notes="La dernière phrase est un conseil, pas une étape : garder l'original même "
             "après avoir envoyé la photo. C'est ce que les gens oublient.")

    d.regle('La règle du module',
            "Une procédure a des étapes, un ordre, et quelqu'un qui approuve.",
            precision="Trois éléments à repérer dans toute explication : quelles étapes, "
                      "dans quel ordre, et qui doit donner son accord. Si l'un des trois "
                      "manque, la demande reste bloquée sans qu'on sache pourquoi.",
            notes="Écrire les trois au tableau — ÉTAPES · ORDRE · QUI APPROUVE — et les y "
                  "laisser pour tout le module.")

    d.tableau('Analyse', "La procédure de remboursement",
              ['Étape', 'Ce qu\'on fait'],
              [["1", "ouvrir Ressources+ et appuyer sur Nouvelle demande"],
               ["2", "prendre une photo claire du reçu original"],
               ["3", "inscrire le montant exact et choisir la catégorie"],
               ["4", "attendre l'approbation du superviseur"],
               ["5", "attendre le traitement par les finances, environ dix jours"]],
              cle=0, props=[0.12, 0.88],
              notes="Cinq étapes. Faire remarquer que les deux dernières ne demandent "
                    "rien : attendre fait partie de la procédure.")

    d.vocabulaire('Vocabulaire · 1 de 2', "La demande", [
        ("une procédure", "La façon officielle de faire une demande ou une tâche."),
        ("un remboursement", "L'argent qu'on redonne à quelqu'un pour une dépense."),
        ("un formulaire", "Un document à remplir avec des informations précises."),
        ("un reçu", "Le papier qui prouve un achat."),
        ("joindre", "Ajouter un document à un envoi."),
        ("approuver", "Donner son accord officiel à une demande."),
    ], notes="« Joindre » et « approuver » sont les deux verbes du module. Les faire "
             "employer dans une phrase par chaque élève.")

    d.vocabulaire('Vocabulaire · 2 de 2', "L'application et le travail", [
        ("un onglet", "Une section cliquable dans une application ou un site."),
        ("un jour ouvrable", "Un jour de la semaine où l'entreprise est ouverte."),
        ("un superviseur", "La personne responsable d'une équipe de travail."),
        ("une directive", "Une instruction précise à suivre."),
        ("un bris d'équipement", "Un équipement qui casse ou cesse de fonctionner."),
        ("un véhicule de service", "Un véhicule de l'entreprise, utilisé pour le travail."),
    ], notes="« Jour ouvrable » est le mot piège : dix jours ouvrables, ce sont deux "
             "semaines. Le calculer avec le groupe sur un calendrier.")

    d.pratique('Pratique', "Le dialogue, quatre questions",
               "Répondez sans relire.", [
        ("Pourquoi Samuel a-t-il dû acheter des lunettes de sécurité ?",
         "pour son nouveau poste à l'entrepôt"),
        ("Comment s'appelle l'application ?", "Ressources+"),
        ("Que doit-il faire avant d'entrer le montant ?", "prendre une photo de son reçu"),
        ("Qui doit approuver la demande ?", "son superviseur"),
        ("Combien de temps prend le remboursement ?", "environ dix jours"),
        ("Que doit-il garder, et pourquoi ?", "le reçu original, au cas où"),
    ], corrige=True,
       notes="La cinquième et la sixième sont celles qu'on oublie : le délai et le reçu "
             "original. Ce sont pourtant les deux qui causent le plus d'ennuis.")

    d.piege("Le piège du reçu jeté",
            "J'ai envoyé la photo, je peux jeter le reçu.",
            "Je garde l'original jusqu'à ce que l'argent soit versé.",
            "Une photo floue, un montant illisible, un doute des finances : dans tous ces "
            "cas, on redemande l'original. Sans lui, la demande est refusée et l'argent "
            "est perdu. Gardez le reçu jusqu'au versement.",
            notes="Conseil pratique concret. Suggérer une enveloppe ou une chemise pour "
                  "les reçus en attente de remboursement.")

    d.billet(
        "En cinq lignes : les étapes pour obtenir un remboursement.",
        exemples=[
            "Une ligne par étape, dans l'ordre.",
            "Ajoutez le délai et ce qu'il faut garder.",
        ],
        notes="Ramasser. Ces billets serviront en A4, où l'on expliquera la même "
              "procédure à un collègue.")

    return d.save(dossier)
