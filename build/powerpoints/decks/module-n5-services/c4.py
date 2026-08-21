# -*- coding: utf-8 -*-
"""C4 · Le formulaire qui se bloque.
Bloc C « Défi 2 · L'écran » · couleur ambre · 75 min.
Source : exercices `t2form` et `t2prep`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-services/images/')


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="Le formulaire qui se bloque",
        chapeau="Un formulaire n'est pas un texte : c'est une machine. Il "
                "refuse d'avancer sans presque jamais dire pourquoi. Trois "
                "soirées perdues viennent presque toujours d'un champ mal "
                "compris, pas d'une panne.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 2. Ramasser le devoir C3. Si un élève a une "
                  "démarche en ligne en cours, proposer de la regarder ensemble au "
                  "projecteur : rien n'enseigne mieux cette séance qu'un vrai formulaire.")

    d.objectifs([
        "reconnaître les sept mots des formulaires officiels ;",
        "savoir ce qu'on met dans « nom à la naissance » ;",
        "trouver pourquoi une page se bloque ;",
        "employer les prépositions des démarches.",
    ])

    d.declencheur(
        'Expérience', "La page refuse d'avancer et ne dit pas pourquoi. Que faites-vous ?",
        image=IMG + 'formulaire-ecran.jpg',
        pistes=[
            "Vous recommencez depuis le début ?",
            "Vous changez de navigateur ?",
            "Vous abandonnez et vous vous déplacez ?",
            "Où regardez-vous en premier ?",
        ],
        notes="Presque tout le monde recommence depuis le début, ce qui ne change rien. "
              "Laisser dire, puis donner la méthode : on remonte vérifier les astérisques.")

    d.regle("Un champ obligatoire vide bloque tout, en silence",
            "L'astérisque * marque les champs sans lesquels rien n'avance.",
            precision="Le système ne dit pas toujours lequel manque. Quand une page se "
                      "bloque : remonter et vérifier chaque astérisque, un par un. C'est "
                      "fastidieux, et c'est presque toujours ça.",
            notes="Diapositive à photographier. Ajouter : lire tous les champs AVANT d'en "
                  "remplir un seul. Cinq minutes de lecture épargnent trois soirées.")

    d.tableau('Les mots du formulaire · 1 de 2', "Ce qu'on vous demande",
              ['Le mot', 'Ce qu\'il demande vraiment'],
              [["Nom à la naissance", "celui de votre acte de naissance"],
               ["Champ obligatoire *", "sans lui, le formulaire refuse d'avancer"],
               ["Pièce justificative", "le document qui prouve ce que vous déclarez"],
               ["Téléverser", "envoyer un fichier vers le site"]],
              cle=0,
              note="Au Québec, le nom ne change pas au mariage : ce champ arrête bien du monde.",
              notes="Diapositive à photographier. Le premier mot est celui qui bloque le "
                    "plus de gens, et pour rien.")

    d.tableau('Les mots du formulaire · 2 de 2', "Ce qui vous engage, et votre preuve",
              ['Le mot', 'Ce qu\'il demande vraiment'],
              [["Le cas échéant", "si cela s'applique à vous — sinon, laissez vide"],
               ["Attestation", "la case du bas : vous déclarez que tout est exact"],
               ["Numéro de confirmation", "votre preuve d'envoi — à noter avant de fermer"]],
              cle=0,
              note="L'attestation est la seule ligne du formulaire qui vous engage. On relit avant.",
              notes="Diapositive à photographier. C'est le tableau le plus directement "
                    "réutilisable du module entier.")

    d.cartes("L'adresse, et pourquoi elle bloque", "Le détail de trois lettres", [
        ("L'ordre imposé",
         "Numéro, rue, appartement, ville, code postal. Toujours dans cet ordre."),
        ("L'abréviation",
         "« app. 3 », et non « appartement 3 ». Le système compare à sa propre base."),
        ("Ce n'est pas votre faute",
         "C'est une faiblesse du formulaire. Mais c'est à vous de la contourner."),
        ("Le symptôme",
         "La page redemande l'adresse à la dernière étape, sans expliquer pourquoi."),
    ], notes="C'est exactement ce qui arrive à Leïla au défi 3. Annoncer la suite : la "
             "séance D1 raconte ce qui se passe quand elle finit par se déplacer.")

    d.pratique('Formulaire', "Que faut-il inscrire ?",
               "Complétez.", [
        ("Le nom inscrit sur votre acte de naissance", "nom à la naissance"),
        ("Un champ marqué d'un astérisque", "un champ obligatoire"),
        ("« appartement 3 » doit s'écrire", "app. 3"),
        ("Le document qui prouve ce que vous déclarez", "une pièce justificative"),
        ("Envoyer un fichier vers le site", "téléverser"),
        ("« Si cela s'applique à votre situation »", "le cas échéant"),
        ("La case par laquelle vous déclarez que tout est exact", "l'attestation"),
        ("Ce qu'il faut noter après l'envoi", "le numéro de confirmation"),
    ], corrige=True,
       notes="Après la correction, demander qui a déjà laissé vide un champ « le cas "
             "échéant » sans oser. Plusieurs mains se lèvent, et c'est instructif.")

    d.regle("Les prépositions s'apprennent avec le verbe",
            "s'adresser à · se renseigner sur · avoir besoin de · avoir droit à.",
            precision="Aucune logique ne dit pourquoi on se renseigne SUR un tarif mais "
                      "qu'on s'adresse À un service. Un élève qui apprend « s'adresser » "
                      "sans son « à » l'apprendra deux fois. Notez-les toujours en groupe.",
            notes="Diapositive à photographier. Faire recopier les quatre groupes dans le "
                  "cahier de vocabulaire, pas dans le cahier de grammaire.")

    d.pratique('Prépositions', "Complétez",
               "à, au, de, dans, par, pour, avant de, sur.", [
        ("Il faut s'adresser ___ service des collectes.", "au"),
        ("Je me suis renseignée ___ les tarifs en vigueur.", "sur"),
        ("Vous pouvez faire votre demande ___ téléphone.", "par"),
        ("Vérifiez le temps d'attente ___ vous déplacer.", "avant de"),
        ("Vous recevrez une réponse ___ trois jours ouvrables.", "dans"),
        ("J'ai besoin ___ une preuve de résidence.", "d'"),
        ("Elle s'est présentée ___ guichet avec ses pièces.", "au"),
        ("Les résidents ont droit ___ quatre visites gratuites.", "à"),
    ], corrige=True,
       notes="Faire remarquer « par téléphone », sans article — sauf « par la poste », "
             "seule exception des quatre canaux.")

    d.piege("Demander POUR quelque chose",
            "Je demande pour un renseignement.",
            "Je demande un renseignement au préposé.",
            "On demande quelque chose à quelqu'un, sans « pour ». C'est l'erreur la plus "
            "fréquente de tout ce module, et elle s'entend au premier mot de l'appel.",
            notes="Écrire la forme fautive au tableau et la barrer devant le groupe. "
                  "Y revenir à chaque séance suivante : elle demande plusieurs passages.")

    d.billet(
        "Ouvrez un formulaire officiel en ligne, sans le remplir.",
        exemples=[
            "Comptez les champs obligatoires et relevez deux mots que vous ne connaissiez pas.",
            "N'envoyez rien. On regarde, c'est tout.",
        ],
        notes="La deuxième consigne est importante : plusieurs élèves ont de vraies "
              "démarches en cours et il ne s'agit pas de les leur faire rater en devoir.")

    return d.save(dossier)
