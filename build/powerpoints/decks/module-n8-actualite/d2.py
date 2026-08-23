# -*- coding: utf-8 -*-
"""D2 · Ce qui n'a pas eu lieu, et ce qu'on met en avant
Bloc D « Défi 3 · Prendre position » · couleur ambre · 75 min.
Source : exercices `t3irreel`, `t3emph` et `t3rel`, et leurs mini-leçons.
Les trois n'ont pas le même poids ici : l'irréel et l'emphase servent
directement la tribune et la lettre, les relatives sont d'abord un savoir de
lecture et occupent le dernier quart d'heure.
Dossier inventé : Rivière-aux-Cèdres, le boisé Sainte-Perpétue.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Le reproche civilisé, et ce qu'on souligne à l'oral",
        chapeau="Deux tournures font presque tout le travail d'une prise de "
                "position : celle qui parle du monde qui n'a pas eu lieu, et "
                "celle qui dit à l'auditoire ce qu'il doit retenir.",
        duree='75 minutes')

    d.titre(notes="Séance de langue, la plus chargée du bloc. Trois points au "
                  "programme, et ils ne se valent pas : l'irréel prend la première "
                  "heure avec l'emphase, les relatives le dernier quart d'heure. Ne "
                  "pas répartir également, on perdrait les trois.")

    d.objectifs([
        "employer l'hypothèse irréelle du passé : si plus plus-que-parfait, conditionnel passé ;",
        "reconnaître le « si » qui n'est pas une hypothèse ;",
        "mettre en relief avec c'est... qui, ce que... c'est, et le détachement ;",
        "choisir dont, auquel, pour lesquelles selon la préposition du verbe.",
    ], notes="Les deux premiers vont ensemble et occupent la moitié de la séance. Le "
             "quatrième est un savoir de lecture avant d'être un savoir "
             "d'écriture : le dire au groupe, cela change ce qu'on en attend.")

    d.declencheur(
        'Discussion', "Qu'est-ce qui aurait dû se passer autrement ?",
        pistes=[
            "Reprenez le dossier du boisé : quel geste manque, selon vous ?",
            "Comment reprocher une décision sans accuser personne ?",
            "Comment dire un regret sans dire « c'est de ma faute » ?",
            "Est-ce qu'on peut critiquer et rester écoutable ?",
        ],
        notes="Recueillir trois ou quatre réponses au tableau, telles qu'elles "
              "viennent. On y reviendra à la fin de la première partie pour les "
              "reformuler à l'irréel : c'est là que la forme se justifie toute seule.")

    d.regle("Si plus plus-que-parfait, puis conditionnel passé",
            "Si la Ville avait publié l'évaluation, personne n'aurait "
            "demandé de référendum. Jamais de conditionnel après « si » : "
            "c'est la faute la plus connue du français.",
            precision="Plus-que-parfait dans la moitié « si » : avoir ou être à "
                      "l'imparfait, plus le participe. Conditionnel passé dans "
                      "l'autre : avoir ou être au conditionnel, plus le même "
                      "participe. Les deux moitiés peuvent s'échanger ; quand « si » "
                      "passe en second, la virgule disparaît.",
            notes="Diapositive à photographier. Faire écrire les deux moitiés l'une "
                  "sous l'autre et souligner l'auxiliaire dans chacune. « Si "
                  "j'aurais » se corrige en se rappelant que « si » et « -rais » ne "
                  "se rencontrent jamais.")

    d.tableau('Analyse', "Ce que cette forme sert à dire",
              ['Ce qu\'on veut faire', 'Ce qu\'on dit'],
              [["Reprocher sans accuser",
                "Si l'évaluation avait été publiée, cette discussion n'aurait pas lieu d'être."],
               ["Regretter",
                "Si j'avais parlé à l'assemblée, j'aurais eu ma réponse."],
               ["Tirer une leçon",
                "Si le conseil avait attendu deux semaines, le vote aurait été mieux compris."],
               ["Dire que l'effet dure encore",
                "S'ils avaient mieux consulté, nous n'en serions pas là aujourd'hui."]],
              cle=0,
              note="La dernière ligne mêle les deux temps : passé dans la condition, présent dans la conséquence.",
              notes="Diapositive à photographier. La quatrième ligne est celle qui "
                    "surprend : ce qui s'est mal fait hier produit encore ses effets, "
                    "donc conditionnel présent. Y revenir à la pratique.")

    d.pratique('Pratique 1 de 3', "Ce qui aurait pu se passer autrement",
               "Écrivez seulement le groupe verbal demandé.", [
        ("Si la Ville avait publié l'évaluation, le comité ___ (ne pas ouvrir) de registre.", "n'aurait pas ouvert"),
        ("Si le conseil ___ (attendre) deux semaines, le vote aurait été mieux compris.", "avait attendu"),
        ("Si j'avais eu ces documents la semaine dernière, je ___ (ne pas appeler) ce matin.", "n'aurais pas appelé"),
        ("Nous ___ (venir) plus nombreux si la séance n'avait pas duré jusqu'à vingt-trois heures.", "serions venus"),
        ("S'ils avaient mieux consulté, nous n'en ___ (être) pas là aujourd'hui.", "serions - l'effet dure encore"),
        ("Je me demande si la Ville ___ (publier) enfin l'évaluation avant mardi.", "publiera - ce n'est pas une hypothèse"),
    ], corrige=True,
       notes="Les deux dernières lignes sont les pièges de l'exercice. « Serions » "
             "sans participe, parce que l'effet dure ; « publiera » parce que « si » "
             "y introduit une question indirecte, où le futur est permis.")

    d.piege('Piège', "« si » veut toujours dire hypothèse",
            "« si » introduit aussi une question indirecte",
            "« Je me demande si la Ville publiera l'évaluation » n'est pas "
            "une hypothèse : c'est une question rapportée, et le futur y est "
            "correct. La règle « jamais de conditionnel après si » ne vaut "
            "que pour l'hypothèse. Le test : peut-on remplacer « si » par "
            "« oui ou non » dans la phrase ?",
            notes="Ce piège fait rater la dernière ligne de la pratique à presque "
                  "tout le monde, et c'est très bien : on ne retient une exception "
                  "qu'après y être tombé une fois.")

    d.regle("Ce que je demande, c'est...",
            "À l'écrit on souligne ; à l'oral, on ne peut pas. Le français a "
            "des tournures qui font le même travail : elles déplacent un "
            "groupe de mots et le mettent en évidence.",
            precision="Quatre outils. C'est... qui quand le groupe extrait est le "
                      "sujet, c'est... que dans tous les autres cas. Ce que... c'est "
                      "pour annoncer qu'un point important arrive. Le détachement "
                      "avec reprise par un pronom, à l'oral. Quant à, à l'écrit "
                      "soutenu.",
            notes="Diapositive à photographier. « Ce que je demande, c'est... » est "
                  "la meilleure façon de commencer la dernière phrase d'une "
                  "intervention : elle annonce la conclusion sans dire « en "
                  "conclusion ».")

    d.tableau('Analyse', "La même idée, cinq mises en relief",
              ['La phrase', 'Ce qu\'elle produit'],
              [["La procédure me dérange.",
                "phrase neutre - rien ne ressort"],
               ["C'est la procédure qui me dérange.",
                "on écarte tout le reste : ce n'est pas le projet"],
               ["Ce qui me dérange, c'est la procédure.",
                "on annonce, puis on livre : l'auditoire attend"],
               ["La procédure, elle me dérange.",
                "détachement parlé, très direct, bon à la radio"],
               ["Quant à la procédure, elle me dérange.",
                "registre soutenu, bon en tête de paragraphe"]],
              cle=0,
              notes="Diapositive à photographier. Faire lire les cinq à voix haute, "
                    "dans l'ordre : c'est en les entendant les unes après les autres "
                    "qu'on entend ce que chacune ajoute.")

    d.pratique('Pratique 2 de 3', "Mettre en avant ce qui compte",
               "Récrivez avec la tournure indiquée.", [
        ("La procédure me dérange, pas le projet. (c'est... qui)", "C'est la procédure qui me dérange, pas le projet."),
        ("Je demande la publication de l'évaluation. (ce que... c'est)", "Ce que je demande, c'est la publication de l'évaluation."),
        ("Une étude du terrain de l'aréna manque. (ce qui... c'est)", "Ce qui manque, c'est une étude du terrain de l'aréna."),
        ("On a voté à vingt-deux heures cinquante. (c'est... que)", "C'est à vingt-deux heures cinquante qu'on a voté."),
        ("Je veux ce document avant mardi. (détachement et pronom)", "Ce document-là, je le veux avant mardi."),
        ("L'évaluation n'a toujours pas été publiée. (quant à)", "Quant à l'évaluation, elle n'a toujours pas été publiée."),
    ], corrige=True,
       notes="Deux vigilances : « c'est moi qui ai », jamais « qui a » ; et une seule "
             "mise en relief par phrase. Deux dans la même phrase s'annulent, trois "
             "dans une intervention suffisent.")

    d.regle("Les relatives qui portent une préposition",
            "Cherchez la préposition que demande le verbe de la relative, "
            "puis le genre et le nombre de ce qu'elle reprend. Le pronom s'en "
            "déduit tout seul.",
            precision="De donne dont : un dossier dont tout le monde parle. À donne "
                      "auquel, à laquelle, auxquelles - ou « à qui » pour des "
                      "personnes. Les autres prépositions donnent lequel accordé : "
                      "sur lequel, pour lesquelles. Le lieu et le temps donnent où, "
                      "qui allège la phrase.",
            notes="Diapositive à photographier. Le dire franchement : ici, c'est un "
                  "savoir de lecture. Dans un éditorial, ce qui suit « dont » ou "
                  "« auquel » est presque toujours l'argument, et le pronom renvoie "
                  "parfois trois lignes plus haut.")

    d.pratique('Pratique 3 de 3', "Quel pronom relatif ?",
               "Complétez.", [
        ("C'est un projet ___ je m'oppose pour des raisons de procédure.", "auquel - s'opposer à"),
        ("L'assemblée ___ j'ai assisté jeudi a duré deux heures.", "à laquelle - assister à"),
        ("Voici les deux raisons ___ j'ai décidé de signer.", "pour lesquelles"),
        ("C'est un dossier ___ tout le monde parle depuis lundi.", "dont - parler de"),
        ("Le comité ___ le porte-parole est madame Sauvé compte trente membres.", "dont - jamais « dont son »"),
        ("Je n'oublierai pas le soir ___ le vote a été pris.", "où - le temps"),
    ], corrige=True,
       notes="Faire écrire le verbe et sa préposition au crayon avant de répondre : "
             "s'opposer à, assister à, parler de. La difficulté vient toujours de la "
             "préposition, jamais du pronom.")

    d.billet(
        "Écrivez trois phrases sur le dossier du boisé, une par tournure.",
        exemples=[
            "Une hypothèse irréelle : si la Ville avait..., je n'aurais pas...",
            "Une mise en relief : ce que je demande, c'est...",
            "Une relative à préposition : les raisons pour lesquelles...",
        ],
        notes="Devoir central du bloc. Ces trois phrases entreront telles quelles "
              "dans l'intervention de E1 et dans la lettre de E2 : le dire, cela "
              "change le soin qu'on y met.")

    return d.save(dossier)
