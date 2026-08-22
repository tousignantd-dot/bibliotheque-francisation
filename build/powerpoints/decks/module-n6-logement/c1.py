# -*- coding: utf-8 -*-
"""C1 · Sur le palier du deuxième
Bloc C « Défi 2 · L'avis et la réponse » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Sur le palier du deuxième",
        chapeau="La règle du site ne parlait de personne. Ce soir, elle "
                "rencontre un propriétaire de soixante-trois ans qui n'aime "
                "pas les surprises.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 2. Faire le lien à voix haute : tout ce qui a été "
                  "lu au Défi 1 sert maintenant à tenir une conversation debout dans "
                  "un escalier, sans notes.")

    d.objectifs([
        "suivre une conversation où les deux personnes ne veulent pas la "
        "même chose ;",
        "reconnaître ce qui, dans le discours de Farida, vient du site ;",
        "nommer les cinq mots de la réponse écrite ;",
        "distinguer une demande de signature d'une demande d'accord.",
    ], notes="Le quatrième objectif est le plus fin de la séance, et le plus utile : "
             "faire signer une copie ne veut pas dire obtenir un oui.")

    d.declencheur(
        'Discussion', "Comment annoncer une chose que l'autre ne veut pas entendre ?",
        pistes=[
            "Faut-il commencer par la mauvaise nouvelle ou par la bonne ?",
            "Qu'est-ce qui met l'autre sur la défensive tout de suite ?",
            "Avez-vous déjà eu à annoncer quelque chose à un propriétaire ?",
        ],
        notes="Laisser les récits venir : plusieurs élèves ont eu des conversations "
              "difficiles avec un propriétaire. Ne pas juger les stratégies, les "
              "comparer ensuite avec celle de Farida.")

    d.dialogue('Dialogue · 1 de 3', "Le malentendu du début", [
        ("FARIDA", "Monsieur Tardif ? Vous avez deux minutes ? J'ai un papier à vous remettre et j'aimerais mieux vous l'expliquer moi-même.", True),
        ("LUCIEN", "Un papier. Ça commence bien. Ne me dites pas que vous résiliez : le bail court jusqu'au trente juin.", True),
        ("FARIDA", "Je ne résilie rien. C'est le contraire : je veux garder mon logement. Je pars six mois et je reviens le premier juillet.", True),
        ("LUCIEN", "Six mois. Et le loyer, pendant ce temps-là, il tombe du ciel ?", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Le malentendu est instructif : le locateur entend « départ » et pense "
             "« résiliation ». C'est le tableau de A1 qui règle la question, et Farida "
             "le fait en une phrase.")

    d.dialogue('Dialogue · 2 de 3', "Elle arrive avec un nom", [
        ("LUCIEN", "Sous-louer. J'ai déjà donné, moi. Il y a six ans, au quatre, ç'a été un vrai cirque.", True),
        ("FARIDA", "Je comprends que ça vous rende méfiant. C'est pour ça que je ne viens pas demander la permission en l'air : je viens avec un nom, une adresse et des dates.", True),
        ("LUCIEN", "Un étudiant. Il va me faire des partys jusqu'à trois heures du matin.", True),
        ("FARIDA", "Vous avez le droit de vérifier son dossier, et je vous encourage à le faire. Mais pour refuser, il faut un motif sérieux, et il doit regarder la personne.", True),
    ], notes="Deux choses à faire remarquer : elle reconnaît l'inquiétude de l'autre "
             "avant de répondre, et elle cite la règle sans dire « c'est la loi ». "
             "Les deux se réutilisent au jeu de rôle du bloc E.")

    d.dialogue('Dialogue · 3 de 3', "La date, pas l'accord", [
        ("FARIDA", "Voici l'avis. Daté d'aujourd'hui, le dix-huit novembre. Le nom de monsieur Trudel, son adresse, et les dates : du cinq janvier au vingt-huit juin.", True),
        ("LUCIEN", "Et je fais quoi avec ça, moi ?", True),
        ("FARIDA", "Vous avez quinze jours pour me répondre par écrit. Si vous ne répondez pas d'ici le trois décembre, la loi considère que vous avez consenti.", True),
        ("FARIDA", "Est-ce que vous accepteriez de me signer cette copie ? Ce n'est pas un accord, c'est une date.", True),
    ], notes="La dernière réplique est le cœur de la séance. Beaucoup de locateurs "
             "refusent de signer parce qu'ils croient s'engager : dire « ce n'est pas "
             "un accord, c'est une date » lève le refus neuf fois sur dix.")

    d.tableau('Analyse', "Ce qu'elle fait, et pourquoi ça marche",
              ['Elle fait', 'Ce que ça évite'],
              [["elle corrige le malentendu", "une conversation sur une résiliation"],
               ["elle nomme la personne", "un refus vague sur un projet vague"],
               ["elle cite la page", "de parler comme si elle décidait"],
               ["elle demande la date", "de ne pas pouvoir prouver le délai"]],
              cle=0,
              notes="Diapositive à photographier. C'est la grille du jeu de rôle de E1 : "
                    "les quatre gestes s'y retrouvent, et l'assistant les attend.")

    d.regle("Faire signer une copie, ce n'est pas obtenir un accord",
            "Une signature de réception prouve une date, rien de plus.",
            precision="Et c'est déjà l'essentiel : le délai de quinze jours part de "
                      "la réception. Sans preuve de cette date, on ne peut pas "
                      "établir la fin du délai — donc pas se prévaloir du silence. "
                      "Le dire à la personne avant de lui tendre le stylo enlève "
                      "toute la méfiance.",
            notes="Diapositive à photographier. Faire jouer la phrase par deux ou trois "
                  "élèves, debout, avec le ton : c'est une phrase qui se dit, pas une "
                  "phrase qui se sait.")

    d.vocabulaire('Vocabulaire', "Les cinq mots de la réponse écrite", [
        ("le consentement", "L'accord donné par une personne à ce que l'autre lui propose."),
        ("un accusé de réception", "La preuve écrite qu'une personne a bien reçu un document, avec la date."),
        ("une indemnité", "L'argent versé pour réparer une perte causée à quelqu'un."),
        ("des dommages", "Les dégâts causés à un logement, ou la perte d'argent qui en résulte."),
        ("le défaut de paiement", "Le fait de ne pas payer son loyer à la date prévue."),
    ], notes="Ces cinq mots paraîtront dans la lettre de refus lue en C3. Les poser "
             "maintenant évite d'avoir à s'arrêter en pleine lecture.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la scène du palier.", [
        ("Farida vient annoncer qu'elle résilie son bail.", "faux - elle veut le garder"),
        ("Elle arrive avec un nom, une adresse et des dates.", "vrai"),
        ("Monsieur Tardif a déjà eu une mauvaise sous-location.", "vrai"),
        ("Elle lui demande la permission de chercher quelqu'un.", "faux - elle a déjà trouvé"),
        ("Elle fait signer la copie pour prouver l'accord.", "faux - pour prouver la date"),
        ("Sans réponse avant le 3 décembre, il a consenti.", "vrai"),
    ], corrige=True,
       notes="Le cinquième énoncé est celui qui compte. Faire relire la réplique exacte "
             "avant de corriger : la nuance ne s'entend qu'une fois qu'on la cherche.")

    d.billet(
        "Quelle phrase de Farida vous a paru la plus habile ? Pourquoi ?",
        exemples=[
            "Une phrase, et une raison.",
            "Pensez à ce qui aurait pu mal tourner sans elle.",
        ],
        notes="Deux minutes. Les réponses servent à ouvrir E1 : ce que la classe a "
              "repéré comme habile est ce qu'elle réemploiera au jeu de rôle.")

    return d.save(dossier)
