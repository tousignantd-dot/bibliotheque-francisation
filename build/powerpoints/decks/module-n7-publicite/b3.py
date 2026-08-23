# -*- coding: utf-8 -*-
"""B3 · Plus chaleureux — mais que quoi ?
Bloc B « Défi 1 » · couleur teal · écoute et réponds · 75 min.
Source : exercice `t1comp`, mini-leçon `t1comp`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='teal',
        titre="Plus chaleureux — mais que quoi ?",
        chapeau="Le comparatif le plus courant de la publicité est incomplet. "
                "Il compare à rien, et laisse votre tête placer elle-même le "
                "point de comparaison.",
        duree='75 minutes')

    d.titre(notes="Séance d'écoute active. Prévoir de faire réécouter les deux "
                  "capsules du Défi 1 au moins deux fois : on cherche cette fois un "
                  "mot précis, pas le sens général.")

    d.objectifs([
        "former un comparatif complet, avec ses deux termes ;",
        "repérer un comparatif tronqué et poser la question qui manque ;",
        "distinguer une quantité chiffrée d'une comparaison vague ;",
        "employer « meilleur » et « mieux » sans se tromper.",
    ], notes="Le troisième objectif prévient le contresens de la séance : « plus de "
             "vingt appareils » est une quantité, pas un comparatif tronqué.")

    d.declencheur(
        'Écoute', "Une question à poser à voix haute",
        pistes=[
            "« Un environnement plus chaleureux. » Plus chaleureux que quoi ?",
            "« Des résultats plus rapides. » Plus rapides que quoi ?",
            "« Moins de frais. » Moins de frais que chez qui ?",
            "Que se passe-t-il dans votre tête quand personne ne répond ?",
        ],
        notes="La quatrième question est le cœur de la séance : la tête complète "
              "toute seule, avec ce qui l'arrange. Personne n'a menti, et pourtant "
              "quelque chose a été dit.")

    d.tableau('Analyse', "Les trois degrés du comparatif",
              ['Le degré', 'La forme'],
              [["Supériorité", "plus grand que celui de la rue Parent"],
               ["Infériorité", "moins élevé que l'an dernier"],
               ["Égalité", "aussi cher que son voisin"],
               ["Avec un nom", "plus de, moins de, autant de"]],
              cle=0,
              note="Le deuxième terme s'introduit toujours par « que ».",
              notes="Diapositive à photographier. La quatrième ligne est la seule "
                    "irrégularité : avec un nom, « autant de » remplace « aussi ».")

    d.regle("Un comparatif tronqué n'a qu'un terme",
            "« Un environnement plus chaleureux. » Plus chaleureux que quoi ? "
            "Rien n'est dit, donc rien n'est vérifiable.",
            precision="Un superlatif, lui, engage vraiment : « le plus grand centre "
                      "de la Rivière-du-Nord » se compare à tout le reste, donc se "
                      "vérifie. C'est pour cela que les agences préfèrent le "
                      "comparatif vague au superlatif précis.",
            notes="Diapositive à photographier. La dernière phrase est celle qui "
                  "éclaire : ce n'est pas de la paresse d'écriture, c'est un choix.")

    d.cartes('Analyse', "Deux formes irrégulières, aucune exception", [
        ("bon devient meilleur", "un meilleur prix — jamais « plus bon »"),
        ("bien devient mieux", "on y dort mieux — jamais « plus bien »"),
        ("le superlatif de bon", "le meilleur prix en ville"),
        ("le superlatif de bien", "c'est là qu'on dort le mieux"),
    ], cols=1,
       notes="« Meilleur » accompagne un nom, « mieux » accompagne un verbe. Le test : "
             "si on peut mettre « très » devant, c'est « mieux ».")

    d.pratique('Pratique', "Complétez la comparaison",
               "Ajoutez le deuxième terme, et voyez ce que l'annonce évitait de dire.", [
        ("Un environnement plus chaleureux ___ (celui de l'an dernier).", "que celui de l'an dernier"),
        ("Des résultats plus rapides ___ (une marche quotidienne).", "qu'une marche quotidienne"),
        ("Vous dormirez mieux ___ (sur votre vieux matelas).", "que sur votre vieux matelas"),
        ("Moins de frais ___ (chez nos concurrents).", "que chez nos concurrents"),
        ("Un plus bon prix.", "un meilleur prix"),
        ("On y dort plus bien.", "on y dort mieux"),
        ("Ce centre est grand : c'est ___ centre de la région.", "le plus grand"),
    ], corrige=True,
       notes="Exercice `t1comp` du module. Après correction, faire relire la colonne "
             "de gauche : les annonces réelles s'arrêtent toutes avant le « que ».")

    d.piege('Écoute',
            "confondre « plus de vingt » et « plus chaleureux »",
            "un chiffre n'est pas une impression",
            "« Plus de vingt appareils neufs » est une quantité vérifiable : "
            "on peut aller les compter. « Plus chaleureux » ne se vérifie "
            "pas. Le même mot « plus », deux natures très différentes — et "
            "seule la première engage l'annonceur.",
            notes="Piège fréquent une fois la séance comprise : les élèves se mettent "
                  "à voir des comparatifs tronqués partout. Le chiffre les arrête.")

    d.billet(
        "Trouvez un comparatif tronqué dans une annonce, et écrivez la question qui manque.",
        exemples=[
            "« Plus rapide » : plus rapide que quoi ?",
            "Notez aussi ce que votre tête avait complété toute seule.",
        ],
        notes="Devoir d'observation. La deuxième consigne est la plus instructive : "
              "les élèves découvrent qu'ils avaient déjà répondu sans s'en rendre "
              "compte.")

    return d.save(dossier)
