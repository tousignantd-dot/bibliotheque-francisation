# -*- coding: utf-8 -*-
"""C4 · Il faudrait que, et par exemple
Bloc C « Défi 2 » · couleur ambre · 75 min. Grammaire et connecteurs.
Source : exercices `t2subj` et `t2exempl`, leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="Il faudrait que, et par exemple",
        chapeau="Le français des professionnels adoucit ses consignes. "
                "L'adoucissement ne retire rien — et croire qu'on avait le "
                "choix coûte parfois une place dans un calendrier.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 2. Deux points : le subjonctif des "
                  "consignes, puis les connecteurs d'exemplification. Le premier est "
                  "grammatical, le second est immédiatement utilisable à l'oral.")

    d.objectifs([
        "reconnaître les verbes qui appellent le subjonctif ;",
        "former le subjonctif présent, y compris cinq irréguliers ;",
        "entendre qu'« il faudrait que » est une obligation ;",
        "annoncer un exemple avant de le donner.",
    ], notes="Le troisième objectif n'est pas grammatical : c'est de la lecture "
             "sociale. Il vaut au moins autant que les deux premiers.")

    d.declencheur(
        'Observation', "« Il faudrait que vous passiez d'autres prélèvements. »",
        pistes=[
            "Est-ce que c'est obligatoire, ou est-ce un conseil ?",
            "Qu'est-ce qui vous fait pencher d'un côté ou de l'autre ?",
            "Comment le vérifieriez-vous, sur place ?",
        ],
        notes="Cinq minutes, et le groupe se divisera. C'est exactement le but : la "
              "phrase est ambiguë pour qui vient d'ailleurs, et elle ne l'est pas "
              "pour qui a grandi ici.")

    d.tableau('Analyse', "Les verbes qui appellent le subjonctif",
              ['Ce qu\'ils expriment', 'Les verbes'],
              [["Une obligation", "il faut que, il faudrait que, exiger que"],
               ["Un souhait", "j'aimerais que, je voudrais que, je préfère que"],
               ["Un conseil", "il vaut mieux que, il vaudrait mieux que"],
               ["Une crainte", "je crains que, j'ai peur que"]],
              cle=0,
              note="C'est le verbe qui décide, jamais le sens général de la phrase.",
              notes="Diapositive à photographier. Ajouter à l'oral ce qui n'appelle "
                    "pas le subjonctif : je pense que, je vois que, il est certain "
                    "que. Ces verbes constatent au lieu de demander.")

    d.regle("Il faudrait que est une obligation, dite poliment",
            "Le conditionnel adoucit le ton ; il ne retire pas la consigne.",
            precision="Si vous n'êtes pas certain, demandez : « est-ce que c'est "
                      "obligatoire, ou est-ce que c'est un conseil ? » La question "
                      "est parfaitement normale, elle ne froisse personne, et elle "
                      "vous évite de repartir en croyant avoir le choix.",
            notes="Diapositive à photographier. Faire répéter la question par tout le "
                  "groupe. C'est une des trois phrases les plus utiles du module.")

    d.tableau('Analyse', "Comment on forme le subjonctif",
              ['L\'étape', 'Ce qu\'on fait'],
              [["On part de", "la 3e personne du pluriel du présent : ils notent"],
               ["On enlève", "la terminaison -ent : ils not-"],
               ["On ajoute", "-e, -es, -e, -ions, -iez, -ent"],
               ["Ce qui surprend", "à nous et vous, ça ressemble à l'imparfait"]],
              cle=0,
              note="Cinq irréguliers à savoir par cœur : que je sois, que j'aie, que j'aille, que je fasse, que je puisse.",
              notes="Diapositive à photographier. Faire apprendre les cinq irréguliers "
                    "avec « que » devant : c'est ainsi qu'ils apparaissent, et jamais "
                    "autrement.")

    d.pratique('Grammaire', "Mettez le verbe au subjonctif",
               "La première phrase donne le ton.", [
        ("Il faut que vous ___ d'autres prélèvements. (passer)", "passiez"),
        ("Elle aimerait que vous ___ vos journées. (noter)", "notiez"),
        ("Il vaut mieux que ce ___ court et régulier. (être)", "soit"),
        ("Il faudrait qu'elle ___ joignable en avant-midi. (être)", "soit"),
        ("Elle préfère que vous ___ la voir avec la lettre. (aller)", "alliez"),
        ("Il craint qu'elle ___ tout à la dernière minute. (faire)", "fasse"),
    ], corrige=True,
       notes="Faire relire chaque phrase entière une fois corrigée, avec le « que ». "
             "Séparer le subjonctif de son « que » le rend introuvable dans la "
             "mémoire.")

    d.tableau('Analyse', "Annoncer un exemple",
              ['Le connecteur', 'Où il se place'],
              [["par exemple", "à peu près partout, entre virgules"],
               ["comme", "collé au nom, sans virgule"],
               ["notamment", "au milieu, pour faire ressortir un élément"],
               ["entre autres", "au milieu, quand la liste est plus longue"],
               ["ainsi", "en tête de la phrase suivante, suivi d'une virgule"]],
              cle=0,
              note="Et « c'est-à-dire » n'est pas un exemple : il redit la même chose autrement.",
              notes="Diapositive à photographier. La note du bas est la distinction "
                    "qui coûte le plus longtemps aux élèves : le test est de "
                    "remplacer par « autrement dit ».")

    d.piege('Écriture',
            "une anémie, par exemple un sang qui transporte moins bien l'oxygène",
            "une anémie, c'est-à-dire un sang qui transporte moins bien l'oxygène",
            "Un exemple donne un cas parmi d'autres ; « c'est-à-dire » redit la "
            "même chose en plus simple. Confondre les deux laisse croire qu'il "
            "existe plusieurs anémies possibles, alors qu'il s'agit d'une "
            "définition.",
            notes="« C'est-à-dire » est le mot le plus utile de tous quand on cherche "
                  "à se faire comprendre. Le donner comme un outil, pas comme une "
                  "correction.")

    d.pratique('Écriture', "Un connecteur par phrase",
               "Aucun ne revient deux fois.", [
        ("Notez ce qui a changé, ___ l'heure du lever.", "par exemple"),
        ("Certains examens se font sans rendez-vous, ___ une prise de sang.", "comme"),
        ("Apportez tout ce qui vient d'ailleurs, ___ les résultats privés.", "notamment"),
        ("Le feuillet répond à plusieurs questions, ___ celle des visites.", "entre autres"),
        ("Tout ce qui se prend compte. ___, les vitamines aussi.", "Ainsi"),
        ("Une anémie légère, ___ un sang qui transporte moins bien l'oxygène.", "c'est-à-dire"),
    ], corrige=True,
       notes="Le dernier n'est pas un connecteur d'exemple, et c'est voulu : il "
             "vérifie que la distinction du tableau précédent a été comprise.")

    d.billet(
        "Écrivez une consigne que vous avez reçue et que vous n'aviez pas comprise.",
        exemples=[
            "Au travail, à l'école, dans un bureau.",
            "Est-ce que c'était une obligation ou un conseil ?",
        ],
        notes="Deux minutes. Ces billets font une excellente ouverture pour le Défi 3, "
              "où l'on retrouvera par écrit ce qui a été dit de vive voix.")

    return d.save(dossier)
