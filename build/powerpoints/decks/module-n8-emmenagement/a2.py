# -*- coding: utf-8 -*-
"""A2 · Ce que la voix dit et que les mots ne disent pas
Bloc A « Je découvre » · couleur indigo · 60 min. Phonétique.
Source du module : l'exercice `prInto` et la mini-leçon du même nom.

Le seul savoir de phonétique du niveau 8 est l'intonation expressive. Il n'y a
donc **aucun son à opposer** dans cette séance, contrairement à toutes les
autres séances de graphie-phonie du dépôt : on n'y compare pas deux voyelles,
on y écoute quatre mélodies. Les sons se nomment par leurs lettres partout
ailleurs ; ici, les mélodies se décrivent par leur mouvement — monte d'un
coup, freine, descend et appuie, tombe dès la première syllabe.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Ce que la voix dit et que les mots ne disent pas",
        chapeau="Une même phrase de six mots peut dire la surprise, la "
                "déception ou la détermination. Au téléphone, c'est tout ce "
                "que l'autre a pour vous juger.",
        duree='60 minutes')

    d.titre(notes="Séance de graphie-phonie du module, et elle ne ressemble à "
                  "aucune autre : le programme du niveau 8 ne demande plus "
                  "qu'une chose à l'oreille, l'intonation expressive. Pas de "
                  "paire de sons à opposer, donc pas de tableau de lettres.")

    d.objectifs([
        "reconnaître quatre intentions à la seule mélodie de la voix ;",
        "produire la surprise, la déception et la volonté ;",
        "entendre qu'une voix qui monte transforme une affirmation en question ;",
        "choisir trois phrases à travailler avant un appel important.",
    ], notes="Objectif de production, pas de reconnaissance seulement. Prévoir "
             "que chaque personne dise au moins trois phrases à voix haute.")

    d.declencheur(
        'Pour commencer', "« Cent vingt dollars. » Dites-le trois fois, en "
                          "changeant seulement la voix.",
        pistes=[
            "Une fois comme si vous étiez étonné.",
            "Une fois comme si vous étiez déçu.",
            "Une fois comme si vous refusiez.",
        ],
        notes="Faire faire par trois personnes différentes, debout. Ne pas "
              "expliquer avant : l'exercice fonctionne parce que la classe "
              "entend la différence sans qu'on l'ait nommée.")

    d.tableau('Analyse', "Quatre mélodies, quatre mouvements",
              ['L\'intention', 'Ce que fait la voix'],
              [["la surprise", "monte d'un coup sur les deux dernières syllabes"],
               ["la déception", "tombe dès la première syllabe et ne remonte pas"],
               ["la volonté", "descend, ralentit, et détache chaque mot"],
               ["l'incompréhension", "freine au milieu, avec un silence avant le mot en cause"]],
              cle=0,
              note="Aucun symbole à apprendre : ces mélodies s'entendent et se répètent.",
              notes="Diapositive à photographier. Faire tracer le mouvement "
                    "avec la main pendant qu'on prononce : le geste ancre la "
                    "mélodie mieux que la description.")

    d.cartes('Écoute', "Une phrase par intention", [
        ("Surprise", "« Cent vingt dollars pour le meuble de ma mère ? »"),
        ("Déception", "« Ah. Je pensais que l'inventaire réglait la question. »"),
        ("Volonté", "« Ce point-là, je le conteste, et je vais vous dire pourquoi. »"),
        ("Incompréhension", "« Le mot “subrogation”… vous l'entendez comment ? »"),
    ], cols=2,
       notes="Faire écouter l'audio du module, puis faire répéter en "
             "exagérant. L'exagération est ce qui fait entrer une mélodie "
             "dans l'oreille ; on rabat ensuite tout seul.")

    d.regle("Une voix qui monte transforme une affirmation en question",
            "« Je conteste ce point » dit en montant devient une demande de permission.",
            precision="C'est le défaut le plus fréquent, et il vient de la "
                      "prudence : on n'ose pas conclure. Quand vous affirmez, "
                      "la voix descend.",
            notes="Diapositive à photographier. Faire dire la même phrase "
                  "montante puis descendante, par la même personne, et "
                  "demander à la classe laquelle elle croirait.")

    d.piege('Attention',
            "parler d'une voix parfaitement égale pendant tout un appel",
            "varier la mélodie sur les trois phrases importantes, pas plus",
            "Une voix plate se lit comme de l'indifférence, jamais comme du "
            "calme. Personne ne demande de jouer la comédie : trois phrases "
            "variées dans un appel de vingt minutes suffisent à changer "
            "l'impression qu'on laisse.",
            notes="Rassurer : beaucoup d'élèves parlent plat par prudence, "
                  "pas par froideur, et ils l'ignorent complètement.")

    d.pratique('Pratique', "Quelle intention la voix porte-t-elle ?",
               "Écoutez, puis dites : surprise, déception ou volonté.", [
        ("« Comment ça, la rampe était déjà croche ? »", "surprise"),
        ("« Bon. Tant pis pour les albums, alors. »", "déception"),
        ("« Je tiens à recevoir la décision par écrit. »", "volonté"),
        ("« Vous êtes le premier à me parler de soixante cents la livre ! »", "surprise"),
        ("« Six ans que je gardais ce vaisselier pour rien. »", "déception"),
        ("« J'irai jusqu'à la révision s'il le faut. »", "volonté"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `prInto` du module, dans sa version projetée. "
             "Faire écouter chaque réplique deux fois avant de demander la "
             "réponse, et faire répéter après la correction.")

    d.billet(
        "Écris la phrase que tu diras le plus fermement dans ton prochain appel difficile.",
        exemples=[
            "Une seule phrase, dix mots au maximum.",
            "Souligne le mot sur lequel ta voix va descendre.",
        ],
        notes="Trois minutes. Faire dire trois d'entre elles à voix haute "
              "avant de sortir : c'est la seule façon de vérifier que la "
              "mélodie descendante est comprise.")

    return d.save(dossier)
