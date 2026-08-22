# -*- coding: utf-8 -*-
"""B1 · Trois jours, quatre retours en arrière
Bloc B « Défi 1 · Le déroulement du film » · couleur acier · 75 min.
Source : dialogue `t1` (bande-annonce et discussion), exercice `t1vf`,
quatre cartes de FC_CARDS de la section t1.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Trois jours, quatre retours en arrière",
        chapeau="« Les Marées de novembre » tient en trois jours, et recule "
                "quatre fois jusqu'en 1978. Un film difficile n'est presque "
                "jamais difficile à cause de ses mots.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 1. Projeter la bande-annonce avant tout "
                  "commentaire — deux minutes — puis laisser le silence trente "
                  "secondes. Les réactions spontanées valent mieux que la première "
                  "question.")

    d.objectifs([
        "repérer le déroulement d'un film malgré les retours en arrière ;",
        "nommer les signaux qui annoncent un changement d'époque ;",
        "distinguer une scène d'un retour en arrière ;",
        "employer les quatre mots du déroulement avec leur article.",
    ], notes="Le premier objectif est l'intention de compréhension orale du programme, "
             "mot pour mot : regarder un film pour en repérer le déroulement.")

    d.declencheur(
        'Observation', "Après la bande-annonce : qu'est-ce que tu sais déjà ?",
        pistes=[
            "Qui est le personnage principal, et où va-t-elle ?",
            "Combien de temps dure l'histoire, d'après ce qu'on t'a montré ?",
            "Qu'est-ce que la bande-annonce ne t'a pas dit ?",
            "Est-ce que tu sais comment ça finit ?",
        ],
        notes="La troisième piste est celle qui compte. Faire lister ce qui manque : "
              "c'est la démonstration en direct de ce qu'on a vu en A1.")

    d.dialogue('Dialogue · 1 de 3', "La bande-annonce", [
        ("NARRATEUR", "Novembre. Une maison vide au bord de l'eau. Estelle Bourgault revient dans le village où elle avait grandi, pour vider la maison de sa mère en trois jours.", True),
        ("NARRATEUR", "Elle croyait n'avoir que des boîtes à faire. Mais dans le tiroir du bas, il y avait une lettre qu'on ne lui avait jamais montrée.", True),
        ("NARRATEUR", "« Les Marées de novembre ». Un film d'Aurélie Pichette.", True),
        ("THÉRÈSE", "Bon. J'ai suivi, mais pas tout le temps. Il y a un moment où je ne savais plus si on était aujourd'hui ou avant.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Faire remarquer les deux plus-que-parfaits de la bande-annonce : « où "
             "elle avait grandi », « qu'on ne lui avait jamais montrée ». Ils "
             "reviennent en B3, on ne fait que les signaler.")

    d.dialogue('Dialogue · 2 de 3', "La scène du quai", [
        ("BRUNO", "Lequel ?", True),
        ("THÉRÈSE", "La scène du quai, avec le jeune homme et le chien. Elle arrive juste après la cuisine, et le lendemain matin, Estelle est encore dans la cuisine.", True),
        ("BRUNO", "Ça se suit très bien, mais pas dans l'ordre où c'est arrivé. La scène du quai, c'est un retour en arrière : novembre 1978. Le jeune homme, c'est son frère Réal.", True),
        ("THÉRÈSE", "Ah. Moi je pensais que c'était son fils.", True),
    ], notes="L'erreur de Thérèse est celle de la moitié du groupe, toujours. La "
             "nommer à voix haute déculpabilise et ouvre la séance suivante.")

    d.dialogue('Dialogue · 3 de 3', "Les trois signaux", [
        ("BRUNO", "Le film te l'avait dit avant, avec un détail : la mère dit « ton frère avait le même manteau ». Après cette phrase-là, tout le reste se replace.", True),
        ("THÉRÈSE", "Je n'ai pas entendu la phrase. J'étais en train de lire les sous-titres.", True),
        ("BRUNO", "Chez Pichette, il y a trois signaux : l'image devient plus froide, la musique disparaît, et le bruit de la mer revient.", True),
        ("THÉRÈSE", "Donc quand j'entends la mer, je suis en 1978.", True),
    ], notes="Écrire les trois signaux au tableau et les y laisser tout le bloc B. "
             "Ils servent en B2, et le quatrième item de l'exercice les réutilise.")

    d.tableau('Analyse', "Les trois signaux du film",
              ['Le signal', 'Ce qu\'il annonce'],
              [["l'image", "elle devient plus froide, presque grise"],
               ["la musique", "elle s'arrête net"],
               ["le son", "le bruit de la mer revient"],
               ["les trois ensemble", "on vient de reculer en novembre 1978"]],
              cle=0,
              note="Le son est le plus sûr : on peut manquer une couleur en lisant les sous-titres.",
              notes="Diapositive à photographier. La remarque sur les sous-titres est "
                    "vraie pour tout le groupe et rarement dite : lire coûte de "
                    "l'attention visuelle, et c'est l'image qui en paie le prix.")

    d.vocabulaire('Vocabulaire', "Les quatre mots du déroulement", [
        ("le déroulement", "L'ordre dans lequel les choses arrivent, du début jusqu'à la fin."),
        ("une scène", "Un morceau de film qui se passe dans un seul lieu et d'un seul tenant."),
        ("un retour en arrière", "Un passage qui montre ce qui s'était passé bien avant, puis qui revient."),
        ("le dénouement", "Le moment de la fin où l'on apprend enfin comment tout se termine."),
    ], notes="« Le dénouement » se pose ici avec une consigne de classe : on ne le "
             "raconte pas. La tenir jusqu'à E2, y compris entre élèves.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la bande-annonce et la discussion.", [
        ("Estelle revient vider la maison de sa mère en trois jours.", "vrai"),
        ("Le jeune homme du quai est le fils d'Estelle.", "faux - c'est son frère Réal"),
        ("Les retours en arrière se passent en novembre 1978.", "vrai"),
        ("Le film annonce chaque retour en arrière par trois signaux.", "vrai"),
        ("Estelle est arrivée au village le samedi matin.", "faux - le vendredi soir"),
        ("La réalisatrice suit sa règle jusqu'à la dernière image.", "faux - elle la casse une fois, exprès"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le dernier item "
             "annonce B2 : une règle cassée une fois est un effet, cassée trois fois "
             "c'est une erreur.")

    d.billet(
        "À quel moment as-tu perdu le fil, et qu'est-ce qui t'a fait décrocher ?",
        exemples=[
            "Une phrase suffit.",
            "Il n'y a pas de mauvaise réponse : tout le monde décroche une fois.",
        ],
        notes="Deux minutes. Ces billets décident du rythme de B2 : s'ils citent tous "
              "le même moment, c'est celui-là qu'il faut reprendre image par image.")

    return d.save(dossier)
