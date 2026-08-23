# -*- coding: utf-8 -*-
"""C4 · « Ils », et les mots qui reprennent
Bloc C « Défi 2 » · couleur teal · écoute et réponds · 75 min.
Source : exercices `t2ils`, `t2subst` et `t2deux`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='teal',
        titre="« Ils », et les mots qui reprennent",
        chapeau="« L'usine a rouvert en mars. Ils ont investi douze "
                "millions. » Qui, « ils » ? Personne ne l'a dit — et vous "
                "n'avez rien manqué.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 2. Elle règle la deuxième grande cause de "
                  "perte du fil dans un texte long, après la nominalisation de A4.")

    d.objectifs([
        "reconnaître un « ils » qui ne reprend aucun groupe nommé ;",
        "chercher le référent dans le paragraphe, pas dans la phrase ;",
        "repérer les quatre façons de reprendre un mot sans le répéter ;",
        "achever sa feuille de comparaison à deux colonnes.",
    ], notes="Le deuxième objectif est un geste de lecture, pas une règle : remonter "
             "d'un paragraphe. Le faire faire trois fois dans la séance.")

    d.declencheur(
        'Observation', "À qui renvoie « ils » ?",
        pistes=[
            "« L'usine a rouvert en mars. Ils ont investi douze millions. »",
            "Cherchez le mot au pluriel dans la première phrase.",
            "Il n'y en a pas. Est-ce une faute ?",
            "De qui parle-t-on, alors ?",
        ],
        notes="Laisser chercher une bonne minute. La découverte qu'il n'y a rien à "
              "trouver est le cœur de la séance : plusieurs élèves relisent ce genre "
              "de phrase cinq fois en croyant s'être trompés.")

    d.regle("Un « ils » peut n'avoir aucun antécédent écrit",
            "Il désigne alors les décideurs sans les nommer : l'entreprise, "
            "la direction, la municipalité, le gouvernement.",
            precision="C'est ce qu'on appelle un référent implicite. Le contexte "
                      "tranche : si le paragraphe parle d'une usine, ce sont ses "
                      "propriétaires ; s'il parle d'un budget, c'est le "
                      "gouvernement. Et quand rien ne tranche, c'est que la phrase "
                      "ne veut pas qu'on tranche.",
            notes="Diapositive à photographier. Ajouter le « ils » du français parlé "
                  "au Québec, prononcé [i] ou [j] : « Y ont fermé à cinq heures. » "
                  "C'est du français standard, pas une négligence.")

    d.cartes('Analyse', "Retrouver le référent dans le paragraphe", [
        ("La direction a présenté son plan au conseil. Ils ont approuvé.", "le conseil"),
        ("Le laboratoire compte sept personnes. Ils cherchent deux techniciens.", "le laboratoire, comme équipe"),
        ("Le gouvernement a publié le portrait. Ils y donnent le PIB.", "le gouvernement"),
        ("Elle a appelé les ressources humaines. Ils ont demandé son dossier.", "le service des ressources humaines"),
        ("Le budget a été voté en avril. Ils avaient promis un centre.", "des élus — aucun nom n'est donné"),
    ], cols=1,
       notes="Exercice `t2ils` du module interactif. La dernière carte est la plus "
             "importante : « aucun nom n'est donné » est une réponse acceptable, et "
             "souvent la seule honnête.")

    d.piege('Écriture',
            "« ils m'ont demandé de former deux techniciennes »",
            "« la direction m'a demandé de former deux techniciennes »",
            "Ce flou est permis au journaliste, dont le sujet est le fait. "
            "Dans une lettre de candidature, il laisse penser que vous ne "
            "savez pas qui vous employait. Précision et responsabilité vont "
            "ensemble ; c'est vrai aussi de « on ».",
            notes="Point à répéter avant le bloc D. Le « on » vague est encore plus "
                  "fréquent que le « ils » dans les lettres d'élèves.")

    d.tableau('Analyse', "Quatre façons de reprendre un mot",
              ['Le procédé', 'Le mot, puis sa reprise'],
              [["Synonyme", "une usine, une fabrique"],
               ["Mot générique", "l'aluminium, ce métal"],
               ["Nominalisation", "on a embauché, cette embauche"],
               ["Périphrase", "le Saguenay, cette région du nord du fleuve"]],
              cle=0,
              note="Le signal le plus fiable : un « ce » ou un « cette » devant un mot très général.",
              notes="Diapositive à photographier. La troisième ligne fait la jonction "
                    "avec A4 : la nominalisation sert aussi à reprendre.")

    d.pratique('Lecture', "Qu'est-ce qui reprend quoi ?",
               "Associez le mot et sa reprise.", [
        ("l'aluminium", "ce métal"),
        ("le Saguenay–Lac-Saint-Jean", "cette région du nord du fleuve"),
        ("l'usine de Jonquière", "l'établissement"),
        ("on a embauché douze personnes", "cette embauche"),
        ("les techniciennes et les techniciens", "ce personnel spécialisé"),
        ("la transformation du bois", "cette activité"),
    ], corrige=True,
       notes="Exercice `t2subst` du module interactif. Faire remarquer que la reprise "
             "est presque toujours un peu plus vague que le mot de départ : c'est "
             "normal, et c'est même son intérêt.")

    d.pratique('Compréhension', "Achevez la comparaison",
               "Complétez d'après le portrait et le dialogue.", [
        ("Le Saguenay transforme surtout des ressources ___ .", "naturelles"),
        ("Chaudière-Appalaches transforme surtout des ___ et du métal ouvré.", "aliments"),
        ("Le secteur primaire du Saguenay pèse ___ fois la moyenne québécoise.", "deux"),
        ("La construction y occupe 8,9 %, contre ___ % au Québec.", "7,0"),
        ("Les services y représentent plus des trois ___ de l'emploi.", "quarts"),
        ("Pour savoir s'il manque de la main-d'œuvre, il faut consulter ___ .", "IMT en ligne"),
    ], corrige=True,
       notes="Exercice `t2deux` du module interactif. La dernière réponse ferme le "
             "Défi 2 : un portrait ne dit jamais le manque.")

    d.billet(
        "Troisième ligne de votre feuille : votre famille pourrait-elle vivre dans cette région ?",
        exemples=[
            "Aucun document ne répondra à votre place.",
            "Écrivez ce qui vous retient, et ce qui vous attire.",
        ],
        notes="Fin de la feuille de comparaison commencée en C1. Elle devient le plan "
              "de l'exposé oral du bloc E : le dire maintenant, pour que personne ne "
              "la jette.")

    return d.save(dossier)
