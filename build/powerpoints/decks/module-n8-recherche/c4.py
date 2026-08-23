# -*- coding: utf-8 -*-
"""C4 · Les mots qui articulent, et ceux qui renvoient
Bloc C « Défi 2 » · couleur teal · 75 min.
Source : exercices `t2conn` et `t2rel`, et leurs mini-leçons. Savoirs du
niveau 8 : les connecteurs argumentatifs (opposition, concession,
complémentation, conclusion) et les relatifs qui portent une préposition.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='teal',
        titre="Certes, en revanche, dont, auquel",
        chapeau="Les phrases longues d'un document d'entreprise tiennent sur "
                "deux familles de mots : ceux qui articulent un raisonnement, "
                "et ceux qui renvoient à ce qui précède.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire dense. La couper en deux moitiés nettes : "
                  "connecteurs d'abord, relatifs ensuite, avec une pause entre les "
                  "deux. Ne pas mélanger.")

    d.objectifs([
        "employer les connecteurs d'opposition, de concession, d'ajout et de conclusion ;",
        "concéder avant d'avancer : certes... mais, bien que... soit ;",
        "choisir le relatif d'après la préposition que demande le verbe ;",
        "ne jamais écrire « dont » avec un second « de ».",
    ], notes="Le deuxième objectif est le plus rentable de tout le module : c'est le "
             "mouvement qui change ce qu'un comité pense d'un candidat.")

    d.declencheur(
        'Observation', "Le même couple de faits, quatre articulations",
        pistes=[
            "L'acquisition n'a supprimé aucun emploi. Elle a réorganisé la production.",
            "... en revanche, elle a réorganisé la production.",
            "... par ailleurs, elle a réorganisé la production.",
            "... par conséquent, elle a réorganisé la production.",
        ],
        notes="Trois connecteurs, trois sens complètement différents pour deux faits "
              "identiques. Faire dire au groupe ce que chacun change avant de nommer "
              "les familles.")

    d.cartes('Analyse', "Quatre familles de connecteurs", [
        ("Opposer",
         "en revanche, par contre, alors que, tandis que. Deux faits vrais "
         "qui se contredisent, et qui gardent le même poids."),
        ("Concéder",
         "certes... mais, bien que plus le subjonctif, même si plus "
         "l'indicatif. On donne raison, puis on avance. C'est la forme reine "
         "de l'entrevue."),
        ("Ajouter",
         "de plus reste sur le même sujet, par ailleurs change légèrement "
         "d'angle. En outre et qui plus est sont soutenus : parfaits à "
         "l'écrit."),
        ("Conclure",
         "par conséquent, ainsi, c'est pourquoi. Une seule fois : deux "
         "conclusions de suite annulent la première."),
    ], notes="Faire noter le couple « bien que » plus subjonctif et « même si » plus "
             "indicatif. Il revient en D2, et c'est la faute la plus fréquente du "
             "niveau.")

    d.regle("Concéder, c'est donner raison avant d'avancer",
            "Certes mon expérience a été acquise ailleurs, mais elle porte "
            "sur seize ans d'usine. Bien que la question soit interdite, je "
            "comprends l'inquiétude.",
            precision="Ce mouvement en deux temps dit à votre interlocuteur que vous "
                      "avez entendu son objection, que vous ne la niez pas, et que "
                      "vous avez quand même quelque chose à répondre. Nier "
                      "l'objection ferme la conversation ; la concéder l'ouvre.",
            notes="Diapositive à photographier. Shirin l'emploie deux fois au défi 3. "
                  "Le faire remarquer quand on y arrivera.")

    d.pratique('Pratique 1 de 2', "Le bon connecteur",
               "Un seul convient : le sens de la phrase le désigne.", [
        ("L'acquisition n'a supprimé aucun emploi ; ___, elle a tout réorganisé.", "en revanche"),
        ("___ mon expérience vient d'ailleurs, mais elle est vérifiable.", "Certes"),
        ("___ que la question soit interdite, je comprends l'inquiétude.", "Bien"),
        ("L'équipe reste à bâtir ; ___, le poste comporte du recrutement.", "par conséquent"),
        ("Le carnet a doublé ; ___, un troisième quart a été ouvert.", "par ailleurs"),
        ("Les arrêts planifiés sont exclus ; ___, ces dix points sont perdus.", "autrement dit"),
    ], corrige=True,
       notes="Le dernier n'est pas un connecteur d'argument : il reformule. Le dire "
             "après la correction, c'est la nuance à emporter.")

    d.regle("Le verbe décide du relatif",
            "Si le verbe se construit avec « de », ce sera « dont ». S'il se "
            "construit avec « à », ce sera auquel, à laquelle, auxquels ou "
            "auxquelles. On ne devine pas : on regarde le verbe.",
            precision="Parler de, avoir besoin de, s'occuper de donnent « dont ». "
                      "Participer à, penser à, s'attendre à donnent la famille de "
                      "« auquel ». Le test : refaites la phrase simple, et la "
                      "préposition apparaît.",
            notes="Diapositive à photographier. C'est un savoir de reprise de "
                  "l'information, pas de grammaire de la phrase : il sert d'abord à "
                  "lire les documents du bloc.")

    d.pratique('Pratique 2 de 2', "Dont, auquel, laquelle",
               "Regardez d'abord quelle préposition le verbe demande.", [
        ("C'est le poste ___ je vous ai parlé.", "dont - parler DE"),
        ("Une entreprise ___ le carnet a doublé embauche forcément.", "dont - le carnet DE"),
        ("L'équipe comptera seize personnes, ___ neuf restent à recruter.", "dont - la partie d'un tout"),
        ("Voici le processus ___ je participe.", "auquel - participer À"),
        ("Ce sont les conditions ___ je m'attendais.", "auxquelles - s'attendre À"),
        ("L'échelle ___ les salaires sont fixés compte six échelons.", "selon laquelle"),
    ], corrige=True,
       notes="Faire dire la phrase simple à voix haute avant de choisir : « je "
             "participe À ce processus ». La préposition entendue donne le relatif.")

    d.piege('Piège', "« l'entreprise dont son carnet a doublé »",
            "« l'entreprise dont le carnet a doublé »",
            "« Dont » contient déjà le « de ». Ajouter un possessif derrière "
            "fait doublon, et c'est la faute qu'un correcteur repère en "
            "premier à ce niveau. Même chose avec un second « de » : jamais "
            "« dont le carnet de l'entreprise ».",
            notes="Écrire les trois versions au tableau, la juste au milieu. La faute "
                  "vient d'une bonne intuition — on sent qu'il manque quelque chose — "
                  "et il faut le dire.")

    d.billet(
        "Écrivez trois phrases sur une entreprise qui vous intéresse.",
        exemples=[
            "Une avec une concession : certes..., mais...",
            "Une avec « dont », une avec « auquel » ou « à laquelle ».",
        ],
        notes="Devoir. Les phrases de concession se reprennent telles quelles au "
              "défi 3 : ce sont elles qui répondent à l'objection.")

    return d.save(dossier)
