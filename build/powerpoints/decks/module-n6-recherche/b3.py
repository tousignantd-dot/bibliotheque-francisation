# -*- coding: utf-8 -*-
"""B3 · Les mots en -able.
Bloc B « Défi 1 · L'offre d'emploi » · couleur ambre · 60 min.
Source : exercice `t1able`, mini-leçon du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Les mots en -able",
        chapeau="Une offre d'emploi est un texte court qui doit tout dire. "
                "Elle écrit « un contrat renouvelable » plutôt que « un "
                "contrat qu'on peut renouveler ». Un suffixe, et quatre mots "
                "économisés.",
        duree='60 minutes')

    d.titre(notes="La séance prolonge A3 sur la formation des mots, mais avec un seul "
                  "suffixe, celui qui revient le plus dans les offres.")

    d.objectifs([
        "former un adjectif en -able à partir d'un verbe ;",
        "comprendre qu'il dit toujours une possibilité ;",
        "connaître la petite famille en -ible ;",
        "employer le préfixe in- pour dire le contraire.",
    ])

    d.declencheur(
        'Observation', "« Une expérience transférable. »",
        pistes=[
            "De quel verbe vient ce mot ?",
            "Que veut-il dire, exactement ?",
            "Pourquoi l'offre l'écrit-elle ainsi ?",
            "Cela vous concerne-t-il ?",
        ],
        notes="Le mot « transférable » vaut la séance à lui seul : c'est celui qu'un "
              "élève doit employer pour dire que son expérience acquise ailleurs "
              "compte ici.")

    d.tableau('Anatomie', "Trois gestes, toujours les mêmes",
              ['L\'étape', 'Ce qu\'on fait'],
              [["1. On part du verbe", "renouveler"],
               ["2. On enlève -er ou -re", "renouvel-"],
               ["3. On ajoute -able", "renouvelable"]],
              cle=0,
              note="Le sens ne change jamais : -able veut toujours dire « qu'on peut ».",
              notes="Diapositive à photographier. Faire fabriquer trois adjectifs avec "
                    "des verbes du métier de chacun.")

    d.cartes("Les mots en -ible", "Une petite famille à apprendre par cœur", [
        ("disponible",
         "Le plus utile de tous : libre, prêt à commencer. « Je suis disponible dès lundi. »"),
        ("flexible, accessible",
         "Un horaire flexible s'adapte ; un lieu accessible se rejoint facilement."),
        ("compatible, lisible, possible",
         "Ils s'apprennent un par un : aucune règle ne permet de deviner le -ible."),
        ("Ce sont presque tous des mots du travail",
         "C'est une bonne nouvelle : les apprendre sert deux fois."),
    ], notes="Ne pas chercher de règle : il n'y en a pas. Insister sur « disponible », "
             "qui reviendra dans la lettre de motivation et en entrevue.")

    d.regle("Le préfixe in-",
            "On le colle devant, et le sens s'inverse.",
            precision="Acceptable devient inacceptable ; disponible devient indisponible. "
                      "Devant un b ou un p, in- s'écrit im- : impossible, imprévisible. "
                      "Devant un l, il- : illisible. Quelques adjectifs refusent le "
                      "préfixe et prennent « non » devant, séparé par une espace : un "
                      "salaire non négociable.",
            notes="Diapositive à photographier. En cas de doute sur in- ou non, « non » "
                  "passe toujours : c'est le refuge sûr.")

    d.pratique('Application', "Formez l'adjectif",
               "Transformez le verbe entre parenthèses.", [
        ("Une expérience qu'on peut transférer. (transférer)", "transférable"),
        ("Un contrat qu'on peut renouveler. (renouveler)", "renouvelable"),
        ("Un horaire qu'on peut adapter. (adapter)", "adaptable"),
        ("Un salaire qu'on peut négocier. (négocier)", "négociable"),
        ("Un poste qu'on ne peut pas accepter. (accepter, au négatif)", "inacceptable"),
        ("Une candidate qu'on peut joindre. (le mot en -ible)", "disponible"),
    ], corrige=True,
       notes="Le dernier item n'est pas une transformation : c'est un mot de vocabulaire. "
             "Le dire, sinon le groupe cherche un verbe qui n'existe pas.")

    d.pratique('Lecture', "Six phrases d'offres réelles",
               "Que veut dire le mot souligné ?", [
        ("Le poste est disponible immédiatement.", "libre, à prendre tout de suite"),
        ("Votre expérience est transférable.", "elle compte ici aussi"),
        ("Contrat renouvelable après un an.", "on peut le prolonger"),
        ("L'horaire est flexible du lundi au jeudi.", "il peut s'adapter"),
        ("Ce document est illisible : réécrivez-le.", "on ne peut pas le lire"),
        ("Salaire négociable selon l'expérience.", "on peut en discuter"),
    ], corrige=True,
       notes="La dernière phrase est celle qu'on cherche : elle veut dire que le montant "
             "affiché n'est pas le dernier mot.")

    d.piege("Croire que -able dit un fait accompli",
            "Un horaire modifiable est un horaire qui a été modifié.",
            "Un horaire modifiable est un horaire qu'on peut modifier.",
            "Le suffixe dit une possibilité, jamais un fait. La différence compte : un "
            "poste « renouvelable » n'est pas renouvelé d'avance, et une expérience "
            "« transférable » demande encore d'être expliquée à l'employeur.",
            notes="Point de vigilance pour les langues où le même suffixe marque le "
                  "passé. Vérifier auprès du groupe.")

    d.billet(
        "Écrivez trois adjectifs en -able utiles à votre métier.",
        exemples=[
            "Partez de trois verbes que vous employez tous les jours au travail.",
            "Exemple : réparer · réparable ; livrer · livrable ; laver · lavable.",
        ],
        notes="Certains donneront des formes qui n'existent pas. Les accueillir : la "
              "règle est productive, et l'erreur montre qu'elle est comprise.")

    return d.save(dossier)
