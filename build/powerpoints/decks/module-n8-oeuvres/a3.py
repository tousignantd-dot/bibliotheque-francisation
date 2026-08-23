# -*- coding: utf-8 -*-
"""A3 · Les mots de l'interprétation
Bloc A « Je découvre » · couleur framboise · vocabulaire · 75 min.
Source : `FC_CARDS` (dix-sept cartes) et l'exercice `prVocab`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Les mots de l'interprétation",
        chapeau="Dix-sept mots, et pas un seul ne se photographie. C'est un "
                "vocabulaire d'opérations, pas d'objets : ce qu'on fait avec "
                "un texte, et non ce qu'on y trouve.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Prévenir le groupe : ces mots-là ne "
                  "s'illustrent pas, et c'est normal. Chacun se comprend par un "
                  "exemple tiré d'une œuvre, jamais par une image.")

    d.objectifs([
        "nommer les trois opérations : fait, interprétation, jugement ;",
        "employer les mots de l'écran : une fin ouverte, un plan fixe, un indice ;",
        "employer les mots du livre : une nouvelle, un recueil, une strophe ;",
        "employer les mots de la discussion : une critique, un argument.",
    ], notes="Quatre familles, une par quart d'heure. Ne pas mélanger : le groupe "
             "retient mieux quatre listes courtes qu'une longue.")

    d.declencheur(
        'Observation', "Comment appelle-t-on ce qui est écrit et ce qui se devine ?",
        pistes=[
            "« On avait commencé sans elle » : qu'est-ce qui est écrit ?",
            "Et qu'est-ce que vous comprenez, qui n'est pas écrit ?",
            "Est-ce que tout le monde comprend la même chose ?",
            "Comment appelle-t-on ce qui se comprend sans être dit ?",
        ],
        notes="La quatrième question amène « l'implicite », le mot le plus abstrait du "
              "dossier. L'installer ici, avec cet exemple-là : il servira toute la "
              "semaine.")

    d.vocabulaire('Vocabulaire · 1 de 3', "Comprendre une œuvre", [
        ("une interprétation", "Ce qu'une personne comprend d'une œuvre, au-delà de ce qui y est montré."),
        ("une lecture", "Une façon défendable de comprendre une œuvre, appuyée sur des détails précis."),
        ("l'implicite", "Ce qu'un texte ou une image laisse entendre sans jamais le dire."),
        ("un fait vérifiable", "Ce que tout le monde peut constater dans l'œuvre en la revoyant."),
        ("un jugement de valeur", "Une phrase qui dit si c'est bon ou mauvais, et non ce qui se passe."),
        ("un indice", "Un détail qu'une personne met en avant pour appuyer ce qu'elle comprend."),
    ], notes="Faire répéter avec l'article. « Une lecture » a ici un sens que les "
             "élèves ne connaissent pas : ce n'est pas l'acte de lire, c'est une façon "
             "de comprendre. Le dire explicitement.")

    d.vocabulaire('Vocabulaire · 2 de 3', "L'écran et la page", [
        ("une fin ouverte", "Une fin qui donne tout ce qu'il faut, mais qui ne conclut pas à votre place."),
        ("un plan fixe", "Un moment de film où la caméra ne bouge pas du tout."),
        ("un dénouement", "Le moment où l'histoire se règle, juste avant qu'elle s'arrête."),
        ("une nouvelle littéraire", "Un récit très court, souvent quelques pages, qui s'arrête net."),
        ("un recueil", "Un livre qui rassemble plusieurs textes courts du même auteur."),
        ("une strophe", "Un groupe de vers séparé des autres par une ligne blanche, dans un poème."),
    ], notes="« Une nouvelle » est un faux ami avec lui-même : la nouvelle du "
             "téléjournal et la nouvelle littéraire. Le préciser, sinon la confusion "
             "dure jusqu'en C2.")

    d.vocabulaire('Vocabulaire · 3 de 3', "En parler, en écrire", [
        ("une métaphore", "Une image qui remplace un mot par un autre, sans dire qu'elle compare."),
        ("le narrateur", "La voix qui raconte dans un texte, jamais tout à fait la personne qui écrit."),
        ("une critique", "Un texte de journal qui rend compte d'une œuvre et en dit du bien ou du mal."),
        ("un argument", "La raison précise qu'on donne pour appuyer ce qu'on avance."),
        ("le courrier des lecteurs", "La page d'un journal où le public envoie ses réponses signées."),
    ], notes="Cinq mots seulement dans cette famille : ce sont ceux du bloc D et du "
             "bloc E. « Le narrateur n'est pas l'auteur » se dira trois fois d'ici "
             "la fin ; c'est la première.")

    d.regle("Un mot abstrait s'apprend par un exemple, pas par une image",
            "Une ironie, une concession, un implicite ne se photographient pas.",
            precision="Pour chacun de ces mots, gardez en tête une phrase du module "
                      "plutôt qu'une définition. « L'implicite », c'est « on avait "
                      "commencé sans elle ». « Un indice », c'est la corde restée "
                      "attachée. La phrase se retient, la définition s'oublie.",
            notes="Diapositive à photographier. C'est aussi pourquoi les cartes du "
                  "module n'ont pas d'image : une photo générique de bibliothèque "
                  "derrière « une métaphore » aiderait moins que rien.")

    d.pratique('Pratique', "Le mot et sa définition",
               "Quel mot correspond ?", [
        ("Ce qu'un texte laisse entendre sans le dire.", "l'implicite"),
        ("Un récit de quelques pages qui s'arrête net.", "une nouvelle littéraire"),
        ("Un détail qui appuie ce qu'on comprend.", "un indice"),
        ("La voix qui raconte, dans un texte.", "le narrateur"),
        ("Une fin qui ne conclut pas à votre place.", "une fin ouverte"),
        ("Un groupe de vers séparé par une ligne blanche.", "une strophe"),
    ], corrige=True,
       notes="Exercice `prVocab` du module, en version courte. Le faire à l'oral, sans "
             "écran, puis renvoyer aux cartes mémoire pour le reste.")

    d.pratique('Pratique', "Fait, interprétation ou jugement ?",
               "Nommez l'opération.", [
        ("La corde reste attachée au taquet.", "fait"),
        ("Elle est prisonnière de ce chalet.", "interprétation"),
        ("Cette dernière scène est ratée.", "jugement"),
        ("Le contremaître l'appelle deux fois Ginette.", "fait"),
        ("Personne n'a retenu son nom en trente et un ans.", "interprétation"),
        ("C'est la plus belle scène de la série.", "jugement"),
    ], corrige=True,
       notes="Reprise du tableau d'A1, avec des phrases neuves. Les élèves qui "
             "hésitent cherchent le verbe : « s'asseoir » se voit, « renoncer » se "
             "déduit, « être raté » se juge.")

    d.billet(
        "Choisissez trois mots de la séance et écrivez une phrase avec chacun, "
        "à propos d'une œuvre que vous connaissez.",
        exemples=[
            "« Le narrateur de ce livre ne juge personne. »",
            "« La fin est ouverte : on ne sait pas s'il revient. »",
        ],
        notes="Ramasser et relire : les phrases fausses de cette liste-là disent "
              "exactement quel mot n'est pas passé, et il n'y en a jamais plus de "
              "deux.")

    return d.save(dossier)
