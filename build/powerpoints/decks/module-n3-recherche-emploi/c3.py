# -*- coding: utf-8 -*-
"""C3 · De l'heure, par semaine, aux deux semaines.
Bloc C « Défi 2 » · couleur teal · 75 min. Écoute et calcul.
Source du module : exercice `t2chiffres` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='teal',
        titre="De l'heure, par semaine, aux deux semaines",
        chapeau="Trois petits mots collés à des chiffres, et tout le calcul "
                "en dépend. Les confondre coûte un matin, ou une illusion "
                "sur ce qu'on gagnera.",
        duree='75 minutes')

    d.titre(notes="Séance de chiffres. Prévoir une calculatrice par table, ou laisser "
                  "les téléphones ouverts : le but est la lecture, pas le calcul mental.")

    d.objectifs([
        "comprendre « de l'heure », « par semaine », « aux deux semaines » ;",
        "calculer ce que rapporte une semaine de travail ;",
        "distinguer temps plein et temps partiel ;",
        "lire un montant en dollars à voix haute.",
    ])

    d.tableau('Analyse', "Trois mots, trois choses différentes",
              ['On lit', 'Ça compte', "L'exemple"],
              [["de l'heure", "l'argent d'une seule heure", "16,50 $ de l'heure"],
               ["par semaine", "le total d'une semaine", "20 heures par semaine"],
               ["aux deux semaines", "quand la paie arrive", "payé aux deux semaines"],
               ["sur", "combien sur combien", "ouvert six jours sur sept"]],
              cle=0,
              note="16,50 $ de l'heure fois 20 heures : 330 $ par semaine, 660 $ aux deux semaines.",
              notes="Diapo à photographier. Faire le calcul au tableau avec le groupe "
                    "avant de montrer la note du bas.")

    d.regle("Moins de trente heures, c'est du temps partiel",
            "20 heures par semaine, c'est du temps partiel.",
            precision="Un temps plein tourne autour de trente-cinq heures. Entre les "
                      "deux, on parle de temps partiel. Deux emplois à temps partiel "
                      "peuvent faire un temps plein, mais rarement avec des horaires "
                      "compatibles.",
            notes="Diapo à photographier. Demander qui, dans le groupe, cherche du "
                  "temps plein et qui cherche du temps partiel, et pourquoi.")

    d.cartes("Lire l'argent en français", "Quatre habitudes du Québec", [
        ("La virgule et le signe",
         "On écrit 16,50 $ : la virgule sépare les cents, et le signe de dollar se "
         "met après le nombre, avec une espace. On dit « seize dollars cinquante »."),
        ("Le rythme de la paie",
         "Payé aux deux semaines, c'est le plus courant ici : une paie tous les quinze "
         "jours, souvent le jeudi."),
        ("Le premier chèque",
         "Il arrive rarement le premier vendredi : compter deux ou trois semaines "
         "après le premier jour. À prévoir avant de compter dessus."),
        ("Brut et net",
         "Le montant de l'annonce est brut. Des retenues sont prises avant que le "
         "chèque arrive : ce qu'on reçoit est toujours plus bas."),
    ], notes="La dernière carte surprend souvent. Ne pas entrer dans le détail des "
             "retenues : dire seulement que l'écart existe et qu'il est normal.")

    d.piege("Lire le salaire comme un total",
            "16,50 $ ? C'est ce que je gagne dans ma journée ?",
            "C'est le prix d'une heure. Une journée de 4 h en fait 66 $.",
            "« De l'heure » compte une heure et une seule. Pour savoir ce que fait la "
            "semaine, on multiplie par le nombre d'heures. C'est le calcul que Fanta "
            "fait toute seule dans le dialogue.",
            notes="Faire refaire le calcul à haute voix par deux ou trois élèves, avec "
                  "des nombres différents.")

    d.pratique('Écriture', "Complétez avec le bon petit mot",
               "Complétez avec : de, par, aux, à, sur.", [
        ("Le salaire est de 16,50 $ ___ l'heure.", "de"),
        ("C'est un poste de vingt heures ___ semaine.", "par"),
        ("La paie arrive ___ deux semaines, le jeudi.", "aux"),
        ("On travaille de neuf heures ___ une heure.", "à"),
        ("La boulangerie est ouverte six jours ___ sept.", "sur"),
        ("Vingt heures ___ semaine à 16,50 $, ça fait 330 $.", "par"),
    ], corrige=True,
       notes="Même exercice que t2chiffres dans le module. Faire relire chaque phrase "
             "complète, avec le montant dit en toutes lettres.")

    d.pratique('Calcul', "Combien fait la semaine ?",
               "Multipliez le salaire de l'heure par le nombre d'heures.", [
        ("16,00 $ de l'heure, 20 h par semaine", "320 $ par semaine, 640 $ aux deux semaines"),
        ("16,50 $ de l'heure, 20 h par semaine", "330 $ par semaine, 660 $ aux deux semaines"),
        ("16,50 $ de l'heure, 35 h par semaine", "577,50 $ par semaine, 1 155 $ aux deux semaines"),
        ("20,00 $ de l'heure, 20 h par semaine", "400 $ par semaine, 800 $ aux deux semaines"),
        ("20,00 $ de l'heure, 35 h par semaine", "700 $ par semaine, 1 400 $ aux deux semaines"),
    ], corrige=True,
       notes="Rappeler à la fin que tous ces montants sont bruts. Ne pas laisser le "
             "groupe repartir avec le chiffre du haut en tête.")

    d.pratique('Oral', "Dites le montant à voix haute",
               "Chacun lit un montant, en toutes lettres.", [
        ("16,50 $", "seize dollars cinquante"),
        ("330 $ par semaine", "trois cent trente dollars par semaine"),
        ("1 155 $", "mille cent cinquante-cinq dollars"),
        ("20 h par semaine", "vingt heures par semaine"),
        ("de 9 h à 13 h", "de neuf heures à treize heures"),
        ("six jours sur sept", "six jours sur sept"),
    ], corrige=True, cols=2,
       notes="Les nombres se disent mal quand on ne les dit jamais. Faire le tour du "
             "groupe : personne ne passe son tour.")

    d.billet(
        "Combien fait une semaine à 17 $ de l'heure, 20 heures par semaine ?",
        exemples=[
            "Écrivez le calcul et le résultat.",
            "Puis le montant aux deux semaines.",
        ],
        notes="Deux minutes. Réponse : 340 $ par semaine, 680 $ aux deux semaines. "
              "C'est le salaire de la boulangerie de Gilles.")

    return d.save(dossier)
