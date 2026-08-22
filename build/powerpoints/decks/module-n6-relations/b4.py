# -*- coding: utf-8 -*-
"""B4 · Ce qui était déjà arrivé avant le reste
Bloc B « Défi 1 » · couleur ambre · grammaire · 75 min.
Source : exercices `t1pqp` et `t1ordre` et leurs mini-leçons — le
plus-que-parfait, et les quatre indices qui donnent l'ordre du récit.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Ce qui était déjà arrivé avant le reste",
        chapeau="Le plus-que-parfait n'ajoute aucun évènement. Il en "
                "replace un. C'est le seul temps du français dont le "
                "travail soit de mettre de l'ordre.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 1. Elle referme le bloc : après les "
                  "reprises de B3, les temps. Ce sont les deux fils qui tiennent un "
                  "texte long.")

    d.objectifs([
        "comprendre qu'un plus-que-parfait recule d'un cran dans le passé ;",
        "former le plus-que-parfait avec avoir ou être à l'imparfait ;",
        "accorder le participe passé avec être, comme au passé composé ;",
        "remettre sept évènements dans l'ordre sans que le texte le donne.",
    ], notes="Le programme demande seulement de comprendre ce temps. On le fait "
             "quand même écrire une fois : c'est le meilleur moyen de le reconnaître "
             "ensuite.")

    d.declencheur(
        'Observation', "Quand tu racontes ta semaine, commences-tu par le début ?",
        pistes=[
            "Ou par ce qui t'a le plus marqué ?",
            "Comment fais-tu comprendre qu'une chose est arrivée avant ?",
            "Dans ta langue, y a-t-il un temps pour dire c'était déjà fait ?",
            "Qu'arrive-t-il si l'ordre se perd ?",
        ],
        notes="Presque toutes les langues ont un moyen de reculer d'un cran. Faire "
              "nommer celui de deux ou trois langues du groupe avant de donner le "
              "français.")

    d.tableau('Analyse', "Deux passés, deux moments",
              ['La phrase', 'Ce qu\'elle place'],
              [["Il a vendu la maison", "la vente au moment dont on parle"],
               ["Il avait vendu la maison", "la vente avant le moment dont on parle"],
               ["Elle est arrivée", "l'arrivée au moment dont on parle"],
               ["Elle était arrivée", "l'arrivée avant ce moment"],
               ["Il n'avait pas encore repris", "le retour au travail après ce moment"]],
              cle=0,
              note="Auxiliaire à l'imparfait plus participe passé : rien d'autre à retenir.",
              notes="Diapositive à photographier. Faire lire les paires à voix haute, "
                    "deux élèves en alternance : la différence de sens s'entend.")

    d.regle("Kadiatou était arrivée depuis un mois quand il est tombé",
            "Une date qui n'est écrite nulle part, et qu'on peut pourtant calculer.",
            precision="L'accident est en novembre. Le plus-que-parfait place l'arrivée "
                      "un mois avant : octobre. Personne ne l'a écrit. C'est le temps "
                      "du verbe, et lui seul, qui donne la date — et qui explique "
                      "pourquoi Kadiatou a pu aider la famille.",
            notes="Diapositive à photographier. C'est l'exemple qui fait comprendre à "
                  "quoi sert ce temps : il porte une information que le texte ne dit "
                  "pas autrement.")

    d.pratique('Grammaire', "Mettez le verbe au plus-que-parfait",
               "Le verbe est entre parenthèses. Attention à l'auxiliaire.", [
        ("Quand Ousmane a écrit en avril, ils (vendre) ... déjà la maison.", "avaient vendu"),
        ("Kadiatou (arriver) ... depuis un mois quand l'accident est arrivé.", "était arrivée"),
        ("Marisol (lire) ... le courriel deux fois avant d'en parler.", "avait lu"),
        ("Assia (naître) ... trois mois avant le déménagement.", "était née"),
        ("Ils (s'installer) ... dans le nouveau logement quand l'automne a commencé.", "s'étaient installés"),
        ("Ghislain n'(voir) ... jamais Kadiatou avant ce vendredi-là.", "avait jamais vu"),
    ], corrige=True,
       notes="Faire dire l'auxiliaire avant la forme complète. La question à poser "
             "chaque fois : avoir ou être ? Le reste suit tout seul.")

    d.piege('Auxiliaire', "Il avait tombé de la plateforme",
            "Il était tombé de la plateforme",
            "Les verbes qui prennent être au passé composé le gardent au "
            "plus-que-parfait : tomber, arriver, partir, venir, rester, et tous les "
            "verbes pronominaux. Rien de nouveau à apprendre — la liste est celle "
            "qu'on connaît déjà.",
            notes="Rassurer : il n'y a pas deux listes à retenir. Celle du passé "
                  "composé sert telle quelle.")

    d.tableau('Méthode', "Quatre indices donnent l'ordre",
              ['L\'indice', 'Un exemple du courriel'],
              [["Une date", "le 14 mars, en juin, le samedi 12"],
               ["Une durée", "depuis un mois, trois mois sans marcher"],
               ["Un plus-que-parfait", "on l'avait déjà vendue"],
               ["Un verbe en re-", "il est retourné travailler : il y travaillait déjà"]],
              cle=0,
              note="Le dernier paragraphe d'un courriel n'est presque jamais le dernier évènement.",
              notes="Diapositive à photographier. Le quatrième indice est le plus "
                    "discret et le plus rentable : un simple préfixe place un "
                    "évènement dans le temps.")

    d.billet(
        "Écris une phrase avec un plus-que-parfait, sur ta propre semaine.",
        exemples=[
            "Exemple : Quand je suis arrivé au cours, j'avais déjà déjeuné.",
            "Souligne l'auxiliaire.",
        ],
        notes="Deux minutes. Fin du Défi 1 : annoncer le Défi 2, où il faudra décrire "
              "quelqu'un assez bien pour qu'un inconnu le reconnaisse.")

    return d.save(dossier)
