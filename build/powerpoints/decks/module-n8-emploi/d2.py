# -*- coding: utf-8 -*-
"""D2 · Auquel, dont, et si j'avais su.
Bloc D « Défi 3 » · couleur ambre · 60 min. Fin du Défi 3.
Source : exercices `t3rel`, `t3hyp`, `t3reprise` et `t3quest`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Auquel, dont, et si j'avais su",
        chapeau="Trois points de langue au service d'une seule chose : "
                "écrire une demande qui se tienne. Le pronom qui relie, "
                "l'hypothèse qui chiffre, la reprise qui évite la répétition.",
        duree='60 minutes')

    d.titre(notes="Séance dense : trois points en soixante minutes. Aller vite sur le "
                  "premier, qui est connu, et garder le temps pour l'hypothèse et la "
                  "reprise, qui sont neufs.")

    d.objectifs([
        "choisir le pronom relatif que commande la préposition du verbe ;",
        "construire une hypothèse sur le passé, sans conditionnel après « si » ;",
        "reprendre une information par un nom générique ou une nominalisation ;",
        "poser trois questions utiles à une conseillère en formation.",
    ], notes="L'objectif 2 est celui qui sert directement à convaincre : il chiffre ce "
             "qu'une lacune a coûté.")

    d.regle("Le pronom porte la préposition",
            "Le verbe commande une préposition ; le pronom la porte.",
            precision="On s'adresse à un service : le service auquel je m'adresse. On "
                      "parle de quelque chose : la démarche dont je parle. On écrit sur "
                      "un formulaire : le formulaire sur lequel elle a écrit. Trouvez la "
                      "préposition du verbe, et le pronom se choisit tout seul.",
            notes="Diapositive à photographier. C'est la seule question à se poser : "
                  "« ce verbe demande quelle préposition ? »")

    d.tableau('Analyse', "Les formes, selon la préposition",
              ['La préposition', 'Le pronom'],
              [["à", "auquel · à laquelle · auxquels · auxquelles"],
               ["de", "dont — presque toujours ; duquel dans une locution"],
               ["sur, pour, avec, sans", "sur lequel · pour laquelle · avec lesquels"],
               ["aucun nom devant", "ce dont · ce à quoi"]],
              cle=1,
              note="« Dont » contient déjà le « de » : « dont j'en ai besoin » le répète.",
              notes="Diapositive à photographier. Faire produire une phrase par ligne, "
                    "sur la démarche de formation de chacun.")

    d.regle("L'hypothèse sur le passé",
            "Si j'avais su utiliser le module, j'aurais économisé quarante heures.",
            precision="« Si » plus plus-que-parfait, puis conditionnel passé. C'est la "
                      "phrase qui transforme un souhait en argument : elle chiffre ce "
                      "qu'une lacune a coûté. Et la règle absolue : après « si » de "
                      "condition, jamais de -rais ni de -rait. Les si n'aiment pas les "
                      "rais.",
            notes="Diapositive à photographier. C'est la phrase à placer dans la demande "
                  "écrite de E2.")

    d.cartes("Les trois hypothèses", "Une seule chose change : la distance au réel", [
        ("C'est probable",
         "si + présent, puis futur : si vous m'écrivez cette semaine, je répondrai avant vendredi."),
        ("C'est imaginé",
         "si + imparfait, puis conditionnel présent : si le cours était offert le jour, je m'inscrirais."),
        ("C'est trop tard",
         "si + plus-que-parfait, puis conditionnel passé : si j'avais su, j'aurais économisé quarante heures."),
    ], cols=1,
       notes="Les apprendre ensemble : c'est en les comparant qu'on cesse de les "
             "mélanger.")

    d.piege("Le conditionnel après si",
            "Si j'aurais su, j'aurais demandé plus tôt.",
            "Si j'avais su, j'aurais demandé plus tôt.",
            "La faute la plus repérée du français, y compris chez les locuteurs natifs. "
            "Elle n'a aucune exception : après le « si » de condition, ni -rais ni "
            "-rait. Attention toutefois : le « si » d'une question rapportée est un "
            "autre mot, et lui accepte le conditionnel — je me demande s'il accepterait.",
            notes="Écrire les deux « si » au tableau, côte à côte. La distinction est "
                  "difficile et vaut les cinq minutes.")

    d.tableau('Reprise', "Ne pas répéter le même mot",
              ['La répétition', 'La reprise'],
              [["Lachance livre en dix jours. Dix jours nous mettent en défaut.",
                "Ce délai nous met en défaut."],
               ["Le fournisseur a augmenté ses prix. L'augmentation…",
                "Cette hausse…"],
               ["Nous avons reporté la décision. La décision est notée.",
                "Ce report est noté au compte rendu."]],
              cle=1,
              note="On transforme le verbe en nom, précédé d'un démonstratif : c'est la reprise reine du compte rendu.",
              notes="Attention à l'ambiguïté : « celui-ci » et « ce dernier » reprennent "
                    "toujours le dernier élément nommé. Dans le doute, répéter le nom.")

    d.pratique('Grammaire', "Le pronom et le temps justes",
               "Complétez.", [
        ("Le service ___ je dois m'adresser est celui de la reconnaissance des acquis.", "auquel"),
        ("___ vous me parlez est un besoin très précis.", "Ce dont"),
        ("La formation ___ elle pense se donne le soir.", "à laquelle"),
        ("C'est une démarche ___ je ne connaissais pas les étapes.", "dont"),
        ("Si j'___ (savoir) utiliser le module, j'aurais économisé quarante heures.", "avais su"),
        ("Si nous avions eu cette formation, nous ___ (ne pas reprendre) douze factures.", "n'aurions pas repris"),
        ("Si le cours était offert le jour, je m'___ (inscrire) tout de suite.", "inscrirais"),
        ("Si vous m'écrivez cette semaine, je ___ (répondre) avant vendredi.", "répondrai"),
    ], corrige=True,
       notes="Les quatre derniers items balaient les trois hypothèses. Faire nommer "
             "laquelle avant de répondre.")

    d.pratique('Production', "Trois questions à poser",
               "Écrivez trois questions à une conseillère en formation. Vouvoiement, forme soutenue.", [
        ("Sur la durée et l'horaire.", "Combien de temps dure la formation, et à quelles heures ?"),
        ("Sur le coût et sur qui l'assume.", "Quels sont les frais, et l'employeur peut-il en assumer une partie ?"),
        ("Sur ce que la formation donne à la fin.", "Est-ce que cette formation mène à une attestation ?"),
    ], corrige=True,
       notes="Rappeler qu'une question fermée obtient « oui ». « Quels cours sont "
             "offerts le soir cet automne ? » obtient une liste.")

    d.billet(
        "Écrivez une phrase en « si j'avais… j'aurais… » sur votre propre travail.",
        exemples=[
            "Elle doit contenir un chiffre.",
            "Vérifiez : aucun -rais après « si ».",
        ],
        notes="Cette phrase entre telle quelle dans la demande écrite de E2.")

    return d.save(dossier)
