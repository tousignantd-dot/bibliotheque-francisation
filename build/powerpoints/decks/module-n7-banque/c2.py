# -*- coding: utf-8 -*-
"""C2 · Lire un document qui compare
Bloc C « Défi 2 · Faire travailler l'argent » · couleur teal · 90 min.
Source : exercices `t2doc` (type texte) et `t2ranger`, et leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='teal',
        titre='Lire un document qui compare',
        chapeau="Un document qui compare trois produits ne se lit pas du "
                "début à la fin. On lui pose une question, et on la pose aux "
                "trois.",
        duree='90 minutes')

    d.titre(notes="Séance de lecture. Distribuer la documentation sur l'épargne avant "
                  "de projeter quoi que ce soit, et laisser cinq minutes de lecture "
                  "silencieuse.")

    d.objectifs([
        "lire un document comparatif par question et non par page ;",
        "se servir des intertitres comme d'une table des matières ;",
        "ranger une caractéristique sous le bon produit ;",
        "dire ce que l'impôt fait à l'entrée et à la sortie.",
    ], notes="Le quatrième objectif est celui qui distingue vraiment le CELI du REER, "
             "et c'est la seule chose que les élèves doivent retenir des deux.")

    d.declencheur(
        'Observation', "Comment lis-tu un dépliant qui présente trois produits ?",
        pistes=[
            "Du début à la fin, ou en cherchant quelque chose ?",
            "Regardes-tu les titres de section avant le texte ?",
            "Combien de temps te faut-il pour trouver un taux ?",
            "Et si le document n'avait aucun intertitre ?",
        ],
        notes="La dernière question est instructive : un document sans intertitres se "
              "lit trois fois plus lentement, et c'est parfois exprès.")

    d.regle("On lit par question, pas par page",
            "Choisissez la vôtre - combien, pour quand, avec quel impôt - et posez-la "
            "aux trois produits.",
            precision="Les intertitres sont là pour qu'on saute directement à sa "
                      "question. C'est le savoir que le programme du niveau 7 appelle "
                      "« organiser clairement de l'information dans le but de comparer "
                      "des éléments », et il vaut pour lire comme pour écrire.",
            notes="Diapositive à photographier. Faire l'exercice en direct : donner une "
                  "question, chronométrer trente secondes, demander la réponse.")

    d.tableau('Analyse', "L'impôt, à l'entrée et à la sortie",
              ['Le régime', 'Ce que fait l\'impôt'],
              [['CELI', 'rien à l\'entrée, rien à la sortie'],
               ['REER', 'déduction à l\'entrée, impôt à la sortie'],
               ['dépôt à terme', 'ce n\'est pas un régime, c\'est un placement'],
               ['compte épargne', "l'intérêt s'ajoute au revenu de l'année"]],
              cle=0,
              note="Plafond du CELI : 7 000 $ pour 2026. Droit REER : 18 % du revenu gagné.",
              notes="Diapositive à photographier. Les deux chiffres de la note sont "
                    "vérifiés auprès de l'Agence du revenu du Canada.")

    d.regle("Un abri n'est pas un placement",
            "Le CELI et le REER ne rapportent rien par eux-mêmes : ce qu'on met dedans, "
            "voilà le placement.",
            precision="Un CELI qui contient un compte à zéro pour cent rapporte zéro "
                      "pour cent, exonéré d'impôt. Demandez toujours les deux choses : "
                      "quel placement, et dans quel régime. Un conseiller qui ne répond "
                      "qu'à l'une des deux n'a répondu qu'à moitié.",
            notes="Diapositive à photographier. C'est la phrase que les élèves "
                  "réemploieront le plus souvent hors de la classe.")

    d.pratique('Lecture', "Cherchez la réponse dans le document",
               "Une question, un passage. Soulignez-le au crayon.", [
        ("Quel taux le dépôt à terme offre-t-il, et pour combien de temps ?", "3,10 % pour deux ans"),
        ("Que se passe-t-il si on retire avant l'échéance ?", "pénalité ou perte des intérêts"),
        ("Combien peut-on verser dans un CELI en 2026 ?", "7 000 $, plus les droits non utilisés"),
        ("Quand récupère-t-on le droit de remettre un retrait de CELI ?", "le 1er janvier suivant"),
        ("Comment se calcule le droit annuel au REER ?", "18 % du revenu gagné de l'année précédente"),
        ("Jusqu'à quel montant les dépôts sont-ils protégés ?", "100 000 $ par catégorie et par institution"),
    ], corrige=True,
       notes="Faire souligner sur le papier avant de corriger. Le quatrième piège tout "
             "le monde : le droit ne revient pas le mois suivant.")

    d.pratique('Application', "De quel produit parle-t-on ?",
               "Répondez : CELI, REER ou dépôt à terme.", [
        ("Ce que j'y mets est déduit de mon revenu cette année.", "REER"),
        ("Le taux est fixé au départ et ne bouge plus.", "dépôt à terme"),
        ("Mes retraits ne sont pas imposables.", "CELI"),
        ("Le plafond est de sept mille dollars pour 2026.", "CELI"),
        ("Tout ce que j'en sors s'ajoute à mon revenu de l'année.", "REER"),
        ("C'est le produit d'un projet qui a une date connue.", "dépôt à terme"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la ligne du document. C'est la même "
             "compétence que l'exercice précédent, appliquée dans l'autre sens.")

    d.piege('Le piège', "remettre en mars l'argent sorti du CELI en janvier",
            "attendre le 1er janvier suivant",
            "Le montant retiré n'est rendu aux droits de cotisation que l'année "
            "suivante. Le remettre avant crée un excédent, frappé d'un impôt de un pour "
            "cent par mois. La faute se commet toujours de bonne foi, et elle coûte de "
            "l'argent tous les mois jusqu'au retrait de l'excédent.",
            notes="Fait vérifié auprès de l'Agence du revenu du Canada. Insister : "
                  "c'est la seule pénalité du bloc C.")

    d.billet("Pour ton propre projet le plus proche, écris la date et le produit qui "
             "conviendrait.",
             exemples=["Dans dix-huit mois : un dépôt à terme dans un CELI.",
                       "Dans quinze ans : un REER."],
             notes="Trois minutes. La date d'abord, le produit ensuite : refuser les "
                   "billets écrits dans l'autre ordre.")

    return d.save(dossier)
