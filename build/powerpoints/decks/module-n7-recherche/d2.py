# -*- coding: utf-8 -*-
"""D2 · Mettre en avant, et demander poliment
Bloc D « Défi 3 » · couleur ambre · écriture · 75 min.
Source : exercices `t3cliv`, `t3cond`, `t3subj` et `t3cv`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Mettre en avant, et demander poliment",
        chapeau="Le français n'insiste pas avec la voix : il déplace. Et "
                "dans une lettre d'affaires, l'indicatif brut ne passe pas "
                "pour direct — il passe pour brusque.",
        duree='75 minutes')

    d.titre(notes="Séance la plus chargée du module : trois points de grammaire et "
                  "la mise en page. Ne pas tout traiter avec la même profondeur — "
                  "le clivage et le conditionnel d'abord, le subjonctif ensuite.")

    d.objectifs([
        "mettre un élément en avant avec « c'est… qui » et « c'est… que » ;",
        "employer le conditionnel de politesse dans une lettre ;",
        "employer le subjonctif après « pour que » et « avant que » ;",
        "ranger les sept rubriques d'un curriculum vitæ.",
    ], notes="Le troisième objectif se limite à deux conjonctions : ne pas ouvrir le "
             "subjonctif en général, le module n'en a pas le temps et n'en a pas "
             "besoin.")

    d.declencheur(
        'Observation', "Comment insiste-t-on, en français ?",
        pistes=[
            "« La rigueur a fait mon métier. »",
            "« C'est la rigueur qui a fait mon métier. »",
            "« Ce que j'apporte, c'est neuf ans de contrôle. »",
            "Laquelle des trois lit-on le plus vite ? Laquelle retient-on ?",
        ],
        notes="Écrire les trois au tableau. Un élève qui traduit mot à mot de "
              "l'anglais produit la première et se demande pourquoi elle sonne "
              "plate : il lui manque le déplacement.")

    d.regle("« qui » si l'élément fait l'action, « que » sinon",
            "C'est la rigueur qui a fait mon métier. C'est le contrôle de "
            "la qualité que je vise.",
            precision="Même règle que dans les subordonnées relatives : une seule à "
                      "retenir pour deux emplois. Et pour le pseudoclivage — « ce "
                      "que j'apporte, c'est… » —, la virgule n'est pas décorative : "
                      "elle marque la pause avant la révélation, et c'est elle qui "
                      "fait l'effet.",
            notes="Diapositive à photographier. Doser : une mise en avant par "
                  "paragraphe, pas davantage. Trois de suite sonnent comme une "
                  "publicité.")

    d.cartes('Analyse', "La phrase à plat, la phrase mise en avant", [
        ("La rigueur a fait mon métier.", "C'est la rigueur qui a fait mon métier."),
        ("J'ai appris ce métier à Alger.", "C'est à Alger que j'ai appris ce métier."),
        ("Je vise le contrôle de la qualité.", "Ce que je vise, c'est le contrôle de la qualité."),
        ("Votre travail m'intéresse.", "Ce qui m'intéresse, c'est votre travail."),
        ("J'apporte neuf ans d'expérience.", "Ce que j'apporte, c'est neuf ans d'expérience."),
        ("Mes neuf années comptent le plus.", "Ce sont mes neuf années qui comptent le plus."),
    ], cols=1,
       notes="Exercice `t3cliv` du module interactif. Faire lire les deux colonnes à "
             "voix haute, avec la pause de la virgule : la différence s'entend.")

    d.regle("Le conditionnel de politesse fait lire votre lettre",
            "« Je veux ce poste » se fait écarter. « Je souhaiterais poser "
            "ma candidature » se fait lire.",
            precision="Radical du futur, terminaisons de l'imparfait. Six verbes "
                      "suffisent : j'aimerais, je souhaiterais, je voudrais, "
                      "pourriez-vous, auriez-vous, je serais. Et jamais de "
                      "conditionnel après « si » d'hypothèse : si j'étais retenue, "
                      "je serais disponible.",
            notes="Diapositive à photographier. Anticiper l'objection : le "
                  "conditionnel n'affaiblit pas la demande, c'est l'indicatif brut "
                  "qui dessert.")

    d.tableau('Analyse', "Un sujet ou deux ?",
              ['Le cas', 'Ce qu\'on écrit'],
              [["Le but, un seul sujet", "Je téléphone pour obtenir des précisions."],
               ["Le but, deux sujets", "Je téléphone pour que vous ayez mon nom en tête."],
               ["Le temps, un seul sujet", "Je vous appelle avant d'envoyer mon dossier."],
               ["Le temps, deux sujets", "Je vous appelle avant que le poste soit comblé."]],
              cle=0,
              note="Après « pour que » et « avant que », le subjonctif est obligatoire. Après « après que », c'est l'indicatif.",
              notes="Diapositive à photographier. Les quatre irréguliers à savoir : "
                    "que vous ayez, soyez, fassiez, puissiez.")

    d.pratique('Grammaire', "Le ton d'une lettre",
               "Mettez le verbe au conditionnel, ou au subjonctif.", [
        ("Je ___ poser ma candidature au poste. (souhaiter)", "souhaiterais"),
        ("J'___ vous rencontrer pour vous en dire davantage. (aimer)", "aimerais"),
        ("___ -vous me préciser la date d'entrée en fonction ? (pouvoir)", "Pourriez"),
        ("Je ___ disponible dès janvier. (être)", "serais"),
        ("Je vous écris pour que vous ___ mon dossier avant la fin du mois. (avoir)", "ayez"),
        ("Je téléphone avant que le poste ne ___ comblé. (être)", "soit"),
        ("J'ai joint mes attestations pour que vous ___ vérifier. (pouvoir)", "puissiez"),
        ("Si j'étais retenue, je ___ m'installer avant janvier. (pouvoir)", "pourrais"),
    ], corrige=True,
       notes="Exercices `t3cond` et `t3subj` du module interactif. Le dernier est le "
             "piège du « si » : imparfait d'un côté, conditionnel de l'autre.")

    # Le titre annonçait sept rubriques pour six rangées, et six rangées **plus**
    # une note ne tiennent pas sur une diapositive projetée : le garde-fou de
    # `theme.py` refuse. Le compte est corrigé, les cellules raccourcies, et la
    # note descendue dans les notes de l'enseignante.
    d.tableau('Analyse', "Les six rubriques, dans l'ordre",
              ['Rubrique', 'Ce qu\'on y met'],
              [["En-tête", "nom, téléphone, courriel, ville"],
               ["Titre", "le titre exact du poste, mot pour mot"],
               ["Expérience pertinente", "les emplois liés au poste, trois tâches"],
               ["Autre expérience", "les autres, une ligne et les dates"],
               ["Formation", "les diplômes, du plus récent au plus ancien"],
               ["Références", "« fournies sur demande »"]],
              cle=0,
              notes="Exercice `t3cv` du module interactif. Insister sur le nom du "
                    "fichier : nom-prenom-titre.pdf, jamais cv-final-2.pdf. Et "
                    "dire la règle qui ne tient pas sur la diapositive : ni "
                    "photo, ni date de naissance, ni état civil — une ou deux "
                    "pages, jamais trois.")

    d.billet(
        "Écrivez la première ligne et le premier paragraphe de votre lettre.",
        exemples=[
            "Le titre exact du poste dans l'objet.",
            "Un conditionnel de politesse dans la première phrase.",
        ],
        notes="Premier brouillon de la production écrite du bloc E. Ramasser, "
              "annoter, redistribuer en E2.")

    return d.save(dossier)
