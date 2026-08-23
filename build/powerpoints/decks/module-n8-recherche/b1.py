# -*- coding: utf-8 -*-
"""B1 · Vingt minutes au téléphone
Bloc B « Défi 1 · L'appel de présélection » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t11`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="L'appel qu'on croit subir",
        chapeau="Un appel de présélection n'est pas un interrogatoire : "
                "c'est la première fois où l'on peut poser des questions, et "
                "presque personne ne s'en sert.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc B. Demander d'abord qui a déjà reçu un appel de "
                  "ce genre, et ce qu'on y a dit. La réponse la plus fréquente est "
                  "« j'ai répondu à ses questions », et c'est exactement le problème.")

    d.objectifs([
        "comprendre ce que vérifie réellement un appel de présélection ;",
        "reconnaître le mot « vérifiable » et savoir ce qu'il demande ;",
        "poser une question ouverte plutôt qu'une question fermée ;",
        "reformuler à la fin ce qu'on a compris.",
    ], notes="Le troisième objectif est le geste du bloc. Les trois séances suivantes "
             "y reviennent chacune par un côté.")

    d.declencheur(
        'Discussion', "Qu'est-ce que vous auriez le droit de demander, au téléphone ?",
        pistes=[
            "Le salaire ? L'horaire ? Le nom du supérieur ?",
            "Pourquoi le poste est ouvert ?",
            "Combien de personnes il y a dans l'équipe ?",
            "Qu'est-ce qui vous retient de le demander ?",
        ],
        notes="La dernière question est la vraie. La réponse est presque toujours la "
              "même : la peur de paraître exigeant. Ne pas la balayer, la nommer.")

    d.dialogue('Dialogue 1 de 4', "On vérifie trois choses", [
        ("DANIELLE", "Madame Tabatabai ? Danielle Éthier, conseillère en acquisition de talents chez Boréalis Emballages.", True),
        ("DANIELLE", "C'est un appel d'une vingtaine de minutes, sans piège : je vérifie quelques éléments et je réponds à vos questions.", True),
        ("DANIELLE", "Premièrement, la disponibilité. Le quart va de quinze heures à vingt-trois heures trente. Est-ce que cet horaire vous conviendrait ?", True),
        ("SHIRIN", "Il me conviendrait, oui. Je travaille déjà de soir depuis deux ans, et j'ai organisé ma vie autour de cet horaire-là.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer « je réponds à vos questions » : c'est une invitation, "
             "et elle est presque toujours ignorée. Shirin, elle, la prendra.")

    d.dialogue('Dialogue 2 de 4', "Le mot qui n'a pas été compris", [
        ("DANIELLE", "Et ces onze années, elles sont vérifiables ?", True),
        ("SHIRIN", "Excusez-moi, je ne suis pas certaine de comprendre le mot « vérifiables ». Vous voulez dire que quelqu'un pourrait le confirmer ?", True),
        ("DANIELLE", "C'est exactement ça. Une personne qu'on pourrait joindre, ou un document.", True),
        ("SHIRIN", "Alors oui. Mon ancien directeur vit à Montréal depuis 2019 et il accepte de servir de référence.", True),
    ], notes="Le geste central de la séance, et il tient en une phrase. Shirin ne dit "
             "pas « je n'ai pas compris » : elle nomme le mot, un seul, et propose "
             "elle-même une interprétation. Dix secondes, et l'appel repart.")

    d.dialogue('Dialogue 3 de 4', "La question que personne n'avait posée", [
        ("SHIRIN", "L'annonce dit « superviseure de production, quart de soir ». Est-ce que l'équipe existe déjà, ou faut-il la constituer ?", True),
        ("DANIELLE", "Je dois vous avouer que la question me surprend un peu — vous êtes la première à la poser. L'équipe se constitue.", True),
        ("SHIRIN", "Neuf à embaucher, donc. Et la personne qui supervise participerait-elle au choix de ces neuf-là ?", True),
        ("DANIELLE", "Elle y participerait, oui, avec le directeur de la production. C'est une bonne question. Je la note.", True),
    ], notes="« Je la note » veut dire ce qu'il dit : la question entre au dossier, et "
             "le dossier se relit avant l'entrevue finale. Une question bien placée "
             "vous suit dans le processus.")

    d.dialogue('Dialogue 4 de 4', "On referme en résumant", [
        ("SHIRIN", "Pourriez-vous me dire ce que l'examen écrit évalue exactement ? Je voudrais m'y préparer sans perdre mon temps.", True),
        ("DANIELLE", "Une mise en situation : une ligne qui s'arrête, trois problèmes en même temps, et vous décidez dans quel ordre.", True),
        ("SHIRIN", "Je vous remercie. Autrement dit, c'est le raisonnement qu'on regarde, pas la bonne réponse.", True),
        ("DANIELLE", "Vous avez tout compris. Je vous envoie la convocation aujourd'hui.", True),
    ], notes="La reformulation finale est ce qui laisse l'impression. Faire remarquer "
             "que Shirin change les mots : elle ne répète pas « mise en situation », "
             "elle dit « le raisonnement ». Répéter ne prouve rien.")

    d.tableau('Analyse', "Ce qu'on vérifie, ce qu'on peut demander",
              ['Ce que vérifie l\'employeur', 'Ce que vous pouvez demander'],
              [["la disponibilité réelle",
                "pourquoi le poste est ouvert"],
               ["l'expérience annoncée, et si elle se vérifie",
                "si l'équipe existe ou reste à constituer"],
               ["la façon dont vous parlez",
                "ce que l'examen évalue, et comment s'y préparer"]],
              cle=0,
              note="Trois et trois : l'appel n'est pas à sens unique, et il ne dure que vingt minutes.",
              notes="Diapositive à photographier. Faire noter les trois questions de "
                    "droite : ce sont celles du devoir de A1, reformulées.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'appel.", [
        ("Shirin dit avoir dirigé jusqu'à vingt-deux personnes.", "vrai"),
        ("Elle fait semblant d'avoir compris le mot « vérifiables ».", "faux - elle le fait préciser"),
        ("L'équipe du quart de soir est complète.", "faux - sept sur seize"),
        ("La personne embauchée participera au choix des recrues.", "vrai"),
        ("Madame Éthier avait déjà reçu cette question d'un autre candidat.", "faux - Shirin est la première"),
        ("L'examen écrit évalue surtout l'orthographe.", "faux - le raisonnement"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le dernier "
             "rassure beaucoup d'élèves, et c'est une bonne raison de le garder.")

    d.billet(
        "Écrivez les trois questions que vous poseriez, vous, au téléphone.",
        exemples=[
            "Aucune ne doit pouvoir se répondre par oui ou par non.",
            "Une doit porter sur ce que l'annonce ne dit pas.",
        ],
        notes="Devoir. Les questions produites servent d'exercice en B3, quand on les "
              "réécrira à la forme soutenue.")

    return d.save(dossier)
