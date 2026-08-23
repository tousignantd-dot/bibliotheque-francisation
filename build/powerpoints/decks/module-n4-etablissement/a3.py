# -*- coding: utf-8 -*-
"""A3 · Les seize mots du téléphone et des motifs
Bloc A « Je découvre » · couleur framboise · 75 min. Vocabulaire.
Source du module : `FC_CARDS`, exercices `prVocab`, `prImg`.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n4-etablissement/images/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Les seize mots du téléphone et des motifs",
        chapeau="Seize mots, quatre familles : ce qu'il y a au bout du fil, "
                "ce qu'on laisse comme message, ce qui empêche de venir, et "
                "ce qu'on écrit ensuite. Ce sont les mots du module entier.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. La faire tôt : les trois blocs suivants "
                  "supposent tous ces seize mots connus. Écrire les quatre familles au "
                  "tableau et les laisser affichées jusqu'à la fin de la séance.")

    d.objectifs([
        "nommer les quatre objets du téléphone : la ligne, le clavier, le poste, la boîte vocale ;",
        "employer les mots du message : le signal sonore, les coordonnées ;",
        "choisir entre retard, absence, abandon et empêchement ;",
        "nommer ce qui va sur le papier : une note, un motif, une signature, une copie.",
    ], notes="Le troisième objectif est celui qui compte le plus, et il sera repris "
             "seul en A4. Les trois autres se travaillent aujourd'hui.")

    d.declencheur(
        'Observation', "Quelqu'un téléphone debout dans un escalier. "
                       "Pourquoi là ?",
        image=img('appel-cage-escalier.jpg'),
        pistes=[
            "Où appelez-vous quand vous devez téléphoner au centre ?",
            "Qu'est-ce qui rend un appel difficile : le bruit, la gêne, les mots ?",
            "Qu'est-ce que vous avez sous la main quand vous appelez ?",
            "Est-ce que vous préparez ce que vous allez dire, ou pas ?",
        ],
        notes="La dernière piste ouvre le bloc B. Presque personne ne prépare, et "
              "presque tout le monde reconnaît que ça se sent. Ne pas commenter : "
              "laisser la question ouverte, elle trouvera sa réponse en B1.")

    d.vocabulaire("Famille 1", "Ce qu'il y a au bout du fil", [
        ("la boîte vocale", "Le service qui enregistre votre message quand personne ne décroche."),
        ("un répondeur", "L'appareil ou le service qui répond tout seul."),
        ("le clavier", "Les touches numérotées du téléphone."),
        ("la ligne", "La liaison elle-même : libre, occupée ou coupée."),
    ], notes="Faire répéter avec l'article. « La ligne est occupée » est une phrase "
             "toute faite qu'on entend partout : la faire dire deux fois.")

    d.vocabulaire("Famille 2", "Le message qu'on laisse", [
        ("un poste", "Le numéro à trois chiffres qui mène au téléphone d'une personne."),
        ("le signal sonore", "Le petit son qui dit que l'enregistrement commence."),
        ("un message", "Ce qu'on laisse enregistré pour quelqu'un qui n'était pas là."),
        ("les coordonnées", "Ce qui permet de vous joindre : nom, numéro, courriel."),
    ], notes="« Les coordonnées » est toujours au pluriel et surprend. Le faire "
             "remarquer, et donner l'équivalent simple : « comment on peut vous "
             "joindre ».")

    d.vocabulaire("Famille 3", "Ce qui empêche de venir", [
        ("un retard", "Arriver après l'heure, mais venir quand même."),
        ("une absence", "Manquer un cours en entier, une journée ou plusieurs."),
        ("un abandon", "Arrêter un cours avant la fin, et le dire officiellement."),
        ("un empêchement", "Ce qui survient et vous empêche de venir."),
    ], notes="Ces quatre-là reviennent seuls en A4. Aujourd'hui, se contenter de les "
             "faire prononcer et écrire : les trois premiers portent tous une voyelle "
             "nasale travaillée en A2.")

    d.vocabulaire("Famille 4", "Ce qu'on écrit ensuite", [
        ("une note", "Le court texte écrit et signé qu'on remet pour expliquer."),
        ("un motif", "La raison qu'on écrit officiellement."),
        ("une signature", "Votre nom écrit de votre main, qui rend le papier valable."),
        ("une copie", "Le double qu'on garde pour soi quand on remet l'original."),
    ], notes="La quatrième famille sera le bloc D au complet. Annoncer dès maintenant "
             "que ces quatre mots-là vont ensemble : une note porte un motif, une "
             "signature, et on en garde une copie.")

    d.tableau('Le bon mot', "Six phrases à compléter",
              ['Ce qui manque', 'La phrase'],
              [["la boîte vocale", "Avant huit heures, c'est ___ qui répond."],
               ["le clavier", "Appuyez sur le 2 du ___."],
               ["la ligne", "___ était occupée : elle a rappelé plus tard."],
               ["un poste", "Le secrétariat, c'est le ___ 224."],
               ["un retard", "L'autobus n'est pas passé : vingt minutes de ___."],
               ["un empêchement", "Elle a téléphoné dès qu'elle a su qu'elle avait ___."]],
              cle=0,
              notes="Masquer la colonne de gauche, faire compléter à l'oral, puis "
                    "révéler. Les deux dernières demandent de choisir entre deux mots "
                    "proches : c'est exactement le travail de A4.")

    d.pratique('Association', "La photo et la phrase",
               "Quelle photo va avec quelle description ?", [
        ("Un téléphone qui sonne sur un comptoir sans personne derrière.",
         "telephone-comptoir-vide"),
        ("Quelqu'un qui téléphone debout dans une cage d'escalier vide.",
         "appel-cage-escalier"),
        ("Un réveille-matin allumé dans une chambre encore sombre.",
         "reveil-avant-aube"),
        ("Un enfant couché avec un thermomètre à côté.", "enfant-malade-lit"),
        ("Un arrêt d'autobus sous la neige, avec des gens qui attendent.",
         "autobus-neige-arret"),
        ("Une feuille pliée qui passe d'une main à une autre.", "note-remise-main"),
    ], corrige=True,
       notes="Les six photos sont celles de l'exercice 3 du module. Les projeter une à "
             "une et faire décrire avant de donner la phrase : le vocabulaire sort de "
             "lui-même, et il sort en phrases complètes.")

    d.piege("Confondre le poste et le numéro",
            "J'ai appelé au 224 et ça ne répondait pas.",
            "J'ai appelé au 450 555-0180, poste 224.",
            "Un poste est un numéro interne : il ne fonctionne qu'une fois le "
            "numéro principal composé. Composer le poste tout seul ne mène nulle "
            "part, et c'est une des raisons pour lesquelles un élève croit que "
            "le centre ne répond jamais.",
            notes="Vérifier au passage que chacun a le numéro principal du centre dans "
                  "son téléphone. C'était le billet de sortie de A1 : le moment est "
                  "venu de le ramasser.")

    d.billet(
        "Écrivez quatre mots de la séance, un par famille, avec leur article.",
        exemples=[
            "Un mot du téléphone, un du message, un des motifs, un du papier.",
            "Avec l'article : la, le, un, une.",
        ],
        notes="Ramasser. Les articles fautifs se corrigent individuellement : « une "
              "poste » et « le boîte vocale » sont les deux qui reviennent.")

    return d.save(dossier)
