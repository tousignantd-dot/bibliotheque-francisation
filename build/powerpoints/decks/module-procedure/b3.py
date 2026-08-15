# -*- coding: utf-8 -*-
"""B3 · Ce qui est obligatoire et ce qui ne l'est pas.
Bloc B · couleur ambre (écriture) · 60 min.
Source : dialogue `t1` — lire une directive et en tirer les obligations.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Obligatoire, interdit, facultatif",
        chapeau="« Vous devez », « il faut », « ne tentez jamais », « vous pouvez ». "
                "Quatre formulations, trois degrés d'obligation. Les confondre, c'est "
                "faire ce qui est interdit ou omettre ce qui est exigé.",
        duree='60 minutes')

    d.titre(notes="Écrire les quatre formulations au tableau et demander laquelle est la "
                  "plus forte. Le classement du groupe servira de point de départ.")

    d.objectifs([
        "reconnaître ce qui est obligatoire dans une directive écrite ;",
        "reconnaître une interdiction et sa force ;",
        "distinguer le facultatif du conseillé ;",
        "reformuler une directive en disant clairement son degré.",
    ])

    d.tableau('Analyse', "Quatre formulations, trois degrés",
              ['La formulation', 'Le degré'],
              [["vous devez, il faut", "obligatoire"],
               ["est obligatoire, est exigé", "obligatoire, dit encore plus fort"],
               ["ne tentez jamais, il est interdit", "interdit"],
               ["vous pouvez, si vous le souhaitez", "facultatif"],
               ["il est conseillé, nous recommandons", "conseillé, mais pas obligatoire"]],
              cle=1, props=[0.55, 0.45],
              notes="Le cinquième degré est le plus difficile : conseillé n'est pas "
                    "obligatoire, mais ne pas le suivre a souvent des conséquences. "
                    "Faire chercher, dans les directives du module, un exemple pour "
                    "chaque ligne. Ils y sont tous.")

    d.regle('La règle de lecture',
            "Cherchez le verbe : devoir, falloir, pouvoir, ou une interdiction.",
            precision="« Vous devez remplir » : obligatoire. « Vous pouvez consulter » : "
                      "facultatif. « Ne tentez jamais de réparer » : interdit. Le verbe "
                      "porte le degré, pas le ton de la phrase.",
            notes="Écrire la règle au tableau. Les élèves ont tendance à juger au ton : "
                  "une phrase polie peut être une obligation stricte.")

    d.cartes('Analyse', "Les quatre obligations du module", [
        ("La photo du reçu",
         "« Une photo claire du reçu est obligatoire, sinon la demande est refusée. » "
         "Obligatoire, avec la conséquence écrite noir sur blanc."),
        ("L'approbation du superviseur",
         "« Votre superviseur doit approuver la demande. » Obligatoire, et c'est une "
         "étape qui ne dépend pas de vous."),
        ("Ne pas réparer soi-même",
         "« Ne tentez jamais de réparer l'équipement vous-même. » Interdit — et "
         "« jamais » renforce l'interdiction."),
        ("Garder le reçu original",
         "« Gardez votre reçu original, au cas où. » Conseillé, pas obligatoire. Mais "
         "ne pas le faire coûte parfois le remboursement."),
    ], notes="La quatrième carte montre bien la différence : conseillé ne veut pas dire "
             "sans conséquence.")

    d.pratique('Pratique · 1 de 4', "Obligatoire, interdit ou facultatif ?",
               "Cherchez le verbe.", [
        ("Vous devez remplir le formulaire dans l'application.", "obligatoire"),
        ("Une photo claire du reçu est obligatoire.", "obligatoire"),
        ("Ne tentez jamais de réparer l'équipement vous-même.", "interdit"),
        ("Vous pouvez vérifier le statut de votre demande.", "facultatif"),
        ("Il est conseillé de garder votre reçu original.", "conseillé"),
        ("Il faut arrêter immédiatement la machine.", "obligatoire"),
    ], corrige=True,
       notes="Faire nommer le verbe à voix haute avant de classer. C'est lui qui décide, "
             "pas la longueur ni le ton de la phrase.")

    d.pratique('Pratique · 2 de 4', "Quelle est la conséquence ?",
               "Une obligation sans conséquence écrite n'est pas moins forte.", [
        ("Sans photo du reçu…", "la demande est refusée"),
        ("Sans approbation du superviseur…", "les finances ne traitent pas la demande"),
        ("Si on répare soi-même l'équipement…", "on met sa sécurité et son emploi en jeu"),
        ("Si on jette le reçu original…", "on ne peut pas répondre à une demande de vérification"),
    ], corrige=True,
       notes="Faire remarquer que seule la première conséquence est écrite dans la "
             "directive. Les autres se déduisent — et c'est ce qu'on apprend ici.")

    d.piege("Le piège de la formulation polie",
            "« Nous vous invitons à joindre une photo du reçu » — c'est facultatif.",
            "Une invitation dans une directive est presque toujours une obligation.",
            "Les entreprises écrivent souvent poliment ce qui est exigé : « nous vous "
            "invitons à », « merci de bien vouloir ». Cherchez la conséquence : si "
            "l'omission fait refuser la demande, c'est une obligation, quelle que soit "
            "la politesse de la phrase.",
            notes="Point culturel utile : la politesse administrative québécoise atténue "
                  "les obligations. Il faut lire la conséquence, pas le ton.")

    d.piege("Le piège du « jamais »",
            "Ne réparez pas l'équipement — sauf si c'est simple.",
            "Ne tentez jamais de réparer l'équipement vous-même.",
            "« Jamais » n'admet aucune exception, même quand la réparation paraît "
            "facile. Une consigne de sécurité écrite avec « jamais » couvre les cas où "
            "on croit savoir. C'est justement ceux-là qui causent les accidents.",
            notes="Lier au module 2 : une consigne de sécurité ne se négocie pas. "
                  "Beaucoup d'élèves ont l'habitude de réparer eux-mêmes.")

    d.pratique('Pratique · 3 de 4', "Reformulez la directive",
               "Dites clairement le degré, sans changer le sens.", [
        ("Nous vous invitons à joindre une photo du reçu.",
         "Vous devez joindre une photo du reçu."),
        ("Il serait préférable de réserver le véhicule à l'avance.",
         "Il est conseillé de réserver le véhicule à l'avance."),
        ("L'équipement ne doit en aucun cas être réparé par l'employé.",
         "Ne réparez jamais l'équipement vous-même."),
        ("Le statut de la demande peut être consulté en tout temps.",
         "Vous pouvez consulter le statut de la demande quand vous voulez."),
    ], corrige=True,
       notes="Exercice de reformulation. Le but n'est pas d'écrire plus joliment, mais "
             "plus clairement : c'est une compétence de lecture, pas de style.")

    d.pratique('Pratique · 4 de 4', "Écrivez la directive",
               "Employez la formulation qui correspond au degré demandé.", [
        ("Obligatoire : arrêter la machine avant de signaler un bris.",
         "Vous devez arrêter la machine avant de signaler un bris."),
        ("Interdit : réparer l'équipement soi-même.",
         "Ne tentez jamais de réparer l'équipement vous-même."),
        ("Conseillé : garder une copie de la demande.",
         "Il est conseillé de garder une copie de la demande."),
        ("Facultatif : consulter le statut dans l'application.",
         "Vous pouvez consulter le statut dans l'application."),
    ], corrige=True,
       notes="Ces quatre phrases préparent C4, où l'impératif remplacera « vous devez ». "
             "Le signaler au groupe.")

    d.billet(
        "Relevez trois directives de votre travail ou de votre école, et dites leur degré.",
        exemples=[
            "Une obligatoire, une interdite, une conseillée.",
            "Écrivez la phrase exacte, puis le degré à côté.",
        ],
        notes="Les directives apportées par les élèves sont souvent plus riches que les "
              "exemples du cours. En garder quelques-unes pour D1 et D2.")

    return d.save(dossier)
