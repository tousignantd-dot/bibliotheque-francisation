# -*- coding: utf-8 -*-
"""D2 · « Elle sortira jeudi » et « la docteure dit que… ».
Bloc D « Défi 3 » · couleur ambre · 75 min. Écriture.
Source : exercices `t3fut` et `t3rap`, et leurs mini-leçons.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-urgence/images/')


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="« Elle sortira jeudi », « la docteure dit que… »",
        chapeau="Deux outils pour un seul appel : le futur simple pour "
                "annoncer ce qui s'en vient, le discours rapporté pour "
                "redire ce qu'on vous a dit sans le déformer.",
        duree='75 minutes')

    d.titre(notes="Dernière séance de grammaire du module. Relire deux billets de D1 et "
                  "faire produire oralement la réponse de la docteure : le futur simple "
                  "sort tout seul.")

    d.objectifs([
        "former le futur simple, y compris ses irréguliers utiles ;",
        "employer le futur après « quand » et « dès que » ;",
        "rapporter une affirmation avec « dit que » et un ordre avec « demande de » ;",
        "ajuster les pronoms et les déterminants en rapportant.",
    ])

    d.declencheur(
        'Situation', "Vous appelez votre frère du corridor. Que lui dites-vous de "
                     "ce qui n'est pas encore arrivé ?",
        image=IMG + 'telephone-nuit.jpg',
        pistes=[
            "Quand sortira-t-elle ?",
            "Qui viendra la voir ?",
            "Qu'est-ce qu'il faudra apporter ?",
            "Que faut-il rapporter des paroles du médecin ?",
        ],
        notes="Écrire les réponses spontanées au tableau. Le futur proche domine toujours "
              "— « elle va sortir » — et c'est l'entrée en matière parfaite.")

    d.regle("L'infinitif, plus six terminaisons",
            "sortir + a donne elle sortira. Les terminaisons sont celles du verbe avoir.",
            precision="Toutes les formes du futur contiennent le r de l'infinitif. Si "
                      "vous ne l'entendez pas, la forme est fausse. Les verbes en -re "
                      "perdent leur e : attendre donne elle attendra.",
            notes="Diapositive à photographier. Le repère du r est le plus efficace pour "
                  "l'autocorrection à l'oral.")

    d.tableau('Les irréguliers dont on a besoin ici', "Neuf verbes couvrent presque tout",
              ['Infinitif', 'Futur', 'Dans le module'],
              [["être · avoir", "sera · aura", "Elle sera prête jeudi."],
               ["aller · faire", "ira · fera", "Nous irons la chercher."],
               ["venir", "viendra", "Une intervenante viendra."],
               ["pouvoir · devoir", "pourra · devra", "Elle devra marcher."],
               ["voir · falloir", "verra · faudra", "Il faudra une barre d'appui."]],
              cle=1,
              notes="Les faire apprendre dans les phrases de la colonne de droite, pas en "
                    "liste. Une conjugaison hors contexte ne ressort pas au téléphone.")

    d.pratique('Formation', "Mettez au futur simple",
               "À l'oral d'abord, puis à l'écrit.", [
        ("Elle ___ (sortir) dans trois ou quatre jours.", "sortira"),
        ("Vous ___ (recevoir) un résumé et les ordonnances.", "recevrez"),
        ("Une intervenante du CLSC ___ (venir) avant sa sortie.", "viendra"),
        ("Elle ___ (devoir) marcher avec une marchette.", "devra"),
        ("Il ___ (falloir) une barre d'appui dans l'escalier.", "faudra"),
        ("Nous ___ (aller) la chercher en voiture jeudi matin.", "irons"),
        ("Elle sortira quand elle ___ (marcher) quinze pas.", "marchera"),
        ("Je vous ___ (appeler) dès que j'___ (avoir) la date.", "appellerai · aurai"),
    ], corrige=True,
       notes="Les deux dernières portent le piège du « quand » : en français, le futur "
             "est obligatoire après quand et dès que. Beaucoup de langues font l'inverse.")

    d.piege("Mettre le présent après « quand »",
            "Elle sortira quand elle marche quinze pas.",
            "Elle sortira quand elle marchera quinze pas.",
            "Après quand, dès que, aussitôt que, le français met le futur. C'est une des "
            "rares règles qui n'a aucune exception.",
            notes="La faire répéter oralement cinq fois avec des sujets différents : "
                  "c'est un automatisme, pas une réflexion.")

    d.regle("Rapporter, c'est changer de bouche sans changer l'information",
            "« Votre mère sortira jeudi. » donne La docteure dit que ma mère sortira jeudi.",
            precision="Le « que » est obligatoire. Les pronoms et les déterminants "
                      "changent de propriétaire. Avec un verbe introducteur au présent, "
                      "les temps ne bougent pas.",
            notes="Diapositive à photographier. Au niveau 5, s'en tenir au présent : « la "
                  "docteure dit que… ». Le décalage des temps viendra plus tard.")

    d.cartes("Quatre mécanismes, et rien d'autre", "Ils suffisent à tout un appel de nouvelles", [
        ("Une affirmation", "dire que · expliquer que · ajouter que"),
        ("Un ordre", "demander de + infinitif : « elle m'a demandé de vérifier »"),
        ("Une question fermée", "demander si : « elle m'a demandé si maman avait des "
                                "allergies »"),
        ("Le changement de personne", "« votre mère » devient « ma mère » ; « je » "
                                      "devient « elle »"),
    ], notes="Faire remarquer que le troisième mécanisme est celui de la séance C3 : il "
             "revient, et c'est normal. Un module bien construit fait revenir ses outils.")

    d.pratique('Transformation', "Rapportez ce qu'on vous a dit",
               "Complétez.", [
        ("« La douleur est contrôlée. » donne La docteure dit ___ la douleur est contrôlée.", "que"),
        ("« Votre mère devra marcher. » donne Elle dit que ___ mère devra marcher.", "ma"),
        ("« Je passerai demain. » donne La physiothérapeute dit qu'___ passera demain.", "elle"),
        ("« Vérifiez les allergies. » donne L'infirmière m'a demandé ___ vérifier.", "de"),
        ("« Est-ce qu'elle a des allergies ? » donne Elle m'a demandé ___ elle avait des allergies.", "si"),
        ("« Nous la gardons trois jours. » donne Ils disent qu'ils ___ gardent trois jours.", "la"),
        ("« Apportez ses lunettes. » donne Je lui ai demandé ___ apporter ses lunettes.", "d'"),
    ], corrige=True,
       notes="La deuxième et la troisième sont les plus formatrices : c'est le changement "
             "de propriétaire qui rend un message compréhensible ou non.")

    d.piege("Rapporter un ordre avec « que »",
            "Elle m'a demandé que je vérifie les allergies.",
            "Elle m'a demandé de vérifier les allergies.",
            "Avec le verbe « demander », un ordre se rapporte par de + infinitif. La "
            "construction avec « que » existe, mais elle appelle le subjonctif et "
            "n'appartient pas à ce niveau.",
            notes="Ne pas développer le subjonctif ici. Donner la forme sûre et passer.")

    d.billet(
        "Écrivez quatre phrases de nouvelles : deux au futur, deux rapportées.",
        exemples=[
            "« Elle sortira… », « il faudra… », « la docteure dit que… », « elle m'a demandé si… ».",
            "Comme si vous écriviez vraiment à quelqu'un ce soir.",
        ],
        notes="Fin du bloc D. Ces quatre phrases sont le brouillon de la production orale "
              "de E1 : le dire, cela motive à les soigner.")

    return d.save(dossier)
