# -*- coding: utf-8 -*-
"""C2 · Les verbes pronominaux.
Bloc C « Défi 2 · La langue » · couleur ambre (écriture) · 75 min.
Source du module : exercice `l2` et sa mini-leçon « Les verbes pronominaux ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Les verbes pronominaux',
        chapeau="« Je me sens fatiguée. » Sans le petit mot du milieu, la phrase change "
                "de sens : « je sens » parle d'une odeur.",
        duree='75 minutes')

    d.titre(notes="Le petit mot du titre est le contenu entier de la séance. L'écrire au "
                  "tableau, seul, avant de commencer : ME.")

    d.objectifs([
        "reconnaître un verbe pronominal ;",
        "accorder le pronom avec le sujet ;",
        "employer se sentir, se reposer, se réveiller ;",
        "distinguer « je sens » et « je me sens ».",
    ])

    d.regle('La règle',
            "Le pronom change avec la personne, comme le sujet.",
            precision="je me · tu te · il se · nous nous · vous vous · ils se. Le pronom "
                      "se place entre le sujet et le verbe, et il ne disparaît jamais.",
            notes="La diapositive à photographier. Faire remarquer la symétrie « nous "
                  "nous » et « vous vous » : elle surprend, mais elle est régulière.")

    d.tableau('Analyse', "Se sentir, aux six personnes",
              ['La personne', 'La forme complète'],
              [["je", "je me sens"],
               ["tu", "tu te sens"],
               ["il / elle", "elle se sent"],
               ["nous", "nous nous sentons"],
               ["vous", "vous vous sentez"],
               ["ils / elles", "ils se sentent"]],
              cle=0,
              notes="Deux mots changent à chaque ligne : le pronom et la terminaison. "
                    "Faire lire la colonne de droite à voix haute, en groupe — c'est un "
                    "exercice d'oreille avant d'être un exercice d'écriture.")

    d.cartes('Analyse', "Trois verbes de la santé", [
        ("se sentir",
         "Comment on va, en général. « Je me sens fatiguée. » Suivi d'un adjectif."),
        ("se reposer",
         "Arrêter de travailler pour récupérer. « J'ai besoin de me reposer. »"),
        ("se réveiller",
         "Sortir du sommeil. « Il se réveille souvent la nuit. » — un symptôme fréquent "
         "qu'on rapporte au médecin."),
        ("s'inquiéter",
         "Devant une voyelle, le pronom s'élide : je m'inquiète, elle s'inquiète."),
    ], notes="La quatrième carte introduit l'élision. Elle n'est pas dans les exercices "
             "du module, mais elle arrive dès qu'on parle de sa santé.")

    d.pratique('Pratique · 1 de 4', "Complétez",
               "La bonne forme du verbe pronominal.", [
        ("Je ___ très fatiguée.", "je me sens très fatiguée"),
        ("Tu ___ à la maison.", "tu te reposes à la maison"),
        ("Il ___ souvent la nuit.", "il se réveille souvent la nuit"),
        ("Nous ___ le week-end.", "nous nous reposons le week-end"),
        ("Les enfants ___ mieux aujourd'hui.", "les enfants se sentent mieux aujourd'hui"),
    ], corrige=True,
       notes="C'est l'exercice 2 du défi 2. Faire dire chaque phrase complète à voix "
             "haute après l'avoir écrite.")

    d.capture('l2', "Les verbes pronominaux")

    d.piege("Le piège du pronom oublié",
            "Je sens fatiguée.",
            "Je me sens fatiguée.",
            "Sans pronom, « sentir » veut dire percevoir une odeur : « je sens le "
            "café ». Avec le pronom, il parle de votre état. Le petit mot porte tout le "
            "sens de la phrase.",
            notes="Faire entendre les deux phrases l'une après l'autre. L'écart de sens "
                  "fait rire, et c'est ce qui fait retenir.")

    d.piege("Le piège du pronom qui ne suit pas",
            "Nous se reposons le week-end.",
            "Nous nous reposons le week-end.",
            "Le pronom prend toujours la personne du sujet. « Se » n'appartient qu'à la "
            "troisième personne — il / elle / ils / elles.",
            notes="Erreur systématique quand la langue d'origine a un pronom invariable. "
                  "Ne pas s'en étonner, la corriger sans commenter.")

    d.pratique('Pratique · 2 de 4', "Avec ou sans pronom ?",
               "Les deux existent. Laquelle convient ici ?", [
        ("___ le café du matin. (sentir)", "je sens le café — une odeur"),
        ("___ mieux depuis hier. (se sentir)", "je me sens mieux — mon état"),
        ("___ ma sœur pendant une heure. (reposer / se reposer)",
         "j'ai attendu ma sœur — attention, ici c'est un autre verbe"),
        ("___ à midi tous les jours. (se réveiller)", "il se réveille à midi"),
    ], corrige=True,
       notes="La troisième ligne est un piège volontaire : le verbe attendu n'existe "
             "pas dans la phrase. Laisser chercher avant de le dire.")

    d.pratique('Pratique · 3 de 4', "Chez le médecin",
               "Répondez aux questions du médecin, avec un verbe pronominal.", [
        ("« Comment vous sentez-vous aujourd'hui ? »", "Je me sens un peu mieux."),
        ("« Est-ce que vous vous reposez assez ? »", "Non, je me repose très peu."),
        ("« Vous réveillez-vous la nuit ? »", "Oui, je me réveille deux ou trois fois."),
        ("« Est-ce que vous vous inquiétez pour votre santé ? »", "Oui, je m'inquiète un peu."),
    ], corrige=True,
       notes="Les quatre questions sont celles d'une vraie consultation. Les faire "
             "poser par un élève, pas par l'enseignant.")

    d.pratique('Pratique · 4 de 4', "Votre semaine, en trois phrases",
               "Trois verbes pronominaux, sur vous.", [
        ("Comment vous vous sentez", "aujourd'hui, vraiment"),
        ("Quand vous vous reposez", "quel jour, quel moment"),
        ("À quelle heure vous vous réveillez", "en semaine et le week-end"),
    ], corrige=False,
       notes="Dix minutes. Ramasser : les pronoms oubliés se comptent vite et disent où "
             "en est le groupe.")

    d.billet(
        "Écrivez trois phrases avec me, te ou se, sur votre santé.",
        exemples=[
            "Une phrase avec « je », une avec « nous », une avec « ils ».",
            "Le pronom doit suivre le sujet à chaque fois.",
        ],
        notes="Ramasser. C'est le contrôle le plus rapide de la séance : le pronom est "
              "juste ou il ne l'est pas.")

    return d.save(dossier)
