# -*- coding: utf-8 -*-
"""C3 · « Elle disait je, vous dites elle »
Bloc C « Défi 2 · Ce que les gens ont dit » · couleur ambre · 75 min.
Source : exercice `t2pron`, mini-leçon `t2pron`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="« Elle disait je, vous dites elle »",
        chapeau="« J'ai tout perdu dans mon sous-sol », dit la résidente. "
                "Rapporté, ça devient : la résidente raconte qu'elle a tout "
                "perdu dans son sous-sol. Le je devient elle, le mon devient "
                "son. C'est la partie qu'on oublie, et c'est celle qui fait "
                "sourire.",
        duree='75 minutes')

    d.titre(notes="Ouvrir en lisant une déclaration au « je » puis en la rapportant "
                  "sans rien changer : « la résidente dit que j'ai tout perdu dans "
                  "mon sous-sol ». Laisser le groupe rire, puis demander qui a perdu "
                  "quelque chose dans cette phrase. C'est l'enseignante.")

    d.objectifs([
        "changer les pronoms quand on rapporte une parole ;",
        "changer les déterminants possessifs de la même façon ;",
        "savoir ce qui ne change pas : le temps du verbe rapporté ;",
        "régler le « vous » en regardant qui écoute.",
    ], notes="Le troisième objectif est une bonne nouvelle qu'il faut annoncer tôt : "
             "au niveau 5, on rapporte au présent, donc le temps du verbe rapporté ne "
             "bouge pas. Cela retire la moitié de la difficulté.")

    d.regle("La personne parlait d'elle ; vous, vous parlez d'elle",
            "Tout ce qui lui appartenait dans sa phrase lui appartient "
            "encore, mais vu de l'extérieur.",
            precision="« J'ai perdu mes outils. » devient : il dit qu'il a perdu "
                      "ses outils. Le je devient il, le mes devient ses. Rien "
                      "d'autre ne bouge : ni le verbe, ni l'ordre des mots.",
            notes="Diapositive à photographier. Le mot « de l'extérieur » fait "
                  "comprendre le mécanisme mieux qu'une liste : on regarde la scène "
                  "d'où l'on est, pas d'où la personne était.")

    d.tableau('Le tableau à savoir', "Ce qui change de main",
              ['Elle disait', 'Vous dites'],
              [["je", "il ou elle"],
               ["me, moi", "le, la, lui"],
               ["mon, ma, mes", "son, sa, ses"],
               ["nous", "ils ou elles"],
               ["notre, nos", "leur, leurs"]],
              cle=1,
              note="Ce tableau se récite en dix secondes et il règle la moitié des "
                   "fautes du défi 2. Le faire recopier dans le cahier.",
              notes="Faire réciter la colonne de droite en cachant celle de gauche, "
                    "puis l'inverse. C'est un des rares contenus du module qui gagne "
                    "à être mémorisé tel quel.")

    d.cartes("Ce qui ne bouge pas", "Trois bonnes nouvelles", [
        ("Le temps du verbe",
         "« J'ai tout perdu. » devient : elle raconte qu'elle a tout perdu."),
        ("L'ordre des mots",
         "Rien ne se déplace : on remplace des mots, on ne réorganise pas."),
        ("Les noms propres",
         "Sherbrooke, la rue des Peupliers, la Croix-Rouge : tels quels."),
        ("Le sens",
         "Rapporter n'est pas résumer : on garde ce que la personne a dit."),
    ], notes="La première carte est celle qui rassure. Le passé composé reste au "
             "passé composé, l'imparfait reste à l'imparfait : c'est ce qui rend le "
             "discours rapporté abordable au niveau 5.")

    d.regle("Le « vous » se règle en regardant qui écoute",
            "« Vous devez évacuer. » Si le porte-parole vous parlait à "
            "vous : il dit que nous devons évacuer.",
            precision="Si le journal rapporte une consigne adressée aux gens de la "
                      "rue, on écrit plutôt : il demande aux résidents d'évacuer. "
                      "Regardez toujours à qui la phrase était adressée avant de "
                      "choisir le pronom.",
            notes="Point plus délicat que les autres : ne pas l'imposer, le montrer. "
                  "Faire produire les deux versions de la même consigne et laisser le "
                  "groupe dire laquelle convient à quelle situation.")

    d.pratique('Écriture', "Rapportez la parole",
               "Écrivez seulement la partie qui suit « que ».", [
        ("« J'ai tout perdu dans mon sous-sol. » — la résidente raconte qu'…",
         "elle a tout perdu dans son sous-sol"),
        ("« Nous pompons depuis mercredi. » — les pompiers expliquent qu'…",
         "ils pompent depuis mercredi"),
        ("« J'ai vu trois vélos dans une remorque. » — le commerçant dit qu'…",
         "il a vu trois vélos dans une remorque"),
        ("« Notre enquête se poursuit. » — la police annonce que…",
         "leur enquête se poursuit"),
        ("« J'ai cogné à toutes les portes. » — le locataire raconte qu'…",
         "il a cogné à toutes les portes"),
        ("« Mes voisins sont sortis avant moi. » — elle dit que…",
         "ses voisins sont sortis avant elle"),
    ], corrige=True,
       notes="Exercice t2pron de l'activité. La dernière est la plus complète : elle "
             "demande de changer un déterminant et un pronom tonique dans la même "
             "phrase. Y consacrer le temps qu'il faut.")

    d.piege("Rapporter en gardant le « je »",
            "La résidente dit que j'ai tout perdu dans mon sous-sol.",
            "La résidente dit qu'elle a tout perdu dans son sous-sol.",
            "Avec le je gardé, c'est vous qui avez perdu votre sous-sol. La phrase "
            "est grammaticalement correcte : elle veut simplement dire autre chose, "
            "et personne ne vous arrêtera pour vous le signaler.",
            notes="Faire dire la version fautive à voix haute par un élève volontaire "
                  "et laisser le groupe réagir. Le rire fait le travail, à condition "
                  "qu'il porte sur la phrase et non sur la personne.")

    d.piege("Oublier le déterminant possessif",
            "Il dit qu'il a perdu mes outils.",
            "Il dit qu'il a perdu ses outils.",
            "Le pronom est corrigé, le déterminant ne l'est pas : c'est la faute qui "
            "reste quand on a compris la règle à moitié. Relisez en cherchant les "
            "mon, ma, mes, notre, nos.",
            notes="Donner la consigne de relecture ciblée : on ne relit pas tout, on "
                  "cherche une seule chose. C'est la technique de correction la plus "
                  "efficace pour les élèves de ce niveau.")

    d.billet(
        "Rapportez deux paroles du dialogue de C1, en changeant tout ce qu'il faut.",
        exemples=[
            "Une parole d'une personne, une parole d'un service.",
            "Relisez en cherchant les je, les mon et les nous qui auraient survécu.",
        ],
        notes="Ramasser. La consigne de relecture est la moitié de l'exercice : "
              "vérifier qu'elle a été suivie, et non pas seulement lue.")

    return d.save(dossier)
