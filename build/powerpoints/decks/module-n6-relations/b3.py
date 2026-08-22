# -*- coding: utf-8 -*-
"""B3 · Le petit mot qui renvoie à ce qui précède
Bloc B « Défi 1 » · couleur ambre · grammaire du texte · 75 min.
Source : exercice `t1repr` (cols:1) et sa mini-leçon — la reprise de
l'information, premier des cinq savoirs de grammaire du texte du niveau 6.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Le petit mot qui renvoie à ce qui précède",
        chapeau="Le, en, y : trois mots de deux lettres qui portent chacun "
                "une phrase entière. C'est là que se perd le fil d'un texte "
                "long.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire du texte. Commencer par écrire au tableau « on "
                  "l'avait déjà vendue » et demander : vendu quoi ? Sans le contexte, "
                  "personne ne peut répondre — et c'est exactement le point.")

    d.objectifs([
        "retrouver ce que remplacent le, en et y dans un texte suivi ;",
        "employer ces pronoms pour ne pas répéter un mot trois fois ;",
        "garder la préposition quand il s'agit d'une personne ;",
        "placer le pronom devant le verbe, y compris à la négative.",
    ], notes="Le troisième objectif est celui qu'on rate le plus longtemps : « j'y "
             "pense » pour une personne s'entend jusqu'au niveau 8.")

    d.declencheur(
        'Observation', "Pourquoi ne dit-on jamais deux fois le même nom ?",
        pistes=[
            "Lis à voix haute : j'ai vendu la maison, la maison était trop petite.",
            "Qu'est-ce que ça donne ?",
            "Comment fais-tu dans ta langue pour éviter la répétition ?",
            "Est-ce qu'on remplace, ou est-ce qu'on supprime ?",
        ],
        notes="La comparaison entre langues est utile ici : certaines répètent le nom "
              "sans que ce soit lourd, d'autres suppriment complètement. Le français "
              "remplace, et c'est ce remplacement qui donne du travail au lecteur.")

    d.tableau('Analyse', "Trois pronoms, trois emplois",
              ['Le pronom', 'Ce qu\'il remplace'],
              [["le", "une idée entière déjà dite : je le sais"],
               ["l', la, les", "un nom précis : il l'a vendue"],
               ["en", "de + une chose : il en parle"],
               ["y", "à + une chose, ou un lieu : j'y pense"],
               ["celui-là, celle-là", "un nom déjà nommé, quand il faut choisir"]],
              cle=0,
              note="Pour une personne, on garde la préposition : de lui, à elle.",
              notes="Diapositive à photographier. La note du bas est la règle la plus "
                    "utile de la séance ; y revenir à chaque exemple.")

    d.regle("Devant un petit mot sans nom, recule d'une phrase",
            "C'est un geste, pas une règle de grammaire.",
            precision="On lit « on l'avait déjà vendue ». On recule : le paragraphe "
                      "d'avant parle de la maison de la rue Perreault. On conclut, et "
                      "on avance. Deux secondes, et le fil est retrouvé pour tout le "
                      "reste du paragraphe.",
            notes="Diapositive à photographier. Faire le geste ensemble, à voix haute, "
                  "sur trois exemples du courriel. C'est un réflexe qui s'installe par "
                  "répétition, pas par explication.")

    d.pratique('Grammaire', "Le, en ou y ?",
               "Complétez la deuxième phrase avec le, l', en ou y.", [
        ("Ousmane a vendu la maison. Quand il a écrit, il ... avait déjà vendue.", "l'"),
        ("Marisol savait que Kadiatou arrivait vendredi. Elle ... savait depuis mardi.", "le"),
        ("Il parle de son nouveau logement. Il ... parle dans tout le deuxième paragraphe.", "en"),
        ("Il n'a pas pu aller aux funérailles. Il n'... est pas allé.", "y"),
        ("Marisol pense souvent à cette amitié. Elle ... pense en passant devant la boulangerie.", "y"),
        ("Ghislain ne connaît pas Kadiatou. Il ne ... a jamais vue.", "l'"),
    ], corrige=True,
       notes="Faire dire à chaque fois ce que le pronom remplace, avant de donner la "
             "forme. Sans cela, l'exercice devient un jeu de sonorités.")

    d.piege('Reprise', "Je pense à ma sœur, donc j'y pense",
            "Je pense à ma sœur, donc je pense à elle",
            "En et y ne remplacent jamais une personne. Pour une personne, on garde "
            "la préposition : je parle de lui, je pense à elle, il s'occupe d'eux. "
            "C'est la seule chose à retenir pour éviter les trois quarts des erreurs.",
            notes="Dédramatiser : l'erreur se comprend toujours et ne bloque jamais la "
                  "communication. Mais elle s'entend, et elle se corrige facilement.")

    d.cartes('Accord', "Deux phrases, une lettre de différence", [
        ("Il a vendu la maison.",
         "Le complément suit le verbe : le participe ne s'accorde pas. On écrit vendu."),
        ("Il l'a vendue.",
         "Le complément est passé devant, sous la forme de l'. Le participe s'accorde : vendue."),
        ("Il l'a jamais vue.",
         "Même chose au féminin : le e final ne s'entend pas, mais il s'écrit."),
        ("Je le sais.",
         "Ce le remplace une idée entière et ne s'accorde jamais : ni genre ni nombre."),
    ], notes="Cette page relie la reprise à l'accord du participe, que les élèves "
             "connaissent déjà du niveau 5 sans l'avoir relié à ce pronom.")

    d.billet(
        "Écris deux phrases : la seconde reprend un mot de la première.",
        exemples=[
            "Exemple : Ma sœur est arrivée en octobre. Je l'attendais depuis un an.",
            "Souligne le mot que tu remplaces.",
        ],
        notes="Deux minutes. Les billets se corrigent vite et disent exactement qui a "
              "compris le mécanisme.")

    return d.save(dossier)
