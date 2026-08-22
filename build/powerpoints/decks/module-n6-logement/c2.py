# -*- coding: utf-8 -*-
"""C2 · L'avis, ligne par ligne
Bloc C « Défi 2 · L'avis et la réponse » · couleur teal · 90 min.
Source : exercice `t2avis` (type texte) et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='teal',
        titre="L'avis, ligne par ligne",
        chapeau="La même règle qu'au Défi 1, mais avec un nom, une adresse et "
                "une date. C'est là que le texte cesse d'être général.",
        duree='90 minutes')

    d.titre(notes="Séance longue, en deux temps : lecture de l'avis à la première "
                  "heure, exercice interactif à la seconde. Projeter la lettre entière "
                  "avant de la découper.")

    d.objectifs([
        "reconnaître les cinq renseignements obligatoires d'un avis ;",
        "distinguer un avis d'une demande de permission ;",
        "nommer trois façons de dater sa remise ;",
        "repérer dans une lettre le passage qui répond à une question.",
    ], notes="Le deuxième objectif est celui qui change une démarche. Un élève qui "
             "écrit « accepteriez-vous que… » n'a pas fait d'avis, et son délai ne "
             "court pas.")

    d.declencheur(
        'Observation', "« Je vous avise » ou « accepteriez-vous » : quelle différence ?",
        pistes=[
            "Laquelle des deux formules fait partir un délai ?",
            "Laquelle est plus polie ? Est-ce que ça compte ici ?",
            "Peut-on être ferme et poli en même temps ?",
        ],
        notes="La question de la politesse revient toujours, et la réponse est "
              "importante : un avis n'est pas impoli, il est simplement d'une autre "
              "nature qu'une demande. La politesse est ailleurs, dans le ton.")

    d.tableau('Analyse', "Les cinq renseignements obligatoires",
              ['Ce qu\'il faut', 'Dans l\'avis de Farida'],
              [["la date", "Québec, le 18 novembre"],
               ["ce qu'on annonce", "une sous-location, pas une location"],
               ["qui", "monsieur Nicolas Trudel, et son adresse"],
               ["quand", "du 5 janvier au 28 juin inclusivement"]],
              cle=0,
              note="Le cinquième est le rappel du délai de quinze jours.",
              notes="Diapositive à photographier. Faire vérifier sur la lettre "
                    "projetée que les cinq y sont, et faire dire ce qui manquerait à "
                    "la démarche si l'un sautait.")

    d.regle("Un avis informe, il ne quête pas",
            "Écrit à la bonne date, avec les bons renseignements, il travaille tout seul.",
            precision="Au quinzième jour, quelque chose se produit, que le locateur "
                      "ait répondu ou non. C'est ce qui distingue un avis d'une "
                      "lettre ordinaire, et c'est pour cela qu'on écrit « je vous "
                      "avise de mon intention de » plutôt que « j'aimerais savoir "
                      "si vous seriez d'accord pour ».",
            notes="Diapositive à photographier. Écrire les deux formules au tableau, "
                  "l'une sous l'autre, et les laisser jusqu'à E2 : c'est le modèle du "
                  "courriel que chacun écrira.")

    d.cartes('Preuve', "Trois façons de dater sa remise", [
        ("Faire signer une copie", "Une ligne, une date, une signature. Le plus simple, et le plus souvent accepté si l'on précise que ce n'est pas un accord."),
        ("Un envoi qui laisse une trace", "On garde le reçu. Il n'y a plus rien à discuter, ni sur la date ni sur le fait que le document est parti."),
        ("Deux témoins", "Le moins solide, mais mieux que rien. Un voisin qui a vu la remise vaut toujours plus qu'un souvenir."),
        ("Ce qui ne vaut rien", "« Je le lui ai dit dans l'escalier mardi. » Sans écrit et sans date, il n'y a pas d'avis, donc pas de délai."),
    ], notes="Faire choisir à chacun celle qu'il emploierait, et pourquoi. Le débat "
             "vaut la peine : plusieurs élèves n'osent pas demander une signature, et "
             "c'est justement ce que la séance doit débloquer.")

    d.pratique('Lecture', "Où est la réponse dans la lettre ?",
               "Nommez le passage de l'avis qui répond.", [
        ("Quel jour l'avis a-t-il été écrit ?", "la date, en haut"),
        ("De quoi la lettre traite-t-elle ?", "la ligne d'objet"),
        ("Qui est la personne proposée ?", "le paragraphe du nom et de l'adresse"),
        ("Sur quelle période ?", "du 5 janvier au 28 juin"),
        ("Qui reste responsable du loyer ?", "le paragraphe de l'engagement"),
        ("Quel délai est rappelé ?", "quinze jours de la réception"),
    ], corrige=True,
       notes="Même travail que dans l'exercice interactif, où l'élève clique le "
             "passage dans la lettre. Le faire d'abord au tableau, sur la lettre "
             "projetée, avec un élève qui vient pointer.")

    d.tableau('Comparaison', "Ce qui affaiblit un avis",
              ['Faible', 'Solide'],
              [["je voudrais peut-être sous-louer", "je vous avise de mon intention"],
               ["à une personne sérieuse", "à monsieur Trudel, adresse complète"],
               ["pour quelques mois", "du 5 janvier au 28 juin"],
               ["j'espère que vous direz oui", "vous disposez de quinze jours"]],
              cle=1,
              notes="Faire lire les deux colonnes à voix haute par deux élèves "
                    "différents : la différence de ton s'entend mieux qu'elle ne "
                    "s'explique.")

    d.billet(
        "Écrivez la ligne d'objet et la première phrase de votre propre avis.",
        exemples=[
            "Deux lignes.",
            "Employez « je vous avise de mon intention de ».",
        ],
        notes="Cinq minutes. C'est le premier jet du courriel de E2. Ramasser, annoter "
              "brièvement, et les rendre au début de la séance E2 plutôt que de les "
              "corriger devant tout le monde.")

    return d.save(dossier)
