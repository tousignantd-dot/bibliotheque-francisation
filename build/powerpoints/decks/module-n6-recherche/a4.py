# -*- coding: utf-8 -*-
"""A4 · Les métiers et leurs secteurs.
Bloc A « Je découvre » · couleur teal · 60 min. Bilan du bloc A.
Source : exercices `prMetiers` et `prImg`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n6-recherche/images/')


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre="Les métiers et leurs secteurs",
        chapeau="Un métier se cherche dans un secteur. Savoir lequel change "
                "la liste des employeurs à qui écrire — et, pour certains "
                "métiers, il faut d'abord passer par un ordre professionnel.",
        duree='60 minutes')

    d.titre(notes="Dernière séance du bloc A. Elle met en commun le vocabulaire des "
                  "trois séances précédentes et prépare la lecture d'offres du bloc B.")

    d.objectifs([
        "associer un métier à son secteur d'activité ;",
        "nommer les lieux et les gestes de la recherche d'emploi ;",
        "savoir ce qu'est un ordre professionnel et quand il concerne ;",
        "dire où et comment on cherche une offre au Québec.",
    ])

    d.declencheur(
        'Observation', "Où cherche-t-on un emploi, ici ?",
        image=IMG + 'offre-ecran.jpg',
        pistes=[
            "Sur un site d'emploi ?",
            "Sur le site de l'entreprise elle-même ?",
            "Par quelqu'un qu'on connaît ?",
            "En allant porter son curriculum vitæ sur place ?",
        ],
        notes="Les quatre réponses sont bonnes et complémentaires. Insister sur la "
              "deuxième : beaucoup d'entreprises affichent d'abord chez elles, et "
              "l'offre y reste plus longtemps que sur les grands sites.")

    d.tableau('Association · 1 de 2', "Le métier et son secteur",
              ['Le métier', 'Le secteur d\'activité'],
              [["un préposé aux bénéficiaires", "la santé et les services sociaux"],
               ["un charpentier-menuisier", "la construction"],
               ["un commis à l'inventaire", "le transport et la logistique"]],
              cle=0,
              notes="Faire ajouter les métiers du groupe, avec leur secteur. Certains "
                    "hésitent — c'est le moment de trancher ensemble.")

    d.tableau('Association · 2 de 2', "Le métier et son secteur",
              ['Le métier', 'Le secteur d\'activité'],
              [["un cuisinier", "la restauration"],
               ["une éducatrice à l'enfance", "les services de garde"],
               ["un soudeur", "la fabrication industrielle"]],
              cle=0,
              note="Le secteur est le mot qu'on tape à côté du titre, sur un site d'emploi.",
              notes="Terminer par les métiers du groupe qui n'entrent dans aucune de ces "
                    "six lignes : il y en a toujours.")

    d.cartes("Les lieux de la recherche", "Quatre endroits, quatre usages", [
        ("Le site de l'entreprise",
         "Section « Carrières » ou « Emplois ». C'est souvent là que l'offre paraît en premier."),
        ("Les grands sites d'emploi",
         "Beaucoup d'offres, beaucoup de candidats. Le titre exact du poste sert de filtre."),
        ("Un organisme en employabilité",
         "Un service gratuit : aide au curriculum vitæ, préparation à l'entrevue, contacts avec des employeurs."),
        ("Les gens qu'on connaît",
         "Un ancien collègue, un voisin, une personne du cours. Beaucoup de postes se comblent ainsi."),
    ], notes="Nommer l'organisme en employabilité du quartier, si le groupe ne le connaît "
             "pas. Le service est gratuit et beaucoup l'ignorent.")

    d.regle("Un ordre professionnel",
            "Certains métiers demandent un permis avant d'être exercés.",
            precision="Infirmière, ingénieur, comptable, travailleur social : ces "
                      "professions sont encadrées par un ordre, qui vérifie la formation "
                      "et donne le droit d'exercer. Un diplôme obtenu à l'étranger doit "
                      "y être reconnu. Ce n'est pas le cas de la plupart des métiers — "
                      "mais quand ça l'est, la démarche prend du temps et se commence tôt.",
            notes="Diapositive à photographier. Demander si quelqu'un du groupe exerçait "
                  "une profession de ce type. Si oui, la démarche vaut d'être expliquée "
                  "à part, après la séance.")

    d.pratique('Vocabulaire', "De quoi parle-t-on ?",
               "Nommez ce que décrit chaque phrase.", [
        ("L'annonce par laquelle une entreprise fait savoir qu'elle cherche quelqu'un.", "une offre d'emploi"),
        ("Le grand bâtiment où on garde la marchandise avant de la livrer.", "un entrepôt"),
        ("La rencontre où l'employeur pose des questions.", "une entrevue"),
        ("Le document qui résume la formation et l'expérience.", "un curriculum vitæ"),
        ("Les jours et les heures où on peut travailler.", "les disponibilités"),
        ("La personne qui accepte de parler de votre travail.", "une référence"),
    ], corrige=True,
       notes="Les deux derniers mots reviendront au bloc C. Les faire noter dès "
             "maintenant.")

    d.piege("Chercher « du travail »",
            "Je cherche du travail, n'importe quoi.",
            "Je cherche un poste de commis à l'inventaire.",
            "Un employeur qui entend « n'importe quoi » comprend « rien en particulier », "
            "et il n'a pas de poste appelé « n'importe quoi ». Le titre exact n'exclut "
            "rien : on peut en viser deux ou trois, et se présenter avec celui qui "
            "correspond à l'offre qu'on a devant soi.",
            notes="Reprendre le billet de la séance A1 : chacun devrait maintenant avoir "
                  "son titre écrit.")

    d.billet(
        "Trouvez une offre d'emploi réelle dans votre secteur.",
        exemples=[
            "Imprimez-la ou notez son adresse : elle servira aux quatre séances du bloc B.",
            "Choisissez-en une qui vous intéresse vraiment.",
        ],
        notes="Devoir essentiel : tout le bloc B travaille sur une offre. Ceux qui n'en "
              "trouvent pas travailleront sur celle de Boisverte, mais c'est moins fort.")

    return d.save(dossier)
