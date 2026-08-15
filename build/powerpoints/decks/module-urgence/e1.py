# -*- coding: utf-8 -*-
"""E1 · À toi : l'appel au 811 et le message.
Bloc E · couleur teal (je me lance) · 90 min.
Source : section `appli`, exercices `t2appel` et `aFiche` (la coupure profonde).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="À toi : l'appel et le message",
        chapeau="Tout le module en une séance. Lire une fiche qu'on n'a jamais vue, "
                "appeler le 811 et décrire une blessure, puis écrire à la personne "
                "qui reste à la maison.",
        duree='90 minutes')

    d.titre(notes="Séance d'application. Aucun contenu nouveau. Un tiers de lecture, un "
                  "tiers d'oral, un tiers d'écrit — et tenir l'horaire.")

    d.objectifs([
        "lire une fiche-conseil nouvelle et en tirer les gestes à faire ;",
        "décrire une blessure au téléphone, au passé composé ;",
        "dire ce qu'on a fait et ce qu'on n'a pas fait ;",
        "écrire un message court à une personne blessée.",
    ])

    # ── premier temps · la lecture ─────────────────────────────────
    d.tableau('Lire', "La fiche-conseil sur les coupures",
              ['La rubrique', 'Ce qu\'elle dit'],
              [["les premiers gestes", "comprimer, élever le membre, nettoyer à l'eau"],
               ["consulter rapidement", "si le saignement dure plus de dix minutes"],
               ["consulter aussi", "plaie profonde, longue, sale, ou au visage"],
               ["le tétanos", "un rappel si le dernier date de plus de dix ans"]],
              cle=0,
              note="Ce sont les mêmes rubriques que la fiche sur les brûlures, en C4. "
                   "Un contenu nouveau dans une structure connue.",
              notes="Ne rien expliquer avant l'exercice : c'est une lecture autonome. "
                    "Cinq minutes de lecture silencieuse.")

    d.pratique('Pratique · 1 de 4', "Vrai ou faux — la coupure",
               "D'après la fiche que vous venez de lire.", [
        ("Il faut comprimer la plaie avec un linge propre.", "VRAI"),
        ("Élever le membre blessé aide à ralentir le saignement.", "VRAI"),
        ("Il faut consulter si le saignement continue après dix minutes.", "VRAI"),
        ("Une coupure au visage peut attendre plusieurs jours.", "FAUX — consulter"),
        ("Le rappel du tétanos se fait tous les deux ans.", "FAUX — dix ans"),
    ], corrige=True,
       notes="Corriger en renvoyant chaque fois à la rubrique. L'important n'est pas la "
             "réponse mais l'endroit où on l'a trouvée.")

    # ── deuxième temps · l'appel ───────────────────────────────────
    d.regle("L'appel au 811, en trois temps",
            "Ce qui est arrivé · ce que j'ai déjà fait · ce que je vois maintenant.",
            precision="L'infirmière posera exactement ces trois questions. Les préparer "
                      "d'avance évite de chercher ses mots au téléphone, où l'on ne voit "
                      "pas le visage de l'autre.",
            notes="Écrire les trois au tableau avant de lancer l'exercice oral. Les "
                  "élèves les regarderont pendant les jeux de rôle : c'est voulu.")

    d.cartes('Le modèle', "Ce que l'infirmière veut entendre", [
        ("Le récit, au passé composé",
         "« Je me suis coupé la main avec un couteau, il y a vingt minutes. » "
         "L'événement, la partie du corps, le moment."),
        ("Les gestes déjà faits",
         "« J'ai comprimé avec un linge propre pendant dix minutes. » Avec la durée : "
         "c'est ce qui change la réponse."),
        ("Ce que je n'ai pas fait",
         "« Je n'ai rien mis sur la plaie. » Une phrase négative, et l'infirmière sait "
         "où on en est."),
        ("Ce que je vois maintenant",
         "« Ça saigne encore un peu, la plaie fait deux centimètres. » Une description "
         "au présent, avec une mesure si possible."),
    ], notes="La quatrième carte est celle qui manque le plus souvent. Faire pratiquer "
             "la description au présent : longueur, profondeur, couleur, saignement.")

    d.pratique('Pratique · 2 de 4', "À deux · l'appel au 811",
               "L'un est l'infirmière, l'autre appelle. Puis on échange.", [
        ("L'infirmière ouvre", "Info-Santé, bonjour. Décrivez-moi la blessure."),
        ("Vous racontez", "au passé composé, avec le moment"),
        ("L'infirmière demande", "Qu'avez-vous fait jusqu'ici ?"),
        ("L'infirmière demande", "Est-ce que la douleur augmente ?"),
        ("L'infirmière conclut", "Rendez-vous à l'urgence aujourd'hui."),
    ], corrige=False,
       notes="Dix minutes par personne, dos à dos si possible : au téléphone, on ne voit "
             "pas l'autre. Cela change complètement l'exercice.")

    d.piege("Le piège du téléphone",
            "Vous répondez par oui et par non, et l'infirmière doit tout deviner.",
            "Vous racontez, puis vous répondez aux questions.",
            "Au téléphone, l'infirmière ne voit rien. Chaque information que vous ne "
            "donnez pas est une question de plus, et le temps compte. Un récit de "
            "trente secondes remplace dix questions.",
            notes="Faire refaire l'exercice une seconde fois, en interdisant les "
                  "réponses en un mot. La différence est spectaculaire.")

    # ── troisième temps · l'écrit ──────────────────────────────────
    d.cartes('Écrire', "Le message à une personne blessée", [
        ("Prendre des nouvelles",
         "« Comment va ton bras aujourd'hui ? » Une question précise, pas « ça va ? ». "
         "Elle montre qu'on a retenu ce qui s'est passé."),
        ("Souhaiter un rétablissement",
         "« Bon rétablissement » ou « j'espère que la douleur diminue ». Court et "
         "sincère."),
        ("Offrir quelque chose de précis",
         "« Je peux faire ton quart de vendredi. » Une offre concrète se répond par oui "
         "ou par non ; une offre vague oblige à demander."),
        ("Ne pas donner de conseil médical",
         "N'écrivez pas ce qu'il faut mettre sur la plaie. C'est le rôle de "
         "l'infirmière, et un mauvais conseil circule vite."),
    ], notes="La quatrième carte est un point d'éthique simple. Le dire une fois, "
             "clairement.")

    d.pratique('Pratique · 3 de 4', "Écrivez le message",
               "Trois à cinq phrases. Nouvelles, souhait, offre concrète.", [
        ("La situation",
         "Votre collègue s'est brûlé l'avant-bras au travail et a trois jours de congé."),
        ("Ce que vous savez",
         "La brûlure est du deuxième degré. Il doit appliquer une crème deux fois par "
         "jour."),
        ("Ce que vous offrez",
         "Quelque chose de précis, que vous pouvez vraiment faire cette semaine."),
    ], corrige=False,
       notes="Vingt minutes d'écriture individuelle. Ramasser : ces messages sont "
             "l'évaluation écrite du module.")

    d.pratique('Pratique · 4 de 4', "Relisez avant d'envoyer",
               "Cinq vérifications, dans l'ordre.", [
        ("Les verbes du passé sont-ils au passé composé ?", "auxiliaire + participe"),
        ("Les auxiliaires sont-ils les bons ?", "être pour les pronominaux"),
        ("Les participes sont-ils accordés ?", "avec être seulement"),
        ("L'offre est-elle concrète ?", "elle se répond par oui ou non"),
        ("Est-ce que je donne un conseil médical ?", "si oui, l'enlever"),
    ], corrige=True,
       notes="Faire faire la relecture par le voisin. Une relecture croisée trouve deux "
             "fois plus d'oublis qu'une relecture par l'auteur.")

    d.billet(
        "En une phrase : qu'est-ce que vous ferez différemment la prochaine fois qu'un accident arrivera ?",
        exemples=[
            "Pensez à la première séance : l'huile, l'eau froide, les quinze minutes.",
            "Une seule phrase, honnête. Elle n'est pas notée.",
        ],
        notes="Lire quelques billets à voix haute, sans nommer les auteurs. C'est la "
              "meilleure préparation à la séance de bilan.")

    return d.save(dossier)
