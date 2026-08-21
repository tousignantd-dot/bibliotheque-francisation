# -*- coding: utf-8 -*-
"""A2 · Deux mots qui se collent
Bloc A « Je découvre » · couleur indigo · 75 min. Graphie-phonie.
Source : exercice `prPhon`, mini-leçon `prPhon`.

Le gabarit est en Verdana : ni alphabet phonétique ni flèches. On dit donc
« la liaison se fait » et « elle ne se fait pas », et le trait bas marque
l'endroit où les deux mots se collent.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Deux mots qui se collent",
        chapeau="Au téléphone, la personne ne voit ni votre bouche ni vos "
                "mains : elle n'a que le rythme de vos mots. Une phrase "
                "sans liaisons arrive hachée, et il faut la faire répéter.",
        duree='75 minutes')

    d.titre(notes="Séance de prononciation, la seule du module. Commencer en disant deux "
                  "fois la même phrase : « vous avez un appel en attente », d'abord "
                  "mot par mot, puis normalement. Demander laquelle est plus facile à "
                  "comprendre. C'est toute la séance en dix secondes.")

    d.objectifs([
        "reconnaître une liaison à l'oreille ;",
        "faire les liaisons obligatoires après un déterminant et un pronom ;",
        "ne pas faire de liaison après « et » ni devant un h aspiré ;",
        "prononcer le s de liaison comme un z.",
    ])

    d.regle("La lettre muette se réveille",
            "La dernière lettre d'un mot, muette d'habitude, se colle au mot "
            "suivant quand celui-ci commence par une voyelle.",
            precision="Rien ne change à l'écrit : vous_avez, un_appel, les_heures "
                      "s'écrivent comme avant. Tout se joue dans l'oreille. Le trait "
                      "bas des exemples marque l'endroit où les deux mots se collent.",
            notes="Écrire au tableau « vous avez » puis « vous_avez » et faire dire les "
                  "deux. Le groupe entend la différence tout de suite ; c'est le nommer "
                  "qui est neuf.")

    d.cartes("Les liaisons obligatoires", "Trois cas, et ils couvrent presque tout", [
        ("Après un déterminant",
         "les_heures · un_appel · ces_employés · deux_appels"),
        ("Après un pronom sujet",
         "vous_avez · nous_attendons · ils_ont · on_arrive"),
        ("Après un petit mot",
         "très_occupée · en_avant · chez_elle · dans_une_heure"),
        ("Le principe, pour ne pas apprendre la liste",
         "Plus les deux mots sont soudés par le sens, plus la liaison est obligatoire."),
    ], notes="La quatrième carte évite l'apprentissage par cœur. Faire produire deux "
             "exemples de plus par le groupe pour chacun des trois premiers cas.")

    d.cartes("Les liaisons interdites", "Trois cas, et le premier n'a aucune exception", [
        ("Après « et », jamais",
         "et / elle · et / un formulaire · et / après"),
        ("Devant un h aspiré",
         "en / haut · les / haricots · le / hall"),
        ("Après un nom au singulier",
         "le bureau / ouvert · un appel / urgent"),
        ("Mais au pluriel, elle revient",
         "des appels_urgents · des bureaux_ouverts"),
    ], notes="Le « et » est la seule règle sans exception de la séance : le dire ainsi, "
             "les élèves s'y accrochent. Le h aspiré ne s'apprend pas : il se rencontre.")

    d.tableau('Le son de la lettre', "Elle ne se dit pas comme elle s'écrit",
              ['On écrit', 'On entend'],
              [["les heures", "lé-zeur"],
               ["deux appels", "deu-zappel"],
               ["vous avez", "vou-zavé"],
               ["un grand immeuble", "un gran-timmeuble"],
               ["neuf heures", "neu-veur"]],
              cle=1,
              note="Le s et le x se disent « z » · le d se dit « t » · le f de « neuf » "
                   "se dit « v » devant heures et ans.",
              notes="La colonne de droite n'est pas de l'alphabet phonétique : c'est une "
                    "transcription approximative, faite pour être lue à voix haute par le "
                    "groupe. La faire lire par trois élèves différents.")

    d.pratique('Écoute', "Est-ce que les deux mots se collent ?",
               "Écoutez, puis dites si la liaison se fait ou non.", [
        ("vous avez", "oui — vou-zavé"),
        ("un appel", "oui — un-nappel"),
        ("et elle", "non — jamais après « et »"),
        ("les heures", "oui — lé-zeur"),
        ("le bureau ouvert", "non — nom au singulier"),
        ("en haut", "non — h aspiré"),
        ("très occupée", "oui — trè-zoccupée"),
        ("deux appels", "oui — deu-zappel"),
    ], cols=2, corrige=True,
       notes="Faire répondre à main levée avant d'afficher la correction. Les deux "
             "erreurs attendues sont « et elle », que beaucoup lient, et « le bureau "
             "ouvert », que peu savent refuser.")

    d.piege("Prononcer le s comme un s",
            "les heures dit « lé-seur »",
            "les heures dit « lé-zeur »",
            "Le s et le x de liaison se disent « z ». C'est pour ça que « les heures » "
            "est si difficile à reconnaître la première fois : on cherche un mot qui "
            "commencerait par un z.",
            notes="Faire répéter « les heures, les employés, les appels » trois fois de "
                  "suite. C'est le groupe de mots le plus fréquent d'un bureau.")

    d.pratique('Répétition', "Six phrases du module",
               "Répétez chaque phrase deux fois : la première pour comprendre, "
               "la seconde en ne guettant que les liaisons.", [
        ("Vous êtes bien à la Coopérative d'aide à domicile.", "vous_êtes"),
        ("Un instant, je vous prie, je vérifie au registre.", "un_instant"),
        ("Nous avons deux employés à l'accueil ce matin.", "nous_avons, deux_employés"),
        ("Il est neuf heures et il n'est pas encore arrivé.", "neuf_heures, rien après « et »"),
        ("Elle a laissé son numéro et elle attend un rappel.", "elle_a, rien après « et »"),
        ("En haut de la page, en avant du formulaire.", "en / haut non, en_avant oui"),
    ], corrige=True,
       notes="Ces six phrases sont celles des extraits audio du module : les élèves les "
             "réentendront seuls dans la mini-leçon. Les faire répéter en groupe, puis "
             "individuellement à trois ou quatre élèves.")

    d.billet(
        "Écrivez trois groupes de mots de votre travail où la liaison se fait.",
        exemples=[
            "Marquez l'endroit où les deux mots se collent avec un trait bas.",
            "Ajoutez-en un où elle ne se fait pas, et dites pourquoi.",
        ],
        notes="Les groupes de mots trouvés par les élèves dans leur propre métier valent "
              "mieux que ceux du module. En noter quelques-uns pour les réemployer en A4.")

    return d.save(dossier)
