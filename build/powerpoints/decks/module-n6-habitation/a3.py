# -*- coding: utf-8 -*-
"""A3 · Le mot du métier et le mot de tous les jours
Bloc A « Je découvre » · couleur ambre · 75 min. Formation des mots.
Source : exercice `prMots` et sa mini-leçon. Savoirs du programme : employer
des préfixes et des suffixes dans la formation des mots ; exploiter les
familles de mots pour la nominalisation ou l'adjectivation.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='ambre',
        titre="Le mot du métier et le mot de tous les jours",
        chapeau="« L'eau part mal le long du mur » et « l'écoulement des eaux "
                "de surface est déficient » disent la même flaque. Ce sont "
                "les mêmes verbes, habillés d'un suffixe.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire et de grammaire à la fois. Commencer par "
                  "reprendre les mots rapportés dans les billets de A2 : la moitié "
                  "d'entre eux se démonte avec ce qu'on va voir.")

    d.objectifs([
        "fabriquer un nom à partir d'un verbe avec -age, -ment, -tion ;",
        "fabriquer un adjectif avec -able, et son contraire avec in- ;",
        "reconnaître le verbe caché dans un nom technique ;",
        "employer re- et dé- pour dire refaire et défaire.",
    ], notes="Le troisième objectif est celui qui sert vraiment : lire un rapport, "
             "c'est défaire des noms.")

    d.declencheur(
        'Observation', "« L'écoulement des eaux de surface est déficient. » Qu'est-ce que ça dit ?",
        pistes=[
            "Quel verbe se cache dans « écoulement » ?",
            "Comment le dirais-tu à un voisin, en dix mots ?",
            "Pourquoi un document écrit ainsi plutôt qu'autrement ?",
        ],
        notes="Laisser traduire par le groupe. Quelqu'un finira par dire « l'eau part "
              "mal » : c'est la bonne réponse, et il faut le dire clairement pour "
              "que personne ne croie que la phrase technique dit plus.")

    d.tableau('Analyse', "Trois suffixes qui font des noms",
              ['Le suffixe', 'Du verbe au nom'],
              [["-age", "sécher, le séchage · nettoyer, le nettoyage"],
               ["-ment", "écouler, l'écoulement · effondrer, un effondrement"],
               ["-tion", "rénover, une rénovation · inspecter, une inspection"],
               ["-ure", "couvrir, une couverture · ouvrir, une ouverture"]],
              cle=0,
              note="Le genre suit le suffixe : -age et -ment masculins, -tion et -ure féminins.",
              notes="Diapositive à photographier. La note règle l'article du même "
                    "coup, et c'est une règle qui ne se trompe presque jamais.")

    d.tableau('Analyse', "Un suffixe qui fait des adjectifs, deux préfixes qui font des verbes",
              ['La marque', 'Ce qu\'elle fait'],
              [["-able", "ce qu'on peut : habitable, réparable, payable"],
               ["in-, im-, ir-", "le contraire : inhabitable, irréparable"],
               ["re-, ré-", "refaire : recouler, réaménager, rouvrir"],
               ["dé-, dés-", "défaire : démonter, déshumidifier"]],
              cle=0,
              note="Sur un chantier, on refait plus souvent qu'on ne fait.",
              notes="Diapositive à photographier. « Déshumidifier » se dira tous les "
                    "jours pendant quatre semaines dans ce module : c'est le verbe "
                    "de l'attente.")

    d.regle("Retrouver le verbe caché dans le nom",
            "Un document technique dit avec des noms ce qu'on dit avec des verbes.",
            precision="La politique écrit « le remplacement du drain » ; à la table de "
                      "cuisine, on dit « on change le drain ». C'est la même chose. "
                      "Défaire cet habillage, c'est comprendre une phrase de rapport "
                      "en une seconde au lieu de trois.",
            notes="Diapositive à photographier. C'est la règle du bloc, et elle "
                  "resservira tout le bloc C, quand on lira le rapport et la "
                  "soumission.")

    d.pratique('Pratique', "Du verbe au nom",
               "Donnez le nom de la même famille, avec son article.", [
        ("on rénove le sous-sol", "la rénovation"),
        ("on inspecte la maison", "l'inspection"),
        ("l'eau s'écoule mal", "l'écoulement"),
        ("on isole les murs", "l'isolation"),
        ("on sèche le mur", "le séchage"),
        ("on installe la plomberie", "l'installation"),
    ], corrige=True,
       notes="Faire dire l'article à voix haute chaque fois. « L'isolation » et non "
             "« l'isolement » : c'est l'erreur à corriger ici, pas plus tard.")

    d.piege('Piège', "dire « l'isolement des murs »",
            "dire « l'isolation »",
            "L'isolation est le matériau et le travail ; l'isolement est le fait "
            "d'être seul. Deux suffixes, deux mondes. Sur une soumission, on ne lit "
            "jamais « isolement », et le mot ferait sourire l'entrepreneur.",
            notes="Écrire les deux au tableau, l'un sous l'autre, et les laisser "
                  "jusqu'à la fin de la séance.")

    d.pratique('Pratique', "Du nom au verbe",
               "Traduisez la phrase du rapport en phrase de tous les jours.", [
        ("l'écoulement est déficient", "l'eau part mal"),
        ("la rénovation du sous-sol", "on refait le sous-sol"),
        ("l'inspection du bâtiment", "quelqu'un est venu voir la maison"),
        ("la période de séchage", "on attend que ça sèche"),
        ("le sous-sol est habitable", "on peut y vivre"),
        ("le solde est payable en trois versements", "on paiera en trois fois"),
    ], corrige=True,
       notes="Exercice central de la séance, et le plus utile des deux : c'est dans "
             "ce sens-là qu'on lit un document. Accepter toute traduction juste, ne "
             "pas corriger le style.")

    d.billet(
        "Écris une phrase de document que tu as reçue et que tu n'as pas comprise.",
        exemples=[
            "Une phrase suffit.",
            "Souligne le nom qui cache un verbe.",
        ],
        notes="Trois minutes. Les phrases rapportées de la vraie vie — bail, "
              "assurance, ville — valent mieux que celles du module. Les garder pour "
              "le bloc C.")

    return d.save(dossier)
