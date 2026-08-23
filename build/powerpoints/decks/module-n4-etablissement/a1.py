# -*- coding: utf-8 -*-
"""A1 · « Il faut appeler avant huit heures »
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source du module : dialogue `prep`, exercice `pr1`.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n4-etablissement/images/')


def img(nom):
    """Le chemin d'une illustration, ou None si elle n'a pas encore été
    produite. Les séances se construisent sans les images et les reprennent
    d'elles-mêmes à la reconstruction."""
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="« Il faut appeler avant huit heures »",
        chapeau="Nourhane Ouazzani est arrivée du Maroc il y a un an. Son "
                "fils de cinq ans s'est réveillé dimanche soir avec une "
                "otite, et demain matin elle sera à la clinique au lieu "
                "d'être en classe. Le bureau du centre ouvre à huit heures, "
                "le cours commence à huit heures : quand elle appellera, il "
                "n'y aura personne.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une seule question, à main "
                  "levée : qui, dans le groupe, a déjà manqué un cours sans prévenir "
                  "personne ? Puis : pourquoi ? Les réponses tournent presque toujours "
                  "autour de deux choses — le bureau était fermé, ou on ne savait pas "
                  "quoi dire. Le module répond exactement à ces deux-là.")

    d.objectifs([
        "comprendre pourquoi le centre est fermé au moment où l'on doit appeler ;",
        "nommer ce qu'il y a au bout du fil : la ligne, le clavier, la boîte vocale ;",
        "savoir ce qu'un message enregistré règle, et ce qu'il ne règle pas ;",
        "distinguer ce qu'on se dit entre élèves de ce qu'on dit au bureau.",
    ], notes="Le troisième objectif est le vrai contenu de la séance. Beaucoup d'élèves "
             "croient l'affaire close après l'appel et découvrent trois semaines plus "
             "tard une absence non motivée. Insister là-dessus plutôt que sur le "
             "vocabulaire, qui viendra en A3.")

    d.declencheur(
        'Observation', "Un téléphone qui sonne sur un comptoir vide. "
                       "Qui va répondre ?",
        image=img('telephone-comptoir-vide.jpg'),
        pistes=[
            "Quelle heure est-il, à votre avis, sur cette photo ?",
            "À quelle heure ouvre le bureau de votre centre ? Et le cours ?",
            "Que se passe-t-il si vous appelez avant l'ouverture ?",
            "Est-ce que le message que vous laissez sera écouté ? Par qui ?",
        ],
        notes="La deuxième piste est celle qui déclenche la discussion : presque "
              "personne ne connaît les heures d'ouverture du secrétariat de son propre "
              "centre. Les faire chercher, et écrire les deux heures au tableau.")

    d.dialogue('Dialogue · 1 de 4', "Tu sais le numéro du centre ?", [
        ("NOURHANE", "Wilner, tu sais le numéro du centre ? Le vrai, pas "
                     "celui du site.", True),
        ("WILNER", "Le 450 555-0180. Pourquoi ? Tu es là, pourtant.", True),
        ("NOURHANE", "C'est pour demain. Mon garçon a une otite et la "
                     "clinique est à neuf heures.", True),
        ("WILNER", "Alors tu appelles demain matin, avant huit heures. Pas "
                   "ce soir.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Relever la précision de Wilner : « le vrai, pas celui du site ». Un "
             "centre a souvent plusieurs numéros, et celui du site mène au standard "
             "général. Demander au groupe qui a le bon numéro dans son téléphone.")

    d.dialogue('Dialogue · 2 de 4', "Une machine, ça compte ?", [
        ("NOURHANE", "Le bureau est fermé le matin. Personne ne va "
                     "décrocher.", True),
        ("WILNER", "Justement. Tu laisses ton message dans la boîte vocale, "
                   "et ça compte pareil.", True),
        ("NOURHANE", "Ça compte ? Une machine, ça compte ?", True),
        ("WILNER", "Madame Sansregret écoute tout à huit heures et elle "
                   "écrit dans le dossier.", True),
    ], notes="La question de Nourhane est celle de tout le groupe. Répondre "
             "franchement : oui, le message compte, et il est même daté — c'est ce "
             "qui prouvera que vous avez prévenu avant le début du cours.")

    d.dialogue('Dialogue · 3 de 4', "Elle ne pourra pas te faire répéter", [
        ("NOURHANE", "Et si je parle mal ? Elle ne pourra pas me demander de "
                     "répéter.", True),
        ("WILNER", "C'est ça, le piège. Ton nom, ton groupe, la date. "
                   "Lentement, au début.", True),
        ("NOURHANE", "Mon nom est long. Ouazzani, personne ne l'écrit du "
                     "premier coup.", True),
        ("WILNER", "Tu l'épelles. Et tu laisses ton numéro deux fois, à la "
                   "fin.", True),
    ], notes="Voilà la contrainte qui tient tout le module : personne ne peut vous "
             "faire répéter. Faire épeler son nom de famille à chacun, à voix haute, "
             "tout de suite. C'est court et c'est utile toute la vie.")

    d.dialogue('Dialogue · 4 de 4', "Ce qui fait long, c'est l'otite", [
        ("NOURHANE", "Deux fois le numéro ? Ça fait long, pour une minute.", True),
        ("WILNER", "Une minute, c'est beaucoup. Ce qui fait long, c'est de "
                   "raconter l'otite.", True),
        ("NOURHANE", "Bon. Le nom, le groupe, la date, la raison en une "
                     "phrase, le numéro.", True),
        ("WILNER", "Voilà. Et pour le papier de la clinique, tu le donnes à "
                   "Fabien jeudi.", False),
    ], notes="L'avant-dernière réplique est le plan du bloc B au complet. La faire "
             "répéter et l'écrire au tableau : les cinq morceaux resteront affichés "
             "jusqu'à la fin du module.")

    d.regle("Deux moitiés, pas une",
            "L'appel dit que vous avez prévenu. La note écrite dit pourquoi.",
            precision="Un message enregistré ne motive jamais une absence à lui "
                      "seul : il faut le papier, ensuite.",
            notes="Diapositive à photographier. Elle revient en D1 et en E2. C'est la "
                  "phrase du module que les élèves emporteront s'ils n'en retiennent "
                  "qu'une.")

    d.cartes("Au bout du fil", "Quatre mots avant tout le reste", [
        ("La boîte vocale",
         "Le service qui enregistre votre message quand personne ne décroche."),
        ("Un répondeur",
         "L'appareil ou le service qui répond tout seul et garde ce qu'on lui dit."),
        ("Le clavier",
         "Les touches numérotées sur lesquelles on appuie pour choisir."),
        ("La ligne",
         "La liaison elle-même, qui peut être libre, occupée ou coupée."),
    ], notes="Faire répéter avec l'article. Signaler que « peser sur le 1 » s'entend "
             "partout au Québec et veut dire « appuyer sur le 1 » : ce n'est pas une "
             "faute, c'est la langue de tous les jours.")

    d.tableau('Deux façons de parler', "Entre nous, et au bureau",
              ['Avec un camarade', 'Au téléphone, au bureau'],
              [["Je viens pas demain.", "Je serai absente demain, jeudi le 17."],
               ["Mon petit est malade.", "Mon fils est malade et j'ai un rendez-vous."],
               ["Je vais être en retard.", "J'aurai environ trente minutes de retard."],
               ["Bon, ben, merci là.", "Je vous remercie. Bonne journée."]],
              cle=1,
              notes="Faire compléter la colonne de droite avant de l'afficher. Ne pas "
                    "présenter la colonne de gauche comme fautive : elle est juste "
                    "entre camarades. C'est l'interlocuteur qui change, pas la qualité "
                    "du français.")

    d.piege("Croire que l'appel suffit",
            "J'ai téléphoné, c'est réglé.",
            "J'ai téléphoné, et j'apporte ma note écrite avant vendredi.",
            "Le message est écouté et inscrit au dossier, mais il ne motive rien. "
            "Sans note signée, l'absence reste marquée non motivée, et personne ne "
            "vous préviendra que quelque chose manque.",
            notes="Ce piège est le vrai obstacle du module, et il ne vient pas d'un "
                  "manque de vocabulaire : il vient de ce qu'un appel donne le "
                  "sentiment d'avoir fait sa part. Le nommer maintenant, il reviendra "
                  "en C1 et en D1.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le fils de Nourhane a une otite.", "vrai"),
        ("Wilner lui conseille de téléphoner ce soir.",
         "faux — demain avant huit heures"),
        ("Le bureau du centre est fermé tôt le matin.", "vrai"),
        ("Un message dans la boîte vocale ne compte pas.",
         "faux — il est écouté et inscrit"),
        ("Nourhane doit épeler son nom de famille.", "vrai"),
        ("Wilner conseille de raconter l'otite en détail.",
         "faux — c'est ce qui fait long"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la réplique exacte. La quatrième est "
             "celle que le groupe manque : on croit spontanément qu'une machine ne "
             "compte pas.")

    d.billet(
        "Écrivez à quelle heure ouvre le bureau de votre centre, et à quelle "
        "heure commence votre cours.",
        exemples=[
            "Les deux heures, en chiffres.",
            "Ajoutez le numéro de téléphone du secrétariat si vous le connaissez.",
        ],
        notes="Ramasser les billets. Ceux qui ne connaissent pas le numéro le "
              "chercheront d'ici A4 : c'est le petit devoir de la semaine, et il "
              "servira vraiment.")

    return d.save(dossier)
