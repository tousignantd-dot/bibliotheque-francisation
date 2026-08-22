# -*- coding: utf-8 -*-
"""A2 · Quand les lettres mentent : ch, x, sh
Bloc A « Je découvre » · couleur indigo · 75 min.
Source : exercice `prGraphie` et sa mini-leçon « Quand les lettres mentent ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Quand les lettres mentent : ch, x, sh",
        chapeau="Chronologie, orchestre, flash-back, schéma : le vocabulaire "
                "du cinéma est plein de mots dont l'écriture trompe "
                "l'oreille. Trois cas, et ils se comptent sur les doigts.",
        duree='75 minutes')

    d.titre(notes="Séance de graphie-phonie du module. Le savoir est commun à tout le "
                  "niveau 6 ; ce qui change ici, ce sont les mots choisis, tous tirés "
                  "du vocabulaire des arts.")

    d.objectifs([
        "entendre le son k derrière les lettres ch dans les mots savants ;",
        "entendre le son s derrière la lettre x dans les nombres ;",
        "entendre le son ch derrière les lettres sh et sch ;",
        "retrouver un mot au dictionnaire quand on ne l'a qu'entendu.",
    ], notes="Le quatrième objectif est le vrai enjeu pratique : un mot entendu qu'on "
             "écrit comme on l'entend ne se retrouve jamais.")

    d.declencheur(
        'Observation', "Écoute ces quatre mots. Comment les écrirais-tu ?",
        pistes=[
            "cro-no-lo-gie · or-kestre · flach-back · ché-ma",
            "Écris-les comme tu les entends, sans regarder.",
            "Compare ensuite avec l'écriture réelle.",
            "Lequel t'a le plus surpris ?",
        ],
        notes="Faire écrire avant de montrer. La surprise fait tout le travail : un "
              "élève qui a écrit « cronologie » de sa main retient la règle mieux "
              "qu'un élève à qui on l'explique.")

    d.tableau('Analyse', "Trois cas, et rien de plus",
              ['Les lettres', 'Ce qu\'on entend, et où'],
              [["ch", "le son k, dans les mots savants : chronologie, orchestre, chorale"],
               ["x", "le son s, dans quelques nombres : dix, six, soixante"],
               ["sh, sch", "le son ch, dans les mots empruntés : flash-back, schéma"],
               ["ch, ailleurs", "le son ch normal : chercher, chaque, chose"]],
              cle=0,
              note="La quatrième ligne est la règle ; les trois premières sont les exceptions.",
              notes="Diapositive à photographier. Insister sur la quatrième ligne : le "
                    "son k est l'exception, pas la règle. Sans elle, des élèves se "
                    "mettent à dire « kercher ».")

    d.regle("Les mots savants gardent leur k",
            "Presque tous les ch qui se disent k viennent du grec.",
            precision="Chronologie, orchestre, chorale, chorégraphie, psychologie, "
                      "technique : ce sont des mots d'école, de musique et de "
                      "sciences. Ils sont peu nombreux et ils s'apprennent un par "
                      "un — mais ils reviennent sans arrêt dès qu'on parle d'art.",
            notes="Diapositive à photographier. Faire chercher au groupe d'autres mots "
                  "de la même famille : chœur, archéologie, chaos. Le repère du « y » "
                  "ou du « ph » à côté fonctionne souvent.")

    d.regle("Le x de dix, six et soixante",
            "Ce x se dit comme un s, et il change encore selon ce qui suit.",
            precision="Dix, tout seul, se dit « dis ». Dix minutes se dit « di "
                      "minutes ». Dix ans se dit « diz ans ». Trois formes pour un "
                      "seul mot, et personne ne vous reprendra si vous vous trompez : "
                      "ce qui compte est de reconnaître les trois à l'écoute.",
            notes="Diapositive à photographier. Rassurer explicitement : la production "
                  "parfaite n'est pas demandée ici, seulement la reconnaissance.")

    d.pratique('Phonétique', "Quel son entends-tu ?",
               "Écoutez chaque mot, puis écrivez k, s ou ch.", [
        ("la chronologie", "k"),
        ("un orchestre", "k"),
        ("une chorale", "k"),
        ("dix", "s"),
        ("soixante-dix", "s"),
        ("un flash-back", "ch"),
        ("un schéma", "ch"),
        ("une chorégraphie", "k"),
    ], corrige=True, cols=2,
       notes="Faire écouter deux fois chaque mot avant de laisser répondre. Les "
             "extraits sont dans l'activité interactive, exercice 2 de « Je "
             "découvre ».")

    d.piege("Chercher au dictionnaire le mot tel qu'on l'a entendu",
            "J'ai entendu « cronologie » : je cherche cronologie.",
            "J'ai entendu « cronologie » : j'essaie ch à la place du k.",
            "C'est la conséquence pratique de toute la séance. Un mot entendu qui ne "
            "se trouve pas au dictionnaire n'est presque jamais un mot rare : c'est "
            "presque toujours un mot dont on a deviné l'écriture. Deux essais "
            "suffisent : ch à la place du k, x à la place du s.",
            notes="Faire l'exercice pour de vrai avec un téléphone, en classe. Trente "
                  "secondes, et la règle devient un réflexe.")

    d.cartes("Le réflexe", "Un mot entendu qui ne se trouve pas", [
        ("Essaie ch",
         "le son k dans un mot savant s'écrit souvent ch : chronologie."),
        ("Essaie x",
         "le son s dans un nombre s'écrit souvent x : dix, six, soixante."),
        ("Essaie sh ou sch",
         "le son ch dans un mot court venu d'ailleurs : flash-back, schéma."),
        ("Sinon, demande",
         "trois essais suffisent ; au-delà, c'est plus rapide de demander."),
    ], notes="Quatre gestes, à copier dans le cahier. Le dernier compte : on ne veut "
             "pas d'élèves qui passent dix minutes sur un mot.")

    d.billet(
        "Écris un mot que tu as déjà entendu sans savoir l'écrire.",
        exemples=[
            "Un seul mot suffit.",
            "On les cherchera ensemble à la prochaine séance.",
        ],
        notes="Deux minutes. Ramasser les billets : ils font une liste de mots utiles "
              "propre au groupe, et souvent bien meilleure que celle du manuel.")

    return d.save(dossier)
