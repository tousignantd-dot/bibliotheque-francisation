# -*- coding: utf-8 -*-
"""C4 · Ce qui aura lieu, et le message qui le dit
Bloc C « Défi 2 · La décision, et pourquoi » · couleur teal · 75 min.
Source : exercices `t2fut` et `t2msg`, et leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='teal',
        titre="Ce qui aura lieu, et le message qui le dit",
        chapeau="Une décision s'annonce toujours au futur : la nouvelle date, "
                "l'heure, le lieu. Deux futurs se partagent le travail, et "
                "un message de deux lignes réunit tout le Défi 2.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 2. Ouvrir en lisant trois des billets de C3 : "
                  "le groupe entend six versions de la même décision et choisit. On "
                  "passe ensuite au temps du verbe, puis à la phrase complète.")

    d.objectifs([
        "employer le futur proche à l'oral et le futur simple à l'écrit ;",
        "ne jamais mettre le futur après « si » ;",
        "écrire la décision et sa raison dans la même phrase ;",
        "donner la nouvelle date, l'heure et le lieu du premier coup.",
    ])

    d.regle("Deux futurs, deux distances",
            "Je vais vous rappeler ce soir. La sortie aura lieu le 22 février.",
            precision="Le futur proche — aller au présent + l'infinitif — est celui "
                      "du téléphone : il donne l'impression que c'est déjà parti. Le "
                      "futur simple est celui de l'avis affiché et du courriel : "
                      "devant un groupe, il fait sérieux et il engage. Les deux "
                      "cohabitent dans le même message sans que personne trouve cela "
                      "bizarre.",
            notes="Diapositive à photographier. Faire relever dans le message de "
                  "Marisol lequel des deux futurs revient le plus : c'est le proche, à "
                  "l'oral, et le simple dès qu'une date est fixée.")

    d.piege("Le futur après « si »",
            "Si l'avertissement sera levé…",
            "Si l'avertissement est levé, nous maintiendrons la sortie.",
            "Présent après « si », futur dans l'autre moitié de la phrase. C'est la "
            "faute la plus fréquente du niveau, et elle s'entend tout de suite. La "
            "corriger une fois pour toutes vaut mieux que la reprendre dix fois.",
            notes="Faire produire trois phrases en « si » par élève, à l'oral, avant "
                  "de passer à l'écrit. L'oreille prend l'habitude plus vite que la "
                  "main.")

    d.tableau('Analyse', "Ce que le futur ne fait pas",
              ["La phrase", "Ce que le lecteur entend"],
              [["La sortie sera peut-être reportée.", "elle hésite encore"],
               ["La sortie est reportée.", "c'est décidé, c'est fait"],
               ["Je vous confirmerai vendredi.", "elle n'a pas tranché"],
               ["La sortie aura lieu le 22 février.", "la date est fixée"]],
              cle=1,
              note="Une décision prise se dit au présent : il est plus ferme que le "
                   "futur.",
              notes="Diapositive à photographier. C'est le point le plus utile de la "
                    "séance, et le plus contre-intuitif : le futur adoucit, donc il "
                    "affaiblit une décision déjà prise.")

    d.pratique('Grammaire', "Futur proche ou futur simple ?",
               "Complétez selon ce que la phrase demande.", [
        ("Je ___ (rappeler) dès que j'aurai la confirmation.", "vais vous rappeler"),
        ("La sortie ___ (avoir lieu) le samedi 22 février, à treize heures.", "aura lieu"),
        ("Ça ___ (commencer) dans une heure environ.", "va commencer"),
        ("Je vous ___ (confirmer) vendredi à midi au plus tard.", "confirmerai"),
        ("Si l'avertissement ___ (être) levé jeudi, nous maintiendrons la sortie.", "est"),
        ("Nous ___ (partir) du Centre à treize heures précises.", "partirons"),
    ], corrige=True, cols=2,
       notes="Ce sont les six items de l'exercice `t2fut`. Faire dire à voix haute "
             "avant d'écrire : le proche et le simple se choisissent d'abord à "
             "l'oreille.")

    d.cartes("Le message au groupe", "Quatre exigences, et rien de plus", [
        ("Une phrase, deux moitiés",
         "La décision et la raison. L'ordre se choisit selon ce que le lecteur doit "
         "retenir en premier."),
        ("La décision porte la nouvelle date",
         "« Reportée » laisse trente personnes sans réponse ; « reportée au 22, même "
         "heure, même endroit » les règle toutes."),
        ("Une raison, pas trois",
         "La plus forte, et on s'arrête. Trois raisons alignées donnent l'air de se "
         "justifier — et on se fait discuter."),
        ("Une ligne pour la suite",
         "Ce que le lecteur doit faire : rien, appeler avant jeudi, confirmer. Sans "
         "elle, chacun invente sa marche à suivre."),
    ], notes="Diapositive à photographier. Les quatre points sont la grille de "
             "correction du billet, et celle de la production écrite de E2.")

    d.pratique('Écriture', "La décision et sa raison, dans la même phrase",
               "Une phrase par situation. Rien d'autre que la décision et la "
               "raison.", [
        ("Verglas · trottoirs glacés · marche du 8 · nouvelle date : le 22, 13 h.",
         "Comme un avertissement de pluie verglaçante est en vigueur, la marche est reportée au samedi 22, à treize heures."),
        ("Crue printanière · sentiers inondés · visite du Bic dimanche · le parc rouvre dans deux semaines.",
         "La visite du parc du Bic est reportée, parce que la crue a inondé les sentiers du bas du parc."),
        ("Chaleur extrême · indice UV de neuf · pétanque samedi 14 h · déplacée à 9 h.",
         "Étant donné l'avertissement de chaleur extrême, la pétanque est déplacée à neuf heures du matin."),
        ("Tempête · le spectacle passe une seule fois · aucune autre date.",
         "Le spectacle est annulé, puisqu'une tempête est annoncée et qu'aucune autre date n'est possible."),
    ], corrige=True,
       notes="Ce sont les quatre situations de l'exercice `t2msg`. Les corrigés "
             "proposés ne sont pas les seuls justes : faire lire deux versions "
             "d'élèves avant d'afficher la correction, et comparer.")

    d.billet(
        "Écrivez votre message au groupe pour la situation du verglas : deux lignes, pas plus.",
        exemples=[
            "Une phrase pour la décision et la raison, une ligne pour ce qu'il faut faire.",
            "Relisez-vous en vous demandant : est-ce que quelqu'un rappellerait pour poser une question ?",
        ],
        notes="Ramasser les billets. Ils sont le brouillon du message vocal de E1 : "
              "les rendre au début de cette séance-là, et non corrigés.")

    return d.save(dossier)
