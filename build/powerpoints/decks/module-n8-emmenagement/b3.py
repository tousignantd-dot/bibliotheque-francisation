# -*- coding: utf-8 -*-
"""B3 · Le subjonctif présent, et ce qui le déclenche
Bloc B « Défi 1 · Ce qui est couvert » · couleur ambre · 75 min. Écriture.
Source du module : l'exercice `t1subj` et la mini-leçon du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Le subjonctif présent, et ce qui le déclenche",
        chapeau="« Il faut que je déclare », « j'aimerais que la décision me "
                "parvienne », « bien que la clause existe ». Trois emplois, "
                "et vous avez de quoi mener tout le défi 2.",
        duree='75 minutes')

    d.titre(notes="Le programme du niveau 8 nomme explicitement le subjonctif "
                  "pour la nécessité et l'obligation. Les deux autres emplois "
                  "— le souhait et la concession — sont ceux dont la "
                  "réclamation a besoin.")

    d.objectifs([
        "former le subjonctif présent à partir de la troisième personne du pluriel ;",
        "conjuguer les six irréguliers sans hésiter ;",
        "reconnaître ses trois déclencheurs utiles ici ;",
        "ne pas le mettre après « même si », « après que » et « j'espère que ».",
    ], notes="Le quatrième objectif prendra le tiers de la séance : c'est là "
             "que se font toutes les fautes, et elles sont audibles.")

    d.declencheur(
        'Pour commencer', "« Je sais qu'elle vient. » « Je veux qu'elle… » — "
                          "terminez la phrase.",
        pistes=[
            "Pourquoi la deuxième forme est-elle différente ?",
            "Dans quel cas est-on sûr qu'elle est venue ?",
            "Est-ce que « je veux qu'elle vienne » dit qu'elle est venue ?",
        ],
        notes="Ne pas nommer le mode avant d'avoir la réponse à la troisième "
              "piste. Le subjonctif ne situe rien dans le temps : il dit "
              "comment on considère le fait, et c'est ça qui doit être compris "
              "d'abord.")

    d.regle("Troisième personne du pluriel, moins -ent, plus les terminaisons",
            "ils écrivent devient : que j'écrive · ils finissent devient : que tu finisses · ils envoient devient : qu'elle envoie",
            precision="« Nous » et « vous » se prennent sur l'imparfait : que "
                      "nous envoyions, que vous envoyiez. Six verbes "
                      "seulement échappent à tout.",
            notes="Diapositive à photographier. Faire fabriquer trois formes "
                  "au tableau à partir de trois verbes donnés par la classe, "
                  "avant de passer aux irréguliers.")

    d.tableau('Analyse', "Les six irréguliers, en entier",
              ['Le verbe', 'que je… / que nous…'],
              [["être", "que je sois · que nous soyons"],
               ["avoir", "que j'aie · que nous ayons"],
               ["aller", "que j'aille · que nous allions"],
               ["faire", "que je fasse · que nous fassions"],
               ["pouvoir", "que je puisse · que nous puissions"],
               ["savoir", "que je sache · que nous sachions"]],
              cle=0,
              notes="Diapositive à photographier. Les faire dire à voix haute "
                    "en chœur, deux fois. Ils reviennent dans huit phrases "
                    "sur dix, et les autres verbes se déduisent de la règle.")

    d.cartes('Analyse', "Trois déclencheurs, trois usages", [
        ("La nécessité", "il faut que… · il est nécessaire que… · j'exige que…"),
        ("Le souhait poli", "j'aimerais que… · je souhaite que… · il vaudrait mieux que…"),
        ("La concession", "bien que… · quoique… · à moins que…"),
        ("Le doute", "je ne crois pas que… — le plus poli des désaccords."),
    ], cols=2,
       notes="Les quatre sont dans le module. Faire produire une phrase de "
             "chaque catégorie, à l'oral, en partant de la situation d'Amira.")

    d.piege('Attention',
            "« Même si la clause soit claire »",
            "« Même si la clause est claire »",
            "« Bien que » veut le subjonctif, « même si » veut l'indicatif — "
            "et les deux disent pourtant la même chose. C'est la confusion la "
            "plus fréquente du niveau, et elle s'entend. Même règle pour "
            "« après que », qui prend l'indicatif parce que l'événement a eu "
            "lieu, contrairement à « avant que ».",
            notes="Faire répéter la paire à voix haute : bien que… soit, même "
                  "si… est. C'est un couple, il s'apprend comme un couple.")

    d.pratique('Pratique', "Mettez le verbe au subjonctif présent",
               "Écrivez seulement le verbe.", [
        ("Il faut que je ___ (déclarer) le sinistre aujourd'hui.", "déclare"),
        ("J'aimerais que la décision me ___ (parvenir) par écrit.", "parvienne"),
        ("Bien que la clause ___ (exister), elle ne vise que le transport.", "existe"),
        ("Il est nécessaire que vous ___ (avoir) une preuve datée.", "ayez"),
        ("Je ne crois pas que cette exclusion ___ (pouvoir) s'appliquer.", "puisse"),
        ("Pour que le dossier ___ (avancer), il manque l'évaluation.", "avance"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t1subj` du module, dans sa version projetée. "
             "Après chaque correction, redemander quel mot a déclenché le "
             "subjonctif : c'est le repère qui reste.")

    d.billet(
        "Écris une phrase avec « il faut que » et une avec « bien que », sur ton déménagement.",
        exemples=[
            "Deux phrases séparées, pas une seule.",
            "Souligne le verbe au subjonctif dans chacune.",
        ],
        notes="Cinq minutes. Ramasser : les erreurs portent presque toujours "
              "sur « bien que », parce que la concession est une idée plus "
              "difficile que la nécessité.")

    return d.save(dossier)
