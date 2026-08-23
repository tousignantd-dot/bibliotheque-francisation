# -*- coding: utf-8 -*-
"""E2 · La lettre au courrier des lecteurs, et le bilan
Bloc E « Je me lance » · couleur framboise · 75 min.
Source : exercice `t3lettre` (type `texte`, le modèle découpé par fonctions),
sa mini-leçon, et la production écrite du bloc `custom`.
La tâche porte les deux intentions de production écrite de la situation au
niveau 8 : rédiger une lettre pour le courrier des lecteurs, et résumer un
texte d'opinion. Elles ne se séparent pas - le premier paragraphe résume
l'éditorial auquel la lettre répond.
Dossier inventé : Rivière-aux-Cèdres, l'hebdomadaire Le Courant de la Rive.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Résumer ce qu'on conteste, puis répondre",
        chapeau="Une lettre qui ne résume pas ce qu'elle conteste n'a aucune "
                "prise, et un résumé sans réponse n'est pas une lettre. Les "
                "deux exigences du programme tiennent dans le même texte.",
        duree='75 minutes')

    d.titre(notes="Dernière séance. Elle se coupe en deux : la lettre pendant une "
                  "heure, le bilan du module ensuite, un quart d'heure. Annoncer le "
                  "découpage au début, sinon le bilan se fait à la sauvette.")

    d.objectifs([
        "résumer un texte d'opinion en trois phrases que son auteur signerait ;",
        "rattacher une lettre à un texte daté, dès la première phrase ;",
        "concéder ce que sa position coûte, puis y répondre ;",
        "terminer par une demande précise, adressée à quelqu'un qui peut agir.",
    ], notes="Le premier objectif est une intention du programme à lui seul. Le dire : "
             "le résumé n'est pas une politesse d'introduction, c'est la moitié de la "
             "tâche évaluée.")

    d.declencheur(
        'Discussion', "Avez-vous déjà eu envie d'écrire à un journal ?",
        pistes=[
            "Qu'est-ce qui vous en a empêché : la langue, le temps, l'utilité ?",
            "Lisez-vous le courrier des lecteurs ? Qu'est-ce qui vous y retient ?",
            "Qu'est-ce qui distingue une lettre publiée d'un commentaire en ligne ?",
            "À qui écrit-on, au juste, quand on écrit à un journal ?",
        ],
        notes="La dernière question ouvre la séance : on écrit à la rédaction, sur "
              "une question publique, jamais à une personne. Presque tout le monde "
              "répond « à l'auteur de l'article », et c'est l'erreur à corriger.")

    d.regle("Résumer avant de répondre",
            "Trois phrases pour dire ce que l'autre a soutenu, dans ses "
            "termes à lui, sans le caricaturer. Le test : l'auteur "
            "signerait-il votre résumé ?",
            precision="Reprenez ses deux meilleurs arguments, pas ses deux plus "
                      "faibles. Résumer en affaiblissant s'appelle un homme de "
                      "paille : on démolit une version faible de l'adversaire, le "
                      "lecteur informé le repère, et toute la suite de la lettre est "
                      "perdue.",
            notes="Diapositive à photographier. C'est la règle la plus importante de "
                  "la séance, et celle qu'on enfreint le plus - la tentation d'un "
                  "résumé arrangeant est très forte quand on est en désaccord.")

    d.tableau('Analyse', "Les six parties d'une lettre au courrier des lecteurs",
              ['La partie', 'Ce qu\'elle contient'],
              [["Le rattachement",
                "le titre du texte, sa date, son auteur - première phrase, toujours"],
               ["Le résumé",
                "la thèse adverse et ses deux meilleurs arguments, en trois phrases"],
               ["La position",
                "une phrase, la vôtre, même si elle surprend"],
               ["Les arguments",
                "deux, dont un chiffré et un tiré de votre expérience"],
               ["La concession et la réfutation",
                "ce que votre position coûte, et pourquoi elle tient quand même"],
               ["La demande et la signature",
                "deux demandes au plus, avec une date - nom et ville"]],
              cle=0,
              notes="Diapositive à photographier. C'est le plan de l'exercice 7 du "
                    "module, où l'élève clique dans la lettre de Mirela pour "
                    "retrouver chaque fonction. Ici, on nomme la fonction avant "
                    "d'écrire : c'est le même travail à l'envers.")

    d.pratique('Pratique 1 de 2', "Quelle fonction remplit ce passage ?",
               "Lisez le passage et nommez la partie.", [
        ("En réaction à l'éditorial « Un terrain qui ne rapportait rien », paru le 14 octobre.", "le rattachement, daté"),
        ("Votre éditorialiste soutient que la cession était nécessaire et urgente.", "le résumé de la thèse adverse"),
        ("Je partage sa conclusion et je signerai malgré tout le registre.", "la position, en une phrase"),
        ("Trois de mes collègues ont quitté la ville faute de logement.", "l'argument vécu"),
        ("Il est vrai qu'un report mettrait le financement en péril.", "la concession"),
        ("Je demande à la Ville de publier l'évaluation avant l'ouverture du registre.", "la demande précise"),
    ], corrige=True,
       notes="Reprend l'exercice de texte du module. Faire remarquer que la "
             "concession vient de l'auteure elle-même, sans qu'on la lui demande : "
             "c'est ce qui la rend difficile à attaquer.")

    d.cartes('Analyse', "Trois registres, et pourquoi il faut les séparer", [
        ("Ce que je sais",
         "Un fait vérifiable, avec sa source : le procès-verbal indique "
         "quatre voix contre trois. On peut vous le contester ; on ne peut "
         "pas vous le reprocher."),
        ("Ce qu'on m'a rapporté",
         "Dites-le comme tel : selon le comité, trois cent quarante-deux "
         "arbres ont été comptés. Vous n'en répondez pas, et cela se voit."),
        ("Ce que j'en pense",
         "Votre opinion, annoncée comme telle : à mon avis, une décision "
         "prise devant onze personnes ne tiendra pas. Personne ne peut "
         "réfuter une opinion signée."),
        ("Et la rumeur : nulle part",
         "Ne la reprenez pas, même pour la nuancer. Une seule rumeur dans "
         "une lettre rend tout le reste suspect, et la rédaction ne publie "
         "pas."),
    ], notes="Mêler les trois registres est ce qui rend une lettre attaquable en une "
             "ligne. Faire relire à chacun son brouillon avec trois crayons de "
             "couleur : c'est plus efficace que n'importe quelle explication.")

    d.pratique('Pratique 2 de 2', "Écrivez votre premier paragraphe",
               "Le rattachement, puis le résumé en trois phrases.", [
        ("Phrase 1", "en réaction à quoi, paru quand"),
        ("Phrase 2", "la thèse de l'éditorial, en ses propres termes"),
        ("Phrase 3", "son meilleur argument, celui qui tient"),
        ("Phrase 4", "ce qu'il concède déjà lui-même"),
    ], corrige=False,
       notes="Vingt minutes au brouillon, puis échange des feuilles par deux. Le "
             "voisin répond à une seule question : est-ce que l'éditorialiste "
             "signerait ce résumé ? Si non, on recommence avant d'aller plus loin.")

    d.piege('Piège', "s'adresser à une personne",
            "s'adresser à la rédaction, sur une question publique",
            "« Monsieur Chamberland devrait avoir honte » ne se publie pas ; "
            "« l'argument de M. Chamberland résiste mal sur un point » se "
            "publie. Même chose pour la longueur : de deux cent cinquante à "
            "trois cent cinquante mots. Au-delà, la rédaction coupe "
            "elle-même, et elle coupe la fin - c'est-à-dire votre demande.",
            notes="Troisième conseil, gratuit et efficace : écrire le soir, envoyer "
                  "le lendemain matin. La lettre qu'on relit une nuit plus tard est "
                  "presque toujours la meilleure.")

    d.tableau('Bilan', "Ce que vous savez faire à la fin du module",
              ['Ce qui a changé', 'Où c\'était'],
              [["Nommer les genres de l'actualité",
                "je découvre"],
               ["Voir ce que chaque version choisit de taire",
                "défi 1"],
               ["Retrouver la thèse et la concession d'un texte",
                "défi 2"],
               ["Répondre à une objection sans esquiver",
                "défi 3"],
               ["Résumer un texte d'opinion, puis y répondre",
                "je me lance"]],
              cle=0,
              notes="Diapositive de clôture, à photographier. Refaire dire à voix "
                    "haute la phrase du défi 3 : « je n'en sais rien, et ce n'est pas "
                    "mon argument ». C'est celle que le module veut laisser.")

    d.billet(
        "Écrivez votre lettre au courrier des lecteurs et déposez-la.",
        exemples=[
            "De 12 à 16 phrases, quatre paragraphes, un résumé honnête au premier.",
            "Une concession, une hypothèse irréelle, une mise en relief, une demande.",
        ],
        notes="Dépôt dans « Je me lance ». Rappeler que le bouton d'envoi "
              "n'apparaît qu'une fois la correction demandée : on ne dépose pas un "
              "texte non relu. Terminer par l'autoévaluation du module.")

    return d.save(dossier)
