# -*- coding: utf-8 -*-
"""D2 · La lettre d'affaires courantes
Bloc D « Défi 3 · Les deux écrits » · couleur ambre · 75 min.
Source du module : dialogue `t3`, exercices `t3formules`, `t3subj` et `t3cond`.
"""
import pathlib

from theme import Deck

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-emploi' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="La lettre d'affaires courantes",
        chapeau="Elle sort de l'entreprise, et ce qui y est écrit peut être "
                "invoqué plus tard. D'où sa longueur, ses formules, et le soin "
                "qu'on met à ne pas écrire « nous voulons acheter » quand on "
                "veut dire « nous demandons un prix ».",
        duree='75 minutes')

    d.titre(notes="Séance dense : le dialogue avec le fournisseur, les sept parties de "
                  "la lettre, ses formules, et les deux modes qui la portent - le "
                  "subjonctif de la demande et le conditionnel de la politesse. Prévoir "
                  "de terminer les deux derniers exercices en autonomie sur le module.")

    d.objectifs([
        "nommer les sept parties d'une lettre d'affaires ;",
        "employer la formule qui fait le travail voulu ;",
        "employer le subjonctif après un verbe de volonté ;",
        "employer le conditionnel pour demander, proposer et estimer.",
    ], notes="Les deux derniers objectifs sont les points de grammaire les plus "
             "exigeants du module. Ils sont ici parce que la lettre les impose : "
             "on ne les enseigne pas dans le vide.")

    d.declencheur(
        'Observation', "Une enveloppe, deux feuilles, un tableau de prix",
        image=IMG + 'quai-expedition.jpg',
        pistes=[
            "Avez-vous déjà écrit à une entreprise, en français ?",
            "Qu'est-ce qui vous a arrêté : les formules, la mise en page, la peur de mal dire ?",
            "Quelle différence avec un courriel ?",
            "Qu'est-ce qui se passe si on écrit « nous voulons acheter » ?",
        ],
        notes="La dernière question est celle du dialogue. La garder en suspens : elle "
              "trouve sa réponse à la quatrième diapositive de dialogue.")

    d.dialogue('Dialogue · 1 de 4', "Demander la bonne chose", [
        ("VINCENT", "Équipements Sorel, bonjour, Vincent Béliveau à l'appareil.", False),
        ("AÏCHA", "Bonjour monsieur Béliveau. Aïcha Traoré, de Meubles Rive-du-Nord. Je vous appelle au sujet d'une table élévatrice pour un poste d'emballage.", True),
        ("VINCENT", "Vous cherchez de l'information, ou vous êtes rendue au prix ?", False),
        ("AÏCHA", "Les deux, je pense. On voudrait une soumission écrite, mais avant je voudrais être sûre de vous demander la bonne chose.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Le conditionnel apparaît deux fois dans la dernière réplique : "
             "« on voudrait », « je voudrais ». Le faire remarquer sans l'expliquer.")

    d.dialogue('Dialogue · 2 de 4', "Trois données pour un prix juste", [
        ("VINCENT", "Il me faut trois choses : la charge maximale sur la palette, les dimensions de la palette, et la hauteur de travail que vous visez.", True),
        ("AÏCHA", "La palette standard, quarante-huit par quarante pouces. Douze cents livres pleine. La hauteur de travail, je ne sais pas.", False),
        ("VINCENT", "Prenez la hauteur du coude de la personne qui travaille là, debout, bras le long du corps. Mesurez-la sur deux ou trois personnes et donnez-moi la moyenne.", True),
        ("AÏCHA", "Je peux faire ça cet après-midi.", False),
    ], notes="Aïcha dit encore une fois ce qu'elle ne sait pas, et obtient une méthode "
             "pour le savoir. C'est le même geste qu'en C2, dans une autre situation.")

    d.dialogue('Dialogue · 3 de 4', "Un ordre de grandeur n'est pas un prix", [
        ("AÏCHA", "Est-ce que vous pouvez me donner un prix approximatif tout de suite ?", False),
        ("VINCENT", "Je peux vous donner un ordre de grandeur, en vous disant bien que ce n'est pas une soumission. Comptez entre quatre et sept mille dollars, selon la finition.", True),
        ("AÏCHA", "Et le plateau tournant, ça sert à quoi ?", False),
        ("VINCENT", "À ne pas contourner la palette. Sur un poste où on fait quatre-vingts caisses, ça change beaucoup de choses. Ça ajoute à peu près huit cents dollars.", True),
    ], notes="« Ce n'est pas une soumission » : le fournisseur se protège comme "
             "monsieur Cormier protégeait son entreprise. Faire remarquer que les deux "
             "côtés font le même geste.")

    d.dialogue('Dialogue · 4 de 4', "Ce qu'il faut écrire, et ce qu'il ne faut pas", [
        ("AÏCHA", "Est-ce que j'écris que nous voulons acheter ?", False),
        ("VINCENT", "Surtout pas. Vous écrivez que vous demandez une soumission. Dites simplement où vous en êtes : le projet est à l'étude, la décision se prend en octobre.", True),
        ("VINCENT", "Et quand vous recevrez notre soumission, regardez la date de validité en bas de page. Un prix d'équipement ne tient pas six mois.", True),
        ("AÏCHA", "Je ne l'aurais pas remarqué. Merci beaucoup, monsieur Béliveau.", False),
    ], notes="La date de validité est un détail que personne n'apprend nulle part et "
             "qui coûte cher. Le noter au tableau.")

    d.tableau('Analyse', "Les sept parties, de haut en bas",
              ['La partie', 'Ce qu\'elle contient'],
              [["Le lieu et la date", "en haut à droite, le mois en toutes lettres"],
               ["La vedette", "nom, fonction, entreprise, adresse du destinataire"],
               ["L'objet", "sans verbe conjugué, comme dans la note"],
               ["L'appel", "« Monsieur, » seul sur sa ligne, avec une virgule"],
               ["Le corps", "trois paragraphes : pourquoi, quoi, la suite"]],
              cle=0,
              note="Puis la salutation, qui reprend l'appel mot pour mot, et la signature, avec p. j. et c. c. s'il y a lieu.",
              notes="Diapositive à photographier. La vedette est ce qui manque le plus "
                    "souvent : sans elle, une lettre a l'air d'un courriel imprimé.")

    d.pratique('Pratique', "Que fait cette formule ?",
               "Chaque formule fait un travail précis.", [
        ("« Nous vous écrivons afin de... »", "ouvrir en disant tout de suite pourquoi"),
        ("« Je vous saurais gré de bien vouloir... »", "demander sans ordonner"),
        ("« Sous réserve de l'approbation du budget... »", "prévenir que rien n'est décidé"),
        ("« Vous trouverez ci-joint... »", "annoncer un document envoyé avec la lettre"),
        ("« Dans l'attente de votre réponse, »", "fermer le corps avant la salutation"),
        ("« Nous accusons réception de... »", "confirmer qu'un document est arrivé"),
    ], corrige=True,
       notes="C'est l'exercice `t3formules` du module, qui en compte huit. Insister sur "
             "« je vous saurais gré » : c'est le verbe savoir, jamais « je vous serais "
             "gré ». L'erreur est fréquente chez les francophones aussi.")

    d.regle("Le subjonctif après le verbe de volonté",
            "Je souhaite que vous nous FASSIEZ parvenir votre soumission.",
            precision="Vouloir que, souhaiter que, demander que, exiger que, préférer "
                      "que, il faut que, il importe que : tous au subjonctif. Les "
                      "verbes d'opinion, eux, prennent l'indicatif à la forme "
                      "affirmative - « je pense que la table EST nécessaire » - et "
                      "basculent au subjonctif à la forme négative : « je ne pense pas "
                      "que la table SOIT nécessaire ». Dès que la certitude tombe, le "
                      "subjonctif arrive.",
            notes="Diapositive à photographier. Écrire au tableau les six irréguliers "
                  "à savoir par coeur : que je sois, que j'aie, que je fasse, que "
                  "j'aille, que je puisse, que je sache. Six verbes couvrent presque "
                  "tous les subjonctifs d'une lettre.")

    d.pratique('Pratique', "Subjonctif ou conditionnel ?",
               "Mettez le verbe à la forme qui convient.", [
        ("Je souhaite que vous nous ... (faire) parvenir votre soumission.", "fassiez"),
        ("Il faut que la soumission ... (être) valide jusqu'en novembre.", "soit"),
        ("Nous ... (vouloir) connaître le prix d'une table élévatrice.", "voudrions"),
        ("... (pouvoir)-vous nous indiquer votre délai de livraison ?", "Pourriez"),
        ("Selon un premier appel, l'appareil ... (coûter) entre quatre et sept mille dollars.", "coûterait"),
        ("Si l'essai était concluant, nous ... (installer) la table en novembre.", "installerions"),
    ], corrige=True,
       notes="Les deux exercices `t3subj` et `t3cond` du module, mêlés. C'est voulu : "
             "dans une vraie lettre, les deux modes se croisent phrase après phrase. "
             "Faire justifier chaque choix.")

    d.piege('Écriture',
            "« Je demanderai votre meilleur prix. »",
            "« Je demanderais votre meilleur prix. »",
            "À l'oral, la différence s'entend à peine. À l'écrit, le -s change tout : "
            "l'un annonce ce que vous ferez, l'autre demande poliment. C'est la faute "
            "la plus fréquente dans les lettres d'affaires. Relisez tous vos verbes en "
            "-rai et en -rais avant d'envoyer. Et jamais de conditionnel juste après "
            "« si » : « si j'étais », pas « si je serais ».",
            notes="Faire relire deux lettres d'élèves à voix haute en insistant sur le "
                  "-s final. C'est la seule façon de rendre la différence audible.")

    d.billet(
        "Écrivez le premier paragraphe de votre lettre au fournisseur.",
        exemples=[
            "« Nous vous écrivons afin de... »",
            "Dites où vous en êtes : le projet est à l'étude.",
            "N'écrivez pas « nous voulons acheter ».",
        ],
        notes="Ramasser. C'est la variante de la production écrite de E2, offerte à "
              "ceux qui vont plus vite. La note de service reste la production "
              "attendue de tous.")

    return d.save(dossier)
