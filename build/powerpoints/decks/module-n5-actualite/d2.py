# -*- coding: utf-8 -*-
"""D2 · « C'est vrai que… Par contre… »
Bloc D « Défi 3 · Ce que j'en pense » · couleur ambre · 75 min.
Source : exercices `t3fait`, `t3disl`, `t3imp`, `t3nuance`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="« C'est vrai que… Par contre… »",
        chapeau="Quand l'autre n'est pas d'accord, ne le contredisez pas "
                "d'un bloc. Donnez-lui ce qu'il a de juste, puis tournez. "
                "C'est plus poli, c'est plus efficace, et la conversation "
                "continue au lieu de bloquer.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 3 et dernière séance de contenu du module. "
                  "Elle réunit trois choses : la mise en relief, les phrases "
                  "impersonnelles, et la réponse à un désaccord. Garder la dernière "
                  "moitié pour l'exercice t3nuance, qui est le plus exigeant du "
                  "module.")

    d.objectifs([
        "construire une phrase de mise en relief : moi, ce qui me…, c'est… ;",
        "employer une phrase impersonnelle pour ne montrer personne du doigt ;",
        "accorder à l'autre ce qu'il a de juste, puis objecter ;",
        "justifier son avis avec « parce que ».",
    ], notes="Les quatre objectifs sont les quatre critères de la production orale de "
             "E1. Les projeter au début et les relire à la fin de la séance.")

    d.regle("Deux moules, à apprendre tels quels",
            "Ce qui me + verbe, c'est + un nom. · Ce que je + verbe, "
            "c'est + un nom.",
            precision="On emploie « ce qui » quand le morceau est le sujet du "
                      "verbe : ce qui me surprend. On emploie « ce que » quand il "
                      "en est le complément : ce que je trouve inquiétant. Et quand "
                      "la suite est une phrase entière, c'est « c'est que ».",
            notes="Diapositive à photographier. Faire produire quatre phrases à "
                  "l'oral, deux avec « ce qui », deux avec « ce que », avant de "
                  "passer à l'exercice.")

    d.tableau('La mise en relief', "Un nom, ou une phrase ?",
              ['La suite', 'Ce qu\'on emploie'],
              [["un nom", "Ce qui me surprend, c'est le nombre."],
               ["une phrase", "Ce qui me dérange, c'est que les cabanons restent ouverts."],
               ["sujet du verbe", "Ce qui me choque… (ce qui = sujet de choquer)"],
               ["complément du verbe", "Ce que je trouve inquiétant… (ce que = complément)"],
               ["le « moi » du début", "Il dit : voici mon point de vue, il n'engage que moi."]],
              cle=1,
              notes="La dernière ligne mérite une minute : le « moi » détaché est "
                    "presque obligatoire quand on répond à quelqu'un qui vient de "
                    "donner son avis. Sans lui, la phrase a l'air d'une correction.")

    d.cartes("Cinq entrées, une même fonction", "Prévenir que c'est vous qui parlez", [
        ("À mon avis…",
         "La plus neutre, et celle qui passe partout, à l'oral comme à l'écrit."),
        ("Personnellement…",
         "Un peu plus appuyée : elle annonce que vous savez qu'on peut penser autrement."),
        ("Je trouve que…",
         "La plus courante à l'oral, et la plus facile à enchaîner avec « parce que »."),
        ("Il me semble que…",
         "La plus prudente : elle laisse la place au doute et à l'autre."),
    ], notes="Faire choisir à chaque élève l'entrée qui lui va, et la faire employer "
             "trois fois dans la séance. Une formule qu'on adopte vaut mieux que cinq "
             "qu'on récite.")

    d.pratique('Écriture', "Moi, ce qui me…, c'est…",
               "Complétez avec : moi, ce qui, c'est, c'est que, par contre.", [
        ("___, ce qui me surprend, c'est le nombre de vélos volés.", "Moi"),
        ("Ce ___ me dérange, c'est qu'on laisse les cabanons ouverts.", "qui"),
        ("Ce que je trouve inquiétant, ___ le retour des mêmes vols.", "c'est"),
        ("Ce qui me rassure, ___ la police a demandé de signaler chaque vol.", "c'est que"),
        ("C'est vrai que ça aide de barrer sa porte. ___, ça n'excuse pas le voleur.", "Par contre"),
        ("___, ce qui me choque, c'est qu'on n'ait rien dit aux voisins.", "Moi"),
    ], corrige=True,
       notes="Exercice t3disl de l'activité. Les deux plus instructives sont la "
             "troisième et la quatrième : un nom appelle « c'est », une phrase appelle "
             "« c'est que ». Une syllabe de différence, et c'est celle qu'on oublie.")

    d.regle("Un « il » qui ne désigne personne",
            "Il faut noter son numéro de série. Il vaut mieux barrer son "
            "cabanon, même pour une heure.",
            precision="« Tu devrais barrer ton cabanon » vise quelqu'un. « Il vaut "
                      "mieux barrer son cabanon » ne vise personne, dit la même "
                      "chose, et n'a pas besoin d'être adoucie. Six tournures "
                      "servent tous les jours : il faut, il faudrait, il est "
                      "important de, il vaut mieux, il arrive que, il y a.",
            notes="Diapositive à photographier. Faire transformer trois reproches "
                  "personnels en phrases impersonnelles à l'oral : l'effet sur le ton "
                  "de la classe est immédiat et parlant.")

    d.pratique('Écriture', "Sans montrer personne du doigt",
               "Complétez avec la tournure impersonnelle qui convient.", [
        ("___ noter le numéro de série de son vélo : la police le demande.", "Il faut"),
        ("___ que des vélos soient retrouvés sans qu'on sache à qui les rendre.", "Il arrive"),
        ("___ barrer son cabanon, même pour une heure.", "Il vaut mieux"),
        ("___ eu une trentaine de vols dans le quartier en un mois.", "Il y a"),
        ("___ refaire le fossé avant l'automne, à mon avis.", "Il faudrait"),
        ("___ signaler chaque vol, même petit.", "Il est important de"),
    ], corrige=True,
       notes="Exercice t3imp de l'activité. Rappeler que le verbe reste au singulier : "
             "« il y a eu trente vols », jamais « il y ont eu ». Le sujet est « il », "
             "pas « trente vols ».")

    d.regle("Accorder d'abord, objecter ensuite",
            "C'est vrai que ça aide de barrer sa porte. Par contre, ça "
            "n'excuse pas celui qui entre.",
            precision="Quatre mots pour tourner : par contre, cependant, quand "
                      "même, n'empêche que. Et une opinion se justifie toujours : "
                      "ajoutez la raison avec « parce que ». Un avis sans raison est "
                      "un avis qu'on ne peut pas discuter.",
            notes="Diapositive à photographier, et à laisser affichée pendant "
                  "l'exercice t3nuance. C'est la structure exacte que le jeu de rôle "
                  "de E1 demandera quand l'assistant ne sera pas d'accord.")

    d.pratique('Écriture', "Répondre à quelqu'un qui pense autrement",
               "Deux phrases : accordez d'abord, objectez ensuite.", [
        ("« Ça, c'est de la négligence, pas du vol. »",
         "C'est vrai qu'une porte barrée aide. Par contre, ça n'excuse pas celui qui entre."),
        ("« Noter un numéro de série, ça n'a jamais ramené un vélo. »",
         "Je comprends que ça paraisse inutile. Cependant, sans numéro, la police ne peut rien rendre."),
        ("« Le monde qui achète au bord de l'eau savait ce qui l'attendait. »",
         "C'est sûr que le risque était connu. N'empêche que personne ne mérite de tout perdre."),
        ("« De toute façon, les journaux en rajoutent toujours. »",
         "Il y a du vrai là-dedans. Par contre, les chiffres de la police, eux, se vérifient."),
    ], corrige=True,
       notes="Exercice t3nuance de l'activité, le plus exigeant du module. Les "
             "corrigés sont des modèles, pas des réponses attendues. Faire lire "
             "quatre productions d'élèves à voix haute avant la fin.")

    d.piege("Présenter son opinion comme un fait",
            "Laisser son cabanon ouvert, c'est de la négligence.",
            "Moi, ce qui me dérange, c'est qu'on laisse les cabanons ouverts.",
            "Sans annonce, votre jugement se range avec les chiffres de la police, et "
            "la personne en face le répétera comme une information. D'abord les "
            "faits, avec leur source ; ensuite votre avis, annoncé comme tel.",
            notes="Dernier piège du module, et celui qui referme les trois défis : "
                  "l'ordre du récit, la source de la parole, la nature de l'avis. Le "
                  "dire ainsi en clôture.")

    d.billet(
        "Répondez en deux phrases à quelqu'un qui n'est pas d'accord avec vous.",
        exemples=[
            "Première phrase : ce que vous lui accordez. Deuxième : votre objection.",
            "Terminez par « parce que » et donnez votre raison.",
        ],
        notes="Fin du bloc D. Corriger et rendre avant E1 : ces deux phrases sont "
              "exactement ce que l'assistant demandera dans le jeu de rôle.")

    return d.save(dossier)
