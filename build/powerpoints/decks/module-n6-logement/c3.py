# -*- coding: utf-8 -*-
"""C3 · La réponse, et ce qui tient debout dedans
Bloc C « Défi 2 · L'avis et la réponse » · couleur teal · 90 min.
Source : exercice `t2reponse` (type texte) et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='teal',
        titre="La réponse, et ce qui tient debout dedans",
        chapeau="Onze jours plus tard, une lettre arrive. Correcte sur un "
                "point, discutable sur deux autres — et c'est tout l'objet de "
                "la séance.",
        duree='90 minutes')

    d.titre(notes="Séance la plus délicate du module. Le réflexe du groupe sera de "
                  "s'indigner ; le travail consiste à découper avant de juger. Le "
                  "dire dès le départ.")

    d.objectifs([
        "découper une lettre de refus en quatre sortes de passages ;",
        "peser un motif avec deux questions ;",
        "distinguer une dépense réelle d'un montant décidé d'avance ;",
        "poser une question par écrit au lieu d'affirmer un droit.",
    ], notes="Le quatrième objectif est le plus important, et le plus difficile pour "
             "un adulte qui se sent lésé. C'est aussi ce qui fait la différence entre "
             "un dossier qui avance et une chicane.")

    d.declencheur(
        'Discussion', "Vous recevez un refus que vous trouvez injuste. Que faites-vous le soir même ?",
        pistes=[
            "Répondre tout de suite, ou attendre le lendemain ?",
            "Aller frapper à la porte, ou écrire ?",
            "Qu'est-ce qui reste au dossier, dans un cas comme dans l'autre ?",
        ],
        notes="Faire dire honnêtement ce que chacun ferait. La réponse « j'irais lui "
              "parler tout de suite » est majoritaire, et c'est celle qu'il faut "
              "retourner : ce qui se dit dans un escalier ne se prouve pas.")

    d.tableau('Analyse', "Quatre sortes de passages, dans la même lettre",
              ['Le passage', 'Ce qu\'on en fait'],
              [["un fait", "on l'accepte : c'est notre propre preuve"],
               ["une décision", "c'est son droit ; on regarde les motifs"],
               ["un motif", "on le pèse, un par un"],
               ["une demande d'argent", "on demande à quoi elle correspond"]],
              cle=0,
              note="Répondre à tout d'un coup fait perdre les trois quarts du terrain.",
              notes="Diapositive à photographier. Faire l'exercice au surligneur sur la "
                    "lettre projetée : quatre couleurs, quatre sortes de passages, "
                    "avant toute discussion sur le fond.")

    d.cartes('Les deux motifs', "Le même critère, deux résultats", [
        ("« je préfère les personnes en emploi »", "Une préférence. Elle ne se vérifie pas et elle ne regarde pas cette personne-ci en particulier : elle vaudrait contre n'importe quel étudiant."),
        ("« un défaut de paiement en 2024 »", "Un fait vérifiable, qui regarde bien la personne proposée. C'est le genre de motif qui tient debout — encore faut-il qu'il soit exact."),
        ("Les deux questions", "Le motif regarde-t-il la personne ou le logement ? Peut-il se montrer ? Il faut deux oui ; un seul ne suffit pas."),
        ("Ce que ce n'est pas à vous de faire", "Trancher. Apprécier un motif est le travail du Tribunal, s'il est saisi. Le vôtre est de savoir quoi demander, et à qui."),
    ], notes="Insister sur la dernière carte. Le module n'apprend pas à gagner : il "
             "apprend à lire, à demander et à savoir où s'adresser. Un enseignant qui "
             "laisse croire autre chose met ses élèves en difficulté.")

    d.regle("Un chiffre rond n'est pas une dépense",
            "Le locateur peut réclamer ce que la sous-location lui occasionne réellement.",
            precision="Une vérification de crédit, par exemple, s'il en fait une. "
                      "Une somme fixe décidée d'avance ne se rattache à aucune "
                      "dépense. La bonne réaction n'est pas de refuser : c'est de "
                      "demander par écrit à quoi le montant correspond. Ou bien la "
                      "réponse le justifie, ou bien elle ne vient pas.",
            notes="Diapositive à photographier. La formule « pourriez-vous me préciser "
                  "à quelles dépenses ce montant correspond » vaut la peine d'être "
                  "écrite au tableau et recopiée : elle sert bien au-delà du logement.")

    d.pratique('Lecture', "Où est la réponse dans la lettre ?",
               "Nommez le passage de la réponse qui répond.", [
        ("Quand la lettre a-t-elle été écrite ?", "la date, le 29 novembre"),
        ("Comment sait-il quand il a reçu l'avis ?", "il a signé la copie le 18"),
        ("A-t-il répondu dans le délai ?", "à l'intérieur des quinze jours"),
        ("Quelle est sa décision ?", "il n'accepte pas la sous-location"),
        ("Quel motif est une préférence ?", "il préfère les personnes en emploi"),
        ("Quel motif se vérifie ?", "le défaut de paiement de 2024"),
    ], corrige=True,
       notes="Même travail que dans l'exercice interactif. Faire remarquer que la "
             "première question a une réponse rassurante : il a répondu dans le délai, "
             "donc le silence n'a pas joué. Un dossier commence par ce qui est acquis.")

    d.piege('Attention',
            "répondre le soir même, fâché",
            "attendre le lendemain matin",
            "Une lettre écrite en colère reste au dossier et donne des "
            "arguments à l'autre partie. Le délai qui vous concernait est "
            "d'ailleurs déjà passé : vous avez le temps, et c'est le seul "
            "avantage de la situation.",
            notes="Prendre le temps de cette diapositive. Elle vaut pour bien d'autres "
                  "situations que le logement, et c'est souvent le conseil dont les "
                  "élèves se souviennent un an plus tard.")

    d.billet(
        "Écrivez la question que vous poseriez sur les deux cents dollars.",
        exemples=[
            "Une seule phrase, au conditionnel.",
            "Demandez, n'affirmez pas.",
        ],
        notes="Cinq minutes. Comparer deux ou trois formulations : celles qui "
              "commencent par « vous n'avez pas le droit » et celles qui commencent "
              "par « pourriez-vous ». La différence de résultat est facile à faire "
              "sentir.")

    return d.save(dossier)
