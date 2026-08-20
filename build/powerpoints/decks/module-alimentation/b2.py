# -*- coding: utf-8 -*-
"""B2 · Du, de la, des.
Bloc B · couleur ambre (écriture) · 90 min.
Source : mini-leçon `t1part`, exercice `t1part`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre='Du, de la, des',
        chapeau="« Je voudrais du poulet. » Trois lettres qui changent tout : "
                "ni « le poulet », ni « un poulet », mais une certaine "
                "quantité, sans dire laquelle.",
        duree='90 minutes')

    d.titre(notes="Séance de grammaire longue, et la plus rentable du module : cette forme "
                  "revient à chaque phrase d'une épicerie.")

    d.objectifs([
        "employer du, de la, de l' et des selon le nom ;",
        "savoir que la quantité n'y change rien ;",
        "employer de après une négation ;",
        "employer de après une quantité précise.",
    ])

    d.tableau('Analyse', "Les quatre formes",
              ['Devant', 'La forme', 'Exemple'],
              [["un masculin", "du", "du poulet"],
               ["un féminin", "de la", "de la truite"],
               ["une voyelle", "de l'", "de l'eau"],
               ["un pluriel", "des", "des poitrines"]],
              cle=1,
              note="C'est le nom qui décide, jamais la quantité.",
              notes="Diapo centrale. Faire recopier. La note est ce qui débloque le plus "
                    "d'élèves : ils cherchent souvent à faire varier la forme selon la "
                    "quantité voulue.")

    d.regle('À la forme négative : toujours « de »',
            "Les quatre formes se réduisent à une seule.",
            precision="« Je prends du riz » devient « je ne prends pas <b>de</b> riz ». "
                      "« Il y a des tomates » devient « il n'y a pas <b>de</b> tomates ». "
                      "Cette règle n'a pas d'exception.",
            notes="Écrire les deux paires au tableau. C'est une des rares règles du "
                  "français sans exception : le dire, ça encourage.")

    d.regle('Après une quantité précise : « de » aussi',
            "Dès qu'il y a un poids, un volume ou un nombre.",
            precision="« du bœuf haché » devient « une livre <b>de</b> bœuf haché ». "
                      "« du jambon » devient « deux cents grammes <b>de</b> jambon ». "
                      "Aussi : un kilo <b>de</b> riz, un litre <b>d'</b>eau, une douzaine "
                      "<b>d'</b>œufs, beaucoup <b>de</b> monde.",
            notes="C'est la partie qui demande le plus de pratique. Faire produire cinq "
                  "exemples par cinq élèves.")

    d.piege("Employer l'article défini",
            "Je voudrais le poulet, s'il vous plaît.",
            "Je voudrais du poulet, s'il vous plaît.",
            "« Le poulet » désigne un poulet précis, que les deux personnes connaissent — "
            "celui qui est sur le comptoir, par exemple. Au moment de commander, on veut "
            "une certaine quantité, sans dire laquelle : c'est <b>du</b>.",
            notes="La faute se comprend, mais elle sonne étrange. Beaucoup de langues "
                  "n'ont pas cette distinction.")

    d.pratique('Pratique · 1 de 2', "Quelle forme ?",
               "Complétez avec du, de la, de l', des ou de.", [
        ("Je voudrais ___ poulet, s'il vous plaît.", "du"),
        ("Est-ce qu'il y a ___ truite aujourd'hui ?", "de la"),
        ("Elle achète ___ poitrines de poulet.", "des"),
        ("Il me faut ___ eau tiède pour diluer le produit.", "de l'"),
        ("Je ne prends pas ___ riz aujourd'hui.", "de"),
        ("Je voudrais une livre ___ bœuf haché.", "de"),
    ], corrige=True,
       notes="Faire dire à voix haute, pour chaque ligne, ce qui décide : le genre, la "
             "négation, ou la quantité.")

    d.pratique('Pratique · 2 de 2', "Mettez à la forme négative",
               "Récrivez chaque phrase en la niant.", [
        ("Je prends du riz.", "Je ne prends pas de riz."),
        ("Il y a des tomates.", "Il n'y a pas de tomates."),
        ("Elle achète de la truite.", "Elle n'achète pas de truite."),
        ("Il reste du bœuf haché.", "Il ne reste pas de bœuf haché."),
        ("Je veux de l'eau.", "Je ne veux pas d'eau."),
    ], corrige=True, cols=1,
       notes="La dernière ligne demande « d' » devant la voyelle. Le faire remarquer.")

    d.cartes('Trois formes qui se ressemblent', "Et qui ne disent pas la même chose", [
        ("« Je voudrais du poulet. »",
         "Une certaine quantité de poulet, sans préciser. C'est ce qu'on dit au comptoir."),
        ("« Je voudrais le poulet. »",
         "Un poulet précis, que la personne voit — celui qui est devant elle."),
        ("« Je voudrais un poulet. »",
         "Un poulet entier, compté comme une unité. C'est autre chose encore."),
    ], notes="Faire jouer les trois phrases au comptoir. Les réactions de la personne "
             "seraient différentes à chaque fois : c'est ce qui rend la distinction "
             "concrète.")

    d.billet(
        "Écrivez votre liste d'épicerie en phrases complètes.",
        exemples=[
            "Six produits, en employant du, de la, de l' et des.",
            "Ajoutez deux phrases négatives : ce que vous ne prenez pas cette semaine.",
        ],
        notes="Corriger individuellement. Cette liste est le brouillon de la production "
              "écrite de E1 — la rendre avant cette séance.")

    return d.save(dossier)
