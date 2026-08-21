# -*- coding: utf-8 -*-
"""B4 · Retenir le prix qu'on vient de me dire.
Bloc B « Défi 1 · Comprendre ce qu'on me répond » · couleur indigo · 60 min.
Source : exercice `t1chiffres`, reprise du dialogue `t1`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='indigo',
        titre="Retenir le prix qu'on vient de me dire",
        chapeau="Un prix se donne une fois, vite, au milieu d'une phrase. "
                "Le retenir est une compétence, et elle se travaille.",
        duree='60 minutes')

    d.titre(notes="Séance courte, entièrement d'écoute. C'est le cœur de l'intention de "
                  "compréhension orale du programme. Prévenir le groupe : on va écouter "
                  "beaucoup et parler peu, et ce n'est pas une évaluation.")

    d.objectifs([
        "retenir un prix dit une seule fois, dans une phrase ;",
        "écrire un prix entendu, en chiffres ;",
        "reconnaître la zone dans laquelle on se déplace ;",
        "oser demander qu'on répète un chiffre.",
    ])

    d.regle("Ce qu'on a le droit de faire au comptoir",
            "« Pardon, pouvez-vous répéter, s'il vous plaît ? »",
            precision="Personne ne vous en voudra. Les gens d'ici le font aussi. "
                      "Un chiffre mal compris coûte de l'argent ; une demande de "
                      "répétition ne coûte rien. Vous pouvez aussi écrire "
                      "pendant qu'on vous parle : c'est normal.",
            notes="Diapositive à photographier. C'est la phrase la plus importante du "
                  "module et celle que les élèves n'osent pas dire. Faire répéter par "
                  "tout le groupe, debout, deux fois.")

    d.tableau('Analyse', "Trois façons de faire répéter",
              ["La phrase", "Quand l'employer"],
              [["Pardon ?", "la plus courte, dite tout de suite"],
               ["Pouvez-vous répéter, s'il vous plaît ?", "la plus polie"],
               ["Plus lentement, s'il vous plaît.", "quand on a entendu mais pas saisi"]],
              cle=0,
              note="Les trois sont polies. La troisième est la plus utile pour un chiffre.",
              notes="Diapositive à photographier. Faire choisir à chacun celle qu'il "
                    "emploiera. Une seule, sue par cœur, vaut mieux que trois qu'on "
                    "cherche au moment où on en a besoin.")

    d.pratique('Écoute', "Écrivez le prix exact",
               "Réécoutez le dialogue du défi 1 et complétez.", [
        ("Un passage tout seul coûte ___ $.", "3,75"),
        ("Le dix passages coûte ___ $.", "35"),
        ("L'hebdo coûte ___ $.", "33,25"),
        ("Le mensuel coûte ___ $.", "110"),
        ("Rosario paie à peu près ___ $ par mois en ce moment.", "140"),
        ("Rosario habite dans la zone ___ .", "A"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice 5 du défi 1. Faire écouter le dialogue en entier une "
             "première fois sans écrire, puis une deuxième en écrivant. Ne pas "
             "découper l'audio : c'est justement l'enchaînement qui est difficile.")

    d.pratique('Écoute', "Un chiffre dans une phrase",
               "Écoutez et notez seulement le nombre.", [
        ("L'hebdo est à trente-trois vingt-cinq.", "33,25"),
        ("Ça revient à trois cinquante le passage.", "3,50"),
        ("La correspondance dure cent vingt minutes.", "120"),
        ("Soixante-cinq ans et plus, c'est le tarif réduit.", "65"),
        ("Une personne peut accompagner cinq enfants au maximum.", "5"),
        ("Le Week-end illimité coûte dix-sept dollars.", "17"),
    ], corrige=True, cols=2,
       notes="Dicter soi-même, à voix normale, une seule fois par phrase. Les élèves "
             "qui demandent une répétition l'obtiennent : c'est exactement le "
             "comportement qu'on veut installer, et il faut le récompenser.")

    d.piege('Écoute',
            "faire oui de la tête sans avoir compris",
            "« Pardon, pouvez-vous répéter ? »",
            "C'est le piège le plus coûteux du module, littéralement. Un élève qui "
            "hoche la tête paie ce qu'on lui dit sans le savoir. Faire répéter "
            "est un geste normal, poli, et fréquent chez les gens d'ici aussi.",
            notes="Demander au groupe qui l'a déjà fait. Presque toutes les mains se "
                  "lèvent. Dédramatiser franchement : la gêne vient de la peur de "
                  "déranger, pas d'un manque de vocabulaire.")

    d.tableau('Analyse', "Vérifier avant de payer",
              ["Ce qu'on redit", "Exemple"],
              [["le nom du titre", "un mensuel"],
               ["la zone", "zone A"],
               ["le prix", "cent dix dollars"],
               ["jusqu'à quand", "jusqu'à la fin du mois"]],
              cle=0,
              note="Quatre choses, une seule phrase : « C'est ça ? »",
              notes="Diapositive à photographier. C'est la phrase de clôture de Rosario "
                    "au défi 2, et c'est ce qu'on demandera à l'oral en E1. La faire "
                    "construire à voix haute par plusieurs élèves.")

    d.billet(
        "Écrivez la phrase que vous direz pour faire répéter un prix.",
        exemples=[
            "Pardon, ___ ?",
            "Plus ___ , s'il vous plaît.",
        ],
        notes="Devoir court. Ramasser et vérifier que chacun en a une : c'est le seul "
              "acquis de la séance qui compte vraiment.")

    return d.save(dossier)
