# -*- coding: utf-8 -*-
"""A1 · Quatre paragraphes après deux ans
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `prVF`, quatre premières cartes de
FC_CARDS.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Quatre paragraphes après deux ans",
        chapeau="Un ami parti dans le Nord écrit enfin. Deux ans de vie "
                "tiennent dans quatre paragraphes, et Marisol n'est pas "
                "certaine d'avoir tout compris.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : "
                  "qui, ici, a quelqu'un de proche qui vit loin ? Comment vous "
                  "donnez-vous des nouvelles ? La réponse la plus fréquente est le "
                  "message vocal ou le message texte — c'est justement ce qui rend un "
                  "long courriel difficile à lire.")

    d.objectifs([
        "nommer les grands évènements qu'un courriel de nouvelles annonce ;",
        "compter les idées d'un texte long en comptant ses paragraphes ;",
        "comprendre qu'un petit mot comme « la » renvoie toujours en arrière ;",
        "employer les quatre premiers mots du dossier avec leur article.",
    ], notes="Le troisième objectif est celui du module entier. Le dire tel quel : "
             "ce qui est difficile au niveau 6, ce n'est plus le vocabulaire, c'est "
             "de savoir à quoi renvoient les petits mots.")

    d.declencheur(
        'Observation', "Comment donnes-tu des nouvelles à quelqu'un qui vit loin ?",
        pistes=[
            "Message texte, appel, message vocal, courriel, lettre ?",
            "Quand as-tu écrit un texte long pour la dernière fois ?",
            "Qu'est-ce qui est plus facile à écrire : parler ou écrire ?",
            "As-tu déjà relu un message deux fois sans être sûr de comprendre ?",
        ],
        notes="Question sans mauvaise réponse. Noter au tableau les moyens nommés : "
              "on y reviendra en E2, quand chacun écrira son propre courriel.")

    d.dialogue('Dialogue · 1 de 3', "Un courriel de quatre paragraphes", [
        ("MARISOL", "Ghislain ! Vous vous rappelez Ousmane, celui qui venait chercher son pain le samedi matin ?", True),
        ("GHISLAIN", "Le grand monsieur qui parlait de son garage. Il est parti dans le Nord, il me semble.", True),
        ("MARISOL", "À Rouyn-Noranda, il y a deux ans. Ce matin, j'ai reçu un courriel de quatre paragraphes.", True),
        ("GHISLAIN", "Quatre paragraphes ! Ça, c'est quelqu'un qui a des choses à raconter.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Deux ans, quatre paragraphes : ces deux chiffres reviennent dans tout "
             "le module. Les écrire au tableau et les y laisser toute la séance.")

    d.dialogue('Dialogue · 2 de 3', "Vendue, mais vendu quoi ?", [
        ("MARISOL", "Il écrit : « on l'avait déjà vendue quand je t'ai écrit la dernière fois ». Vendu quoi ? La maison ? L'auto ?", True),
        ("GHISLAIN", "Recule d'une phrase. Ce petit mot-là ne tombe pas du ciel : il remplace quelque chose qui a été dit avant.", True),
        ("MARISOL", "Attendez… Le paragraphe d'avant parle de leur ancienne maison, sur la rue Perreault. Ah. C'est la maison.", True),
        ("GHISLAIN", "Voilà. Dans un texte long, la moitié du travail, c'est ça : retrouver à quoi renvoient les petits mots.", True),
    ], notes="La dernière réplique est la définition du module. La faire répéter par "
             "deux élèves. Puis refaire le geste ensemble sur une autre phrase.")

    d.dialogue('Dialogue · 3 de 3', "Un blanc, une idée", [
        ("MARISOL", "Il y a beaucoup de nouvelles là-dedans. Une naissance, un déménagement, un accident, des funérailles, un mariage.", True),
        ("GHISLAIN", "Cinq évènements en quatre paragraphes. C'est pour ça qu'il a fait des paragraphes, d'ailleurs.", True),
        ("MARISOL", "C'est vrai qu'il y a un blanc entre chaque. Et l'objet du courriel dit : « Des nouvelles, enfin ».", True),
        ("GHISLAIN", "Un courriel bien fait se lit avant d'être lu. Tu regardes d'abord la forme, ensuite tu suis le fil.", True),
    ], notes="Annoncer ici la production écrite de E2 : dans quatre semaines, chacun "
             "écrira son propre courriel de nouvelles. Le dire tôt donne un but au "
             "reste du module.")

    d.tableau('Analyse', "Ce qu'un courriel de nouvelles annonce",
              ['Le mot', 'Ce que la nouvelle demande'],
              [["Une naissance", "on félicite, et on nomme les parents ou l'enfant"],
               ["Un déménagement", "on demande comment se passe le nouveau quartier"],
               ["Un accident", "on souhaite le rétablissement de la personne"],
               ["Des funérailles", "on offre ses condoléances, sans poser de question"],
               ["Un mariage", "on félicite, et on demande si l'on peut y être"]],
              cle=0,
              note="Le mot juste existe pour chaque nouvelle, et il est court.",
              notes="Diapositive à photographier. Elle revient en A4 sous forme "
                    "d'exercice. Insister sur la quatrième rangée : la cause d'un "
                    "décès ne se demande jamais.")

    d.regle("Regarder la forme avant de lire le texte",
            "Compter les blancs d'un courriel, c'est compter ses nouvelles.",
            precision="L'objet annonce le sujet et le ton. La formule d'appel dit à "
                      "qui l'on parle et si l'on tutoie. Chaque blanc annonce un "
                      "changement d'idée, et la première phrase de chaque paragraphe "
                      "en porte l'essentiel. Dix secondes de regard épargnent deux "
                      "relectures.",
            notes="Diapositive à photographier. On ne demande pas de tout comprendre : "
                  "on demande de savoir quoi chercher, et dans quel ordre.")

    d.vocabulaire('Vocabulaire', "Quatre mots, avec leur article", [
        ("une naissance", "L'arrivée au monde d'un enfant, dans une famille."),
        ("un déménagement", "Le fait de quitter un logement pour aller vivre dans un autre."),
        ("des funérailles", "La cérémonie qu'on tient après la mort de quelqu'un."),
        ("un faire-part", "Une petite carte envoyée pour annoncer un évènement de la vie."),
    ], notes="« Des funérailles » est toujours au pluriel, comme « des fiançailles ». "
             "« Un faire-part » ne change pas au pluriel : des faire-part.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la conversation de Marisol et de Ghislain.", [
        ("Ousmane est parti vivre à Rouyn-Noranda il y a deux ans.", "vrai"),
        ("Marisol a tout compris dès la première lecture.", "faux - elle l'a lu deux fois"),
        ("Un petit mot comme « la » renvoie à quelque chose dit avant.", "vrai"),
        ("Le courriel annonce cinq évènements différents.", "vrai"),
        ("Un long courriel se lit comme un message texte.", "faux - on regarde d'abord la forme"),
        ("Marisol est libre le jour où Ousmane arrive.", "faux - elle travaille"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Laisser du "
             "silence : les élèves relisent plus lentement qu'on ne le croit.")

    d.billet(
        "Quelle nouvelle serait la plus difficile à annoncer par écrit ?",
        exemples=[
            "Une phrase suffit.",
            "Pense à ce que tu écrirais, et à ce que tu préférerais dire de vive voix.",
        ],
        notes="Deux minutes. Les réponses servent en A4 : elles disent quelles "
              "nouvelles intimident le groupe, et ce sont celles-là qu'il faudra "
              "travailler le plus lentement.")

    return d.save(dossier)
