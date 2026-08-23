# -*- coding: utf-8 -*-
"""A2 · Ce que la voix ajoute aux mots
Bloc A « Je découvre » · couleur indigo · 60 min. Le seul savoir de
phonétique du niveau 8 : produire l'intonation expressive.
Source : exercice `prInto` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Quatre mélodies, et ce qu'elles disent à votre place",
        chapeau="Le programme du niveau 8 ne demande plus qu'une chose à "
                "l'oreille : produire l'intonation expressive. Pas un son "
                "nouveau — une mélodie.",
        duree='60 minutes')

    d.titre(notes="Séance courte et très orale. Prévoir de faire répéter debout : "
                  "assis, personne n'ose exagérer, et l'exagération est justement "
                  "ce qui fait entrer une mélodie dans l'oreille.")

    d.objectifs([
        "reconnaître à l'oreille la surprise, l'incompréhension, la volonté et la déception ;",
        "produire chacune des quatre sur une phrase courte ;",
        "comprendre pourquoi une voix plate se lit comme de l'indifférence ;",
        "choisir trois phrases d'entrevue et décider de leur mélodie.",
    ], notes="Le troisième objectif est le seul qui compte vraiment pour l'emploi. "
             "Y revenir à la fin de la séance.")

    d.declencheur(
        'Écoute', "La même phrase, trois fois : qu'est-ce qui change ?",
        pistes=[
            "« L'équipe n'existe pas encore ? »",
            "« L'équipe n'existe pas encore. »",
            "« L'équipe n'existe pas encore... »",
            "Les mots sont identiques. Qu'est-ce qui ne l'est pas ?",
        ],
        notes="Dire les trois soi-même, sans annoncer laquelle est laquelle. Le groupe "
              "entend la différence avant de savoir la nommer, et c'est le bon ordre.")

    d.regle("Quatre mélodies, quatre intentions",
            "La surprise monte d'un coup à la fin. L'incompréhension freine "
            "et laisse un silence. La volonté descend et appuie. La déception "
            "tombe dès la première syllabe.",
            precision="Aucune de ces quatre ne s'écrit : elles ne vivent que dans la "
                      "voix. C'est pour cela qu'un texte bien construit peut être dit "
                      "d'une façon qui le contredit, et que l'interlocuteur croira "
                      "toujours la voix plutôt que les mots.",
            notes="Diapositive à photographier. Les quatre noms sont ceux du programme, "
                  "mot pour mot : surprise, incompréhension, volonté, déception.")

    d.cartes('Analyse', "Comment chacune se fabrique", [
        ("La surprise",
         "La phrase part normalement puis grimpe brusquement sur les deux ou "
         "trois dernières syllabes. Souvent une question, souvent courte."),
        ("L'incompréhension",
         "On ne monte pas : on freine. Le débit se casse à l'endroit précis "
         "où le fil s'est rompu, avec un petit silence avant le mot en cause."),
        ("La volonté",
         "La mélodie descend, le débit ralentit, les syllabes se détachent. "
         "C'est la voix de l'engagement, celle de la négociation."),
        ("La déception",
         "La mélodie descend dès la première syllabe et ne remonte jamais. "
         "Souvent un « ah » ou un « bon » en tête."),
    ], notes="Dire chaque exemple deux fois avant de faire répéter. Insister sur la "
             "volonté : c'est celle que les élèves ratent le plus, parce qu'ils la "
             "montent au lieu de la descendre.")

    d.pratique('Pratique', "Quelle intention entendez-vous ?",
               "Écoutez chaque réplique, puis dites : surprise, incompréhension "
               "ou volonté.", [
        ("Trois étapes pour un poste de superviseure ?", "surprise"),
        ("Attendez, je ne suis pas certaine de vous suivre.", "incompréhension"),
        ("Je vais y arriver, et je vais y arriver cette fois-ci.", "volonté"),
        ("Comment ça, l'équipe n'existe pas encore ?", "surprise"),
        ("Là, honnêtement, je perds le fil de votre explication.", "incompréhension"),
        ("Ce poste-là, je le veux, et je vous dis pourquoi.", "volonté"),
    ], corrige=True,
       notes="Le module en propose neuf ; six suffisent en classe. Faire redire chaque "
             "réplique par un élève après la correction, pas avant.")

    d.piege('Piège', "monter la voix à chaque phrase",
            "descendre quand on affirme",
            "C'est le défaut le plus fréquent, et il vient de la prudence : on "
            "n'ose pas conclure. Une mélodie qui monte partout transforme chaque "
            "affirmation en question, et chaque question en demande "
            "d'autorisation. Devant un comité de sélection, l'effet est "
            "immédiat : la personne paraît attendre la permission de parler.",
            notes="Faire l'expérience à voix haute : dire « ce poste m'intéresse » en "
                  "montant, puis en descendant. Le groupe entend la différence tout "
                  "de suite.")

    d.piege('Piège', "parler d'une voix parfaitement égale",
            "varier sur les trois phrases importantes",
            "Une voix plate se lit comme de l'indifférence, jamais comme du "
            "calme. Il ne s'agit pas de jouer la comédie : trois phrases sur "
            "quarante-cinq minutes suffisent. Choisissez-les d'avance — ce que "
            "vous apportez, ce que vous demandez, et la réponse à la question "
            "difficile.",
            notes="Les élèves très prudents à l'oral sont ceux qui en ont le plus "
                  "besoin, et ce sont ceux qui résisteront le plus. Ne pas insister "
                  "en public.")

    d.pratique('Production', "Dites-le avec la bonne mélodie",
               "Chacun choisit une phrase et la dit deux fois : d'abord à plat, "
               "puis avec l'intention demandée. Le groupe dit s'il l'entend.", [
        ("Ce poste-là, je le veux. (volonté)", "descendante, appuyée sur « veux »"),
        ("Vous avez bien dit quatre-vingt-dix minutes ? (surprise)", "montante sur le chiffre"),
        ("Excusez-moi, le mot « vérifiable ». (incompréhension)", "freinage, silence avant le mot"),
        ("Je tiens à ce que ce soit écrit. (volonté)", "descendante, syllabes détachées"),
    ], corrige=True,
       notes="Exercice debout. Le « à plat » d'abord est essentiel : c'est la "
             "comparaison qui enseigne, pas la réussite du premier essai.")

    d.billet(
        "Enregistrez-vous en disant une phrase d'entrevue, puis réécoutez-vous.",
        exemples=[
            "« Ce que j'apporte, c'est... »",
            "Est-ce que votre voix monte ou descend à la fin ?",
        ],
        notes="Devoir court. Beaucoup d'élèves s'entendent monter pour la première "
              "fois de leur vie, et cela vaut trois explications.")

    return d.save(dossier)
