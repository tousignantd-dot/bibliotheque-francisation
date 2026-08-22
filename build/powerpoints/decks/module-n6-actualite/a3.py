# -*- coding: utf-8 -*-
"""A3 · Le tiret et les guillemets, à la lecture
Bloc A « Je découvre » · couleur ambre · 75 min.
Source : exercice `prPonct` et sa mini-leçon « Le tiret et les guillemets, à
la lecture ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='ambre',
        titre="Le tiret et les guillemets, à la lecture",
        chapeau="Deux signes reviennent à chaque page d'un journal. Ils ne "
                "servent pas à décorer : ils disent qui parle, ce qui est "
                "une précision, et quels mots ne sont pas ceux de l'auteur.",
        duree='75 minutes')

    d.titre(notes="Troisième séance du bloc A. Ouvrir avec deux ou trois mots ramassés "
                  "dans les billets de A2 : cinq minutes, puis on entre dans la "
                  "ponctuation. Apporter un vrai journal si possible ; la page des "
                  "lettres montre les deux signes en une seule vue.")

    d.objectifs([
        "lire un tiret qui ouvre une énumération ;",
        "lire un tiret qui marque un changement de locuteur ;",
        "lire deux tirets qui encadrent une précision ;",
        "distinguer des guillemets qui citent de guillemets qui prennent "
        "leurs distances.",
    ], notes="Quatre emplois seulement. Ne pas ajouter la parenthèse ni la virgule "
             "d'apposition aujourd'hui : le groupe les confondrait tout de suite.")

    d.declencheur(
        'Observation', "Qu'est-ce que ce signe change à la phrase ?",
        pistes=[
            "« Le mot important - raisonnable - n'est pas défini par un chiffre. »",
            "« Trois étapes - le marchand, la lettre, le tribunal. »",
            "« - Et si le marchand refuse ? »",
            "« Sa laveuse était irréparable, paraît-il. »",
        ],
        notes="Écrire les quatre phrases au tableau avec leur ponctuation réelle. "
              "Demander pour chacune : est-ce que le signe ajoute un mot ? Non. "
              "Alors qu'est-ce qu'il ajoute ?")

    d.tableau('Analyse', "Le tiret : trois emplois, trois lectures",
              ['L\'emploi', 'L\'exemple'],
              [["Il ouvre une énumération",
                "Trois étapes - le marchand, la lettre, le tribunal."],
               ["Il marque qui parle",
                "- Et si le marchand refuse ?"],
               ["Deux tirets encadrent une précision",
                "La durée raisonnable - celle de la loi - dépend du prix."]],
              cle=0,
              note="Dans le troisième cas, la phrase reste complète si on enlève ce qui est entre les deux tirets.",
              notes="Diapositive à photographier. Faire faire le test du troisième cas "
                    "à voix haute : on lit la phrase en sautant le passage encadré, et "
                    "elle tient debout. C'est le seul test fiable.")

    d.tableau('Analyse', "Les guillemets : deux emplois très différents",
              ['L\'emploi', 'L\'exemple'],
              [["Ils citent les mots exacts",
                "Elle a répondu : « Je vous rappelle jeudi. »"],
               ["Ils prennent une distance",
                "On lui a dit que l'appareil était « fini »."]],
              cle=0,
              note="Dans le second cas, les guillemets veulent dire : ce mot-là, je ne le prends pas à mon compte.",
              notes="Diapositive à photographier. Le second emploi est le plus utile du "
                    "module : il revient dans le fait divers du bloc D et dans le "
                    "courrier des lecteurs.")

    d.regle("Un signe qui ne s'entend pas",
            "Les guillemets autour d'un seul mot ne citent personne : ils prennent leurs distances.",
            precision="Quand un journal écrit que l'appareil était « irréparable », il "
                      "n'affirme pas qu'il l'était : il rapporte le mot de quelqu'un "
                      "d'autre et il s'en écarte. À l'oral, personne n'entend ces "
                      "guillemets. C'est une des raisons pour lesquelles un texte lu "
                      "et un texte entendu ne disent pas tout à fait la même chose.",
            notes="Diapositive à photographier. Demander au groupe comment on rend ce "
                  "sens à l'oral : le ton, une pause, ou la formule « soi-disant ».")

    d.pratique('Reconnaissance', "Quel emploi reconnais-tu ?",
               "Nommez l'emploi de chaque signe.", [
        ("Trois étapes - le marchand, la lettre, le tribunal.", "un tiret qui ouvre une énumération"),
        ("- Et si le marchand refuse ?", "un tiret qui marque un changement de locuteur"),
        ("La durée raisonnable - celle de la loi - dépend du prix payé.", "deux tirets qui encadrent une précision"),
        ("Elle a répondu : « Je vous rappelle jeudi. »", "des guillemets qui citent les mots exacts"),
        ("On lui a dit que l'appareil était « fini ».", "des guillemets qui mettent un mot à distance"),
    ], corrige=True,
       notes="Faire répondre à l'oral, sans écrire, puis afficher. Le troisième est le "
             "seul qui résiste : rappeler le test de la phrase qui tient debout sans "
             "le passage encadré.")

    d.piege("Prendre une précision pour la suite de la phrase",
            "La durée raisonnable celle de la loi dépend du prix payé.",
            "La durée raisonnable - celle de la loi - dépend du prix payé.",
            "Sans les deux tirets, la phrase devient illisible : on cherche un verbe "
            "pour « celle de la loi » et on ne le trouve pas. Les tirets ne sont pas "
            "un ornement, ils remplacent une pause de la voix. En lecture rapide, "
            "beaucoup d'élèves les sautent et perdent la phrase entière.",
            notes="Faire lire la version fautive à voix haute par un volontaire : "
                  "l'impossibilité s'entend tout de suite, et personne n'oublie.")

    d.cartes("Lire une page de journal sans se perdre", "Quatre réflexes", [
        ("Un tiret en début de ligne",
         "quelqu'un parle. Cherche qui, dans les lignes d'avant."),
        ("Deux tirets dans la phrase",
         "saute ce qu'ils encadrent, lis la phrase, puis reviens."),
        ("Des guillemets longs",
         "ce sont les mots exacts d'une personne, pas ceux du journal."),
        ("Des guillemets sur un mot",
         "le journal se met à distance de ce mot-là."),
    ], notes="À copier dans le cahier. Ces quatre réflexes servent dès le bloc B, où "
             "la chronique est transcrite avec des tirets de dialogue.")

    d.billet(
        "Dans quel cas emploierais-tu des guillemets pour prendre tes distances ?",
        exemples=[
            "Un mot qu'on t'a dit et que tu ne reprends pas à ton compte.",
            "Une phrase suffit ; l'exemple peut venir de ta vie.",
        ],
        notes="Deux minutes. Les meilleures réponses viennent souvent d'une situation "
              "vécue au travail ou dans un commerce ; les garder pour le bloc D.")

    return d.save(dossier)
