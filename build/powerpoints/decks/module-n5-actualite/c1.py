# -*- coding: utf-8 -*-
"""C1 · « Qui a dit ça, au juste ? »
Bloc C « Défi 2 · Ce que les gens ont dit » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2a`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-actualite/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="« Qui a dit ça, au juste ? »",
        chapeau="Trois jours de pluie, la rivière Magog sortie de son lit, "
                "une dizaine de sous-sols inondés. La Ville affirme une "
                "chose, une résidente en demande une autre, les pompiers en "
                "expliquent une troisième. Répéter tout ça sans dire qui "
                "l'a dit, c'est transformer une nouvelle en rumeur.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2. Commencer par un jeu : dire au groupe « il "
                  "paraît que le centre ferme deux jours la semaine prochaine » et "
                  "laisser passer trois secondes. Demander ensuite qui l'a dit. "
                  "Personne. C'est toute la séance.")

    d.objectifs([
        "rapporter au présent une parole lue dans le journal ;",
        "nommer la personne ou le service qui a parlé ;",
        "choisir le verbe qui convient : dit, explique, demande, raconte ;",
        "distinguer une déclaration d'une rumeur.",
    ], notes="Le deuxième objectif est le seul qui compte vraiment. Les trois autres "
             "sont les moyens de le tenir : sans nom, la phrase la mieux construite "
             "ne vaut rien.")

    d.declencheur(
        'Observation', "Un sous-sol où l'eau monte au-dessus des boîtes. "
                       "Qui va parler dans cet article ?",
        image=IMG + 'sous-sol-inonde.jpg',
        pistes=[
            "La personne qui habite la maison : elle raconte ce qu'elle a perdu.",
            "La Ville : elle explique ce qu'elle a fait, et quand.",
            "Les pompiers : ils disent ce qu'ils font en ce moment.",
            "Environnement Canada : l'avertissement avait été émis la veille.",
        ],
        notes="Faire deviner les quatre voix avant de lire le dialogue. Elles y sont "
              "toutes les quatre, et le groupe les retrouvera sans peine : c'est un "
              "bon moyen de montrer qu'un fait divers est prévisible.")

    d.dialogue('Dialogue · 1 de 5', "Il a mouillé sans bon sens", [
        ("TERESA", "Allô ! Ça va ? Il paraît qu'il a mouillé sans bon sens "
                   "chez vous.", True),
        ("MARISOL", "Trois jours de pluie. La rivière Magog est sortie de "
                    "son lit.", True),
        ("TERESA", "Sortie de son lit ? C'est grave, ça ?", True),
        ("MARISOL", "Une dizaine de sous-sols inondés sur la rue des "
                    "Peupliers.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Teresa est une amie qui habite loin : c'est pour cela qu'elle ne sait "
             "rien. Sa toute première phrase commence par « il paraît que » — la "
             "formule que la séance va démonter. La faire remarquer tout de suite.")

    d.dialogue('Dialogue · 2 de 5', "Elle le dit, ou tu le penses ?", [
        ("TERESA", "Et la Ville, elle fait quoi ?", True),
        ("MARISOL", "La Ville dit qu'elle a distribué des sacs de sable dès "
                    "lundi.", True),
        ("TERESA", "Elle le dit, ou tu le penses ?", True),
        ("MARISOL", "Elle le dit. C'est écrit dans le journal, entre "
                    "guillemets.", True),
    ], notes="La question de Teresa est la question du module entier. La projeter "
             "seule si besoin. Faire remarquer la réponse : « entre guillemets » — "
             "c'est le signe visible d'une parole rapportée mot pour mot.")

    d.dialogue('Dialogue · 3 de 5', "Une résidente raconte", [
        ("TERESA", "Et le monde de la rue, ils disent quoi ?", True),
        ("MARISOL", "Une résidente raconte qu'elle a tout perdu dans son "
                    "sous-sol.", True),
        ("TERESA", "Pauvre elle. Elle demande quelque chose ?", True),
        ("MARISOL", "Elle demande si la Ville va refaire le fossé au bout "
                    "de la rue.", True),
    ], notes="Deux structures dans quatre répliques : « raconte que » pour une "
             "affirmation, « demande si » pour une question par oui ou non. Les "
             "signaler sans les développer : elles font l'objet de la séance C2.")

    d.dialogue('Dialogue · 4 de 5', "La Ville n'a pas voulu dire quand", [
        ("TERESA", "Et personne ne répond à ça ?", True),
        ("MARISOL", "Le journal écrit que la Ville n'a pas voulu dire "
                    "quand.", True),
        ("TERESA", "Toi, tu me dis toujours qui parle. J'aime ça.", True),
        ("MARISOL", "Sinon on ne sait plus qui pense quoi. C'est mêlant.", True),
    ], notes="« La Ville n'a pas voulu dire quand » est une information, pas un vide : "
             "un refus de répondre se rapporte comme le reste. Le faire remarquer, "
             "c'est un point de lecture que peu d'élèves voient seuls.")

    d.dialogue('Dialogue · 5 de 5', "Ils pompent depuis mercredi", [
        ("TERESA", "C'est vrai. Bon, et il reste de l'eau dans les "
                   "maisons ?", True),
        ("MARISOL", "Les pompiers expliquent qu'ils pompent depuis mercredi "
                    "matin.", False),
    ], notes="Dernière voix du dialogue, et troisième verbe : dit, raconte, demande, "
             "explique. Faire relever les quatre au tableau avant la mise en commun : "
             "ils sont la matière du reste de la séance.")

    d.regle("On nomme d'abord celui qui parle, on rapporte ensuite",
            "La Ville dit qu'elle a distribué des sacs de sable. Les "
            "pompiers expliquent qu'ils pompent depuis mercredi.",
            precision="Le verbe reste au présent : la parole a été dite hier, mais "
                      "elle tient encore aujourd'hui. C'est la position de la "
                      "Ville, pas un évènement de sa journée. Sans le nom au début, "
                      "la phrase devient « il paraît que » — et ça ne vaut rien.",
            notes="Diapositive à photographier. C'est la règle que le jeu de rôle de "
                  "E1 vérifie : l'assistant demandera « qui dit ça ? » chaque fois "
                  "qu'une information arrivera sans propriétaire.")

    d.tableau('Quatre voix', "Qui parle, et ce que chacun apporte",
              ['Qui parle', 'Ce qu\'il apporte'],
              [["La Ville", "Ce qu'elle a fait, et quand : les sacs de sable dès lundi"],
               ["Une résidente", "Ce qu'elle a vécu, et ce qu'elle demande"],
               ["Les pompiers", "Ce qui se passe en ce moment : ils pompent"],
               ["Le journal", "Ce que personne n'a voulu dire : la date du fossé"],
               ["« Il paraît que »", "Rien du tout : personne ne le dit"]],
              cle=0,
              notes="La dernière ligne est la leçon. Demander au groupe ce qu'on peut "
                    "faire d'une information sans propriétaire : ni la vérifier, ni "
                    "la corriger, ni la citer. On ne peut que la répéter.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'appel du soir avec Teresa.", [
        ("Il a plu trois jours de suite à Sherbrooke.", "vrai"),
        ("La rivière Magog est sortie de son lit.", "vrai"),
        ("Une trentaine de sous-sols ont été inondés.", "faux — une dizaine"),
        ("La Ville dit qu'elle a distribué des sacs de sable dès lundi.", "vrai"),
        ("C'est Marisol qui pense que la Ville a distribué des sacs.", "faux — la Ville le dit"),
        ("Une résidente raconte qu'elle a tout perdu dans son sous-sol.", "vrai"),
        ("La Ville a répondu quand elle referait le fossé.", "faux — elle n'a pas voulu dire quand"),
        ("Les pompiers expliquent qu'ils pompent depuis mercredi matin.", "vrai"),
    ], corrige=True,
       notes="Exercice t2a de l'activité. La cinquième est la plus formatrice : elle "
             "demande de se rappeler non pas l'information, mais sa source. C'est "
             "exactement la compétence du défi.")

    d.billet(
        "Rapportez une parole du dialogue, en nommant qui l'a dite.",
        exemples=[
            "Une seule phrase : qui parle, le verbe au présent, puis « que » ou « si ».",
            "Relisez : est-ce qu'on sait de qui vient l'information ?",
        ],
        notes="Ramasser. Les billets sans nom — il y en aura — servent d'ouverture à "
              "C2 : les lire à voix haute sans nommer les auteurs et demander au "
              "groupe ce qui manque.")

    return d.save(dossier)
