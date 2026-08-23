# -*- coding: utf-8 -*-
"""B1 · La contre-proposition
Bloc B « Défi 1 · L'avis du propriétaire » · couleur acier · compréhension
orale · 75 min.
Source : dialogue `t1`, exercice `t1vf` et son bandeau de cinq mots.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="La contre-proposition",
        chapeau="Sokhna a lu l'avis trois fois et appelé le service de "
                "renseignements. Elle entre dans la cuisine avec un chiffre, "
                "une raison et une contrepartie.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Rappeler en trois minutes les chiffres de A1 — "
                  "940, 1 024, 84, un mois — avant de faire écouter. Le dialogue ne se "
                  "comprend pas sans eux.")

    d.objectifs([
        "suivre une négociation de vingt-trois répliques sans la voir écrite ;",
        "repérer la première offre, la contre-offre et l'entente finale ;",
        "reconnaître une contrepartie quand elle est offerte ;",
        "employer cinq mots de la négociation.",
    ], notes="Le deuxième objectif se travaille à l'écoute : faire noter les trois "
             "montants au fil de l'écoute, sans arrêter l'audio.")

    d.declencheur(
        'Avant d\'écouter', "Que diriez-vous à sa place ?",
        pistes=[
            "Accepteriez-vous les 84 $ sans rien dire ?",
            "Refuseriez-vous sans rien proposer d'autre ?",
            "Qu'est-ce que vous pourriez offrir en échange ?",
            "Est-ce que sept ans sans retard, ça se dit ou ça se garde pour soi ?",
        ],
        notes="Recueillir trois réponses, les écrire au tableau, et y revenir après "
              "l'écoute pour comparer avec ce que Sokhna fait réellement.")

    d.dialogue('Dialogue · 1 de 3', "Ce n'est pas la hausse, c'est le montant", [
        ("SOKHNA", "Trois fois. Et j'ai appelé le service de renseignements du Tribunal. J'aimerais vous faire une proposition, si vous permettez.", True),
        ("GÉRALD", "Allez-y.", False),
        ("SOKHNA", "Ce qui me dérange, ce n'est pas que le loyer monte. C'est qu'il monte de quatre-vingt-quatre dollars d'un coup, la même année où la fenêtre de la chambre ne ferme plus.", True),
        ("GÉRALD", "La fenêtre de la chambre. C'est la première fois que j'en entends parler.", True),
        ("SOKHNA", "Je vous l'ai dit en février, au téléphone. Mais je ne vous l'ai jamais écrit, et c'est mon erreur.", True),
    ], consigne="Écouter deux fois, diapositive masquée.",
       notes="La troisième réplique est la phrase emphatique du défi ; elle revient en "
             "B4. La cinquième montre une concession honnête : elle reconnaît son tort, "
             "et c'est ce qui lui donne le droit de demander.")

    d.dialogue('Dialogue · 2 de 3', "Quarante-cinq, et la fenêtre", [
        ("SOKHNA", "Je proposerais quarante-cinq dollars au lieu de quatre-vingt-quatre, et la fenêtre changée avant l'hiver.", True),
        ("GÉRALD", "Quarante-cinq, ça ne couvre même pas la taxe.", True),
        ("SOKHNA", "Peut-être. Mais une fenêtre neuve, c'est votre immeuble qui la garde, pas moi. Moi, je pars un jour ; elle reste.", True),
        ("GÉRALD", "Ça, c'est vrai.", False),
    ], notes="Faire remarquer l'argument de la troisième réplique : elle ne parle pas "
             "de son confort à elle, elle parle de la valeur de l'immeuble à lui. "
             "C'est ce qui fait bouger le propriétaire.")

    d.dialogue('Dialogue · 3 de 3', "Deux lignes avec la date", [
        ("SOKHNA", "Est-ce que vous accepteriez de me le mettre par écrit ? Deux lignes, avec la date, et vos initiales.", True),
        ("GÉRALD", "Vous ne me faites pas confiance ?", True),
        ("SOKHNA", "Je vous fais confiance. C'est à ma mémoire que je ne fais pas confiance, et à la vôtre non plus, avec six logements sur les bras.", True),
        ("GÉRALD", "Cinquante-cinq. Je vous écris les deux lignes ce soir.", True),
    ], notes="La réponse de Sokhna à « vous ne me faites pas confiance ? » est la "
             "phrase la plus utile du module. La faire répéter par trois élèves, telle "
             "quelle : elle se réemploie dans n'importe quelle négociation.")

    d.vocabulaire('Vocabulaire', "Cinq mots de la négociation", [
        ("une contre-proposition", "Une réponse qui garde la discussion ouverte : elle porte toujours un chiffre et une raison."),
        ("une contrepartie", "Ce que vous offrez en retour. C'est l'argument le plus solide, parce qu'il ne demande rien."),
        ("une entente écrite", "Une date, ce qui est convenu, deux initiales. Ce qui compte, c'est de pouvoir la relire dans six mois."),
        ("un compromis", "Les deux personnes sont un peu déçues, et les deux repartent avec quelque chose."),
        ("les travaux d'entretien", "Garder le logement en bon état fait partie des obligations du propriétaire, ce n'est pas une faveur."),
    ], notes="Le cinquième mot est celui que le groupe ignore le plus souvent. Y "
             "insister : l'entretien n'est pas un service qu'on quémande.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la discussion dans la cuisine.", [
        ("Sokhna a appelé le service de renseignements avant de proposer quelque chose.", "vrai"),
        ("Elle reproche au propriétaire de ne pas avoir le droit d'augmenter le loyer.", "faux - elle discute le montant"),
        ("Elle avait signalé la fenêtre en février, mais seulement au téléphone.", "vrai"),
        ("Monsieur Lheureux accepte les quarante-cinq dollars tout de suite.", "faux - il propose soixante"),
        ("L'entente finale est de cinquante-cinq dollars, avec un vitrier.", "vrai"),
        ("Sokhna refuse l'écrit pour ne pas froisser son propriétaire.", "faux - c'est elle qui le demande"),
    ], corrige=True,
       notes="Six des huit items de t1vf. Faire justifier chaque « faux » par la "
             "réplique exacte : c'est l'exercice d'écoute, pas l'exercice de mémoire.")

    d.billet(
        "Quelle contrepartie pourrais-tu offrir, toi, dans une négociation ?",
        exemples=[
            "Quelque chose qui ne te coûte rien mais qui a de la valeur pour l'autre.",
            "Une phrase suffit.",
        ],
        notes="Deux minutes. Les réponses servent en B4 : signer tout de suite, "
              "accepter une date, ne plus revenir dessus sont toutes des contreparties.")

    return d.save(dossier)
