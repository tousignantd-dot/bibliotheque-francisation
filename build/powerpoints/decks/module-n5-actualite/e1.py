# -*- coding: utf-8 -*-
"""E1 · « Raconte-moi ça »
Bloc E « Je me lance » · couleur teal · 75 min.
Source : jeu de rôle `faitdivers`, production orale (message laissé à Teresa).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="« Raconte-moi ça »",
        chapeau="Deux productions orales. D'abord le récit joué avec "
                "l'assistant, qui n'a rien lu et qui fera préciser. Ensuite "
                "le message laissé à Teresa, à Granby : de quarante-cinq à "
                "soixante secondes, cinq morceaux, enregistré et déposé.",
        duree='75 minutes')

    d.titre(notes="Séance de production. Le jeu de rôle vient en premier parce qu'il "
                  "sert de répétition : c'est là que l'élève découvre que « il y a eu "
                  "un problème » ne fait comprendre la nouvelle à personne, et qu'une "
                  "information sans source se fait redemander.")

    d.objectifs([
        "raconter un fait divers d'un seul tenant à quelqu'un qui n'a rien lu ;",
        "croiser le passé composé et l'imparfait dans le même récit ;",
        "rapporter au moins une parole en nommant qui l'a dite ;",
        "terminer par un avis annoncé comme un avis, et justifié.",
    ], notes="Les quatre objectifs sont ceux de l'évaluation du module. Les projeter "
             "au début et les relire à la fin. Ils sont aussi les critères que "
             "l'assistant emploie pour sa rétroaction : l'élève ne doit pas les "
             "découvrir en même temps que sa note.")

    d.cartes("Trois nouvelles", "Choisissez la vôtre dans l'activité", [
        ("L'incendie de la rue Alexandre",
         "Quatre logements, onze sinistrés, la Croix-Rouge, une cause encore incertaine."),
        ("L'eau de la rue des Peupliers",
         "Trois jours de pluie, une dizaine de sous-sols, la Ville et ses sacs de sable."),
        ("Les trente vélos du quartier",
         "Des cabanons laissés ouverts, un numéro de série à noter, un témoin à minuit."),
        ("Le conseil",
         "Prenez celle dont vous connaissez le mieux les paroles rapportées."),
    ], notes="Les trois cas sont ceux des blocs B, C et D. Laisser choisir, mais "
             "signaler que le troisième est le plus exigeant : il demande un avis "
             "défendu contre un interlocuteur qui n'est pas d'accord.")

    d.tableau('Le jeu de rôle', "Ce que l'assistant fera, et ce qu'il ne fera pas",
              ['Il fait', 'Il ne fait pas'],
              [["Il écoute et il relance", "Il ne lit pas le journal à votre place"],
               ["Il demande où et quand", "Il ne devine pas la rue ni l'heure"],
               ["Il demande qui a dit ça", "Il n'accepte pas « il paraît que »"],
               ["Il donne son avis à lui", "Il n'est pas d'accord d'office"],
               ["Il vous tutoie du début à la fin", "Il ne corrige pas votre langue"]],
              cle=1,
              notes="Projeter avant d'ouvrir l'activité. Savoir que l'assistant "
                    "redemandera la source change complètement la préparation : les "
                    "élèves relisent leurs paroles rapportées avant de commencer.")

    d.regle("Cinq morceaux dans le message laissé à Teresa",
            "La nouvelle · le décor · le déroulement · une parole "
            "rapportée · votre avis et sa raison.",
            precision="Teresa habite Granby. Elle n'a rien lu, elle ne connaît pas "
                      "Sherbrooke, et elle voudra savoir qui a dit quoi. Écrivez "
                      "votre message, lisez-le une fois à voix haute, puis "
                      "enregistrez : de quarante-cinq à soixante secondes.",
            notes="Diapositive à photographier, et à laisser au tableau pendant "
                  "l'enregistrement. Faire écrire le message avant de l'enregistrer : "
                  "personne n'improvise un bon message d'une minute.")

    d.tableau('Le plan du message', "Cinq temps, cinq phrases",
              ['Le temps', 'Ce qu\'il contient'],
              [["TEMPS 1", "La nouvelle : ce qui est arrivé, où, quand"],
               ["TEMPS 2", "Le décor, à l'imparfait : l'heure, la rue, les gens"],
               ["TEMPS 3", "Le déroulement, au passé composé : deux ou trois évènements"],
               ["TEMPS 4", "Une parole rapportée, avec le nom de qui l'a dite"],
               ["TEMPS 5", "Votre avis, annoncé comme un avis, et sa raison"]],
              cle=0,
              notes="Ce plan est celui de la carte de production orale de l'activité. "
                    "Le faire recopier avant d'écrire : les élèves qui écrivent sans "
                    "plan produisent un message de deux minutes qui n'en dit pas "
                    "plus.")

    d.cartes("Trois étapes de l'enregistrement", "Ce que dit le panneau de l'activité", [
        ("Je m'enregistre",
         "De quarante-cinq à soixante secondes, après avoir écrit son texte."),
        ("Je m'écoute et je corrige",
         "Comme si vous étiez Teresa, à Granby, qui n'a rien lu du tout."),
        ("J'envoie à mon enseignant",
         "Rien ne part sans un geste de l'élève : la correction reste privée."),
    ], notes="Le deuxième temps est celui qu'on saute. Trois questions à se poser en "
             "s'écoutant : sait-on ce qui est arrivé dès la première phrase ? "
             "peut-on dire qui a affirmé quoi ? sait-on où s'arrête le journal et où "
             "commence l'avis ?")

    d.pratique('Autocorrection', "Écoutez-vous, et vérifiez",
               "Six questions à se poser avant d'envoyer.", [
        ("Est-ce que la nouvelle est dite dès la première phrase ?", "sinon, l'autre attend encore"),
        ("Est-ce que je dis où et quand ?", "une rue, une heure, un jour"),
        ("Y a-t-il au moins une phrase à l'imparfait ?", "le décor : l'heure, le temps, les gens"),
        ("Y a-t-il deux évènements au passé composé, dans l'ordre ?", "ce qui bouge"),
        ("Est-ce que je nomme la personne qui a parlé ?", "pas de « il paraît que »"),
        ("Est-ce que mon avis est annoncé comme un avis ?", "et justifié avec « parce que »"),
    ], corrige=True,
       notes="Faire cocher les six points en s'écoutant, avant l'envoi. Ce sont "
             "exactement les critères que l'assistant reprendra dans sa rétroaction.")

    d.piege("Commencer par le détail au lieu de la nouvelle",
            "Allô Teresa. Bon, il était quatre heures du matin…",
            "Allô Teresa, c'est Marisol. Un immeuble a passé au feu cette nuit.",
            "Sur un répondeur, l'autre ne peut pas vous arrêter pour demander de quoi "
            "vous parlez. La première phrase doit tenir debout toute seule : qui "
            "appelle, et ce qui est arrivé.",
            notes="Le piège de B1, revenu au moment où il coûte le plus cher. Faire "
                  "réécouter à haute voix un message qui commence par l'heure : "
                  "l'effet se comprend immédiatement.")

    d.piege("Mêler le journal et son propre avis",
            "Les gens ne barrent rien, et la police ne fait pas assez.",
            "La police demande de noter le numéro. Moi, je trouve que ce n'est pas assez.",
            "Teresa répétera votre message à quelqu'un d'autre. Si vos deux phrases "
            "sont collées, votre avis voyagera comme s'il était écrit dans le "
            "journal.",
            notes="Dernier rappel avant l'enregistrement. Le dire en une phrase : "
                  "d'abord les faits avec leur source, ensuite l'avis, annoncé comme "
                  "tel, jamais les deux dans la même phrase.")

    d.billet(
        "Notez une chose que l'assistant vous a fait préciser et que vous n'aviez pas prévue.",
        exemples=[
            "Une seule chose, en une phrase.",
            "Notez aussi ce que vous direz différemment dans le courriel de E2.",
        ],
        notes="Les billets de cette séance sont les plus utiles du module : ils disent "
              "exactement ce qui manque encore, juste avant la production écrite de "
              "E2. Les lire avant la séance suivante.")

    return d.save(dossier)
