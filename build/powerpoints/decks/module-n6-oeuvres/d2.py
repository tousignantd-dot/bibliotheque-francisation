# -*- coding: utf-8 -*-
"""D2 · Accorder un point, puis répondre
Bloc D « Défi 3 · La critique et le résumé » · couleur teal · 75 min.
Bilan du bloc. Source : exercices `t3subj`, `t3si` et `t3guill`, et leurs
mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='teal',
        titre="Accorder un point, puis répondre",
        chapeau="Un avis qu'on peut discuter a trois marques : il s'annonce "
                "comme un avis, il accorde quelque chose à l'autre, et il "
                "s'appuie sur un moment précis.",
        duree='75 minutes')

    d.titre(notes="Dernière séance avant « Je me lance ». Elle donne les trois outils "
                  "de langue du Défi 3 — le subjonctif, l'hypothèse en « si », les "
                  "formules de point de vue — et le geste qui les relie.")

    d.objectifs([
        "employer le subjonctif après il faut que, je doute que, il vaut mieux que ;",
        "poser une hypothèse réaliste avec « si », sans futur après « si » ;",
        "accorder un point avant de répondre ;",
        "reconnaître une phrase qui ferme la discussion.",
    ], notes="Le quatrième objectif est le plus utile hors de la classe, et le seul "
             "qui ne soit pas grammatical.")

    d.declencheur(
        'Observation', "Laquelle de ces deux phrases peut-on discuter ?",
        pistes=[
            "« Si vous n'avez pas compris, c'est que vous n'avez pas regardé. »",
            "« Si on manque le signal une fois, on se perd pour vingt minutes. »",
            "Les deux disent presque la même chose. Qu'est-ce qui change ?",
            "À laquelle des deux aurais-tu envie de répondre ?",
        ],
        notes="Les deux phrases sont grammaticalement justes. La première vise la "
              "personne, la seconde pose une condition. Faire trouver la différence "
              "par le groupe avant de la nommer.")

    d.tableau('Analyse', "Les verbes qui demandent le subjonctif",
              ['Le verbe introducteur', 'Ce qui suit'],
              [["il faut que", "subjonctif : il faut qu'elle arrive"],
               ["il vaut mieux que", "subjonctif : il vaut mieux que tu voies"],
               ["je doute que", "subjonctif : je doute qu'il ait compris"],
               ["je pense que", "indicatif : je pense qu'elle est nécessaire"],
               ["j'espère que", "indicatif : j'espère qu'ils publieront"]],
              cle=0,
              note="Les deux dernières lignes sont celles qu'on se trompe : penser et espérer ne le demandent pas.",
              notes="Diapositive à photographier. C'est arbitraire, il n'y a rien à "
                    "comprendre : c'est à retenir. Le dire franchement fait gagner du "
                    "temps.")

    d.regle("Comment se fabrique le subjonctif",
            "On part de la 3e personne du pluriel du présent, et on enlève la terminaison.",
            precision="Ils viennent, que je vienne. Ils prennent, que tu prennes. "
                      "Quatre irréguliers seulement : être, que je sois ; avoir, que "
                      "j'aie ; aller, que j'aille ; faire, que je fasse. Pour la "
                      "plupart des verbes en -er, personne n'entend la différence "
                      "avec le présent.",
            notes="Diapositive à photographier. La dernière phrase rassure : le "
                  "subjonctif s'entend surtout sur les quatre irréguliers.")

    d.regle("Jamais de futur après « si »",
            "Si + présent, puis présent ou futur. Si + passé composé, puis présent ou futur.",
            precision="On n'écrit pas « si tu manqueras » : on écrit « si tu "
                      "manques ». La conséquence, elle, peut être au futur : « si tu "
                      "écris au journal, ils publieront ta lettre ». Attention au "
                      "« si » qui n'est pas une condition : « je me demande si le "
                      "journal publiera » — là, le futur est permis.",
            notes="Diapositive à photographier. C'est la faute la plus fréquente à "
                  "tous les niveaux, et la plus audible. La corriger ici évite vingt "
                  "corrections en E2.")

    d.pratique('Grammaire', "Subjonctif ou indicatif ?",
               "Complétez avec le verbe entre parenthèses.", [
        ("Il faut que la voisine ... (arriver) tard.", "arrive"),
        ("Je doute que le public ... (avoir) appris ces signaux.", "ait"),
        ("Il vaut mieux que tu ... (voir) le film avant la critique.", "voies"),
        ("Il faudrait qu'on ... (être) plus attentif au son.", "soit"),
        ("Je pense que le personnage ... (être) nécessaire.", "est - pas de subjonctif"),
        ("Il faut que ce reproche ... (faire) réagir quelqu'un.", "fasse"),
    ], corrige=True, cols=2,
       notes="Le cinquième item est le piège. L'annoncer avant de commencer : « il y "
             "en a un qui ne prend pas le subjonctif, trouvez-le ».")

    d.pratique('Grammaire', "Posez la condition avec « si »",
               "Attention au temps qui suit « si ».", [
        ("Si tu ... (manquer) le bruit de la mer, tu ne sais plus où tu es.", "manques"),
        ("Si le public n' ... (avoir) jamais appris ces signaux, il ne peut pas les voir.", "a"),
        ("Si tu ... (lire) la critique avant, tu regarderas le film autrement.", "lis"),
        ("Si on ... (rater) le signal une fois, on se perd pour vingt minutes.", "rate"),
        ("Si Thérèse ... (écrire) au journal, ils publieront sa réponse.", "écrit"),
        ("Je me demande si le journal ... (publier) sa lettre.", "publiera - futur permis"),
    ], corrige=True, cols=2,
       notes="Le dernier item est le « si » de la question rapportée. Le garder pour "
             "la fin et le corriger lentement.")

    d.tableau('Analyse', "Annoncer, accorder, nuancer",
              ['L\'intention', 'La formule'],
              [["annoncer un avis", "à mon avis, pour ma part, je trouve que"],
               ["accorder un point", "c'est vrai que..., j'admets que..., mais"],
               ["concéder", "même si, bien que, quand même"],
               ["mettre à distance", "un film qu'on dit « ambitieux »"],
               ["citer", "il écrit : « mon vrai reproche est ailleurs »"]],
              cle=0,
              note="« Bien que » demande le subjonctif ; « même si » demande l'indicatif.",
              notes="Diapositive à photographier. C'est la boîte à outils de E1 et "
                    "E2 : la faire recopier au complet dans le cahier.")

    d.piege("Contredire en bloc",
            "Il a tort.",
            "Il a raison sur la lenteur, mais pas sur les signaux.",
            "Contredire en bloc oblige l'autre à tout défendre, et la discussion "
            "s'arrête. Accorder un point d'abord donne du poids à ce qui suit : celui "
            "qui vient d'être approuvé écoute la suite, celui qui vient d'être "
            "contredit prépare sa réponse.",
            notes="Faire refaire l'exercice à l'oral, deux par deux : un élève attaque "
                  "le film, l'autre doit accorder un point avant de répondre. Trois "
                  "minutes, et le geste est acquis.")

    d.billet(
        "Écris ton avis sur le film en deux phrases : un point accordé, un point défendu.",
        exemples=[
            "Première phrase : « C'est vrai que... »",
            "Deuxième phrase : « Mais, pour ma part... »",
        ],
        notes="Trois minutes. Ces billets sont le brouillon du deuxième paragraphe "
              "de E2. Les faire garder dans le cahier, pas les ramasser.")

    return d.save(dossier)
