# -*- coding: utf-8 -*-
"""D2 · À condition que… : le subjonctif, puis la comparaison
Bloc D « Défi 3 · La promesse d'achat » · couleur ambre · grammaire · 75 min.
Source : exercices `t3subj`, `t3comp` et `t3bilan` et leurs mini-leçons ;
savoirs « subjonctif présent » et « phrases subordonnées corrélatives » du
niveau 7.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="À condition que… : le subjonctif, puis la comparaison",
        chapeau="Une condition écrite parle de ce qui n'est pas encore "
                "arrivé et qui devrait arriver. C'est le terrain du "
                "subjonctif — et c'est pour ça qu'une promesse d'achat en "
                "est remplie.",
        duree='75 minutes')

    d.titre(notes="Séance dense : deux points de grammaire. Le subjonctif prend la "
                  "première heure, la comparaison la seconde. Ne pas les mélanger.")

    d.objectifs([
        "former le subjonctif présent des verbes réguliers et des cinq irréguliers ;",
        "employer le subjonctif après à condition que, pour que, bien que ;",
        "comparer deux options avec plus, moins, aussi et autant de ;",
        "employer « d'autant plus… que » pour comparer et expliquer d'un coup.",
    ], notes="Le quatrième objectif est celui qui distingue un exposé de niveau 7 d'un "
             "exposé de niveau 6 : une seule phrase de ce type suffit à l'entendre.")

    d.regle("Le subjonctif se prend sur « ils »",
            "On enlève -ent à la troisième personne du pluriel, on ajoute -e, -es, -e, -ions, -iez, -ent.",
            precision="ils prennent donne que je prenne ; ils écrivent donne que "
                      "j'écrive ; ils finissent donne que je finisse. Cinq verbes seuls "
                      "font autrement, et ce sont malheureusement les plus fréquents : "
                      "que je sois, que j'aie, que j'aille, que je fasse, que je puisse.",
            notes="Diapositive à photographier. Faire conjuguer les cinq irréguliers en "
                  "chœur, deux fois. C'est de la mémorisation, et elle se fait à voix "
                  "haute.")

    d.tableau('Analyse', "Ce qui appelle le subjonctif, et ce qui ne l'appelle pas",
              ['Ce que le mot annonce', 'Le mode'],
              [["une condition : à condition que, pourvu que", "subjonctif"],
               ["un but : pour que, afin que", "subjonctif"],
               ["une concession : bien que, quoique", "subjonctif"],
               ["une volonté : il faut que, je souhaite que", "subjonctif"],
               ["un fait établi : parce que, après que, puisque", "indicatif"]],
              cle=0,
              notes="Diapositive à photographier. La dernière rangée est celle qui "
                    "manque partout : le subjonctif ne suit pas tous les « que ».")

    d.pratique('Écriture', "Mettez le verbe au subjonctif présent",
               "Un seul mot par trou.", [
        ("La promesse tient à condition que l'acheteuse (obtenir) ___ son prêt.", "obtienne"),
        ("Il faut que l'inspection (être) ___ faite dans les dix jours.", "soit"),
        ("Le vendeur exige une réponse pour que le dossier (pouvoir) ___ avancer.", "puisse"),
        ("Bien que le fonds (avoir) ___ peu d'argent, l'immeuble est bien tenu.", "ait"),
        ("Avant que vous (prendre) ___ votre décision, lisez le procès-verbal.", "preniez"),
        ("J'accepte, à condition que la fenêtre (aller) ___ à un vitrier.", "aille"),
    ], corrige=True,
       notes="Six des huit items de `t3subj`. Faire relire chaque phrase complète "
             "après correction : c'est la phrase entière qu'on retient, pas la forme.")

    d.cartes('Analyse', "Comparer deux options", [
        ("plus / moins / aussi … que", "Avec un adjectif ou un adverbe. Acheter coûte plus cher que louer. Le condo est aussi bien situé que mon logement."),
        ("autant de … que", "Avec un nom. Je n'aurais pas autant de liberté qu'aujourd'hui. C'est la seule distinction à tenir."),
        ("meilleur, mieux, pire", "Bon donne meilleur (adjectif), bien donne mieux (adverbe). « Plus bon » et « plus bien » n'existent pas."),
        ("d'autant plus … que", "Compare et explique en même temps : la décision est d'autant plus difficile que les deux options se défendent."),
    ], notes="Faire produire une phrase de chaque carte sur le dossier de Sokhna. La "
             "quatrième est difficile : donner deux exemples de plus si nécessaire.")

    d.pratique('Écriture', "Complétez la comparaison",
               "Un seul mot par trou.", [
        ("Être propriétaire coûterait 600 $ ___ cher par mois que rester locataire.", "plus"),
        ("Louer engage ___ longtemps qu'acheter.", "moins"),
        ("Le condo est ___ bien situé que le logement de la rue Bourdages.", "aussi"),
        ("En achetant, je n'aurais pas ___ de liberté qu'aujourd'hui.", "autant"),
        ("Une entente écrite vaut ___ qu'une bonne mémoire.", "mieux"),
        ("Pour cette année, rester locataire reste la ___ solution.", "meilleure"),
    ], corrige=True,
       notes="Six des huit items de `t3comp`. Les deux derniers sont les irréguliers : "
             "y revenir en fin de séance si le temps manque.")

    d.billet(
        "Écris une phrase avec « d'autant plus… que » sur ta propre situation.",
        exemples=[
            "« La décision est d'autant plus difficile que… »",
            "Une phrase.",
        ],
        notes="Trois minutes. Ces phrases servent telles quelles dans la production "
              "orale de E1 : le dire au groupe avant qu'il écrive.")

    return d.save(dossier)
