# -*- coding: utf-8 -*-
"""E1 · L'appel, pour de vrai
Bloc E « Je me lance » · couleur teal · 75 min.
Source : jeu de rôle `refusassurance` et production orale du bloc `custom`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Vous menez l'appel",
        chapeau="L'assistant joue l'agente au règlement des sinistres. Elle "
                "est polie, elle connaît le dossier, et elle ne décide rien. "
                "Tout ce qu'elle peut faire, c'est inscrire une note.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Deux temps : le jeu de rôle avec "
                  "l'assistant, environ quarante minutes, puis l'enregistrement de "
                  "la production orale. Prévoir des écouteurs, sinon la salle "
                  "devient inaudible.")

    d.objectifs([
        "mener un appel de contestation du début à la fin ;",
        "obtenir qu'une phrase précise soit inscrite au dossier ;",
        "raconter à voix haute une décision qu'on a subie, en trois temps ;",
        "réemployer la concession et l'hypothèse irréelle sans y penser.",
    ], notes="Le deuxième objectif est le critère de réussite du jeu de rôle, et il "
             "est mesurable : l'agente relit à voix haute ce qu'elle inscrit.")

    d.regle("Ce que vous pouvez obtenir, et ce que vous ne pouvez pas",
            "Vous n'obtiendrez pas que le dossier soit rouvert : cette "
            "personne n'en a pas le pouvoir. Vous pouvez obtenir qu'une "
            "phrase soit inscrite, et qu'une pièce soit demandée.",
            precision="Pour cela, il faut que ce soit inscriptible : un fait, une "
                      "date, une pièce, une demande précise. « C'est injuste » ne "
                      "s'inscrit nulle part et n'atteint personne.",
            notes="Diapositive à photographier avant de commencer. Le dire clairement "
                  "évite la déception du milieu de l'exercice : l'assistant ne cédera "
                  "pas, et ce n'est pas un défaut.")

    d.cartes('Jeu de rôle', "Trois situations, la même personne au bout du fil", [
        ("Le refus, et son motif",
         "Réclamation refusée : « défaut d'entretien du drain de plancher », "
         "exclusion 7.3. Dommages de 19 400 $, franchise de 1 000 $. Vous "
         "appelez pour la première fois depuis la lettre."),
        ("Deux documents, deux tuyaux",
         "La lettre parle du drain de plancher, le rapport du drain de "
         "fondation. Personne chez l'assureur ne l'avait remarqué avant "
         "vous."),
        ("La contre-expertise",
         "Onze pages, vingt-deux photographies datées, une caméra passée le "
         "19 octobre : aucune racine, écoulement libre. Et la facture "
         "acquittée du 3 mai."),
    ], notes="Chaque élève choisit sa situation. Les plus à l'aise prennent la "
             "troisième, qui exige de tenir plusieurs faits à la fois. On peut aussi "
             "jouer l'agente : c'est plus difficile qu'il n'y paraît.")

    d.tableau('Consignes', "Les huit sujets à couvrir",
              ['Au début', 'Ensuite'],
              [["Nom, numéro de dossier, date", "Un fait daté, avec sa pièce"],
               ["« Trois points, ce sera court »", "Une concession : certes…, mais…"],
               ["Le motif cité dans ses mots", "Une hypothèse irréelle"],
               ["", "Trois demandes, puis le délai"]],
              cle=0,
              notes="Diapositive à laisser affichée pendant tout le jeu de rôle. Les "
                    "huit sujets sont aussi dans le module, cochables un par un.")

    d.piege(
        'Registre',
        "Hausser le ton parce qu'on n'obtient rien",
        "Descendre la voix et redemander précisément",
        "L'agente ne cédera pas davantage si vous vous fâchez — elle n'en a "
        "pas le pouvoir. Ce qui la fait avancer, c'est une phrase qu'elle "
        "peut recopier au dossier. Et souvenez-vous de la séance A2 : une "
        "demande dite avec une mélodie montante devient une demande de "
        "permission. Descendez, et appuyez.",
        notes="Faire le lien explicitement avec l'intonation travaillée en A2. C'est "
              "la seule séance où les deux se rencontrent, et les élèves ne font pas "
              "le lien seuls.")

    d.regle("La production orale : trois temps, deux minutes",
            "Racontez une décision que vous avez trouvée injuste — un refus, "
            "un montant, un délai, un dossier fermé. Ici ou dans votre pays.",
            precision="Temps 1 : annoncez de quoi vous allez parler, avec une date. "
                      "Temps 2 : ce qui s'était passé avant, ce qui s'est passé, le "
                      "motif — avec un chiffre. Temps 3 : ce que vous auriez fait "
                      "autrement, puis la démarche entreprise.",
            notes="Diapositive à photographier. Le temps 2 réemploie le "
                  "plus-que-parfait de A4 et le temps 3 l'hypothèse irréelle de C4. "
                  "Le dire : ils reconnaîtront ce qu'ils savent déjà faire.")

    d.pratique('Préparation', "Avant d'enregistrer, notez cinq choses",
               "Cinq mots-clés, pas des phrases : vous ne devez pas lire.", [
        ("La date de la décision", "un jour, un mois, une année"),
        ("Le motif, dans les mots de l'autre", "trois ou quatre mots"),
        ("Un fait qui la contredit", "avec une date"),
        ("Un chiffre", "un montant, une durée, un nombre"),
        ("Ce que vous avez fait ensuite", "une démarche, pas un sentiment"),
    ], corrige=False,
       notes="Cinq minutes de préparation écrite, montre en main. Sans elles, "
             "l'enregistrement part dans tous les sens et dure quatre minutes.")

    d.billet(
        "Écoutez votre enregistrement une fois, et notez une seule chose à améliorer.",
        exemples=[
            "Une seule. Pas trois.",
            "Puis réenregistrez-vous en ne changeant que celle-là.",
        ],
        notes="Le module garde l'enregistrement et permet de l'envoyer à "
              "l'enseignante. Rappeler que rien ne part sans un geste de l'élève : la "
              "rétroaction de l'IA reste privée.")

    return d.save(dossier)
