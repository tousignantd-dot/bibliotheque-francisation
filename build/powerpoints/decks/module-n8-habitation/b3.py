# -*- coding: utf-8 -*-
"""B3 · Dont, auquel, sur laquelle
Bloc B « Défi 1 · Le rapport qu'on discute » · couleur teal · 75 min.
Source : exercice `t1rel` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='teal',
        titre="Suivre le fil d'une phrase longue",
        chapeau="Un contrat, un rapport, une décision : trois genres qui "
                "empilent les précisions dans une seule phrase. Le pronom "
                "relatif est ce qui permet cet empilement.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Rassurer d'entrée : ces phrases sont "
                  "fatigantes pour tout le monde, y compris pour ceux dont c'est la "
                  "langue maternelle. Le problème n'est pas le niveau de l'élève, "
                  "c'est le genre du texte.")

    d.objectifs([
        "reconnaître à quoi renvoie « dont » dans une phrase longue ;",
        "choisir entre auquel, à laquelle, duquel, sur lequel ;",
        "employer « à qui » pour une personne ;",
        "lire la différence que fait une virgule dans une relative.",
    ], notes="Le quatrième objectif est celui qu'on n'enseigne presque jamais et qui "
             "vaut de l'argent dans un contrat.")

    d.declencheur(
        'Lecture', "À quoi renvoie « dont » dans cette phrase du contrat ?",
        pistes=[
            "« … les dommages résultant du manque d'entretien d'un élément dont l'assuré a la charge. »",
            "De quoi l'assuré a-t-il la charge ?",
            "Où est le mot « de » dans cette phrase ?",
            "Pourquoi ne peut-on pas écrire « que » ici ?",
        ],
        notes="Laisser chercher. La phrase est celle de l'article 7.3 du module, et "
              "c'est elle qui fonde le refus : la comprendre n'est pas un exercice "
              "de grammaire, c'est le dossier.")

    d.regle("Le verbe commande, jamais le nom",
            "Trouvez le verbe qui suit le relatif, demandez-vous quelle "
            "préposition ce verbe exige, et vous avez la forme.",
            precision="renvoyer à, donc auquel · s'appuyer sur, donc sur lequel · avoir "
                      "la charge de, donc dont · discuter de, donc dont. L'erreur la plus "
                      "fréquente vient d'un verbe traduit de sa langue maternelle : "
                      "en français, on discute DE quelque chose.",
            notes="Diapositive à photographier. C'est la méthode entière de la séance, "
                  "et elle marche à tous les coups.")

    d.tableau('Formes', "Ce qu'il faut savoir par cœur",
              ['Préposition', 'Forme'],
              [["de", "dont"],
               ["à", "auquel · à laquelle · auxquels · auxquelles"],
               ["de (après un groupe)", "duquel · de laquelle · desquels"],
               ["sur, dans, par…", "sur lequel · dans laquelle · par lesquels"],
               ["une personne", "à qui · avec qui · pour qui"]],
              cle=0,
              notes="Diapositive à photographier. Une seule irrégularité à retenir : "
                    "« à laquelle » et « de laquelle » ne se contractent jamais.")

    d.cartes('Analyse', "Trouver le « de » caché", [
        ("Entre deux noms",
         "« Le drain, dont la grille est bouchée » = la grille DE ce drain. "
         "Le lien entre les deux noms porte le « de », et on ne le voit pas "
         "tant qu'on ne le cherche pas."),
        ("Dans le verbe",
         "« Un élément dont l'assuré a la charge » = il a la charge DE cet "
         "élément. « La clause dont nous discutons » = discuter DE la clause."),
        ("Le test en une seconde",
         "Remplacez « dont » par « de lui », « d'elle », « de cela ». Si la "
         "phrase tient, c'est bien « dont »."),
    ], cols=1,
       notes="Faire appliquer le test sur les trois exemples, à voix haute. Il est "
             "fiable et les élèves le gardent.")

    d.pratique('Grammaire', "Quel relatif ?",
               "Complétez : dont, duquel, auquel, à laquelle, sur laquelle, sur lesquelles, à qui.", [
        ("L'article 7.3, ___ la lettre de refus renvoie, porte sur le défaut d'entretien.", "auquel"),
        ("Le drain, ___ la grille présente un dépôt, se trouve au centre de la dalle.", "dont"),
        ("C'est une exclusion ___ l'assureur s'appuie pour refuser.", "sur laquelle"),
        ("Un élément ___ l'assuré a la charge doit être entretenu.", "dont"),
        ("Voici la facture, au bas ___ figure la date du 3 mai.", "de laquelle"),
        ("L'expert ___ j'ai parlé mardi est venu deux jours après l'orage.", "à qui"),
        ("Ce sont les photographies ___ nous appuyons notre contestation.", "sur lesquelles"),
        ("Le service ___ la demande est adressée n'a pas rendu la décision.", "auquel"),
    ], corrige=True,
       notes="Faire dire le verbe et sa préposition avant chaque réponse. Celui qui "
             "dit « renvoyer à » trouve « auquel » sans hésiter.")

    d.piege(
        'Relatifs',
        "l'article que la lettre renvoie",
        "l'article auquel la lettre renvoie",
        "« Renvoyer » exige la préposition « à ». Le simple « que » ne peut "
        "pas porter une préposition : il ne remplace qu'un complément "
        "direct. C'est l'erreur la plus répandue de tout le niveau, et elle "
        "vient de ce que « que » marche partout dans beaucoup de langues.",
        notes="Faire produire trois phrases justes sur ce modèle avant de passer à la "
              "suite. La règle ne se retient qu'à l'usage.")

    d.regle("Une virgule change ce qu'un contrat couvre",
            "Sans virgule, la relative distingue : « les dommages qui "
            "résultent d'un défaut d'entretien » n'exclut qu'une partie des "
            "dommages. Avec des virgules, elle ajoute : « les dommages, qui "
            "résultent d'un défaut d'entretien, » les exclurait tous.",
            precision="Dans un contrat d'assurance, cette différence-là vaut de "
                      "l'argent. Quand une virgule change ce qui est couvert, elle "
                      "se lit deux fois.",
            notes="Diapositive à photographier. Écrire les deux versions au tableau et "
                  "faire dire au groupe laquelle est dans le contrat de Teodora — "
                  "c'est la première.")

    d.billet(
        "Écrivez trois phrases sur votre logement, chacune avec un relatif différent.",
        exemples=[
            "Une avec « dont ».",
            "Une avec « auquel » ou « à laquelle ».",
            "Une avec « à qui », pour une personne.",
        ],
        notes="Corriger la préposition du verbe plutôt que la forme du relatif : "
              "c'est là qu'est l'erreur, presque toujours.")

    return d.save(dossier)
