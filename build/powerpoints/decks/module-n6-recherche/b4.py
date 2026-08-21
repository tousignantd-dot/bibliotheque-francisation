# -*- coding: utf-8 -*-
"""B4 · Le petit mot « où », et se renseigner sur l'entreprise.
Bloc B « Défi 1 · L'offre d'emploi » · couleur ambre · 75 min. Fin du Défi 1.
Source : exercices `t1ou` et `t1entreprise`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n6-recherche/images/')


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="« où », et se renseigner sur l'entreprise",
        chapeau="« C'est l'entreprise où j'ai appris le métier. » Un mot de "
                "trois lettres évite de répéter, et il sert justement à parler "
                "de son parcours — les lieux et les années.",
        duree='75 minutes')

    d.titre(notes="Deux choses dans cette séance : un point de grammaire et une "
                  "méthode de recherche. Elles se rejoignent à la fin, dans la phrase "
                  "qu'on prépare pour l'entrevue.")

    d.objectifs([
        "relier deux phrases avec « où » ;",
        "employer « où » pour un lieu comme pour un moment ;",
        "ne pas le confondre avec « ou » sans accent ;",
        "trouver en cinq minutes ce qu'il faut savoir d'une entreprise.",
    ])

    d.declencheur(
        'Observation', "Deux phrases, un mot répété.",
        pistes=[
            "« C'est l'entrepôt. Je travaille dans cet entrepôt. »",
            "Quel mot est dit deux fois ?",
            "Comment feriez-vous une seule phrase ?",
            "Et pour « 2024, c'est l'année. Je suis arrivée cette année-là. » ?",
        ],
        notes="La première se trouve vite ; la seconde surprend. Beaucoup proposent "
              "« quand ». C'est précisément la difficulté de la séance.")

    d.tableau('Anatomie', "Un lieu, ou un moment",
              ['Ce qu\'il remplace', 'La phrase'],
              [["un lieu", "C'est l'entrepôt où je travaille."],
               ["un moment", "2024, c'est l'année où je suis arrivée."],
               ["un lieu, au figuré", "C'est le secteur où j'ai le plus d'expérience."]],
              cle=0,
              note="En français, on ne dit pas « l'année quand ». C'est « où », même pour le temps.",
              notes="Diapositive à photographier. C'est la surprise de la séance, et "
                    "l'erreur la plus fréquente à ce point du cours.")

    d.regle("« où » et « ou »",
            "L'accent change tout.",
            precision="« où » avec l'accent parle d'un lieu ou d'un moment. « ou » sans "
                      "accent propose un choix. Le test qui ne rate jamais : remplacez "
                      "par « ou bien ». Si la phrase a du sens, il n'y a pas d'accent — "
                      "« je commence lundi ou bien mardi ». Sinon, l'accent est "
                      "nécessaire.",
            notes="Diapositive à photographier. Le test des « ou bien » se fait de tête, "
                  "en une seconde, et il est fiable.")

    d.pratique('Application', "Reliez les deux phrases avec « où »",
               "Écrivez la phrase complète.", [
        ("C'est l'entreprise. J'ai travaillé six ans dans cette entreprise.",
         "C'est l'entreprise où j'ai travaillé six ans."),
        ("Voici le jour. J'ai passé mon entrevue ce jour-là.",
         "Voici le jour où j'ai passé mon entrevue."),
        ("Longueuil est la ville. Boisverte est installée dans cette ville.",
         "Longueuil est la ville où Boisverte est installée."),
        ("C'est le moment. Il faut poser ses questions à ce moment-là.",
         "C'est le moment où il faut poser ses questions."),
    ], corrige=True,
       notes="Faire lire à voix haute la phrase reliée : l'oreille confirme ce que la "
             "règle explique.")

    d.pratique('Discrimination', "« ou » ou « où » ?",
               "Choisissez, puis justifiez par le test de « ou bien ».", [
        ("Je peux commencer lundi ___ mardi.", "ou — « ou bien » fonctionne"),
        ("L'année ___ je suis arrivée, je ne parlais pas français.", "où — un moment"),
        ("Préférez-vous le jour ___ le soir ?", "ou — un choix"),
        ("C'est l'entrepôt ___ je travaille.", "où — un lieu"),
    ], corrige=True,
       notes="Quatre items suffisent : c'est un réflexe à installer, pas une matière à "
             "couvrir.")

    d.declencheur(
        'Méthode', "« Que savez-vous de nous ? »",
        image=IMG + 'conseillere-bureau.jpg',
        pistes=[
            "Cette question tombe une fois sur deux en entrevue.",
            "Où trouver la réponse, gratuitement ?",
            "Combien de temps faut-il y consacrer ?",
            "Qu'est-ce qu'on cherche, au juste ?",
        ],
        notes="Cinq minutes de lecture suffisent. Le dire clairement : beaucoup croient "
              "qu'il faut une enquête, et renoncent.")

    d.cartes("Où se renseigner", "Trois sources gratuites", [
        ("Le site de l'entreprise",
         "Sections « À propos », « Notre équipe », « Carrières ». L'année de fondation, le nombre d'employés, les postes ouverts."),
        ("Le Registraire des entreprises",
         "L'adresse légale et le nom des dirigeants. Utile pour vérifier qu'une entreprise existe vraiment."),
        ("Les avis d'anciens employés",
         "À lire avec prudence : les gens satisfaits écrivent rarement."),
        ("Ce qu'on en fait",
         "Une seule phrase, en entrevue : « J'ai vu que vous fabriquez du bois massif depuis 1998. »"),
    ], notes="La quatrième carte est l'essentiel : on ne récite pas ce qu'on a lu, on en "
             "tire une phrase.")

    d.billet(
        "Renseignez-vous sur l'entreprise de votre offre, en cinq minutes.",
        exemples=[
            "Depuis quand existe-t-elle ? Combien d'employés ? Où sont ses installations ?",
            "Écrivez ensuite UNE phrase que vous diriez en entrevue.",
        ],
        notes="Cette phrase servira telle quelle en D1 et en E1. Demander de la garder.")

    return d.save(dossier)
