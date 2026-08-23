# -*- coding: utf-8 -*-
"""B2 · L'impératif : la langue des répondeurs
Bloc B « Défi 1 · Le répondeur du centre » · couleur ambre · 75 min.
Source du module : exercice `t1imper` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="L'impératif : la langue des répondeurs",
        chapeau="Appuyez. Composez. Laissez. Ne quittez pas. Raccrochez. "
                "Cinq verbes sans sujet, et vous traversez n'importe quel "
                "menu téléphonique du Québec.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, mais elle sert d'abord à comprendre : "
                  "l'impératif est ici une forme à reconnaître avant d'être une forme à "
                  "produire. Commencer par faire écouter le menu de B1 en demandant "
                  "seulement de compter les verbes.")

    d.objectifs([
        "reconnaître l'impératif dans un menu téléphonique ;",
        "former l'impératif avec « vous » en enlevant le pronom ;",
        "le mettre à la forme négative : ne raccrochez pas ;",
        "placer le pronom derrière au positif, devant au négatif.",
    ], notes="Le quatrième objectif est le seul difficile. Les trois premiers se "
             "règlent en vingt minutes ; garder le reste de la séance pour les "
             "pronoms.")

    d.regle("On enlève le pronom, rien de plus",
            "vous appuyez donne appuyez. vous laissez donne laissez.",
            precision="Aucune autre modification. Aucune exception dans les "
                      "verbes du module.",
            notes="Diapositive à photographier. Faire produire quatre autres impératifs "
                  "à partir du présent : vous signez, vous rappelez, vous remettez, "
                  "vous descendez.")

    d.tableau('Du présent à l\'impératif', "Quatre verbes du répondeur",
              ['Au présent', 'À l\'impératif'],
              [["vous appuyez", "appuyez"],
               ["vous composez", "composez"],
               ["vous laissez", "laissez"],
               ["vous raccrochez", "raccrochez"],
               ["vous restez", "restez"],
               ["vous signez", "signez"]],
              cle=1,
              notes="Masquer la colonne de droite et faire produire à l'oral. C'est "
                    "l'exercice le plus rapide du module : quatre-vingts pour cent du "
                    "groupe l'a en deux minutes.")

    d.regle("À la forme négative, rien ne bouge",
            "Le « ne » devant le verbe, le « pas » derrière : ne raccrochez "
            "pas.",
            precision="À l'oral, le « ne » tombe souvent — mais il ne "
                      "s'écrit jamais sans lui.",
            notes="Signaler « ne quittez pas », qui est une formule fixe du téléphone "
                  "et veut dire « restez en ligne ». Elle n'a rien à voir avec quitter "
                  "un lieu, et elle surprend tout le monde une fois.")

    d.cartes("Avec un pronom", "Deux places, une seule règle", [
        ("Au positif : derrière",
         "Rappelez-moi. Parlez-lui. Lisez-la. Avec un trait d'union."),
        ("Au négatif : devant",
         "Ne me rappelez pas. Ne lui parlez pas. Sans trait d'union."),
        ("« me » devient « moi »",
         "vous me rappelez donne rappelez-moi, jamais « rappelez-me »."),
        ("Le trait d'union",
         "Il montre que le pronom fait partie du verbe. Il n'est pas facultatif."),
    ], notes="La quatrième carte se voit à l'écrit seulement, et c'est le point du jour "
             "qui reviendra en D2 : une note où l'on écrit « rappelez moi » se lit "
             "encore, mais elle se voit.")

    d.pratique('Formation', "Mettez le verbe à l'impératif",
               "À la forme « vous ».", [
        ("(Appuyer) ___ sur le 1 pour signaler une absence.", "Appuyez"),
        ("(Laisser) ___ votre message après le signal sonore.", "Laissez"),
        ("(Composer) ___ le poste 224.", "Composez"),
        ("Ne (raccrocher) ___ pas avant la fin du message.", "raccrochez"),
        ("(Rappeler) ___-moi cet après-midi.", "Rappelez"),
        ("(Lire) ___-la à voix haute avant de la remettre.", "Lisez"),
    ], corrige=True,
       notes="Les deux dernières portent le trait d'union. Les faire écrire au tableau "
             "par deux élèves : c'est là que le trait manque, jamais à l'oral.")

    d.pratique('Positif et négatif', "La même consigne, deux fois",
               "Mettez la phrase à la forme négative.", [
        ("Rappelez-moi avant midi.", "Ne me rappelez pas avant midi."),
        ("Parlez-lui aujourd'hui.", "Ne lui parlez pas aujourd'hui."),
        ("Appuyez tout de suite.", "N'appuyez pas tout de suite."),
        ("Remettez-la au comptoir.", "Ne la remettez pas au comptoir."),
        ("Quittez la ligne.", "Ne quittez pas la ligne."),
        ("Téléphonez-moi ce soir.", "Ne me téléphonez pas ce soir."),
    ], corrige=True,
       notes="C'est l'exercice de la séance. Faire remarquer que le pronom traverse le "
             "verbe : derrière au positif, devant au négatif. Le montrer avec la main, "
             "physiquement, au tableau.")

    d.piege("Laisser le pronom derrière au négatif",
            "Ne rappelez-moi pas avant midi.",
            "Ne me rappelez pas avant midi.",
            "Au positif, le pronom passe derrière avec un trait d'union. Au "
            "négatif, il revient devant, sans trait d'union. C'est la seule chose "
            "à retenir en plus, et elle vaut pour tous les verbes.",
            notes="Cette faute-là s'entend, contrairement au trait d'union. La corriger "
                  "à l'oral chaque fois qu'elle passe, sans commentaire : la répétition "
                  "suffit.")

    d.tableau('Les cinq phrases des répondeurs', "À reconnaître partout",
              ['La phrase', 'Ce qu\'elle veut dire'],
              [["Faites le 1.", "Appuyez sur la touche 1."],
               ["Composez le poste.", "Tapez le numéro interne de la personne."],
               ["Restez en ligne.", "Attendez, quelqu'un va répondre."],
               ["Ne quittez pas.", "La même chose, en plus court."],
               ["Après le signal sonore.", "Parlez seulement quand vous entendez le son."]],
              cle=1,
              notes="Ces cinq-là couvrent presque tous les menus du Québec, celui de la "
                    "banque et celui de la clinique compris. Les faire répéter les yeux "
                    "fermés, comme au téléphone.")

    d.billet(
        "Écrivez deux consignes que vous avez déjà entendues dans un "
        "répondeur, en français.",
        exemples=[
            "Le verbe à l'impératif, comme au téléphone.",
            "Si vous ne vous souvenez pas des mots exacts, écrivez ce que ça voulait dire.",
        ],
        notes="Ramasser. Les réponses viennent souvent de la banque, du service à la "
              "clientèle ou de la clinique : les lire à voix haute au début de B3, elles "
              "montrent que la forme se retrouve partout.")

    return d.save(dossier)
