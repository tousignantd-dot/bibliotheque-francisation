# -*- coding: utf-8 -*-
"""B1 · Le covoiturage du jeudi.
Bloc B « Défi 1 · Ce que je fais de mes semaines » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Le covoiturage du jeudi',
        chapeau="Chantal offre de passer prendre Mariama. Une offre d'aide de "
                "deux phrases devient une vraie conversation : depuis quand tu "
                "joues, qui t'a amenée, où on va en avril.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc B. Rappeler en une phrase où on en était : Mariama et "
                  "Chantal se sont parlé au vestiaire la semaine d'avant.")

    d.objectifs([
        "comprendre un échange informel entre deux personnes qui se connaissent peu ;",
        "repérer comment une offre d'aide ouvre une conversation ;",
        "raconter comment j'ai connu une activité ou un lieu ;",
        "reconnaître les questions qui relancent l'échange.",
    ])

    d.declencheur(
        'Mise en situation', "Quelqu'un vous offre de vous ramener en voiture. Que dites-vous ?",
        pistes=[
            "Comment acceptez-vous sans avoir l'air de profiter ?",
            "Quelle question posez-vous en retour ?",
            "Qu'est-ce qui vous gêne dans une offre comme celle-là ?",
            "Est-ce que ça se fait, ici, entre gens qui se connaissent peu ?",
        ],
        notes="Cinq minutes. Beaucoup d'élèves diront qu'ils refuseraient. C'est exactement "
              "le sujet : au Québec, accepter une offre de covoiturage est ordinaire et "
              "n'engage à rien.")

    d.dialogue('Dialogue · 1 de 3', "L'offre", [
        ("CHANTAL", "Si tu veux, je peux venir te chercher le jeudi. Je passe devant l'hôpital de toute façon.", True),
        ("MARIAMA", "Tu ferais ça ? L'autobus que je prends s'arrête à trois coins de rue d'ici.", False),
        ("CHANTAL", "Ça ne me dérange pas. C'est le trajet que je fais chaque semaine.", True),
        ("MARIAMA", "Merci beaucoup. Le gymnase où on joue n'est pas facile à trouver en autobus le soir.", False),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Les répliques teintées contiennent la formule qui rend l'offre acceptable : "
             "« de toute façon », « ça ne me dérange pas ». Les écrire au tableau. "
             "Trois « qui / que / où » apparaissent déjà ici — les faire remarquer sans "
             "les expliquer : c'est la séance B2.")

    d.dialogue('Dialogue · 2 de 3', "Depuis quand tu joues ?", [
        ("CHANTAL", "Tu joues depuis longtemps ? Tu sers mieux que la moitié de l'équipe.", False),
        ("MARIAMA", "Dans mon pays, je jouais au volleyball trois fois par semaine. Ici, j'ai arrêté pendant un an.", True),
        ("CHANTAL", "Pourquoi tu as arrêté ?", False),
        ("MARIAMA", "Je ne connaissais personne et je ne savais pas où aller. C'est une collègue qui m'a parlé du centre.", True),
    ], notes="« Je jouais » et « je ne connaissais personne » : premier imparfait du module. "
             "Le signaler, sans l'enseigner — le bloc C s'en charge. Ici, on veut seulement "
             "que le sens passe.")

    d.dialogue('Dialogue · 3 de 3', "Six ans dans la même équipe", [
        ("CHANTAL", "C'est souvent comme ça. Moi, c'est ma voisine qui m'a amenée la première fois, il y a six ans.", True),
        ("MARIAMA", "Six ans dans la même équipe !", False),
        ("CHANTAL", "La même équipe, oui. Les gens que je vois le jeudi, c'est presque ma famille maintenant.", True),
        ("MARIAMA", "Et le tournoi dont Julie parlait tantôt, c'est quand ?", False),
    ], notes="« Six ans dans la même équipe ! » est une des exclamations travaillées en A3. "
             "Faire réécouter l'extrait et redemander : est-ce une question ?")

    d.cartes('Ce que le dialogue enseigne', "Quatre choses à retenir", [
        ("Une offre se refuse rarement",
         "« Ça ne me dérange pas », « je passe devant de toute façon » : ces formules "
         "existent pour vous permettre d'accepter sans gêne. Elles sont sincères."),
        ("On demande depuis quand",
         "« Tu joues depuis longtemps ? » est la question la plus fréquente quand on "
         "rencontre quelqu'un dans une activité. Préparez votre réponse."),
        ("On raconte qui nous a amené",
         "Presque personne n'arrive seul dans une activité. Dire « c'est une collègue qui "
         "m'a parlé du centre » est une réponse complète et naturelle."),
        ("On finit par une invitation",
         "La conversation se termine sur le tournoi d'avril. Une rencontre réussie ouvre "
         "sur une prochaine fois."),
    ], notes="La deuxième carte est celle à préparer : faire écrire à chacun sa réponse à "
             "« tu fais ça depuis longtemps ? » pour une activité de sa vie.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Chantal doit faire un détour pour passer à l'hôpital.", "faux — elle passe devant de toute façon"),
        ("Mariama jouait trois fois par semaine dans son pays.", "vrai"),
        ("Elle a joué sans interruption depuis son arrivée.", "faux — elle a arrêté pendant un an"),
        ("C'est une collègue qui lui a parlé du centre.", "vrai"),
        ("Chantal joue dans cette équipe depuis deux ans.", "faux — depuis six ans"),
        ("Le tournoi a lieu à Drummondville, en avril.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. C'est de la "
             "compréhension fine, pas de la mémoire.")

    d.regle("Ce qu'il faut retenir",
            "Une conversation informelle avance par questions courtes, pas par longs récits.",
            precision="Chantal pose cinq questions en douze répliques. Chacune tient en "
                      "moins de dix mots. C'est ce rythme qui rend l'échange agréable — "
                      "un long monologue, même correct, referme la conversation.",
            notes="Compter les questions avec le groupe, à même la diapo du dialogue. "
                  "Le constat frappe plus qu'une explication.")

    d.billet(
        "Racontez en trois phrases comment vous avez connu une activité, un lieu ou un emploi.",
        exemples=[
            "Qui vous en a parlé ? Quand ? Qu'est-ce qui s'est passé ensuite ?",
            "Exemple : « C'est une collègue qui m'a parlé du centre. »",
        ],
        notes="Ces billets serviront directement à la production orale de E1. Les ramasser "
              "et les garder.")

    return d.save(dossier)
