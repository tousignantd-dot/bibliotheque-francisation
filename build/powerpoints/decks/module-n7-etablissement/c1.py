# -*- coding: utf-8 -*-
"""C1 · Vingt-cinq minutes
Bloc C « Défi 2 · L'entrevue de sélection » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf` et son bandeau de quatre mots.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Vingt-cinq minutes',
        chapeau="Deux personnes de l'autre côté de la table, six questions "
                "dont aucune n'a de réponse écrite quelque part. Le comité "
                "cherche qui tiendra les dix-huit mois.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc C. Beaucoup d'élèves n'ont jamais passé "
                  "d'entrevue en français. Le dire, et dire aussi que ce n'est pas "
                  "un examen de langue.")

    d.objectifs([
        "répondre à une question ouverte en deux ou trois phrases ;",
        "donner un exemple concret plutôt qu'un adjectif ;",
        "dire ce qu'on ne connaît pas sans se disqualifier ;",
        "nommer les quatre mots de l'entrevue avec leur article.",
    ], notes="Le troisième objectif est le plus difficile et le plus payant : le "
             "comité fait davantage confiance à qui sait nommer ce qu'il ignore.")

    d.declencheur(
        'Observation', "Qu'est-ce qu'un comité cherche à savoir ?",
        pistes=[
            "Est-ce qu'il cherche la personne qui parle le mieux ?",
            "Que veut-il savoir sur votre horaire ? sur votre famille ?",
            "Pourquoi demande-t-il ce qui sera difficile pour vous ?",
            "Que répondriez-vous à cette question-là ?",
        ],
        notes="La dernière question fait travailler tout le monde. Laisser trois "
              "minutes d'écriture avant de faire répondre à voix haute.")

    d.dialogue('Dialogue · 1 de 3', "Pourquoi ce diplôme-là", [
        ("ÉMILIEN", "On a vingt-cinq minutes. Il n'y a pas de piège dans nos questions.", True),
        ("ÉMILIEN", "Commençons simplement. Pourquoi ce diplôme-là, et pourquoi maintenant ?", True),
        ("RANIA", "Ce que je fais aujourd'hui, je le fais bien, mais je m'arrête toujours au même endroit.", True),
        ("RANIA", "Quand il faut donner un médicament ou noter un signe, je vais chercher quelqu'un d'autre.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Faire remarquer la structure de la réponse : un constat, puis un "
             "exemple précis. Deux phrases, et le comité sait tout.")

    d.dialogue('Dialogue · 2 de 3', "Ce que je ne connais pas", [
        ("YVAN", "Vous savez ce que ça change, comme responsabilité ?", True),
        ("RANIA", "Une partie, oui. Ce que je ne connais pas, c'est ce qui se passe quand une décision est mauvaise et qu'elle est la mienne.", True),
        ("YVAN", "C'est la bonne réponse, et c'est la seule qui compte pour moi.", True),
        ("ÉMILIEN", "Vous avez fait deux ans en soins infirmiers à Alep. Racontez-nous.", True),
    ], notes="Réplique centrale du bloc. Dire ce qu'on ne connaît pas, précisément, "
             "vaut mieux que prétendre tout savoir. Le faire répéter.")

    d.dialogue('Dialogue · 3 de 3', "L'horaire est déjà réglé", [
        ("YVAN", "La formation est à temps plein, il y a des stages, et vous travaillez. Comment vous organisez-vous ?", True),
        ("RANIA", "J'ai parlé à ma coordonnatrice avant de déposer mon dossier.", True),
        ("RANIA", "Je passe de cinq quarts à deux, les fins de semaine, à partir de septembre.", True),
        ("ÉMILIEN", "Donc c'est déjà réglé ?", True),
    ], notes="Insister sur « avant de déposer mon dossier ». Ce n'est pas une "
             "intention, c'est une chose faite — et le comité entend la différence.")

    d.regle("Un exemple concret vaut mieux qu'un adjectif",
            "« Je suis calme » ne dit rien ; raconter ce qu'on a fait la semaine "
            "passée dit tout.",
            precision="Une aptitude se prouve par une scène : un jour, une personne, "
                      "un geste. Le comité n'a aucun moyen de vérifier un adjectif, et "
                      "il en entend deux cents par année.",
            notes="Diapositive à photographier. C'est la même règle qu'en B1, "
                  "appliquée à l'oral : le groupe doit l'entendre deux fois.")

    d.tableau('Analyse', "Six questions, et ce qu'elles cherchent",
              ['La question', 'Ce que le comité cherche'],
              [['pourquoi ce diplôme', "un motif ancré dans du vécu, pas un rêve"],
               ['votre parcours', "ce qui a été fait, et ce qui manque"],
               ["l'horaire", "si l'organisation est réglée ou souhaitée"],
               ['le plus difficile', "la lucidité, jamais la perfection"],
               ['vos questions', "si la fiche a été lue jusqu'au bout"]],
              cle=0,
              notes="Cinq rangées sans note : la densité tient. Faire préparer une "
                    "réponse par question, à l'écrit, pour la séance C4.")

    d.vocabulaire('Vocabulaire', "Quatre mots de l'entrevue", [
        ("un comité de sélection", "Le petit groupe qui reçoit les candidats et classe les dossiers."),
        ("un plan de carrière", "Ce qu'une personne veut faire dans son métier, et par quelles étapes."),
        ("une aptitude", "Ce qu'une personne est capable de faire, en dehors d'un diplôme."),
        ("un stage", "La période de la formation qui se passe en milieu de travail."),
    ], notes="« Un plan de carrière » fait peur : préciser que deux phrases suffisent "
             "— le diplôme, puis l'étape d'après.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'entrevue de Rania.", [
        ("L'entrevue dure vingt-cinq minutes.", "vrai"),
        ("Yvan Lemay est le conseiller pédagogique.", "faux - il est enseignant du programme"),
        ("Rania dit qu'elle s'arrête toujours au même endroit.", "vrai"),
        ("Elle demande que ses deux années d'études soient reconnues.", "faux - elle ne demande aucune reconnaissance"),
        ("Elle a parlé à sa coordonnatrice avant de déposer son dossier.", "vrai"),
        ("Le plus difficile pour elle sera de parler avec les patients.", "faux - c'est d'écrire au dossier"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique. Le dernier ouvre une "
             "discussion utile : nommer sa difficulté ne coûte rien quand on dit ce "
             "qu'on fait déjà pour la régler.")

    d.billet("Écris en deux phrases pourquoi tu veux la formation que tu vises.",
             exemples=["Je suis préposée depuis cinq ans et je m'arrête toujours au même endroit.",
                       "Je veux être celle qu'on va chercher."],
             notes="Ramasser les billets : ils deviennent la matière première de la "
                   "production orale du bloc E.")

    return d.save(dossier)
