# -*- coding: utf-8 -*-
"""C2 · Nommer ce qu'on montre du doigt
Bloc C « Défi 2 · Lire une bande dessinée » · couleur framboise · 75 min.
Source : exercice `t2mots`, mini-leçon `t2mots`.
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
        code='C2', section='framboise',
        titre="Nommer ce qu'on montre du doigt",
        chapeau="La bande dessinée est le seul art dont le vocabulaire "
                "s'apprend en une minute, parce que chaque mot désigne "
                "quelque chose qu'on voit sur la page. Encore faut-il "
                "savoir en parler à quelqu'un qui n'a pas la page sous les "
                "yeux.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire appliqué. Prévoir un album par deux élèves : la "
                  "séance ne fonctionne pas sans objet à montrer. Si la bibliothèque de "
                  "l'école n'en a pas, imprimer trois planches libres de droits ou "
                  "emprunter au réseau municipal la semaine d'avant.")

    d.objectifs([
        "associer chaque mot à ce qu'il désigne sur la page ;",
        "décrire une case à quelqu'un qui ne la voit pas ;",
        "dire ce que fait une bulle, et ce que sa forme raconte ;",
        "reconnaître une onomatopée et dire à quoi sert sa taille.",
    ], notes="Le deuxième objectif est le plus exigeant : décrire une image sans la "
             "montrer est un exercice de production orale complet, et c'est exactement ce "
             "que l'élève devra faire au club.")

    d.declencheur(
        'Observation', "Une case, une bulle, une planche, une onomatopée : "
                       "montrez-les sur l'album ouvert devant vous.",
        image=photo('planche-ouverte.jpg'),
        pistes=[
            "Combien de cases y a-t-il sur cette planche ?",
            "Y a-t-il une case sans un seul mot ? Qu'est-ce qu'elle montre ?",
            "Trouvez une bulle de pensée. Comment l'avez-vous reconnue ?",
            "Cherchez une onomatopée. De quel bruit s'agit-il ?",
        ],
        notes="Deux par deux, album ouvert, cinq minutes. Puis mise en commun : chaque "
              "équipe montre une chose et la nomme. C'est le meilleur moment de la "
              "séance et il ne demande aucune préparation.")

    d.cartes("Quatre mots, quatre choses", "Ce que chacun désigne exactement", [
        ("Une case",
         "Le petit cadre avec un dessin dedans. Elle peut n'avoir aucun mot."),
        ("Une bulle",
         "La forme blanche qui porte les paroles. Sa pointe dit qui parle."),
        ("Une planche",
         "La page complète, avec toutes ses cases. Une cinquantaine par album."),
        ("Une onomatopée",
         "Un bruit écrit en grosses lettres, hors des bulles : BANG, TOC, VLAN."),
    ], notes="Insister sur la première carte : beaucoup de cases n'ont aucun texte — un "
             "visage, une main, une porte fermée — et ce sont souvent les plus fortes. "
             "Ce sont celles qu'on décrit à voix haute quand on présente l'album.")

    d.regle("Le dessin porte la moitié de l'histoire",
            "Un lecteur qui ne lit que les bulles ne comprend pas pourquoi les "
            "personnages réagissent.",
            precision="La case porte ce qui se voit, la bulle ce qui se lit, et une "
                      "bonne bande dessinée met la moitié de l'histoire dans chacune. "
                      "C'est pour ça qu'on ne peut pas la raconter en lisant seulement "
                      "le texte — et pour ça qu'elle se lit plus lentement qu'elle n'en "
                      "a l'air.",
            notes="Diapositive à photographier. Rassurer les élèves qui trouvent qu'ils "
                  "lisent trop vite une bande dessinée : c'est le signe qu'ils sautent le "
                  "dessin. Leur faire relire une planche en ne regardant que les images.")

    d.tableau('Ce que la forme raconte', "La bulle, sa pointe et son contour",
              ['Ce qu\'on voit', 'Ce que ça veut dire'],
              [["Une pointe ordinaire", "Le personnage parle. Les autres l'entendent."],
               ["Une pointe en petits ronds", "Il pense. Personne ne l'entend."],
               ["Un contour en dents de scie", "Il crie, ou la voix sort d'un appareil."],
               ["Une bulle sans pointe", "Une voix de narrateur, hors de la scène."],
               ["Pas de bulle du tout", "Le dessin raconte seul. Souvent le plus fort."]],
              cle=1,
              notes="Faire chercher chacune des cinq formes dans les albums. Les trois "
                    "premières se trouvent toujours ; la quatrième et la cinquième "
                    "demandent de feuilleter, et c'est justement l'exercice de lecture "
                    "qu'on veut.")

    d.pratique('Reconnaissance', "De quoi parle-t-on ?",
               "Case, bulle, planche ou onomatopée ?", [
        ("Le petit cadre qui contient un dessin.", "une case"),
        ("La forme blanche avec une pointe, qui contient des paroles.", "une bulle"),
        ("La page complète, avec toutes ses cases.", "une planche"),
        ("Un bruit écrit en grosses lettres, en dehors des bulles.", "une onomatopée"),
        ("On y lit d'abord celle qui est la plus haute et la plus à gauche.", "une bulle"),
        ("Elle peut ne contenir aucun mot : un visage, une porte fermée.", "une case"),
        ("Il y en a une cinquantaine dans un album ordinaire.", "une planche"),
        ("BANG, DRING, VLAN, TOC TOC.", "une onomatopée"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice `t2mots` du module interactif, à quatre tuiles. La "
             "cinquième ligne est le piège : on parle de la bulle, pas de la case, parce "
             "que c'est d'un ordre de lecture qu'il s'agit.")

    d.piege("Appeler « bulle » ce qui est une case",
            "Regarde la bulle du haut, on voit toute la ville.",
            "Regarde la case du haut, on voit toute la ville.",
            "La bulle contient des mots ; la case contient un dessin. Si ce que vous "
            "montrez est carré et dessiné, c'est une case. Une bulle ne peut pas "
            "exister en dehors d'une case.",
            notes="La faute est constante au début et elle se corrige vite, à condition de "
                  "la reprendre chaque fois. Pendant tout le défi, corriger le mot sans "
                  "interrompre l'idée : « la case, oui — continue ».")

    d.pratique('À l\'oral', "Décrivez une case à quelqu'un qui ne la voit pas",
               "Deux par deux. L'un décrit, l'autre dessine au crayon.", [
        ("Dites d'abord ce qu'on voit dans la case, sans nommer l'histoire.",),
        ("Dites s'il y a une bulle, et où sa pointe va.",),
        ("Dites s'il y a une onomatopée, et quelle place elle prend.",),
        ("Comparez le dessin de votre voisin avec la vraie case.",),
    ], notes="Exercice long — prévoir vingt minutes — mais c'est le cœur de la séance. Le "
             "dessin du voisin n'a aucune importance en soi : ce qui compte, c'est ce qui "
             "manquait à la description, et le groupe le voit tout seul.")

    d.billet(
        "Décrivez en trois phrases la case qui vous a le plus frappé.",
        exemples=[
            "Employez au moins deux des quatre mots : case, bulle, planche, onomatopée.",
            "Ne racontez rien de l'histoire — décrivez seulement ce qui se voit.",
        ],
        notes="La seconde consigne relie le défi 2 au défi 1 : décrire n'est pas raconter, "
              "et l'on peut parler longtemps d'une œuvre sans rien dévoiler. Garder deux "
              "ou trois billets pour ouvrir la séance C3.")

    return d.save(dossier)
