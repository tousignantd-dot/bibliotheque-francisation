# -*- coding: utf-8 -*-
"""C2 · Mon nom, votre nom.
Bloc C « Défi 2 · Le formulaire d'inscription » · couleur ambre · 75 min.
Source : dialogue `t2b`, exercices `t2mon` et `t2b`, mini-leçon `t2mon`.

Le point de langue du programme est le déterminant possessif, et le comptoir
d'inscription est le seul endroit où il devient évident : deux personnes
parlent de la même chose — le nom de l'élève — et changent de mot selon celui
qui parle. La secrétaire dit votre nom, l'élève dit mon nom.

La séance revient aussi sur l'épellation vue en A2, mais pour la vérification
seulement : « c'est bien écrit ? ». C'est la dernière chose qu'on fait avant
de signer, et c'est celle qu'on oublie.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-inscription/images/')


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Mon nom, votre nom",
        chapeau="Répondre au comptoir avec le bon petit mot, puis vérifier "
                "avant de signer.",
        duree='75 minutes')

    d.titre(notes="Séance de langue et de vérification. Reprendre les formulaires "
                  "remplis en C1 : c'est sur eux qu'on travaille aujourd'hui, pas sur "
                  "des feuilles neuves.")

    d.objectifs([
        "employer votre et vos quand on demande ;",
        "employer mon, ma et mes quand on répond ;",
        "dire mon adresse, jamais « ma adresse » ;",
        "vérifier ce qui est écrit avant de signer.",
    ])

    d.declencheur(
        'Renversement', "La secrétaire dit « votre nom ». Vous répondez comment ?",
        pistes=[
            "Est-ce que vous répétez le mot « votre » ?",
            "Qu'est-ce qui change quand c'est vous qui parlez ?",
            "Est-ce qu'on dit « ma adresse » ?",
            "Pourquoi est-ce que ça se dit mal ?",
        ],
        notes="La deuxième piste porte toute la séance. La troisième fait rire, et la "
              "quatrième donne la raison : deux voyelles collées se disent mal, c'est "
              "tout.")

    d.tableau('Analyse', "Deux personnes, deux séries de mots",
              ["La secrétaire demande", "Vous répondez"],
              [["Votre nom ?", "Mon nom, c'est Haddad."],
               ["Votre adresse ?", "Mon adresse, c'est rue Papineau."],
               ["Votre rue ?", "Ma rue, c'est Papineau."],
               ["Vos papiers ?", "Voici mes papiers."]],
              cle=1,
              note="Le renseignement ne change pas. Seul le petit mot devant change.",
              notes="Diapositive à photographier. Faire jouer les quatre lignes à deux, "
                    "en changeant de rôle à mi-chemin : le passage de votre à mon "
                    "s'entend tout seul.")

    d.regle("Mon, ma, mes",
            "Trois formes seulement, et c'est le mot qui suit qui décide.",
            precision="<b>Mon</b> devant un mot masculin : mon nom, mon prénom, mon "
                      "courriel. <b>Ma</b> devant un mot féminin : ma rue, ma "
                      "signature. <b>Mes</b> devant plusieurs choses : mes papiers. "
                      "Et <b>votre</b> ne change jamais au singulier, masculin ou "
                      "féminin.",
            notes="Diapositive à photographier. Insister sur le dernier point : c'est "
                  "la seule bonne nouvelle de la leçon, et elle enlève la moitié du "
                  "travail.")

    d.piege('Le piège du jour',
            "« ma adresse »",
            "mon adresse",
            "Adresse est un mot féminin, mais il commence par une voyelle. Devant "
            "<b>a, e, i, o, u</b>, le féminin prend <b>mon</b> : mon adresse, mon "
            "école, mon inscription. La raison est simple — deux voyelles collées se "
            "disent mal, et le français les évite partout.",
            notes="Faire dire les deux versions à voix haute. La fausse est physiquement "
                  "désagréable à prononcer, et c'est le meilleur argument.")

    d.pratique('Pratique', "Mon, ma, mes, votre ou vos ?",
               "Complétez chaque réplique du comptoir.", [
        ("« ___ nom de famille, s'il vous plaît. »", "votre"),
        ("« ___ nom de famille, c'est Haddad. »", "mon"),
        ("« ___ date de naissance ? »", "votre"),
        ("« Voici ___ papiers, madame. »", "mes"),
        ("« ___ adresse, c'est 3420, rue Papineau. »", "mon - devant une voyelle"),
    ], corrige=True, cols=1,
       notes="Cinq énoncés. Les faire lire à deux voix, la secrétaire et l'élève : la "
             "réponse vient presque toute seule quand le rôle est clair.")

    d.dialogue('Dialogue', "C'est bien écrit ?", [
        ("MME BOURGEOIS", "Merci. Et votre rue ?", True),
        ("YARA", "Papineau. P, A, P, I, N, E, A, U.", True),
        ("MME BOURGEOIS", "Papineau. C'est bien écrit ?", True),
        ("YARA", "Oui, c'est ça. Merci, madame.", True),
    ], consigne="Écoutez, puis dites qui vérifie.",
       notes="Ici, c'est la secrétaire qui demande la vérification — mais l'élève doit "
             "savoir la demander lui-même quand elle ne le fait pas. Le dire "
             "explicitement au groupe.")

    d.regle("Avant de signer, on regarde",
            "Deux secondes maintenant, ou une semaine plus tard.",
            precision="On relit son nom, sa date de naissance et son adresse. Une "
                      "lettre de travers dans un dossier se corrige par une demande "
                      "écrite, et ça prend des semaines. « C'est bien écrit ? » et "
                      "« Vous pouvez me le montrer ? » sont les deux phrases à "
                      "retenir.",
            notes="Diapositive à photographier. Dernière règle du défi 2, et la plus "
                  "concrète : elle vaut pour le bail, la banque et la clinique.")

    d.pratique('Pratique · à deux', "Le comptoir en entier",
               "Vingt minutes. On joue l'inscription du début à la fin.", [
        ("Étape 1", "B demande les sept cases, une à la fois."),
        ("Étape 2", "A répond avec mon, ma ou mes."),
        ("Étape 3", "B écrit le nom de A, mais fait exprès une faute."),
        ("Étape 4", "A regarde et corrige : « non, D comme dimanche »."),
    ], cols=1,
       notes="L'étape 3 est à préparer discrètement avec les B. C'est le seul moyen de "
             "faire vraiment employer la correction, et le groupe s'en souvient.")

    d.billet(
        "Écrivez cinq phrases avec mon, ma ou mes, en pensant à votre formulaire.",
        exemples=[
            "Mon nom de famille, c'est…",
            "Ma date de naissance, c'est le…",
            "Mon adresse, c'est…",
        ],
        notes="Devoir court. C'est aussi le brouillon de la production écrite de la "
              "séance E1 : le dire au groupe pour que le travail serve deux fois.")

    return d.save(dossier)
