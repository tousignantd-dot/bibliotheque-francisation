# -*- coding: utf-8 -*-
"""D2 · Se plaindre efficacement, sans se fâcher.
Bloc D · couleur ambre (production) · 75 min.
Source : mini-leçon `t3plainte`, exercices `t3plainte` et `t3form`, dialogue `t3b`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre='Se plaindre efficacement, sans se fâcher',
        chapeau="Une plainte qui n'aboutit pas est très souvent une plainte à laquelle "
                "il manquait simplement la demande finale. Décrire n'est pas encore "
                "se plaindre.",
        duree='75 minutes')

    d.titre(notes="Séance la plus utile du module dans la vie réelle. Prévoir beaucoup de "
                  "production orale : la formule ne s'apprend pas en la lisant.")

    d.objectifs([
        "distinguer une description d'une plainte ;",
        "construire une plainte en trois temps : le fait, l'effet sur moi, la demande ;",
        "choisir des mots dont l'intensité correspond au moment ;",
        "rester ferme sans attaquer la personne.",
    ])

    d.piege('Le point de départ',
            "Le bac de recyclage déborde tous les mardis.",
            "Je ne peux plus tolérer que le bac déborde ; pourriez-vous demander une collecte de plus ?",
            "La première phrase est une description : elle dit ce qui se passe, et l'autre "
            "personne peut très bien répondre « ah oui, en effet » sans rien faire. La "
            "seconde est une plainte : elle contient un jugement et une demande. Les deux "
            "sont polies ; une seule des deux fait bouger quelque chose.",
            notes="Ouvrir là-dessus, en reprenant les témoignages de la séance D1. Camille "
                  "décrivait, Jean-Philippe demandait.")

    d.tableau('La formule', "Trois temps, dans cet ordre",
              ['Temps', 'Exemple', 'Ce que ça fait'],
              [["1 · Le fait", "La musique joue jusqu'à deux heures.", "on informe"],
               ["2 · L'effet sur moi", "Je commence à sept heures et je ne dors plus.", "on donne envie d'agir"],
               ["3 · La demande", "Pourriez-vous leur en parler ?", "on dit ce qu'on attend"]],
              cle=1,
              note="Le temps 2 est celui qu'on oublie le plus, et c'est pourtant celui qui "
                   "compte : il transforme un détail en problème réel pour quelqu'un.",
              notes="C'est la diapo à photographier. La faire copier dans le cahier avant "
                    "de continuer.")

    d.regle('Pourquoi le deuxième temps est décisif',
            "Un fait se discute. Un effet sur une personne ne se discute pas.",
            precision="« Le corridor est encombré » peut se contester : encombré selon qui ? "
                      "« Je ne peux plus passer avec ma poussette » ne se conteste pas — "
                      "c'est votre expérience, et personne ne peut vous dire que vous avez "
                      "tort de la vivre.",
            notes="Argument fort pour des adultes. Le faire reformuler par le groupe avec "
                  "leurs propres situations.")

    d.cartes('Les mots', "Une échelle d'intensité, du bas vers le haut", [
        ("1 · La situation dérange",
         "Cette situation est dérangeante. C'est très difficile de… C'est vraiment injuste. "
         "C'est décevant. Pour un premier contact."),
        ("2 · Je dis mon émotion",
         "Je suis irritée par… Je suis fâché de… Je suis contrariée par… Je suis fatigué "
         "de… Je suis très déçue. Pour une deuxième fois."),
        ("3 · Je suis au bout",
         "Je ne peux plus tolérer… Je ne peux plus accepter cette situation. Cette "
         "situation doit se terminer. C'est inacceptable. C'est inapproprié."),
        ("Le principe de l'échelle",
         "On commence par le bas. On garde « inacceptable » pour la deuxième ou la "
         "troisième fois, jamais pour le premier appel — sinon il ne reste plus rien "
         "à dire ensuite."),
    ], notes="La quatrième carte est le vrai enseignement. Beaucoup d'élèves commencent "
             "trop haut par crainte de ne pas être pris au sérieux, et se retrouvent sans "
             "marge de manœuvre.")

    d.tableau('Monter l\'intensité', "Le même problème, trois degrés",
              ['Degré', 'Ce qu\'on dit', 'Quand'],
              [["1 · doux", "C'est un peu dérangeant, mais je préfère vous en parler.", "1er contact"],
               ["2 · ferme", "Je suis fatiguée de ne pas dormir la semaine.", "2e fois"],
               ["3 · très ferme", "Je ne peux plus tolérer ce bruit : c'est inacceptable.", "avant l'écrit"]],
              cle=1,
              note="Même au degré 3, on parle de la situation et jamais de la personne. "
                   "C'est ce qui garde la conversation possible — et c'est ce qui permet "
                   "de continuer à se croiser dans l'escalier.",
              notes="Faire dire les trois phrases à voix haute par la même personne, avec "
                    "le ton correspondant. L'exercice est inconfortable et très efficace.")

    d.pratique('Pratique', 'Se plaindre ou décrire ?',
               "Écoutez chaque phrase et dites si la personne se plaint ou décrit.", [
        ("Le bac de recyclage déborde tous les mardis matin.", "DÉCRIT"),
        ("Je ne peux plus tolérer le bruit après minuit, c'est inacceptable.", "SE PLAINT"),
        ("La porte d'entrée reste ouverte quand il vente très fort.", "DÉCRIT"),
        ("Cette situation est vraiment dérangeante et elle doit se terminer.", "SE PLAINT"),
        ("Je suis très déçue de la façon dont le corridor est laissé.", "SE PLAINT"),
    ], corrige=True,
       notes="Faire nommer le mot qui fait la différence dans chaque cas : tolérer, "
             "dérangeante, déçue. Une plainte contient toujours un mot qui dit « ça ne "
             "va pas ».")

    d.vocabulaire('Au téléphone', "Des phrases prêtes à dire", [
        ("Je vous appelle parce que cette situation est vraiment dérangeante.", "Ouvrir."),
        ("Ça fait cinq semaines que ça dure et je ne peux plus le tolérer.", "Durée et limite."),
        ("Je suis fatiguée de devoir laisser mon auto dans la rue.", "L'effet sur moi."),
        ("Ce n'est pas contre vous, mais il faut que ça change.", "Garder la relation."),
        ("J'aimerais savoir ce que vous comptez faire cette semaine.", "Demande claire."),
        ("Est-ce que vous pourriez faire installer une affiche à l'entrée ?", "Demande précise."),
    ], notes="Faire répéter chacune avec un ton ferme mais calme. Le ton compte autant que "
             "les mots ; c'est le moment de le travailler explicitement.")

    d.piege('Ce qui affaiblit une plainte · 1',
            "Je m'excuse de vous déranger, ce n'est peut-être rien…",
            "Je vous appelle au sujet du bruit du vendredi soir.",
            "Trop d'excuses annonce à l'autre que le problème n'est pas important — et "
            "c'est exactement ce qu'il retiendra. On peut être poli sans s'effacer. "
            "« Bonjour, je vous appelle au sujet de… » est déjà poli, et ça ne diminue rien.",
            notes="Relier à la séance A1 : « je n'aime pas déranger les gens ». C'est la "
                  "même difficulté, et le module se termine dessus.")

    d.piege('Ce qui affaiblit une plainte · 2',
            "Vous êtes vraiment désordonné.",
            "Le corridor est encombré depuis un mois.",
            "Attaquer la personne fait fermer la porte immédiatement, et transforme un "
            "problème réglable en conflit durable. On se plaint d'une situation, jamais de "
            "quelqu'un. Le vouvoiement et le conditionnel — pourriez-vous, j'aimerais — "
            "gardent la porte ouverte à une solution.",
            notes="Renvoyer au dialogue de la séance C1 : Samir n'a jamais dit à "
                  "Jean-Philippe qu'il était désordonné, et il a obtenu ce qu'il voulait "
                  "en une conversation.")

    d.piege('Ce qui affaiblit une plainte · 3',
            "Il faudrait faire quelque chose.",
            "Pourriez-vous faire installer une affiche avant vendredi ?",
            "Sans demande précise ni délai, l'autre personne ne sait pas ce qu'on attend "
            "d'elle — et rien ne bouge. Une bonne demande contient un verbe d'action et, "
            "quand c'est possible, une date. Ce n'est pas de l'impatience : c'est ce qui "
            "rend la demande exécutable.",
            notes="Faire transformer collectivement trois demandes vagues du groupe en "
                  "demandes précises avec délai.")

    d.pratique('Production', 'Formulez votre plainte',
               "Trois temps : le fait, l'effet sur vous, la demande.", [
        ("Le calorifère de votre salon ne chauffe plus depuis trois jours. Il fait quatorze degrés.",
         "…ma fille tousse et je ne dors plus. J'aimerais que vous fassiez venir un électricien cette semaine."),
        ("Les visiteurs du logement voisin occupent votre case de stationnement.",
         "…j'ai dû laisser mon auto dans la rue trois soirs. Pourriez-vous faire installer une affiche ?"),
    ], corrige=True,
       notes="Faire écrire individuellement, puis lire deux ou trois productions à voix "
             "haute. Corriger la structure, pas le vocabulaire.")

    d.pratique('Production', 'Suite',
               "Même consigne. Deux situations plus difficiles.", [
        ("L'ascenseur est en panne depuis cinq jours et vous habitez au sixième étage.",
         "…je monte six étages avec mon épicerie et ma mère de 78 ans ne sort plus. J'aimerais savoir quand la réparation est prévue."),
        ("Une odeur de moisissure persiste dans votre salle de bain malgré vos nettoyages.",
         "…je suis inquiète pour la santé de mes enfants. Il faudrait faire installer un ventilateur."),
    ], corrige=True,
       notes="Le troisième cas justifie le degré 3 de l'échelle : cinq jours, une personne "
             "âgée. Faire remarquer que l'intensité se justifie par les faits, pas par "
             "l'humeur.")

    d.billet(
        "Écrivez votre plainte en trois temps, à partir de votre situation de la séance D1.",
        exemples=[
            "Le fait · l'effet sur vous · la demande, avec un verbe d'action et un délai.",
            "Trois phrases suffisent. Pas d'excuses au début.",
        ],
        notes="Fin du bloc D. Ces billets sont la matière première du jeu de rôle et du "
              "courriel de la séance E1 : les conserver soigneusement.")

    return d.save(dossier)
