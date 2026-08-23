# -*- coding: utf-8 -*-
"""B4 · Mettre en avant ce qui vous a fait rire
Bloc B « Défi 1 » · couleur ambre · écriture et grammaire · 75 min.
Source : exercice `t1emph` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Mettre en avant ce qui vous a fait rire",
        chapeau="Le français n'accentue pas un mot : il construit une phrase "
                "autour. C'est ce qui permet de dire ce qui compte le plus "
                "sans hausser le ton.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 1. La mise en relief servira à toutes les "
                  "productions du module : c'est la forme même du commentaire.")

    d.objectifs([
        "employer « c'est... qui » pour mettre le sujet en avant ;",
        "employer « c'est... que » pour tout le reste ;",
        "annoncer avec « ce qui... c'est » devant un auditoire ;",
        "accorder le verbe avec ce qu'on met en avant.",
    ], notes="Le quatrième objectif porte la faute la plus fréquente de la séance : "
             "« c'est moi qui a ». Elle s'entend, et elle se corrige en une leçon.")

    d.declencheur(
        'Préparation', "Comment dit-on qu'un mot compte plus que les autres ?",
        pistes=[
            "En parlant plus fort ? En ralentissant ?",
            "Est-ce que ça marche à l'écrit ?",
            "Dans votre langue première, y a-t-il un mot pour cela ?",
            "Avez-vous déjà répété une phrase parce qu'on avait mal compris ce que vous visiez ?",
        ],
        notes="La deuxième piste est la clé : à l'écrit, la voix ne sert plus. Le "
              "français a donc trois constructions, et c'est la séance.")

    d.tableau('Analyse', "Trois façons, trois emplois",
              ['La construction', 'Ce qu\'elle met en avant'],
              [["C'est... qui", "le sujet : c'est le ton qui fait rire"],
               ["C'est... que", "tout le reste : c'est à la fin qu'il exagère"],
               ["Ce qui... c'est", "une idée entière, annoncée avant d'être livrée"]],
              cle=0,
              note="Une seule par idée. Trois de suite, et plus rien n'est en avant.",
              notes="Diapositive à photographier. Le test pour choisir entre les deux "
                    "premières : si le mot fait quelque chose, c'est le sujet, donc "
                    "« qui ».")

    d.regle("Le verbe s'accorde avec ce qu'on met en avant",
            "« C'est moi qui ai ri », et non « c'est moi qui a ri ».",
            precision="Le pronom « qui » reprend « moi » : le verbe se met donc à la "
                      "première personne. C'est vrai pour toutes les personnes : "
                      "c'est nous qui avons choisi, c'est vous qui avez raison.",
            notes="Diapositive à photographier. Faire dire les six personnes à voix "
                  "haute d'affilée. C'est un automatisme, pas un raisonnement.")

    d.cartes('Analyse', "La même idée, trois formes", [
        ("Ordinaire", "Le ton fait rire."),
        ("Clivée", "C'est le ton qui fait rire."),
        ("Annoncée", "Ce qui fait rire, c'est le ton."),
        ("Ordinaire", "J'ai aimé la quatrième nuit."),
        ("Clivée", "C'est la quatrième nuit que j'ai aimée."),
        ("Annoncée", "Ce que j'ai aimé, c'est la quatrième nuit."),
    ], cols=2,
       notes="Faire dire les six à voix haute. La troisième de chaque série crée une "
             "seconde d'attente : c'est celle qui fonctionne devant un groupe.")

    d.piege('Grammaire',
            "« C'est le ton que fait rire. »",
            "« C'est le ton qui fait rire. »",
            "Le ton fait quelque chose : il est sujet du verbe, donc « qui ». "
            "Le test tient en une question : est-ce que le mot mis en avant "
            "agit ? Si oui, « qui ». Sinon, « que ».",
            notes="Erreur fréquente et facile à corriger avec le test. La faire "
                  "appliquer sur cinq phrases au tableau avant l'exercice écrit.")

    d.pratique('Grammaire', "Mettez le mot en avant",
               "Employez la construction demandée.", [
        ("Le ton fait rire. (c'est... qui)", "C'est le ton qui fait rire."),
        ("Il exagère à la fin. (c'est... que)", "C'est à la fin qu'il exagère."),
        ("J'ai ri la première. (c'est... qui)", "C'est moi qui ai ri la première."),
        ("Nous avons choisi le film. (c'est... qui)", "C'est nous qui avons choisi le film."),
        ("Le silence me dérange. (ce qui... c'est)", "Ce qui me dérange, c'est le silence."),
        ("Gaétan a le meilleur argument. (c'est... qui)", "C'est Gaétan qui a le meilleur argument."),
    ], corrige=True,
       notes="Exercice `t1emph` du module. Le troisième et le quatrième portent "
             "l'accord : les faire corriger à voix haute, pas au tableau.")

    d.pratique('Production écrite', "Votre commentaire du sketch",
               "Quatre phrases, dont une mise en relief.", [
        ("Phrase 1", "de quoi parle le sketch, en une phrase"),
        ("Phrase 2", "ce que vous en pensez, annoncé comme un avis"),
        ("Phrase 3", "le moment précis qui vous a fait rire, cité"),
        ("Phrase 4", "une mise en relief : ce qui m'a fait rire, c'est..."),
    ], corrige=False,
       notes="Vingt minutes. Ramasser : ces quatre phrases sont un premier "
             "commentaire complet, et l'on voit immédiatement qui a mis la mise en "
             "relief sur une banalité plutôt que sur le cœur de son avis.")

    d.billet(
        "Réécrivez une phrase de votre commentaire avec « ce qui... c'est ».",
        exemples=[
            "Ce qui m'a surpris, c'est...",
            "Ce que je retiens, c'est...",
        ],
        notes="Fin du bloc B. Le bloc C passe à la chanson, et la mise en relief y "
              "reviendra dans les exercices de reprise.")

    return d.save(dossier)
