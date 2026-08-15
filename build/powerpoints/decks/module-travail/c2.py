# -*- coding: utf-8 -*-
"""C2 · Et, ou, mais.
Bloc C · couleur ambre (écriture) · 60 min.
Source : exercice `t2connect` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Et, ou, mais',
        chapeau="Trois petits mots qui relient deux phrases. Le premier ajoute, le "
                "deuxième laisse le choix, le troisième oppose. Se tromper de mot, "
                "c'est dire le contraire de ce qu'on veut.",
        duree='60 minutes')

    d.titre(notes="Écrire au tableau : « J'aimerais suivre ce cours ___ l'horaire ne me "
                  "convient pas. » Faire compléter. Le groupe trouvera « mais » : la "
                  "leçon est déjà commencée.")

    d.objectifs([
        "employer « et » pour ajouter une information ;",
        "employer « ou » pour proposer un choix ;",
        "employer « mais » pour marquer une opposition ;",
        "relier deux phrases courtes en une seule phrase claire.",
    ])

    d.tableau('Analyse', "Trois connecteurs, trois emplois",
              ['Le mot', 'Ce qu\'il fait', 'Un exemple'],
              [["et", "il ajoute", "Il a parlé à la responsable et elle l'a informé."],
               ["ou", "il laisse le choix", "Tu choisis maintenant ou tu attends demain."],
               ["mais", "il oppose", "J'aimerais ce cours, mais l'horaire ne convient pas."]],
              cle=0,
              note="« Mais » est presque toujours précédé d'une virgule. Les deux autres, "
                   "rarement.",
              notes="Faire remarquer la virgule devant « mais ». C'est un repère "
                    "d'écriture simple et fiable à ce niveau.")

    d.regle('La règle',
            "Le connecteur dit la relation entre les deux phrases.",
            precision="« Je viens et j'apporte un billet » : deux choses vraies. « Je "
                      "viens ou j'envoie un courriel » : une seule des deux. « Je "
                      "viendrais, mais je travaille » : la deuxième empêche la "
                      "première.",
            notes="Écrire les trois phrases au tableau, l'une sous l'autre. La "
                  "comparaison fait tout le travail.")

    d.cartes('Analyse', "Comment choisir en deux secondes", [
        ("Les deux sont vraies ?",
         "C'est « et ». « Je préviens mon superviseur et j'envoie un courriel » : je "
         "fais les deux."),
        ("Une seule des deux ?",
         "C'est « ou ». « Tu manges à la cafétéria ou tu apportes ton repas ? » : une "
         "seule possibilité à la fois."),
        ("La deuxième empêche la première ?",
         "C'est « mais ». « J'aimerais t'accompagner, mais je dois travailler » : le "
         "travail empêche l'accompagnement."),
        ("Le test de la surprise",
         "Si la deuxième phrase surprend après la première, c'est « mais ». C'est le "
         "test le plus rapide."),
    ], notes="La quatrième carte donne un critère intuitif qui fonctionne presque "
             "toujours. Le faire appliquer à voix haute.")

    d.pratique('Pratique · 1 de 4', "Et, ou ou mais ?",
               "Posez-vous la question : les deux, une seule, ou une opposition ?", [
        ("Tu préviens ton superviseur ___ tu envoies un courriel ?", "ou"),
        ("J'aimerais t'accompagner, ___ je dois travailler ce jour-là.", "mais"),
        ("Elle fait du bénévolat, ___ elle préfère les activités en plein air.", "mais"),
        ("À midi, tu manges à la cafétéria ___ tu apportes ton repas ?", "ou"),
        ("J'aimerais suivre ce cours du soir, ___ l'horaire ne me convient pas.", "mais"),
        ("Hier, j'ai révisé mes verbes, ___ demain je réviserai le vocabulaire.", "et"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par le critère. Ne jamais accepter « ça "
             "sonne mieux » comme justification.")

    d.piege("Le piège du « et » à la place de « mais »",
            "J'aimerais venir et je dois travailler.",
            "J'aimerais venir, mais je dois travailler.",
            "« Et » met les deux phrases sur le même plan : on comprend que la personne "
            "veut venir et qu'elle travaille, sans lien entre les deux. « Mais » dit que "
            "le travail empêche la venue. C'est cette information qui manque avec "
            "« et ».",
            notes="Erreur très fréquente, et elle passe inaperçue à l'oral. À l'écrit, "
                  "elle rend la phrase illogique.")

    d.piege("Le piège du « ou » dans une question",
            "Tu viens ou ?",
            "Tu viens ou tu restes ?",
            "« Ou » relie deux possibilités : il en faut donc deux. Une question qui se "
            "termine par « ou » laisse la seconde possibilité non dite, et l'auditeur "
            "doit deviner. Nommez toujours les deux.",
            notes="Erreur d'oral courante au Québec dans le langage familier. La "
                  "signaler comme un usage familier, pas comme une faute grave.")

    d.pratique('Pratique · 2 de 4', "Reliez les deux phrases",
               "Choisissez le connecteur qui dit la vraie relation.", [
        ("Je préviens le superviseur. J'envoie un courriel.",
         "Je préviens le superviseur et j'envoie un courriel."),
        ("J'aimerais suivre ce cours. Il se donne seulement à l'hiver.",
         "J'aimerais suivre ce cours, mais il se donne seulement à l'hiver."),
        ("Tu apportes un billet médical. Tu apportes une attestation.",
         "Tu apportes un billet médical ou une attestation."),
        ("Ma voiture est en panne. J'attends la dépanneuse.",
         "Ma voiture est en panne et j'attends la dépanneuse."),
    ], corrige=True,
       notes="Le premier et le quatrième prennent « et », mais pour des raisons "
             "différentes : addition dans un cas, conséquence dans l'autre. Le signaler.")

    d.pratique('Pratique · 3 de 4', "Écrivez la suite",
               "Le début est donné, le connecteur aussi. Complétez.", [
        ("Je serai en retard ce matin, mais…", "…je serai là pour l'évaluation."),
        ("Je vous appelle et…", "…je vous enverrai aussi un courriel."),
        ("Voulez-vous que je vienne demain ou…", "…préférez-vous jeudi ?"),
        ("J'apporterai un billet médical, mais…", "…seulement lundi, la clinique est fermée."),
    ], corrige=True,
       notes="Exercice de production. Accepter toute suite logique : c'est la cohérence "
             "avec le connecteur qu'on évalue.")

    d.pratique('Pratique · 4 de 4', "Corrigez le connecteur",
               "Chaque phrase emploie le mauvais mot.", [
        ("J'aimerais venir et je travaille ce jour-là.", "mais"),
        ("Je préviens le superviseur mais j'envoie un courriel.", "et"),
        ("Tu viens à neuf heures et à dix heures ?", "ou"),
        ("Ma voiture est en panne ou j'attends la dépanneuse.", "et"),
    ], corrige=True,
       notes="Exercice de relecture. C'est la compétence qui sert vraiment : repérer un "
             "connecteur qui ne dit pas ce qu'on voulait dire.")

    d.billet(
        "Écrivez trois phrases sur votre semaine : une avec « et », une avec « ou », une avec « mais ».",
        exemples=[
            "Chacune doit contenir deux phrases reliées.",
            "N'oubliez pas la virgule devant « mais ».",
        ],
        notes="Corriger le choix du connecteur et la virgule. Rendre avant D1, où ces "
              "connecteurs serviront dans un courriel.")

    return d.save(dossier)
