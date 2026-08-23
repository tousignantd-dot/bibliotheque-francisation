# -*- coding: utf-8 -*-
"""C5 · Mettre en relief ce qui compte
Bloc C « Défi 2 · Faire valoir sa réclamation » · couleur ambre · 75 min.
Écriture. Source du module : l'exercice `t2emph` et la mini-leçon du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C5', section='ambre',
        titre="Mettre en relief ce qui compte",
        chapeau="« Ce que je conteste, c'est le refus complet, pas votre "
                "évaluation. » Une phrase ordinaire met tout sur le même "
                "plan ; celle-ci choisit.",
        duree='75 minutes')

    d.titre(notes="La phrase emphatique est un savoir du niveau 8. En "
                  "français, l'ordre des mots est rigide : c'est le seul "
                  "moyen de faire ce que d'autres langues font avec l'accent "
                  "tonique. Le dire d'entrée — la classe le vit tous les jours.")

    d.objectifs([
        "employer « c'est… qui » et « c'est… que » selon la fonction ;",
        "construire « ce que… , c'est » à l'oral ;",
        "reconnaître la reprise par un pronom et savoir où elle vit ;",
        "s'en tenir à une ou deux emphases par paragraphe.",
    ], notes="Le quatrième objectif est celui qu'on oublie : enchaînées, les "
             "emphases s'annulent et le lecteur ne sait plus ce qui compte.")

    d.declencheur(
        'Pour commencer', "« Je conteste le refus complet, pas votre "
                          "évaluation. » Dites-le en mettant « ce que » "
                          "devant.",
        pistes=[
            "Qu'est-ce que la nouvelle phrase ajoute ?",
            "À quel moment l'interlocuteur apprend-il de quoi il s'agit ?",
            "Pourquoi est-ce utile au téléphone ?",
        ],
        notes="La deuxième piste est la clé : la tournure crée une attente, "
              "et l'autre ne peut pas couper avant la fin. C'est un effet "
              "purement oral, et il est très efficace.")

    d.tableau('Analyse', "La même idée, trois tournures",
              ['La phrase ordinaire', 'La mise en relief'],
              [["Le portage a fendu le meuble.", "C'est le portage qui a fendu le meuble."],
               ["Je demande la révision.", "Ce que je demande, c'est la révision."],
               ["La photo date de onze heures.", "C'est à onze heures que la photo a été prise."],
               ["Je conteste ce point-là.", "Ce point-là, je le conteste."]],
              cle=0,
              note="La dernière ligne est parlée : à l'écrit d'affaires, elle sonne relâchée.",
              notes="Diapositive à photographier. Faire lire les cinq "
                    "colonnes de droite à voix haute : la différence "
                    "s'entend, alors qu'elle se voit mal.")

    d.regle("« qui » quand le groupe est sujet, « que » partout ailleurs",
            "C'est le portage qui a fendu le meuble · C'est à onze heures vingt-deux que la photo a été prise.",
            precision="Le test : remplacez le groupe encadré par « il » ou "
                      "par « le ». Si « il » convient, c'est « qui ».",
            notes="Diapositive à photographier. Faire appliquer le test trois "
                  "fois de suite avant de passer à la pratique — c'est la "
                  "seule faute possible de la séance.")

    d.cartes('Analyse', "Trois tournures, trois usages", [
        ("c'est… qui / c'est… que", "la plus discrète, et la plus courante."),
        ("ce que… , c'est", "la plus forte à l'oral : elle crée une attente."),
        ("la reprise par un pronom", "« ce point-là, je le conteste » — parlée, très québécoise."),
        ("Ce qu'elle permet en plus", "dire ce qu'on conteste ET ce qu'on ne conteste pas, en une phrase."),
    ], cols=2,
       notes="La dernière carte est celle qui vaut le plus : elle explique "
             "pourquoi la tournure d'Amira est efficace, et elle vaut un "
             "paragraphe entier de lettre.")

    d.piege('Attention',
            "trois emphases dans un même paragraphe",
            "une, deux au maximum",
            "Enchaînées, les emphases donnent un ton théâtral qui affaiblit "
            "exactement ce qu'elles devaient renforcer. Réservez-les au point "
            "que vous voulez qu'on retienne : dans une lettre de révision, "
            "il n'y en a jamais plus de deux.",
            notes="Montrer l'effet en lisant à voix haute un paragraphe de "
                  "trois emphases. La classe entend immédiatement le "
                  "problème, sans qu'on l'explique.")

    d.pratique('Pratique', "Mettez en relief la partie indiquée",
               "Complétez la tournure.", [
        ("Je conteste le refus complet. devient : ___ je conteste, c'est le refus complet.", "Ce que"),
        ("Le portage a fendu le meuble. devient : ___ le portage qui a fendu le meuble.", "C'est"),
        ("La photo a été prise à onze heures. devient : C'est à onze heures ___ la photo a été prise.", "que"),
        ("Les deux boîtes ont le plus souffert. devient : ___ les deux boîtes qui ont souffert.", "Ce sont"),
        ("Je vous propose un compromis. devient : Ce que je propose, ___ un compromis chiffré.", "c'est"),
        ("Le vaisselier était intact. devient : Le vaisselier, ___ était intact à huit heures.", "il"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t2emph` du module, dans sa version projetée. "
             "Pour le dernier item, redemander où cette tournure s'emploie : "
             "au téléphone, pas dans la lettre.")

    d.billet(
        "Écris la phrase emphatique qui portera ta demande dans ta lettre.",
        exemples=[
            "Commence par « Ce que je conteste, c'est… ».",
            "Ajoute ce que tu ne contestes PAS : c'est ce qui la rend efficace.",
        ],
        notes="Cinq minutes. Garder ces billets : ils serviront tels quels "
              "dans la lettre de la séance E2, et le dire maintenant motive "
              "l'exercice.")

    return d.save(dossier)
