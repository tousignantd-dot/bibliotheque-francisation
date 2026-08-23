# -*- coding: utf-8 -*-
"""D1 · Deux lettres, et ce qui les distingue
Bloc D « Défi 3 · La lettre qui règle » · couleur acier · compréhension orale
et écrite · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3lettre` (type texte).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Deux lettres, et ce qui les distingue",
        chapeau="La première va au voisin : elle est courte, elle est "
                "aimable, elle n'a pas de délai. La seconde va à la "
                "propriétaire et porte un nom : une mise en demeure.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 3. Deux semaines ont passé depuis le bloc B : "
                  "deux engagements sur trois ont été tenus, et le troisième non. "
                  "C'est de là que part la séance.")

    d.objectifs([
        "distinguer la lettre au voisin de la mise en demeure ;",
        "nommer les trois parties d'une mise en demeure ;",
        "repérer dans une lettre l'objet, les dates, la demande et le délai ;",
        "employer quatre mots de l'écrit.",
    ], notes="La distinction du premier objectif est celle qui coûte le plus cher "
             "quand on la rate : une mise en demeure reçue par un voisin transforme un "
             "arrangement en conflit.")

    d.declencheur(
        'Observation', "Deux mesures sur trois ont été prises. Qu'est-ce que tu fais ?",
        pistes=[
            "Tu remontes voir le voisin ? Tu écris ? Tu attends ?",
            "Est-ce que tu remercies pour ce qui a été fait ?",
            "À qui écrirais-tu, et pour demander quoi ?",
            "Combien de temps laisserais-tu ?",
        ],
        notes="Beaucoup diront « j'attends encore ». Faire compter : six semaines de "
              "nuits coupées. Attendre n'est plus neutre.")

    d.dialogue('Dialogue · 1 de 3', "Deux sur trois", [
        ("HUBERT", "Deux semaines de plus, et où en êtes-vous ?", True),
        ("RUSLANA", "Le caoutchouc a été posé le 26 février. Ça a diminué le bruit, mais ça ne l'a pas fait disparaître. Le tapis n'a pas été déplacé.", True),
        ("RUSLANA", "Je me réveille encore. Moins fort, et pas tous les matins. Neuf matins sur les quatorze derniers.", True),
        ("HUBERT", "Vous l'avez noté ? Gardez ça précieusement. Maintenant, écrivez.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Faire remarquer la précision « neuf matins sur quatorze ». Sans le "
             "registre commencé en A1, cette phrase n'existerait pas.")

    d.dialogue('Dialogue · 2 de 3', "Aux deux, mais pas la même lettre", [
        ("RUSLANA", "À monsieur Rondeau ou à la propriétaire ?", True),
        ("HUBERT", "Aux deux, mais pas la même lettre et pas le même jour. Ce sont deux gestes différents.", True),
        ("HUBERT", "La première est une lettre à votre voisin. Elle sert à mettre par écrit ce que vous vous êtes dit sur le palier. Ce n'est pas une menace : c'est une mémoire commune.", True),
        ("HUBERT", "La deuxième a un nom : une mise en demeure. Voici le problème, voici ce que je vous demande, voici le délai que je vous donne.", True),
    ], notes="Écrire au tableau les trois parties de la mise en demeure et les y "
             "laisser jusqu'à la fin du bloc E.")

    d.dialogue('Dialogue · 3 de 3', "Écrivez la conséquence, pas l'émotion", [
        ("RUSLANA", "Pourquoi elle, et pas lui ? Ce n'est pas elle qui court sur le tapis.", True),
        ("HUBERT", "Votre propriétaire s'est engagée, en signant votre bail, à vous procurer la jouissance paisible de votre logement. Et celui qui dérange est lui aussi son locataire.", True),
        ("RUSLANA", "Est-ce que je dois écrire que je suis fatiguée ?", True),
        ("HUBERT", "Écrivez la conséquence, pas l'émotion. Un fait ne se discute pas ; « je suis épuisée et personne ne m'écoute » se discute, et vous perdrez.", True),
    ], notes="La dernière réplique referme la boucle ouverte en A3. Le faire remarquer "
             "au groupe : c'est la même règle, cinq séances plus tard, dans un autre "
             "genre.")

    d.tableau('Analyse', "Deux lettres, six différences",
              ['Lettre au voisin', 'Mise en demeure'],
              [["Ton cordial", "Ton neutre"],
               ["Garder une trace de l'entente", "Mettre une obligation en marche"],
               ["Pas d'objet", "Un objet avant l'appel"],
               ["Aucun délai", "Un délai précis, en jours"],
               ["Demande au conditionnel", "Je vous demande de…"],
               ["Remise en main propre", "Envoyée par courrier recommandé"]],
              cle=1,
              notes="Diapositive à photographier. C'est le tableau de référence du "
                    "bloc D et il revient en E2, au moment d'écrire.")

    d.regle("La mise en demeure : trois choses, dans cet ordre",
            "Le problème, la demande, le délai. Rien d'autre.",
            precision="Le problème : les faits, les dates, la conséquence — dix lignes "
                      "au plus. La demande : ce que vous voulez exactement, en une "
                      "phrase qui se répond par oui ou par non. Le délai : un nombre de "
                      "jours précis à compter de la réception, dix jours en général. "
                      "« La présente » désigne la lettre elle-même.",
            notes="Diapositive à photographier. Tout ce qui n'est pas une date, une "
                  "heure ou une conséquence s'enlève. Le récit complet appartient au "
                  "registre, pas à la lettre.")

    d.vocabulaire('Vocabulaire', "Quatre mots de l'écrit", [
        ("une mise en demeure", "Une lettre qui expose un problème, demande précisément quelque chose et donne un délai."),
        ("un délai raisonnable", "Le temps qu'on laisse pour agir : dix jours, le plus souvent."),
        ("un courrier recommandé", "Un envoi postal dont on garde la preuve, parce que la personne doit signer."),
        ("une diminution de loyer", "La baisse du montant mensuel, accordée quand le logement n'a pas donné ce qu'il devait."),
    ], notes="Le courrier recommandé ne prouve pas ce que vous avez écrit : il prouve "
             "qu'il l'a reçu, et à quelle date. C'est cette date qui fait courir le "
             "délai.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la rencontre avec le médiateur et les deux lettres.", [
        ("Deux des trois engagements du voisin ont été tenus.", "vrai"),
        ("Il faut écrire la même lettre au voisin et à la propriétaire.", "faux - deux gestes différents"),
        ("La lettre au voisin sert à mettre par écrit ce qui a été convenu.", "vrai"),
        ("Une mise en demeure doit contenir un délai précis.", "vrai"),
        ("Il vaut mieux une citation approximative qu'un résumé honnête.", "faux - c'est l'inverse"),
        ("Ruslana écrit à sa propriétaire parce que c'est elle qui fait le bruit.", "faux - parce que le voisin est aussi sa locataire"),
    ], corrige=True,
       notes="Le sixième est le plus important : c'est la raison juridique de toute la "
             "démarche, et elle n'est pas évidente.")

    d.billet(
        "Écris l'objet de la mise en demeure de Ruslana, en huit à douze mots.",
        exemples=[
            "Un groupe de mots, jamais une phrase complète.",
            "Ni plainte, ni explication : de quoi il s'agit, et ce qu'on demande.",
        ],
        notes="Deux minutes. Comparer trois réponses au tableau au début de D2 : la "
              "différence entre un objet qui classe et un objet qui plaide se voit "
              "tout de suite.")

    return d.save(dossier)
