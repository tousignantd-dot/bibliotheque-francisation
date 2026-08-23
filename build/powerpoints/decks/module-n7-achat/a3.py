# -*- coding: utf-8 -*-
"""A3 · Ce que le préfixe change au verbe
Bloc A « Je découvre » · couleur ambre · lexique et formation des mots ·
75 min.
Source : exercice `prMots` et sa mini-leçon ; savoir « formation des mots »
du niveau 7 (deux points).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='ambre',
        titre="Ce que le préfixe change au verbe",
        chapeau="Les documents de la consommation paraissent difficiles. La "
                "plupart de leurs mots sont fabriqués avec des verbes que "
                "vous employez déjà tous les jours.",
        duree='75 minutes')

    d.titre(notes="Séance de lexique, mais pas de liste à apprendre : c'est une "
                  "méthode. Le but est qu'un élève devant un mot inconnu retire la "
                  "pièce ajoutée et retrouve le verbe, plutôt que d'ouvrir un "
                  "dictionnaire.")

    d.objectifs([
        "reconnaître les préfixes ré-, dé- et dys- dans un mot inconnu ;",
        "fabriquer le nom d'un verbe avec -tion et avec -ment ;",
        "employer l'adjectif en -able et sa forme négative ;",
        "retrouver le verbe caché sous un nom de document officiel.",
    ], notes="Le quatrième objectif est le vrai. « En cas de dysfonctionnement, le "
             "remboursement n'est pas automatique » veut dire « si ça ne marche pas, "
             "on ne vous rembourse pas forcément ». Le montrer dès l'ouverture.")

    d.declencheur(
        'Observation', "« Réclamer » : quel mot entendez-vous à l'intérieur ?",
        pistes=[
            "Que veut dire le début du mot, avant « clamer » ?",
            "Connaissez-vous d'autres mots qui commencent pareil ?",
            "Que veut dire « ré- » dans « refaire », dans « revenir » ?",
            "Réclamer, est-ce demander pour la première fois ?",
        ],
        notes="La dernière question est la bonne : réclamer, c'est redemander ce qui "
              "vous revient. Le préfixe porte tout le sens, et l'élève le sait déjà "
              "sans le savoir.")

    d.tableau('Analyse', "Trois préfixes du dossier",
              ['Le préfixe', 'Ce qu\'il ajoute'],
              [["ré-, re-", "de nouveau, ou en retour"],
               ["dé-, dés-", "le contraire, ou défaire"],
               ["dys-", "qui fonctionne mal, sans être défait"],
               ["in-, im-, ir-", "la négation d'un adjectif"]],
              cle=0,
              notes="Diapositive à photographier. Dé- et dys- se confondent à "
                    "l'oreille : on démonte une transmission, on ne la « désfonctionne » "
                    "pas. Faire répéter les deux mots l'un après l'autre.")

    d.tableau('Analyse', "Trois suffixes du dossier",
              ['Le suffixe', 'Ce qu\'il fabrique'],
              [["-tion", "un nom féminin : réclamation, réparation"],
               ["-ment", "un nom masculin : versement, remboursement"],
               ["-able", "un adjectif de possibilité : réparable"],
               ["in- plus -able", "son contraire : inacceptable, irréparable"]],
              cle=0,
              notes="Diapositive à photographier. Faire remarquer que -tion donne "
                    "toujours du féminin et -ment toujours du masculin : c'est une des "
                    "rares règles de genre qui ne souffre pas d'exception ici.")

    d.regle("Le nom en -tion cache celui qui agit",
            "Les documents officiels préfèrent le nom au verbe, parce que le nom ne dit pas qui fait l'action.",
            precision="« Le remboursement n'est pas automatique » ne nomme personne. "
                      "Remettre le verbe et son sujet fait tomber le brouillard : "
                      "« nous ne vous rembourserons pas tout seuls ». C'est le geste de "
                      "lecture le plus rentable devant un contrat, et il ne demande "
                      "aucun vocabulaire nouveau.",
            notes="Diapositive à photographier. Faire l'exercice à voix haute sur trois "
                  "phrases du contrat du module : chaque fois, qui fait l'action ?")

    d.cartes('Exemples', "Quatre mots du module, décomposés", [
        ("une réclamation", "réclamer plus -tion : le fait de redemander ce qui vous revient"),
        ("un dysfonctionnement", "dys- plus fonctionner plus -ment : ça marche, mais mal"),
        ("réparable", "réparer plus -able : qui peut être réparé"),
        ("irrecevable", "ir- plus recevoir plus -able : qu'un tribunal refusera d'examiner"),
    ], notes="Le quatrième est un mot que les élèves rencontreront s'ils vont aux "
             "petites créances. Le donner maintenant évite une mauvaise surprise plus "
             "tard.")

    d.pratique('Grammaire', "Complétez avec le mot de la même famille",
               "Un seul mot par trou.", [
        ("Elle demande au commerçant de réparer : elle fait une ___ .", "réclamation"),
        ("Le garage a fait le travail : la ___ a coûté 1 200 $.", "réparation"),
        ("La pièce n'est pas à jeter : elle est encore ___ .", "réparable"),
        ("La transmission ne fait pas ce qu'elle devrait : il y a un ___ .", "dysfonctionnement"),
        ("Chaque mois, elle paie un ___ de 222,36 $.", "versement"),
        ("Elle veut récupérer les 1 200 $ : elle en demande le ___ .", "remboursement"),
    ], corrige=True,
       notes="Huit items dans le module ; en projeter six. Faire dire le genre de "
             "chaque nom en même temps que le mot : c'est la seule façon de le fixer.")

    d.piege('Piège', "fabriquer un nom qui n'existe pas",
            "vérifier qu'on l'a déjà lu quelque part",
            "« Un réclamement », « un résolvement » : la règle est bonne, le mot "
            "n'existe pas. La fabrication des mots sert à comprendre ce qu'on lit, pas "
            "à inventer ce qu'on écrit. Dans le doute, employer le verbe.",
            notes="Rassurer le groupe : personne ne sera pénalisé pour avoir compris un "
                  "mot en le décomposant. La prudence ne vaut que pour la production "
                  "écrite.")

    d.billet(
        "Écris un mot en -tion ou en -ment que tu as déjà vu sur un papier officiel, et le verbe qui se cache dedans.",
        exemples=[
            "Un mot, un verbe.",
            "Bail, banque, école, hôpital : n'importe quel papier fait l'affaire.",
        ],
        notes="Trois minutes. Les billets font une liste que le groupe reconnaît, et "
              "ils servent d'amorce en A4, où l'on ouvre les deux documents du module.")

    return d.save(dossier)
