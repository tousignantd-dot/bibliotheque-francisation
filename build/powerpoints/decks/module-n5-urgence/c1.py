# -*- coding: utf-8 -*-
"""C1 · « Racontez-moi ce qui est arrivé, du début. »
Bloc C « Défi 2 · Le triage et l'attente » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-urgence/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="« Racontez-moi ce qui est arrivé, du début. »",
        chapeau="Au 9-1-1, on répondait en trois mots. Au triage, c'est le "
                "contraire : quatre minutes de récit, et ce qu'on raconte "
                "pèse dans la décision.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2. Marquer le contraste avec le bloc B : la même "
                  "nuit, la même personne, mais un genre de discours complètement "
                  "différent. C'est ce que le niveau 5 demande — savoir changer de "
                  "registre selon la situation.")

    d.objectifs([
        "raconter au triage ce qui est arrivé, dans l'ordre ;",
        "distinguer ce qui durait de ce qui vient d'arriver ;",
        "répondre aux questions de l'infirmière sans se perdre ;",
        "comprendre ce qu'est un niveau de priorité.",
    ])

    d.declencheur(
        'Observation', "Voici le comptoir où tout se décide. Quatre minutes, une "
                       "infirmière, et un chiffre de 1 à 5.",
        image=IMG + 'triage.jpg',
        pistes=[
            "Qu'est-ce qu'elle a besoin de savoir, exactement ?",
            "Par où commence-t-on un récit ?",
            "Pourquoi l'heure de la chute est-elle importante ?",
            "Qu'est-ce qui décide de l'ordre de passage ?",
        ],
        notes="Faire deviner la durée du triage : les élèves répondent souvent « une "
              "heure ». C'est moins de cinq minutes, et cette brièveté explique tout le "
              "reste de la séance.")

    d.dialogue('Dialogue · 1 de 3', "Le récit, du début", [
        ("KARINE", "Bonsoir. Karine, infirmière au triage. C'est vous qui accompagnez "
                   "madame Quintero ?", True),
        ("MARISOL", "Oui, je suis sa fille. Marisol.", True),
        ("KARINE", "Racontez-moi ce qui est arrivé, du début.", True),
        ("MARISOL", "Elle avait de la fièvre depuis mercredi et elle mangeait très "
                    "peu. Cette nuit, elle s'est levée pour aller à la toilette et "
                    "elle est tombée dans l'escalier.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Le cœur de la séance tient dans la dernière réplique : deux imparfaits, "
             "puis deux passés composés. Le faire remarquer sans encore l'expliquer — "
             "la séance C2 s'en chargera.")

    d.dialogue('Dialogue · 2 de 3', "Les questions, et le niveau", [
        ("KARINE", "Est-ce qu'elle a perdu connaissance ?", True),
        ("MARISOL", "Je ne l'ai pas vue tomber. Quand je suis arrivée en bas, elle me "
                    "parlait déjà.", True),
        ("KARINE", "Chaque personne qui arrive reçoit un niveau, de un à cinq. Un, "
                   "c'est une vie en danger, on entre tout de suite. Cinq, c'est ce "
                   "qui peut attendre longtemps.", True),
        ("KARINE", "Je la mets à trois. Une fracture possible chez une dame de "
                   "soixante et onze ans, avec de la fièvre, ça ne reste pas dans le "
                   "corridor toute la nuit.", True),
    ], notes="Noter la réponse de Marisol : elle ne dit pas non, elle dit ce qu'elle sait "
             "et ce qu'elle n'a pas vu. C'est exactement la bonne réponse.")

    d.dialogue('Dialogue · 3 de 3', "L'attente, et ce qu'on ne promet pas", [
        ("MARISOL", "Ça veut dire combien d'attente ?", True),
        ("KARINE", "Je ne peux pas vous promettre une heure. Ce soir, il y a deux "
                   "priorités un. Si une ambulance arrive avec un cas plus grave, il "
                   "passe avant elle, même s'il est arrivé après.", True),
        ("KARINE", "Une dernière chose : est-ce qu'elle a des allergies ?", True),
        ("MARISOL", "Aux antibiotiques, je crois. Il faudrait vérifier avec mon "
                    "frère.", False),
    ], notes="La question des allergies bloque presque toutes les familles. Annoncer "
             "qu'elle reviendra au défi 3, quand Julio donnera la réponse au téléphone.")

    d.regle("L'ordre d'arrivée ne compte pas",
            "Une personne arrivée après vous passera avant si son niveau est plus urgent.",
            precision="Ce n'est ni un oubli ni une injustice : c'est le fonctionnement "
                      "même du triage. La seule chose à faire pendant l'attente est de "
                      "retourner au comptoir si l'état empire.",
            notes="Diapositive à photographier. Elle change complètement le vécu d'une "
                  "nuit d'attente — beaucoup d'élèves croient avoir été oubliés.")

    d.cartes("Ce que le triage veut entendre", "Quatre choses, dans cet ordre", [
        ("Ce qui est arrivé", "Le récit court, avec l'heure : « vers deux heures »."),
        ("Ce qui durait avant", "La fièvre depuis mercredi, le peu d'appétit."),
        ("Ce que vous ne savez pas", "« Je ne l'ai pas vue tomber » vaut mieux qu'un "
                                     "« non » incertain."),
        ("Le dossier", "Médicaments, allergies, carte d'assurance maladie."),
    ], notes="Conseiller d'apporter la boîte de médicaments elle-même. C'est le conseil "
             "pratique le plus utile du module après celui de l'adresse.")

    d.piege("Raconter tout au même temps",
            "Elle a eu de la fièvre, elle a mangé peu, elle est tombée.",
            "Elle avait de la fièvre, elle mangeait peu, et elle est tombée.",
            "Au passé composé partout, on ne distingue plus ce qui durait de ce qui vient "
            "d'arriver. L'infirmière perd l'information la plus utile : la fièvre "
            "précédait la chute.",
            notes="C'est l'annonce de la séance C2. Ne pas expliquer maintenant, seulement "
                  "faire entendre la différence.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("L'infirmière demande de raconter depuis le début.", "vrai"),
        ("À l'urgence, on entre dans l'ordre d'arrivée.", "faux — selon le niveau"),
        ("Le niveau 1 veut dire que le cas peut attendre.", "faux — vie en danger"),
        ("Amparo reçoit un niveau 3.", "vrai"),
        ("L'infirmière promet une durée d'attente précise.", "faux — elle ne le peut pas"),
        ("Deux personnes peuvent accompagner la patiente.", "faux — une seule"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Racontez en trois phrases ce qui est arrivé à Amparo.",
        exemples=[
            "Première phrase : ce qui durait avant.",
            "Deuxième : ce qui est arrivé, avec l'heure. Troisième : ce que vous avez fait.",
        ],
        notes="Ramasser sans corriger les temps : ils seront le sujet de C2. Se contenter "
              "de vérifier l'ordre des trois phrases.")

    return d.save(dossier)
