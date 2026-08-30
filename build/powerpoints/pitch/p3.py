# -*- coding: utf-8 -*-
"""P3 · Les questions de conformité — Loi 25, sans détour.
Section ambre · le cinquième quart d'heure d'une rencontre.
Source : `assets/presentations/loi-25.html`, qui porte l'inventaire des flux.
"""
from theme import Deck
from vues import ecran, poser
from chiffres import CH, n
from parcours import TEMPS


def build(dossier):
    d = Deck(
        code='P3', section='ambre',
        titre="Les questions de conformité",
        chapeau="Les poser soi-même plutôt que les subir. Ce qui sort du serveur, ce "
                "qui n'en sort jamais, et les trois choses que la loi demande avant de "
                "communiquer hors Québec.",
        duree='6 minutes')

    d.titre(surtitre="PRÉSENTATION  ·  3 SUR 3",
            notes="Ouvrir en disant que cette partie n'attend pas la question : c'est "
                  "nous qui la posons. Une direction qui découvre un flux après coup ne "
                  "revient pas.")

    d.parcours(TEMPS, 2,
               notes="Dernier temps, le plus court. Annoncer qu'on va au-devant "
                     "des questions plutôt que de les attendre.")

    d.chapitre("TROISIÈME TEMPS", "Les questions de conformité",
               "Ce qui sort du serveur, ce qui n'en sort jamais, et les trois "
               "choses que la loi demande.",
               notes="Jalon. Le ton change ici : on ne vend plus, on rend des "
                     "comptes.")

    d.objectifs([
        "savoir ce qui quitte le serveur, et vers où ;",
        "savoir ce qui n'en sort jamais, et pourquoi c'est écrit dans le code ;",
        "connaître les trois exigences de l'article 70.1 avant une sortie du Québec ;",
        "repartir avec la liste de ce que le centre doit décider lui-même.",
    ])

    d.regle('Le principe',
            "Rien n'atteint l'enseignant sans un geste de l'élève.",
            precision="Les corrections de l'assistant s'affichent à l'écran et ne "
                      "s'écrivent nulle part. Ce qui remonte, c'est ce que l'élève a "
                      "choisi d'envoyer — un enregistrement, un texte — jamais ce qu'il "
                      "a essayé.",
            notes="Cette phrase désamorce la moitié des inquiétudes. La dire lentement.")

    d.tableau('L\'inventaire', "Ce qui franchit la frontière, et ce qui reste",
              ['Le flux', 'Ce qui part', 'Vers'],
              [["Les routes d'assistance", "les textes et les réponses de l'élève",
                "Anthropic, États-Unis"],
               ["La reconnaissance vocale", "la voix de l'élève, en continu",
                "Google ou Apple, selon le navigateur"],
               ["La synthèse des voix", "du texte de module, jamais d'élève",
                "Azure"],
               ["Tout le reste", "rien ne sort", "le serveur"]],
              cle=0,
              note="La reconnaissance vocale se ferme par le réglage du micro ; les "
                   "routes d'assistance, par celui de l'assistant.",
              notes="Ne pas cacher la première ligne : c'est elle qui rend le reste "
                    "crédible. L'inventaire complet est dans la page Loi 25.")

    d.cartes('Ce qui ne sort jamais', "Écrit dans le code, pas dans une promesse",
             [("Le vrai nom", "Le portail ne connaît que des pseudonymes. "
               "L'enseignant refait le lien, hors de l'outil."),
              ("Les corrections de l'assistant", "Affichées, jamais enregistrées. "
               "Le registre des appels compte des jetons et ne garde aucun texte."),
              ("Le texte des réponses ouvertes", "Le tableau de classe reçoit juste ou "
               "faux et le nombre d'essais ; le serveur jette le reste."),
              ("La voix, si le centre le décide", "Trois états : l'enregistrement gardé, "
               "la transcription seule, ou rien du tout.")],
             notes="La quatrième carte est celle qui intéresse un conseiller juridique : "
                   "la transcription ferme le passif sans coûter la production orale.")

    ecran(d, "Ce que la direction voit", "L'espace direction",
          poser('cas', '13-espace-direction'),
          "Les comptes du centre, les réglages, et la dépense estimée. Aucune "
          "réponse d'élève n'y figure.",
          notes="La question qui suit est toujours « et les données des élèves ? ». "
                "La réponse est à l'écran : elles n'y sont pas.")

    d.regle("La règle de l'article 70.1",
            "Hors Québec est permis, à trois conditions.",
            precision="Une évaluation des facteurs relatifs à la vie privée faite avant "
                      "la communication ; une conclusion de protection adéquate ; une "
                      "entente écrite qui en tient compte. Sans évaluation, ce qui est "
                      "en défaut, c'est le flux — pas l'emplacement du disque.",
            notes="« Hors Québec » comprend l'Ontario : un hébergement à Toronto est une "
                  "sortie au même titre qu'en Virginie. Le dire avant qu'on le demande.")

    d.piege('L\'idée reçue',
            "« Il faut héberger au Québec. »",
            "« Il faut avoir fait l'évaluation, et l'avoir écrite. »",
            "C'est une condition à la sortie, pas une frontière fermée. L'inventaire des "
            "flux existe justement pour alimenter cette évaluation.",
            notes="Si la personne insiste, proposer le mode sans assistant : plus aucun "
                  "texte d'élève ne quitte le serveur, et la question tombe.")

    d.tableau('Ce que le centre décide', "Quatre décisions qui ne sont pas techniques",
              ['La décision', 'Ce qu\'elle demande'],
              [["La durée de conservation", "combien de temps on garde les traces d'un "
                "élève après son départ"],
               ["La communication hors Québec", "l'évaluation, la conclusion, l'entente"],
               ["Qui a accès", "les comptes de direction, et ce qu'ils voient"],
               ["Le responsable", "la personne qui répond d'une demande d'accès"]],
              note="Aucune ne demande de développement : trois interrupteurs sont déjà "
                   "construits, celles-ci s'écrivent.",
              notes="Terminer là-dessus : ce sont des décisions d'organisme, pas des "
                    "fonctionnalités à attendre.")

    ecran(d, "Sans rien collecter", "Une classe entière, sans un compte",
          poser('cas', '04-suivi-seance'),
          "Le suivi de l'enseignant est le même écran. Les élèves s'appellent "
          "« Participant 3 » : il n'existe aucune donnée pour les nommer.",
          notes="C'est la réponse la plus courte à la Loi 25 : on ne protège pas "
                "une donnée qu'on n'a pas créée.")

    d.billet("La question à emporter : qui, chez vous, signe l'évaluation des facteurs "
             "relatifs à la vie privée ?",
             exemples=["Le guide pour la direction contient le modèle et les articles.",
                       "Un groupe pilote sans assistant n'attend aucune de ces réponses."],
             notes="Donner le guide en partant. C'est le document qui fait avancer le "
                   "dossier entre deux rencontres.")

    return d.save(dossier)
