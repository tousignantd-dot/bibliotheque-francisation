# -*- coding: utf-8 -*-
"""C3 · Rapporter ce que quelqu'un a dit
Bloc C « Défi 2 · L'article » · couleur ambre · 75 min.
Source : exercice `t2indirect` et sa mini-leçon — la concordance des temps
dans le discours indirect au passé.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Rapporter ce que quelqu'un a dit",
        chapeau="Quand vous racontez aujourd'hui ce que quelqu'un a dit hier, "
                "vous vous placez à hier. Les temps reculent d'un cran pour "
                "le montrer.",
        duree='75 minutes')

    d.titre(notes="Deuxième point de grammaire du Défi 2, et le plus exigeant du "
                  "module. Prévoir de l'étaler : mieux vaut deux déplacements maîtrisés "
                  "que trois survolés.")

    d.objectifs([
        "transformer une parole directe en parole rapportée au passé ;",
        "employer le plus-que-parfait pour ce qui était déjà fait ;",
        "employer le conditionnel présent pour ce qui restait à venir ;",
        "adapter les repères de temps et les pronoms.",
    ], notes="Les objectifs deux et trois sont les seuls exigibles à l'évaluation. Le "
             "quatrième se travaille par imitation.")

    d.declencheur(
        'Observation', "La même phrase, deux fois",
        pistes=[
            "Elle a dit : « Je vous rappellerai. »",
            "Elle a promis qu'elle me rappellerait.",
            "Qu'est-ce qui a changé dans le verbe ?",
            "Et dans le pronom ?",
        ],
        notes="Deux changements à trouver, pas un. Les élèves voient le verbe et "
              "manquent presque toujours le passage de « vous » à « me ».")

    d.regle("Le point de référence recule",
            "Verbe introducteur au passé : les temps de ce qui est rapporté reculent d'un cran.",
            precision="Ce n'est vrai que si le verbe qui introduit est au passé. « Elle "
                      "dit qu'elle viendra » ne change rien ; « elle a dit qu'elle "
                      "viendrait », oui. Le déclencheur est toujours le verbe "
                      "introducteur - c'est lui qu'il faut regarder en premier.",
            notes="Diapositive à photographier. Faire chercher le verbe introducteur "
                  "avant toute transformation : c'est le réflexe à installer.")

    d.tableau('Analyse', "Les trois déplacements, et rien de plus",
              ['Ce qu\'on rapporte', 'Le temps devient'],
              [["ce qui était déjà fait (passé composé)", "le plus-que-parfait : il avait perdu"],
               ["ce qui était en cours (présent)", "l'imparfait : le dossier était à l'étude"],
               ["ce qui restait à venir (futur)", "le conditionnel présent : elle rappellerait"],
               ["variante plus parlée", "aller à l'imparfait + infinitif : elle allait rappeler"]],
              cle=0,
              note="Trois lignes. Presque tout le discours indirect au passé tient là-dedans.",
              notes="Diapositive à photographier. C'est le tableau de référence : y "
                    "revenir à chaque phrase de l'exercice.")

    d.cartes("Les trois transformations sur des phrases du module", "Direct, puis rapporté", [
        ("« J'ai perdu des clients. »",
         "Il a expliqué qu'il avait perdu des clients. - passé composé vers plus-que-parfait"),
        ("« Le dossier est à l'étude. »",
         "Elle a précisé que le dossier était à l'étude. - présent vers imparfait"),
        ("« Je vous rappellerai. »",
         "Elle a promis qu'elle me rappellerait. - futur vers conditionnel"),
        ("« Je vais vous répondre par écrit. »",
         "Elle a dit qu'elle allait me répondre par écrit. - futur proche vers imparfait"),
    ], notes="Les quatre phrases viennent de l'entrevue. Faire retrouver l'original dans "
             "l'extrait : le lien avec un texte réel fixe la règle mieux qu'un tableau.")

    d.piege("Le conditionnel qui n'est pas un doute",
            "Selon la conseillère, elle viendrait peut-être.",
            "Elle a promis qu'elle viendrait.",
            "Le même conditionnel sert deux fois dans ce module, et c'est le piège "
            "central du Défi 2. Au Défi 1, il marquait une information non confirmée. "
            "Ici, il marque simplement de l'avenir raconté depuis le passé : elle a "
            "bien promis, il n'y a aucun doute. C'est le verbe introducteur qui tranche - "
            "« selon nos informations » ou « elle a promis ».",
            notes="Piège essentiel. Le poser explicitement : les élèves qui ont bien "
                  "compris B3 vont sur-interpréter ici, et c'est bon signe.")

    d.tableau('Analyse', "Ce qui change aussi, et qu'on oublie",
              ['Au style direct', 'Rapporté au passé'],
              [["hier", "la veille"],
               ["demain", "le lendemain"],
               ["maintenant", "alors"],
               ["« je vous rappellerai »", "elle me rappellerait"]],
              cle=0,
              note="Dans un article, c'est souvent au pronom qu'on repère qu'une parole est rapportée.",
              notes="Ces changements ne sont pas exigibles à l'évaluation, mais ils "
                    "s'entendent partout. Les faire reconnaître, pas produire.")

    d.pratique('Application', "Rapportez au passé",
               "Le verbe introducteur est déjà au passé composé.", [
        ("« Le comité n'a pas encore reçu l'analyse. » Elle m'a dit que...", "le comité n'avait pas encore reçu l'analyse"),
        ("« Je vous rappellerai. » Elle a promis qu'elle...", "me rappellerait"),
        ("« J'ai déjà perdu des clients. » Il a expliqué qu'il...", "avait déjà perdu des clients"),
        ("« Le dossier est à l'étude. » Elle a précisé que...", "le dossier était à l'étude"),
        ("« Le conseil se prononcera le 14 octobre. » Elle a annoncé que...", "le conseil se prononcerait le 14 octobre"),
        ("« Les heures seront négociées plus tard. » Elle a indiqué que...", "les heures seraient négociées plus tard"),
    ], corrige=True,
       notes="La dernière combine passif et conditionnel : la garder pour la fin et la "
             "faire décomposer en deux temps.")

    d.billet(
        "Rapportez une phrase que quelqu'un vous a dite cette semaine.",
        exemples=[
            "Commencez par : « Il m'a dit que... » ou « Elle m'a dit que... »",
            "Attention au temps du verbe, et au pronom.",
        ],
        notes="Deux minutes. Les erreurs de pronom sont les plus fréquentes et les plus "
              "faciles à corriger en groupe.")

    return d.save(dossier)
