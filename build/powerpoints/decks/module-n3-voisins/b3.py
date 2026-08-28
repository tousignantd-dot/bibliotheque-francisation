# -*- coding: utf-8 -*-
"""B3 · Le, la, les, lui.
Bloc B « Défi 1 · Est-ce que je peux ? » · couleur ambre (écriture) · 60 min.
Source : exercice `t1pron`, mini-leçon `t1pron`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Le, la, les, lui : ne pas répéter le mot",
        chapeau="Une demande polie qui répète trois fois « mon vélo » "
                "devient lourde. Quatre petits mots suffisent à ne rien "
                "redire — encore faut-il savoir lequel prendre.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture. Reprendre au tableau deux demandes ramassées au "
                  "billet de B2 et faire chercher ce qui s'y répète : le nom de l'objet "
                  "revient presque toujours deux fois.")

    d.objectifs([
        "remplacer un nom déjà dit par « le », « la » ou « les » ;",
        "employer « lui » quand la personne est précédée de « à » ;",
        "placer le petit mot avant le verbe ;",
        "reconnaître le seul cas où il passe derrière.",
    ])

    d.regle("Le français déteste répéter",
            "Mon vélo gêne : je vais le mettre dans la remise.",
            precision="Le mot « le » remplace « mon vélo », qui vient d'être "
                      "dit. On ne redit jamais un nom que l'autre a déjà "
                      "entendu dans la phrase d'avant.",
            notes="Diapo à photographier. Faire relire la phrase avec la répétition — "
                  "« je vais mettre mon vélo dans la remise » — puis sans. Le groupe "
                  "entend tout de suite laquelle sonne juste.")

    d.tableau('Analyse', "Quel petit mot, pour quoi",
              ["Ce qu'on remplace", "Le petit mot"],
              [["une chose masculine — mon vélo", "le : je le mets dans la remise"],
               ["une chose féminine — la tondeuse", "la : je la laisse passer"],
               ["plusieurs choses — mes clés", "les : je les remets ce soir"],
               ["une personne avec « à » devant — à monsieur Nadeau", "lui : je lui parle"]],
              cle=1,
              note="Les trois premiers changent avec le genre et le nombre. "
                   "« Lui » ne change jamais : il vaut pour un homme comme "
                   "pour une femme.",
              notes="Diapo à photographier. La quatrième ligne est celle qui coûte : "
                    "faire chercher le mot « à » dans la phrase de départ avant de "
                    "choisir. S'il y est, c'est « lui ».")

    d.regle("Il se place avant le verbe",
            "Je le mets. Je lui parle. Je les remets.",
            precision="Toujours devant, jamais derrière — sauf à l'impératif, "
                      "quand on donne un ordre ou un conseil : "
                      "« Accrochez-le au mur ! »",
            notes="Diapo à photographier. Manon emploie les deux formes dans le dialogue "
                  "de B1 : « je l'ai vu » et « accrochez-le au mur du fond ». Les faire "
                  "retrouver.")

    d.pratique('Écriture', "Complétez avec le, la, les ou lui",
               "Cherchez d'abord ce que le petit mot remplace.", [
        ("Mon vélo gêne : je vais ___ mettre dans la remise.", "le — mon vélo"),
        ("La clé de la remise ? Le concierge ___ garde chez lui.", "la — la clé"),
        ("J'ai trouvé des clés dans l'escalier. Je vais ___ remettre ce soir.", "les — des clés"),
        ("Monsieur Nadeau est en bas : je vais ___ demander la clé.", "lui — à monsieur Nadeau"),
        ("Madame Lachapelle m'a aidé. Je vais ___ dire merci.", "lui — à madame Lachapelle"),
        ("Mes boîtes sont encore pleines : je vais ___ vider ce soir.", "les — mes boîtes"),
    ], corrige=True,
       notes="C'est l'exercice `t1pron` du module interactif, mot pour mot. Faire dire à "
             "voix haute ce que le petit mot remplace avant d'écrire : c'est là que "
             "l'erreur se joue, pas dans l'orthographe.")

    d.piege("Répéter le nom au lieu de le remplacer",
            "Je vais mettre mon vélo dans la remise, mon vélo est dans le corridor.",
            "Mon vélo est dans le corridor : je vais le mettre dans la remise.",
            "Répéter n'est pas une faute de grammaire — c'est une faute de ton. "
            "La phrase devient lourde, et l'autre a l'impression qu'on lui parle "
            "comme à un enfant. Le petit mot est ce qui rend la demande adulte.",
            notes="Ne pas dramatiser : l'élève est compris dans les deux cas. Le dire "
                  "franchement, ça enlève la peur et ça laisse la place au travail.")

    d.pratique('Écriture', "Réécrivez sans répéter",
               "Une seule phrase, avec le petit mot au bon endroit.", [
        ("J'ai trouvé un trousseau de clés. Je vais remettre le trousseau ce soir.",
         "Je vais le remettre ce soir."),
        ("La corde à linge est libre. Je vais utiliser la corde à linge demain.",
         "Je vais l'utiliser demain."),
        ("Monsieur Nadeau a la clé. Je vais demander la clé à monsieur Nadeau.",
         "Je vais la lui demander. — ou : je vais lui demander la clé."),
        ("Mes voisins m'ont aidé. Je veux dire merci à mes voisins.",
         "Je veux leur dire merci."),
    ], corrige=True, cols=1,
       notes="La dernière ligne fait apparaître « leur », le pluriel de « lui ». Ne pas "
             "l'enseigner ici : le nommer, dire qu'il suit exactement la même règle, et "
             "passer. Il reviendra au niveau 4.")

    d.billet(
        "Réécrivez votre demande de B2 en supprimant les répétitions.",
        exemples=[
            "Trois phrases, et le nom de l'objet une seule fois.",
            "« Ma poussette bloque l'entrée. Est-ce que je pourrais la mettre dans la remise ? »",
        ],
        notes="Devoir court. Ramasser : c'est la troisième version de la même demande, et "
              "c'est celle que l'élève dira en E1. La progression se voit d'un billet à "
              "l'autre, et vaut la peine d'être montrée à l'élève.")

    return d.save(dossier)
