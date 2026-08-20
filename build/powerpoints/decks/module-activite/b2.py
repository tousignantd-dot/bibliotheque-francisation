# -*- coding: utf-8 -*-
"""B2 · Il faut, il est important de.
Bloc B · couleur ambre (écriture) · 90 min.
Source : mini-leçon `t1imperso`, exercice `t1imperso`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre='Il faut, il est important de',
        chapeau="« Il faut une preuve de résidence. » Ce « il » ne désigne "
                "personne. C'est la langue des règles — celle des dépliants, "
                "des formulaires et des consignes.",
        duree='90 minutes')

    d.titre(notes="Séance de grammaire longue. Commencer par écrire « il faut » au tableau "
                  "et demander : de qui parle-t-on ? Le flottement est instructif.")

    d.objectifs([
        "reconnaître une forme impersonnelle et ce qu'elle annonce ;",
        "employer il faut + un nom ou un verbe ;",
        "employer il est + adjectif + de + verbe ;",
        "reconnaître il faut que suivi du subjonctif.",
    ])

    d.tableau('Analyse', "Quatre formes, une seule fonction",
              ['La forme', 'Exemple'],
              [["il faut + nom", "Il faut une preuve."],
               ["il faut + verbe", "Il faut arriver à l'heure."],
               ["il est + adj + de + verbe", "Il est important d'arriver tôt."],
               ["il faut que + subjonctif", "Il faut que vous soyez là."]],
              cle=2,
              note="Les trois premières ne nomment personne. Seule la quatrième désigne quelqu'un.",
              notes="Diapo centrale. Faire recopier avant de continuer.")

    d.regle("Le « il » qui ne désigne personne",
            "Dans « il faut », le mot « il » est vide.",
            precision="Ce n'est ni vous, ni moi, ni la personne au comptoir. La forme "
                      "impersonnelle sert justement à énoncer une règle qui vaut pour tout "
                      "le monde à la fois. Ne cherchez pas de qui on parle.",
            notes="Beaucoup d'élèves cherchent le sujet et se perdent. Le dire clairement "
                  "règle une confusion durable.")

    d.regle('La forme écrite : il est + adjectif',
            "C'est celle des dépliants et des affiches.",
            precision="« Il est important d'arriver dix minutes d'avance. » · « Il est "
                      "préférable de rester dans la salle. » · « Il est interdit de courir "
                      "au bord de la piscine. » Trois adjectifs, trois forces différentes.",
            notes="Écrire les trois adjectifs au tableau — important, préférable, interdit — "
                  "et les classer du plus fort au plus faible avec le groupe.")

    d.regle('Quand la personne compte : que + subjonctif',
            "On ajoute « que », et le verbe qui suit change de forme.",
            precision="« Il faut que vous soyez là. » · « Il est important qu'il n'ait pas "
                      "peur. » Cette forme s'appelle le subjonctif. Le cours vous demande "
                      "de la <b>reconnaître</b>, pas de la produire.",
            notes="Insister sur la dernière phrase : elle rassure et elle est conforme au "
                  "programme. « Il faut arriver tôt » évite la difficulté et reste correct.")

    d.piege('Confondre obligation et conseil',
            "Il est préférable que les parents restent dans la salle. — Donc c'est interdit d'entrer ?",
            "Non : c'est un conseil. « Il faut » aurait été une obligation.",
            "« Il faut » oblige. « Il est préférable » conseille. « Il est interdit » "
            "défend. Trois formules qui se ressemblent et qui ne demandent pas du tout la "
            "même chose. Écoutez laquelle vous entendez.",
            notes="C'est la distinction la plus utile de la séance. Y consacrer du temps.")

    d.pratique('Pratique · 1 de 2', "Quelle forme ?",
               "Complétez avec il faut ou il est + adjectif.", [
        ("___ une preuve de résidence pour le tarif réduit.", "Il faut"),
        ("___ d'arriver dix minutes avant le cours.", "Il est important / préférable"),
        ("___ apporter un maillot et une serviette.", "Il faut"),
        ("___ que les parents restent dans la salle.", "Il est préférable"),
        ("___ que vous soyez là à neuf heures pile.", "Il faut"),
        ("___ qu'il n'ait pas peur de l'eau, c'est tout.", "Il est important"),
    ], corrige=True,
       notes="Plusieurs réponses sont acceptables. Faire justifier : obligation ou conseil ?")

    d.pratique('Pratique · 2 de 2', "Obligation, conseil ou interdiction ?",
               "Classez chaque phrase.", [
        ("Le bonnet de bain est obligatoire.", "obligation"),
        ("Il est préférable que les parents restent dans la salle.", "conseil"),
        ("Il est interdit de courir au bord de la piscine.", "interdiction"),
        ("Des sandales sont recommandées.", "conseil"),
        ("Il faut une preuve de résidence.", "obligation"),
        ("Il n'est pas nécessaire de venir en personne.", "ni l'un ni l'autre — c'est permis"),
    ], corrige=True, cols=1,
       notes="La dernière ligne est la plus fine : « pas nécessaire » ne veut pas dire "
             "« interdit ». C'est une permission.")

    d.cartes('Où vous le retrouverez', "Bien au-delà des loisirs", [
        ("Sur les formulaires",
         "« Il est important de remplir toutes les cases. » · « Il faut joindre une copie "
         "de votre pièce d'identité. »"),
        ("Dans les consignes de sécurité",
         "« Il est interdit de fumer. » · « Il faut porter des chaussures fermées. »"),
        ("Dans les lettres officielles",
         "« Il est nécessaire de nous prévenir dix jours à l'avance. » C'est la formule la "
         "plus fréquente de l'administration."),
    ], notes="Le dire au groupe : cette séance ressert chez le médecin, à la banque et à "
             "l'école de leurs enfants. C'est ce qui justifie les quatre-vingt-dix minutes.")

    d.billet(
        "Écrivez quatre conditions pour une activité que vous connaissez.",
        exemples=[
            "Une obligation, un conseil, une interdiction, une permission.",
            "Employez il faut, il est important de, il est interdit de, il n'est pas nécessaire de.",
        ],
        notes="Corriger individuellement. Rendre avant E1 : ces phrases servent à la "
              "production orale, où il faut expliquer une activité.")

    return d.save(dossier)
