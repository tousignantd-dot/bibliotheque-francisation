# -*- coding: utf-8 -*-
"""C1 · Au comptoir du service à la clientèle
Bloc C « Défi 2 · La réclamation au comptoir » · couleur acier · compréhension
orale · 75 min.
Source : dialogue `t2` et exercice `t2vf` avec son bandeau de cinq mots.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Au comptoir du service à la clientèle",
        chapeau="« Une auto de sept ans, c'est de l'usure normale. » La "
                "phrase tombe dès la deuxième réplique. Ce qui suit décide "
                "de tout.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2, et la séance la plus attendue du module. Poser "
                  "d'entrée que la personne au comptoir n'est pas l'ennemie : elle "
                  "applique ce qu'on lui a appris. Cette nuance change la façon dont "
                  "le groupe écoute le dialogue.")

    d.objectifs([
        "reconnaître l'argument de l'usure normale et savoir qu'il se démontre ;",
        "distinguer une exclusion de contrat d'une règle de loi ;",
        "citer la catégorie de son étiquette pour appuyer une réclamation ;",
        "employer cinq mots de la réclamation.",
    ], notes="Le deuxième objectif est le plus difficile et le plus utile. Une "
             "exclusion vise la garantie qu'on a payée ; elle ne retire rien à celle "
             "que la loi donne. Le répéter au moins deux fois.")

    d.declencheur(
        'Mise en situation', "Vous a-t-on déjà répondu « c'est normal » à propos d'un objet brisé ?",
        pistes=[
            "Quel objet, et depuis combien de temps l'aviez-vous ?",
            "Qu'avez-vous répondu ? Qu'auriez-vous pu répondre ?",
            "Comment prouve-t-on que ce n'est pas normal ?",
            "Qui doit prouver : vous, ou la personne qui l'affirme ?",
        ],
        notes="La dernière question a une réponse nette : celui qui avance l'usure "
              "normale doit la démontrer. Presque personne ne le sait, et c'est le "
              "renversement de la séance.")

    d.dialogue('Dialogue · 1 de 3', "L'usure normale, tout de suite", [
        ("ERNESTINE", "Bonjour madame. Je viens pour l'auto que j'ai achetée ici le six avril. La transmission cogne.", True),
        ("MARYSE", "Une auto de sept ans avec cent quatre mille kilomètres, c'est de l'usure normale. Ça ne se couvre pas.", True),
        ("ERNESTINE", "Vingt-quatre jours après l'achat ?", True),
        ("MARYSE", "La date ne change rien à l'usure. Vous avez pris la garantie prolongée, ça je le vois.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Relever la réponse d'Ernestine : quatre mots, une question, aucun "
             "adjectif. C'est le modèle de réplique du bloc, et le groupe peut "
             "l'apprendre par cœur sans risque.")

    d.dialogue('Dialogue · 2 de 3', "L'exclusion de la page trois", [
        ("MARYSE", "Mais la transmission, dans ce contrat-là, il y a une exclusion pour les joints et les carters.", True),
        ("ERNESTINE", "Donc j'ai payé douze cents dollars pour une garantie qui ne couvre pas la transmission.", True),
        ("ERNESTINE", "Madame Turgeon, ce n'est pas de la garantie prolongée que je viens vous parler. C'est de celle qui est dans la loi.", True),
        ("MARYSE", "Pardon ?", True),
    ], notes="La troisième réplique est une phrase emphatique, et elle sera reprise "
             "telle quelle en C4. La faire répéter maintenant, sans l'expliquer : "
             "l'analyse viendra à sa place.")

    d.dialogue('Dialogue · 3 de 3', "La lettre sur l'étiquette", [
        ("ERNESTINE", "Sur l'étiquette que monsieur Vachon m'a remise, il y a une case « catégorie ». Elle dit C.", True),
        ("ERNESTINE", "Une auto de catégorie C est couverte un mois ou mille sept cents kilomètres, selon la première limite atteinte.", True),
        ("ERNESTINE", "Le six avril plus un mois, ça nous mène au six mai. On est le deux. J'ai fait neuf cents kilomètres.", True),
        ("MARYSE", "Vous avez lu ça où ?", True),
    ], notes="Le ton de la dernière réplique change tout : la personne au comptoir "
             "n'est pas hostile, elle est surprise. Faire écouter deux fois et "
             "demander au groupe ce qu'il entend dans sa voix.")

    d.tableau('Analyse', "Deux arguments, deux effets",
              ['Ce qu\'elle dit', 'Ce que ça produit'],
              [["« J'ai payé 1 200 $ »", "on lui répond par les exclusions"],
               ["« C'est écrit page trois »", "la discussion reste dans son contrat"],
               ["« Mon étiquette dit C »", "elle va chercher le dossier"],
               ["« Un mois ou 1 700 km »", "le chiffre remplace l'opinion"],
               ["« 24 jours, 900 km »", "il ne reste rien à contredire"]],
              cle=0,
              notes="Diapositive à photographier. Elle explique pourquoi on invoque la "
                    "garantie chiffrée en premier : elle est écrite sur le document du "
                    "commerçant lui-même.")

    d.vocabulaire('Vocabulaire', "Cinq mots de la réclamation", [
        ("la garantie légale", "La protection écrite dans la loi, qui ne s'achète pas."),
        ("la garantie de bon fonctionnement", "Celle des autos d'occasion, dont la durée dépend de la catégorie."),
        ("l'usure normale", "La détérioration qu'un objet subit forcément à l'usage."),
        ("une réclamation", "La démarche par laquelle un client demande de réparer ou de rembourser."),
        ("une exclusion", "Ce qu'un contrat de garantie payante refuse de couvrir."),
    ], notes="Faire répéter les deux premières l'une après l'autre : c'est la paire "
             "que tout le monde confond, et le bloc entier repose sur la différence.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'échange au comptoir.", [
        ("Madame Turgeon commence par invoquer l'usure normale.", "vrai"),
        ("La garantie prolongée couvre les fuites de joint.", "faux - elles sont exclues, page trois"),
        ("En catégorie C, la garantie dure six mois.", "faux - un mois ou 1 700 km"),
        ("Ernestine réclame les pièces et la main-d'œuvre.", "vrai"),
        ("Madame Turgeon accepte sur-le-champ.", "faux - elle doit en parler au directeur"),
        ("Le vendeur avait informé Ernestine de la garantie légale.", "faux - elle l'a demandé deux fois"),
    ], corrige=True,
       notes="Le sixième item ouvre C4 et la lettre du bloc D. Le laisser en suspens : "
             "on ne dit pas encore ce que ce manquement vaut.")

    d.billet(
        "Que répondrais-tu à « c'est de l'usure normale » ?",
        exemples=[
            "Une phrase, avec un chiffre dedans.",
            "Pas de reproche : un fait.",
        ],
        notes="Trois minutes. Les billets sans chiffre montrent qui n'a pas encore "
              "saisi le mécanisme, et ils resservent en C2 quand la table des "
              "catégories arrive.")

    return d.save(dossier)
