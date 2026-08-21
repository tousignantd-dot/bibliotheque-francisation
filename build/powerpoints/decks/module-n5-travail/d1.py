# -*- coding: utf-8 -*-
"""D1 · Six étapes et un formulaire
Bloc D « Défi 3 · La demande de congé » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3a` et `t3etapes`.

Les faits de normes du travail cités ici ont été vérifiés auprès de la CNESST
et de Légis Québec le 21 août 2026. Le délai de trois semaines, lui, est une
politique inventée de la coopérative — et le module dit lequel est lequel.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-travail/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Six étapes et un formulaire",
        chapeau="Demander un congé n'est pas demander une permission : "
                "c'est suivre une procédure. Six étapes, un formulaire, "
                "deux signatures, et une confirmation écrite sans laquelle "
                "le congé n'existe pas.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 3, et cœur de l'intention du programme : comprendre "
                  "des explications sur les principales étapes d'une démarche "
                  "administrative simple. Commencer en demandant au groupe comment on "
                  "demande un congé à leur travail. Les réponses vont de « je le dis à "
                  "mon boss » à un formulaire en ligne : tout l'écart est intéressant.")

    d.objectifs([
        "comprendre les six étapes d'une démarche administrative expliquées une seule fois ;",
        "les nommer soi-même, dans l'ordre, sans notes ;",
        "distinguer ce que dit la loi de ce que décide l'employeur ;",
        "réclamer une confirmation écrite avant de sortir du bureau.",
    ])

    d.declencheur(
        'Observation', "Une feuille à cases et un stylo. Qu'est-ce qui se "
                       "passe avant, et qu'est-ce qui se passe après ?",
        image=IMG + 'formulaire-rempli.jpg',
        pistes=[
            "Où prend-on un formulaire vierge ?",
            "Que faut-il savoir avant de le remplir ?",
            "Qui doit signer, et à qui l'envoie-t-on ?",
            "Comment sait-on que la demande a été acceptée ?",
        ],
        notes="Les quatre pistes sont, dans l'ordre, les étapes 2, 1, 4-5 et 6. Le "
              "groupe reconstruit presque toute la démarche seul : ne pas la donner "
              "avant d'avoir laissé chercher.")

    d.dialogue('Dialogue · 1 de 3', "Deux dates, et un remplacement", [
        ("DORINE", "Ghislain, est-ce que je peux vous parler deux minutes de mes "
                   "vacances ?", True),
        ("GHISLAIN", "Entrez. Quelles dates ?", True),
        ("DORINE", "Du lundi 12 août au vendredi 16 août. Cinq jours. Ma sœur arrive "
                   "de Kinshasa le 12.", True),
        ("GHISLAIN", "La semaine du 12 est déjà prise par Amel. Celle du 19 est libre.", True),
        ("DORINE", "Alors ce sera du 19 au 23 août. Retour le lundi 26.", True),
        ("GHISLAIN", "Bien. Qui répond au téléphone de l'accueil pendant ce temps-là ?", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer deux choses : Ghislain demande les dates avant tout le "
             "reste, et Dorine donne la date du retour, pas seulement la durée. Ce sont "
             "les deux réflexes du jeu de rôle de la séance E1.")

    d.dialogue('Dialogue · 2 de 3', "Les six étapes, dites une seule fois", [
        ("DORINE", "Pas exactement. Dites-moi les étapes, je les écris.", True),
        ("GHISLAIN", "Six. D'abord vous vérifiez au registre combien de jours il vous "
                     "reste. Ensuite vous prenez le formulaire au babillard. Puis vous "
                     "le remplissez : les deux dates, le nom de la personne qui vous "
                     "remplace. Après, vous me le faites signer. Ensuite vous l'envoyez "
                     "à Sylvie, à la paie. Et enfin vous attendez sa confirmation par "
                     "courriel.", True),
    ], consigne="Écoutez deux fois. À la deuxième écoute seulement, écrivez.",
       notes="C'est l'exercice de compréhension orale du programme, dans sa forme la plus "
             "pure : une démarche expliquée une seule fois, à débit normal, avec des "
             "marqueurs de temps. Ceux de la séance C3 servent ici à repérer les étapes.")

    d.dialogue('Dialogue · 3 de 3', "Une entente de corridor ne vaut rien", [
        ("DORINE", "Et si je ne reçois rien ?", True),
        ("GHISLAIN", "Vous relancez. Tant que la confirmation n'est pas écrite, votre "
                     "congé n'existe pas. Une entente de corridor ne vaut rien au mois "
                     "d'août.", True),
        ("DORINE", "Combien de temps d'avance ?", True),
        ("GHISLAIN", "Ici, trois semaines : c'est notre politique. La loi, elle, oblige "
                     "l'employeur à annoncer les dates de vacances au moins quatre "
                     "semaines à l'avance.", False),
    ], notes="La dernière réplique distingue la règle de l'employeur de celle de la loi. "
             "C'est une compétence de citoyen autant que de langue : savoir d'où vient "
             "une règle permet de savoir si elle se discute.")

    d.regle("Tant que ce n'est pas écrit, le congé n'existe pas",
            "La confirmation de la paie, par courriel, est la seule preuve.",
            precision="Un silence n'est pas un oui : si rien n'arrive après quelques "
                      "jours, on relance. Et on garde le courriel — c'est celui qu'on "
                      "vous demandera si quelqu'un a oublié.",
            notes="Diapositive à photographier. Elle reprend la règle de A1 — « ce qui "
                  "n'est pas écrit n'a pas eu lieu » — appliquée au cas le plus concret "
                  "du module.")

    d.tableau('Les six étapes', "Ce qu'on y fait exactement",
              ['Étape', 'Ce qu\'on y fait'],
              [["1 · Vérifier", "Combien de jours il reste, au registre"],
               ["2 · Prendre", "Le formulaire vierge, au babillard"],
               ["3 · Remplir", "Les deux dates et qui vous remplace"],
               ["4 · Faire signer", "Par le chef d'équipe, sur le formulaire"],
               ["5 · Envoyer", "Le formulaire signé, à la paie"],
               ["6 · Attendre", "La confirmation écrite, et la garder"]],
              cle=1,
              notes="Faire répéter les six verbes sans le tableau : vérifier, prendre, "
                    "remplir, faire signer, envoyer, attendre. C'est ce que l'élève doit "
                    "savoir redire, et c'est l'intention de production orale du programme.")

    d.cartes("Ce que dit la loi du Québec", "Vérifié auprès de la CNESST", [
        ("Deux journées payées par année",
         "Pour maladie ou obligations familiales, après trois mois de service continu."),
        ("Jusqu'à dix journées d'absence",
         "Par année, pour la santé d'un proche ou les obligations familiales."),
        ("Deux semaines de vacances après un an",
         "Et trois semaines après trois ans de service continu."),
        ("Quatre semaines d'avis",
         "L'employeur doit faire connaître les dates de vacances au moins quatre "
         "semaines à l'avance."),
    ], notes="Ces quatre faits sont vrais et vérifiables : ils viennent de la CNESST et "
             "de la Loi sur les normes du travail. Le délai de trois semaines de la "
             "coopérative, lui, est une politique interne. Faire dire la différence.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Dorine demande d'abord la semaine du 12 août.", "vrai"),
        ("Cette semaine-là est déjà prise par quelqu'un d'autre.", "vrai"),
        ("La démarche compte six étapes.", "vrai"),
        ("La dernière étape est de faire signer le formulaire.", "faux — d'attendre la confirmation"),
        ("Une entente de vive voix suffit pour partir en congé.", "faux — jamais"),
        ("Le délai de trois semaines vient de la loi.", "faux — de la coopérative"),
    ], corrige=True,
       notes="La dernière est la plus importante et la plus discutée. Y revenir : "
             "confondre une politique d'employeur et une loi empêche de poser les "
             "bonnes questions.")

    d.billet(
        "Écrivez les six étapes, dans l'ordre, sans regarder vos notes.",
        exemples=[
            "Un verbe par étape suffit.",
            "Ajoutez, pour votre propre travail, ce qui serait différent.",
        ],
        notes="Faire d'abord de mémoire, puis vérifier. L'écart entre les deux est ce "
              "que la séance D2 devra consolider avant le jeu de rôle de E1.")

    return d.save(dossier)
