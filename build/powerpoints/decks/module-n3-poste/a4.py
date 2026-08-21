# -*- coding: utf-8 -*-
"""A4 · Je voudrais, j'aimerais, est-ce que je pourrais.
Bloc A « Je découvre » · couleur ambre (écriture) · 75 min.
Source : mini-leçon `prPoli`, exercice `prPoli`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Je voudrais, j'aimerais, est-ce que je pourrais",
        chapeau="Au comptoir, « je veux » sonne dur. Trois formules polies "
                "suffisent pour tout demander, et une quatrième pour faire "
                "répéter la personne devant soi.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire et d'écriture. C'est la séance qui rend possible "
                  "tout le défi 1 : sans ces formules, l'élève ouvre la bouche et "
                  "s'arrête.")

    d.objectifs([
        "employer « je voudrais » pour dire ce qu'on vient faire ;",
        "employer « j'aimerais » pour un achat ;",
        "employer « est-ce que je pourrais » pour une permission ;",
        "employer « est-ce que vous pouvez » pour demander un service.",
    ])

    d.regle("La phrase qui ouvre tout",
            "Je voudrais envoyer ce colis, s'il vous plaît.",
            precision="Jamais « je veux ». « Je veux » n'est pas incorrect, mais "
                      "au comptoir il sonne dur, comme un ordre. « Je voudrais » "
                      "dit exactement la même chose et ouvre la conversation.",
            notes="Diapo à photographier. Faire répéter la phrase par tout le groupe, "
                  "puis par chaque élève en changeant le mot « colis » : une lettre, un "
                  "mandat, une boîte.")

    d.tableau('Analyse', "Quatre formules, quatre emplois",
              ['La formule', 'Quand', 'Exemple'],
              [["Je voudrais", "dire ce qu'on vient faire", "Je voudrais envoyer ce colis."],
               ["J'aimerais", "surtout pour un achat", "J'aimerais des timbres, s'il vous plaît."],
               ["Est-ce que je pourrais", "demander une permission", "Est-ce que je pourrais payer par carte ?"],
               ["Est-ce que vous pouvez", "demander un service à l'autre", "Est-ce que vous pouvez répéter ?"]],
              cle=0,
              note="Les deux premières parlent de soi. Les deux dernières demandent quelque chose à l'autre.",
              notes="Diapo à photographier. C'est la diapositive la plus utile du bloc A : "
                    "elle tient dans une photo de téléphone et elle sert au comptoir.")

    d.cartes("Les trois mots de la politesse", "Ils ne coûtent rien", [
        ("bonjour",
         "Au début, toujours. On ne commence pas une demande sans saluer : ici, "
         "c'est presque une obligation, même entre inconnus."),
        ("s'il vous plaît",
         "À la fin de la demande. Sans lui, la phrase devient un ordre, même avec "
         "un verbe poli devant."),
        ("merci",
         "Avant de partir, et aussi au milieu quand on reçoit une réponse. On peut "
         "le dire deux ou trois fois dans le même échange."),
        ("vous, jamais tu",
         "Au comptoir, on vouvoie toujours, même une personne plus jeune. C'est la "
         "règle des lieux de service au Québec."),
    ], notes="Faire jouer le contraste : dire la même demande sans les trois mots, puis "
             "avec. Les élèves entendent la différence immédiatement.")

    d.regle("Pour faire répéter",
            "Est-ce que vous pouvez répéter, s'il vous plaît ?",
            precision="Cette phrase-là sert tous les jours, partout, et elle ne "
                      "gêne personne. On peut ajouter : « un peu moins vite, "
                      "s'il vous plaît ». Ne pas comprendre n'est pas une faute.",
            notes="Diapo à photographier. Faire répéter la phrase jusqu'à ce qu'elle "
                  "sorte sans hésitation : c'est celle qui sauve les élèves quand tout "
                  "le reste échoue.")

    d.pratique('Écriture', "Complétez la demande",
               "Écrivez « voudrais », « aimerais », « pourrais » ou « pouvez ».", [
        ("Je ___ envoyer ce colis, s'il vous plaît.", "voudrais"),
        ("J' ___ un carnet de timbres.", "aimerais"),
        ("Est-ce que je ___ payer par carte de débit ?", "pourrais"),
        ("Est-ce que vous ___ répéter le prix, s'il vous plaît ?", "pouvez"),
        ("Je ___ savoir combien de temps ça prend.", "voudrais — « j'aimerais » se dit aussi"),
        ("Est-ce que vous ___ parler un peu moins vite ?", "pouvez"),
    ], corrige=True,
       notes="C'est l'exercice `prPoli` du module interactif. Le faire d'abord à l'écrit "
             "sur la fiche, puis le refaire à l'écran : la correction automatique accepte "
             "les deux réponses de l'avant-dernière ligne.")

    d.piege(
        "Au comptoir",
        "Je veux envoyer ce colis.",
        "Je voudrais envoyer ce colis, s'il vous plaît.",
        "La première phrase est comprise, mais elle ferme le visage de la personne "
        "en face. Un seul mot change, et tout le reste de l'échange devient plus "
        "facile — y compris le droit de faire répéter trois fois.",
        notes="Demander qui a déjà employé « je veux » sans y penser. Beaucoup l'ont "
              "fait : c'est la traduction directe de leur langue. Dédramatiser.")

    d.pratique('À l\'oral', "Dites-le à votre voisin",
               "Deux par deux : l'un est le client, l'autre la préposée.", [
        ("Vous voulez envoyer une boîte à Montréal.", "Bonjour. Je voudrais envoyer ce colis à Montréal, s'il vous plaît."),
        ("Vous voulez acheter un carnet de timbres.", "J'aimerais un carnet de timbres, s'il vous plaît."),
        ("Vous voulez payer avec votre carte.", "Est-ce que je pourrais payer par carte de débit ?"),
        ("Vous n'avez pas compris le prix.", "Est-ce que vous pouvez répéter, s'il vous plaît ?"),
    ], corrige=True,
       notes="Cinq minutes par rôle, puis on échange. Passer entre les rangées et "
             "corriger seulement la formule, pas la prononciation : ce n'est pas la "
             "séance pour ça.")

    d.billet(
        "Écrivez une demande polie que vous devrez faire cette semaine, ailleurs qu'à la poste.",
        exemples=[
            "À la pharmacie, à l'école de vos enfants, chez le propriétaire ?",
            "Laquelle des quatre formules convient le mieux ?",
        ],
        notes="Devoir court. Il montre que ces quatre formules ne servent pas seulement "
              "au bureau de poste, ce qui est l'intention du programme au niveau 3.")

    return d.save(dossier)
