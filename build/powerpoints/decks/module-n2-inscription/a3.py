# -*- coding: utf-8 -*-
"""A3 · Quel est votre nom ?
Bloc A « Je découvre » · couleur teal · 75 min. Séance d'écoute et de réponse.
Source : exercices `prQuel` et `prImg`, mini-leçon `prQuel`.

Une inscription, c'est six questions courtes, toujours les mêmes, et elles
reviennent ensuite à la clinique, à la banque, à la bibliothèque. La séance
installe leur reconnaissance avant leur grammaire : l'élève doit pouvoir
répondre à « votre adresse ? » sans avoir à décider si le mot est masculin.

Le point de langue du programme est la phrase interrogative partielle sans
inversion. Il vient après, et il tient en deux lignes : quel devant un mot
masculin, quelle devant un mot féminin, et les deux se disent pareil.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-inscription/images/')


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre="Quel est votre nom ?",
        chapeau="Reconnaitre les six questions du comptoir et y répondre en "
                "trois mots.",
        duree='75 minutes')

    d.titre(notes="Séance d'écoute. Poser les six questions au groupe avant d'ouvrir la "
                  "moindre diapositive, et voir lesquelles sont déjà comprises. C'est "
                  "souvent plus que ce qu'on croit.")

    d.objectifs([
        "reconnaitre les six questions de l'inscription ;",
        "répondre en trois ou quatre mots ;",
        "employer quel devant un mot masculin, quelle devant un féminin ;",
        "demander de répéter au lieu de rester muet.",
    ])

    d.declencheur(
        'Écoute', "Qu'est-ce qu'on vous demande à un comptoir ?",
        pistes=[
            "Quelle est la première question, toujours ?",
            "Combien de questions en tout ?",
            "Qu'est-ce qui est difficile à comprendre ?",
            "Qu'est-ce qu'on répond quand on n'a pas compris ?",
        ],
        notes="Noter au tableau ce que le groupe donne. La liste ressemble presque "
              "toujours aux six questions du module : le savoir est là, il manque les "
              "mots.")

    d.tableau('Analyse', "Six questions, six réponses courtes",
              ["On vous demande", "Vous répondez"],
              [["Quel est votre nom de famille ?", "Haddad."],
               ["Quel est votre prénom ?", "Yara."],
               ["Quelle est votre date de naissance ?", "Le 7 mars 1994."],
               ["Quelle est votre adresse ?", "3420, rue Papineau."]],
              cle=1,
              note="Trois ou quatre mots suffisent. Une phrase entière n'est pas plus juste.",
              notes="Diapositive à photographier. Faire jouer les quatre lignes à deux, "
                    "en changeant de rôle à mi-chemin.")

    d.regle("Quel ou quelle : la différence ne s'entend pas",
            "Les deux se disent « kèl ». Seule l'écriture change.",
            precision="On écrit <b>quel</b> devant un mot masculin — nom, prénom, "
                      "courriel, numéro — et <b>quelle</b> devant un mot féminin — "
                      "adresse, date, ville, scolarité. À l'oral, il n'y a rien à "
                      "choisir : c'est un savoir d'écriture, pas d'oreille.",
            notes="Diapositive à photographier. Le dire clairement au groupe : inutile "
                  "de tendre l'oreille, il faut connaitre le genre du mot qui suit.")

    d.cartes("Les mots du formulaire", "Masculin d'un côté, féminin de l'autre", [
        ("Masculin — quel", "le nom · le prénom · le courriel · le numéro · le cours"),
        ("Féminin — quelle", "l'adresse · la date · la ville · la scolarité · la signature"),
    ], cols=2, notes="Diapositive à photographier. Faire ajouter au tableau les mots que "
                     "le groupe apporte : la liste vaut plus quand elle est la sienne.")

    d.pratique('Pratique', "Quel ou quelle ?",
               "Complétez chaque question.", [
        ("___ est votre nom de famille ?", "quel"),
        ("___ est votre adresse ?", "quelle"),
        ("___ est votre prénom ?", "quel"),
        ("___ est votre date de naissance ?", "quelle"),
        ("___ est votre numéro de téléphone ?", "quel"),
        ("___ est votre scolarité ?", "quelle"),
    ], corrige=True, cols=2,
       notes="Six énoncés, faits à l'oral d'abord. Rappeler à chaque erreur que c'est "
             "le mot qui suit qui décide, jamais la personne à qui on parle.")

    d.regle("« Pouvez-vous répéter, s'il vous plaît ? »",
            "La phrase qui débloque tout le reste.",
            precision="Une question mal entendue ne se devine pas. La faire répéter "
                      "prend deux secondes ; la personne au comptoir répète toute la "
                      "journée. Rester muet, au contraire, arrête la démarche.",
            notes="Diapositive à photographier. Faire dire la phrase par chaque élève. "
                  "C'est un énoncé à mémoriser du programme, et il vaut pour toutes les "
                  "situations du niveau.")

    d.pratique('Pratique · au comptoir', "Six questions, deux par deux",
               "Vingt minutes. On échange les rôles à mi-chemin.", [
        ("Étape 1", "A pose les six questions dans l'ordre."),
        ("Étape 2", "B répond en trois ou quatre mots, sans phrase complète."),
        ("Étape 3", "A pose une question trop vite. B fait répéter."),
        ("Étape 4", "On échange les rôles et on recommence."),
    ], cols=1,
       notes="L'étape 3 se prépare : demander à A d'aller vraiment vite une fois. C'est "
             "le seul moyen de faire employer « pouvez-vous répéter » pour de bon.")

    d.billet(
        "Écrivez les six questions de l'inscription, et votre réponse à chacune.",
        exemples=[
            "Quel est votre nom de famille ? — …",
            "Quelle est votre adresse ? — …",
            "Quelle est votre date de naissance ? — …",
        ],
        notes="Devoir court. Ceux qui le font arrivent au défi 2 avec leurs réponses "
              "déjà prêtes, ce qui change complètement la séance C1.")

    return d.save(dossier)
