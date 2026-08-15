# -*- coding: utf-8 -*-
"""D2 · Officiel ou familier ? Devoir et il faut.
Bloc D · couleur ambre (écriture) · 75 min.
Source : exercices `t3formel`, `t3devoir` et `t3falloir`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre='Officiel ou familier ?',
        chapeau="« Salut Nadia » et « Madame, » ne s'écrivent pas à la même personne. "
                "Choisir le mauvais registre est plus visible qu'une faute "
                "d'orthographe — et plus difficile à rattraper.",
        duree='75 minutes')

    d.titre(notes="Séance double : le registre d'abord, l'obligation ensuite. Prévoir une "
                  "pause nette au milieu.")

    d.objectifs([
        "choisir une formule d'appel selon la personne ;",
        "choisir une formule de salutation qui va avec ;",
        "employer devoir + infinitif pour une obligation personnelle ;",
        "employer il faut + infinitif pour une consigne générale.",
    ])

    d.tableau('Analyse', "Deux registres, deux séries de formules",
              ['Registre', "Formules d'appel", 'Salutations'],
              [["officiel", "Madame, · Monsieur, · Bonjour Madame,",
                "Sincères salutations, · Respectueusement,"],
               ["familier", "Bonjour Karim, · Salut Nadia, · Chère Farida,",
                "À bientôt, · Amicalement,"]],
              cle=0,
              note="On ne mélange jamais les deux : « Madame, … Amicalement » sonne faux.",
              notes="Faire remarquer la cohérence exigée : le début et la fin doivent "
                    "être du même registre.")

    d.regle('La règle du registre',
            "Le registre dépend de la relation, pas de l'importance du message.",
            precision="On écrit « Madame, » à une superviseure qu'on connaît depuis "
                      "deux semaines, et « Salut » à un collègue qu'on tutoie depuis "
                      "trois ans. Ce n'est pas la gravité du sujet qui décide, c'est "
                      "la personne.",
            notes="Beaucoup d'élèves croient qu'un sujet sérieux impose le registre "
                  "officiel. Le corriger explicitement.")

    d.cartes('En apprendre plus', "Quatre repères pour choisir", [
        ("Est-ce que je la tutoie ?",
         "Si oui, registre familier. Si non ou si vous hésitez, registre officiel. "
         "C'est le repère le plus fiable."),
        ("Depuis combien de temps ?",
         "Deux semaines : officiel. Trois ans : cela dépend de la relation. Le temps "
         "seul ne suffit pas."),
        ("Quelle est sa position ?",
         "Une direction, une superviseure, un fonctionnaire : officiel, même après des "
         "années."),
        ("Dans le doute, officiel",
         "Le registre officiel n'offense jamais personne. Le registre familier employé "
         "trop tôt, si."),
    ], notes="La quatrième carte est la règle de sécurité. La donner comme telle : dans "
             "le doute, on ne se trompe pas en étant poli.")

    d.pratique('Pratique · 1 de 4', "Officiel ou familier ?",
               "Pensez à la relation, pas au sujet.", [
        ("Un message à votre collègue, avec qui vous prenez souvent la pause.", "familier"),
        ("Un message à l'infirmière de l'école, à qui vous avez parlé une fois.", "officiel"),
        ("Un message à votre voisin, qui garde parfois votre chat.", "familier"),
        ("Un message à votre superviseure, pour qui vous travaillez depuis deux semaines.",
         "officiel"),
        ("Un message à la directrice du centre, où vous étudiez depuis six mois.", "officiel"),
        ("Un message à votre enseignant, avec qui vous avez fait du bénévolat.", "familier"),
    ], corrige=True,
       notes="Le dernier item se discute : la relation extérieure au cours change le "
             "registre. Laisser le groupe argumenter avant de trancher.")

    d.piege("Le piège du mélange",
            "Madame Bélisle, … Amicalement, Karim",
            "Madame Bélisle, … Sincères salutations, Karim Haddad",
            "Un début officiel et une fin familière donnent l'impression qu'on a copié "
            "deux modèles différents. Les deux extrémités du message doivent aller "
            "ensemble — c'est ce qu'on remarque en premier à la relecture.",
            notes="Montrer trois courriels mélangés au tableau et faire trouver "
                  "l'incohérence. Exercice rapide et efficace.")

    # ── seconde partie · l'obligation ───────────────────────────────
    d.regle("L'obligation, deux façons",
            "Devoir désigne quelqu'un. Il faut ne désigne personne.",
            precision="« Je dois m'inscrire aujourd'hui » : c'est moi. « Il faut remplir "
                      "le formulaire jaune » : c'est vrai pour tout le monde. Les deux "
                      "sont suivis d'un verbe à l'infinitif.",
            notes="Écrire les deux exemples au tableau, l'un sous l'autre. La différence "
                  "est immédiatement visible.")

    d.tableau('Analyse', "Devoir au présent",
              ['La personne', 'La forme', 'Un exemple'],
              [["je", "je dois", "Je dois aller chez le dentiste."],
               ["tu", "tu dois", "Tu dois prévenir la secrétaire."],
               ["il, elle", "elle doit", "Nour doit demander une explication."],
               ["nous", "nous devons", "Nous devons remplir le formulaire."],
               ["vous", "vous devez", "Vous devez apporter une preuve."]],
              cle=1,
              notes="« Ils doivent » complète le tableau ; le donner à l'oral. Il sert "
                    "peu dans les messages du module, où l'on parle de soi ou à vous.")

    d.pratique('Pratique · 2 de 4', "Transformez avec devoir",
               "Devoir au présent, puis le verbe à l'infinitif.", [
        ("Je vais chez le dentiste dans vingt minutes.", "Je dois aller chez le dentiste."),
        ("Nour demande une explication à sa collègue.", "Nour doit demander une explication."),
        ("J'arrive toujours à l'heure à mon rendez-vous.", "Je dois arriver à l'heure."),
        ("Il avertit la secrétaire pour justifier son absence.", "Il doit avertir la secrétaire."),
        ("J'écris un courriel à mon enseignante.", "Je dois écrire un courriel."),
    ], corrige=True,
       notes="Faire vérifier chaque fois que le second verbe est bien à l'infinitif. "
             "C'est le seul point à corriger.")

    d.pratique('Pratique · 3 de 4', "Transformez avec il faut",
               "Une consigne générale, sans désigner personne.", [
        ("Expliquez la procédure aux nouveaux employés.", "Il faut expliquer la procédure."),
        ("Justifiez votre retard par écrit avant midi.", "Il faut justifier son retard avant midi."),
        ("Apportez votre billet médical à la réception.", "Il faut apporter son billet médical."),
        ("Prenez le temps de bien vous reposer.", "Il faut prendre le temps de se reposer."),
    ], corrige=True,
       notes="Faire remarquer que « votre » devient « son » : la consigne générale ne "
             "s'adresse plus à quelqu'un en particulier.")

    d.piege("Le piège de l'infinitif",
            "Il faut vous justifiez votre retard.",
            "Il faut justifier votre retard.",
            "Après « il faut » et après « devoir », le verbe reste à l'infinitif. Il ne "
            "se conjugue pas et ne prend pas de sujet. C'est une erreur qui vient de la "
            "traduction directe, et elle disparaît dès qu'on la voit une fois.",
            notes="Faire relire les neuf réponses des deux exercices précédents en "
                  "vérifiant uniquement l'infinitif.")

    d.pratique('Pratique · 4 de 4', "Devoir ou il faut ?",
               "Est-ce que la phrase désigne quelqu'un ?", [
        ("___ prévenir avant de partir. (règle du centre)", "Il faut"),
        ("Je ___ partir plus tôt aujourd'hui.", "dois"),
        ("Vous ___ apporter deux documents.", "devez"),
        ("___ remplir le formulaire jaune. (consigne affichée)", "Il faut"),
        ("Nour ___ accompagner sa mère demain.", "doit"),
    ], corrige=True,
       notes="Les mentions entre parenthèses donnent la clé : une règle ou une consigne "
             "affichée n'a pas de destinataire, donc « il faut ».")

    d.billet(
        "Écrivez le début et la fin d'un courriel officiel, puis d'un courriel familier.",
        exemples=[
            "Quatre lignes en tout : deux appels, deux salutations.",
            "Ajoutez une phrase avec « je dois » et une avec « il faut ».",
        ],
        notes="Corriger la cohérence des registres avant l'infinitif. Rendre avant E1, "
              "où le courriel complet sera écrit.")

    return d.save(dossier)
