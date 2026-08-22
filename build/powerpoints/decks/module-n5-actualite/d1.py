# -*- coding: utf-8 -*-
"""D1 · « Moi, ce qui me surprend, c'est le nombre »
Bloc D « Défi 3 · Ce que j'en pense » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3a` et `t3fait`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-actualite/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="« Moi, ce qui me surprend, c'est le nombre »",
        chapeau="Trente vélos volés dans le quartier en un mois, presque "
                "tous dans des cabanons laissés ouverts. Une fois la "
                "nouvelle racontée, il reste la vraie conversation : ce que "
                "ça vous fait. Et là, deux choses comptent — annoncer son "
                "avis comme un avis, et savoir répondre à qui pense "
                "autrement.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 3. Commencer par annoncer le chiffre — trente "
                  "vélos en un mois — et demander au groupe sa réaction, sans "
                  "consigne. Les réponses spontanées mêlent presque toujours faits et "
                  "opinions : c'est le matériau de la séance.")

    d.objectifs([
        "annoncer un avis comme un avis, et non comme un fait ;",
        "distinguer un fait vérifiable d'un jugement ;",
        "justifier une opinion avec « parce que » ;",
        "accorder à l'autre ce qu'il a de juste avant d'objecter.",
    ], notes="Le quatrième objectif est celui qui rend la conversation possible. Le "
             "montrer dans le dialogue : Marisol accorde deux fois à Sylvain avant de "
             "tourner, et c'est pour ça qu'il finit par l'écouter.")

    d.declencheur(
        'Observation', "Une porte de cabanon grande ouverte. "
                       "Qu'est-ce qui est un fait, ici ?",
        image=IMG + 'cabanon-ouvert.jpg',
        pistes=[
            "La porte est ouverte : ça se voit, c'est un fait.",
            "Trente vélos ont disparu en un mois : ça se compte, c'est un fait.",
            "« C'est de la négligence » : ça ne se vérifie pas, c'est un jugement.",
            "« Il faudrait des caméras dans les ruelles » : c'est une opinion aussi.",
        ],
        notes="Les quatre pistes suffisent à installer le tri. Insister sur la "
              "troisième : « négligence » est un mot de jugement, et personne ne peut "
              "aller le vérifier nulle part.")

    d.dialogue('Dialogue · 1 de 5', "Trente ? Voyons donc", [
        ("MARISOL", "Sylvain, trente vélos volés dans le quartier en un "
                    "mois.", True),
        ("SYLVAIN", "Trente ? Voyons donc. Volés où ?", True),
        ("MARISOL", "Dans des cabanons et des garages laissés ouverts, "
                    "presque tous.", True),
        ("SYLVAIN", "Bon. Ça, c'est de la négligence, pas du vol.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="La quatrième réplique est une opinion présentée comme un fait, et elle "
             "arrive au bout de quinze secondes. La faire relever : c'est exactement "
             "ce que la séance apprend à repérer.")

    d.dialogue('Dialogue · 2 de 5', "Une porte ouverte n'est pas une invitation", [
        ("MARISOL", "Je ne suis pas d'accord avec toi. Une porte ouverte, "
                    "ce n'est pas une invitation.", True),
        ("SYLVAIN", "Peut-être. Mais barre ta porte, et il n'arrive rien.", True),
        ("MARISOL", "C'est vrai que ça aide. Par contre, ça n'excuse pas "
                    "celui qui entre.", True),
        ("SYLVAIN", "La police dit quoi, elle ?", True),
    ], notes="La troisième réplique est le modèle du désaccord poli : « c'est vrai "
             "que… par contre… ». La faire répéter à voix haute par tout le groupe. "
             "C'est la formule évaluée en D2 et en E1.")

    d.dialogue('Dialogue · 3 de 5', "Noter le numéro de série", [
        ("MARISOL", "Elle demande aux gens de noter le numéro de série de "
                    "leur vélo.", True),
        ("SYLVAIN", "Un numéro. Ça ne ramènera jamais un vélo, ça.", True),
        ("MARISOL", "Moi, ce qui me surprend, c'est qu'un vélo retrouvé "
                    "sans numéro reste à la police.", True),
        ("SYLVAIN", "Ah oui ? Ils le gardent ?", True),
    ], notes="La troisième réplique porte la formule du défi. Faire remarquer sa "
             "construction : le « moi » qui annonce, le sentiment qui se nomme, puis "
             "ce dont il s'agit. Elle se démontera en D2.")

    d.dialogue('Dialogue · 4 de 5', "Tu marques un point", [
        ("MARISOL", "Ils ne savent pas à qui le rendre. C'est pour ça que "
                    "le numéro sert.", True),
        ("SYLVAIN", "Ça, je ne le savais pas. Tu marques un point.", True),
        ("MARISOL", "Et il y a un témoin : un commerçant a vu trois vélos "
                    "dans une remorque.", True),
        ("SYLVAIN", "Tard le soir, j'imagine ?", True),
    ], notes="« Tu marques un point » vaut d'être relevé : dans une discussion, "
             "reconnaître qu'on a appris quelque chose n'est pas une défaite. Le dire "
             "explicitement — beaucoup d'élèves croient l'inverse.")

    d.dialogue('Dialogue · 5 de 5', "Tu me fais lire le journal", [
        ("MARISOL", "Vers minuit. Il l'a signalé le lendemain matin.", True),
        ("SYLVAIN", "C'est plate à dire, mais tu me fais lire le journal "
                    "sans que je le lise.", False),
    ], notes="Clôture du dernier dialogue du module. La réplique de Sylvain dit la "
             "réussite de Marisol : elle lui a transmis une nouvelle complète, avec "
             "ses sources et son avis, sans qu'il ait ouvert le journal.")

    d.regle("Annoncer son avis comme un avis",
            "Moi, ce qui me surprend, c'est le nombre.",
            precision="On annonce qu'on parle de soi, on nomme ce qu'on ressent, "
                      "puis on dit de quoi. La personne en face sait tout de suite "
                      "que ce n'est pas un fait du journal, et elle vous écoute "
                      "autrement.",
            notes="Diapositive à photographier. Elle sera démontée pièce par pièce en "
                  "D2 ; ici, on l'installe entière et on la fait répéter.")

    d.tableau('Le tri', "Un fait, ou une opinion ?",
              ['La phrase', 'Le test'],
              [["Trente vélos ont été volés en un mois.", "On compte : un fait"],
               ["C'est de la négligence.", "On ne vérifie pas : une opinion"],
               ["La police recommande de noter le numéro.", "C'est écrit : un fait"],
               ["La police n'en fait pas assez.", "« pas assez » juge : une opinion"],
               ["Il faudrait des caméras dans les ruelles.", "« il faudrait » : une opinion"]],
              cle=1,
              notes="Une seule question suffit : est-ce qu'on peut aller vérifier ? "
                    "Faire remarquer les mots qui trahissent l'opinion — trop, pas "
                    "assez, il faudrait, inacceptable, c'est normal.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la discussion avec Sylvain.", [
        ("Une trentaine de vélos ont été volés en un mois.", "vrai"),
        ("Presque tous les vols ont eu lieu dans des cabanons ouverts.", "vrai"),
        ("Marisol est d'accord quand Sylvain parle de négligence.", "faux — elle n'est pas d'accord"),
        ("La police demande de noter le numéro de série.", "vrai"),
        ("Un vélo retrouvé sans numéro est rendu tout de suite.", "faux — il reste à la police"),
        ("Un commerçant a vu trois vélos dans une remorque vers minuit.", "vrai"),
        ("Le commerçant a signalé la chose le soir même.", "faux — le lendemain matin"),
        ("Sylvain reconnaît à la fin qu'il a appris quelque chose.", "vrai"),
    ], corrige=True,
       notes="Exercice t3a de l'activité. Enchaîner ensuite avec t3fait, le tri entre "
             "fait et opinion : le tableau projeté plus haut sert de corrigé partiel.")

    d.billet(
        "Écrivez un fait tiré de la nouvelle, puis votre avis sur ce fait.",
        exemples=[
            "Le fait : quelque chose qu'on peut aller vérifier.",
            "L'avis : commencez par « Moi, ce qui me… » ou par « Je trouve que… ».",
        ],
        notes="Ramasser. Beaucoup mélangeront encore les deux : c'est normal à ce "
              "stade, et ces billets ouvrent parfaitement la séance D2.")

    return d.save(dossier)
