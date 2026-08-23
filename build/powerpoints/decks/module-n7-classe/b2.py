# -*- coding: utf-8 -*-
"""B2 · Les panneaux de route d'un exposé
Bloc B « Défi 1 » · couleur teal · 75 min.
Source : exercices `t1conn` et `t1conf`, mini-leçon `t1conn`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='teal',
        titre="Les panneaux de route d'un exposé",
        chapeau="Dans une conversation, on répond à ce qui vient d'être dit. "
                "Devant quelqu'un qui expose, on sait à l'avance ce qui "
                "s'en vient — à condition d'entendre les panneaux.",
        duree='75 minutes')

    d.titre(notes="Séance d'écoute et de prise de notes. Elle sert deux fois : pour "
                  "comprendre la personne-ressource, et pour construire son propre "
                  "exposé au bloc E. Le dire dès le début.")

    d.objectifs([
        "reconnaître le connecteur qui annonce le plan d'un exposé ;",
        "reconnaître ceux qui marquent les étapes et ceux qui changent de sujet ;",
        "entendre qu'une reformulation ne contient rien de neuf ;",
        "prendre des notes en mots-clés, pas en phrases.",
    ], notes="Le quatrième objectif est celui qui change le plus la vie des élèves, "
             "et le plus difficile à tenir : on écrit des phrases par réflexe.")

    d.declencheur(
        'Observation', "Qu'est-ce que ces quatre phrases annoncent ?",
        pistes=[
            "« Avant de commencer, je vous dis où je m'en vais. »",
            "« Deuxième point. »",
            "« Quant au secteur de votre centre… »",
            "« Autrement dit, il refroidit l'air autour de lui. »",
        ],
        notes="Les quatre familles de la séance, dans l'ordre. Ne pas donner les "
              "noms tout de suite : laisser le groupe dire ce que chacune fait.")

    d.tableau('Analyse', "Quatre familles de connecteurs",
              ['Ce qu\'il annonce', 'Les mots'],
              [["Le plan",
                "avant de commencer, je vais parler d'abord de, mon exposé comprend"],
               ["Une étape",
                "premier point, deuxième point, d'abord, ensuite, enfin"],
               ["Un changement",
                "quant à, en ce qui concerne, à propos de"],
               ["Une reformulation",
                "autrement dit, c'est-à-dire, en d'autres mots"],
               ["Une conséquence",
                "par conséquent, donc, ainsi"],
               ["La fin",
                "en somme, pour finir, ce qu'il faut retenir"]],
              cle=0,
              notes="Diapositive à photographier, et la plus réutilisée du module : "
                    "elle sert au bloc C pour écrire et au bloc E pour parler.")

    d.regle("Le connecteur dit quoi faire de la suite",
            "Un connecteur ne décore pas la phrase : il dit à celui qui "
            "écoute ce qu'il doit faire de ce qui vient.",
            precision="« Quant à » veut dire : nouveau paragraphe dans vos notes. "
                      "« Autrement dit » veut dire : rien de neuf, voici la version "
                      "courte, notez celle-là. « En somme » veut dire : c'est fini.",
            notes="Diapositive à photographier. C'est la formulation qui débloque la "
                  "prise de notes : on n'écoute plus des mots, on suit des consignes.")

    d.pratique('Compréhension', "Que faut-il faire de ce qui suit ?",
               "Pour chaque phrase entendue, dites quoi noter.", [
        ("« En ce qui concerne l'arrosage… »", "nouveau point, nouveau paragraphe"),
        ("« Autrement dit, la canopée compte plus. »", "la version courte, à noter"),
        ("« Par conséquent, le secteur chauffe. »", "une conséquence de ce qui précède"),
        ("« Deuxième point : ce que fait un arbre. »", "une étape, il en reste"),
        ("« En somme, c'est la canopée. »", "la fin, la phrase du résumé"),
        ("« À propos de la méthode… »", "on quitte le sujet précédent"),
    ], corrige=True,
       notes="Faire répondre à voix haute et vite. L'objectif est l'automatisme, "
             "pas l'analyse.")

    d.piege('Écoute',
            "« Quand à notre secteur… »",
            "« Quant à notre secteur… »",
            "Les deux se prononcent pareil et ne s'écrivent pas pareil. "
            "« Quant à » est suivi d'un nom et annonce un changement de "
            "sujet ; « quand » est suivi d'un verbe et parle du temps. La "
            "suite de la phrase les sépare, l'oreille ne le fait pas.",
            notes="Piège d'écriture, à voir maintenant parce qu'il reviendra dans "
                  "les résumés du bloc C. Écrire les deux au tableau et les y "
                  "laisser.")

    d.tableau('Analyse', "Prendre des notes pendant un exposé",
              ['Ce qu\'on écrit', 'Ce qu\'on n\'écrit pas'],
              [["Un tiret par idée", "des phrases complètes"],
               ["Le connecteur entendu", "les mots de liaison inutiles"],
               ["Les chiffres et leur année", "les chiffres seuls"],
               ["Un point d'interrogation sur ce qui est estimé", "rien du tout"]],
              cle=0,
              note="Trois ou quatre mots par idée suffisent, et la phrase suivante ne se perd pas.",
              notes="Diapositive à photographier. Faire un essai : lire trois "
                    "répliques de Perrine et demander des notes, puis comparer les "
                    "feuilles. Les plus courtes sont les meilleures.")

    d.pratique('Écoute', "La transcription du début de la rencontre",
               "Retrouvez dans le texte le passage qui répond à chaque question.", [
        ("Où annonce-t-elle ses trois parties ?", "« je vais parler d'abord de… »"),
        ("Quelle est la définition d'un îlot de chaleur ?", "« un secteur où la température de surface dépasse… »"),
        ("Quel renseignement est présenté comme certain ?", "« l'asphalte noir monte bien plus haut… »"),
        ("Quel chiffre est donné au conditionnel ?", "« l'écart serait d'une dizaine de degrés »"),
        ("Quel passage reformule en plus court ?", "« autrement dit, il refroidit l'air… »"),
        ("Quel connecteur annonce un changement ?", "« quant au secteur de votre centre »"),
    ], corrige=True,
       notes="Le module fait cliquer dans le texte ; en classe, projeter la "
             "transcription et faire venir un élève la surligner au tableau. Même "
             "exercice, même bénéfice.")

    d.billet(
        "Écrivez la phrase par laquelle vous annoncerez le plan de votre exposé.",
        exemples=[
            "Commencez par « Avant de commencer… » ou « Je vais parler d'abord de… ».",
            "Trois parties, pas quatre.",
        ],
        notes="Devoir concret, et première pierre de l'exposé du bloc E. Ramasser "
              "et corriger : une annonce de plan bien faite vaut une minute de "
              "présentation.")

    return d.save(dossier)
