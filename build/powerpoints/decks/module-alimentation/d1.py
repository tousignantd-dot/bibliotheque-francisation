# -*- coding: utf-8 -*-
"""D1 · Les trois lignes qui comptent.
Bloc D « Défi 3 · L'étiquette et le mode d'emploi » · couleur acier · 75 min.
Source : mini-leçon `t3etiq`, dialogue `t3`, exercices `t3vf` et `t3etiq`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre='Les trois lignes qui comptent',
        chapeau="Un tableau de valeur nutritive contient une quarantaine de "
                "chiffres. Trois seulement servent au quotidien. Le reste ne "
                "se lit que si on cherche quelque chose de précis.",
        duree='75 minutes')

    d.titre(notes="Apporter trois emballages du même type de produit, marques différentes. "
                  "Toute la séance se fait sur du vrai.")

    d.objectifs([
        "trouver la portion, le sodium et les sucres sur n'importe quel tableau ;",
        "employer la colonne du pourcentage pour juger vite ;",
        "comparer deux marques correctement ;",
        "distinguer les deux dates.",
    ])

    d.dialogue('Dialogue · 1 de 2', "Trois lignes, pas quarante", [
        ("CLAUDE", "Tu regardes toujours les étiquettes ? Moi, je n'y comprends rien.", False),
        ("FARIDA", "J'ai appris à regarder trois lignes seulement. Le reste, je le saute.", True),
        ("CLAUDE", "Lesquelles ?", False),
        ("FARIDA", "La portion, en haut. Tout le tableau parle de cette portion-là, pas du contenant.", True),
    ], consigne="Écoutez, puis cherchez la portion sur les emballages distribués.",
       notes="Faire chercher immédiatement sur les vrais emballages. La portion est souvent "
             "beaucoup plus petite que ce que les gens croient.")

    d.dialogue('Dialogue · 2 de 2', "Les dates", [
        ("FARIDA", "Ensuite le sodium, et le sucre. Ce sont les deux qui varient le plus d'une marque à l'autre.", True),
        ("CLAUDE", "Et la date, tu la regardes où ?", False),
        ("FARIDA", "« Meilleur avant », en avant ou sur le dessus. Ce n'est pas une date de danger, c'est une date de qualité.", True),
        ("FARIDA", "« Date limite d'utilisation », ça, c'est sérieux.", True),
    ], notes="La distinction entre les deux dates est le point le plus utile de la séance. "
             "Y consacrer du temps.")

    d.tableau('Analyse', "Les trois lignes",
              ['La ligne', 'Ce qu\'elle dit'],
              [["La portion, en haut", "tous les chiffres valent pour elle"],
               ["Le sodium", "la ligne qui varie le plus entre marques"],
               ["Les sucres", "l'autre ligne à surveiller"],
               ["La colonne % à droite", "5 % ou moins = peu · 15 % ou plus = beaucoup"]],
              cle=0,
              note="La première ligne conditionne toutes les autres.",
              notes="Diapo centrale. Faire recopier. Le repère du pourcentage est officiel "
                    "et figure sur les documents de Santé Canada.")

    d.regle('La portion décide de tout',
            "Deux marques qui affichent des portions différentes ne se comparent pas.",
            precision="Une marque annonce 30 g par portion, l'autre 55 g. Les chiffres de "
                      "sodium ne sont pas comparables tels quels : il faut d'abord ramener "
                      "au même poids. C'est le piège le plus fréquent — et il est parfois "
                      "voulu.",
            notes="Faire vérifier sur les emballages apportés. Il arrive que les portions "
                  "diffèrent entre deux marques du même produit.")

    d.regle('Deux dates, deux sens',
            "« Meilleur avant » est une date de qualité ; « date limite d'utilisation » est une date de sécurité.",
            precision="Après « meilleur avant », le goût ou la texture changent, mais "
                      "l'aliment n'est pas dangereux. « Date limite d'utilisation » est "
                      "rare : préparations pour nourrissons, quelques produits frais. "
                      "Après celle-là, on ne consomme pas.",
            notes="Diapo à photographier. Confondre les deux fait jeter beaucoup de "
                  "nourriture encore bonne.")

    d.piege('Comparer sans regarder la portion',
            "Marque A : 240 mg. Marque B : 180 mg. B est moins salée.",
            "A : 240 mg par 100 g. B : 180 mg par 55 g. B est deux fois plus salée.",
            "Sans ramener à la même portion, la comparaison est fausse — et elle peut "
            "l'être dans les deux sens. La première ligne du tableau n'est pas un détail : "
            "c'est la clé de lecture de tout le reste.",
            notes="Faire le calcul au tableau. C'est le moment où le groupe comprend "
                  "pourquoi la portion est en haut.")

    d.pratique('Pratique · 1 de 2', "Où je regarde ?",
               "Dites où se trouve la réponse.", [
        ("« Ces chiffres valent pour combien ? »", "la portion, tout en haut"),
        ("« Est-ce que c'est salé ? »", "la ligne du sodium"),
        ("« Est-ce que c'est sucré ? »", "la ligne des sucres"),
        ("« 15 %, c'est beaucoup ? »", "oui — 15 % ou plus, c'est beaucoup"),
        ("« Est-ce encore bon après la date ? »", "oui, si c'est « meilleur avant »"),
    ], corrige=True, cols=1,
       notes="Faire chercher sur les emballages avant de corriger.")

    d.pratique('Pratique · 2 de 2', "Comparez deux marques",
               "Laquelle choisir, et pourquoi ?", [
        ("A : 240 mg de sodium / portion de 100 g · B : 80 mg / 100 g", "B — trois fois moins de sel"),
        ("A : 12 g de sucre / 250 ml · B : 5 g / 250 ml", "B — même portion, moins de sucre"),
        ("A : 200 mg / 100 g · B : 150 mg / 55 g", "A — B est presque deux fois plus salée au poids"),
    ], corrige=True, cols=1,
       notes="La troisième ligne est celle qui compte. Prendre le temps de la faire "
             "calculer.")

    d.cartes('Ce qu\'on peut sauter', "Le reste du tableau", [
        ("Les calories",
         "Utiles pour un suivi particulier, rarement pour choisir entre deux marques du "
         "même produit."),
        ("Les vitamines et minéraux",
         "En bas du tableau. Ils ne varient presque pas d'une marque à l'autre."),
        ("La liste des ingrédients",
         "Séparée du tableau. Elle sert surtout aux allergies — et là, elle est "
         "essentielle : les allergènes y sont en gras."),
    ], notes="La troisième carte mérite une minute : pour une allergie, c'est la liste "
             "d'ingrédients qu'il faut lire, pas le tableau.")

    d.billet(
        "Comparez deux marques du même produit et écrivez quatre phrases.",
        exemples=[
            "La portion de chacune, le sodium, les sucres, votre choix.",
            "Employez une comparaison : plus salée que, la moins sucrée des deux.",
        ],
        notes="Devoir concret, à faire à l'épicerie ou avec deux emballages de la maison.")

    return d.save(dossier)
