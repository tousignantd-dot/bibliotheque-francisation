# -*- coding: utf-8 -*-
"""B1 · Au comptoir du secrétariat.
Bloc B « Défi 1 » · couleur acier · 75 min. Première séance du défi.
Source : dialogue `t1`, exercices `t1vf` et `t1quest`, mini-leçon « Poser sa
question au comptoir ».

C'est la séance qui porte les deux intentions orales du programme —
s'informer sur le fonctionnement de l'établissement, en compréhension et en
production. Elle tient en cinq questions et une règle de rythme : une
question, une réponse, on répète, puis la suivante.

Le comptoir est un lieu difficile pour un débutant, non parce qu'on y parle
vite, mais parce qu'on y est pressé. La séance travaille donc autant le
« pouvez-vous répéter ? » que les questions elles-mêmes.
"""
import pathlib
from theme import Deck

IMG = (pathlib.Path(__file__).resolve().parents[4]
       / 'assets' / 'interactive' / 'module-n2-secretaire' / 'images')


def img(nom):
    """La photo si elle existe, sinon rien — voir a1.py."""
    chemin = IMG / (nom + '.jpg')
    return str(chemin) if chemin.exists() else None


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Au comptoir du secrétariat",
        chapeau="Saluer, dire son nom, demander une seule chose.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 1. Demander d'abord qui est déjà allé au "
                  "secrétariat, et ce qui s'est passé. Les récits sont courts et ils "
                  "disent tous la même chose : ça va trop vite.")

    d.objectifs([
        "saluer et dire son nom au comptoir ;",
        "demander un papier avec « je voudrais » ;",
        "poser une question avec « est-ce que », « où », « quand » ;",
        "demander de répéter sans être gêné.",
    ])

    d.declencheur(
        'Observation', "Que se passe-t-il à ce comptoir ?",
        image=img('lieu-secretariat'),
        pistes=[
            "Qui est derrière le comptoir ?",
            "Qu'est-ce qu'on vient demander ici ?",
            "Comment est-ce qu'on commence à parler ?",
            "Qu'est-ce qu'on fait quand on n'a pas compris la réponse ?",
        ],
        notes="La dernière piste est celle qui compte. Presque tout le monde répond "
              "« rien » ou « je pars ». C'est ce que la séance change.")

    d.dialogue('Dialogue · 1 de 2', "Je voudrais une attestation", [
        ("AMEL", "Bonjour, madame.", True),
        ("LINE", "Bonjour ! Qu'est-ce que je peux faire pour vous ?", True),
        ("AMEL", "Je voudrais une attestation, s'il vous plaît.", True),
        ("LINE", "Votre nom ?", True),
        ("AMEL", "Amel Tazi. T-A-Z-I.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire écouter deux fois, diapositive masquée. Compter les mots d'Amel : "
             "elle en dit onze en tout, et elle obtient son papier.")

    d.dialogue('Dialogue · 2 de 2', "C'est prêt jeudi", [
        ("LINE", "Vous êtes dans le groupe de madame Dufresne ?", True),
        ("AMEL", "Oui. Le cours du matin, local 214.", True),
        ("LINE", "Parfait. L'attestation est prête jeudi.", True),
        ("AMEL", "Jeudi. À quelle heure ?", True),
        ("LINE", "Après neuf heures. Vous venez au comptoir.", True),
        ("AMEL", "D'accord. Jeudi, après neuf heures. Merci beaucoup.", True),
    ], notes="La dernière réplique est le cœur du module : Amel répète le jour et "
             "l'heure avant de partir. Le faire remarquer, puis le faire faire.")

    d.regle("Une question, une réponse, on répète.",
            "Jamais trois questions dans la même phrase.",
            precision="Au comptoir, la personne répond à la <b>dernière</b> question "
                      "qu'elle entend. « Bonjour je voudrais une attestation et c'est "
                      "où et à quelle heure ? » — le reste est perdu. Une chose à la "
                      "fois.",
            notes="Diapositive à photographier. C'est la règle de rythme du module, et "
                  "elle vaut au-delà du secrétariat : à la banque, à la pharmacie, au "
                  "bureau du propriétaire.")

    d.tableau('Analyse', "Cinq questions suffisent",
              ["Ce qu'on veut", "Ce qu'on dit"],
              [["demander une chose", "Je voudrais une attestation, s'il vous plaît."],
               ["vérifier une chose", "Est-ce que le bureau est ouvert ?"],
               ["l'endroit", "Où est le local 214 ?"],
               ["le jour", "Quand est-ce que le papier est prêt ?"],
               ["l'heure", "À quelle heure ouvre le secrétariat ?"]],
              cle=1,
              note="La sixième sauve les cinq autres : « Pouvez-vous répéter, s'il vous plaît ? »",
              notes="Diapositive à photographier. Faire écrire les six phrases sur une "
                    "carte à garder dans la poche : plusieurs élèves la ressortent au "
                    "comptoir pendant des mois.")

    d.piege('Politesse', "Je veux une attestation.",
            "Je voudrais une attestation, s'il vous plaît.",
            "« Je veux » n'est pas faux : il est sec. Au Québec, on adoucit une "
            "demande. <b>Je voudrais</b> et <b>s'il vous plaît</b> ne coûtent rien et "
            "changent tout le ton de l'échange.",
            notes="Faire jouer les deux versions par la même personne, avec le même "
                  "ton. La différence s'entend tout de suite, et elle ne s'explique pas "
                  "autrement.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Amel demande une attestation.", "vrai"),
        ("La secrétaire demande son nom.", "vrai"),
        ("Le papier est prêt aujourd'hui.", "faux - il est prêt jeudi"),
        ("Amel répète le jour et l'heure avant de partir.", "vrai"),
    ], corrige=True, cols=1,
       notes="Quatre énoncés. Les faire à l'oral d'abord. Insister sur le dernier : "
             "c'est la stratégie, pas un détail du dialogue.")

    d.pratique('Pratique · au comptoir', "Deux par deux, un assis, un debout",
               "Vingt-cinq minutes. On échange les rôles à mi-temps.", [
        ("Étape 1", "A salue et dit son nom : « Bonjour, madame. Je m'appelle… »"),
        ("Étape 2", "A demande une seule chose : « Je voudrais… »"),
        ("Étape 3", "B répond en trois mots, vite, comme au vrai comptoir."),
        ("Étape 4", "A demande de répéter, puis redit la réponse et remercie."),
    ], cols=1,
       notes="Demander à l'élève qui joue la secrétaire de parler vite : c'est ce qui "
             "rend l'exercice utile. L'étape 4 est obligatoire, même quand A a compris "
             "du premier coup.")

    d.billet(
        "Écrivez les deux phrases que vous direz au comptoir cette semaine.",
        exemples=[
            "Bonjour, madame. Je m'appelle…",
            "Je voudrais…, s'il vous plaît.",
        ],
        notes="Devoir court. Demander au cours suivant qui est vraiment allé au "
              "comptoir : la démarche compte plus que la phrase écrite.")

    return d.save(dossier)
