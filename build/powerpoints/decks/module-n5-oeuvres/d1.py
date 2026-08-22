# -*- coding: utf-8 -*-
"""D1 · Moi, ce qui m'a touchée, c'est le silence
Bloc D « Défi 3 · Dire ce qu'on en pense » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3a` et `t3fait`.
"""
import pathlib

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-oeuvres/images/')


def photo(nom):
    """La photo si elle est sur le disque, None sinon — voir a1.py."""
    p = pathlib.Path(IMG + nom)
    return str(p) if p.exists() else None


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Moi, ce qui m'a touchée, c'est le silence",
        chapeau="Le soir du club. Mai donne son avis, Karim n'est pas "
                "d'accord, et personne ne se fâche. C'est là que le module "
                "se joue : « c'est bon » n'apprend rien à personne.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 3, et la plus importante du module. Ouvrir "
                  "en demandant au groupe de dire en un mot ce qu'il a pensé du "
                  "dernier film qu'il a vu. Les réponses seront « bon », « pas bon », "
                  "« correct ». Ne rien commenter : c'est le point de départ.")

    d.objectifs([
        "remplacer « c'est bon » par un adjectif qui dit quoi ;",
        "mettre une raison derrière chaque jugement ;",
        "distinguer un fait vérifiable d'un avis qui vous appartient ;",
        "répondre à quelqu'un qui pense autrement sans le contredire.",
    ])

    d.declencheur(
        'Observation', "Que se passe-t-il dans cette salle ?",
        image=photo('salle-du-fond.jpg'),
        pistes=[
            "Combien de personnes, et disposées comment ?",
            "Qu'est-ce qu'on fait quand quelqu'un parle et qu'on n'est pas d'accord ?",
            "Est-ce qu'un désaccord est un problème, ici ?",
            "Qu'est-ce qui vous ferait peur, à la place de Mai ?",
        ],
        notes="La troisième question est celle qui compte. Beaucoup d'élèves viennent "
              "de cultures où contredire quelqu'un en public est impoli ; le club "
              "est un endroit où ça ne l'est pas, à condition de dire pourquoi.")

    d.dialogue('Dialogue · 1 de 4', "Expliquez-moi ça", [
        ("GILBERTE", "Alors, Mai. Qu'est-ce qui vous a le plus touchée là-dedans ?", True),
        ("MAI", "Moi, ce qui m'a touchée, c'est le silence entre les deux sœurs.", True),
        ("GILBERTE", "Le silence. Expliquez-moi ça.", True),
        ("MAI", "Elles ne se disent presque rien, et on comprend tout quand même.", True),
    ], consigne="Écoutez deux fois avant de lire le texte.",
       notes="« Expliquez-moi ça » est la question de l'animatrice tout au long du "
             "dialogue. La faire remarquer : au club, un avis sans raison appelle "
             "toujours cette question-là.")

    d.dialogue('Dialogue · 2 de 4', "C'est vrai que c'est lent", [
        ("KARIM", "Moi, franchement, j'ai trouvé ça lent. Il ne se passe rien pendant cent pages.", True),
        ("MAI", "C'est vrai que c'est lent. Par contre, c'est justement ce que j'ai aimé.", True),
        ("KARIM", "Aimé parce que c'est lent ? Expliquez-moi ça, vous aussi.", True),
        ("MAI", "Parce que le temps du livre est le temps du village. On attend avec elles.", True),
    ], notes="Le mouvement en deux temps de Mai — « c'est vrai que », puis « par "
             "contre » — est le cœur de la séance. L'écrire au tableau et le faire "
             "répéter avant d'aller plus loin.")

    d.dialogue('Dialogue · 3 de 4', "Vous le conseilleriez à qui ?", [
        ("GILBERTE", "Quelle belle façon de le dire. Vous le conseilleriez à qui ?", True),
        ("MAI", "À quelqu'un qui a quitté un pays. Il va reconnaître quelque chose.", True),
        ("KARIM", "Ça, ça me parle plus que « c'est bon ».", True),
        ("MAI", "« C'est bon », ça ne dit rien. Il fallait que je trouve mieux.", True),
    ], notes="La recommandation adressée à quelqu'un de précis est ce que les gens "
             "retiennent d'une présentation. Ce n'est plus un jugement : c'est une "
             "adresse.")

    d.dialogue('Dialogue · 4 de 4', "Deux avis, deux raisons", [
        ("KARIM", "Bon. Je vais le lire. Mais je maintiens que c'est lent.", True),
        ("MAI", "Vous avez le droit. Vous me direz jeudi prochain.", True),
        ("GILBERTE", "Voilà. Deux avis, deux raisons, et personne ne s'est fâché.", True),
        ("MAI", "C'est la première fois que je parle deux minutes sans m'arrêter.", True),
    ], notes="La dernière réplique est celle du module entier. La lire à voix haute "
             "et s'arrêter là : c'est exactement ce qu'on demandera aux élèves en E1.")

    d.regle("« C'est bon » ne dit rien",
            "Émouvant. Lent. Drôle. Dur. Prévisible. Surprenant. Reposant.",
            precision="Un seul adjectif précis vaut trois phrases vagues — il dit ce "
                      "qui est bon, et pour qui. Et derrière l'adjectif, toujours une "
                      "raison : sans elle, l'autre ne peut rien faire de ce que vous "
                      "venez de dire.",
            notes="Diapositive à photographier. Faire chercher au groupe cinq "
                  "adjectifs de plus et les écrire à côté. Les élèves en connaissent "
                  "plus qu'ils n'en emploient.")

    d.piege("Contredire de front",
            "Non, ce n'est pas lent du tout.",
            "C'est vrai que c'est lent. Par contre, c'est ce qui m'a plu.",
            "Personne ne change d'avis quand on lui dit qu'il a tort ; tout le monde "
            "écoute quand on lui donne raison sur un point d'abord. On accorde ce "
            "qui est juste, puis on tourne.",
            notes="Faire jouer l'échange à deux, debout, trois fois : l'un affirme, "
                  "l'autre accorde puis tourne, et on échange. C'est le seul exercice "
                  "de la séance qui se fait entièrement à l'oral.")

    d.tableau('Analyse', "Un fait, ou un avis ?",
              ["La phrase", "Ce que c'est"],
              [["Le roman compte trois cents pages.", "un fait : ça se vérifie"],
               ["La fin est un peu prévisible.", "un avis : moi, j'ai deviné"],
               ["La série a huit épisodes.", "un fait"],
               ["Il ne se passe rien pendant cent pages.", "un avis"]],
              cle=1,
              note="Les adjectifs sont presque toujours des avis, même quand ils "
                   "sonnent comme des constats.",
              notes="Diapositive à photographier. Le test est simple : deux personnes "
                    "qui vérifient trouvent-elles le même résultat ? Si oui, c'est un "
                    "fait.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Relisez le dialogue du club, puis répondez.", [
        ("Ce qui a touché Mai, c'est le silence entre les deux sœurs.", "vrai"),
        ("Karim a trouvé le livre trop rapide.", "faux — il l'a trouvé lent"),
        ("Mai accorde à Karim que le livre est lent.", "vrai"),
        ("Mai raconte la fin du roman à Gilberte.", "faux — c'est la règle du club"),
        ("Karim change d'avis et trouve le livre rapide.", "faux — il maintient"),
        ("Gilberte trouve normal que deux avis se contredisent.", "vrai"),
    ], corrige=True,
       notes="Six des huit énoncés de l'exercice `t3a`. Les faire d'abord sans le "
             "texte sous les yeux.")

    d.pratique('Écoute et réponds', "Fait ou avis ?",
               "Pour chaque phrase, dites si elle se vérifie ou si elle vous "
               "appartient.", [
        ("L'histoire se passe dans un village au bord de la mer.", "un fait"),
        ("C'est le livre le plus émouvant que j'ai lu cette année.", "un avis"),
        ("L'album est le premier tome d'une série de quatre.", "un fait"),
        ("Je trouve que le dessin est plus fort que le texte.", "un avis"),
        ("On garde une bande dessinée trois semaines à la bibliothèque.", "un fait"),
        ("Ce personnage-là m'a agacée du début à la fin.", "un avis"),
    ], corrige=True, cols=2,
       notes="Six des dix items de `t3fait`. Faire remarquer les mots qui annoncent "
             "un avis — je trouve que, selon moi, à mon avis — et qui évitent tout "
             "malentendu.")

    d.billet(
        "Écrivez ce que vous avez pensé de votre œuvre, sans employer « bon » ni « intéressant ».",
        exemples=[
            "Un adjectif précis, puis une raison derrière.",
            "Écrivez aussi une chose que vous avez moins aimée : elle servira en D2.",
        ],
        notes="Ramasser les billets et les rendre en D2 : ils sont le brouillon de "
              "l'avis de la présentation orale.")

    return d.save(dossier)
