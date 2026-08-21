# -*- coding: utf-8 -*-
"""A3 · « Les seize mots du voisinage »
Bloc A « Je découvre » · couleur framboise · 75 min. Vocabulaire.
Source : exercices `prVocab`, `prImg`, `prMots`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-voisinage/images/')


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Les seize mots du voisinage",
        chapeau="Le programme ne fournit aucun lexique pour cette situation. "
                "Les seize mots de ce module viennent donc des savoirs du "
                "niveau et de la vie réelle d'un immeuble montréalais : la "
                "ruelle, le hangar, le répondeur, les félicitations.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Elle vient en troisième position parce que les "
                  "mots ont d'abord été entendus dans le dialogue de A1 : on nomme ce "
                  "qu'on a déjà rencontré, jamais l'inverse.")

    d.objectifs([
        "nommer les lieux d'un immeuble et d'une ruelle ;",
        "nommer ce qui entoure une invitation : le plat, la date, l'empêchement ;",
        "nommer les objets du téléphone et du message écrit ;",
        "employer chaque mot avec son article.",
    ], notes="Le quatrième objectif est le plus important et le moins spectaculaire. "
             "L'article fait partie du mot : « un hangar », jamais « hangar ».")

    d.vocabulaire('Vocabulaire · 1 de 4', "L'immeuble et la ruelle", [
        ("une ruelle verte", "Le passage derrière les immeubles, planté et entretenu par les gens qui habitent autour."),
        ("un hangar", "La petite construction de bois, au fond de la cour, où l'on range ce qui ne va pas dans le logement."),
        ("une corvée", "Un travail que plusieurs personnes font ensemble, la même journée, pour un endroit commun."),
        ("le voisinage", "L'ensemble des gens qui habitent tout près de chez soi."),
    ], notes="Distinguer « un voisin », qui est une personne, et « le voisinage », qui est "
             "l'ensemble et le lien. Rappeler qu'on dit « dans la ruelle », jamais « sur "
             "la ruelle ».")

    d.vocabulaire('Vocabulaire · 2 de 4', "L'invitation et la réponse", [
        ("une invitation", "La proposition de venir quelque part, à une date et à une heure données."),
        ("un plat à partager", "Ce qu'on prépare en grande quantité pour le mettre au milieu de la table."),
        ("reporter", "Déplacer une chose prévue à une date plus tard."),
        ("un empêchement", "Ce qui vous oblige à dire non alors que vous auriez voulu dire oui."),
    ], notes="« Un empêchement » est le mot le plus utile de la liste : il permet de "
             "refuser sans raconter sa vie. « J'ai un empêchement ce jour-là » est une "
             "phrase complète et suffisante.")

    d.vocabulaire('Vocabulaire · 3 de 4', "Le téléphone et le mot écrit", [
        ("un répondeur", "L'appareil ou le service qui enregistre les appels quand personne ne décroche."),
        ("un mot", "Le petit papier écrit à la main qu'on laisse pour informer quelqu'un."),
        ("prévenir", "Dire une chose à l'avance à quelqu'un, pour qu'il puisse s'organiser."),
        ("arroser", "Donner de l'eau à une plante ou à un jardin."),
    ], notes="« Un mot » est piégeant : c'est le même mot que « un mot de vocabulaire ». "
             "Donner les deux emplois dans la même minute pour que la confusion se règle "
             "tout de suite.")

    d.vocabulaire('Vocabulaire · 4 de 4', "Les nouvelles et les félicitations", [
        ("des félicitations", "Les paroles qu'on dit à quelqu'un à qui il arrive une bonne chose."),
        ("la citoyenneté", "Le fait de devenir officiellement citoyen d'un pays, avec un certificat."),
        ("une cérémonie", "Une rencontre officielle, avec des discours, pour marquer un moment important."),
        ("fêter", "Marquer une bonne nouvelle en se réunissant, autour d'un repas ou d'un café."),
    ], notes="« Félicitations » prend toujours un s, et on félicite « pour » quelque "
             "chose. L'écrire au tableau : c'est l'erreur écrite la plus fréquente du "
             "défi 3.")

    d.declencheur(
        'Observation', "Six lieux, six phrases. Lequel va avec laquelle ?",
        image=IMG + 'boites-lettres.jpg',
        pistes=[
            "Une rangée de boîtes aux lettres dans une petite entrée.",
            "Un balcon d'en arrière avec deux chaises et des pots de fleurs.",
            "Un papier retenu par un aimant sur la porte d'un réfrigérateur.",
            "Un bac brun sorti sur le trottoir un jour de collecte.",
        ],
        notes="Projeter, faire décrire à l'oral, puis ouvrir l'exercice prImg dans "
              "l'activité : les six photos s'y glissent sur leur phrase. La description "
              "orale doit venir avant la manipulation.")

    d.pratique('Écriture', "Chaque chose à son nom",
               "Complétez avec le mot juste, sans article.", [
        ("Les tables de la fête sont montées dans la ___ .", "ruelle"),
        ("Il range ses pots et sa pelle dans le ___ .", "hangar"),
        ("Les restes de table vont dans le bac ___ .", "brun"),
        ("Six logements sur douze sont venus à la ___ de printemps.", "corvée"),
        ("En trois ans, elle n'avait parlé à personne du ___ .", "voisinage"),
        ("L' ___ extérieur en colimaçon donne sur la rue.", "escalier"),
    ], corrige=True,
       notes="Exercice prMots dans l'activité interactive. Le faire d'abord à l'oral, "
             "collectivement, puis laisser les élèves le refaire seuls sur les postes.")

    d.piege("Oublier l'article en apprenant le mot",
            "hangar, ruelle, répondeur",
            "un hangar, une ruelle, un répondeur",
            "L'article porte le genre, et le genre décide de tout ce qui suit : « ce "
            "hangar », « cette ruelle ». Un mot appris sans article est un mot à "
            "réapprendre.",
            notes="Insister : c'est le conseil de vocabulaire qui rapporte le plus sur "
                  "trois ans. Les cartes mémoire du module donnent toujours l'article.")

    d.billet(
        "Choisissez trois mots de la séance et écrivez une phrase avec chacun.",
        exemples=[
            "Une phrase qui parle de votre immeuble, pas de celui de Marisol.",
            "Vérifiez l'article avant de remettre votre billet.",
        ],
        notes="Ramasser. Les phrases des élèves sur leur propre immeuble serviront "
              "d'exemples en A4 et en B2.")

    return d.save(dossier)
