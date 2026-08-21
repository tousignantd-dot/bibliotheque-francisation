# -*- coding: utf-8 -*-
"""A3 · Les seize mots du bureau de poste.
Bloc A « Je découvre » · couleur teal · 75 min.
Source : banc `FC_CARDS`, exercices `prVocab` et `prImg`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-poste/images/')


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre='Les seize mots du bureau de poste',
        chapeau="Quatre familles de mots : l'endroit, l'envoi, l'adresse et "
                "les services. Seize mots qui suffisent à tenir toute une "
                "démarche au comptoir.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Prévoir les postes ou les tablettes : la "
                  "deuxième moitié de la séance se fait dans le module interactif, "
                  "avec les photos.")

    d.objectifs([
        "nommer les seize mots du module avec leur article ;",
        "associer chaque mot à sa définition ;",
        "reconnaître sept objets du bureau de poste en photo ;",
        "employer six de ces mots dans une phrase.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce que c'est, et à quoi ça sert ?",
        image=IMG + 'cases-postales.jpg',
        pistes=[
            "Où voit-on ce mur de petites portes ?",
            "Qu'est-ce qu'il y a derrière chacune d'elles ?",
            "Qui a la clé ?",
            "Est-ce que vous avez déjà eu une case comme celle-là ?",
        ],
        notes="Les cases postales existent surtout dans les villages et les petits "
              "immeubles. Beaucoup d'élèves en ont une sans savoir comment ça s'appelle.")

    d.vocabulaire('Famille 1', "L'endroit et l'envoi", [
        ("un bureau de poste", "Le magasin du gouvernement où on envoie et où on ramasse le courrier."),
        ("un préposé", "La personne qui travaille derrière le comptoir et qui te sert."),
        ("un timbre", "Le petit papier collant qu'on colle sur une lettre pour payer l'envoi."),
        ("affranchir", "Payer l'envoi d'une lettre ou d'un colis, avec un timbre ou au comptoir."),
        ("un envoi", "Tout ce qu'on confie à la poste : une lettre, un colis, un mandat."),
        ("un colis", "Une boîte qu'on envoie par la poste, plus grosse qu'une lettre."),
    ], notes="Faire répéter chaque mot avec son article. « Affranchir » est le seul "
             "verbe de la liste : le faire employer dans une phrase tout de suite.")

    d.vocabulaire('Famille 2', "L'adresse et le suivi", [
        ("l'expéditeur", "La personne qui envoie. Son adresse va en haut à gauche."),
        ("le destinataire", "La personne qui reçoit. Son adresse va au milieu de la boîte."),
        ("le code postal", "Les six caractères qui disent exactement où livrer, comme G1L 2M4."),
        ("le repérage", "Le numéro qui permet de suivre son colis sur Internet."),
        ("une balance", "L'appareil du comptoir qui dit combien pèse le colis."),
        ("un reçu", "Le petit papier qu'on te remet après avoir payé."),
    ], notes="Expéditeur et destinataire se confondent tout le temps. Donner le truc : "
             "l'expéditeur expédie, le destinataire est la destination.")

    d.vocabulaire('Famille 3', "Ce qu'on demande au comptoir", [
        ("fragile", "Qui casse facilement : du verre, une assiette, un cadre."),
        ("un avis de livraison", "Le carton laissé dans ta boîte aux lettres quand un colis t'attend."),
        ("le courrier recommandé", "Un envoi que la personne doit signer quand elle le reçoit."),
        ("un mandat-poste", "Un papier acheté à la poste qui vaut de l'argent, plus sûr que du comptant."),
    ], notes="Ces quatre mots sont ceux des défis 2 et 3. Les poser aujourd'hui sans les "
             "développer : ils reviendront avec leur situation.")

    d.tableau('Analyse', "Deux mots qui se ressemblent et qu'il ne faut pas confondre",
              ['Le mot', 'Qui est-ce ?', 'Où va son adresse ?'],
              [["l'expéditeur", "celui qui envoie la boîte", "en haut à gauche, en petit"],
               ["le destinataire", "celui qui reçoit la boîte", "au milieu, en plus gros"]],
              cle=0,
              note="Si la boîte ne se rend pas, elle retourne à l'expéditeur.",
              notes="Diapo à photographier. Faire écrire les deux mots au tableau par un "
                    "élève, puis faire placer les deux adresses sur une vraie boîte de "
                    "carton si vous en avez une.")

    d.pratique('Vocabulaire', "Quel mot manque ?",
               "Complétez avec un mot de la liste.", [
        ("La personne qui envoie le colis est l' ___ .", "expéditeur"),
        ("La personne qui reçoit le colis est le ___ .", "destinataire"),
        ("Les six caractères comme G1J 3K7 forment le code ___ .", "postal"),
        ("Le carton laissé dans la boîte aux lettres est un ___ de livraison.", "avis"),
        ("Le numéro qui permet de suivre le colis est le ___ .", "repérage"),
        ("Coller un timbre ou payer au comptoir, c'est ___ son envoi.", "affranchir"),
    ], corrige=True,
       notes="C'est l'exercice `aComp` du module, celui de la dernière section. Le faire "
             "ici en découverte, sans pénaliser : les élèves le retrouveront en E1.")

    d.declencheur(
        'Dans le module interactif', "Sept photos, sept phrases",
        image=IMG + 'ruban-boite.jpg',
        pistes=[
            "Le comptoir où on parle à la préposée.",
            "La boîte rouge de la rue, pour les lettres déjà timbrées.",
            "Une boîte posée sur la balance du comptoir.",
            "Un carnet de timbres, moins cher qu'à l'unité.",
        ],
        notes="Annoncer l'exercice `prImg` : sept photos à faire glisser vers la phrase "
              "qui les décrit. Ouvrir le module sur les postes pour la deuxième heure. "
              "Les trois autres phrases sont : un petit carton trouvé dans la boîte aux "
              "lettres, le mur de petites cases, une boîte fermée avec du ruban.")

    d.billet(
        "Écrivez trois mots du bureau de poste que vous ne connaissiez pas ce matin.",
        exemples=[
            "Un mot pour l'endroit, un pour l'envoi, un pour l'adresse ?",
            "Lequel des seize vous semble le plus difficile à retenir ?",
        ],
        notes="Ramasser les billets : ils disent quels mots reprendre au début du "
              "défi 1, et ils préparent la révision de la séance E2.")

    return d.save(dossier)
