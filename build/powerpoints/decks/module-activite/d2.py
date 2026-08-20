# -*- coding: utf-8 -*-
"""D2 · Deux façons de dire la même chose.
Bloc D · couleur ambre (écriture) · 75 min.
Source : mini-leçon `t3registre`, dialogue `t3b`, exercices `t3registre` et `t3b`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre='Deux façons de dire la même chose',
        chapeau="« Envoye, embarque ! » et « Entrez dans l'eau, s'il vous "
                "plaît. » Deux façons de dire exactement la même chose. Aucune "
                "des deux n'est fautive.",
        duree='75 minutes')

    d.titre(notes="Séance délicate et très attendue des élèves. Annoncer d'emblée qu'aucune "
                  "des deux façons de parler n'est une faute : c'est ce qui débloque la "
                  "discussion.")

    d.objectifs([
        "reconnaître le registre familier et le registre standard ;",
        "savoir lequel employer selon la situation ;",
        "comprendre quelques mots courants du français parlé au Québec ;",
        "demander de reformuler quand je ne comprends pas.",
    ])

    d.dialogue('Dialogue', "Pardon ?", [
        ("KEVIN", "Envoye, embarque ! On commence dans deux minutes !", True),
        ("ROSA", "Pardon ? Je n'ai pas compris.", True),
        ("KEVIN", "Excusez-moi. Je voulais dire : entrez dans l'eau, s'il vous plaît. On commence bientôt.", True),
        ("LOUISE", "Kevin parle vite quand il est au bord de la piscine. Avec les parents, il est plus tranquille.", False),
    ], consigne="Écoutez, puis comparez la première et la troisième réplique.",
       notes="Les deux répliques de Kevin disent la même chose. Le faire constater avant "
             "toute explication : c'est le cœur de la séance.")

    d.tableau('Analyse', "Deux registres, deux situations",
              ['', 'Familier', 'Standard'],
              [["Le pronom", "tu", "vous"],
               ["La phrase", "courte, directe", "complète"],
               ["Où", "entre collègues, au bord de la piscine", "au comptoir, à l'écrit"]],
              cle=2,
              note="Les deux sont du bon français. Ce qui change, c'est la situation.",
              notes="Diapo centrale. Faire recopier. La note est ce que les élèves doivent "
                    "retenir avant tout.")

    d.cartes('Trois mots du français parlé ici', "Ce qu'ils veulent dire", [
        ("« Envoye ! »",
         "Veut dire « vas-y, dépêche-toi ». Se dit aussi « enweille ». Très employé, "
         "absent des manuels."),
        ("« Embarque ! »",
         "Veut dire « entre, monte ». On embarque dans une voiture, dans l'eau, dans un "
         "projet."),
        ("« C'est correct, pas de trouble. »",
         "Veut dire « c'est bien, il n'y a aucun problème ». Une des phrases les plus "
         "employées au Québec."),
    ], notes="Ces trois expressions valent à elles seules la séance. Les élèves les "
             "entendent chaque semaine sans les comprendre.")

    d.regle('Comment savoir lequel employer',
            "Un inconnu, un service, un employeur : vous. Un collègue, un ami : tu.",
            precision="Dans le doute, employez <b>vous</b>. Personne n'a jamais été vexé "
                      "d'être vouvoyé. Et si un moniteur vous tutoie, vous n'êtes pas "
                      "obligé de le tutoyer en retour — le tutoiement n'est pas toujours "
                      "réciproque.",
            notes="Diapo à photographier. La dernière phrase règle une inquiétude "
                  "fréquente.")

    d.regle("La phrase à savoir par cœur",
            "« Pardon ? Je n'ai pas compris. »",
            precision="C'est ce que dit Rosa, et Kevin reformule immédiatement en standard. "
                      "La plupart des gens passent spontanément au registre standard quand "
                      "on le leur demande. Cinq mots suffisent.",
            notes="Faire répéter par tout le groupe, deux fois. C'est la phrase la plus "
                  "utile du module.")

    d.piege("Croire que le familier est une faute",
            "Il parle mal, je ne devrais pas l'écouter.",
            "Il parle familièrement. C'est du bon français, dans la bonne situation.",
            "Le registre familier n'est pas du français abîmé : c'est le français qu'on "
            "emploie entre proches. Employer le registre standard entre amis sonne aussi "
            "étrange que l'inverse. Ce n'est pas une question de correction, mais de "
            "situation.",
            notes="Certains élèves ont appris un français très soigné et jugent le parler "
                  "d'ici. Le dire calmement et sans détour.")

    d.pratique('Pratique · 1 de 2', "Familier ou standard ?",
               "Classez chaque phrase.", [
        ("Envoye, embarque ! On commence dans deux minutes !", "familier"),
        ("Entrez dans l'eau, s'il vous plaît.", "standard"),
        ("Ça coûte combien, ton affaire ?", "familier"),
        ("Quel est le tarif pour les résidents ?", "standard"),
        ("Y reste-tu des places ?", "familier"),
        ("Est-ce qu'il reste des places disponibles ?", "standard"),
    ], corrige=True,
       notes="« Y reste-tu » : le « -tu » n'est pas le pronom, c'est une marque de "
             "question propre au français du Québec. L'expliquer, elle s'entend partout.")

    d.pratique('Pratique · 2 de 2', "Traduisez en standard",
               "Récrivez la phrase familière en registre standard.", [
        ("Envoye, embarque !", "Entrez dans l'eau, s'il vous plaît."),
        ("Ça coûte combien, ton affaire ?", "Quel est le tarif ?"),
        ("Y reste-tu des places ?", "Est-ce qu'il reste des places ?"),
        ("C'est correct, pas de trouble.", "Il n'y a aucun problème."),
        ("Amène ton papier d'adresse la semaine prochaine.", "Veuillez apporter votre preuve de résidence au premier cours."),
    ], corrige=True, cols=1,
       notes="La dernière ligne montre l'écart maximal : de l'oral familier à l'écrit "
             "administratif. Les deux disent la même chose.")

    d.cartes("Ce qu'on écrit, toujours", "Le standard à l'écrit", [
        ("Dans un courriel à un service",
         "Toujours le registre standard, même si la personne vous tutoie au téléphone."),
        ("Sur un formulaire",
         "Standard, et souvent impersonnel : « il est nécessaire de », « veuillez »."),
        ("Dans un message à un collègue",
         "Le familier passe très bien. Un courriel de travail trop soigné peut même "
         "paraître distant."),
    ], notes="Cette distinction sert directement à la production écrite de E1 — un courriel "
             "au service des loisirs.")

    d.billet(
        "Notez trois phrases familières entendues cette semaine et récrivez-les en standard.",
        exemples=[
            "Au travail, dans l'autobus, à la télévision.",
            "Si vous ne comprenez pas une phrase, écrivez-la comme vous l'avez entendue : on la décodera ensemble.",
        ],
        notes="Le meilleur billet du module. Les relevés font une excellente ouverture de "
              "la séance E1 — et souvent un grand moment du groupe.")

    return d.save(dossier)
