# -*- coding: utf-8 -*-
"""A4 · Les lieux du dossier et les mots pour les nommer
Bloc A « Je découvre » · couleur ambre · 75 min. Dernière séance du bloc :
les six lieux, les seize mots, et le passage au défi 1.
Source : exercices `prImg` et `prVocab`, banc `FC_CARDS`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n8-actualite' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Seize mots, et onze qui ne s'illustrent pas",
        chapeau="Le vocabulaire de l'actualité est presque tout abstrait : "
                "une thèse, une concession, un parti pris. Il ne se retient "
                "pas en regardant une photo ; il se retient en s'en servant.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. Prévenir le groupe dès le début : cinq "
                  "mots seulement ont une image dans le module, et ce n'est pas un "
                  "oubli. Les onze autres ne se voient pas.")

    d.objectifs([
        "comprendre et employer les seize mots du module ;",
        "reconnaître les six lieux du dossier et dire ce qui s'y passe ;",
        "distinguer ce qui se photographie de ce qui ne se photographie pas ;",
        "réemployer les mots du bloc A dans une phrase de son cru.",
    ], notes="Le troisième objectif prépare la lecture des deux articles du bloc B, "
             "qui sont abstraits d'un bout à l'autre.")

    d.declencheur(
        'Observation', "Où se décide ce dossier, concrètement ?",
        image=IMG + 'hotel-de-ville.jpg',
        pistes=[
            "Qu'est-ce que ce bâtiment ? À quoi le voit-on ?",
            "Qui y entre un soir de séance du conseil ?",
            "Combien de personnes étaient dans la salle, selon le module ?",
            "Êtes-vous déjà entré dans un hôtel de ville au Québec ?",
        ],
        notes="Onze personnes dans la salle : c'est le chiffre à faire ressortir. "
              "Une ville de vingt-quatre mille habitants, un vote qui engage onze "
              "hectares, onze personnes présentes. Le groupe le remarque tout seul.")

    d.cartes('Analyse', "Six lieux, six moments du dossier", [
        ("De grands érables en lisière",
         "Les quatre hectares boisés que le comité veut garder. Des érables "
         "de soixante ans, et les toits d'un quartier juste derrière."),
        ("Du gravier plat, une clôture",
         "Les trois hectares de remblai, sur l'ancienne cour de voirie. "
         "Plus rien n'y pousse : c'est le « terrain vague » du Courant."),
        ("Un hôtel de ville en brique rouge",
         "La séance du conseil, un soir d'automne, devant onze personnes. "
         "C'est là aussi que le registre s'ouvrira, pour une journée."),
        ("Un studio minuscule, un micro",
         "La chronique du mercredi et la tribune téléphonique de CIRC, la "
         "radio communautaire. Douze minutes d'antenne, une ligne ouverte."),
        ("Un comptoir de retour de livres",
         "Là où Mirela travaille, et où le dossier commence : une affiche "
         "oubliée et une question posée à une habituée."),
        ("Un terrain vide derrière un aréna",
         "Le second terrain municipal, déjà déboisé, déjà desservi. "
         "Il n'est dans aucun des deux articles."),
    ], notes="Reprend l'exercice d'association du module. Le dernier lieu est le "
             "plus important : c'est celui qui n'est nulle part dans la presse, "
             "parce qu'il n'était pas dans le communiqué de la Ville.")

    d.vocabulaire('Vocabulaire 1 de 3', "Les genres et les médias", [
        ("un éditorial", "Le texte où un journal dit lui-même ce qu'il pense d'une question."),
        ("une chronique", "Un texte ou une capsule signés, où une même personne donne son avis chaque semaine."),
        ("le courrier des lecteurs", "La page d'un journal où le public peut faire publier son opinion."),
        ("un communiqué", "Le texte qu'un organisme envoie aux médias pour annoncer sa version d'une nouvelle."),
        ("une manchette", "Le grand titre du haut de la page, celui qu'on lit même sans lire l'article."),
        ("une radio communautaire", "Une petite station locale sans but lucratif, animée en partie par des bénévoles."),
    ], notes="Les six mots de A1. Les faire redire sans les définitions à l'écran : "
             "une semaine a passé, la reprise coûte deux minutes.")

    d.vocabulaire('Vocabulaire 2 de 3', "Lire un texte d'opinion", [
        ("un parti pris", "Le fait de pencher d'un côté avant même d'examiner la question."),
        ("une source", "La personne ou le document d'où vient un renseignement rapporté."),
        ("une thèse", "L'idée principale qu'un texte d'opinion veut faire accepter."),
        ("une concession", "Le moment où l'on reconnaît que l'autre a raison sur un point, avant de répondre."),
        ("une nuance", "Une précision qui empêche de prendre une phrase pour plus large qu'elle n'est."),
    ], notes="Les cinq mots les plus abstraits du module, et les cinq qui servent le "
             "plus au bloc C. « Concession » est le mot pivot : le poser "
             "soigneusement, avec l'exemple du chroniqueur qui se contredit.")

    d.vocabulaire('Vocabulaire 3 de 3', "Le terrain et la procédure", [
        ("un boisé", "Un petit terrain couvert d'arbres, souvent en ville ou juste à côté."),
        ("un remblai", "Un terrain rempli de terre et de gravier rapportés, où presque rien ne pousse."),
        ("une assemblée de consultation", "La rencontre publique où une ville explique un projet et écoute les gens."),
        ("un registre référendaire", "Le cahier qu'on ouvre une journée pour compter ceux qui demandent un référendum."),
        ("une personne habile à voter", "Quelqu'un qui a le droit de signer ou de voter dans une municipalité donnée."),
    ], notes="Les cinq mots concrets, dont quatre portent une image dans le module. "
             "« Personne habile à voter » est une expression figée du droit municipal "
             "québécois : la faire répéter en entier, elle ne se découpe pas.")

    d.tableau('Analyse', "Pourquoi onze mots n'ont pas de photo",
              ['Se photographie', 'Ne se photographie pas'],
              [["un boisé, un remblai",
                "une thèse, une concession"],
               ["un registre référendaire",
                "un parti pris, une nuance"],
               ["une assemblée de consultation",
                "un éditorial, une source, une manchette"]],
              cle=0,
              notes="Diapositive à photographier. La leçon vaut au-delà du module : un "
                    "mot abstrait se retient par un exemple, jamais par une image, et "
                    "une image posée derrière lui montre le thème à sa place.")

    d.pratique('Pratique 1 de 2', "Le mot juste",
               "Complétez avec un mot du module.", [
        ("Les deux journaux ont travaillé à partir du même ___ de la Ville.", "communiqué"),
        ("La ___ parlait d'un terrain vague ; l'article, lui, parlait d'érables.", "manchette"),
        ("La ___ de l'éditorial tient en une phrase : le logement passe avant le paysage.", "thèse"),
        ("Sa ___ est franche : il admet que le vote a été pris trop vite.", "concession"),
        ("Le ___ exigeait sept cent quatre-vingt-douze signatures.", "registre référendaire"),
        ("Il ajoute une ___ : c'est une estimation du service, pas une règle de loi.", "nuance"),
        ("Le reportage cite deux ___ : le promoteur et le service de l'urbanisme.", "sources"),
        ("Elle a envoyé sa lettre au ___ le lendemain de l'assemblée.", "courrier des lecteurs"),
    ], corrige=True,
       notes="Faire lire la phrase entière une fois le mot trouvé. Les huit phrases "
             "sont réutilisables telles quelles dans la lettre du bloc E.")

    d.pratique('Pratique 2 de 2', "Deux mots qu'on confond",
               "Dites lequel des deux convient, et pourquoi.", [
        ("Le journal appuie le projet dans son ___ de la semaine.", "éditorial - c'est le journal qui parle"),
        ("Ferland donne son avis chaque mercredi dans sa ___.", "chronique - une personne signe"),
        ("Quatre hectares d'érables de soixante ans : un ___.", "boisé"),
        ("Trois hectares de gravier où rien ne pousse : un ___.", "remblai"),
        ("La Ville explique, le public parle, rien ne se vote : une ___.", "assemblée de consultation"),
        ("On y écrit son nom pendant une journée : un ___.", "registre référendaire"),
    ], corrige=True,
       notes="Les deux premières paires sont celles qui reviennent aux examens. "
             "Formule à faire retenir : l'éditorial engage le journal, la chronique "
             "n'engage que celui qui la signe.")

    d.regle("Ce qui manque est aussi une information",
            "Un chiffre qu'on ne trouve nulle part, une évaluation non "
            "publiée, un terrain jamais étudié : l'absence se remarque et se "
            "dit.",
            precision="C'est la porte du défi 1. Vous allez lire deux articles sur la "
                      "même séance du conseil, et l'exercice ne sera pas de trouver "
                      "qui ment : ce sera de relever ce que chacun a choisi de garder, "
                      "et ce qu'il n'a mis nulle part.",
            notes="Diapositive à photographier. Elle ferme le bloc A et annonce le "
                  "bloc B : le dire explicitement, pour que la séance suivante ne "
                  "parte pas de zéro.")

    d.billet(
        "Reprenez les deux comptes rendus que vous avez trouvés à la séance A1.",
        exemples=[
            "Écrivez une phrase qui n'apparaît que dans l'un des deux.",
            "Écrivez une chose que vous auriez voulu y lire et qui n'y est pas.",
        ],
        notes="Devoir écrit court. La deuxième consigne est la vraie : elle fait "
              "chercher une absence, ce que personne ne fait spontanément. Les "
              "réponses ouvrent la séance B1.")

    return d.save(dossier)
