# -*- coding: utf-8 -*-
"""B5 · Un peu d'histoire, et beaucoup d'exemples
Bloc B « Défi 1 · Ce que dit le site » · couleur ambre · 75 min. Bilan du défi.
Source : exercices `t1ps` et `t1conn`, leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B5', section='ambre',
        titre="Un peu d'histoire, et beaucoup d'exemples",
        chapeau="Un temps qu'on lit sans jamais l'écrire, et quatre familles "
                "de mots qui préviennent le lecteur de ce qui vient.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 1. Elle ferme le bloc et prépare le "
                  "suivant : les connecteurs travaillés ici sont ceux que l'élève "
                  "emploiera dans son courriel et dans sa production orale.")

    d.objectifs([
        "reconnaître un passé simple à la troisième personne ;",
        "le traduire en passé composé pour comprendre ;",
        "annoncer un exemple et annoncer un avis ;",
        "rapporter une règle sans se porter garant.",
    ], notes="Le quatrième objectif est le plus utile du bloc pour la suite : "
             "« selon la page du Tribunal » met l'élève à l'abri, et c'est ce qu'il "
             "dira à son locateur en C1.")

    d.declencheur(
        'Observation', "« La Régie du logement fut créée en 1980. » Que veut dire « fut » ?",
        pistes=[
            "Est-ce du futur ? Pourquoi la ressemblance ?",
            "Comment le diriez-vous en parlant ?",
            "Où avez-vous déjà rencontré ce genre de phrase ?",
        ],
        notes="La confusion avec le futur est systématique et il faut la nommer : "
              "c'est une pure coïncidence de ressemblance. « Fut » égale « a été », "
              "et rien d'autre.")

    d.tableau('Analyse', "Le passé simple à la troisième personne",
              ['La terminaison', 'Les verbes'],
              [["-a, -èrent", "il adopta, ils adoptèrent"],
               ["-it, -irent", "il finit, ils finirent"],
               ["-ut, -urent", "il reçut, ils reçurent"],
               ["irréguliers", "il fut, il eut, il fit"]],
              cle=0,
              note="Au pluriel, le groupe -rent se voit de loin.",
              notes="Diapositive à photographier. Insister : le programme demande de "
                    "reconnaître, jamais d'écrire. Personne ne doit produire un passé "
                    "simple dans ce cours.")

    d.pratique('Pratique', "Dites-le comme on le dirait",
               "Traduisez en passé composé.", [
        ("Le législateur adopta une loi.", "il a adopté"),
        ("La Régie du logement fut créée en 1980.", "elle a été créée"),
        ("Elle devint le Tribunal administratif du logement.", "elle est devenue"),
        ("Le nouveau nom entra en vigueur en 2020.", "il est entré"),
        ("Farida lut la page trois fois.", "elle a lu"),
        ("Elle prit un crayon et nota les dates.", "elle a pris, elle a noté"),
    ], corrige=True,
       notes="Deux faits vrais dans cette liste : la Régie du logement a bien été "
             "créée en 1980 et le Tribunal administratif du logement l'a remplacée "
             "le 31 août 2020. Le dire — les élèves demandent toujours.")

    d.regle("Un passé simple se lit, ne s'écrit pas",
            "Dans un avis, dans un courriel, c'est le passé composé.",
            precision="Le passé simple survit à l'écrit : les romans, les contes, "
                      "les notices historiques, les encadrés « un peu d'histoire » "
                      "des sites officiels. Un courriel au passé simple ne fait pas "
                      "sérieux : il fait bizarre. Devant une forme courte qui vous "
                      "étonne, essayez le passé composé — si la phrase tient, "
                      "c'était un passé simple.",
            notes="Diapositive à photographier. Rassurer : ce temps ne sera jamais "
                  "exigé en production, ni dans ce cours, ni au suivant.")

    d.cartes('Connecteurs', "Quatre familles, pour un dossier", [
        ("Annoncer un exemple", "par exemple, notamment, entre autres, ainsi. Ils préviennent : ce qui suit n'est pas une règle nouvelle, c'est un cas de la règle d'avant."),
        ("Annoncer un avis", "à mon avis, selon moi, pour ma part. Ils disent : ce qui suit n'est plus le texte, c'est moi. Sans eux, un avis passe pour une affirmation de droit."),
        ("Rapporter une source", "selon la page, d'après monsieur Tardif. On rapporte sans se porter garant — exactement ce qu'il faut faire d'une règle qu'on vient de lire."),
        ("Opposer deux choses vraies", "en revanche, par contre, cependant, toutefois. Le cas le plus fréquent d'un dossier : les deux phrases sont vraies et tirent en sens contraires."),
    ], notes="Faire produire une phrase par famille, sur le dossier. Les meilleures "
             "vont au tableau et servent de modèle en C1, quand Farida devra citer la "
             "page devant son locateur.")

    d.pratique('Pratique', "Quel connecteur ?",
               "Complétez avec un mot ou une expression de la bonne famille.", [
        ("Le motif doit être sérieux. …, un défaut de paiement.", "par exemple / ainsi"),
        ("La page nomme plusieurs papiers, … l'accusé de réception.", "notamment"),
        ("…, ce refus ne tient pas debout.", "à mon avis / selon moi"),
        ("… la page du Tribunal, le silence vaut consentement.", "selon / d'après"),
        ("Il peut réclamer ses frais. …, il ne peut pas fixer un montant.", "en revanche / par contre"),
        ("Elle a gardé une copie. …, elle peut prouver la date.", "ainsi / donc"),
    ], corrige=True,
       notes="Accepter toute réponse de la bonne famille. Ce qui se corrige, c'est le "
             "choix de la famille, pas celui du mot : les synonymes se valent, la "
             "confusion entre exemple et opinion, non.")

    d.piege('Attention',
            "« Ce refus n'est pas valable. »",
            "« À mon avis, ce refus n'est pas valable. »",
            "La première phrase est une affirmation de droit, et vous n'êtes "
            "pas un tribunal. La seconde est une opinion, et personne ne peut "
            "vous la reprocher. Trois mots de différence, et tout le ton du "
            "dossier change.",
            notes="C'est le point le plus utile du bloc pour la production écrite. Le "
                  "faire écrire au tableau et le laisser là jusqu'à la fin du module.")

    d.billet(
        "Résumez le Défi 1 en trois phrases : ce que dit la page sur l'avis, le délai et le refus.",
        exemples=[
            "Une phrase par point.",
            "Employez au moins un connecteur.",
        ],
        notes="Cinq minutes. C'est le bilan du bloc et la répétition générale de la "
              "production orale de E1. Garder les billets : ils servent de point de "
              "départ à cette séance-là.")

    return d.save(dossier)
