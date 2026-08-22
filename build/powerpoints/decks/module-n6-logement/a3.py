# -*- coding: utf-8 -*-
"""A3 · Quand la lettre ment sur le son
Bloc A « Je découvre » · couleur indigo · 60 min. Séance de graphie-phonie.
Source : exercice `prGraphie` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='indigo',
        titre="Quand la lettre ment sur le son",
        chapeau="Trois groupes de lettres qui ne se disent pas comme ils "
                "s'écrivent — et le jour où ça vous fait perdre une heure.",
        duree='60 minutes')

    d.titre(notes="Séance courte et vivante. Elle se tient debout : beaucoup de "
                  "répétition, peu d'écriture. Prévoir les postes pour la seconde "
                  "moitié, l'exercice se fait à l'oreille.")

    d.objectifs([
        "entendre le son [k] derrière les lettres ch ;",
        "entendre le son [s] derrière la lettre x, dans les nombres ;",
        "entendre le son de « chat » derrière sh et sch ;",
        "retrouver un mot entendu quand la première orthographe ne donne rien.",
    ], notes="Le quatrième objectif est le plus utile de la séance : c'est celui "
             "qui sert dans la vraie vie, quand on cherche un mot entendu au "
             "téléphone.")

    d.declencheur(
        'Mise en situation', "Vous entendez un mot au téléphone. Vous le cherchez ensuite, et rien ne sort. Que faites-vous ?",
        pistes=[
            "Avez-vous déjà écrit un mot comme vous l'entendiez ?",
            "Quel mot français vous a le plus surpris à l'écrit ?",
            "Dans votre langue, l'orthographe suit-elle la prononciation ?",
        ],
        notes="Beaucoup de langues des élèves s'écrivent comme elles se disent. Le "
              "français les déroute pour cette raison précise, et le dire soulage : "
              "ce n'est pas leur oreille qui est en cause.")

    d.tableau('Analyse', "Trois groupes, trois sons",
              ['On lit', 'On entend'],
              [["ch (mots d'étude)", "[k] — une chorale, la technologie, le chaos"],
               ["x (dans les nombres)", "[s] — dix-huit, soixante-quinze"],
               ["sh et sch (emprunts)", "le son de « chat » — un schéma, un flash"]],
              cle=0,
              note="Trois cas seulement, mais très fréquents.",
              notes="Diapositive à photographier. Ne pas chercher de règle générale : "
                    "il n'y en a pas. Ces mots s'apprennent un par un, et ils sont peu "
                    "nombreux.")

    d.cartes('Détail', "Ce qui se cache derrière chaque groupe", [
        ("ch qui dit k", "Des mots venus du grec : une chorale, la technologie, un psychologue, le chaos. Presque toujours des mots d'école ou de science."),
        ("Ce qui ne change pas", "Chercher, chaque, chambre, chauffage gardent le son ordinaire. Le k est l'exception, jamais la règle."),
        ("x qui dit s", "Dix-huit, soixante-quinze. Seul, le s s'entend ; devant une consonne, il se tait ; devant une voyelle, il se lie."),
        ("sh et sch", "Un schéma, un sushi, un flash, un t-shirt. Trois de ces quatre mots existent aussi en anglais : la bouche doit rester française."),
    ], notes="Faire dire chaque exemple par le groupe entier avant de commenter. "
             "L'oreille apprend en répétant, pas en écoutant l'enseignante expliquer.")

    d.pratique('Écoute', "Quel son porte le groupe de lettres ?",
               "Écoutez, puis dites : comme K, comme S, ou comme CH.", [
        ("une chorale", "comme K"),
        ("la technologie", "comme K"),
        ("dix-huit", "comme S"),
        ("six mois", "comme S"),
        ("un schéma", "comme CH"),
        ("un sushi", "comme CH"),
    ], corrige=True,
       notes="Les douze cartes de l'exercice interactif reprennent la même liste, "
             "avec l'audio. Faire cet échauffement de vive voix d'abord : le "
             "casque vient après.")

    d.regle("Un mot introuvable se cherche autrement",
            "Quand l'orthographe entendue ne donne rien, changez de lettre.",
            precision="Vous entendez « tecnologie » : essayez « ch » à la place du "
                      "k. Vous entendez « soisante » : essayez « x » à la place du "
                      "s. Deux essais suffisent presque toujours, et ils "
                      "remplacent une demi-heure de recherche.",
            notes="Diapositive à photographier. Faire faire l'essai en direct sur un "
                  "poste, avec un mot que le groupe choisit lui-même.")

    d.piege('Attention',
            "« un t-shirt » dit à l'anglaise",
            "« un t-shirt » dit à la française : ti-cheurt",
            "Ces mots sont français depuis longtemps. La consonne est bien "
            "celle de « chat », mais la voyelle aussi doit être française. "
            "Un mot emprunté se prononce avec la bouche de la langue qui "
            "l'accueille.",
            notes="Le faire entendre deux fois, dans les deux prononciations. Les "
                  "élèves qui parlent anglais entendent la différence tout de suite ; "
                  "les autres ont besoin de la comparaison.")

    d.billet(
        "Notez un mot français dont l'orthographe vous a déjà trompé.",
        exemples=[
            "Un mot suffit.",
            "Écrivez-le comme vous l'entendiez, puis comme il s'écrit.",
        ],
        notes="Deux minutes. Ramasser les billets et en faire une liste de classe : "
              "elle sert de banque d'exercices pour les séances suivantes, et elle "
              "vient des élèves.")

    return d.save(dossier)
