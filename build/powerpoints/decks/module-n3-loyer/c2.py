# -*- coding: utf-8 -*-
"""C2 · Je voudrais, j'aimerais, est-ce que je pourrais.
Bloc C « Défi 2 · Téléphoner pour visiter » · couleur teal · 75 min.
Source : exercice `t2poli` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='teal',
        titre="Je voudrais, j'aimerais, est-ce que je pourrais",
        chapeau="Au téléphone, la politesse remplace le sourire. Trois blocs "
                "de deux mots suffisent à changer tout un appel.",
        duree='75 minutes')

    d.titre(notes="Séance de langue, tirée directement de l'appel de la séance C1. "
                  "Ouvrir en faisant lire à voix haute les premières phrases écrites au "
                  "billet précédent, et en demandant au groupe lesquelles sonnent "
                  "polies.")

    d.objectifs([
        "employer je voudrais et j'aimerais pour demander ;",
        "employer est-ce que je pourrais pour demander une permission ;",
        "savoir que le verbe qui suit ne change jamais ;",
        "finir chaque demande par s'il vous plaît.",
    ])

    d.regle("Ce que le téléphone enlève",
            "Le visage, les gestes, le sourire",
            precision="En personne, le visage adoucit tout. Au téléphone, il "
                      "ne reste que les mots, et « je veux visiter » sonne dur "
                      "même quand on ne le pense pas. Trois formules suffisent "
                      "à rétablir ce que la voix seule ne dit pas.",
            notes="Diapositive à photographier. Faire l'expérience : dire « je veux "
                  "visiter » en souriant, puis les yeux baissés et sans expression. Le "
                  "groupe entend la différence tout de suite.")

    d.tableau('Analyse', "Les trois formules polies",
              ["On dit", "Quand"],
              [["je voudrais", "pour demander quelque chose"],
               ["j'aimerais", "pour annoncer une question"],
               ["est-ce que je pourrais", "pour demander une permission"],
               ["est-ce que je peux", "la même chose, un peu plus direct"]],
              cle=0,
              note="Les quatre sont corrects. Le premier suffit presque toujours.",
              notes="Diapositive à photographier. Ne pas expliquer le conditionnel : au "
                    "niveau 3, ces formes s'apprennent comme des blocs. La conjugaison "
                    "viendra plus tard, dans un autre cours.")

    d.tableau('Analyse', "Le verbe qui suit ne change jamais",
              ["On dit", "Le second verbe"],
              [["je voudrais visiter", "visiter"],
               ["j'aimerais savoir", "savoir"],
               ["est-ce que je pourrais venir", "venir"],
               ["est-ce que je peux rappeler", "rappeler"]],
              cle=1,
              note="C'est la forme du dictionnaire : elle ne se conjugue pas.",
              notes="Diapositive à photographier. C'est la même mécanique que le futur "
                    "proche de la séance C4 : un verbe qui change, un verbe qui ne "
                    "change pas. Le signaler, ça prépare le terrain.")

    d.tableau('Analyse', "Les quatre phrases polies de l'appel",
              ["Le moment", "La phrase"],
              [["ouvrir", "Bonjour. Je vous appelle pour l'annonce."],
               ["annoncer", "J'aimerais poser trois questions."],
               ["demander", "Est-ce que je pourrais le visiter ?"],
               ["faire répéter", "Pouvez-vous répéter, s'il vous plaît ?"]],
              cle=0,
              note="Quatre phrases, et l'appel entier tient debout.",
              notes="Diapositive à photographier. Les faire apprendre par cœur : ce sont "
                    "des blocs, pas des phrases à construire. C'est ce qui permet de "
                    "téléphoner sans paniquer.")

    d.piege('Registre',
            "« Je veux voir le logement. »",
            "« Je voudrais visiter le logement, s'il vous plaît. »",
            "Ce n'est pas une faute de grammaire, c'est une faute de ton. La "
            "personne au bout du fil peut décider de ne pas rappeler, et vous "
            "ne saurez jamais pourquoi.",
            notes="Le dire franchement, sans dramatiser. Beaucoup d'élèves emploient "
                  "« je veux » parce que c'est le premier verbe appris, pas par "
                  "impolitesse.")

    d.piege('Grammaire',
            "« je voudrais je visite »",
            "« je voudrais visiter »",
            "Après je voudrais, j'aimerais et je pourrais, le verbe reste à sa "
            "forme de base : visiter, savoir, venir, parler. Un seul verbe se "
            "conjugue dans la phrase.",
            notes="Erreur classique des langues où les deux verbes se conjuguent. Faire "
                  "produire cinq phrases correctes à l'oral avant de passer à l'écrit.")

    d.pratique('Grammaire', "Complétez la demande",
               "Je voudrais, j'aimerais ou est-ce que je pourrais ?", [
        ("Bonjour. ___ visiter le logement, s'il vous plaît.", "je voudrais"),
        ("___ poser trois questions, si vous avez une minute.", "j'aimerais"),
        ("___ venir samedi matin ?", "est-ce que je pourrais"),
        ("___ vous rappeler demain ?", "est-ce que je peux"),
        ("Pouvez-vous répéter l'adresse, ___ ?", "s'il vous plaît"),
        ("___ savoir si le chauffage est compris.", "j'aimerais"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice 2 du Défi 2. Plusieurs réponses sont acceptables : "
             "accepter toute formule polie et le dire au groupe, pour éviter la chasse à "
             "la bonne réponse unique.")

    d.pratique('Répétition', "Quatre phrases à savoir par cœur",
               "Écoutez, puis répétez sans regarder.", [
        ("Bonjour. Je vous appelle pour l'annonce.", "ouvrir"),
        ("J'aimerais poser trois questions.", "annoncer"),
        ("Est-ce que je pourrais le visiter cette semaine ?", "demander"),
        ("Pouvez-vous répéter, s'il vous plaît ?", "faire répéter"),
        ("Merci beaucoup, madame. Bonne journée.", "fermer"),
    ], corrige=True,
       notes="Répétition en chœur, puis individuellement, puis les yeux fermés. Ces cinq "
             "phrases sont l'ossature de la production orale : elles doivent sortir sans "
             "réfléchir.")

    d.billet(
        "Écrivez trois demandes polies que vous ferez au téléphone.",
        exemples=[
            "Je voudrais ___ .",
            "J'aimerais ___ . Est-ce que je pourrais ___ ?",
        ],
        notes="Devoir court. Vérifier surtout le verbe qui suit : il doit rester à sa "
              "forme de base. Les erreurs relevées se reprennent en début de séance C3.")

    return d.save(dossier)
