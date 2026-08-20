# -*- coding: utf-8 -*-
"""B3 · Demander de l'aide.
Bloc B « Défi 1 » · couleur ambre · 60 min.
Source : mini-leçon `t1aide`, exercice `t1aide`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Demander de l'aide",
        chapeau="Trois phrases : une pour attirer l'attention, une pour "
                "demander, une pour remercier. Et une quatrième, la plus "
                "utile de toutes — celle qui fait répéter.",
        duree='60 minutes')

    d.titre(notes="Séance de langue et de confiance. Beaucoup d'élèves évitent de demander "
                  "par crainte de mal dire : c'est ce qu'il faut désamorcer ici.")

    d.objectifs([
        "attirer l'attention avant de poser sa question ;",
        "demander de trois façons différentes ;",
        "faire répéter sans gêne ;",
        "remercier et comprendre la réponse.",
    ])

    d.declencheur(
        'Mise en situation', "Vous voulez demander où est le riz. Par quoi commencez-vous ?",
        pistes=[
            "Par la question ?",
            "Par « excusez-moi » ?",
            "Et si la personne est de dos ?",
            "Combien de temps faut-il attendre avant de parler ?",
        ],
        notes="Le temps que la personne se tourne — une seconde ou deux. Poser la question "
              "à quelqu'un de dos oblige à tout répéter.")

    d.tableau('Analyse', "Les quatre phrases",
              ['Le moment', "Ce qu'on dit"],
              [["Attirer l'attention", "Excusez-moi (monsieur, madame)"],
               ["Demander", "Je cherche… / Où est… ?"],
               ["Faire répéter", "Pardon ? / Plus lentement, s'il vous plaît."],
               ["Remercier", "Merci beaucoup."]],
              cle=2,
              note="La troisième est celle qu'on ose le moins — et celle qui sert le plus.",
              notes="Diapo à photographier. Faire répéter les quatre à voix haute, en "
                    "chœur, puis individuellement.")

    d.regle("Trois façons de demander",
            "Les trois sont correctes et polies.",
            precision="« <b>Où est</b> le riz ? » — court et clair. « <b>Je cherche</b> le "
                      "riz. » — encore plus simple, et c'est la formule la plus employée. "
                      "« <b>Pourriez-vous m'indiquer</b> le riz ? » — plus long, plus "
                      "poli. Choisissez celle que vous direz sans hésiter : c'est la "
                      "meilleure pour vous.",
            notes="Diapo à photographier. Insister : « je cherche » n'a rien d'impoli, "
                  "c'est ce que disent les gens d'ici.")

    d.cartes("Faire répéter", "Quatre phrases à savoir par cœur", [
        ("Pardon ?",
         "La plus courte. Elle suffit dans la plupart des cas."),
        ("Vous pouvez répéter ?",
         "Plus claire. La personne redira la même phrase."),
        ("Plus lentement, s'il vous plaît.",
         "La plus utile quand on a entendu sans comprendre : ce n'est pas le volume qui "
         "manque, c'est la vitesse."),
        ("Allée cinq ou allée quinze ?",
         "La meilleure : donner les deux possibilités obtient une réponse d'un seul mot."),
    ], notes="Diapo à photographier. Ces quatre phrases valent bien au-delà de l'épicerie.")

    d.piege("Dire « oui » sans avoir compris",
            "Oui, oui, merci. — et on cherche vingt minutes.",
            "Pardon, vous pouvez répéter ?",
            "Un « oui » poli coûte plus cher qu'un « pardon ». Personne ne juge quelqu'un "
            "qui demande de répéter — tout le monde le fait, même les gens nés ici, quand "
            "il y a du bruit dans le magasin.",
            notes="C'est le cœur de la séance. Le dire deux fois, et le rappeler à chaque "
                  "pratique orale du module.")

    d.pratique('Pratique · 1 de 2', "Que dites-vous ?",
               "Une phrase pour chaque situation.", [
        ("Attirer l'attention d'un commis.", "Excusez-moi."),
        ("Vous cherchez le riz.", "Je cherche le riz. / Où est le riz ?"),
        ("Vous n'avez pas compris le numéro.", "Pardon ? Vous pouvez répéter ?"),
        ("On parle trop vite.", "Plus lentement, s'il vous plaît."),
        ("On vient de vous aider.", "Merci beaucoup."),
    ], corrige=True, cols=1,
       notes="Utiliser l'exercice 3 du module, qui accepte plusieurs formulations.")

    d.pratique('Pratique · 2 de 2', "À deux · la demande complète",
               "Trois produits, trois demandes, du début à la fin.", [
        ("Étape 1", "Excusez-moi — et attendre que la personne se tourne"),
        ("Étape 2", "Je cherche… (un produit précis)"),
        ("Étape 3", "Faire répéter le numéro, en donnant les deux possibilités"),
        ("Étape 4", "Remercier, et écouter la réponse au merci"),
    ], cols=1,
       notes="Vingt minutes. Exiger les quatre étapes à chaque fois, même quand la "
             "compréhension est bonne du premier coup.")

    d.billet(
        "Cette semaine, demandez où se trouve un produit, pour vrai.",
        exemples=[
            "Notez la phrase que vous avez dite.",
            "Notez la réponse : l'avez-vous comprise du premier coup ?",
        ],
        notes="Le devoir le plus important du module. Prendre cinq minutes à la séance "
              "suivante pour entendre trois récits.")

    return d.save(dossier)
