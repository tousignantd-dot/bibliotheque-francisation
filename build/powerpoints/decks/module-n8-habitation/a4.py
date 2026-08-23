# -*- coding: utf-8 -*-
"""A4 · Ce qui s'était passé avant
Bloc A « Je découvre » · couleur ambre · 75 min.
Source : exercice `prPqp` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Le plus-que-parfait, ou l'étage du dessous",
        chapeau="Une contestation est un récit ordonné. Celui qui mélange les "
                "étages du passé perd son lecteur en trois lignes — et "
                "l'ordre des faits est précisément son argument.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, dernière du bloc A. Le lien avec le module "
                  "n'est pas décoratif : le dossier de Teodora se gagne parce que le "
                  "nettoyage du drain a eu lieu AVANT le sinistre. Sans le "
                  "plus-que-parfait, cette phrase-là ne se dit pas.")

    d.objectifs([
        "former le plus-que-parfait avec le bon auxiliaire ;",
        "raconter au plus-que-parfait ce qui précède un fait déjà passé ;",
        "employer le plus-que-parfait de passé lointain, seul ;",
        "accorder le participe passé dans les deux cas.",
    ], notes="Le troisième emploi est le moins connu et le plus fréquent dans les "
             "documents : « le drain avait été refait en 2019 ».")

    d.declencheur(
        'Discussion', "Racontez la dernière fois qu'un appareil est tombé en panne chez vous",
        pistes=[
            "Qu'est-ce qui s'est passé, ce jour-là ?",
            "Et qu'est-ce qui s'était passé avant, qu'on ne voyait pas ?",
            "Aviez-vous remarqué quelque chose les semaines précédentes ?",
            "Est-ce que quelqu'un était déjà venu le réparer ?",
        ],
        notes="Les deux premières questions suffisent à faire apparaître les deux "
              "étages. Noter au tableau, en deux colonnes, les verbes que le groupe "
              "emploie : la règle se lira dedans.")

    d.regle("Deux étages, et il faut les tenir",
            "Le passé composé raconte ce qui s'est passé. Le plus-que-parfait "
            "descend d'un étage : ce qui s'était déjà passé avant.",
            precision="« L'eau est montée par le drain, parce que l'orage avait duré "
                      "trois heures. » Le premier verbe est l'événement, le second "
                      "est sa cause, et elle est antérieure. Deux passés composés "
                      "n'auraient rien dit de cet ordre.",
            notes="Diapositive à photographier. Faire relire la phrase deux fois, en "
                  "insistant sur « avait duré ».")

    d.tableau('Formation', "L'auxiliaire à l'imparfait, plus le participe",
              ['Auxiliaire', 'Exemples du dossier'],
              [["avoir", "j'avais nettoyé · nous avions gardé · ils avaient conclu"],
               ["être", "elle était descendue · l'eau était montée"],
               ["pronominaux", "je m'étais absentée · ils s'étaient plaints"]],
              cle=0,
              note="Mêmes auxiliaires qu'au passé composé, mêmes accords. Rien de neuf, tout est décalé d'un cran.",
              notes="Diapositive à photographier. Insister : celui qui dit « je suis "
                    "descendue » dit « j'étais descendue ». L'auxiliaire ne change "
                    "jamais d'un temps à l'autre.")

    d.cartes('Analyse', "Deux emplois, pas un", [
        ("L'antériorité dans un récit",
         "Deux faits passés, l'un précède l'autre. Le fait principal au passé "
         "composé, celui d'avant au plus-que-parfait. Les mots qui le "
         "déclenchent : parce que, quand, après que, puisque. "
         "« Il a fermé le dossier sans savoir qu'une entreprise avait "
         "nettoyé le drain en mai. »"),
        ("Le passé lointain, seul",
         "Aucun autre passé après lui : le plus-que-parfait dit simplement "
         "que c'est ancien, et rangé. C'est la forme des rapports "
         "d'expertise quand ils parlent de l'histoire d'un immeuble. "
         "« Le drain de fondation avait été refait en 2019, par l'ancien "
         "propriétaire. »"),
    ], cols=1,
       notes="Comparer à voix haute : « le drain a été refait en 2019 » rattache le "
             "fait à aujourd'hui ; « avait été refait » le range dans une autre "
             "époque. La nuance est réelle et les élèves l'entendent.")

    d.pratique('Grammaire', "Mettez le verbe au plus-que-parfait",
               "Chaque phrase raconte un fait antérieur à celui qui précède.", [
        ("L'eau est montée par le drain, parce que l'orage ___ (durer) trois heures.", "avait duré"),
        ("Elle a réclamé le 15 septembre ; elle ___ (prendre) vingt photographies la veille.", "avait pris"),
        ("Le drain de fondation ___ (être) refait en 2019 par l'ancien propriétaire.", "avait été"),
        ("Quand l'expert est arrivé, les boîtes ___ (rester) deux jours dans l'eau.", "étaient restées"),
        ("Il a fermé le dossier sans savoir qu'une entreprise ___ (nettoyer) le drain en mai.", "avait nettoyé"),
        ("En sept ans, l'eau ne ___ (jamais remonter) par ce drain.", "n'était jamais remontée"),
    ], corrige=True,
       notes="Le quatrième et le sixième portent l'accord avec être. Les faire "
             "justifier : « les boîtes » est féminin pluriel, « l'eau » est féminin "
             "singulier.")

    d.piege(
        'Accord',
        "la facture que j'avais gardé",
        "la facture que j'avais gardée",
        "Avec l'auxiliaire avoir, le participe s'accorde avec le complément "
        "direct placé AVANT. Ici « que » remplace « la facture », qui est "
        "placée avant : gardée. Mais dans « j'avais gardé la facture », le "
        "complément est après, et il n'y a aucun accord. C'est la même règle "
        "qu'au passé composé — on la sur-corrige souvent en ajoutant un e "
        "partout.",
        notes="Écrire les deux phrases au tableau, l'une sous l'autre, et faire "
              "trouver la différence par le groupe avant de l'expliquer.")

    d.billet(
        "Racontez en trois phrases ce qui est arrivé à Teodora, avec les deux étages.",
        exemples=[
            "Une phrase au passé composé : ce qui s'est passé le 14 septembre.",
            "Une au plus-que-parfait : ce qui s'était passé avant.",
            "Une au présent : où en est le dossier aujourd'hui.",
        ],
        notes="Trois phrases, pas plus. C'est le premier brouillon du récit qu'ils "
              "referont à l'oral en E1 et par écrit en E2.")

    return d.save(dossier)
