# -*- coding: utf-8 -*-
"""E2 · La demande de révision, et le bilan
Bloc E « Je me lance » · couleur framboise · 75 min.
Source : exercices `t3rev` (type `texte`) et `t3emph`, production écrite du
bloc `custom`.

La tâche écrite vient des **attentes de fin de cours** du niveau 8, la
situation « Problèmes reliés à l'habitation » ne portant aucune intention de
production écrite : « il rédige des lettres ou des courriels d'affaires ayant
des objectifs particuliers » et « il résume les propos de son interlocuteur ».
C'est écrit ici pour qu'on ne la prenne pas pour une invention.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="La lettre qui demande qu'on recommence",
        chapeau="Ce n'est ni une plainte ni une lettre de colère. C'est une "
                "demande adressée à une entreprise pour qu'elle réexamine "
                "une décision, avec des raisons qu'elle n'avait pas.",
        duree='75 minutes')

    d.titre(notes="Dernière séance. Elle se coupe en deux : la lettre d'abord, une "
                  "heure ; le bilan du module ensuite, un quart d'heure. Rappeler que "
                  "les trois quarts de la lettre sont déjà écrits — billets de C3, "
                  "C4 et D2.")

    d.objectifs([
        "rappeler un dossier en une ligne, avec ses trois dates ;",
        "citer le motif dans les mots de l'assureur, puis le retourner ;",
        "mettre en avant l'essentiel : ce que je conteste, c'est… ;",
        "faire le bilan de ce qu'on sait faire à la fin du module.",
    ], notes="Le troisième objectif est le seul point de langue neuf de la séance. Le "
             "reste est un assemblage de ce qui a été écrit dans les blocs C et D.")

    d.declencheur(
        'Lecture', "Voici la lettre modèle. Que fait chaque paragraphe ?",
        pistes=[
            "Lequel rattache la lettre au bon dossier ?",
            "Lequel cite l'assureur, entre guillemets ?",
            "Lequel concède quelque chose ?",
            "Lequel demande, et combien de demandes contient-il ?",
        ],
        notes="C'est l'exercice `t3rev` du module, le troisième de type `texte`. Il ne "
              "sert pas à comprendre un document administratif de plus : il fait "
              "lire, découpé par fonctions, le modèle du texte qu'on va écrire "
              "vingt minutes plus tard.")

    # Six rangées à libellés longs dépassaient le garde-fou du gabarit. La
    # colonne de gauche porte donc le travail du paragraphe en un mot, et le
    # modèle de phrase passe à droite : le retournement raccourcit la colonne
    # courte et se lit mieux de la dernière rangée.
    d.tableau('Plan', "Ce que fait chaque paragraphe",
              ['Son travail', 'Le modèle'],
              [["Rattacher", "Objet : demande de révision — dossier, sinistre, décision"],
               ["Annoncer", "Je vous adresse une demande de révision de la décision du…"],
               ["Citer, puis retourner", "Votre lettre motive le refus ainsi : « … ». Or…"],
               ["Concéder", "Certes… ; il n'en reste pas moins que…"],
               ["Opposer", "Le drain a été nettoyé le 3 mai ; la facture est jointe."],
               ["Demander", "Je demande que… que… et que…"]],
              cle=0,
              notes="Diapositive à photographier, et plan de rédaction. Faire recopier "
                    "la colonne de gauche : c'est le squelette de la lettre, en six "
                    "mots.")

    d.regle("Le motif se cite, il ne se reformule pas",
            "Entre guillemets, précédés de deux points, dans les mots exacts "
            "de l'assureur. On ne conteste pas une décision qu'on aurait "
            "réécrite à sa façon.",
            precision="Le mot « Or » qui ouvre la phrase suivante est le pivot de "
                      "toute la lettre : il annonce que ce qui vient contredit ce "
                      "qu'on vient de citer. Un seul mot, et le lecteur sait où il "
                      "va.",
            notes="Diapositive à photographier. C'est aussi un savoir de ponctuation "
                  "du niveau : les deux points devant les guillemets d'un discours "
                  "direct.")

    d.cartes('Mise en relief', "Une seule phrase sera relue : choisissez laquelle", [
        ("Ce qui / ce que / ce dont…, c'est",
         "« Ce que je conteste, c'est le motif, non le montant. » Le choix "
         "entre les trois dépend du verbe : étonner quelque chose, demander "
         "quelque chose, disposer DE quelque chose."),
        ("C'est… qui / c'est… que",
         "« C'est le drain de fondation que le rapport décrit. » « Qui » si "
         "l'élément mis en avant est le sujet, « que » s'il est complément. "
         "Cette forme corrige sans contredire."),
        ("Le futur antérieur après « quand »",
         "« Quand vous aurez reçu ma lettre, le délai commencera à courir. » "
         "Deux futurs de suite ne diraient pas cet ordre-là. Très utile dans "
         "la dernière phrase."),
    ], cols=1,
       notes="Trois formes, et une seule est vraiment neuve pour le groupe : le futur "
             "antérieur. Les deux premières se retrouvent déjà dans les dialogues.")

    d.pratique('Grammaire', "Mettez en avant, et fixez l'ordre",
               "Complétez.", [
        ("___ que je conteste, c'est le motif, non le montant.", "Ce"),
        ("Ce ___ m'étonne, c'est qu'aucune caméra n'ait été passée.", "qui"),
        ("Ce ___ je dispose, c'est d'une facture acquittée.", "dont"),
        ("C'est le drain de fondation ___ le rapport décrit.", "que"),
        ("C'est Plomberie Chartier ___ est intervenue le 3 mai.", "qui"),
        ("Quand vous ___ (recevoir) ma lettre, le délai commencera à courir.", "aurez reçu"),
    ], corrige=True,
       notes="Le troisième est le piège : « avoir besoin de », « disposer de » "
             "appellent « ce dont », et la faute est très fréquente y compris chez "
             "les locuteurs natifs.")

    d.piege(
        'Lettre',
        "Menacer de poursuites dès la première lettre",
        "Rappeler le délai de soixante jours",
        "Une menace prématurée fait passer le dossier au service juridique, "
        "où il ralentit. Le délai, lui, oblige sans braquer : il dit à votre "
        "lecteur que la lettre sera relue à cette date-là, et il est écrit "
        "dans le règlement, pas dans votre colère.",
        notes="Deuxième piège à nommer si le temps le permet : raconter toute "
              "l'histoire depuis le début. Le lecteur a le dossier sous les yeux ; ce "
              "qu'il n'a pas, c'est ce que vous apportez de neuf.")

    d.regle("Douze à seize phrases, et rien de plus",
            "Trois dates, une phrase qui dit ce que la lettre est, le motif "
            "cité puis retourné, une concession, deux faits avec leurs "
            "pièces, une hypothèse irréelle, trois demandes, un numéro de "
            "téléphone.",
            precision="N'écrivez aucun fait qu'une pièce jointe ne puisse confirmer. "
                      "Et tenez le vouvoiement et le registre soutenu du début à la "
                      "fin : on ne commence pas par « Madame, Monsieur » pour finir "
                      "par « à bientôt ».",
            notes="Diapositive à photographier. C'est la consigne de rédaction "
                  "complète ; elle est aussi dans le module, en cases à cocher.")

    d.billet(
        "Qu'est-ce que vous savez faire ce matin que vous ne saviez pas faire il y a quatre semaines ?",
        exemples=[
            "Une phrase, pas une liste.",
            "Commencez par « Maintenant, je sais… ».",
        ],
        notes="Faire lire quelques réponses à voix haute avant de fermer le module. "
              "L'autoévaluation en dix-huit énoncés se fait ensuite dans « Je retiens "
              "des mots », chacun à son rythme.")

    return d.save(dossier)
