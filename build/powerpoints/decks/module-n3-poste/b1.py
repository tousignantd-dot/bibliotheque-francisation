# -*- coding: utf-8 -*-
"""B1 · Combien ça coûte, combien de temps ça prend.
Bloc B « Défi 1 · Demander avant de choisir » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-poste/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Combien ça coûte, combien de temps ça prend',
        chapeau="Au comptoir, le prix et le délai ne s'affichent nulle part. "
                "Ils se demandent. La préposée répond à ce qu'on lui demande, "
                "et à rien d'autre.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Rappeler les quatre formules polies de la séance "
                  "A4 : elles servent dès la première réplique du dialogue d'aujourd'hui.")

    d.objectifs([
        "comprendre un échange complet au comptoir ;",
        "repérer les deux renseignements qui décident du choix ;",
        "entendre la différence entre deux services d'envoi ;",
        "savoir qu'on peut faire répéter un prix avant de dire oui.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qui se passe avant qu'on donne un prix ?",
        image=IMG + 'balance-colis.jpg',
        pistes=[
            "Pourquoi la préposée pose-t-elle la boîte là-dessus ?",
            "Est-ce que le prix dépend seulement du poids ?",
            "Qu'est-ce qu'elle doit savoir d'autre avant de répondre ?",
            "Qu'est-ce que vous demanderiez avant de choisir ?",
        ],
        notes="La réponse attendue est double : le poids et la destination. La vitesse "
              "de l'envoi vient ensuite, et c'est le client qui la choisit — c'est la "
              "découverte de la séance.")

    d.dialogue('Dialogue · 1 de 3', "Il va où, votre colis ?", [
        ("YASSINE", "Bonjour. Je voudrais envoyer ce colis, s'il vous plaît.", True),
        ("CAROLE", "Bonjour. Il va où, votre colis ?", True),
        ("YASSINE", "À Calgary, en Alberta.", False),
        ("CAROLE", "Parfait. Je le pèse. Deux kilos et cent grammes.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Présenter Carole, la préposée. Faire remarquer que la première question "
             "n'est pas « qu'est-ce que vous voulez » mais « il va où » : la destination "
             "vient avant tout.")

    d.dialogue('Dialogue · 2 de 3', "Ça dépend de la vitesse", [
        ("YASSINE", "Combien est-ce que ça coûte ?", True),
        ("CAROLE", "Ça dépend de la vitesse. Vous êtes pressé ?", True),
        ("YASSINE", "Pas trop. C'est un cadeau pour le douze du mois.", False),
        ("CAROLE", "Alors le colis standard suffit. C'est le moins cher.", True),
    ], notes="Le cœur du défi : la question du prix appelle une contre-question. "
             "Beaucoup d'élèves se figent à ce moment-là. Faire répéter « Pas trop » et "
             "« Oui, assez » : deux réponses courtes suffisent.")

    d.dialogue('Dialogue · 3 de 3', "Est-ce que vous pouvez répéter le prix ?", [
        ("YASSINE", "Combien de temps est-ce que ça prend ?", True),
        ("CAROLE", "De Québec à Calgary, comptez à peu près une semaine.", True),
        ("YASSINE", "Est-ce que vous pouvez répéter le prix, s'il vous plaît ?", True),
        ("CAROLE", "Bien sûr. Standard, vingt-deux dollars. Xpresspost, trente-huit dollars.", True),
    ], notes="La troisième réplique est celle de la séance A4, employée pour de vrai. "
             "Souligner qu'elle arrive AVANT le choix, pas après le paiement.")

    d.tableau('Analyse', "Deux services, deux prix, deux délais",
              ['Le service', 'Le délai', 'Le prix'],
              [["Le colis standard", "à peu près une semaine", "vingt-deux dollars"],
               ["L'Xpresspost", "un ou deux jours ouvrables", "trente-huit dollars"]],
              cle=0,
              note="Le repérage est compris dans les deux : il ne coûte pas un sou de plus.",
              notes="Diapo à photographier. Les prix sont ceux du scénario ; dire au "
                    "groupe qu'ils changent chaque année, mais que la façon de les "
                    "demander, elle, ne change pas.")

    d.regle("Ce qui décide du prix",
            "le poids, la destination, la vitesse",
            precision="Les deux premiers, la préposée les trouve toute seule : elle "
                      "pèse la boîte et elle lit l'adresse. Le troisième, c'est vous "
                      "qui le choisissez, et vous ne pouvez le choisir qu'après avoir "
                      "demandé le prix et le délai.",
            notes="Diapo à photographier. C'est la logique entière du défi 1 en une "
                  "phrase : demander d'abord, choisir ensuite.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("La préposée demande d'abord où va le colis.", "vrai"),
        ("Le colis pèse deux kilos et cent grammes.", "vrai"),
        ("Le prix est le même pour toutes les vitesses.", "faux — vingt-deux ou trente-huit dollars"),
        ("Le colis standard met à peu près une semaine jusqu'à Calgary.", "vrai"),
        ("Le repérage coûte un supplément.", "faux — il est compris dans les deux services"),
        ("Yassine fait répéter le prix avant de choisir.", "vrai"),
    ], corrige=True,
       notes="C'est l'exercice `t1vf` du module. Faire justifier chaque « faux » par la "
             "réplique exacte, comme en A1.")

    d.billet(
        "Écrivez ce que vous demanderiez en premier, avec vos mots.",
        exemples=[
            "Vous avez une boîte à envoyer à l'autre bout du pays.",
            "Deux questions suffisent : lesquelles ?",
        ],
        notes="Deux minutes. Ramasser : les billets montrent qui pose déjà les deux "
              "questions du défi et qui commence encore par « combien » tout seul.")

    return d.save(dossier)
