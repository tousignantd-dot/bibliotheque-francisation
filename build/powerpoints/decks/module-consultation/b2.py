# -*- coding: utf-8 -*-
"""B2 · Dire pourquoi : parce que, à cause de, car.
Bloc B · couleur ambre (écriture) · 75 min.
Source : exercice `t1cause` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre='Dire pourquoi',
        chapeau="« Je consulte parce que mon genou est enflé » ou « à cause de mon "
                "genou enflé » ? Les deux existent, et le choix ne dépend pas du sens. "
                "Il dépend de ce qui suit.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire écrite. Écrire les deux phrases du chapeau au "
                  "tableau et demander laquelle est correcte. Réponse : les deux — c'est "
                  "le point de départ, pas la fin.")

    d.objectifs([
        "choisir entre parce que, à cause de et car selon ce qui suit ;",
        "reconnaître une phrase complète et un simple groupe du nom ;",
        "expliquer pourquoi on consulte, en une phrase juste ;",
        "savoir lequel des trois s'écrit et lequel se dit.",
    ])

    d.regle('La règle',
            "Ce qui suit décide : une phrase complète, ou un simple nom.",
            precision="Parce que et car sont suivis d'un sujet et d'un verbe conjugué. "
                      "À cause de est suivi d'un nom, jamais d'un verbe conjugué. Le "
                      "sens des trois est le même ; la construction ne l'est pas.",
            notes="Écrire la règle au tableau et l'y laisser toute la séance. Les élèves "
                  "y reviendront à chaque exercice.")

    d.tableau('Analyse', "parce que + une phrase complète",
              ['Ce qu\'on a', 'Le mot', 'Pourquoi'],
              [["Le résultat", "Je consulte", "ce qui arrive"],
               ["Le mot de cause", "parce que", "il annonce une phrase"],
               ["Une phrase complète", "mon genou est enflé", "sujet + verbe conjugué"]],
              cle=1,
              note="La phrase entière : « Je consulte parce que mon genou est enflé. » "
                   "« Parce que » répond directement à la question « pourquoi ? ».",
              notes="Faire souligner le sujet et le verbe de la troisième ligne. C'est ce "
                    "repérage, et lui seul, qui décide du mot de cause.")

    d.tableau('Analyse', "à cause de + un nom",
              ['Ce qu\'on a', 'Le mot', 'Pourquoi'],
              [["Le résultat", "Je boite", "ce qui arrive"],
               ["Le mot de cause", "à cause de", "il annonce un nom"],
               ["Un nom, pas une phrase", "la douleur", "aucun verbe conjugué"]],
              cle=1,
              note="La phrase entière : « Je boite à cause de la douleur. » Comparez les "
                   "deux tableaux : seule la troisième ligne change.",
              notes="Mettre les deux tableaux côte à côte au tableau noir. La différence "
                    "tient à un seul mot : « est ».")

    d.regle('Le test qui tranche',
            "Cherchez un verbe conjugué. S'il y en a un, c'est parce que. S'il n'y en a pas, c'est à cause de.",
            precision="« mon genou est enflé » contient « est » : parce que. « mon genou "
                      "enflé » n'en contient pas : à cause de. Le test fonctionne dans "
                      "tous les cas, sans exception.",
            notes="Faire pratiquer ce test à voix haute sur cinq exemples inventés par le "
                  "groupe avant de passer à l'écrit.")

    d.cartes('En apprendre plus', "Ce qui n'est pas dans la règle", [
        ("« car » s'écrit, ne se dit pas",
         "Car fonctionne comme parce que — une phrase complète le suit — mais il "
         "appartient à l'écrit. Ne jamais commencer une réponse orale par « car »."),
        ("Jamais en début de phrase",
         "« Parce que j'ai mal, je consulte » est lourd et rare. En français courant, la "
         "cause vient après le résultat, pas avant."),
        ("À cause de : la forme change",
         "Devant le, à cause de devient « à cause du » ; devant les, « à cause des ». "
         "À cause du travail, à cause des boîtes."),
        ("Grâce à, pour une bonne cause",
         "« À cause de » sous-entend souvent un problème. Quand la cause est heureuse, "
         "on dit « grâce à » : grâce à la physiothérapie, je marche mieux."),
    ], notes="La quatrième carte est celle que les élèves aiment le plus. Faire produire "
             "une phrase avec « grâce à » sur le module.")

    d.pratique('Pratique · 1 de 3', "Parce que ou à cause de ?",
               "Utilisez le test : y a-t-il un verbe conjugué après ?", [
        ("Je vais à la clinique ___ j'ai mal au genou.", "parce que — « j'ai » est un verbe"),
        ("Il ne peut pas courir ___ son inflammation.", "à cause de — un nom seul"),
        ("La salle est pleine ___ beaucoup de gens sont malades.", "parce que — « sont »"),
        ("Elle porte une attelle ___ sa blessure au poignet.", "à cause de — un nom seul"),
        ("Il ne travaille pas, ___ il doit se reposer.", "car — à l'écrit, ou parce que"),
        ("Je boite ___ la douleur au genou.", "à cause de — un nom seul"),
    ], corrige=True,
       notes="Corriger en faisant nommer le verbe conjugué chaque fois qu'il y en a un. "
             "Ne jamais corriger par « ça se dit comme ça ».")

    d.piege('Le piège le plus fréquent',
            "Je boite à cause de j'ai mal.",
            "Je boite parce que j'ai mal.",
            "« J'ai mal » est une phrase : un sujet, un verbe conjugué. « À cause de » ne "
            "peut pas l'introduire. C'est l'erreur la plus courante du module, et elle "
            "vient de ce qu'on traduit le sens sans regarder la construction.",
            notes="Écrire l'erreur au tableau, faire trouver le verbe, puis corriger avec "
                  "le groupe. Cette diapo mérite dix minutes à elle seule.")

    d.piege("Le piège dans l'autre sens",
            "Je consulte parce que mon genou enflé.",
            "Je consulte à cause de mon genou enflé.",
            "« Mon genou enflé » n'a pas de verbe conjugué : ce n'est pas une phrase, "
            "c'est un groupe du nom. Il lui faut « à cause de ». Le même contenu peut "
            "s'écrire des deux façons — il suffit d'ajouter ou d'enlever le verbe.",
            notes="Faire transformer chaque phrase de l'exercice précédent dans l'autre "
                  "construction. C'est l'exercice qui installe vraiment la règle.")

    d.pratique('Pratique · 2 de 3', 'Transformez la phrase',
               "Passez de « parce que » à « à cause de », ou l'inverse.", [
        ("Je consulte parce que mon genou est enflé.",
         "Je consulte à cause de mon genou enflé."),
        ("Il est fatigué à cause de son travail de nuit.",
         "Il est fatigué parce qu'il travaille de nuit."),
        ("Elle ne marche pas parce que sa cheville est blessée.",
         "Elle ne marche pas à cause de sa cheville blessée."),
        ("L'attente est longue à cause du nombre de patients.",
         "L'attente est longue parce qu'il y a beaucoup de patients."),
    ], corrige=True,
       notes="Exercice difficile : il demande de créer ou de supprimer un verbe. Laisser "
             "cinq minutes et circuler.")

    d.pratique('Pratique · 3 de 3', 'Expliquez votre consultation',
               "Écrivez pourquoi vous consultez. Une phrase, un mot de cause.", [
        ("Vous avez le dos bloqué depuis trois jours.",
         "Je consulte parce que mon dos est bloqué depuis trois jours."),
        ("Votre enfant a de la fièvre.",
         "Je viens à cause de la fièvre de mon enfant."),
        ("Vous ne dormez plus depuis une semaine.",
         "Je consulte parce que je ne dors plus depuis une semaine."),
        ("Une douleur au poignet vous empêche de travailler.",
         "Je ne travaille pas, car j'ai une douleur au poignet."),
    ], corrige=True,
       notes="Accepter toute phrase correcte, même avec un autre mot de cause que celui "
             "du corrigé — pourvu que la construction suive ce qui vient après.")

    d.billet(
        "Écrivez deux phrases : une avec « parce que », une avec « à cause de ».",
        exemples=[
            "Les deux doivent parler de santé ou de consultation.",
            "Soulignez le verbe conjugué dans la première, et le nom dans la seconde.",
        ],
        notes="Corriger les billets en dehors du cours et rendre à la séance suivante : "
              "cette notion demande une rétroaction individuelle.")

    return d.save(dossier)
