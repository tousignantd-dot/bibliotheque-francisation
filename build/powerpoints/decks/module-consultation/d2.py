# -*- coding: utf-8 -*-
"""D2 · Le pluriel, devoir et il faut.
Bloc D · couleur ambre (écriture) · 75 min.
Source : exercices `t3plur` et `t3devoir`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre='Le pluriel, devoir et il faut',
        chapeau="Deux savoirs d'écriture pour finir le défi 3 : mettre au pluriel sans "
                "se tromper, et dire une obligation autrement qu'en donnant un ordre.",
        duree='75 minutes')

    d.titre(notes="Séance double. Prévoir une pause nette au milieu : la première moitié "
                  "est de l'orthographe, la seconde de la grammaire de l'oral.")

    d.objectifs([
        "former le pluriel des noms et des adjectifs réguliers ;",
        "connaître les pluriels en -aux et en -x ;",
        "employer devoir + infinitif pour dire une obligation ;",
        "employer il faut + infinitif quand l'obligation vaut pour tous.",
    ])

    # ── première partie · le pluriel ────────────────────────────────
    d.regle('Le pluriel · la règle générale',
            "On ajoute un s au nom et à l'adjectif qui l'accompagne.",
            precision="Un tendon irrité devient des tendons irrités. Le s se met sur les "
                      "deux : le nom et l'adjectif s'accordent ensemble. C'est le cas de "
                      "la grande majorité des mots français.",
            notes="Écrire la transformation au tableau en soulignant les deux s ajoutés. "
                  "L'oubli de l'accord de l'adjectif est plus fréquent que celui du nom.")

    d.tableau('Analyse', "Trois cas particuliers à connaître",
              ['La finale', 'Ce qui se passe', 'Exemple'],
              [["-al", "devient -aux", "un mal général, des maux généraux"],
               ["-eau, -eu", "prend un x", "un nouveau bureau, des nouveaux bureaux"],
               ["-s, -x, -z", "ne change pas", "un bras droit, des bras droits"]],
              cle=0,
              note="La troisième ligne piège : le nom ne change pas, mais l'adjectif "
                   "prend son s quand même.",
              notes="Faire chercher d'autres mots en -al du domaine de la santé : un "
                    "hôpital, un signal, un journal. Tous font -aux.")

    d.pratique('Pratique · 1 de 4', 'Mettez au pluriel',
               "Le nom et l'adjectif changent ensemble.", [
        ("un genou enflé", "des genoux enflés"),
        ("un mal général", "des maux généraux"),
        ("un nouveau patient", "des nouveaux patients"),
        ("un bras droit", "des bras droits"),
        ("un tendon irrité", "des tendons irrités"),
        ("un os cassé", "des os cassés"),
    ], corrige=True, cols=2,
       notes="« Genou » fait « genoux » : c'est une exception de la liste des sept noms "
             "en -ou qui prennent un x. Ne pas donner la liste complète, seulement "
             "celui-là, qui est du module.")

    d.piege('Le piège du bras',
            "des bras droit",
            "des bras droits",
            "Le nom « bras » ne change pas au pluriel, parce qu'il finit déjà par un s. "
            "Mais l'adjectif, lui, doit s'accorder : « droits » avec un s. Le nom "
            "invariable ne rend pas l'adjectif invariable.",
            notes="Erreur très fréquente et très visible à l'écrit. Faire écrire trois "
                  "exemples au tableau : des bras droits, des os cassés, des nez rouges.")

    # ── seconde partie · l'obligation ───────────────────────────────
    d.regle("L'obligation · deux façons",
            "Devoir + infinitif désigne quelqu'un. Il faut + infinitif ne désigne personne.",
            precision="« Vous devez revenir dans une semaine » s'adresse à vous. « Il "
                      "faut plier les genoux pour soulever » vaut pour tout le monde. "
                      "Choisir l'un ou l'autre change le ton complètement.",
            notes="Diapo charnière de la séance. La laisser affichée pendant les deux "
                  "exercices qui suivent.")

    d.tableau('Analyse', "Devoir au présent",
              ['La personne', 'La forme', 'Un exemple'],
              [["je", "je dois", "Je dois me reposer."],
               ["tu", "tu dois", "Tu dois éviter de forcer."],
               ["il, elle", "il doit", "Yannick doit se reposer."],
               ["nous", "nous devons", "Nous devons attendre."],
               ["vous", "vous devez", "Vous devez revenir."]],
              cle=1,
              notes="La forme « ils doivent » complète le tableau ; la donner à l'oral. "
                    "Elle est peu utile en consultation, où l'on parle de soi ou à vous.")

    d.cartes('Ouvrir la mini-leçon', "Quatre nuances de l'obligation", [
        ("« Il faut » est plus doux",
         "Dire « il faut mettre de la glace » est moins direct que « vous devez mettre "
         "de la glace ». Le personnel de santé emploie souvent la première forme."),
        ("Toujours un infinitif après",
         "Devoir et il faut sont suivis d'un verbe à l'infinitif, jamais d'un verbe "
         "conjugué : il faut plier, jamais il faut vous pliez."),
        ("« Il ne faut pas » est une interdiction",
         "« Il ne faut pas forcer » est plus fort que « vous ne devez pas forcer ». "
         "C'est la forme des consignes de sécurité."),
        ("« Devoir » sert aussi au futur proche",
         "« Je dois revenir dans une semaine » n'est pas seulement une obligation, "
         "c'est aussi un rendez-vous prévu."),
    ], notes="La deuxième carte est la règle de forme la plus utile. Les deux autres "
             "sont des nuances de ton : les traiter plus vite.")

    d.pratique('Pratique · 2 de 4', 'Complétez avec devoir ou il faut',
               "Attention à la personne du verbe devoir.", [
        ("Yannick ___ se reposer quatre jours.", "doit"),
        ("Vous ___ appliquer de la glace trois fois par jour.", "devez"),
        ("___ plier les genoux pour soulever une boîte.", "Il faut"),
        ("Je ___ prendre un rendez-vous en physiothérapie.", "dois"),
        ("___ éviter de forcer pendant une semaine.", "Il faut"),
        ("Nous ___ arriver tôt à la clinique.", "devons"),
    ], corrige=True,
       notes="Faire justifier les choix de « il faut » : est-ce que la consigne vise "
             "quelqu'un en particulier ? Non, donc « il faut ».")

    d.piege("Le piège de l'infinitif",
            "Il faut vous pliez les genoux.",
            "Il faut plier les genoux.",
            "Après « il faut » et après « devoir », le verbe reste à l'infinitif : "
            "plier, éviter, revenir, prendre. Il ne se conjugue pas et ne prend pas de "
            "sujet. C'est une erreur qui vient de la traduction directe.",
            notes="Faire relire les six réponses de l'exercice précédent en vérifiant "
                  "que le verbe qui suit est bien à l'infinitif.")

    d.pratique('Pratique · 3 de 4', "Transformez la consigne",
               "Passez de « il faut » à « devoir », ou l'inverse.", [
        ("Il faut mettre de la glace trois fois par jour.",
         "Vous devez mettre de la glace trois fois par jour."),
        ("Vous devez revenir dans une semaine.",
         "Il faut revenir dans une semaine."),
        ("Il ne faut pas soulever de charges.",
         "Vous ne devez pas soulever de charges."),
        ("Je dois finir tout le traitement.",
         "Il faut finir tout le traitement."),
    ], corrige=True,
       notes="Faire remarquer que le ton change à chaque transformation. Demander laquelle "
             "des deux formes on préférerait entendre de son médecin.")

    d.pratique('Pratique · 4 de 4', "Écrivez les consignes de la docteure",
               "Quatre consignes, données à Yannick. Variez les deux formes.", [
        ("Repos, quatre jours", "Vous devez vous reposer quatre jours."),
        ("Glace, vingt minutes, trois fois", "Il faut mettre de la glace vingt minutes, trois fois par jour."),
        ("Ne pas soulever de charges", "Il ne faut pas soulever de charges."),
        ("Rendez-vous en physiothérapie", "Vous devez prendre un rendez-vous en physiothérapie."),
    ], corrige=True,
       notes="C'est la synthèse du défi 3 : le contenu vient de C1, la forme vient "
             "d'ici. Faire remarquer au groupe qu'il réécrit la consultation entière.")

    d.billet(
        "Écrivez trois consignes de santé, au pluriel quand c'est possible.",
        exemples=[
            "Une avec « vous devez », une avec « il faut », une avec « il ne faut pas ».",
            "Exemple : « Il faut protéger vos genoux quand vous soulevez des charges. »",
        ],
        notes="Corriger l'infinitif et l'accord du pluriel — les deux savoirs de la "
              "séance. Rendre avant E1.")

    return d.save(dossier)
