# -*- coding: utf-8 -*-
"""B2 · Exigence ou atout ?
Bloc B « Défi 1 · L'offre d'emploi » · couleur teal · 75 min.
Source : exercices `t1parties` et `t1exig`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='teal',
        titre="Exigence ou atout ?",
        chapeau="Une ligne d'offre dit soit « il me le faut », soit « ce "
                "serait bien ». Confondre les deux fait renoncer à des postes "
                "qu'on aurait obtenus.",
        duree='75 minutes')

    d.titre(notes="Séance courte en matière neuve, longue en pratique. L'essentiel se "
                  "joue sur les offres réelles apportées par le groupe.")

    d.objectifs([
        "reconnaître les mots qui annoncent une exigence ;",
        "reconnaître ceux qui annoncent un atout ;",
        "situer une ligne dans la bonne partie de l'offre ;",
        "décider de postuler ou non, et savoir pourquoi.",
    ])

    d.declencheur(
        'Observation', "« L'anglais serait apprécié. »",
        pistes=[
            "Cette phrase veut-elle dire que l'anglais est obligatoire ?",
            "Postuleriez-vous sans parler anglais ?",
            "Et si c'était écrit « anglais requis » ?",
            "Qu'est-ce qui change, entre les deux phrases ?",
        ],
        notes="Le conditionnel « serait » est le signal. Le faire remarquer avant de "
              "donner la règle : le groupe le trouve souvent seul.")

    d.tableau('Repérage', "Les mots qui annoncent",
              ['Ce qui est écrit', 'Ce que ça veut dire'],
              [["requis, exigé, obligatoire, indispensable", "sans cela, la candidature n'est pas retenue"],
               ["un atout, un plus, serait apprécié", "un avantage, jamais une condition"],
               ["souhaitable, un atout majeur", "l'employeur y tient, mais il engagera sans"],
               ["une capacité, une aptitude", "à vérifier : parfois requis, parfois non"]],
              cle=0,
              note="Le conditionnel — serait, pourrait — annonce presque toujours un atout.",
              notes="Diapositive à photographier. Cette grille se lit sur n'importe "
                    "quelle offre du secteur.")

    d.pratique('Application', "Exigence, ou atout ?",
               "Six lignes tirées d'offres réelles.", [
        ("« Deux ans d'expérience en entrepôt sont requis. »", "exigence"),
        ("« La connaissance d'un logiciel d'inventaire est un atout. »", "atout"),
        ("« Français fonctionnel à l'oral et à l'écrit. »", "exigence"),
        ("« L'anglais serait apprécié. »", "atout"),
        ("« Capacité à soulever des charges de 20 kg. »", "exigence"),
        ("« Une expérience du meuble serait un plus. »", "atout"),
    ], corrige=True,
       notes="Faire dire à voix haute le mot qui a permis de décider. C'est le mot, pas "
             "le sens général, qui tranche.")

    d.pratique('Repérage', "De quelle partie vient cette ligne ?",
               "Nommez la partie de l'offre.", [
        ("« Quarante employés, à Longueuil, depuis 1998. »", "l'entreprise"),
        ("« Recevoir les livraisons et vérifier les quantités. »", "les tâches"),
        ("« Deux ans d'expérience sont requis. »", "les exigences"),
        ("« 37,5 h par semaine, du lundi au vendredi. »", "les conditions"),
        ("« Assurance collective après trois mois. »", "les avantages"),
        ("« Faire parvenir votre CV avant le 15 mars. »", "comment postuler"),
    ], corrige=True,
       notes="Les deux dernières parties ne sont pas dans la grille de quatre : les "
             "avantages prolongent les conditions, et « comment postuler » ferme "
             "l'offre. Le dire, sans compliquer la grille.")

    d.regle("La date limite",
            "Elle se lit en premier, pas en dernier.",
            precision="« Faire parvenir votre curriculum vitæ avant le 15 mars » : cette "
                      "ligne se trouve à la fin de l'offre, et c'est celle qui décide si "
                      "on a le temps de postuler. La chercher avant de lire le reste "
                      "évite de préparer une candidature pour rien.",
            notes="Diapositive à photographier. Faire vérifier tout de suite la date "
                  "limite de l'offre que chacun a apportée.")

    d.piege("Renoncer parce qu'un atout manque",
            "Je ne connais pas leur logiciel, je ne postule pas.",
            "Je connais un logiciel semblable, je postule.",
            "Un atout n'est pas une condition : l'employeur l'écrit précisément parce "
            "qu'il est prêt à engager sans. Se retirer soi-même d'un concours qu'on "
            "n'a pas perdu est l'erreur la plus coûteuse de la recherche d'emploi.",
            notes="Demander qui, dans le groupe, a déjà renoncé à postuler pour cette "
                  "raison. Presque toujours, plusieurs mains se lèvent.")

    d.billet(
        "Sur votre offre, soulignez les exigences et encerclez les atouts.",
        exemples=[
            "Comptez : combien d'exigences avez-vous ? Combien vous en manque-t-il ?",
            "S'il ne manque que des atouts, vous postulez.",
        ],
        notes="Ce billet mène directement à la décision de postuler. Prévoir de "
              "l'accompagner pour ceux à qui il manque une exigence réelle.")

    return d.save(dossier)
