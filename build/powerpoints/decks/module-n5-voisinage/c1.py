# -*- coding: utf-8 -*-
"""C1 · « Un message dans le répondeur »
Bloc C « Défi 2 · Le message et le mot » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2a`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-voisinage/vocab/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="« Un message dans le répondeur »",
        chapeau="Personne ne décroche du premier coup. Une voisine travaille "
                "de nuit, l'autre est au travail, la troisième dort : entre "
                "voisins, on se parle surtout par répondeur et par petits "
                "papiers.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2. Demander au groupe : quand vous appelez quelqu'un "
                  "et que ça ne répond pas, est-ce que vous laissez un message ? Beaucoup "
                  "répondent non — par gêne, ou parce qu'ils ne savent pas quoi dire en "
                  "trente secondes. C'est exactement ce que la séance travaille.")

    d.objectifs([
        "comprendre un message laissé sur un répondeur, écouté une fois ;",
        "repérer les cinq renseignements qu'un bon message contient ;",
        "noter une date, un numéro et une heure pendant l'écoute ;",
        "comprendre pourquoi une note s'écrit pour quelqu'un d'autre que soi.",
    ], notes="Le troisième objectif est une compétence de survie : personne ne redemande "
             "un numéro à un répondeur. Fournir du papier avant l'écoute, pas après.")

    d.declencheur(
        'Observation', "Un voyant rouge qui clignote. Qu'est-ce que vous "
                       "faites avant d'appuyer ?",
        image=IMG + 'repondeur.jpg',
        pistes=[
            "Est-ce que vous prenez un crayon avant d'écouter ?",
            "Combien de fois pouvez-vous réécouter un message ?",
            "Qu'est-ce que vous notez en premier : le nom, ou le numéro ?",
            "Si quelqu'un d'autre lit votre note, est-ce qu'il comprendra ?",
        ],
        notes="La première piste est le geste que la séance veut installer : prendre le "
              "crayon avant d'appuyer. La dernière est le test de Réjean, qui reviendra "
              "en C4.")

    d.dialogue('Dialogue · 1 de 3', "Le message de madame Faye", [
        ("NDEYE", "Bonsoir madame Vergara, c'est Ndeye Faye, du troisième.", True),
        ("NDEYE", "Je voulais vous dire deux choses. D'abord, je ne peux pas "
                  "venir à la fête du 7 : je travaille de midi à minuit ce "
                  "jour-là.", True),
        ("NDEYE", "Ensuite, je cherche quelqu'un pour arroser mes plantes du "
                  "10 au 20 juillet. Je pars au Sénégal avec le petit.", True),
        ("NDEYE", "Si ça vous intéresse, rappelez-moi au 514 555-0148, après "
                  "trois heures de l'après-midi. Pas avant, je dors.", True),
    ], consigne="Écoutez une seule fois, crayon en main.",
       notes="Faire écouter une première fois sans rien dire, puis demander ce que chacun "
             "a noté. L'écart entre les cahiers est le vrai contenu de la séance. "
             "Réécouter ensuite une seconde fois, jamais plus.")

    d.dialogue('Dialogue · 2 de 3', "« Vous avez tout compris, vous ? »", [
        ("MARISOL", "Vous avez tout compris, vous ?", True),
        ("RÉJEAN", "J'ai compris qu'elle ne vient pas. Le reste, non.", True),
        ("MARISOL", "Elle demande si je peux arroser ses plantes en juillet. "
                    "Du 10 au 20.", True),
        ("RÉJEAN", "Écrivez-le, sinon dans deux jours il n'en restera rien.", True),
    ], notes="Réjean, qui est né ici, n'a pas tout compris non plus. Le faire remarquer : "
             "ce n'est pas une question de langue maternelle, c'est une question "
             "d'attention et de crayon. Ça détend beaucoup le groupe.")

    d.dialogue('Dialogue · 3 de 3', "Écrire pour quelqu'un d'autre", [
        ("MARISOL", "J'écris quoi ? « Ndeye, plantes, juillet » ?", True),
        ("RÉJEAN", "Écrivez-le pour quelqu'un d'autre que vous. Si votre "
                   "fils lit ce papier, est-ce qu'il comprend ?", True),
        ("MARISOL", "Non. Il ne sait pas qui est Ndeye.", True),
        ("RÉJEAN", "Alors mettez le nom au complet, l'étage, la date, ce "
                   "qu'elle demande et le numéro.", False),
    ], notes="La question de Réjean est le critère de tout le défi 2, et elle s'applique "
             "aussi bien à la maison qu'au travail. L'écrire au tableau et l'y laisser "
             "jusqu'à C4.")

    d.regle("Cinq renseignements dans un message",
            "Qui parle et d'où · pourquoi on appelle · les faits, lentement · "
            "ce qu'on attend · le numéro et le moment où rappeler.",
            precision="Le dernier est celui qu'on oublie le plus. Sans le moment, "
                      "on vous rappelle à huit heures du matin ; sans le numéro, on "
                      "ne vous rappelle pas du tout.",
            notes="Diapositive à photographier. Les cinq renseignements sont exactement le "
                  "plan de la production orale de la séance E1.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le message entendu.", [
        ("Ndeye Faye se nomme dès la première phrase.", "vrai"),
        ("Elle dit à quel étage elle habite.", "vrai"),
        ("Elle appelle pour une seule raison.", "faux — elle en annonce deux"),
        ("Elle part au Sénégal du 10 au 20 juillet.", "vrai"),
        ("Elle cherche quelqu'un pour garder son fils.", "faux — pour arroser ses plantes"),
        ("On peut la rappeler le matin.", "faux — après trois heures, elle dort le matin"),
        ("Elle explique pourquoi elle n'a pas rappelé plus tôt.", "vrai — elle était de nuit"),
    ], corrige=True,
       notes="Exercice t2a de l'activité. Faire justifier chaque réponse par la phrase "
             "exacte du message : c'est ce travail de retour au texte qui prépare la note "
             "écrite de C4.")

    d.piege("Écouter d'abord, noter ensuite",
            "J'écoute tout, puis j'écris ce dont je me souviens.",
            "Je prends le crayon avant d'appuyer sur la touche.",
            "Un numéro de téléphone ne se retient pas pendant vingt secondes, et un "
            "répondeur ne répète pas. Ce qui n'est pas noté pendant l'écoute est perdu.",
            notes="Vérifiable sur place : demander qui a noté le numéro correctement à la "
                  "première écoute. Le résultat parle de lui-même.")

    d.billet(
        "Écrivez ce que vous notez d'un message : les cinq mots-clés, dans l'ordre.",
        exemples=[
            "Qui, quand, quoi, les dates, comment rappeler.",
            "Écrivez-les comme vous les écririez sur un vrai papier, en abrégé.",
        ],
        notes="Ramasser. Les abréviations que les élèves emploient déjà sont un excellent "
              "point de départ pour C4.")

    return d.save(dossier)
