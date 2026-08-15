# -*- coding: utf-8 -*-
"""C4 · La condition avec « si ».
Bloc C · couleur ambre (écriture) · 60 min.
Source : exercice `t2condition` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="La condition avec « si »",
        chapeau="« On remonte si la pluie verglaçante cesse. » Toute la logique d'une "
                "journée de chantier tient dans ce petit mot : rien n'est décidé "
                "d'avance, tout dépend d'une condition.",
        duree='60 minutes')

    d.titre(notes="Relire la dernière réplique de Josée, en A1. Elle contient un « si » : "
                  "c'est ce qui laisse la porte ouverte à une reprise du travail.")

    d.objectifs([
        "construire une phrase avec une condition introduite par « si » ;",
        "écrire « s' » devant « il » ;",
        "placer la condition avant ou après la conséquence ;",
        "employer le bon temps de chaque côté.",
    ])

    d.regle('La règle',
            "Si + la condition, puis la conséquence — ou l'inverse.",
            precision="« Si le vent tombe, nous poserons la membrane. » ou « Nous "
                      "poserons la membrane si le vent tombe. » Les deux ordres sont "
                      "corrects. Quand « si » ouvre la phrase, une virgule sépare les "
                      "deux moitiés.",
            notes="Écrire les deux ordres au tableau. La virgule est le seul détail "
                  "d'écriture à retenir.")

    d.tableau('Analyse', "Les temps de chaque côté",
              ['Après « si »', 'Dans la conséquence', 'Un exemple'],
              [["présent", "futur simple", "Si le vent tombe, nous poserons la membrane."],
               ["présent", "impératif", "S'il commence à grésiller, descends de l'échelle."],
               ["présent", "présent", "Si la route est fermée, on reste à l'atelier."]],
              cle=0, props=[0.2, 0.25, 0.55],
              notes="Jamais de futur après « si » : c'est la règle la plus importante de "
                    "la séance. L'écrire en gros au tableau.")

    d.regle("La règle qu'on oublie toujours",
            "Jamais de futur après « si ».",
            precision="On écrit « si le vent tombe », jamais « si le vent tombera ». Le "
                      "futur va dans l'autre moitié de la phrase : « nous poserons la "
                      "membrane ». C'est une des rares règles du français sans "
                      "exception.",
            notes="Diapo centrale. Beaucoup d'élèves écrivent le futur des deux côtés : "
                  "c'est logique, mais c'est faux.")

    d.cartes('En apprendre plus', "Quatre choses à savoir en plus", [
        ("« Si » devient « s' » devant il",
         "« S'il pleut », « s'il commence à venter ». Mais on écrit « si elle », « si "
         "on » : l'élision ne se fait que devant « il » et « ils »."),
        ("La condition peut ouvrir ou fermer",
         "« Si le vent tombe, on monte » et « on monte si le vent tombe » disent la "
         "même chose. Le premier ordre insiste sur la condition."),
        ("« Si » n'est pas toujours une condition",
         "« Je ne sais pas s'il viendra » est une question rapportée, pas une "
         "condition. Là, le futur est possible."),
        ("« Quand » remplace « si » quand c'est certain",
         "« Quand le vent tombera, on montera » — on est sûr que le vent tombera. Avec "
         "« si », on ne l'est pas."),
    ], notes="La quatrième carte est utile et rarement enseignée : c'est la différence "
             "entre une éventualité et une certitude.")

    d.pratique('Pratique · 1 de 4', "Complétez la condition",
               "Après « si », le présent.", [
        ("Nous poserons la membrane du toit…", "si le vent tombe."),
        ("S'il tombe du verglas cette nuit,…", "l'équipe restera à l'atelier."),
        ("Prisca prendra la route…", "si la visibilité s'améliore."),
        ("Si l'avertissement est levé avant midi,…", "nous partirons pour Granby."),
    ], corrige=True,
       notes="Accepter toute suite logique. Vérifier une seule chose : pas de futur "
             "après « si ».")

    d.piege("Le piège du futur après « si »",
            "Si le vent tombera, nous poserons la membrane.",
            "Si le vent tombe, nous poserons la membrane.",
            "Après « si », on emploie le présent, même quand on parle du futur. Le futur "
            "va dans l'autre moitié de la phrase. C'est une règle sans exception, et "
            "c'est l'erreur la plus fréquente à ce niveau.",
            notes="Faire relire les quatre phrases de l'exercice précédent en vérifiant "
                  "uniquement le temps après « si ».")

    d.piege("Le piège de l'élision",
            "Si il commence à grésiller, descends.",
            "S'il commence à grésiller, descends.",
            "« Si » perd son i devant « il » et « ils » : s'il, s'ils. Devant « elle », "
            "« on », « un », il ne change pas : si elle, si on, si un. C'est la seule "
            "élision de ce mot.",
            notes="Point rapide. Faire écrire les cinq formes au tableau et passer.")

    d.pratique('Pratique · 2 de 4', "Si ou s' ?",
               "L'élision ne se fait que devant « il » et « ils ».", [
        ("___ il commence à venter, on descend.", "S'il"),
        ("___ elle arrive avant huit heures, on part ensemble.", "Si"),
        ("___ on annule, il faut prévenir le client.", "Si"),
        ("___ ils ne peuvent pas monter, ils restent à l'atelier.", "S'ils"),
        ("___ un avertissement est publié, Mado nous écrit.", "Si"),
    ], corrige=True,
       notes="Cinq items, deux élisions. Le contraste rend la règle visible.")

    d.pratique('Pratique · 3 de 4', "Écrivez la conséquence",
               "La condition est donnée. Que se passe-t-il ?", [
        ("Si les rafales dépassent quarante kilomètres à l'heure,…",
         "…personne ne monte sur le toit."),
        ("Si la visibilité tombe sous deux cents mètres,…", "…on ne prend pas la route."),
        ("Si l'avertissement est levé,…", "…Mado enverra un message à l'équipe."),
        ("Si la pluie verglaçante cesse en après-midi,…", "…on remonte sur le toit."),
    ], corrige=True,
       notes="Ces quatre conditions sont celles du module. Les faire relier aux règles "
             "de sécurité vues en A1 et A4.")

    d.pratique('Pratique · 4 de 4', "Écrivez la règle de votre travail",
               "Une phrase avec « si », une condition chiffrée.", [
        ("Une règle de sécurité", "Si les rafales dépassent 40 km/h, personne ne monte."),
        ("Une règle de route", "Si la visibilité tombe sous 200 mètres, on n'y va pas."),
        ("Une règle de température", "S'il fait moins vingt-sept ressenti, on limite les pauses dehors."),
        ("Votre propre règle", "réponse personnelle, avec un chiffre"),
    ], corrige=True,
       notes="La quatrième est libre. Les règles apportées par le groupe valent souvent "
             "mieux que les trois premières.")

    d.billet(
        "Écrivez trois phrases avec « si ».",
        exemples=[
            "Une avec « s'il », une avec la condition au début, une avec la condition "
            "à la fin.",
            "Vérifiez : aucun futur après « si ».",
        ],
        notes="Corriger le temps après « si » avant tout. C'est le savoir de la séance ; "
              "le reste viendra plus tard.")

    return d.save(dossier)
