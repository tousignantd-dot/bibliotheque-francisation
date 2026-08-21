# -*- coding: utf-8 -*-
"""E2 · Écrire à la clinique, et faire le bilan.
Bloc E « Je me lance » · couleur framboise · 75 min. Production écrite et bilan.
Source : bloc `appli` — production écrite — et « Je retiens des mots ».
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-rendezvous/images/')


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Écrire à la clinique, et faire le bilan",
        chapeau="La ligne est occupée depuis deux jours et le rendez-vous "
                "approche. Un courriel de six à dix phrases, factuel — et "
                "une demande claire se traite plus vite qu'une plainte.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Commencer par faire écouter deux "
                  "enregistrements de E1 choisis d'avance, avec l'accord des élèves. "
                  "Puis annoncer que la même histoire s'écrit aujourd'hui.")

    d.objectifs([
        "écrire un courriel de demande à un service, en six à dix phrases ;",
        "rester factuel plutôt que de se plaindre ;",
        "réemployer les temps du module : imparfait, passé composé, futur, subjonctif ;",
        "faire le bilan de ce qu'on sait faire maintenant.",
    ])

    d.declencheur(
        'Observation', "Deux courriels, la même demande. Lequel se traite le "
                       "premier ?",
        image=IMG + 'ordonnance-papier.jpg',
        pistes=[
            "« Ça fait trois fois que j'essaie de vous appeler, c'est inadmissible. »",
            "« Mon horaire de travail a changé le 1er juillet. »",
            "Lequel donne un fait ? Lequel donne une humeur ?",
            "Avec lequel peut-on agir tout de suite ?",
        ],
        notes="Personne ne défend jamais le premier, et pourtant c'est celui que la moitié "
              "du groupe écrirait spontanément. Le dire gentiment.")

    d.regle("Une demande claire se traite plus vite qu'une plainte",
            "On donne un fait, une date, et ce qu'on veut. Rien d'autre.",
            precision="La personne qui lit votre courriel n'est pas celle qui n'a pas "
                      "répondu au téléphone. Lui reprocher l'attente ne fait pas avancer "
                      "votre dossier ; lui donner votre numéro de carte et vos "
                      "disponibilités, oui.",
            notes="Diapositive à photographier, et à laisser affichée pendant l'écriture.")

    d.cartes("Ce que le courriel doit contenir", "Six éléments, six à dix phrases", [
        ("Qui vous êtes",
         "Nom, date de naissance, et le rendez-vous visé : date, heure, professionnel."),
        ("Ce que vous demandez",
         "Déplacer, et non annuler. Dit clairement, dès la deuxième phrase."),
        ("Pourquoi",
         "Une phrase, à l'imparfait et au passé composé. « Mon horaire a changé le 1er juillet. »"),
        ("Quand vous êtes libre",
         "Avec « à partir de », « avant », « d'ici ». C'est ce qui abrège tout le reste."),
        ("Une obligation, un engagement",
         "« Il faut que je sois au travail à sept heures. » · « Je serai là quinze minutes avant. »"),
        ("Comment vous joindre",
         "Un numéro, et le moment où vous répondez."),
    ], cols=3,
       notes="Les six éléments sont cochables : les élèves peuvent vérifier leur propre "
             "texte avant de demander la correction.")

    d.tableau('Le cadre du courriel', "Ce qui se met où",
              ['Ligne', 'Contenu'],
              [["À", "l'accueil de la clinique"],
               ["Objet", "Demande de déplacement — rendez-vous du 8 juillet, 11 h"],
               ["Première phrase", "Bonjour, je m'appelle… né le…"],
               ["Dernière phrase", "un numéro, un moment, et un remerciement"]],
              cle=0,
              note="Un objet qui nomme la date du rendez-vous fait gagner une journée.",
              notes="L'objet est la partie que les élèves négligent le plus, et c'est la "
                    "seule que le service lit avant d'ouvrir.")

    d.piege("Écrire au service comme à un ami",
            "« Salut, je peux pas venir le 8, tu peux changer ça ? »",
            "« Bonjour, je voudrais déplacer mon rendez-vous du 8 juillet. »",
            "Le courriel à un service commence par « Bonjour, » et emploie « vous ». Ce "
            "n'est pas de la distance : c'est ce qui fait traiter votre demande comme une "
            "demande.",
            notes="Le contraire existe aussi — le français de lettre du dix-neuvième "
                  "siècle. Rester simple et poli, c'est tout.")

    d.pratique('Production écrite', "Votre courriel, six à dix phrases",
               "Vérifiez les six éléments avant de demander la correction.", [
        ("Vous nommez-vous, avec votre date de naissance ?", "et le rendez-vous visé"),
        ("Dites-vous « déplacer » et non « annuler » ?", "les deux ne font pas la même chose"),
        ("Donnez-vous une raison, en une phrase ?", "imparfait et passé composé"),
        ("Dites-vous quand vous êtes libre ?", "à partir de, avant, d'ici"),
        ("Y a-t-il une obligation et un engagement ?", "il faut que… · je serai…"),
        ("Laissez-vous un numéro et un moment ?", "et vous remerciez"),
    ], corrige=True,
       notes="Faire écrire dans le module, puis demander la correction de l'assistant. "
             "Les élèves rapides peuvent écrire le second courriel : celui qui annule.")

    d.vocabulaire('Bilan', "Ce que vous savez faire maintenant", [
        ("Dire depuis quand", "depuis, ça fait… que, il y a — et le verbe au présent."),
        ("Téléphoner", "Une phrase pour ouvrir, deux pour le motif, sept lignes à noter."),
        ("Raconter", "Le début, le décor, ce qui a changé, aujourd'hui."),
        ("Dire à quel moment", "En me levant, en montant l'escalier, en me penchant."),
        ("Questionner", "Quatre questions, et « vous pouvez me le redire autrement ? »"),
        ("Déplacer et annuler", "Trois choses à dire, vingt-quatre heures, six éléments de message."),
    ], notes="Faire relire cette liste dans le module, section « Je retiens des mots », et "
             "compléter l'autoévaluation avant de terminer.")

    d.billet(
        "En une phrase : qu'est-ce que vous ferez différemment à votre prochain appel ?",
        exemples=[
            "Une seule chose, précise, que vous ferez vraiment.",
            "« Je noterai l'heure d'arrivée », « je demanderai le délai d'annulation »…",
        ],
        notes="Dernier billet du module. Les lire à voix haute, sans nommer les auteurs : "
              "c'est la meilleure révision possible en cinq minutes.")

    return d.save(dossier)
