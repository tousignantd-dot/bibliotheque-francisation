# -*- coding: utf-8 -*-
"""C2 · La phrase emphatique.
Bloc C · couleur ambre (écriture) · 75 min.
Source : exercice `t2emph` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Ce qui m\'a plu, c\'est…',
        chapeau="« La chambre m'a plu » ou « ce qui m'a plu, c'est la chambre » ? La "
                "seconde met la chambre en vedette — et c'est ainsi qu'on dit ce qui "
                "compte vraiment.",
        duree='75 minutes')

    d.titre(notes="Écrire les deux phrases au tableau et les faire dire à voix haute. "
                  "Demander laquelle sonne comme une vraie conversation. Le groupe "
                  "choisira la seconde.")

    d.objectifs([
        "mettre un élément en évidence avec c'est… qui ou c'est… que ;",
        "employer « ce qui…, c'est… » et « ce que…, c'est… » ;",
        "employer « celui que…, c'est… » pour une personne ou une chose précise ;",
        "dire ce qui plaît et ce qui inquiète.",
    ])

    d.tableau('Analyse', "Quatre constructions",
              ['La construction', 'Un exemple'],
              [["C'est… qui", "C'est Ginette qui fournit la peinture."],
               ["C'est… que", "C'est le camion de farine que je crains."],
               ["Ce qui…, c'est…", "Ce qui m'a plu, c'est la chambre."],
               ["Ce que…, c'est…", "Ce que je changerais, c'est la couleur des murs."]],
              cle=0, props=[0.24, 0.76],
              notes="Les deux premières mettent en évidence un nom ; les deux dernières "
                    "ouvrent la phrase sur ce qu'on va dire. Le sens est proche.")

    d.regle('La règle de « qui » et « que »',
            "« Qui » si l'élément fait l'action. « Que » dans tous les autres cas.",
            precision="« C'est Ginette qui fournit » — Ginette fournit, elle fait "
                      "l'action. « C'est le camion que je crains » — le camion ne craint "
                      "rien, c'est moi qui crains. Le test est le même qu'au module 5.",
            notes="Faire poser la question « qui fait l'action ? » avant chaque choix. "
                  "C'est mécanique et fiable.")

    d.regle("« Ce qui » et « ce que »",
            "Même règle : « ce qui » fait l'action, « ce que » la subit.",
            precision="« Ce qui m'a plu » — quelque chose m'a plu, cette chose fait "
                      "l'action. « Ce que je changerais » — je changerais quelque chose, "
                      "c'est moi qui agis. Regardez ce qui suit : un verbe, ou un sujet.",
            notes="Le repère du module 4 fonctionne encore : après « qui », un verbe ; "
                  "après « que », un sujet.")

    d.cartes('Ouvrir la mini-leçon', "Quatre choses à savoir en plus", [
        ("« Celui que », « celle que »",
         "Pour une personne ou une chose déjà nommée : « Celui que je crains, c'est le "
         "camion. » « Celle que je préfère, c'est la chambre. »"),
        ("« Ce sont » au pluriel",
         "« Ce sont les voisins qui font du bruit. » À l'oral on entend souvent "
         "« c'est » ; à l'écrit, « ce sont »."),
        ("La virgule",
         "« Ce qui m'a plu, c'est la chambre. » Une virgule sépare les deux moitiés. "
         "Elle marque la pause qu'on fait en parlant."),
        ("Pourquoi c'est utile",
         "Quand on compare deux logements, cette construction dit tout de suite ce qui "
         "compte : « Ce qui me décide, c'est le prix. »"),
    ], notes="La quatrième carte relie la grammaire à l'usage du module. C'est la "
             "construction du défi 2, et elle sert en E1.")

    d.pratique('Pratique · 1 de 4', "Quel élément est mis en évidence ?",
               "Ce qui suit « c'est ».", [
        ("Ce qui m'a plu, c'est la chambre sur la cour.", "la chambre sur la cour"),
        ("Celui que je crains, c'est le camion de farine.", "le camion de farine"),
        ("Ce que je changerais, c'est la couleur des murs.", "la couleur des murs"),
        ("Celle que Leyla a remarquée, c'est la fenêtre de la cuisine.",
         "la fenêtre de la cuisine"),
        ("C'est Ginette qui fournit la peinture.", "Ginette"),
        ("Ce qui presse le plus, c'est la signature du bail.", "la signature du bail"),
    ], corrige=True,
       notes="L'élément est toujours juste après « c'est ». Faire souligner : le motif "
             "est constant.")

    d.pratique('Pratique · 2 de 4', "Qui ou que ?",
               "L'élément fait-il l'action ?", [
        ("C'est Ginette ___ fournit la peinture.", "qui — Ginette fournit"),
        ("C'est le camion ___ je crains.", "que — je crains"),
        ("Ce ___ m'a plu, c'est la chambre.", "qui — la chambre m'a plu"),
        ("Ce ___ je changerais, c'est la couleur.", "que — je changerais"),
        ("Ce sont les voisins ___ font du bruit.", "qui — les voisins font"),
    ], corrige=True,
       notes="Faire nommer qui fait l'action à voix haute avant chaque réponse. Sans "
             "cela, l'exercice devient un jeu de hasard.")

    d.piege("Le piège du « ce que » à la place de « ce qui »",
            "Ce que m'a plu, c'est la chambre.",
            "Ce qui m'a plu, c'est la chambre.",
            "« La chambre m'a plu » : c'est la chambre qui fait l'action de plaire. Donc "
            "« ce qui ». Le test : après « qui », un verbe ; après « que », un sujet. "
            "Ici, « m'a plu » est un verbe.",
            notes="Erreur très fréquente parce que « me plaire » paraît passif. Faire "
                  "chercher le sujet du verbe : c'est la chambre.")

    d.piege("Le piège de la virgule oubliée",
            "Ce qui m'a plu c'est la chambre.",
            "Ce qui m'a plu, c'est la chambre.",
            "La virgule marque la pause qu'on fait naturellement en parlant. Sans elle, "
            "la phrase se lit d'un trait et l'effet de mise en évidence disparaît. Elle "
            "est obligatoire dans cette construction.",
            notes="Faire lire les deux versions à voix haute. La pause s'entend, et la "
                  "virgule la note.")

    d.pratique('Pratique · 3 de 4', "Transformez la phrase",
               "Mettez l'élément souligné en évidence.", [
        ("La chambre m'a plu.", "Ce qui m'a plu, c'est la chambre."),
        ("Je crains le camion de farine.", "Ce que je crains, c'est le camion de farine."),
        ("Ginette fournit la peinture.", "C'est Ginette qui fournit la peinture."),
        ("Je changerais la couleur des murs.",
         "Ce que je changerais, c'est la couleur des murs."),
        ("Les voisins font du bruit.", "Ce sont les voisins qui font du bruit."),
    ], corrige=True,
       notes="Faire vérifier la virgule dans les quatre premières. Elle manque presque "
             "toujours à la première rédaction.")

    d.pratique('Pratique · 4 de 4', "Dites ce qui compte pour vous",
               "Quatre phrases emphatiques sur un logement.", [
        ("Ce qui vous plaît le plus", "Ce qui m'a plu, c'est la lumière du salon."),
        ("Ce qui vous inquiète", "Ce que je crains, c'est le bruit de la rue."),
        ("Ce que vous changeriez", "Ce que je changerais, c'est la couleur de la cuisine."),
        ("Ce qui vous décide", "Ce qui me décide, c'est le prix."),
    ], corrige=True,
       notes="Faire écrire à partir des billets de C1 : chacun a déjà sa liste de ce qui "
             "plaît et de ce qui inquiète.")

    d.billet(
        "Écrivez quatre phrases emphatiques sur votre logement actuel ou souhaité.",
        exemples=[
            "Une avec « ce qui », une avec « ce que », une avec « c'est… qui », une "
            "avec « celui que ».",
            "N'oubliez pas la virgule.",
        ],
        notes="Corriger le choix entre qui et que, puis la virgule. Rendre avant C3, où "
              "ces phrases seront dites à voix haute.")

    return d.save(dossier)
