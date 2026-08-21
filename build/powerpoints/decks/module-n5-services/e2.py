# -*- coding: utf-8 -*-
"""E2 · Le courriel de relance, et le bilan.
Bloc E « Je me lance » · couleur framboise · 75 min. Production écrite et clôture.
Source : bloc `appli` — production écrite ; section `retiens`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Le courriel de relance",
        chapeau="Une semaine a passé et rien n'est arrivé. Un courriel qui "
                "accuse se traite moins vite qu'un courriel qui informe — "
                "et il tient en dix phrases, numéro de requête compris.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Prévoir du temps pour le bilan et "
                  "l'autoévaluation : ils font partie de la séance, ils ne sont pas ce "
                  "qu'on coupe quand on a pris du retard.")

    d.objectifs([
        "écrire un courriel de relance à un service public ;",
        "rappeler une démarche au passé composé et à l'imparfait ;",
        "poser deux demandes en subordonnée interrogative ;",
        "faire le bilan de ce qu'on est maintenant capable de faire.",
    ])

    d.declencheur(
        'Comparaison', "Deux courriels. Lequel sera traité en premier ?",
        pistes=[
            "« Ça fait trois fois que je vous écris, c'est inadmissible. »",
            "« Le bac n'a toujours pas été vidé. Requête 24-118-7690, ouverte le 12 mai. »",
            "Lequel donne le plus d'information ?",
            "Lequel donne le plus envie de répondre ?",
        ],
        notes="Les élèves choisissent le second sans hésiter, mais écrivent souvent le "
              "premier quand ils sont fâchés. Nommer cet écart : c'est le vrai sujet de "
              "la séance.")

    d.regle("Restez factuel : c'est ce qui va vite",
            "Un courriel qui informe se traite ; un courriel qui accuse se transmet.",
            precision="Un service public ne juge pas votre ton, mais il traite d'abord ce "
                      "qu'il peut traiter. Un numéro de requête, une date, un fait : "
                      "voilà de quoi agir. La colère, elle, doit d'abord être lue par "
                      "quelqu'un d'autre avant que rien ne bouge.",
            notes="Diapositive à photographier. Dire aussi qu'on a le droit d'être fâché : "
                  "il s'agit de la stratégie, pas du sentiment.")

    d.tableau('Les cinq éléments du courriel', "Rien de plus, rien de moins",
              ['Élément', 'Exemple'],
              [["Le numéro et la date", "« la requête 24-118-7690, ouverte le mardi 12 mai »"],
               ["Le rappel de la situation", "« J'avais appelé parce que mon bac n'était pas ramassé. »"],
               ["Le délai annoncé", "« On m'avait annoncé trois jours ouvrables. »"],
               ["Deux demandes en subordonnée", "« Je voudrais savoir si… », « Pouvez-vous me dire… »"],
               ["La suite et vos coordonnées", "« Si rien ne bouge d'ici vendredi, je rappellerai. »"]],
              cle=0,
              note="De six à dix phrases. Au-delà, le courriel perd son lecteur.",
              notes="Diapositive à photographier. C'est la grille exacte du cadre de "
                    "document dans le module : les élèves la retrouveront à l'écran.")

    d.cartes("La forme du courriel", "Quatre repères", [
        ("L'objet",
         "« Requête 24-118-7690 — collecte non effectuée, suivi ». Le numéro dans l'objet."),
        ("L'ouverture",
         "« Bonjour, » puis « Je vous écris au sujet de… » — et « vous » du début à la fin."),
        ("Le corps",
         "Le passé composé pour les étapes, l'imparfait pour le décor. Comme en D2."),
        ("La clôture",
         "Une formule de salutation, votre nom, et un numéro où vous joindre."),
    ], notes="La première carte est celle qu'on oublie : un objet sans numéro oblige le "
             "service à chercher, et le courriel attend.")

    d.pratique('Écriture', "Écrivez les phrases une à une",
               "Une phrase par élément, avant de rédiger le courriel complet.", [
        ("Le numéro et la date de votre appel",
         "« Je vous écris au sujet de la requête … , ouverte le … »"),
        ("Le rappel, à l'imparfait",
         "« J'avais appelé parce que … »"),
        ("Ce qui avait été annoncé",
         "« On m'avait annoncé un délai de … »"),
        ("L'état actuel, au présent",
         "« À ce jour, … »"),
        ("Une demande avec « si »",
         "« Je voudrais savoir si … »"),
        ("Une demande avec « ce que » ou un autre mot",
         "« Pouvez-vous me dire … »"),
        ("La suite",
         "« Si … , je … »"),
    ], corrige=False,
       notes="Quinze minutes. Faire écrire les sept phrases séparément avant d'assembler : "
             "les élèves qui rédigent d'un trait produisent presque toujours du hors-sujet.")

    d.piege("Écrire un courriel sans numéro de requête",
            "« Bonjour, j'avais appelé la semaine dernière au sujet de mon bac. »",
            "« Bonjour, je vous écris au sujet de la requête 24-118-7690, ouverte le 12 mai. »",
            "Sans numéro, le service doit chercher — par nom, par adresse, par date — et "
            "votre courriel attend derrière ceux qui en ont un. Le numéro n'est pas un "
            "détail administratif : c'est ce qui rend la relance possible.",
            notes="Boucler avec la règle de B1 : une demande sans requête n'existe pas. "
                  "Les élèves font le lien eux-mêmes, et c'est le moment de le souligner.")

    d.vocabulaire('Bilan · les mots à emporter', "Les huit qui servent partout", [
        ("une requête", "la demande enregistrée, avec son numéro"),
        ("un délai", "le temps annoncé, en jours ouvrables"),
        ("un préposé", "la personne qui répond, au téléphone ou au comptoir"),
        ("en vigueur", "ce qui s'applique aujourd'hui"),
        ("une pièce justificative", "le document qui prouve ce que vous déclarez"),
        ("une preuve de résidence", "le papier qui montre où vous habitez"),
        ("le cas échéant", "si cela s'applique à vous"),
        ("un jour ouvrable", "du lundi au vendredi, sauf les fériés"),
    ], notes="Ces huit-là dépassent le module : ils servent à la RAMQ, à la SAAQ, à "
             "l'école, à l'assurance. Le dire explicitement en terminant.")

    d.pratique('Autoévaluation', "Qu'est-ce que je suis capable de faire ?",
               "Pour chaque énoncé : pas encore, un peu, ou oui.", [
        ("Je peux téléphoner à un service et dire en une phrase pourquoi j'appelle.", ""),
        ("Je pose mes questions avec « Pouvez-vous me dire… ».", ""),
        ("Je note un numéro de requête et je le répète pour le confirmer.", ""),
        ("Je comprends la différence entre trois jours et trois jours ouvrables.", ""),
        ("Je trouve l'encadré qui compte dans une page de service public.", ""),
        ("Je comprends les mots d'un formulaire officiel.", ""),
        ("Je peux me présenter à un guichet et raconter ce que j'ai déjà essayé.", ""),
        ("Je peux écrire à un service pour relancer une demande.", ""),
    ], corrige=False,
       notes="L'autoévaluation se fait aussi dans le module, à l'écran. La faire ici à "
             "l'oral, en groupe : les élèves découvrent qu'ils ne sont pas seuls à hésiter "
             "sur les mêmes lignes.")

    d.billet(
        "Terminez le module en ligne : envoyez votre courriel et votre enregistrement.",
        exemples=[
            "Le module garde votre avancement : vous pouvez finir à la maison.",
            "Et la semaine prochaine, faites une vraie démarche avec ce que vous savez.",
        ],
        notes="Dernier billet du module. La seconde consigne est la vraie : tout ce "
              "module ne sert que si une démarche réelle est tentée dans les jours qui "
              "suivent. Le dire une dernière fois.")

    return d.save(dossier)
