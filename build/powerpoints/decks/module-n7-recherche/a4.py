# -*- coding: utf-8 -*-
"""A4 · Le verbe caché sous le nom
Bloc A « Je découvre » · couleur ambre · écriture et lexique · 75 min.
Source : exercice `prNom`, mini-leçon `prNom`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Le verbe caché sous le nom",
        chapeau="« La transformation des ressources naturelles » plutôt que "
                "« on transforme le bois ». Un texte officiel nomme des "
                "activités au lieu de raconter, et c'est ce qui le rend "
                "court, froid et difficile.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A, et la plus exigeante. Elle donne la clé "
                  "de lecture du bloc C : sans elle, le portrait régional reste un mur.")

    d.objectifs([
        "reconnaître un nom formé sur un verbe ;",
        "connaître les quatre fabriques : -tion, -ment, -ance, et rien du tout ;",
        "remettre un verbe debout pour comprendre une phrase officielle ;",
        "savoir qu'une lettre de candidature s'écrit, elle, avec des verbes.",
    ], notes="Le quatrième objectif est un contrepoids nécessaire : on apprend à lire "
             "la nominalisation, on n'apprend pas à s'en servir dans sa lettre.")

    d.declencheur(
        'Observation', "Ces deux phrases disent-elles la même chose ?",
        pistes=[
            "« On transforme le bois dans quatre usines de la région. »",
            "« La transformation du bois occupe quatre établissements régionaux. »",
            "Laquelle est la plus courte ? Laquelle est la plus difficile ?",
            "Où est passé le verbe ?",
        ],
        notes="Écrire les deux phrases au tableau, l'une sous l'autre. Faire compter "
              "les mots. La deuxième est plus courte de trois mots et deux fois plus "
              "lourde à lire : c'est tout le sujet.")

    d.regle("Nominaliser, c'est transformer une action en chose",
            "Le verbe disparaît, le nom prend sa place — et avec le verbe "
            "s'en va celui qui agissait.",
            precision="Un nom n'a ni sujet ni temps. « La fermeture de l'usine » ne "
                      "dit ni qui ferme, ni quand. C'est commode pour l'auteur d'un "
                      "rapport, et c'est exactement ce qui rend le texte opaque pour "
                      "le lecteur.",
            notes="Diapositive à photographier. Ne pas présenter la nominalisation "
                  "comme une ruse : c'est la langue normale des documents publics.")

    d.tableau('Analyse', "Les quatre fabriques",
              ['La fabrique', 'Le verbe donne'],
              [["-tion, -sion, -ation — féminin",
                "transformer, la transformation · produire, la production"],
               ["-ment — masculin",
                "recruter, le recrutement · investir, l'investissement"],
               ["-ance, -ence — féminin",
                "croître, la croissance · exiger, l'exigence"],
               ["rien du tout",
                "embaucher, l'embauche · demander, la demande · appeler, l'appel"]],
              cle=0,
              note="Tous les noms en -tion sont féminins, sans exception. C'est une des rares règles sans trou.",
              notes="Diapositive à photographier. Les mots de la quatrième ligne sont "
                    "les plus fréquents dans une offre d'emploi, et les seuls qui ne "
                    "s'annoncent par aucun suffixe.")

    d.cartes('Analyse', "Remettre le verbe debout", [
        ("La transformation des ressources naturelles", "on transforme le bois et le métal"),
        ("La baisse de l'embauche", "on engage moins de monde"),
        ("Le comblement des postes par voie interne", "on remplit les postes avec les gens de la maison"),
        ("L'évaluation comparative de vos études", "on compare vos études à celles d'ici"),
        ("La mise en valeur de votre expérience", "vous montrez ce que votre expérience vaut"),
        ("Une hausse de quatre virgule sept pour cent", "l'économie a grandi de 4,7 %"),
    ], cols=1,
       notes="Faire l'exercice à l'envers ensuite : donner la colonne de droite, "
             "demander la gauche. C'est plus difficile, et c'est ce que la lettre "
             "de candidature n'exigera jamais.")

    d.piege('Écriture',
            "nominaliser sa propre lettre de candidature",
            "écrire avec des verbes, à la première personne",
            "« La formation de deux techniciennes » convient à un rapport "
            "annuel. Dans une lettre où vous vous présentez, écrivez « j'ai "
            "formé deux techniciennes » : le nom efface justement celui qui "
            "agit, et c'est vous.",
            notes="Point important, et contre-intuitif : l'élève croit bien faire en "
                  "imitant la langue des documents officiels. Le lui dire maintenant, "
                  "avant le bloc D.")

    d.pratique('Grammaire', "Du verbe au nom",
               "Écrivez le nom qui correspond au verbe entre parenthèses.", [
        ("On transforme l'aluminium : la ___ de l'aluminium. (transformer)", "transformation"),
        ("L'entreprise fabrique des pièces : la ___ de pièces. (fabriquer)", "fabrication"),
        ("On recrute peu : le ___ est difficile cette année. (recruter)", "recrutement"),
        ("Le laboratoire a agrandi ses locaux : l'___ date de 2021. (agrandir)", "agrandissement"),
        ("L'économie croît : la ___ a été de 4,7 %. (croître)", "croissance"),
        ("Ils ont investi douze millions : cet ___ crée trente postes. (investir)", "investissement"),
        ("L'usine embauche : l'___ se fera avant janvier. (embaucher)", "embauche"),
        ("Le poste exige un diplôme : c'est une ___ de l'employeur. (exiger)", "exigence"),
    ], corrige=True,
       notes="Exercice `prNom` du module interactif. Faire dire l'article : c'est lui "
             "qui fixe le genre, et le genre est régulier par famille.")

    d.billet(
        "Trouvez dans un document officiel une phrase pleine de noms, et récrivez-la avec des verbes.",
        exemples=[
            "Un avis de la ville, une lettre d'un organisme, une page du gouvernement.",
            "Deux lignes suffisent.",
        ],
        notes="Ramasser les billets : les phrases rapportées serviront d'échauffement "
              "à la séance C1, où le portrait régional arrive.")

    return d.save(dossier)
