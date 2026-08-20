# -*- coding: utf-8 -*-
"""A1 · Dans l'allée des conserves — mise en situation.
Bloc A « Je découvre » · couleur teal · 75 min.
Source du module : dialogue `prep`, exercices `prVocab` et `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-alimentation/images/')


def build(dossier):
    d = Deck(
        code='A1', section='teal',
        titre="Dans l'allée des conserves",
        chapeau="Farida est arrivée du Maroc il y a deux ans. Elle fait son "
                "épicerie chaque semaine, mais elle perd du temps à chercher — "
                "et elle n'a jamais vraiment su lire une étiquette.",
        duree='75 minutes')

    d.titre(notes="Ouverture du module. Question d'entrée : « combien de temps prend votre "
                  "épicerie ? ». Les réponses varient du simple au triple, et c'est "
                  "presque toujours le temps passé à chercher.")

    d.objectifs([
        "demander où se trouve un produit dans un magasin ;",
        "comprendre une réponse qui situe un produit ;",
        "savoir où regarder sur un emballage : le tableau, la provenance, la date ;",
        "comparer deux marques du même produit.",
    ])

    d.declencheur(
        'Mise en situation', "Vous cherchez un produit et vous ne le trouvez pas. Que faites-vous ?",
        image=IMG + 'allee-conserves.jpg',
        pistes=[
            "Combien de temps cherchez-vous avant de demander ?",
            "À qui demandez-vous ? Comment commencez-vous la phrase ?",
            "Y a-t-il un produit que vous n'avez jamais réussi à trouver ici ?",
            "Comment choisissez-vous entre deux marques ?",
        ],
        notes="Cinq minutes. La troisième piste fait souvent sortir des produits du pays "
              "d'origine : c'est une bonne occasion de parler des épiceries de quartier.")

    d.cartes('La situation', "Ce qu'on sait de Farida", [
        ("D'où elle vient",
         "Du Maroc. Elle est au Québec depuis deux ans et fait son épicerie chaque "
         "semaine."),
        ("Ce qui lui coûte du temps",
         "Elle cherche. Elle a fait deux fois le tour du magasin avant de demander."),
        ("Ce qu'elle ne sait pas faire",
         "Lire une étiquette. Elle ne sait pas où regarder, et il y a quarante chiffres."),
        ("Ce qu'elle apprend aujourd'hui",
         "Que le commis connaît ses allées par cœur, et que le tableau nutritif est "
         "toujours au même endroit."),
    ], notes="La deuxième carte est celle qui parle au groupe : presque tout le monde a "
             "déjà fait deux fois le tour d'une épicerie.")

    d.dialogue('Dialogue · 1 de 3', "Demander où", [
        ("FARIDA", "Excusez-moi, je cherche de la pâte de tomate. J'ai fait deux fois le tour.", True),
        ("SIMON", "De la pâte de tomate… C'est dans l'allée cinq, avec les sauces. Pas avec les légumes en conserve.", False),
        ("FARIDA", "Ah, je cherchais du mauvais côté. Il y a plusieurs marques ?", True),
        ("SIMON", "Trois ou quatre. Celle du bas est la moins chère, mais elle est plus salée.", False),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="La formule complète est dans la première réplique : « Excusez-moi, je "
             "cherche… ». Faire répéter par le groupe. Noter aussi « de la pâte de "
             "tomate » : la forme sera travaillée au bloc B.")

    d.dialogue('Dialogue · 2 de 3', "Comparer deux marques", [
        ("FARIDA", "Comment vous savez ça ?", False),
        ("SIMON", "C'est écrit sur l'étiquette. Regardez la ligne du sodium : deux cent quarante milligrammes contre quatre-vingts.", True),
        ("FARIDA", "Je ne sais jamais où regarder sur ces étiquettes.", True),
        ("SIMON", "Le tableau de la valeur nutritive est toujours au dos, en noir et blanc. Toujours au même endroit.", True),
    ], notes="Trois fois plus de sel pour un produit qui se ressemble : le faire "
             "remarquer. C'est ce qui justifie la séance D1 du module.")

    d.dialogue('Dialogue · 3 de 3', "D'où ça vient", [
        ("FARIDA", "Et ça, ça vient d'où ?", True),
        ("SIMON", "La provenance est écrite en petit, sous le code-barres. Celle-là vient de l'Ontario.", True),
        ("FARIDA", "Merci beaucoup. Vous m'avez sauvé dix minutes.", False),
        ("SIMON", "Ça fait plaisir. Si vous ne trouvez pas quelque chose, demandez : on connaît nos allées par cœur.", True),
    ], notes="La dernière réplique est celle à retenir : demander est normal et attendu. "
             "Beaucoup d'élèves croient déranger.")

    d.vocabulaire('Vocabulaire · 1 de 2', "Le magasin", [
        ("une allée", "Le corridor entre deux rangées d'étagères."),
        ("une conserve", "Un aliment vendu dans une boîte de métal fermée."),
        ("un comptoir", "L'endroit où un employé sert : boucherie, poissonnerie, charcuterie."),
        ("un commis", "L'employé qui remplit les tablettes et renseigne les clients."),
        ("un spécial", "Un rabais temporaire. Au Québec, on dit « il y a un spécial »."),
    ], notes="« Un spécial » est un québécisme très employé. Donner aussi « en solde », "
             "compris partout.")

    d.vocabulaire('Vocabulaire · 2 de 2', "L'emballage", [
        ("une étiquette", "Le papier collé sur un produit, avec le prix et les informations."),
        ("la valeur nutritive", "Le tableau des calories, du sodium et des sucres."),
        ("la provenance", "Le pays ou la région d'où vient le produit."),
        ("le code-barres", "Les traits noirs que la caisse lit. La provenance est souvent juste en dessous."),
        ("le prix au kilo", "Le prix ramené au poids : c'est lui qui permet de comparer deux formats."),
    ], notes="Le prix au kilo est le grand oublié. Le montrer sur une vraie étiquette de "
             "tablette si possible.")

    d.regle("Ce qu'il faut retenir",
            "Demandez. Le commis connaît ses allées par cœur.",
            precision="Dix minutes de recherche contre dix secondes de question. Les "
                      "employés d'épicerie sont là pour ça, et personne ne trouve la "
                      "question dérangeante. « Excusez-moi, je cherche… » suffit.",
            notes="Faire répéter la phrase par deux élèves. C'est la diapo à photographier.")

    d.piege('Chercher au lieu de demander',
            "J'ai fait deux fois le tour.",
            "Excusez-moi, je cherche de la pâte de tomate.",
            "Les deux mènent au produit, mais l'une prend dix minutes et l'autre dix "
            "secondes. La gêne de demander coûte, chaque semaine, plus de temps que tout "
            "le reste de l'épicerie.",
            notes="Ne pas culpabiliser : cette gêne est très commune, y compris chez les "
                  "gens d'ici.")

    d.billet(
        "Notez trois produits que vous cherchez souvent et où ils se trouvent.",
        exemples=[
            "Dans votre épicerie habituelle.",
            "Si vous ne savez pas, écrivez la question que vous poserez.",
        ],
        notes="Ramasser. Les questions serviront au jeu de rôle de E1.")

    return d.save(dossier)
