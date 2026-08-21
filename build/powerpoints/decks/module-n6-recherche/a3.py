# -*- coding: utf-8 -*-
"""A3 · Une racine, plusieurs mots.
Bloc A « Je découvre » · couleur ambre · 75 min. Formation des mots.
Source : exercice `prMots`, mini-leçon du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='ambre',
        titre="Une racine, plusieurs mots",
        chapeau="Le vocabulaire du travail n'est pas une liste de mots "
                "séparés : c'est une dizaine de racines qui se recombinent. "
                "Apprendre la racine vaut mieux qu'apprendre cent mots.",
        duree='75 minutes')

    d.titre(notes="Séance de lexique, mais qui apprend une méthode plutôt qu'une liste. "
                  "C'est la séance qui rend les trois blocs suivants moins lourds.")

    d.objectifs([
        "reconnaître la racine commune d'une famille de mots ;",
        "former le nom de la personne avec le suffixe -eur ;",
        "former le nom de l'action avec le suffixe -tion ;",
        "employer les préfixes re-, in- et dé- pour changer le sens.",
    ])

    d.declencheur(
        'Observation', "Employer, un emploi, un employé, un employeur.",
        pistes=[
            "Qu'ont ces quatre mots en commun ?",
            "Lequel désigne la personne qui donne le travail ?",
            "Lequel désigne celle qui le reçoit ?",
            "Combien d'autres mots pouvez-vous former ?",
        ],
        notes="Laisser le groupe trouver « employable » — il vient toujours de "
              "quelqu'un. C'est le pont vers la séance B3 sur les mots en -able.")

    d.tableau('Anatomie', "Trois morceaux, trois effets",
              ['Le morceau', 'Ce qu\'il fabrique'],
              [["-eur, -euse, -trice",
                "La personne qui fait l'action : un employeur, un formateur, une formatrice, un travailleur."],
               ["-é, -ée",
                "La personne qui la reçoit : un employé, une employée."],
               ["-tion, -sion",
                "Le nom de l'action : la formation, la production, la décision. Toujours féminin."],
               ["-able, -ible",
                "Ce qui est possible : transférable, renouvelable, disponible."]],
              cle=0,
              note="Ces quatre morceaux couvrent la grande majorité des mots du monde du travail.",
              notes="Diapositive à photographier. Les élèves peuvent la recopier au dos de "
                    "leur cahier et s'y référer tout le module.")

    d.cartes("Trois préfixes qui changent le sens", "Devant le mot", [
        ("re-  ·  recommencer",
         "refaire son curriculum vitæ, revoir sa lettre, rappeler l'employeur."),
        ("in-, im-, il-  ·  le contraire",
         "un dossier incomplet, une offre inacceptable, un horaire imprévisible, une écriture illisible."),
        ("dé-, dés-  ·  défaire",
         "déplacer un rendez-vous, désapprouver une décision."),
        ("Attention à la lettre qui suit",
         "in- devient im- devant b et p, et il- devant l. Le sens ne change pas."),
    ], notes="Faire chercher au groupe d'autres mots en re- : ils en trouvent une dizaine "
             "en deux minutes, et ils les connaissent déjà tous.")

    d.regle("Les noms en -tion sont féminins",
            "La formation, la production, la décision, la profession.",
            precision="Sans exception. C'est une des rares règles du français qui ne "
                      "demande rien à retenir d'autre qu'elle-même. Comme ces mots sont "
                      "très fréquents dans les offres d'emploi, la règle sert tout de "
                      "suite.",
            notes="Diapositive à photographier.")

    d.pratique('Application', "Complétez avec le mot de la même famille",
               "Un seul mot par ligne.", [
        ("Boisverte cherche quelqu'un : c'est donc un ___ .", "un employeur"),
        ("Marisol veut devenir une ___ de cette entreprise.", "une employée"),
        ("Elle a suivi une ___ de six mois en logistique.", "une formation"),
        ("La personne qui donne le cours est le ___ .", "le formateur"),
        ("Son dossier était incomplet : elle doit le ___ .", "refaire — ou compléter"),
        ("Un horaire qu'on peut modifier est un horaire ___ .", "modifiable"),
    ], corrige=True,
       notes="Le dernier item annonce la séance B3. Ne pas l'expliquer ici : il suffit "
             "que le mot ait été rencontré une fois.")

    d.vocabulaire('Vocabulaire', "Les mots de la séance",
                  [("un poste", "L'emploi précis qu'une personne occupe, avec son titre et ses tâches."),
                   ("un secteur d'activité", "Le grand domaine où une entreprise travaille : la construction, la santé."),
                   ("un curriculum vitæ", "Le document qui résume la formation et l'expérience. On dit aussi « un CV »."),
                   ("le temps partiel", "Un horaire de moins de trente heures par semaine."),
                   ("un ordre professionnel", "L'organisme qui donne le droit d'exercer certains métiers.")],
                  notes="« Curriculum vitæ » se dit en entier à l'écrit, « CV » à l'oral. "
                        "Faire prononcer les deux — le æ surprend toujours.")

    d.piege("Confondre « employé » et « employeur »",
            "Je cherche un employé.",
            "Je cherche un emploi.",
            "Une seule syllabe sépare les deux mots, et le sens s'inverse complètement : "
            "l'employeur donne le travail, l'employé le reçoit. Dit en entrevue, le "
            "premier fait mauvais effet — et l'erreur est très fréquente.",
            notes="Faire répéter la paire trois fois. C'est court, et ça évite une "
                  "situation embarrassante.")

    d.billet(
        "Écrivez quatre mots de la famille de votre métier.",
        exemples=[
            "Le métier, la personne qui l'exerce, la formation, l'action.",
            "Exemple : cuisiner · un cuisinier · une formation en cuisine · la cuisson.",
        ],
        notes="Certains métiers résistent : « soudeur » n'a pas de nom d'action courant. "
              "C'est une bonne occasion de dire que la langue n'est pas un système parfait.")

    return d.save(dossier)
