# -*- coding: utf-8 -*-
"""E1 · À toi : l'appel et le courriel.
Bloc E « Je me lance » · couleur teal · 90 min.
Source du module : section `appli` — production orale (appeler la clinique) et
production écrite (demander un renouvellement d'ordonnance).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="À toi : l'appel et le courriel",
        chapeau="Deux productions, deux canaux : on appelle la clinique à voix haute, "
                "puis on écrit à la pharmacie. Tout le module sert ici.",
        duree='90 minutes')

    d.titre(notes="Rendre d'abord les billets de A4, B4, C5 et C3 : chacun contient une "
                  "phrase prête. Personne ne part d'une page blanche — c'est la "
                  "condition pour que la séance tienne en 90 minutes.")

    d.objectifs([
        "prendre un rendez-vous au téléphone, à voix haute ;",
        "s'enregistrer, s'écouter, recommencer ;",
        "écrire une demande de renouvellement d'ordonnance ;",
        "employer avoir besoin de ou le futur proche à l'écrit.",
    ])

    d.regle('Production orale · les trois temps',
            "Qui tu es · pourquoi tu appelles · ce que tu demandes.",
            precision="Trente secondes suffisent. C'est la règle de A1, et c'est la "
                      "grille d'évaluation de l'enregistrement.",
            notes="La laisser au tableau pendant tous les enregistrements. Les élèves y "
                  "reviennent des yeux entre deux essais.")

    d.cartes('Production orale', "Ce qu'on dit à chaque temps", [
        ("Temps 1 · Qui tu es",
         "« Bonjour, je m'appelle… Je suis déjà venu chez vous l'an dernier. »"),
        ("Temps 2 · Pourquoi tu appelles",
         "« Je me sens fatigué depuis deux semaines et j'ai souvent mal à la tête. »"),
        ("Temps 3 · Ce que tu demandes",
         "« Est-ce que le docteur a une place cette semaine ? »"),
        ("Et si on te propose une heure",
         "Tu confirmes : « Donc c'est bien mardi à 14 h 30 ? » — la reformulation de B2."),
    ], notes="Les trois temps sont ceux de l'activité interactive. La quatrième carte "
             "ajoute la confirmation : c'est ce qui distingue un bon appel d'un appel "
             "récité.")

    d.pratique('Pratique · 1 de 3', "Avant d'enregistrer",
               "Relisez vos billets et complétez.", [
        ("Votre nom, et si vous êtes déjà venu", "billet de A1"),
        ("Votre phrase de symptôme", "billet de A4"),
        ("Ce dont vous avez besoin", "billet de C3"),
        ("Trois moments où vous êtes libre", "billet de B2"),
    ], corrige=False,
       notes="Dix minutes en silence. Circuler et vérifier que les quatre lignes sont "
             "remplies avant d'autoriser le premier enregistrement.")

    d.pratique('Pratique · 2 de 3', "S'enregistrer, s'écouter, recommencer",
               "Dans l'activité, section « Je me lance ». Trois étapes.", [
        ("1 · Je m'enregistre", "environ 30 secondes, sans lire mot à mot"),
        ("2 · Je m'écoute et je corrige", "ce qui manque, ce qui va trop vite"),
        ("3 · J'envoie à mon enseignant", "quand vous en êtes satisfait, pas avant"),
    ], corrige=False,
       notes="Trente minutes. Insister sur l'étape 2 : c'est elle qui fait progresser, "
             "et c'est celle qu'on saute. Autoriser autant d'essais que voulu.")

    d.piege("Le piège de la lecture à voix haute",
            "(On lit ses quatre lignes sans lever les yeux.)",
            "(On regarde ses notes, puis on parle.)",
            "Un texte lu s'entend : le débit est plat et les mots sont ceux de l'écrit. "
            "Au téléphone, la réceptionniste attend une conversation. Les notes servent "
            "de rappel, pas de script.",
            notes="Faire écouter deux versions, si un volontaire accepte. La différence "
                  "s'entend immédiatement.")

    d.regle('Production écrite · le renouvellement',
            "Qui vous êtes · le médicament · combien il en reste · votre demande.",
            precision="Il vous reste deux comprimés et l'ordonnance est terminée. Vous "
                      "écrivez à ordonnances@pharmacienotredame.ca. Quatre à six "
                      "phrases suffisent.",
            notes="Deuxième moitié de la séance. Le courriel est celui de l'activité "
                  "interactive : les élèves le rédigent dans le module, pas sur papier.")

    d.tableau('Production écrite', "Ce que le courriel doit contenir",
              ['L\'élément', 'Ce qu\'on écrit'],
              [["votre nom", "prénom et nom, comme sur l'ordonnance"],
               ["le médicament", "son nom exact, tel qu'écrit sur la boîte"],
               ["ce qu'il en reste", "deux comprimés, une journée"],
               ["la demande", "un renouvellement, et pour quand"]],
              cle=0,
              notes="Employer au moins une fois « avoir besoin de » ou le futur proche : "
                    "c'est la contrainte de langue, et elle est écrite dans l'activité.")

    d.pratique('Pratique · 3 de 3', "Le courriel, phrase par phrase",
               "Écrivez-le dans l'activité, puis faites-le vérifier.", [
        ("Objet", "Demande de renouvellement d'ordonnance"),
        ("Première phrase", "Bonjour, je m'appelle… et je suis client chez vous."),
        ("Le médicament et ce qu'il en reste",
         "Il me reste deux comprimés de… et mon ordonnance est terminée."),
        ("La demande", "J'ai besoin d'un renouvellement. Je vais passer jeudi."),
        ("La formule finale", "Merci de votre aide. / Merci à l'avance."),
    ], corrige=True,
       notes="Trente minutes. Le bouton « Vérifier mon message » de l'activité corrige "
             "la langue ; l'enseignant vérifie le contenu — les quatre éléments y "
             "sont-ils ?")

    d.billet(
        "Notez ce qui a été le plus difficile : l'appel ou le courriel ? Pourquoi ?",
        exemples=[
            "Deux ou trois phrases.",
            "Ce que vous referiez autrement la prochaine fois.",
        ],
        notes="Ramasser. Ces billets orientent la révision de E2 : on y reprend ce que "
              "le groupe nomme, pas ce qu'on avait prévu.")

    return d.save(dossier)
