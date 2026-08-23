# -*- coding: utf-8 -*-
"""D2 · La question interdite, et l'échelon qui n'est pas affiché
Bloc D « Défi 3 » · couleur ambre · 75 min.
Source : exercices `t3subj`, `t3emph` et `t3interdit`, et leurs mini-leçons.
Fait vérifié : article 18.1 de la Charte des droits et libertés de la
personne, qui renvoie aux motifs de l'article 10.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Ce qu'on n'a pas le droit de vous demander",
        chapeau="Ce n'est pas une règle de politesse : c'est une loi "
                "québécoise. Le difficile n'est pas de le savoir — c'est de "
                "répondre en trois secondes sans se soumettre ni se fâcher.",
        duree='75 minutes')

    d.titre(notes="Séance sensible. Plusieurs élèves ont vécu la situation et ne "
                  "l'avaient jamais nommée. Prévoir du temps, et ne pas forcer les "
                  "témoignages.")

    d.objectifs([
        "nommer la règle et les motifs qu'elle protège ;",
        "distinguer une question interdite de sa jumelle permise ;",
        "répondre à l'inquiétude réelle, puis refermer sans s'excuser ;",
        "employer le subjonctif après ses déclencheurs, et l'emphase pour mettre en relief.",
    ], notes="Le troisième objectif est le seul qui demande de la pratique orale. Les "
             "deux points de langue viennent le servir, pas l'inverse.")

    d.declencheur(
        'Discussion', "Vous a-t-on déjà posé une question qui vous a mise mal à l'aise ?",
        pistes=[
            "En entrevue, ou sur un formulaire d'embauche ?",
            "Avez-vous répondu ? Qu'est-ce qui se serait passé si vous aviez refusé ?",
            "Saviez-vous que vous aviez le droit de ne pas répondre ?",
            "Est-ce que la question portait sur vous, ou sur le travail ?",
        ],
        notes="La dernière question annonce toute la séance : la tâche est permise, "
              "la personne ne l'est pas. Laisser le groupe y arriver.")

    d.regle("L'article 18.1 de la Charte",
            "Nul ne peut, dans un formulaire de demande d'emploi ou lors "
            "d'une entrevue, exiger un renseignement portant sur l'un des "
            "motifs de discrimination énumérés à l'article 10.",
            precision="Les quatorze motifs : la race, la couleur, le sexe, l'identité "
                      "ou l'expression de genre, la grossesse, l'orientation "
                      "sexuelle, l'état civil, l'âge, la religion, les convictions "
                      "politiques, la langue, l'origine ethnique ou nationale, la "
                      "condition sociale, le handicap. La règle vaut à toutes les "
                      "étapes : formulaire, examen préembauche, entrevue.",
            notes="Diapositive à photographier. C'est la Commission des droits de la "
                  "personne et des droits de la jeunesse qui reçoit les plaintes en "
                  "matière de discrimination à l'embauche.")

    d.tableau('Analyse', "Chaque question interdite a une jumelle permise",
              ['Interdite', 'Permise'],
              [["Avez-vous des enfants en bas âge ?",
                "Êtes-vous disponible de quinze heures à vingt-trois heures trente ?"],
               ["Avez-vous un problème de dos ?",
                "Pouvez-vous soulever des caisses de vingt kilos ?"],
               ["Dans quel pays êtes-vous née ?",
                "Êtes-vous légalement autorisée à travailler au Canada ?"],
               ["Votre religion vous empêche-t-elle de travailler le soir ?",
                "Y a-t-il des dates où vous ne seriez pas disponible ?"]],
              cle=0,
              notes="Diapositive à photographier. Les deux colonnes cherchent le même "
                    "renseignement utile ; une seule des deux a le droit de le "
                    "chercher. C'est là qu'il faut ramener la conversation.")

    d.regle("L'exception, et sa limite exacte",
            "Une question redevient permise quand le renseignement est fondé "
            "sur les aptitudes ou qualités requises par l'emploi.",
            precision="Le test qui marche : la question porte-t-elle sur la tâche ou "
                      "sur la personne ? La tâche est permise, la personne ne l'est "
                      "pas. On peut demander si vous pouvez soulever vingt kilos ; on "
                      "ne peut pas demander si vous avez mal au dos.",
            notes="Diapositive à photographier. L'exception est étroite et elle se "
                  "vérifie phrase par phrase, jamais en bloc.")

    d.pratique('Pratique 1 de 3', "A-t-on le droit de la poser ?",
               "Décidez pour chacune.", [
        ("Êtes-vous disponible cinq jours par semaine ?", "permise - la tâche"),
        ("Avez-vous des enfants en bas âge ?", "interdite - l'état civil"),
        ("Avez-vous déjà supervisé plus de quinze personnes ?", "permise - l'expérience"),
        ("Quel âge avez-vous ?", "interdite - l'âge"),
        ("Êtes-vous autorisée à travailler au Canada ?", "permise - une condition d'emploi"),
        ("Prévoyez-vous une grossesse cette année ?", "interdite - la grossesse"),
    ], corrige=True,
       notes="Faire nommer le motif à chaque « interdite ». C'est en le nommant qu'on "
             "s'en souvient, pas en le reconnaissant.")

    d.cartes('Analyse', "La réponse en trois temps", [
        ("Répondre à l'inquiétude réelle",
         "Je vais vous répondre sur ce qui vous intéresse : je suis "
         "disponible pour le quart de soir cinq jours sur cinq, et je le suis "
         "depuis deux ans."),
        ("Refermer le reste",
         "Pour le reste, je préfère ne pas répondre. Une phrase, calme, "
         "mélodie descendante. On ne cite pas la loi et on ne se fâche pas."),
        ("Enchaîner sans silence",
         "On repart tout de suite sur autre chose. Le silence après le refus "
         "est ce qui rend le moment lourd, et c'est à vous de ne pas le "
         "laisser s'installer."),
    ], notes="Faire apprendre la deuxième phrase par cœur. En situation, on n'invente "
             "pas : « pour le reste, je préfère ne pas répondre ».")

    d.pratique('Pratique 2 de 3', "Le subjonctif et ses déclencheurs",
               "Subjonctif, ou indicatif ?", [
        ("Je tiens à ce que ce ___ (être) écrit dans la lettre.", "soit"),
        ("Bien que la question ___ (être) interdite, je comprends l'inquiétude.", "soit"),
        ("Même si l'équipe ___ (être) incomplète, la production continue.", "est - indicatif"),
        ("Il paraît que le groupe ___ (vouloir) ouvrir une deuxième usine.", "veut - indicatif"),
        ("Je ne crois pas qu'ils ___ (pouvoir) répondre avant vendredi.", "puissent"),
        ("Il est certain qu'elle ___ (avoir) l'expérience demandée.", "a - indicatif"),
    ], corrige=True,
       notes="Les trois indicatifs sont les exceptions qui trahissent : même si, il "
             "paraît que, adjectif de certitude. Les faire encadrer au crayon.")

    d.pratique('Pratique 3 de 3', "Mettre en avant ce qui compte",
               "Réécrivez en mettant le groupe souligné en relief.", [
        ("J'apporte seize ans d'usine.", "Ce que j'apporte, c'est seize ans d'usine."),
        ("Le raisonnement vous intéresse.", "Ce qui vous intéresse, c'est le raisonnement."),
        ("J'ai besoin d'une date.", "Ce dont j'ai besoin, c'est d'une date."),
        ("J'avais approuvé l'étiquette.", "C'est moi qui avais approuvé l'étiquette."),
        ("Je veux ce poste.", "Ce poste-là, je le veux."),
    ], corrige=True,
       notes="Attention à l'accord : « c'est moi qui ai décidé », jamais « qui a ». "
             "Et une ou deux emphases par entrevue, pas davantage : le procédé s'use.")

    d.piege('Piège', "demander un échelon de plus",
            "proposer un échelon contre une contrepartie datée",
            "Une demande nue se refuse en trois secondes : « ça ne se donne "
            "pas comme ça ». Une proposition qui offre quelque chose met "
            "l'autre en position d'accepter sans rien concéder d'avance. "
            "Chiffrez ce que votre contrepartie vaut pour l'employeur, jamais "
            "ce que l'échelon vaut pour vous.",
            notes="Reprendre la dernière réplique de Shirin, en D1. Elle accepte que "
                  "le refus soit écrit aussi, et c'est ce qui rend la proposition "
                  "crédible.")

    d.billet(
        "Écrivez la phrase que vous direz si on vous pose une question interdite.",
        exemples=[
            "Deux parties : la disponibilité, puis « pour le reste... ».",
            "Apprenez-la par cœur : en situation, on n'invente pas.",
        ],
        notes="Devoir court, à faire relire à voix haute au début de E1. C'est la "
              "seule phrase du module qui doit être sue mot pour mot.")

    return d.save(dossier)
