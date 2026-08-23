# -*- coding: utf-8 -*-
"""A2 · Constater, se plaindre, accuser
Bloc A « Je découvre » · couleur indigo · prosodie · 75 min.
Source : exercice `prProso` (douze cartes écoutables) et sa mini-leçon ;
savoir « système prosodique » du niveau 7 (trois points).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Constater, se plaindre, accuser",
        chapeau="La même information, dite de trois façons, ne produit pas "
                "le même effet. Et ce n'est pas le vocabulaire qui décide : "
                "c'est la voix.",
        duree='75 minutes')

    d.titre(notes="Séance d'écoute. Prévoir un appareil qui porte bien dans la salle : "
                  "tout le contenu se joue sur des différences de mélodie, et un "
                  "haut-parleur d'ordinateur portable ne suffit pas.")

    d.objectifs([
        "entendre la différence entre un constat, une plainte et une accusation ;",
        "reconnaître la syllabe que la voix appuie dans chaque cas ;",
        "produire la même information sur les trois tons ;",
        "savoir laquelle des trois fait avancer une réclamation.",
    ], notes="Le quatrième objectif est le seul qui compte à long terme. Il ne "
             "s'enseigne pas : il se démontre, en faisant jouer les trois versions "
             "devant le groupe et en demandant ce qu'on répondrait.")

    d.declencheur(
        'Mise en situation', "Quelqu'un vous a-t-il déjà mal pris une phrase que vous pensiez neutre ?",
        pistes=[
            "Qu'aviez-vous dit exactement, avec quels mots ?",
            "Qu'est-ce que la personne a compris ?",
            "Auriez-vous pu le dire autrement avec les mêmes mots ?",
            "Est-ce arrivé plus souvent en français que dans votre langue ?",
        ],
        notes="La dernière question ouvre une discussion utile : la mélodie du reproche "
              "n'est pas la même d'une langue à l'autre, et un débit rapide fait tomber "
              "la fin des phrases en français. Ce n'est pas un défaut de politesse.")

    d.tableau('Analyse', "Trois intentions, trois mélodies",
              ['On dit', 'La voix'],
              [["On constate", "plate, régulière, descente légère à la fin"],
               ["On se plaint", "monte sur le mot de jugement, puis retombe"],
               ["On accuse", "appuie sur « vous », débit qui s'accélère"],
               ["Ce qu'on retient", "un fait, une émotion, ou une attaque"],
               ["Ce qu'on obtient", "une note au dossier, de la pitié, ou une défense"]],
              cle=0,
              notes="Diapositive à photographier. La dernière rangée est celle qui "
                    "convainc : personne ne veut de la deuxième colonne au comptoir.")

    d.cartes('Écoute', "La même panne, trois fois", [
        ("On constate", "« La transmission cogne le matin, depuis le vingt-quatre avril. »"),
        ("On se plaint", "« Je trouve inacceptable qu'une auto brise après vingt-quatre jours. »"),
        ("On accuse", "« Vous m'avez vendu une auto que vous saviez brisée. »"),
        ("Ce qui les sépare", "Le premier est vérifiable, le deuxième est vrai, le troisième est indémontrable."),
    ], notes="Lire les trois à voix haute soi-même avant de les faire écouter. Le "
             "groupe entend mieux la différence chez une personne présente que dans un "
             "extrait enregistré.")

    d.regle("Le constat est la voix qui obtient quelque chose",
            "Un fait daté ne se discute pas ; une émotion se plaint ; une accusation se défend.",
            precision="Se plaindre n'est pas interdit, et le programme le demande même "
                      "explicitement : manifester sa déception et son mécontentement. "
                      "Mais une plainte ne fait pas avancer un dossier toute seule. "
                      "Elle s'emploie une fois, après les faits, et de préférence avec "
                      "un chiffre : « c'est la troisième fois que je me déplace » est "
                      "une plainte qui laisse une trace.",
            notes="Diapositive à photographier. Insister sur l'ordre : les faits "
                  "d'abord, la plainte ensuite si elle sert, l'accusation jamais à "
                  "l'oral. Ce qui est grave s'écrit.")

    d.pratique('Écoute', "Qu'est-ce que la voix fait entendre ?",
               "Écoutez chaque phrase et dites : on constate, on se plaint, ou on accuse.", [
        ("La transmission cogne le matin, depuis le 24 avril.", "on constate"),
        ("Je trouve inacceptable qu'une auto brise après 24 jours.", "on se plaint"),
        ("Vous m'avez vendu une auto que vous saviez brisée.", "on accuse"),
        ("L'étiquette porte la mention « catégorie C ».", "on constate"),
        ("C'est la troisième fois que je me déplace pour rien.", "on se plaint"),
        ("Vous faites exprès de ne pas rappeler vos clients.", "on accuse"),
    ], corrige=True,
       notes="Douze cartes dans le module ; en projeter six et garder les six autres "
             "pour la reprise à l'écran. Faire redire chaque phrase par un élève sur le "
             "bon ton avant de passer à la suivante.")

    d.piege('Piège', "dire un fait avec la voix d'une plainte",
            "lire ses trois premières phrases à voix haute avant d'entrer",
            "Un fait dit sur un ton de plainte s'entend comme une plainte, et se "
            "traite comme telle. Se les répéter une fois dans l'auto suffit à les "
            "aplatir. C'est le conseil le plus utile de tout le bloc, et il ne coûte "
            "rien.",
            notes="Faire l'exercice pour vrai : chacun écrit ses trois phrases "
                  "d'ouverture et les lit à son voisin. Cinq minutes, et l'effet se "
                  "voit dès le bloc C.")

    d.pratique('Production', "La même idée, sur le bon ton",
               "Deux par deux : l'un dit la phrase, l'autre nomme l'intention entendue.", [
        ("Le rendez-vous promis n'a pas eu lieu.", "constat : deux dates, rien de plus"),
        ("Je suis déçue du service que je reçois.", "plainte : vraie, et elle ne prouve rien"),
        ("Vous ne rappelez jamais personne.", "accusation : « jamais » la rend invérifiable"),
        ("Vous deviez me rappeler vendredi ; nous sommes mardi.", "constat : la même chose, en mieux"),
    ], corrige=True,
       notes="Le quatrième item est la réécriture du troisième. Le faire remarquer "
             "explicitement : on ne renonce à rien en passant de l'un à l'autre.")

    d.billet(
        "Écris une phrase que tu dirais au comptoir, sur le ton du constat.",
        exemples=[
            "Une date, un fait, aucun adjectif.",
            "Relis-la à voix haute avant de l'écrire.",
        ],
        notes="Trois minutes. Ramasser les billets : ceux qui contiennent un adjectif "
              "de jugement montrent où en est le groupe, et ils resservent en C1.")

    return d.save(dossier)
