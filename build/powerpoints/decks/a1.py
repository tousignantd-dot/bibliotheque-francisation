# -*- coding: utf-8 -*-
"""A1 · Un problème dans mon logement — mise en situation.
Bloc A « Je découvre » · couleur teal · 75 min.
Source du module : dialogue `prep`, exercices `prVocab` et `pr1`, cartes mémoire.
"""
from theme import Deck

IMG = '/Users/danieltousignant/Claude/bibliotheque-francisation/assets/interactive/module-probleme/images/'


def build(dossier):
    d = Deck(
        code='A1', section='teal',
        titre='Un problème dans mon logement',
        chapeau="Oksana loue le 4B, au dernier étage d'un immeuble de six logements. "
                "Il fait quatorze degrés dans son salon et le calorifère reste froid. "
                "Que faire avant d'appeler la propriétaire ?",
        duree='75 minutes')

    d.titre(notes="Ouverture du module 9. Ne pas encore expliquer le vocabulaire : "
                  "la séance commence par une situation, pas par une liste de mots. "
                  "Écrire au tableau : 4B, dernier étage, six logements.")

    d.objectifs([
        "nommer un problème de mon logement avec le mot précis, pas avec « il y a un problème » ;",
        "dire depuis quand le problème dure ;",
        "savoir ce que je dois vérifier moi-même avant de téléphoner ;",
        "savoir ce que je dois noter pour garder une trace de ma demande.",
    ], notes="Lire chaque objectif à voix haute. Dire au groupe qu'on y reviendra à la fin, "
             "sur le billet de sortie.")

    d.declencheur(
        'Mise en situation', "Que voyez-vous ? Qu'est-ce que vous feriez ?",
        image=IMG + 'plafond.jpg',
        pistes=[
            "Qu'est-ce qu'il y a au plafond, exactement ?",
            "Est-ce que c'est grave ? Est-ce que ça peut attendre ?",
            "Qui faut-il appeler : le concierge ou la propriétaire ?",
            "Qu'est-ce que vous diriez au téléphone, en une phrase ?",
        ],
        notes="Cinq minutes de discussion libre, en grand groupe. Ne rien corriger encore. "
              "Noter au tableau les mots que le groupe utilise — on y reviendra à la diapo "
              "du vocabulaire pour comparer avec les mots justes.")

    d.cartes('La situation', "Ce qu'on sait d'Oksana", [
        ("Où elle habite",
         "Au 4B, le dernier étage d'un immeuble privé de six logements. La propriétaire "
         "s'appelle madame Rioux."),
        ("Ce qui ne va pas",
         "Il fait quatorze degrés dans le salon. Le calorifère est resté froid toute la nuit, "
         "même avec le thermostat à vingt-deux."),
        ("Qui elle appelle en premier",
         "Bertrand, un ami. Pas encore la propriétaire — elle veut d'abord comprendre ce qui "
         "se passe."),
        ("Ce qui l'arrête",
         "Elle n'aime pas déranger les gens. C'est une hésitation très courante, et c'est "
         "justement le sujet de la séance."),
    ], notes="Insister sur la quatrième carte : beaucoup d'élèves reconnaîtront cette "
             "hésitation. Demander : « qui a déjà attendu avant d'appeler son propriétaire ? »")

    # ── le dialogue, en trois temps ────────────────────────────────
    d.dialogue('Dialogue · 1 de 3', 'Il fait quatorze degrés au 4B', [
        ("OKSANA", "Bertrand, il fait quatorze degrés chez moi. Le calorifère du salon est resté froid toute la nuit.", False),
        ("BERTRAND", "Quatorze ? En novembre, c'est beaucoup trop bas. Est-ce que les autres pièces chauffent ?", False),
        ("OKSANA", "La cuisine et la chambre, oui. C'est seulement celui du salon qui ne réagit plus, même quand je monte le thermostat à vingt-deux.", True),
        ("BERTRAND", "Avant d'appeler ta propriétaire, descends au panneau électrique. Cherche un disjoncteur qui n'est pas dans le même sens que les autres.", True),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="Passer l'audio du module (section « Je découvre ») avant d'afficher le texte. "
             "Les deux répliques teintées portent l'essentiel : elle décrit précisément, "
             "il fait vérifier avant d'appeler.")

    d.dialogue('Dialogue · 2 de 3', 'Vérifier soi-même, d\'abord', [
        ("OKSANA", "Attends, je regarde… Oui, il y en a un qui est arrêté au milieu.", False),
        ("BERTRAND", "Pousse-le à fond vers « arrêt », puis ramène-le vers « marche ». S'il retombe tout de suite, ne le touche plus.", True),
        ("OKSANA", "Il vient de retomber. Deux fois.", False),
        ("BERTRAND", "Alors ce n'est pas le thermostat, c'est le circuit. Tu appelles madame Rioux aujourd'hui, pas la semaine prochaine.", True),
    ], notes="Vocabulaire à expliquer ici : le panneau électrique, le disjoncteur, "
             "« arrêté au milieu ». Faire mimer le geste avec la main.")

    d.dialogue('Dialogue · 3 de 3', "Ce n'est pas déranger", [
        ("OKSANA", "Je n'aime pas déranger les gens pour ça.", False),
        ("BERTRAND", "Tu ne déranges personne : le chauffage fait partie du logement que tu paies. Prends une photo de ton thermomètre avec la date, et note l'heure de ton appel.", True),
        ("OKSANA", "Pourquoi noter tout ça ?", False),
        ("BERTRAND", "Parce que si elle tarde, tes notes deviennent ta preuve. Et ne t'en fais pas : dans neuf cas sur dix, ça se règle en un coup de fil.", True),
    ], notes="C'est le cœur de la séance. Faire reformuler la phrase de Bertrand par un élève, "
             "dans ses mots : le chauffage fait partie de ce qu'on paie.")

    # ── vocabulaire ────────────────────────────────────────────────
    d.vocabulaire('Vocabulaire · 1 de 3', "Le logement et ses appareils", [
        ("un calorifère", "L'appareil fixé au mur qui chauffe une pièce."),
        ("un disjoncteur", "L'interrupteur du panneau électrique qui coupe le courant en cas de danger."),
        ("un chauffage d'appoint", "Un petit appareil de chauffage qu'on ajoute temporairement."),
        ("le bail", "Le contrat signé entre le locataire et le propriétaire."),
        ("une partie commune", "Un espace de l'immeuble partagé par tous les locataires."),
    ], notes="Faire répéter chaque mot avec son article : « un calorifère », jamais « calorifère ». "
             "L'article fait partie du mot.")

    d.vocabulaire('Vocabulaire · 2 de 3', "Ce qui abîme un logement", [
        ("une infiltration", "De l'eau qui entre par le toit ou par un mur."),
        ("la moisissure", "Des taches noires ou vertes causées par l'humidité."),
        ("l'insalubrité", "L'état d'un logement malpropre ou dangereux pour la santé."),
        ("l'ampleur", "La grandeur, l'importance d'un problème."),
        ("encombrer", "Occuper une place et gêner le passage."),
    ], notes="« Infiltration » et « moisissure » reviendront à toutes les séances du bloc B. "
             "Les écrire au tableau et les y laisser.")

    d.vocabulaire('Vocabulaire · 3 de 3', "Demander, et garder une trace", [
        ("se plaindre", "Dire qu'on n'accepte plus une situation et demander qu'elle change."),
        ("un avis écrit", "Une lettre ou un courriel qui garde une trace d'une demande."),
        ("un recours", "Le moyen légal de faire régler un problème qui traîne."),
        ("une sortie de secours", "Le chemin à garder libre pour évacuer en cas d'incendie."),
        ("un couvreur", "La personne qui répare les toitures."),
    ], notes="« Se plaindre » sera repris au complet à la séance D2. Ici, on installe seulement "
             "le mot.")

    # ── la règle de la séance ──────────────────────────────────────
    d.regle('Ce qu\'il faut retenir',
            "Un problème nommé précisément se règle deux fois plus vite qu'un problème décrit vaguement.",
            precision="« Il y a un problème dans mon salon » peut vouloir dire dix choses. "
                      "« Le calorifère du salon ne chauffe plus depuis avant-hier, il fait quatorze degrés » "
                      "dit tout en une phrase : l'appareil, la pièce, depuis quand, et à quel point c'est grave.",
            notes="Faire répéter la phrase de la carte blanche par deux élèves différents. "
                  "C'est la diapo à photographier.")

    d.piege('Nommer le problème',
            "Bonjour, il y a un problème chez moi.",
            "Le calorifère du salon ne chauffe plus depuis avant-hier.",
            "Les deux phrases sont grammaticalement correctes. Seule la deuxième permet à la "
            "propriétaire de savoir qui appeler et à quel point c'est urgent. Une phrase précise "
            "n'est pas une phrase impolie : c'est une phrase utile.",
            notes="Ne pas présenter la colonne de gauche comme une faute de langue — c'est une "
                  "phrase juste, mais inefficace. La nuance compte pour des adultes.")

    d.cartes('Avant de téléphoner', "Les quatre choses à faire", [
        ("1 · Je vérifie ce que je peux vérifier",
         "Le panneau électrique, le thermostat, le robinet d'arrêt. Sans jamais toucher à ce "
         "qui est dangereux : un disjoncteur qui retombe deux fois, on n'y touche plus."),
        ("2 · Je mesure",
         "Le nombre de degrés, la grandeur de la tache, le nombre de jours. Un chiffre vaut "
         "dix adjectifs."),
        ("3 · Je photographie",
         "Le thermomètre, la tache, le dégât — avec la date visible. La photo montre l'ampleur "
         "mieux qu'une description."),
        ("4 · Je note",
         "La date et l'heure de mon appel, le nom de la personne à qui j'ai parlé, ce qui a été "
         "promis. Si la réparation tarde, ces notes deviennent ma preuve."),
    ], notes="Faire copier ces quatre points dans le cahier. C'est la seule chose de la séance "
             "que les élèves doivent avoir par écrit chez eux.")

    # ── pratique guidée ────────────────────────────────────────────
    d.pratique('Pratique', 'Vrai ou faux',
               "Écoutez de nouveau le dialogue, puis répondez.", [
        ("Toutes les pièces du logement sont froides.", "FAUX — seul le salon."),
        ("Oksana a monté son thermostat jusqu'à vingt-deux degrés.", "VRAI"),
        ("Bertrand lui conseille d'appeler la propriétaire avant de vérifier quoi que ce soit.", "FAUX — il fait vérifier d'abord."),
        ("Le disjoncteur est retombé deux fois.", "VRAI"),
        ("Bertrand pense que le problème vient du thermostat.", "FAUX — du circuit."),
        ("Il lui conseille de photographier son thermomètre avec la date.", "VRAI"),
    ], corrige=True, notes="Faire répondre à main levée avant d'afficher la correction. "
                           "Redemander l'audio si le groupe hésite sur trois énoncés ou plus.")

    d.pratique('Pratique', 'Le mot juste',
               "Quel mot du vocabulaire correspond à chaque définition ?", [
        ("De l'eau qui entre par le toit ou par un mur.", "une infiltration"),
        ("L'interrupteur qui coupe le courant en cas de danger.", "un disjoncteur"),
        ("La grandeur, l'importance d'un problème.", "l'ampleur"),
        ("Un espace partagé par tous les locataires.", "une partie commune"),
        ("Le contrat signé entre le locataire et le propriétaire.", "le bail"),
        ("La personne qui répare les toitures.", "un couvreur"),
    ], corrige=True, notes="Exiger l'article dans la réponse. « Infiltration » seul ne compte pas.")

    d.billet(
        "Décrivez un problème de votre logement en une seule phrase précise.",
        exemples=[
            "Utilisez : le nom de l'appareil ou de la pièce · ce qui ne fonctionne pas · depuis quand.",
            "Exemple : « Le robinet de la cuisine goutte depuis trois jours. »",
        ],
        notes="Deux minutes. Ramasser les billets : ils servent de point de départ à la séance A4, "
              "où on classera ces problèmes par type et par urgence.")

    return d.save(dossier)
