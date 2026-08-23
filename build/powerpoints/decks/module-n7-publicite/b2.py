# -*- coding: utf-8 -*-
"""B2 · « Pourraient » : le conditionnel qui ne promet rien
Bloc B « Défi 1 » · couleur acier · 75 min.
Source : exercice `t1cond`, mini-leçon `t1cond`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='acier',
        titre="« Pourraient » : le conditionnel qui ne promet rien",
        chapeau="Un seul temps de verbe, deux métiers très différents. En "
                "publicité, il donne l'image d'un résultat sans s'y engager. "
                "Au téléphone, il rend une demande polie.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, mais elle sert deux fois : l'élève doit "
                  "reconnaître ce conditionnel dans les annonces, et le produire "
                  "lui-même dans l'appel de E1.")

    d.objectifs([
        "former le conditionnel présent de tout verbe ;",
        "connaître les six radicaux irréguliers les plus fréquents ;",
        "reconnaître le conditionnel d'incertitude dans une annonce ;",
        "employer le conditionnel de politesse au téléphone.",
    ], notes="Les deux derniers objectifs sont les mêmes formes dans deux emplois. "
             "Le dire tout de suite : les élèves cherchent souvent deux conjugaisons.")

    d.declencheur(
        'Observation', "Que promet cette phrase ?",
        pistes=[
            "« Nos entraîneurs pourraient vous faire découvrir un corps que vous ne connaissez pas. »",
            "Remplacez « pourraient » par « vont ». Qu'est-ce qui change ?",
            "Laquelle des deux phrases pourriez-vous contester ?",
            "Pourquoi une agence choisirait-elle la première ?",
        ],
        notes="La quatrième question est la clé. Une affirmation doit pouvoir se "
              "prouver ; une possibilité, non. Le conditionnel est le procédé le plus "
              "courant de la publicité et le plus difficile à attaquer.")

    d.regle("Radical du futur, terminaisons de l'imparfait",
            "je parlerais · tu parlerais · il parlerait · nous parlerions · "
            "vous parleriez · ils parleraient",
            precision="Il y a toujours un « r » juste avant la terminaison, et c'est "
                      "lui qui distingue « je parlerais » de « je parlais ». Un seul "
                      "mécanisme, pour tous les verbes sans exception.",
            notes="Diapositive à photographier. Faire entendre la différence entre "
                  "« je parlais » et « je parlerais » : elle tient au « r », et elle "
                  "est mince à l'oral.")

    d.tableau('Analyse', "Six radicaux irréguliers",
              ['Le verbe', 'Au conditionnel'],
              [["être", "je serais · nous serions"],
               ["avoir", "j'aurais · vous auriez"],
               ["aller", "j'irais · nous irions"],
               ["faire", "je ferais · vous feriez"],
               ["pouvoir", "je pourrais · nous pourrions"],
               ["voir", "je verrais · vous verriez"]],
              cle=0,
              notes="Ce sont les mêmes radicaux qu'au futur simple : les apprendre une "
                    "fois sert deux fois. Le dire, ça soulage.")

    d.cartes('Analyse', "Le même temps, deux emplois", [
        ("L'incertitude, en publicité", "Ce produit pourrait réduire vos coûts."),
        ("Ce que ça promet", "rien du tout : la phrase n'a rien affirmé"),
        ("La politesse, au téléphone", "Pourriez-vous me confirmer le montant total ?"),
        ("Ce que ça change", "la demande est adoucie, l'autre n'est pas bousculé"),
    ], cols=1,
       notes="Même forme, deux intentions. C'est le contexte qui tranche, jamais la "
             "conjugaison. Les élèves demandent souvent comment on fait la différence : "
             "on ne la fait pas, on l'entend.")

    d.pratique('Pratique', "Mettez au conditionnel présent",
               "Écrivez la forme demandée.", [
        ("Nos entraîneurs ___ (pouvoir) vous faire découvrir un corps que vous ne connaissez pas.", "pourraient"),
        ("Ce matelas ___ (améliorer) la qualité de votre sommeil.", "améliorerait"),
        ("Vous ___ (économiser) jusqu'à trois cents dollars par année.", "économiseriez"),
        ("Nos clients ___ (voir) une différence dès la première semaine.", "verraient"),
        ("Vous ___ (avoir) accès à toutes nos succursales.", "auriez"),
        ("Nous ___ (être) heureux de vous compter parmi nos membres.", "serions"),
        ("Ce produit ___ (faire) partie des meilleurs vendeurs de la saison.", "ferait"),
    ], corrige=True,
       notes="Exercice `t1cond` du module. Après correction, relire chaque phrase et "
             "demander : qu'est-ce qui est promis ? La réponse est toujours « rien ».")

    d.piege('Grammaire',
            "« si j'aurais le temps, je lirais tout »",
            "« si j'avais le temps, je lirais tout »",
            "Jamais de conditionnel après « si ». C'est l'imparfait qui va "
            "dans la condition, et le conditionnel dans la conséquence. La "
            "faute est très fréquente et très visible : elle vaut la peine "
            "d'être corrigée une fois pour toutes.",
            notes="Faire répéter la phrase juste trois fois à voix haute. C'est la "
                  "faute que l'oreille corrige mieux que la règle.")

    d.billet(
        "Écrivez trois demandes polies au conditionnel, adressées à un service à la clientèle.",
        exemples=[
            "Pourriez-vous… · J'aimerais… · Je souhaiterais…",
            "Une demande par phrase, et une demande précise.",
        ],
        notes="Devoir de production. Ces trois phrases seront réutilisées telles "
              "quelles dans l'appel de E1 : le dire, ça motive.")

    return d.save(dossier)
