# -*- coding: utf-8 -*-
"""D2 · Elle ouvrit un atelier, et on nomma le poste
Bloc D « Défi 3 · Le compte rendu » · couleur teal · 75 min.
Source : exercices `t3ps`, `t3nom` et `t3si`, leurs mini-leçons. Savoirs du
programme : reconnaître les verbes courants au passé simple à la 3e personne
et les associer au passé composé ; employer des procédés de substitution
lexicale ; exprimer la condition dans une hypothèse avec « si ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='teal',
        titre="Elle ouvrit un atelier, et on nomma le poste",
        chapeau="Un temps qu'on ne parle jamais et qu'on lit tout le temps, "
                "une façon d'écrire court, et la petite conjonction qui "
                "permet de demander sans accuser.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 3. Trois points, et le troisième — « si » — "
                  "est celui qui sert le plus dans la vraie vie : garder du temps pour "
                  "lui.")

    d.objectifs([
        "reconnaître un passé simple et le traduire par un passé composé ;",
        "remplacer un verbe par le nom de la même famille ;",
        "reprendre une phrase par un nom précédé de « cette » ou « ce » ;",
        "poser une hypothèse avec « si » sans mettre de futur après « si ».",
    ], notes="Le premier objectif est un objectif de reconnaissance seulement : le "
             "programme ne demande pas de produire un passé simple, et il ne faut pas "
             "le faire écrire.")

    d.declencheur(
        'Observation', "« En 1961, Aline Bocage ouvrit un petit atelier. » Est-ce du passé ou du futur ?",
        pistes=[
            "Où as-tu déjà lu des formes comme celle-là ?",
            "Comment le dirais-tu en parlant ?",
            "Qu'est-ce qui te le fait deviner : la forme, ou la date ?",
        ],
        notes="La réponse — c'est la date qui tranche — est la stratégie de la "
              "séance. Beaucoup d'élèves lisent « il fut » comme un futur, à cause "
              "des lettres.")

    d.tableau('Analyse', "Le passé simple, et ce qu'on dit en parlant",
              ['Ce qui est écrit', "Ce qu'on dit"],
              [["elle ouvrit un atelier", "elle a ouvert un atelier"],
               ["l'entreprise déménagea", "l'entreprise a déménagé"],
               ["un client perdit un lot", "un client a perdu un lot"],
               ["ils choisirent une employée", "ils ont choisi une employée"],
               ["ce fut le premier poste", "ça a été le premier poste"],
               ["les propriétaires eurent une idée", "ils ont eu une idée"]],
              cle=0,
              notes="Diapositive à photographier. Six rangées sans note. Insister sur "
                    "les deux dernières : « fut » et « eurent » ne ressemblent à rien "
                    "et s'apprennent tels quels.")

    d.regle("Le reconnaître, jamais l'écrire",
            "Le passé simple est le temps du récit écrit — jamais celui d'une conversation ni d'un courriel.",
            precision="Terminaisons de la troisième personne : -a et -èrent pour les "
                      "verbes en -er, -it et -irent pour beaucoup d'autres, -ut et "
                      "-urent pour quelques-uns. Le meilleur repère à l'œil est "
                      "l'absence d'auxiliaire : un passé composé a toujours « avoir » "
                      "ou « être » devant lui.",
            notes="Diapositive à photographier. Le dire clairement : personne ne vous "
                  "demandera d'en écrire un au travail, et en employer un à l'oral "
                  "vous ferait remarquer.")

    d.pratique('Pratique', "Dis-le comme on le dirait en parlant",
               "Traduisez chaque forme par un passé composé.", [
        ("l'atelier grandit lentement", "l'atelier a grandi lentement"),
        ("elle prit un nouveau nom", "elle a pris un nouveau nom"),
        ("ils choisirent une employée de l'expédition", "ils ont choisi une employée"),
        ("ce fut le premier poste du genre", "ça a été le premier poste du genre"),
        ("les propriétaires eurent alors une idée simple", "ils ont eu une idée simple"),
    ], corrige=True,
       notes="Le premier item est ambigu — « grandit » peut être un présent. Le "
             "signaler : c'est la date qui tranche, et dans un récit tous les verbes "
             "sont au même temps.")

    d.tableau('Analyse', "Nommer au lieu de raconter",
              ['On dit', 'Le compte rendu écrit'],
              [["on a affiché le poste", "l'affichage du poste"],
               ["elle s'est portée candidate", "sa candidature"],
               ["le comité a sélectionné", "la sélection"],
               ["on a décidé", "la décision"],
               ["on remplacera Yaneth", "le remplacement de Yaneth"],
               ["elle a suivi une formation", "sa formation"]],
              cle=0,
              notes="Diapositive à photographier. C'est la séance A3 qui revient, "
                    "appliquée à un texte réel. Rappeler les suffixes : -tion, -ment, "
                    "-age, -ure.")

    d.regle("Le nom reprend la phrase d'avant",
            "« Le comité a rencontré les candidats. Cette rencontre a duré trente minutes. »",
            precision="Le nom ne sert pas seulement à écrire court : il reprend toute "
                      "la phrase précédente sans la recopier. C'est de la reprise de "
                      "l'information, exactement comme « le », « en » et « y » du "
                      "Défi 1 — et c'est le déterminant démonstratif, « cette », "
                      "« ce », « cet », qui fait le lien.",
            notes="Diapositive à photographier. Faire produire deux paires de phrases "
                  "au tableau. Sans le démonstratif, le nom paraît tomber de nulle "
                  "part : le montrer en enlevant « cette ».")

    d.pratique('Pratique', "Poser une condition avec « si »",
               "Complétez. Jamais de futur juste après « si ».", [
        ("Si tu ___ (remplir) le formulaire avant vendredi, il sera reçu.", "remplis"),
        ("Si le comité l'accepte, elle ___ (commencer) au début d'octobre.", "commencera"),
        ("Si vous ___ (avoir) suivi la formation, vous êtes admissible.", "avez"),
        ("Si ça ne convient pas, ___ (revenir) à ton ancien poste.", "reviens"),
        ("Si personne à l'interne ne ___ (convenir), le poste sort à l'externe.", "convient"),
        ("Si tu ___ (vouloir) mon avis, prépare trois exemples précis.", "veux"),
    ], corrige=True,
       notes="Faire remarquer que le futur apparaît dans la seconde moitié, jamais "
             "dans celle qui commence par « si ». C'est toute la règle.")

    d.piege('Piège', "si tu viendras demain",
            "si tu viens demain",
            "Jamais de futur juste après « si ». Le futur va dans l'autre moitié de la "
            "phrase, celle qui dit la conséquence : « si tu viens demain, je te "
            "montrerai le formulaire ». C'est la faute la plus fréquente à tous les "
            "niveaux, et elle s'entend tout de suite.",
            notes="Ajouter la nuance si le groupe est solide : « je me demande si elle "
                  "viendra » n'est pas une condition mais une question rapportée, et "
                  "là le futur est permis. Sinon, la garder pour une autre fois.")

    d.pratique('Bilan du bloc', "Poser sa question à la rencontre",
               "En équipes de deux : une question avec « si », et sa réponse.", [
        ("Si je ne suis pas choisie, est-ce que je peux me présenter l'an prochain ?", "au contraire, le comité garde une note"),
        ("Si deux personnes se valent, qu'est-ce qui décide ?", "l'ancienneté départage, article 4.3"),
        ("Si ça ne me convient pas après un mois ?", "droit de retour, aux mêmes conditions"),
        ("Si personne à l'interne ne se présente ?", "le poste sort à l'externe"),
    ], corrige=True,
       notes="Répétition du jeu de rôle d'E1. Insister sur ce que « si » permet : "
             "poser une question difficile sans accuser personne. C'est un outil de "
             "travail, pas seulement une règle de grammaire.")

    d.billet(
        "Écris une question avec « si » que tu poserais à ton employeur.",
        exemples=[
            "Une seule phrase.",
            "Vérifie qu'il n'y a pas de futur juste après « si ».",
        ],
        notes="Cinq minutes. Ramasser : c'est la mesure du bloc D, et la matière "
              "première du jeu de rôle d'E1.")

    return d.save(dossier)
