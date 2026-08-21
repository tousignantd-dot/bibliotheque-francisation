# -*- coding: utf-8 -*-
"""C2 · « Le répondeur de la maison »
Bloc C « Défi 2 · Le message et le mot » · couleur ambre · 75 min.
Source : exercice `t2acc`, mini-leçon `t2acc`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="« Le répondeur de la maison »",
        chapeau="Au travail, un message d'accueil parle au nom de "
                "l'employeur. Chez soi, c'est l'inverse : le message est "
                "court, il ne nomme presque rien, et sa qualité se mesure à "
                "ce qu'il ne dit pas.",
        duree='75 minutes')

    d.titre(notes="Si le groupe a fait le module « Le travail par écrit », annoncer tout "
                  "de suite qu'il faudra désapprendre la moitié de ce qui y a été appris. "
                  "Sinon, commencer par faire écouter deux messages d'accueil inventés — "
                  "un trop long, un trop bavard — et demander ce qui cloche.")

    d.objectifs([
        "enregistrer un message d'accueil personnel en quatre phrases ;",
        "savoir ce qu'un message d'accueil ne doit jamais contenir ;",
        "distinguer le message du bureau et celui de la maison ;",
        "tenir la durée : quinze à vingt secondes.",
    ], notes="Le deuxième objectif est le plus important et le moins linguistique : c'est "
             "une question de sécurité personnelle.")

    d.regle("Quatre phrases, et rien de plus",
            "Le repère, l'absence sans sa raison, la demande de message, "
            "le merci.",
            precision="Bonjour, vous avez bien rejoint le 514 555-0112. Je ne peux "
                      "pas vous répondre pour le moment. Laissez-moi un message et "
                      "je vous rappellerai. Merci.",
            notes="Diapositive à photographier, et à faire répéter en chœur : c'est un "
                  "texte que chacun réenregistrera chez lui le soir même. Faire remarquer "
                  "le futur simple de « je vous rappellerai », vu en B4.")

    d.cartes("Ce qu'on ne met jamais", "Quatre erreurs, et pourquoi", [
        ("Votre adresse",
         "Un message d'accueil s'écoute par n'importe qui, y compris au hasard."),
        ("Vos dates d'absence",
         "Dire qu'on part jusqu'au 20 juillet revient à l'afficher sur sa porte."),
        ("Vos horaires de travail",
         "Ils disent à quelles heures le logement est vide."),
        ("Le prénom des enfants",
         "Une information qui ne sert à personne, sauf à qui vous voulez tromper."),
    ], notes="Ne pas dramatiser, mais ne pas édulcorer : ces quatre erreurs sont "
             "fréquentes et faciles à corriger. La deuxième est celle qui surprend le "
             "plus, parce qu'elle part d'une bonne intention.")

    d.tableau('Deux répondeurs', "Le même appareil, deux métiers",
              ['Au bureau', 'À la maison'],
              [["On nomme l'organisation", "On donne le numéro, ou rien"],
               ["On nomme son service", "On ne nomme pas son service"],
               ["On donne une autre ressource", "On ne donne rien d'autre"],
               ["Vouvoiement obligatoire", "Vouvoiement, mais chaleureux"],
               ["Trente secondes", "Quinze à vingt secondes"]],
              cle=1,
              notes="Le tableau répond à une question réelle : beaucoup d'élèves ont un "
                    "seul modèle en tête et l'appliquent partout. Faire dire les deux "
                    "versions à voix haute, l'une après l'autre.")

    d.pratique('Jugement', "On le met, ou on ne le met pas ?",
               "Vous enregistrez le message de votre téléphone, à la maison.", [
        ("Le numéro de téléphone, dit lentement.", "on le met"),
        ("Votre adresse complète, avec le numéro d'appartement.", "on ne le met pas"),
        ("« Je ne peux pas vous répondre pour le moment. »", "on le met"),
        ("« Je suis en voyage jusqu'au 20 juillet. »", "on ne le met pas"),
        ("« Laissez-moi un message et je vous rappellerai. »", "on le met"),
        ("Vos heures de travail, jour par jour.", "on ne le met pas"),
        ("Une chanson de trente secondes avant le bip.", "on ne le met pas"),
    ], corrige=True,
       notes="Exercice t2acc de l'activité. La dernière fait rire, et elle sert : un "
             "message d'accueil trop long se fait raccrocher au nez, et la personne qui "
             "rappelle deux fois se lasse.")

    d.piege("Annoncer son voyage sur son message d'accueil",
            "Je suis à l'extérieur jusqu'au 20 juillet.",
            "Je ne peux pas vous répondre pour le moment.",
            "Prévenez directement les personnes concernées — comme le fait madame Faye "
            "dans son message, à une voisine — et laissez votre message d'accueil "
            "habituel pendant votre absence.",
            notes="Faire le lien explicite avec le dialogue de C1 : Ndeye annonce son "
                  "voyage à une personne, pas à tout le monde. C'est la bonne façon.")

    d.piege("Dire « c'est moi » en laissant un message",
            "Allô, c'est moi, rappelle-moi.",
            "Bonsoir madame Vergara, c'est Ndeye Faye, du troisième.",
            "Sur un répondeur, personne n'est « moi ». Donnez votre nom au complet et "
            "un repère, même à quelqu'un que vous connaissez bien.",
            notes="Ce piège annonce la séance E1 : c'est la première phrase de la "
                  "production orale, et celle qui décide si on sera rappelé.")

    d.billet(
        "Écrivez le message d'accueil que vous enregistrerez ce soir.",
        exemples=[
            "Quatre phrases. Comptez-les avant de remettre votre billet.",
            "Relisez : est-ce qu'une personne inconnue apprend quelque chose sur vous ?",
        ],
        notes="Ramasser et corriger : ce billet devient le brouillon de la production "
              "orale. Demander à la séance suivante qui l'a réellement enregistré.")

    return d.save(dossier)
