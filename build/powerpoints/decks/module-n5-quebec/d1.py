# -*- coding: utf-8 -*-
"""D1 · Le gîte, puis le sentier
Bloc D « Défi 3 · Sur place, avec les gens de la région » · acier · 75 min.
Source : dialogue `t3`, exercices `t3a` et `t3reg`.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-quebec/images/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Le gîte, puis le sentier",
        chapeau="Thuy est arrivée. Il y a Rose-Aimée, qui tient le gîte et "
                "lui parle de la marée et du temps qu'il fera ; il y a "
                "Denis, un vacancier sur le sentier, qui lui demande d'où "
                "elle vient. Ces conversations-là ne se préparent pas.",
        duree='75 minutes')

    d.titre(notes="Première des deux séances du défi 3. Le programme appelle cela une "
                  "« conversation spontanée » et c'est ce qui l'oppose aux deux défis "
                  "précédents : au comptoir, on savait ce qu'on venait chercher. Ici, "
                  "non. Le dire au groupe, ça change leur écoute.")

    d.objectifs([
        "saluer et répondre à une salutation d'usage ;",
        "tenir le vouvoiement avec des inconnus de la région ;",
        "engager une conversation spontanée sur les vacances ;",
        "répondre à « d'où venez-vous ? » sans réciter sa biographie.",
    ], notes="Le quatrième objectif mérite d'être discuté : beaucoup d'élèves "
             "répondent par un récit d'immigration complet à une question de politesse. "
             "Thuy donne deux phrases, et c'est exactement ce qu'il faut.")

    d.declencheur(
        'Observation', "Quelqu'un s'arrête à côté de vous et dit : « Belle "
                       "journée, hein ? » Que répondez-vous ?",
        image=img('sentier-bord-eau.jpg'),
        pistes=[
            "Est-ce une vraie question sur la météo ?",
            "Qu'est-ce qui se passe si vous répondez seulement « oui » ?",
            "Est-ce qu'on tutoie ou est-ce qu'on vouvoie cette personne ?",
            "Qu'est-ce que vous pourriez demander en retour ?",
        ],
        notes="La deuxième piste est le point de la séance : « oui » ferme la porte. "
              "Une salutation d'usage attend qu'on la relance. Faire essayer les deux "
              "versions par deux binômes.")

    d.dialogue('Dialogue · 1 de 3', "Vous avez fait bon voyage ?", [
        ("ROSE-AIMÉE", "Bienvenue ! Vous avez fait bon voyage ?", True),
        ("THUY", "Bonjour madame. Oui, très bon. Huit heures, mais je n'ai "
                 "pas vu le temps passer : je regardais dehors tout le "
                 "long.", True),
        ("ROSE-AIMÉE", "C'est la première fois que vous descendez par ici ?", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Thuy ne répond pas « oui ». Elle donne une durée, puis une image. C'est "
             "exactement la relance attendue, et elle tient en une phrase et demie. "
             "Faire compter au groupe combien de mots ça fait de plus qu'un « oui ».")

    d.dialogue('Dialogue · 2 de 3', "La marée descend vers dix heures", [
        ("ROSE-AIMÉE", "Le déjeuner est servi de sept heures à neuf heures, "
                       "en bas. Demain il va faire beau et frais, quatorze "
                       "degrés. La marée descend vers dix heures : c'est le "
                       "bon moment pour aller voir les phoques.", True),
        ("THUY", "Je peux y aller à pied depuis ici ?", True),
        ("ROSE-AIMÉE", "En marchant, comptez quarante minutes. En passant "
                       "par le petit chemin derrière l'église, vous coupez "
                       "dix minutes.", True),
    ], notes="Rose-Aimée donne trois informations qu'on ne lui a pas demandées : le "
             "déjeuner, la météo, la marée. C'est ce que fait quelqu'un de la région, "
             "et c'est précisément ce qui n'était écrit nulle part en C1.")

    d.dialogue('Dialogue · 3 de 3', "Vous n'êtes pas du coin, vous non plus ?", [
        ("DENIS", "Vous n'êtes pas du coin, vous non plus ? Moi je viens de "
                  "Sherbrooke. On monte ici tous les automnes, ma femme et "
                  "moi.", True),
        ("THUY", "J'arrive de Montréal. C'est ma première fois dans la "
                 "région.", True),
        ("DENIS", "Et vous êtes montée jusqu'au belvédère ? C'est là-haut, à "
                  "vingt minutes.", False),
    ], notes="Denis se présente avant de questionner : il donne sa ville, puis il "
             "demande. C'est la règle non écrite de la conversation entre inconnus, et "
             "elle rend la question acceptable. La faire remarquer.")

    d.regle("On vouvoie, et on relance",
            "Vouvoiement avec les inconnus, du début à la fin. Et jamais un "
            "« oui » tout seul : on ajoute une phrase.",
            precision="Personne ne propose le tutoiement à Thuy en six jours. Ce "
                      "n'est pas de la froideur : c'est l'usage avec quelqu'un "
                      "qu'on rencontre.",
            notes="Diapositive à photographier. Le vouvoiement est un des savoirs "
                  "nommés par le programme — « salutations d'usage » — et c'est celui "
                  "que les élèves manquent le plus souvent, dans les deux sens.")

    d.tableau('Tu ou vous ?', "Quatre personnes du module",
              ['La personne', 'On dit'],
              [["Camille, collègue de travail", "tu"],
               ["Serge, au comptoir", "vous"],
               ["Rose-Aimée, au gîte", "vous"],
               ["Denis, sur le sentier", "vous"]],
              cle=1,
              notes="Une seule personne sur quatre se tutoie, et c'est la collègue "
                    "qu'on voit tous les jours. Faire remarquer que Denis est "
                    "chaleureux et vouvoie quand même : la chaleur ne passe pas par le "
                    "tutoiement.")

    d.piege("Répondre « oui » à une salutation d'usage",
            "« Belle journée, hein ? » — « Oui. »",
            "« Oui, magnifique. Je n'avais jamais vu le fleuve comme ça. »",
            "« Belle journée » n'est pas une question sur la météo : c'est une "
            "porte ouverte. Un « oui » seul la referme, et la personne s'éloigne "
            "en pensant qu'on ne voulait pas parler.",
            notes="Beaucoup d'élèves croient avoir été polis en répondant brièvement. "
                  "Leur dire que l'effet produit est l'inverse est utile, et souvent "
                  "un soulagement.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Thuy reste six nuits au gîte.", "vrai"),
        ("Le déjeuner est servi jusqu'à dix heures.", "faux — de sept à neuf heures"),
        ("La marée descend vers dix heures.", "vrai"),
        ("Denis habite la région.", "faux — il vient de Sherbrooke"),
        ("Thuy est déjà montée au belvédère.", "faux — pas encore"),
        ("Rose-Aimée tutoie Thuy.", "faux — elle la vouvoie"),
    ], corrige=True,
       notes="Faire justifier chaque réponse. La quatrième est instructive : Denis "
             "connaît bien la région sans y habiter, et c'est fréquent. On peut "
             "renseigner sans être « du coin ».")

    d.billet(
        "Écrivez votre réponse à « D'où venez-vous ? », en deux phrases, pas plus.",
        exemples=[
            "Deux phrases : d'où vous arrivez, et une chose sur vous.",
            "Gardez le reste pour si l'on vous en redemande.",
        ],
        notes="Ramasser les billets et les rendre en D2. La contrainte des deux phrases "
              "est le vrai exercice : elle apprend à doser, ce que le niveau 5 demande.")

    return d.save(dossier)
