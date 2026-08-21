# -*- coding: utf-8 -*-
"""C4 · Lire l'article du lendemain
Bloc C « Défi 2 · L'article » · couleur teal · 75 min.
Source : exercices `t2nom`, `t2dates` et `t2lire`, mini-leçon `t2nom`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n7-actualite/images/')


def build(dossier):
    d = Deck(
        code='C4', section='teal',
        titre="Lire l'article du lendemain",
        chapeau="Trois passives, une nominalisation dans le titre, un "
                "conditionnel, et pas un seul « je » : c'est la signature "
                "d'un article informatif. Une fois qu'on la reconnaît, on lit "
                "beaucoup plus vite.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 2. Elle rassemble tout le bloc : le passif "
                  "de C2, le discours rapporté de C3, et la nominalisation qu'on "
                  "découvre aujourd'hui.")

    d.objectifs([
        "retrouver le verbe caché derrière un nom ;",
        "comprendre pourquoi les titres emploient des noms plutôt que des verbes ;",
        "distinguer ce qu'un article dit de ce qu'il ne dit pas ;",
        "situer les dates du dossier de la consigne.",
    ], notes="Le troisième objectif est le plus important et le plus difficile : "
             "beaucoup d'élèves complètent un texte avec ce qu'ils croient savoir.")

    d.declencheur(
        'Observation', "Pourquoi les titres n'ont-ils pas de verbe ?",
        image=IMG + 'journal-etale.jpg',
        pistes=[
            "« Le dépôt ouvrira en mars. »",
            "« Ouverture du dépôt en mars. »",
            "Lequel des deux tient dans un titre ?",
            "Lequel dit qui va ouvrir le dépôt ?",
        ],
        notes="La quatrième piste est le coeur de la séance : aucun des deux ne le dit, "
              "mais le second efface même la possibilité de le demander.")

    d.tableau('Analyse', "Les suffixes qui transforment un verbe en nom",
              ['Le suffixe', 'Des exemples'],
              [["-tion, -sion", "installer devient l'installation ; décider devient la décision"],
               ["-ment", "stationner devient le stationnement"],
               ["-ure", "ouvrir devient l'ouverture ; fermer devient la fermeture"],
               ["-age", "dépanner devient le dépannage"],
               ["sans suffixe", "reporter devient le report ; appeler devient l'appel"]],
              cle=0,
              note="Le genre suit le suffixe : -tion et -ure sont féminins, -ment et -age sont masculins.",
              notes="Diapositive à photographier. La règle de genre est presque sans "
                    "exception et règle beaucoup d'hésitations.")

    d.regle("Ce que la nominalisation efface",
            "Un nom ne dit ni qui a agi, ni quand.",
            precision="« Report de la décision » ne dit pas qui a reporté, ni si c'est "
                      "fait ou prévu. C'est très commode pour informer vite - et très "
                      "commode aussi pour ne désigner aucun responsable. Un titre "
                      "nominal mérite toujours qu'on lise l'article en dessous.",
            notes="Diapositive à photographier. Même logique que le passif sans « par » "
                  "vu en C2 : le faire remarquer, les deux procédés se combinent.")

    d.cartes("L'article du lendemain, en quatre observations", "Ce qu'il faut voir", [
        ("Le titre est nominal",
         "« Dépôt de consigne : Boisjoli en tête. » Aucun verbe conjugué."),
        ("Trois phrases passives",
         "a été retenu, sera prise, n'ont pas été fixées. Personne n'agit visiblement."),
        ("Un conditionnel",
         "« seraient réservées » : l'information n'est pas confirmée."),
        ("Pas un seul « je »",
         "Le journaliste ne se met jamais dans son texte. Une chronique, elle, ferait le contraire."),
    ], notes="Projeter l'article, puis cette diapositive. Le groupe doit pouvoir "
             "retrouver chaque observation dans le texte, en la pointant.")

    d.pratique('Application', "Du verbe au nom",
               "Remplacez le verbe souligné par le nom de la même famille.", [
        ("On installera le dépôt au printemps.", "l'installation du dépôt"),
        ("Le local ouvrira en mars.", "l'ouverture du local"),
        ("On a fermé la caisse il y a deux ans.", "la fermeture de la caisse"),
        ("On stationne devant le dépanneur.", "le stationnement devant le dépanneur"),
        ("Le conseil décidera le 14 octobre.", "la décision du conseil"),
        ("On a reporté le vote.", "le report du vote"),
        ("Les citoyens participent à la séance.", "la participation des citoyens"),
    ], corrige=True,
       notes="Attention au complément : « de + le » donne « du », « de + les » donne "
             "« des ». C'est le seul calcul à faire, et il se rate souvent.")

    d.pratique('Lecture', "Est-ce écrit dans le texte ?",
               "Attention : ne complétez pas avec ce que vous savez d'ailleurs.", [
        ("Le local de Boisjoli est l'emplacement recommandé.", "dans le texte"),
        ("Le conseil municipal tranchera le 14 octobre.", "dans le texte"),
        ("Marquette a été écarté parce qu'il est trop petit.", "pas dans le texte - la raison vient de l'entrevue, pas de l'article"),
        ("Deux places seraient réservées pour quinze minutes.", "dans le texte"),
        ("Le commerçant voisin s'oppose au projet.", "pas dans le texte - il s'inquiète du stationnement, ce n'est pas la même chose"),
        ("La Ville n'exploitera pas elle-même le dépôt.", "dans le texte"),
        ("Le journaliste trouve que la décision a trop tardé.", "pas dans le texte - un article informatif ne juge pas"),
    ], corrige=True,
       notes="Exercice central de la séance. Les trois « pas dans le texte » sont "
             "exactement les trois façons de se tromper : importer d'une autre source, "
             "durcir une nuance, prêter une opinion au journaliste.")

    d.billet(
        "Écrivez un titre nominal pour une nouvelle de votre semaine.",
        exemples=[
            "Un nom, pas de verbe conjugué. Cinq mots au maximum.",
            "Puis dites ce que votre titre n'apprend pas au lecteur.",
        ],
        notes="Fin du Défi 2. La seconde consigne est celle qui compte : elle vérifie "
              "que la lecture critique a suivi la grammaire.")

    return d.save(dossier)
