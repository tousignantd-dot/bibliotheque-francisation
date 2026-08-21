# -*- coding: utf-8 -*-
"""A1 · Qu'est-ce que vous cherchez, exactement ?
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n6-recherche/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Qu'est-ce que vous cherchez, exactement ?",
        chapeau="Une recherche d'emploi commence par une phrase, pas par un "
                "curriculum vitæ : le titre du poste qu'on vise. Sans elle, on "
                "postule partout et on n'est rappelé nulle part.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Demander d'abord au groupe qui a déjà "
                  "cherché un emploi au Québec, et qui travaille en ce moment. Les "
                  "réponses donnent le ton : beaucoup ont un emploi qui ne correspond "
                  "pas à ce qu'ils faisaient avant.")

    d.objectifs([
        "nommer un poste par son titre exact et son secteur d'activité ;",
        "dire ce qu'on faisait avant, avec une durée ;",
        "reconnaître les mots de base du monde du travail ;",
        "distinguer le temps plein du temps partiel, le permanent du contrat.",
    ], notes="Le quatrième objectif paraît mince. Il ne l'est pas : « permanent » et "
             "« temps partiel » décident du revenu réel d'une famille.")

    d.declencheur(
        'Observation', "Que faisiez-vous, dans votre pays ?",
        image=IMG + 'conseillere-bureau.jpg',
        pistes=[
            "Quel était le titre exact de votre poste ?",
            "Pendant combien de temps ?",
            "Est-ce que ce métier existe ici ?",
            "Faites-vous la même chose aujourd'hui ?",
        ],
        notes="Question sensible : plusieurs élèves occupaient un poste plus qualifié "
              "que celui qu'ils ont ici. Accueillir la réponse sans commenter. Le module "
              "part de ce qu'ils savent faire, jamais de ce qui leur manque.")

    d.dialogue('Dialogue · 1 de 3', "Deux ans, et un temps partiel", [
        ("DJAMILA", "Bonjour, madame Aguirre. Asseyez-vous. Alors, vous venez me voir pour une recherche d'emploi ?", True),
        ("MARISOL", "Oui. Ça fait deux ans que je suis au Québec. Je travaille trois jours par semaine dans un entrepôt, mais c'est du temps partiel.", True),
        ("DJAMILA", "Et vous aimeriez un poste à temps plein. Qu'est-ce que vous faisiez avant d'arriver ici ?", True),
        ("MARISOL", "J'étais responsable des stocks dans une entreprise de meubles, à Medellín. Pendant six ans.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Djamila reformule avant de poser sa question : « Et vous aimeriez un poste "
             "à temps plein. » C'est ce que fait une bonne conseillère, et c'est ce qu'un "
             "élève peut faire aussi pour vérifier qu'il a compris.")

    d.dialogue('Dialogue · 2 de 3', "L'expérience se raconte", [
        ("DJAMILA", "Six ans, c'est une belle expérience. Vous aviez des gens sous votre responsabilité ?", True),
        ("MARISOL", "Trois personnes. Je faisais l'inventaire, je vérifiais les commandes, je préparais les bons de livraison.", True),
        ("DJAMILA", "Donc vous connaissez le domaine. Ce n'est pas rien : beaucoup de gens changent complètement de secteur en arrivant.", True),
        ("MARISOL", "Je ne veux pas changer. Je veux le même travail, mais ici. Le problème, c'est que je ne sais pas comment m'y prendre.", True),
    ], notes="Marisol répond par des verbes d'action : je faisais, je vérifiais, je "
             "préparais. Faire remarquer qu'elle ne dit pas « je travaillais » tout court "
             "— c'est déjà la leçon du Défi 2.")

    d.dialogue('Dialogue · 3 de 3', "Ce qu'on offre, pas ce qui manque", [
        ("MARISOL", "Commis à l'inventaire, je dirais. Ou adjointe à la logistique, si c'est possible.", True),
        ("DJAMILA", "Très bien. Ce sont deux titres qui existent vraiment, et ça, c'est la moitié du travail.", True),
        ("MARISOL", "Et si l'employeur voit que je viens d'arriver ? Il va prendre quelqu'un d'autre.", True),
        ("DJAMILA", "Vous avez six ans dans le domaine. C'est ce que vous offrez, et c'est ça qu'il faut dire. Pas ce qui vous manque.", True),
    ], notes="La dernière réplique est la phrase-clé du module entier. La faire répéter, "
             "puis y revenir en E1.")

    d.tableau('Analyse', "Ce que Djamila cherche à savoir, et pourquoi",
              ['Sa question', 'Ce qu\'elle en fait'],
              [["Depuis quand êtes-vous ici ?", "situer le parcours, pas juger"],
               ["Que faisiez-vous avant ?", "trouver l'expérience à réutiliser"],
               ["Aviez-vous des gens sous votre responsabilité ?", "mesurer le niveau du poste"],
               ["Quel titre visez-vous ?", "sans titre, la recherche part dans tous les sens"]],
              cle=0,
              note="Une conseillère pose quatre questions en cinq minutes. Elles suffisent à orienter une recherche.",
              notes="Diapositive à photographier. Ces quatre questions sont exactement "
                    "celles que l'élève devra se poser seul.")

    d.regle("Le titre du poste",
            "Une recherche d'emploi commence par un titre exact.",
            precision="« Je cherche du travail » ne mène nulle part : les offres sont "
                      "classées par titre. « Commis à l'inventaire », « préposé aux "
                      "bénéficiaires », « aide-cuisinier » — ce sont ces mots-là qu'on "
                      "tape dans un site d'emploi, et ce sont eux qu'on écrit dans une "
                      "lettre.",
            notes="Diapositive à photographier. Faire chercher, pour la prochaine séance, "
                  "le titre exact du métier de chacun.")

    d.cartes("Quatre mots qui décident du revenu", "À bien distinguer", [
        ("Le temps plein",
         "De trente-cinq à quarante heures par semaine. C'est ce que la plupart cherchent."),
        ("Le temps partiel",
         "Moins de trente heures. Souvent le premier emploi, rarement le dernier."),
        ("Un poste permanent",
         "Sans date de fin prévue. Ce n'est pas une garantie d'emploi à vie, mais ce n'est pas un contrat."),
        ("Un contrat ou un remplacement",
         "Avec une date de fin écrite. Utile pour entrer quelque part, à savoir dès le départ."),
    ], notes="Demander qui, dans le groupe, sait si son emploi actuel est permanent. "
             "Beaucoup ne le savent pas — et c'est écrit sur leur relevé de paie.")

    d.piege("Répondre par ce qui manque",
            "Je viens d'arriver, je ne parle pas bien.",
            "J'ai six ans d'expérience dans ce domaine.",
            "Un employeur n'engage pas pour combler un manque : il engage pour un besoin. "
            "La phrase qui commence par une excuse place le candidat en position de "
            "demandeur ; celle qui commence par l'expérience le place en position "
            "d'offrant. Les deux sont vraies — une seule fait avancer.",
            notes="Ce piège revient dans toutes les entrevues du module. Le nommer ici, "
                  "y revenir en D1 et en E1.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Marisol est au Québec depuis deux ans.", "vrai"),
        ("Elle travaille à temps plein dans un entrepôt.", "faux — trois jours par semaine"),
        ("Elle était responsable des stocks pendant six ans.", "vrai"),
        ("Elle veut changer complètement de secteur.", "faux — elle veut le même métier, ici"),
        ("Son curriculum vitæ est en français.", "faux — encore en espagnol"),
        ("Djamila lui conseille de parler de ce qui lui manque.", "faux — de ce qu'elle offre"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Écrivez le titre exact du poste que vous cherchez.",
        exemples=[
            "Dans quel secteur d'activité se trouve-t-il ?",
            "Combien d'années avez-vous faites dans ce domaine ?",
        ],
        notes="Devoir concret. Ces deux lignes serviront de point de départ à toutes les "
              "séances suivantes, jusqu'à la lettre de motivation du bloc C.")

    return d.save(dossier)
