# -*- coding: utf-8 -*-
"""B3 · Qui, que, où — recoller les phrases
Bloc B « Défi 1 · Ce que raconte l'histoire » · couleur acier · 75 min.
Source : exercice `t1rel`, mini-leçon `t1rel`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='acier',
        titre="Qui, que, où — recoller les phrases",
        chapeau="« C'est une femme. Elle revient au village. Elle a quitté "
                "ce village il y a vingt ans. » Trois phrases correctes, et "
                "l'auditeur perd le fil. Trois petits mots suffisent à n'en "
                "faire qu'une, sans rien perdre.",
        duree='75 minutes')

    d.titre(notes="Séance de langue. Écrire au tableau les trois phrases courtes du "
                  "chapeau et demander au groupe de les dire d'un seul souffle. "
                  "Quelqu'un trouvera « qui » ou « que » tout seul : partir de là plutôt "
                  "que de la règle.")

    d.objectifs([
        "relier deux phrases avec « qui », « que » ou « où » ;",
        "choisir entre les trois par ce qui suit le trou ;",
        "ne jamais élider « qui » devant une voyelle ;",
        "employer « où » après un nom de temps : le jour où, la fois où.",
    ], notes="Les deux derniers objectifs sont les fautes réelles du niveau 5. « Qu'a "
             "quitté un pays » et « le jour que je l'ai fini » s'entendent partout, y "
             "compris chez des locuteurs de naissance. À l'écrit corrigé, elles comptent.")

    d.declencheur(
        'Mise en route', "Comment dire en une seule phrase : « C'est une "
                         "femme. Elle revient au village. » ?",
        pistes=[
            "Quel petit mot mettriez-vous entre les deux ?",
            "Et pour : « le roman » + « j'ai lu ce roman » ?",
            "Et pour : « le village » + « elle est née dans ce village » ?",
            "Est-ce que le même mot sert dans les trois cas ?",
        ],
        notes="Les trois cas donnent qui, que, où — dans cet ordre. Laisser le groupe "
              "essayer et se tromper : les erreurs qui sortent ici sont exactement celles "
              "que la règle va régler, et il vaut mieux les avoir entendues avant.")

    d.regle("Regardez ce qui vient juste après le trou",
            "Un verbe tout seul, c'est qui. Un sujet, c'est que. Un lieu ou "
            "un moment devant, c'est où.",
            precision="Trois secondes de test valent mieux qu'une règle apprise par "
                      "cœur. « Une femme ___ revient » : après le trou, un verbe sans "
                      "sujet, donc qui. « Le roman ___ j'ai lu » : après le trou, un "
                      "sujet — j' —, donc que. « Le village ___ elle est née » : devant "
                      "le trou, un lieu, donc où.",
            notes="Diapositive à photographier. Faire appliquer le test à voix haute sur "
                  "cinq ou six exemples avant l'exercice écrit : c'est un réflexe à "
                  "installer, pas une connaissance à retenir.")

    d.tableau('Les trois cas', "Ce qui suit, ce qui précède, et le mot qui va",
              ['Ce qu\'on voit', 'Le mot', 'Un exemple du module'],
              [["Un verbe suit, sans sujet", "qui", "une femme qui revient au village"],
               ["Un sujet suit", "que", "le roman que j'ai lu la semaine passée"],
               ["Un lieu précède", "où", "le village où elle est née"],
               ["Un moment précède", "où", "le jour où elle ouvre la boîte"],
               ["Une voyelle suit « que »", "qu'", "la boîte qu'elle trouve au grenier"]],
              cle=1,
              notes="La cinquième rangée est la seule contraction du tableau : que devient "
                    "qu' devant une voyelle. Qui ne change jamais, et c'est l'objet du "
                    "piège de la séance.")

    d.cartes("Ce que les relatives permettent", "Quatre choses en une phrase", [
        ("Décrire un personnage",
         "Un personnage qui ne parle presque jamais, c'est difficile à raconter."),
        ("Situer une œuvre",
         "Une histoire qui se passe en hiver, dans un village au bord de la mer."),
        ("Désigner ce qu'on a lu",
         "L'album que vous tenez est le premier tome de la série."),
        ("Marquer le moment qui bascule",
         "Le jour où elle ouvre la boîte, tout change pour elle."),
    ], notes="La quatrième carte est celle qui fait le plus d'effet dans une présentation : "
             "« le jour où… » annonce que quelque chose bascule, sans dire quoi. C'est "
             "exactement l'endroit où l'on s'arrête de raconter.")

    d.pratique('Complétez', "qui, que ou où ?",
               "Appliquez le test : regardez ce qui vient juste après le trou.", [
        ("C'est une femme ___ revient au village après vingt ans.", "qui"),
        ("Le roman ___ j'ai lu la semaine passée fait trois cents pages.", "que"),
        ("Le village ___ elle est née se trouve au bord de la mer.", "où"),
        ("Un personnage ___ ne parle presque jamais est difficile à raconter.", "qui"),
        ("La boîte ___ elle trouve dans le grenier contient des lettres.", "qu'"),
        ("Le jour ___ elle ouvre la boîte, tout change pour elle.", "où"),
    ], corrige=True,
       notes="C'est l'exercice `t1rel` du module interactif. La cinquième ligne demande "
             "l'élision ; la sixième est celle où l'oreille dit « que » et où l'écrit "
             "demande « où ». Les deux méritent qu'on s'y arrête.")

    d.piege("Élider « qui » devant une voyelle",
            "Je le recommande à quelqu'un qu'a quitté un pays.",
            "Je le recommande à quelqu'un qui a quitté un pays.",
            "« Que » s'élide, « qui » ne s'élide jamais, dans aucun cas. C'est la faute "
            "d'écriture la plus fréquente du niveau 5, et elle se corrige une fois pour "
            "toutes : le i de « qui » ne tombe pas.",
            notes="Faire écrire au tableau les deux formes côte à côte et faire dire la "
                  "phrase juste trois fois. À l'oral, la différence s'entend à peine — "
                  "c'est pour ça que la faute passe à l'écrit sans que personne la voie.")

    d.piege("Employer « que » après un nom de temps",
            "Le jour que je l'ai fini, j'ai pleuré.",
            "Le jour où je l'ai fini, j'ai pleuré.",
            "Après un nom qui dit le temps — le jour, l'année, la fois, le moment —, "
            "c'est « où » qu'il faut. L'oreille dit le contraire parce que « le jour "
            "que » s'entend partout ; l'écrit corrigé demande « où ».",
            notes="Ne pas dire que la forme entendue est fautive en soi : elle est très "
                  "répandue à l'oral au Québec comme ailleurs. La règle vaut pour la "
                  "production écrite, qui est ce qui sera corrigé.")

    d.pratique('À l\'oral', "Une phrase, deux informations",
               "Reprenez votre présentation et collez deux phrases en une.", [
        ("« C'est une femme… » — ajoutez « qui » et ce qu'elle fait.",),
        ("« C'est un roman… » — ajoutez « que » et ce que vous en avez fait.",),
        ("« Ça se passe dans… » — ajoutez « où » et ce qui s'y passe.",),
        ("Redites les trois phrases d'affilée, sans regarder vos notes.",),
    ], notes="Deux par deux, puis quelques passages devant le groupe. Consigne à "
             "l'auditeur : compter les relatives entendues. Deux par présentation "
             "suffisent — six la rendent illisible, et il vaut mieux le dire tout de suite.")

    d.billet(
        "Réécrivez le temps 3 de votre présentation avec « qui » ou « que ».",
        exemples=[
            "Avant : « C'est une femme. Elle revient au village. Elle l'a quitté il y a vingt ans. »",
            "Après : « C'est une femme qui revient dans le village qu'elle a quitté il y a vingt ans. »",
        ],
        notes="Le billet transforme du matériel que l'élève a déjà écrit en B1 : c'est ce "
              "qui rend la règle concrète. Ramasser et relire avant B4 — les phrases "
              "réécrites font d'excellents exemples de départ.")

    return d.save(dossier)
