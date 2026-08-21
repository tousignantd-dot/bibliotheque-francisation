# -*- coding: utf-8 -*-
"""D2 · Il faut que, et raconter sa démarche.
Bloc D « Défi 3 · Le guichet » · couleur ambre · 75 min.
Source : exercices `t3imp` et `t3passe`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Il faut que, et raconter sa démarche",
        chapeau="« Vous avez oublié votre signature » désigne un coupable. "
                "« Il manque votre signature » désigne un manque. Même "
                "information, et ce n'est pas du tout la même conversation.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, deux points en un : la phrase impersonnelle et "
                  "les deux passés. Ils vont ensemble parce qu'un échange au guichet les "
                  "emploie tous les deux, dans la même minute.")

    d.objectifs([
        "employer « il faut que » avec le subjonctif ;",
        "connaître les quatre subjonctifs des démarches ;",
        "employer « il manque » et « il reste » au singulier ;",
        "raconter une démarche au passé composé et à l'imparfait.",
    ])

    d.declencheur(
        'Comparaison', "Deux façons de dire la même chose. Laquelle préférez-vous entendre ?",
        pistes=[
            "« Vous avez oublié votre signature. »",
            "« Il manque votre signature. »",
            "Qui est nommé dans la première ?",
            "Et dans la seconde ?",
        ],
        notes="Le groupe sent la différence tout de suite, même sans pouvoir la nommer. "
              "Poser la question « qui est nommé ? » suffit à faire trouver la réponse.")

    d.regle("Le « il » qui ne remplace personne",
            "Il faut · il manque · il reste · il s'agit de — un sujet vide.",
            precision="C'est la forme préférée de l'administration parce qu'elle énonce "
                      "une règle sans désigner de coupable. Et le verbe reste au "
                      "singulier même si ce qui manque est au pluriel : « il manque deux "
                      "documents », jamais « il manquent ».",
            notes="Diapositive à photographier. Le point d'accord surprend : le faire "
                  "vérifier en cherchant le sujet, qui est « il » et non « deux documents ».")

    d.tableau('Trois formes de « il faut »', "Selon qu\'on nomme quelqu\'un ou non",
              ['Forme', 'Quand', 'Exemple'],
              [["il faut + nom", "personne n'est nommé", "Il faut une preuve de résidence."],
               ["il faut + infinitif", "personne n'est nommé", "Il faut apporter deux pièces."],
               ["il faut que + subjonctif", "on nomme la personne", "Il faut que vous apportiez deux pièces."]],
              cle=0,
              note="Tant que vous ne nommez personne, aucun subjonctif à faire.",
              notes="Diapositive à photographier. La note du bas rassure beaucoup : le "
                    "subjonctif n'est obligatoire que dans un cas sur trois.")

    d.cartes("Les quatre subjonctifs à savoir par cœur", "Ils reviennent dans toute démarche", [
        ("être",
         "que je sois · que vous soyez · qu'elle soit. « Il faut que la facture soit récente. »"),
        ("avoir",
         "que j'aie · que vous ayez. « Il faut que j'aie mon numéro de requête. »"),
        ("faire, pouvoir",
         "que je fasse · que je puisse. « Il faut que vous puissiez revenir. »"),
        ("Les verbes réguliers",
         "sur le « ils » du présent : ils apport-ent donne que vous apport-iez. Aucun effort."),
    ], notes="La quatrième carte enlève l'essentiel de la peur : les réguliers se "
             "fabriquent, seuls quatre irréguliers s'apprennent.")

    d.pratique('Subjonctif', "Complétez",
               "Attention au subjonctif après « il faut que ».", [
        ("Il ___ deux pièces d'identité.", "faut"),
        ("Il faut que vous ___ une preuve de résidence. (apporter)", "apportiez"),
        ("Il faut que la facture ___ récente. (être)", "soit"),
        ("Il ___ une signature au bas du formulaire.", "manque"),
        ("Il ___ dix minutes avant la fermeture.", "reste"),
        ("Il faut que j'___ mon numéro de requête. (avoir)", "aie"),
        ("Il faut que nous ___ la demande avant vendredi. (faire)", "fassions"),
        ("Il faut que vous ___ revenir demain. (pouvoir)", "puissiez"),
    ], corrige=True,
       notes="Les quatre premières se font vite. Les quatre dernières demandent du temps : "
             "les faire écrire au tableau par des élèves différents.")

    d.regle("Les étapes au passé composé, le décor à l'imparfait",
            "J'ai appelé la Ville parce que mon bac débordait.",
            precision="Le passé composé dit ce qui est arrivé, une fois, à un moment. "
                      "L'imparfait dit la situation autour : ce qui durait, ce qui se "
                      "répétait. Un récit qui n'emploie qu'un seul des deux sonne faux, "
                      "même quand chaque phrase est correcte.",
            notes="Diapositive à photographier. Le test simple : si on peut ajouter "
                  "« mardi dernier » sans que ce soit bizarre, c'est le passé composé.")

    d.tableau('Le schéma le plus fréquent', "Ce qui durait, ce qui coupe",
              ['Ce qui durait', 'Ce qui l\'interrompt'],
              [["J'attendais depuis vingt minutes", "quand un préposé a répondu."],
               ["Je remplissais le formulaire", "quand la page s'est bloquée."],
               ["Il y avait douze personnes", "quand mon numéro a été appelé."]],
              cle=0,
              note="« Quand » annonce la coupure. Le repérer, et les deux temps se placent tout seuls.",
              notes="Diapositive à photographier. Faire produire trois phrases de plus par "
                    "le groupe, sur le même modèle.")

    d.pratique('Récit', "Passé composé ou imparfait ?",
               "Mettez le verbe à la bonne forme.", [
        ("Avant, je ___ le bac le mardi vers midi. (sortir)", "sortais — une habitude"),
        ("La semaine dernière, j'___ la Ville. (appeler)", "ai appelé"),
        ("J'___ depuis vingt minutes quand il a répondu. (attendre)", "attendais"),
        ("Elle ___ au guichet avec ses deux pièces. (se présenter)", "s'est présentée"),
        ("Le formulaire ___ toujours à la dernière page. (se bloquer)", "se bloquait"),
        ("Il ___ que je me déplace au comptoir. (falloir)", "a fallu"),
        ("Quand je suis arrivée, il y ___ douze personnes. (avoir)", "avait"),
    ], corrige=True,
       notes="La quatrième porte l'accord du participe avec « être ». La souligner : elle "
             "revient dans le courriel de E2.")

    d.piege("Tout mettre au passé composé",
            "J'ai attendu, il a répondu, la page s'est bloquée, je me suis déplacée.",
            "J'attendais depuis vingt minutes quand il a répondu. La page se bloquait, alors je me suis déplacée.",
            "Chaque phrase de la version fautive est correcte, et pourtant le récit sonne "
            "comme une liste. Le décor a besoin de l'imparfait : c'est lui qui explique "
            "pourquoi les étapes ont eu lieu.",
            notes="Lire les deux versions à voix haute, l'une après l'autre. La différence "
                  "s'entend immédiatement, bien mieux qu'elle ne s'explique.")


    d.billet(
        "Racontez en six phrases une démarche que vous avez déjà faite.",
        exemples=[
            "Les étapes au passé composé, le décor à l'imparfait.",
            "Terminez par ce qu'il a fallu faire, ou ce qui manquait.",
        ],
        notes="Devoir de synthèse du défi 3, et brouillon direct du courriel de E2. "
              "Le dire : les élèves gardent leur texte.")

    return d.save(dossier)
