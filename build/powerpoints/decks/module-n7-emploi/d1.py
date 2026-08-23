# -*- coding: utf-8 -*-
"""D1 · La note de service
Bloc D « Défi 3 · Les deux écrits » · couleur ambre · 75 min.
Source du module : exercices `t3note` (type texte), `t3genres` et `t3ponct`.
"""
import pathlib

from theme import Deck

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-emploi' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='D1', section='ambre',
        titre="La note de service",
        chapeau="Le plus court des écrits de travail, et le plus lu. Elle "
                "circule à l'intérieur de l'entreprise, entre des gens qui se "
                "connaissent. Elle ne fait pas de phrases : elle informe, elle "
                "demande, elle date.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 3. Ce que le groupe a présenté à l'oral doit "
                  "maintenant s'écrire, et pas de la même façon selon à qui l'on "
                  "écrit. Aujourd'hui : la note interne. Demain : la lettre qui sort "
                  "de l'entreprise.")

    d.objectifs([
        "nommer les six parties d'une note de service ;",
        "écrire un objet sans verbe conjugué ;",
        "distinguer ce qui appartient à la note et ce qui appartient à la lettre ;",
        "respecter la ponctuation et la mise en page des écrits de travail.",
    ], notes="Le troisième objectif est celui qui produit les erreurs les plus "
             "visibles : un « veuillez agréer » au bas d'une note de service fait "
             "sourire toute une équipe.")

    d.declencheur(
        'Observation', "Une seule feuille au milieu du babillard",
        image=IMG + 'babillard.jpg',
        pistes=[
            "Qu'est-ce qui vous fait lire une feuille affichée plutôt qu'une autre ?",
            "Quelle ligne lisez-vous en premier ?",
            "Combien de temps y accordez-vous ?",
            "Qu'est-ce qui vous fait passer votre chemin ?",
        ],
        notes="Amener l'idée que l'objet est souvent la seule ligne lue. C'est ce qui "
              "justifie qu'on y passe autant de temps dans la séance.")

    d.tableau('Analyse', "Les six parties d'une note de service",
              ['La partie', 'Ce qu\'elle contient'],
              [["L'en-tête", "DESTINATAIRE, EXPÉDITEUR, DATE, OBJET"],
               ["L'objet", "six à dix mots, sans verbe conjugué"],
               ["Le contexte", "une ou deux phrases : pourquoi cette note existe"],
               ["Le message", "ce qui change, avec les dates et les personnes"],
               ["La demande", "ce que le lecteur doit faire, et avant quand"]],
              cle=0,
              note="Puis la signature : prénom, nom, fonction. Une note ne se termine JAMAIS par une formule de politesse.",
              notes="Diapositive à photographier. La note porte la sixième partie et "
                    "l'interdit le plus utile de la séance.")

    d.regle("Une note qui ne demande rien n'a pas besoin d'exister",
            "Ce que le lecteur doit faire, avant quand, auprès de qui.",
            precision="C'est le test le plus simple d'une note de service : si le "
                      "lecteur peut la lire et refermer sans avoir rien à faire ni "
                      "rien à retenir de daté, elle encombre le babillard. Même une "
                      "note purement informative demande quelque chose : prendre note "
                      "d'une date, adresser ses questions à quelqu'un.",
            notes="Diapositive à photographier. Faire relire la note d'Aïcha : elle "
                  "demande de noter l'heure de chaque changement sur une feuille au "
                  "poste, et elle donne la date du relevé.")

    d.pratique('Compréhension', "La note de service d'Aïcha",
               "Répondez d'après le document projeté au module.", [
        ("À qui la note s'adresse-t-elle ?", "au personnel du poste 4 et aux chefs d'équipe"),
        ("Quel est l'objet ?", "rotation des tâches au poste 4, à l'essai"),
        ("Qu'est-ce qui change, et à partir de quand ?", "l'alternance, à compter du lundi 22 septembre"),
        ("Combien de temps dure l'essai ?", "quatre semaines"),
        ("Qu'est-ce qu'on demande au lecteur de faire ?", "noter l'heure de chaque changement"),
        ("Qu'est-ce qui ne change pas pendant l'essai ?", "les quotas de production"),
    ], corrige=True,
       notes="Ouvrir l'exercice `t3note` du module en parallèle : les élèves cliquent "
             "dans la note pendant que le groupe répond à l'oral.")

    d.tableau('Analyse', "Note de service ou lettre d'affaires ?",
              ['L\'élément', 'Où il va'],
              [["DESTINATAIRE et EXPÉDITEUR", "la note de service"],
               ["L'adresse du destinataire", "la lettre d'affaires"],
               ["« Monsieur, » seul sur sa ligne", "la lettre d'affaires"],
               ["« Veuillez agréer... »", "la lettre d'affaires"],
               ["Elle finit sur la fonction", "la note de service"]],
              cle=0,
              note="La note reste dans l'entreprise et n'engage que l'équipe. La lettre en sort, et ce qui y est écrit peut être invoqué plus tard.",
              notes="Diapositive à photographier. C'est l'exercice `t3genres` du "
                    "module, qui en compte dix. La note dit la différence de fond, et "
                    "elle explique toutes les différences de forme.")

    d.pratique('Pratique', "Corrigez l'objet",
               "Un objet n'a pas de verbe conjugué. Réécrivez-le.", [
        ("Objet : nous changeons l'horaire du poste 4", "Objet : modification de l'horaire du poste 4"),
        ("Objet : il faut ranger la cafétéria", "Objet : rangement de la cafétéria"),
        ("Objet : on va fermer l'entrepôt le 3 juillet", "Objet : fermeture de l'entrepôt le 3 juillet"),
        ("Objet : je demande une soumission", "Objet : demande de soumission"),
        ("Objet : la formation aura lieu jeudi", "Objet : formation du jeudi 14 mai"),
    ], corrige=True,
       notes="Le passage du verbe au nom - la nominalisation - est le même geste qu'au "
             "compte rendu, en B4. Le rappeler : c'est ce qui rend les écrits de "
             "travail secs et courts.")

    d.piege('Ponctuation',
            "« Terrebonne, 17/09/26 »",
            "« Terrebonne, le 17 septembre 2026 »",
            "Le mois s'écrit en toutes lettres dans un écrit de travail. Une date en "
            "chiffres ne se lit pas de la même façon partout - le 09/03 est le 9 mars "
            "ici et le 3 septembre ailleurs - et un document se relit parfois deux ans "
            "plus tard. Même règle pour les abréviations : « M. » et non « Mr », qui "
            "est anglais.",
            notes="Ajouter les autres abréviations d'usage au tableau : Mme, p. j. "
                  "(pièce jointe), c. c. (copie conforme), 1er, 2e. Jamais « 1ère » ni "
                  "« 2ème ».")

    d.billet(
        "Écrivez l'en-tête et l'objet de votre note de service.",
        exemples=[
            "Quatre lignes : destinataires, expéditeur, date, objet.",
            "L'objet en six à dix mots, sans verbe conjugué.",
            "La date en toutes lettres.",
        ],
        notes="Ramasser. Ne corriger que l'en-tête et l'objet : le corps de la note "
              "s'écrit en E2, et le corriger d'avance retirerait l'intérêt de la "
              "production finale.")

    return d.save(dossier)
