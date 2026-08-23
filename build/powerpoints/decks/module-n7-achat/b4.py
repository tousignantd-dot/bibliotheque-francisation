# -*- coding: utf-8 -*-
"""B4 · Ce qui s'était passé avant
Bloc B « Défi 1 · Le bruit qu'il faut décrire » · couleur teal · grammaire et
écoute · 75 min.
Source : exercice `t1pqp` et sa mini-leçon ; savoir « indicatif
plus-que-parfait » du niveau 7 (deux points).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='teal',
        titre="Ce qui s'était passé avant",
        chapeau="« Quand j'ai vu la flaque, le bruit avait déjà commencé. » "
                "Un temps de verbe, et la chronologie du dossier bascule.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 1, et la plus grammaticale. La justifier en "
                  "une phrase : une réclamation est d'abord une chronologie, et une "
                  "chronologie floue affaiblit un dossier.")

    d.objectifs([
        "former le plus-que-parfait avec avoir et avec être ;",
        "dire qu'un fait est antérieur à un autre fait déjà passé ;",
        "employer le test du mot « déjà » ;",
        "accorder correctement le participe passé.",
    ], notes="Le deuxième objectif est le seul qui soit du sens ; les trois autres sont "
             "de la forme. Y consacrer la moitié de la séance et pas davantage.")

    d.declencheur(
        'Observation', "Ces deux phrases racontent-elles la même chose ?",
        pistes=[
            "« J'ai vu la flaque et le bruit a commencé. »",
            "« Quand j'ai vu la flaque, le bruit avait déjà commencé. »",
            "Dans laquelle sait-on ce qui est arrivé en premier ?",
            "Laquelle des deux montre que la fuite n'explique pas le bruit ?",
        ],
        notes="La quatrième question est le cœur de la séance. Dans la première "
              "version, un commerçant peut dire que la fuite a causé le bruit ; dans "
              "la seconde, non. Ce n'est pas du style : c'est de la preuve.")

    d.tableau('Analyse', "Comment il se forme",
              ['Avec', 'On dit'],
              [["avoir", "j'avais signé, nous avions remarqué"],
               ["être", "j'étais partie, elles étaient revenues"],
               ["Le choix", "le même qu'au passé composé"],
               ["Ce qui change", "l'auxiliaire passe à l'imparfait"],
               ["Le mot compagnon", "déjà, entre l'auxiliaire et le participe"]],
              cle=0,
              notes="Diapositive à photographier. Rassurer le groupe : aucun verbe n'a "
                    "de forme spéciale au plus-que-parfait. Qui sait dire « j'ai signé » "
                    "sait dire « j'avais signé ».")

    d.regle("Le plus-que-parfait n'existe qu'en paire",
            "Il ne dit pas qu'un fait est ancien : il dit qu'il est antérieur à un autre fait passé.",
            precision="Un événement d'il y a vingt ans se raconte très bien au passé "
                      "composé s'il n'est antérieur à rien. C'est pour cela que le test "
                      "du « déjà » fonctionne si bien : il oblige à chercher le "
                      "deuxième fait. S'il n'y en a pas, le passé composé suffit.",
            notes="Diapositive à photographier. Faire l'essai sur trois phrases du "
                  "groupe : celles où « déjà » n'entre pas n'ont pas besoin du "
                  "plus-que-parfait.")

    d.pratique('Grammaire', "Mettez au plus-que-parfait",
               "Le verbe entre parenthèses.", [
        ("Quand elle a vu la flaque, le cognement (commencer) ___ depuis trois jours.", "avait commencé"),
        ("Le vendeur (ajouter) ___ la garantie avant même qu'elle arrive.", "avait ajouté"),
        ("Personne ne le lui (expliquer) ___ .", "avait expliqué"),
        ("L'auto (servir) ___ de voiture de location pendant deux ans.", "avait servi"),
        ("Elle (partir) ___ de chez elle à six heures.", "était partie"),
        ("Les plaquettes (être) ___ changées par le commerçant.", "avaient été"),
    ], corrige=True,
       notes="Huit items dans le module ; en projeter six. Le cinquième change "
             "d'auxiliaire : le faire remarquer avant de corriger, pas après.")

    d.piege('Piège', "écrire « elle avait signée »",
            "avec avoir, le participe ne s'accorde jamais avec le sujet",
            "Avec être, on accorde avec le sujet : elle était partie. Avec avoir, "
            "jamais : elle avait signé. Le seul accord possible avec avoir arrive "
            "quand un « que » place le complément avant le verbe — « la lettre qu'elle "
            "avait écrite ».",
            notes="Ne pas développer davantage l'accord avec « que » : une phrase "
                  "suffit à ce niveau, et l'exercice du module n'en contient aucun cas.")

    d.tableau('Analyse', "La chronologie d'Ernestine, au bon temps",
              ['Le fait', 'Le temps'],
              [["Le 6 avril, elle a acheté", "passé composé : le point de départ"],
               ["L'auto avait servi de location", "antérieur à tout : plus-que-parfait"],
               ["Le 24 avril, un cognement est apparu", "passé composé"],
               ["Le bruit avait commencé avant la fuite", "antérieur : plus-que-parfait"],
               ["Le 30 avril, le garage a établi", "passé composé"],
               ["Elle avait fait 900 kilomètres", "état antérieur : plus-que-parfait"]],
              cle=0,
              notes="Diapositive à photographier. C'est le squelette du paragraphe des "
                    "faits de la lettre, écrit six séances d'avance. Le dire.")

    d.pratique('Écoute', "Deux faits, dans quel ordre ?",
               "Écoutez chaque paire et dites lequel s'est produit en premier.", [
        ("Quand je me suis présentée, le garage avait écrit son rapport.", "le rapport, avant la visite"),
        ("Je me suis présentée, puis j'ai fait établir un rapport.", "la visite, avant le rapport"),
        ("Quand je suis arrivée, le vendeur avait ajouté la garantie.", "l'ajout, avant l'arrivée"),
        ("Je suis arrivée et le vendeur a ajouté la garantie devant moi.", "les deux à la suite, devant elle"),
    ], corrige=True,
       notes="Faire remarquer que les paires deux à deux racontent deux dossiers "
             "différents avec le même vocabulaire. C'est l'argument le plus fort de la "
             "séance, et il ne se voit qu'en les mettant côte à côte.")

    d.billet(
        "Écris deux faits de ton dossier de B2, en mettant le plus ancien au plus-que-parfait.",
        exemples=[
            "« Quand j'ai remarqué…, cela avait déjà… »",
            "Deux phrases au plus.",
        ],
        notes="Cinq minutes. Ces billets sont la matière première du bloc C : chacun "
              "arrive au comptoir avec une chronologie écrite de sa main.")

    return d.save(dossier)
