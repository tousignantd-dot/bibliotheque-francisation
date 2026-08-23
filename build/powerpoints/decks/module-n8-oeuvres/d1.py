# -*- coding: utf-8 -*-
"""D1 · Le cercle du mardi, huit heures moins dix
Bloc D « Défi 3 · Défendre une lecture » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t31` et `t3conc`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Le cercle du mardi, huit heures moins dix",
        chapeau="Deux lectures s'affrontent, et l'invitée pose la seule "
                "question qui les départage : est-ce que votre lecture "
                "explique aussi l'indice de l'autre ?",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 3, et point d'arrivée du module : tout ce qui a "
                  "été appris depuis A1 se joue dans ce dialogue. Le faire écouter "
                  "d'un trait la première fois, sans consigne.")

    d.objectifs([
        "suivre une discussion à trois voix sur une même scène ;",
        "reprendre l'indice de l'autre dans sa propre lecture ;",
        "concéder avec « bien que » et opposer avec « même si » ;",
        "reformuler la lecture d'autrui avant d'y répondre.",
    ], notes="Le deuxième objectif est le sommet du module. Il n'est pas naturel : "
             "l'instinct est de nier l'indice qui gêne, pas de le reprendre.")

    d.declencheur(
        'Préparation', "Que faites-vous de l'argument qui vous gêne ?",
        pistes=[
            "Vous le passez sous silence, en espérant qu'on l'oublie ?",
            "Vous dites qu'il ne compte pas ?",
            "Vous le sortez vous-même, avant l'autre ?",
            "Laquelle de ces trois réponses se voit le moins ?",
        ],
        notes="La quatrième piste est un piège utile : la troisième réponse ne se "
              "cache pas, elle se montre — et c'est elle qui fonctionne. Le silence, "
              "lui, se voit toujours.")

    d.dialogue('Dialogue · 1 de 3', "Chacun sa lecture", [
        ("FATOUMATA", "Ma lecture : Estelle choisit de rester, et c'est le premier choix qu'elle fait dans toute la série.", True),
        ("LÉANDRE", "Et la corde, madame Sidibé ? Vous passez la corde sous silence, ce soir.", True),
        ("FATOUMATA", "Je ne la passe pas sous silence. Je vous laisse la sortir : c'est votre meilleur argument, et il est à vous.", True),
        ("LÉANDRE", "Une femme assise dans une embarcation attachée, ça ne s'appelle pas un choix, ça s'appelle un piège.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="La réplique de Fatoumata est le geste de la séance : elle laisse "
             "l'argument à celui à qui il appartient au lieu de le désamorcer. Le "
             "faire remarquer.")

    d.dialogue('Dialogue · 2 de 3', "La question qui départage", [
        ("JOSYANE", "Chacun de vous a un indice. Le téléphone contre la corde. Est-ce que l'un des deux explique aussi l'autre ?", True),
        ("LÉANDRE", "Comment ça, expliquer l'autre ?", True),
        ("JOSYANE", "Votre lecture doit rendre compte du téléphone, et la sienne doit rendre compte de la corde.", True),
        ("JOSYANE", "Sinon, chacun de vous a raison sur un tiers de la scène et se tait sur le reste.", True),
    ], notes="La question de Josyane est la règle de B2, posée dans une vraie "
             "discussion. L'écrire au tableau telle quelle : est-ce que votre lecture "
             "explique aussi l'indice de l'autre ?")

    d.dialogue('Dialogue · 3 de 3', "Retourner, plutôt que nier", [
        ("FATOUMATA", "Si elle avait voulu partir, elle l'aurait détachée. Elle ne l'a pas détachée.", True),
        ("FATOUMATA", "Donc soit elle est prise, soit elle a décidé de ne pas partir — et alors la corde n'est pas ce qui la retient, c'est ce qu'elle laisse en place.", True),
        ("JOSYANE", "Vous n'avez pas nié l'indice de l'autre : vous l'avez repris dans votre lecture.", True),
        ("JOSYANE", "Retourner un indice, c'est permis. Le passer sous silence, non.", True),
    ], notes="Le sommet du module. Faire répéter la deuxième réplique par trois élèves "
             "différents : c'est la phrase-modèle de la production orale d'E1.")

    d.tableau('Analyse', "Trois gestes qui font avancer",
              ['Le geste', 'Ce qu\'il produit'],
              [["Laisser l'argument à l'autre", "il l'écoute au lieu de le défendre"],
               ["Reprendre son indice", "la discussion couvre toute la scène"],
               ["Concéder avant de répondre", "on vous accorde la suite"]],
              cle=0,
              note="Aucun des trois ne coûte votre lecture. Les trois la rendent audible.",
              notes="Diapositive à photographier. Ce sont les trois consignes du jeu de "
                    "rôle et de la production orale.")

    d.regle("Bien que veut le subjonctif, même si veut l'indicatif",
            "« Bien que la corde soit attachée » · « Même si vous avez raison "
            "sur la corde ».",
            precision="Le repère est fiable : « même si » contient un « si », et aucun "
                      "« si » du français n'est suivi du subjonctif. Concéder n'est "
                      "pas céder — vous accordez un point, puis vous avancez le "
                      "vôtre, et c'est ce qui vous rend écoutable.",
            notes="Diapositive à photographier. Le repère du « si » vaut la peine "
                  "d'être retenu : il règle aussi l'hypothèse irréelle de B3.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Fatoumata propose la première lecture de la soirée.", "vrai"),
        ("Elle empêche Léandre de parler de la corde.", "faux - elle la lui laisse"),
        ("Josyane demande si chaque lecture explique l'indice de l'autre.", "vrai"),
        ("Léandre refuse de s'expliquer sur le téléphone.", "faux - il s'explique"),
        ("Passer un indice sous silence est permis, selon Josyane.", "faux"),
        ("Le cercle a vu la pièce dont parle la critique.", "faux - personne"),
    ], corrige=True,
       notes="Exercice `t31` du module. Le dernier annonce D2 : on va discuter un "
             "texte sur une œuvre que personne n'a vue.")

    d.pratique('Pratique', "Concéder ou opposer ?",
               "Complétez.", [
        ("___ la corde soit attachée, c'est elle qui l'a remise à l'eau.", "Bien que"),
        ("___ vous avez raison sur la corde, il reste le téléphone.", "Même si"),
        ("La notaire porte la pièce ; ___, les cadets jouent trop fort.", "en revanche"),
        ("___ il ait raison sur un point, sa lecture explique moins.", "Quoiqu'"),
        ("___, la salle n'était pas pleine, mais ce n'est pas le reproche.", "Certes"),
        ("___ la parenthèse, on pourrait défendre la lecture tendre.", "Sans"),
    ], corrige=True,
       notes="Exercice `t3conc` du module. Le sixième rappelle que « malgré » se met "
             "devant un nom : « malgré que » ne se publie pas.")

    d.billet(
        "Écrivez la phrase qui reprend l'indice gênant de votre œuvre et le "
        "retourne, sur le modèle de Fatoumata.",
        exemples=[
            "« La corde n'est pas ce qui la retient : c'est ce qu'elle laisse en place. »",
            "Une seule phrase, avec deux-points au milieu.",
        ],
        notes="Ramasser et rendre annoté avant E1 : cette phrase-là est le troisième "
              "temps de la production orale.")

    return d.save(dossier)
