# -*- coding: utf-8 -*-
"""C2 · Écrivez, signez, gardez.
Bloc C « Défi 2 · Je remplis le formulaire » · couleur ambre · 75 min.
Source : dialogue `t2b`, exercices `t2imper`, `t2poss`, `t2b`,
mini-leçons `t2imper`, `t2poss`.

La grammaire du défi 2, en deux points que le programme du niveau 2 inscrit
tous les deux : les phrases impératives, et les déterminants possessifs. Le
comptoir postal les met côte à côte dans la même minute — « Écrivez votre
nom » — et c'est pourquoi ils s'enseignent ensemble ici.

La séance se termine sur l'avis de livraison, le carton que tout le monde a
déjà trouvé dans sa boîte aux lettres sans savoir le lire.
"""
import os

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-colis/images/')


def _photo(nom):
    """La photo si elle est sur le disque, sinon rien. Voir `a1.py`."""
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Écrivez, signez, gardez",
        chapeau="Comprendre les consignes du comptoir, dire « mon » et "
                "« votre » au bon moment, et lire un avis de livraison.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, mais tirée de phrases entendues au comptoir. Ne "
                  "jamais donner la règle avant la phrase : on part de ce que Luc dit, on "
                  "remonte à la forme.")

    d.objectifs([
        "comprendre une consigne à l'impératif ;",
        "employer mon, ma, mes, votre et vos ;",
        "reconnaître un avis de livraison ;",
        "savoir ce qu'on apporte pour reprendre un colis.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce que ce carton ?",
        image=_photo('poste-avis.jpg'),
        pistes=[
            "Avez-vous déjà trouvé un papier comme celui-là chez vous ?",
            "Qu'avez-vous fait avec ?",
            "Qu'est-ce qu'il annonce, à votre avis ?",
            "Combien de temps peut-on attendre avant d'y aller ?",
        ],
        notes="Presque tout le groupe l'a déjà reçu, et plusieurs l'ont jeté. Le dire sans "
              "reproche : c'est justement pour cela que la séance existe.")

    d.tableau('Analyse', "Le verbe qui donne une consigne",
              ['Ce que dit Luc', 'Ce que ça veut dire'],
              [["Écrivez votre nom.", "vous devez écrire votre nom"],
               ["Signez ici.", "vous devez signer ici"],
               ["Remplissez le formulaire.", "vous devez remplir le formulaire"],
               ["Gardez votre reçu.", "vous devez garder votre reçu"]],
              cle=2,
              note="Le verbe finit par -ez, et il n'y a pas de « vous » devant. C'est la "
                   "forme la plus courte du français.",
              notes="Diapositive à photographier. Faire remarquer qu'on n'entend jamais "
                    "« vous écrivez votre nom » pour donner une consigne : le « vous » "
                    "disparaît, et c'est ce qui rend la phrase brève.")

    d.cartes("Les six verbes de la poste", "Toujours à la même forme", [
        ("écrivez", "Écrivez votre nom dans la case."),
        ("remplissez", "Remplissez ce formulaire, s'il vous plaît."),
        ("signez", "Signez en bas, à droite."),
        ("posez", "Posez la boîte sur la balance."),
        ("gardez", "Gardez votre reçu."),
        ("apportez", "Apportez le carton et une carte avec votre photo."),
    ], cols=3, notes="Diapositive à photographier. Faire dire les six à voix haute, en "
                     "chœur. Un ami dirait « écris », « signe » — sans -ez, et sans s à "
                     "« écris ». Le mentionner sans l'exercer : au comptoir, c'est « vous ».")

    d.regle("Mon nom, votre nom",
            "Quand je parle de moi : mon, ma, mes. Quand on me parle : votre, vos.",
            precision="<b>mon</b> devant un mot masculin, <b>ma</b> devant un mot féminin, "
                      "<b>mes</b> quand il y en a plusieurs. On dit <b>mon</b> adresse et "
                      "non « ma adresse » : le mot commence par une voyelle. Pour "
                      "« votre » et « vos », le masculin et le féminin ne changent rien — "
                      "seul le nombre compte.",
            notes="Diapositive à photographier. « Mon adresse » est la seule exception à "
                  "retenir de la séance, et c'est un mot du module : elle vaut la peine.")

    d.dialogue('Dialogue', "Un carton dans la boîte aux lettres", [
        ("AMARA", "Karim, regarde. C'est quoi, ce carton ?", True),
        ("KARIM", "C'est un avis de livraison.", True),
        ("AMARA", "Alors il est où, mon colis ?", True),
        ("KARIM", "Au comptoir postal. Tu vas le chercher.", True),
        ("AMARA", "J'apporte quoi ?", True),
        ("KARIM", "Le carton et une carte avec ta photo.", True),
        ("AMARA", "Et je signe ?", True),
        ("KARIM", "Oui. Tu signes, et tu prends ton colis.", True),
    ], consigne="Écoutez, puis dites ce qu'Amara doit apporter.",
       notes="Faire écouter deux fois. Trois choses à retenir : où est le colis, quoi "
             "apporter, et qu'on signe. Les faire nommer par trois élèves différents.")

    d.pratique('Écriture', "Écrivez, signez, remplissez",
               "Complétez chaque consigne avec le bon verbe.", [
        ("___ la boîte sur la balance.", "Posez"),
        ("___ ce formulaire, s'il vous plaît.", "Remplissez"),
        ("___ votre nom dans la case.", "Écrivez"),
        ("___ en bas, à droite.", "Signez"),
        ("___ votre reçu à la maison.", "Gardez"),
        ("___ le carton et une carte avec votre photo.", "Apportez"),
    ], corrige=True, cols=2,
       notes="Les six mêmes phrases sont dans le module en ligne, exercice `t2imper`.")

    d.pratique('Écriture', "Mon nom, votre nom",
               "Complétez avec mon, ma, mes, votre ou vos.", [
        ("Voici ___ nom : Diallo.", "mon"),
        ("J'habite dans ___ rue Bélanger.", "ma"),
        ("Écrivez ___ adresse ici.", "votre"),
        ("Apportez ___ papiers au comptoir.", "vos"),
        ("Je cherche ___ colis.", "mon"),
        ("Gardez ___ reçu.", "votre"),
    ], corrige=True, cols=2,
       notes="Les six mêmes phrases sont dans le module en ligne, exercice `t2poss`. "
             "Faire justifier chaque réponse à voix haute : qui parle, et de quoi ?")

    d.pratique('Pratique · à deux', "Je viens chercher mon colis",
               "Deux par deux. L'un tient le comptoir, l'autre arrive avec le carton.", [
        ("Étape 1", "Dites pourquoi vous venez : « Je viens chercher mon colis. »"),
        ("Étape 2", "Le préposé demande le carton et une carte avec photo."),
        ("Étape 3", "Le préposé donne une consigne à l'impératif : « Signez ici. »"),
        ("Étape 4", "Demandez jusqu'à quand un colis est gardé, puis changez de rôle."),
    ], cols=1,
       notes="Vingt minutes. La réponse à l'étape 4 est quinze jours ; après, le colis "
             "repart chez l'expéditeur. C'est le renseignement le plus utile de la séance.")

    d.billet(
        "Écrivez trois consignes que le préposé pourrait vous dire.",
        exemples=[
            "Remplissez ce formulaire.",
            "Signez en bas, à droite.",
            "Gardez votre reçu.",
        ],
        notes="Devoir court. Demander de les lire à voix haute : les six verbes doivent "
              "être reconnus à l'oreille pour la séance E1.")

    return d.save(dossier)
