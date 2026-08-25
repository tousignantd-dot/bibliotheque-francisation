# -*- coding: utf-8 -*-
"""B2 · Le pronom « que ».
Bloc B · couleur ambre (écriture) · 75 min.
Source : exercice `t1que` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Le pronom « que »",
        chapeau="« Il me donne des directives. J'apprécie ces directives. » Deux phrases, "
                "un mot répété. Un seul petit mot les réunit — et ce n'est pas le même "
                "qu'au module 3.",
        duree='75 minutes')

    d.titre(notes="Écrire les deux phrases du chapeau au tableau. Ceux qui ont fait le "
                  "module 3 proposeront « qui » : c'est l'occasion parfaite d'installer "
                  "la différence.")

    d.objectifs([
        "joindre deux phrases avec le pronom « que » ;",
        "retrouver le groupe de mots que « que » reprend ;",
        "distinguer « qui » et « que » par ce qui les suit ;",
        "écrire « qu' » devant une voyelle.",
    ])

    d.regle('La règle',
            "« Que » remplace un groupe du nom qui est complément du verbe.",
            precision="« Il me donne des directives que j'apprécie. » Le mot « que » "
                      "reprend « des directives » et évite de les répéter. Il est "
                      "toujours suivi d'un sujet — jamais directement d'un verbe.",
            notes="Écrire la règle au tableau. Le repère « suivi d'un sujet » est le "
                  "critère de toute la séance.")

    d.tableau('Analyse', "Comment deux phrases deviennent une",
              ['Étape', 'La phrase'],
              [["deux phrases", "Il me donne des directives. J'apprécie ces directives."],
               ["le mot répété", "des directives / ces directives"],
               ["on remplace par que", "Il me donne des directives que j'apprécie."]],
              cle=0,
              note="« Que » se place juste après le groupe qu'il reprend, comme « qui ».",
              notes="Faire la même transformation avec trois autres paires au tableau, "
                    "avec le groupe.")

    d.regle('La différence avec « qui »',
            "Après « qui », un verbe. Après « que », un sujet.",
            precision="« Le formulaire qui doit être signé » — « doit » est un verbe, "
                      "donc « qui ». « Le formulaire que vous devez remplir » — « vous » "
                      "est un sujet, donc « que ». Regardez le mot suivant, et rien "
                      "d'autre.",
            notes="Diapo la plus importante de la séance. L'écrire au tableau et l'y "
                  "laisser jusqu'à la fin.")

    d.tableau('Analyse', "Qui ou que : le mot qui suit décide",
              ['La phrase', 'Le mot qui suit', 'Donc'],
              [["le formulaire ___ doit être signé", "doit — un verbe", "qui"],
               ["le formulaire ___ vous remplissez", "vous — un sujet", "que"],
               ["la commis ___ m'a répondu", "a répondu — un verbe", "qui"],
               ["la commis ___ j'ai appelée", "j' — un sujet", "que"]],
              cle=2,
              notes="Faire appliquer le test à voix haute sur les quatre lignes. C'est "
                    "un test mécanique : il ne demande pas de comprendre pourquoi.")

    d.cartes('Ouvrir la mini-leçon', "Quatre choses à savoir en plus", [
        ("« Que » devient « qu' » devant une voyelle",
         "« La procédure qu'on lui a montrée. » « L'application qu'elle utilise. » "
         "Contrairement à « qui », qui ne s'élide jamais."),
        ("Le verbe ne s'accorde pas avec « que »",
         "« Les directives que j'apprécie » — le verbe s'accorde avec « je », pas avec "
         "« les directives ». C'est l'inverse de « qui »."),
        ("Pourquoi c'est utile au travail",
         "« Voici le reçu que je dois joindre » est plus court et plus clair que deux "
         "phrases séparées. Un courriel gagne en clarté."),
        ("Le participe s'accorde parfois",
         "« La procédure qu'on lui a montrée » — le participe prend un e. C'est une "
         "règle avancée : la reconnaître suffit à ce niveau."),
    ], notes="Ne pas développer la quatrième carte. La mentionner et passer : elle "
             "dépasse le niveau, mais les élèves la verront dans les textes.")

    d.pratique('Pratique · 1 de 4', "Que reprend « que » ?",
               "Trouvez le groupe de mots placé juste avant.", [
        ("Voici le formulaire que vous devez remplir.", "le formulaire"),
        ("Vous devez joindre le reçu que la commis vous a demandé.", "le reçu"),
        ("Nous allons utiliser l'application que Diane m'a montrée.", "l'application"),
        ("Suivez bien la procédure que votre superviseur explique.", "la procédure"),
        ("C'est un remboursement que j'attends depuis dix jours.", "un remboursement"),
        ("Je vais approuver la demande que vous avez soumise ce matin.", "la demande"),
    ], corrige=True,
       notes="Faire souligner le groupe repris dans chaque phrase. Le motif est toujours "
             "le même : juste avant « que ».")

    d.pratique('Pratique · 2 de 4', "Qui ou que ?",
               "Regardez le mot qui suit : un verbe, ou un sujet ?", [
        ("Voici le formulaire ___ doit être signé.", "qui — « doit » est un verbe"),
        ("Voici le formulaire ___ vous devez signer.", "que — « vous » est un sujet"),
        ("C'est la commis ___ m'a répondu hier.", "qui — « a répondu » est un verbe"),
        ("C'est la commis ___ j'ai appelée hier.", "que — « j' » est un sujet"),
        ("L'application ___ Diane m'a montrée est facile.", "que — « Diane » est un sujet"),
        ("L'application ___ sert aux remboursements s'appelle Ressources+.", "qui — « sert »"),
    ], corrige=True,
       notes="Faire nommer le mot qui suit à voix haute avant chaque réponse. Sans cette "
             "étape, l'exercice devient un jeu de hasard.")

    d.piege("Le piège du « qui » à la place de « que »",
            "Le formulaire qui vous devez remplir.",
            "Le formulaire que vous devez remplir.",
            "Après « qui », il faut un verbe. Ici, c'est « vous » qui suit — un sujet. "
            "Le bon pronom est donc « que ». Le test ne demande pas de comprendre la "
            "fonction grammaticale : il suffit de regarder le mot d'après.",
            notes="Erreur très fréquente chez ceux qui viennent d'apprendre « qui ». La "
                  "corriger avec le test, jamais par l'oreille.")

    d.piege("Le piège de l'élision",
            "La procédure que on lui a montrée.",
            "La procédure qu'on lui a montrée.",
            "« Que » perd son e devant une voyelle et devient « qu' ». C'est automatique, "
            "comme « ne » qui devient « n' ». Attention : « qui » ne s'élide jamais — "
            "c'est justement une façon de les distinguer à l'écrit.",
            notes="Faire chercher dans le dialogue de B1 tous les « que » et « qui ». Le "
                  "contraste est visible.")

    d.pratique('Pratique · 3 de 4', "Joignez les deux phrases",
               "Employez « qui » ou « que » selon le cas.", [
        ("Voici le reçu. Je dois joindre ce reçu.",
         "Voici le reçu que je dois joindre."),
        ("C'est l'application. Cette application sert aux remboursements.",
         "C'est l'application qui sert aux remboursements."),
        ("Suivez la procédure. Votre superviseur explique cette procédure.",
         "Suivez la procédure que votre superviseur explique."),
        ("J'attends le remboursement. Ce remboursement devait arriver lundi.",
         "J'attends le remboursement qui devait arriver lundi."),
    ], corrige=True,
       notes="Faire souligner le mot répété avant de transformer. C'est l'étape que les "
             "élèves sautent, et c'est celle qui fait tout le travail.")

    d.pratique('Pratique · 4 de 4', "Écrivez trois phrases",
               "Une avec « qui », une avec « que », une avec « qu' ».", [
        ("Avec qui", "C'est la commis qui traite les demandes."),
        ("Avec que", "Voici le formulaire que je dois remplir."),
        ("Avec qu'", "C'est la procédure qu'on m'a expliquée."),
    ], corrige=True,
       notes="Corriger deux choses seulement : le choix du pronom, et l'élision. Le reste "
             "viendra plus tard.")

    d.billet(
        "Écrivez deux phrases : une avec « qui », une avec « que ».",
        exemples=[
            "Les deux doivent parler d'un formulaire, d'un reçu ou d'une procédure.",
            "Soulignez le mot qui suit le pronom : un verbe, ou un sujet ?",
        ],
        notes="Corriger les billets en dehors du cours. Le mot souligné montre si le test "
              "est acquis, même quand le choix est faux.")

    return d.save(dossier)
