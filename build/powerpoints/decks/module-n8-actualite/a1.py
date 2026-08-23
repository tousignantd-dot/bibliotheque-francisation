# -*- coding: utf-8 -*-
"""A1 · Onze hectares, et deux façons de le dire
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`, six premiers mots de `FC_CARDS`.
"""
from theme import Deck

import pathlib

# Chemin déduit du fichier, jamais écrit en dur : le dépôt se construit aussi
# depuis un worktree git, où un chemin absolu vers la copie principale
# pointerait sur des images qui n'y sont pas encore.
IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n8-actualite' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Deux journaux, deux soirées, aucun menteur",
        chapeau="Tout le monde connaît la nouvelle et personne n'en conteste "
                "les faits. Ce module ne travaille pas la nouvelle : il "
                "travaille le désaccord.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : "
                  "avez-vous déjà lu deux articles sur la même chose et eu "
                  "l'impression de lire deux histoires ? Presque tous disent oui, "
                  "et presque tous concluent que l'un des deux mentait. C'est "
                  "exactement la croyance que la séance va défaire.")

    d.objectifs([
        "suivre un dossier municipal local et en nommer les étapes ;",
        "expliquer comment deux comptes rendus honnêtes peuvent différer ;",
        "comprendre ce qu'est un registre référendaire et à quoi il sert ;",
        "employer les six premiers mots du dossier : un éditorial, une chronique, un communiqué.",
    ], notes="Le deuxième objectif est le cœur du module. L'écrire au tableau et "
             "l'y laisser : les quatre séances du bloc A y reviennent.")

    d.declencheur(
        'Observation', "Où prenez-vous vos nouvelles locales ?",
        image=IMG + 'comptoir-bibliotheque.jpg',
        pistes=[
            "Est-ce que vous lisez le journal de votre ville ou de votre quartier ?",
            "Savez-vous ce que le conseil municipal a décidé le mois dernier ?",
            "Quand deux sources se contredisent, laquelle croyez-vous, et pourquoi ?",
            "Avez-vous déjà assisté à une réunion publique ici ?",
        ],
        notes="Question sans mauvaise réponse. Beaucoup d'élèves suivent l'actualité "
              "de leur pays d'origine et pas celle de leur ville : le dire sans "
              "reproche, c'est le point de départ du module.")

    d.dialogue('Dialogue 1 de 3', "Une affiche oubliée sur le comptoir", [
        ("MIRELA", "Madame Sauvé ? Vous avez oublié votre affiche sur le comptoir des retours.", True),
        ("RÉGINE", "Merci. J'en ai posé quarante ce matin et j'en oublie une sur trois. Et appelez-moi Régine, on se voit toutes les semaines.", True),
        ("MIRELA", "Alors Régine. J'ai lu le journal hier soir et je n'ai pas tout compris. Le boisé est vendu, ou pas encore ?", True),
        ("RÉGINE", "Pas encore. Le conseil a adopté le règlement lundi, à quatre voix contre trois. Il reste l'assemblée de consultation, puis le registre.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer le passage au tutoiement, offert par la plus âgée des "
             "deux. Le reste du module vouvoie : la tribune et la lettre au journal "
             "sont au vouvoiement strict, et c'est un savoir du niveau 8.")

    d.dialogue('Dialogue 2 de 3', "Le mot que personne n'explique", [
        ("MIRELA", "Le registre, c'est quoi exactement ? Le mot revient partout et personne ne l'explique.", True),
        ("RÉGINE", "C'est un cahier qu'on ouvre à l'hôtel de ville pendant une journée. Les personnes habiles à voter y écrivent leur nom si elles veulent un référendum.", True),
        ("MIRELA", "Et vous en êtes loin ?", True),
        ("RÉGINE", "Il nous faut sept cent quatre-vingt-douze signatures. On en a promis un peu plus de trois cents. C'est mince.", True),
    ], notes="Poser le chiffre au tableau : 792 demandées, 312 promises, six jours. "
             "Il revient dans tout le module, jusqu'à la lettre du bloc E.")

    d.dialogue('Dialogue 3 de 3', "Lequel des deux ment ?", [
        ("MIRELA", "Le Courant parle d'un terrain vague, La Vigie parle d'un boisé mature. Lequel des deux ment ?", True),
        ("RÉGINE", "Aucun des deux, et c'est ça qui est difficile. Il y a quatre hectares d'érables de soixante ans, et il y a aussi trois hectares de remblai où plus rien ne pousse.", True),
        ("MIRELA", "Donc les deux disent vrai, et je n'apprends rien.", True),
        ("RÉGINE", "Vous apprenez ce que chacun trouve important. C'est déjà de l'information, à condition de lire les deux.", True),
    ], notes="C'est la thèse du module, en quatre répliques. La dernière est celle "
             "qu'il faut faire redire par un élève, à voix haute, avant de passer "
             "à la suite.")

    d.regle("Deux journaux honnêtes peuvent raconter deux soirées",
            "Ce n'est pas qu'un des deux ment : c'est qu'ils n'ont pas gardé "
            "les mêmes phrases. Chacun décrit sa moitié de la vérité, et "
            "celui qui n'en lit qu'un croit avoir tout lu.",
            precision="Le boisé Sainte-Perpétue fait onze hectares : quatre d'érables "
                      "de soixante ans, trois de remblai où plus rien ne pousse depuis "
                      "l'ancienne cour de voirie. « Boisé mature » et « terrain vague » "
                      "sont vrais tous les deux, sur des moitiés différentes.",
            notes="Diapositive à photographier. Question fréquente : « alors comment "
                  "savoir ? » Réponse honnête : en lisant les deux, ce qui coûte huit "
                  "minutes. Il n'y a pas de méthode plus courte.")

    d.tableau('Analyse', "Le dossier en quatre étapes",
              ['Étape', "Ce qui s'y décide"],
              [["La séance du conseil",
                "le règlement est adopté ou non, ici par quatre voix contre trois"],
               ["L'assemblée publique de consultation",
                "la Ville explique, le public parle, rien ne se vote"],
               ["Le registre référendaire",
                "un cahier ouvert une journée : on compte ceux qui veulent un référendum"],
               ["Le référendum, s'il a lieu",
                "la population tranche, et la décision tient beaucoup plus longtemps"]],
              cle=0,
              notes="Diapositive à photographier. Insister sur la deuxième : à une "
                    "assemblée de consultation, tout le monde a le droit de parler et "
                    "presque personne ne le fait. Plusieurs élèves croient l'inverse.")

    d.vocabulaire('Vocabulaire', "Six mots pour commencer", [
        ("un éditorial", "Le texte où un journal dit lui-même ce qu'il pense d'une question."),
        ("une chronique", "Un texte ou une capsule signés, où une même personne donne son avis chaque semaine."),
        ("le courrier des lecteurs", "La page d'un journal où le public peut faire publier son opinion."),
        ("un communiqué", "Le texte qu'un organisme envoie aux médias pour annoncer sa version d'une nouvelle."),
        ("une manchette", "Le grand titre du haut de la page, celui qu'on lit même sans lire l'article."),
        ("une radio communautaire", "Une petite station locale sans but lucratif, animée en partie par des bénévoles."),
    ], notes="Faire répéter avec l'article. Signaler tout de suite la différence "
             "entre éditorial et chronique : l'éditorial engage le journal, la "
             "chronique n'engage que la personne qui la signe.")

    d.regle("Presque tout part du même communiqué",
            "Un hebdomadaire local n'a pas quatre journalistes. Quand une "
            "ville envoie son communiqué, on le retrouve dans les deux "
            "journaux, souvent dans le même ordre. Ce qui n'y est pas n'est "
            "nulle part.",
            precision="Le terrain vacant derrière l'aréna n'apparaît dans aucun des "
                      "deux articles. Non pas parce qu'on l'a caché : parce qu'il "
                      "n'était pas dans le communiqué de la Ville. Sortir ce qui n'y "
                      "est pas, c'est le travail d'un comité de citoyens.",
            notes="Diapositive à photographier. C'est ici que les élèves comprennent "
                  "pourquoi une absence est une information. On y revient au bloc B.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le conseil a adopté le règlement par quatre voix contre trois.", "vrai"),
        ("Le boisé est déjà vendu au promoteur.", "faux - il reste la consultation et le registre"),
        ("Le registre est un cahier ouvert une journée à l'hôtel de ville.", "vrai"),
        ("Le comité a déjà réuni les 792 signatures nécessaires.", "faux - un peu plus de 300 sont promises"),
        ("Selon Régine, un des deux journaux a écrit quelque chose de faux.", "faux - aucun des deux ne ment"),
        ("Le comité s'oppose au principe même du logement abordable.", "faux - il conteste l'endroit, pas le projet"),
        ("Il existe un autre terrain municipal, déjà déboisé, derrière l'aréna.", "vrai"),
        ("À l'assemblée, seuls les membres d'un comité ont le droit de parler.", "faux - tout le monde a le droit"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le cinquième "
             "est le plus important de la séance : c'est celui qui distingue ce "
             "module du niveau 7, où l'on démasquait encore quelqu'un.")

    d.billet(
        "Cherchez une nouvelle de votre ville et trouvez-en deux comptes rendus.",
        exemples=[
            "Notez un mot que l'un emploie et que l'autre n'emploie pas.",
            "Notez un chiffre présent d'un seul côté.",
        ],
        notes="Devoir concret et faisable en dix minutes. Les deux notes servent "
              "d'amorce au bloc B : chaque élève arrive avec un écart observé "
              "par lui-même, pas par le module.")

    return d.save(dossier)
