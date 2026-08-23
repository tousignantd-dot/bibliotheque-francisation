# -*- coding: utf-8 -*-
"""A2 · Ce que la voix ajoute aux mots
Bloc A « Je découvre » · couleur indigo · 75 min. Le seul savoir de
phonétique du niveau 8 : produire l'intonation expressive.
Source : exercice `prInto` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Quatre mélodies, et ce qu'elles disent à votre place",
        chapeau="Le programme du niveau 8 ne demande plus qu'une chose à "
                "l'oreille et à la voix : produire l'intonation expressive. "
                "Pas un son nouveau — une mélodie.",
        duree='75 minutes')

    d.titre(notes="Séance très orale. Prévoir de faire répéter debout : assis, "
                  "personne n'ose exagérer, et l'exagération est justement ce qui "
                  "fait entrer une mélodie dans l'oreille.")

    d.objectifs([
        "reconnaître à l'oreille la surprise, la déception, la volonté et l'incompréhension ;",
        "produire chacune des quatre sur une phrase courte du dossier ;",
        "comprendre pourquoi une voix plate se lit comme de l'indifférence ;",
        "choisir trois phrases de son intervention et décider de leur mélodie.",
    ], notes="Le troisième objectif est celui qui compte le plus à une tribune "
             "téléphonique, où personne ne voit votre visage. Y revenir à la fin.")

    d.declencheur(
        'Écoute', "La même phrase, trois fois : qu'est-ce qui change ?",
        pistes=[
            "« Quatre voix contre trois, pour onze hectares ? »",
            "« Quatre voix contre trois, pour onze hectares. »",
            "« Quatre voix contre trois... pour onze hectares. »",
            "Les mots sont identiques. Qu'est-ce qui ne l'est pas ?",
        ],
        notes="Dire les trois soi-même, sans annoncer laquelle est laquelle. Le "
              "groupe entend la différence avant de savoir la nommer, et c'est le "
              "bon ordre. Ne pas écrire les noms au tableau tout de suite.")

    d.regle("Quatre mélodies, quatre intentions",
            "La surprise monte d'un coup à la fin. La déception tombe dès la "
            "première syllabe. La volonté descend et appuie. "
            "L'incompréhension freine et laisse un silence avant le mot en "
            "cause.",
            precision="Aucune des quatre ne s'écrit : elles ne vivent que dans la voix. "
                      "C'est pour cela qu'un argument bien construit peut être dit "
                      "d'une façon qui le contredit, et que l'interlocuteur croira "
                      "toujours la voix plutôt que les mots.",
            notes="Diapositive à photographier. Les noms sont ceux du programme, mot "
                  "pour mot. Aucun symbole ni aucun signe de transcription : on décrit "
                  "la mélodie avec des mots, et le groupe la reproduit à l'oreille.")

    d.cartes('Analyse', "Comment chacune se fabrique", [
        ("La surprise",
         "La phrase part normalement puis grimpe brusquement sur les deux ou "
         "trois dernières syllabes. Souvent une question, souvent courte, "
         "souvent annoncée par « comment ça » ou par la répétition du chiffre "
         "qui étonne."),
        ("La déception",
         "La mélodie descend tout de suite et ne remonte jamais. Le débit est "
         "régulier, presque lent, souvent précédé d'un petit mot isolé : "
         "« ah », « bon »."),
        ("La volonté",
         "À l'inverse de la surprise : la mélodie descend, le débit ralentit, "
         "les syllabes se détachent. C'est la voix d'une demande qu'on ne "
         "retirera pas. On ne sourit pas en la disant."),
        ("L'incompréhension",
         "On ne monte pas : on freine. Le débit se casse à l'endroit précis "
         "où le fil s'est rompu, avec un petit silence avant le mot en cause. "
         "La voix isole le mot."),
    ], notes="Dire chaque exemple deux fois avant de faire répéter. Insister sur la "
             "volonté : c'est celle que les élèves ratent le plus, parce qu'ils la "
             "montent au lieu de la descendre.")

    d.tableau('Analyse', "La même phrase, plusieurs intentions",
              ['Ce qui est dit', 'Ce que la voix ajoute'],
              [["Le vote a été pris à vingt-deux heures cinquante ?",
                "surprise : la voix monte sur l'heure"],
               ["Le vote a été pris à vingt-deux heures cinquante.",
                "constat : la voix reste plate"],
               ["Je veux voir l'évaluation.",
                "volonté : la voix descend, les mots pèsent"],
               ["Je veux voir l'évaluation ?",
                "doute : la phrase se retourne contre celui qui parle"],
               ["Bon. Je veux voir l'évaluation.",
                "le « bon » tombe, puis la volonté descend"]],
              cle=0,
              notes="Diapositive à photographier. Faire dire les cinq lignes par cinq "
                    "élèves différents, dans le désordre, et faire deviner au groupe "
                    "laquelle vient d'être dite.")

    d.pratique('Pratique 1 de 2', "Quelle intention entendez-vous ?",
               "Écoutez chaque réplique, puis dites : surprise, déception ou "
               "volonté.", [
        ("Quatre voix contre trois, pour onze hectares ?", "surprise"),
        ("Ah. Je pensais que l'évaluation était publique.", "déception"),
        ("Je vais signer, et je vais le dire en ondes.", "volonté"),
        ("Comment ça, personne n'a compté les arbres ?", "surprise"),
        ("Bon. On avait trois cents signatures ce matin aussi.", "déception"),
        ("Ce document-là, je le veux avant mardi.", "volonté"),
        ("Personne ne nous a répondu. Personne.", "déception"),
        ("Je tiens à ce que ce soit écrit au procès-verbal.", "volonté"),
    ], corrige=True,
       notes="Le module en propose neuf, huit suffisent en classe. Faire redire "
             "chaque réplique par un élève après la correction, jamais avant : "
             "sinon on entend la réponse dans la voix de celui qui lit.")

    d.piege('Piège', "monter la voix à chaque phrase",
            "descendre quand on affirme",
            "C'est le défaut le plus fréquent, et il vient de la prudence : on "
            "n'ose pas conclure. Une mélodie qui monte partout transforme "
            "chaque affirmation en question, et chaque demande en demande "
            "d'autorisation. À une tribune téléphonique, l'effet est immédiat : "
            "l'animateur reprend la parole parce qu'il croit la phrase inachevée.",
            notes="Faire l'expérience à voix haute : dire « je vais signer le "
                  "registre » en montant, puis en descendant. Le groupe entend la "
                  "différence tout de suite, sans explication.")

    d.piege('Piège', "mettre de la colère dans la voix pour être entendu",
            "garder la mélodie de la volonté, qui descend",
            "La colère fait monter et accélérer ; en ondes, elle donne raison "
            "à celui qui reste calme. La voix de la volonté est plus lente que "
            "la voix de la colère, et beaucoup plus difficile à interrompre. "
            "C'est la leçon la plus utile du bloc D, et elle s'apprend ici.",
            notes="Rappeler l'échange du module : Mirela dit « je ne dis pas qu'il "
                  "est illégal, je dis qu'il est petit ». Phrase dure, mélodie "
                  "descendante, personne ne l'interrompt.")

    d.pratique('Pratique 2 de 2', "Dites-le avec la bonne mélodie",
               "Chacun choisit une phrase et la dit deux fois : d'abord à "
               "plat, puis avec l'intention demandée. Le groupe dit s'il "
               "l'entend.", [
        ("Trois cent quarante-deux arbres ? (surprise)", "montante d'un coup sur le chiffre"),
        ("Ah. Bon. (déception)", "deux syllabes qui tombent, sans phrase"),
        ("Ce document-là, je le veux avant mardi. (volonté)", "descendante, appuyée sur « veux »"),
        ("Attendez, je perds le fil. (incompréhension)", "le débit freine, la voix se creuse"),
        ("Vous avez bien dit vingt et un mois ? (surprise)", "on isole le chiffre dont on doute"),
    ], corrige=True,
       notes="Exercice debout. Le « à plat » d'abord est essentiel : c'est la "
             "comparaison qui enseigne, pas la réussite du premier essai. Ne pas "
             "corriger la prononciation ici, seulement la mélodie.")

    d.billet(
        "Enregistrez-vous en disant une phrase de votre future intervention, puis réécoutez-vous.",
        exemples=[
            "« Ce que je demande, c'est... »",
            "Est-ce que votre voix monte ou descend à la fin ?",
        ],
        notes="Devoir court. Beaucoup d'élèves s'entendent monter pour la première "
              "fois de leur vie, et cela vaut trois explications. Reprendre les "
              "enregistrements en une minute au début de A3.")

    return d.save(dossier)
