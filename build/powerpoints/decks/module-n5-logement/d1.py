# -*- coding: utf-8 -*-
"""D1 · Avant de signer : lire le bail.
Bloc D « Défi 3 · Le bail » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf`, `t3bail` et `t3annexe`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-logement/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Avant de signer : lire le bail",
        chapeau="Le bail est le même formulaire pour tout le monde au Québec, "
                "et il est écrit pour être lu. Encore faut-il savoir où "
                "regarder.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 3. Demander qui a apporté une copie de son bail "
                  "(devoir A1). Travailler sur les vrais documents chaque fois que c'est "
                  "possible : l'effet est sans commune mesure avec un exemple inventé.")

    d.objectifs([
        "reconnaître les grandes sections d'un bail ;",
        "comprendre la section G et son utilité ;",
        "savoir que le bail se renouvelle automatiquement ;",
        "connaître son droit de sous-louer ou de céder son bail.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce que vous regardez en premier sur ce document ?",
        image=IMG + 'formulaire-bail.jpg',
        pistes=[
            "Le prix ? La date ? Les noms ?",
            "Combien de temps prendriez-vous pour le lire ?",
            "Qu'est-ce qui est écrit en petit ?",
            "Et cette feuille agrafée derrière ?",
        ],
        notes="La réponse honnête, pour beaucoup, est « je signe sans lire ». Le dire sans "
              "juger : le document est long et la pression du 1er juillet est réelle. La "
              "séance sert à savoir où regarder en cinq minutes.")

    d.dialogue('Dialogue · 1 de 3', "La section G", [
        ("HÉLÈNE", "Voilà le bail. C'est le formulaire officiel, le même pour tout "
                   "le monde au Québec.", True),
        ("NADÈGE", "Je vais le lire au complet, si vous permettez. … Ici, la section "
                   "G, c'est quoi ?", True),
        ("HÉLÈNE", "C'est l'avis au nouveau locataire. Je dois y écrire le loyer le "
                   "plus bas payé dans les douze derniers mois. Mille vingt "
                   "dollars, comme je vous l'ai dit.", True),
        ("NADÈGE", "Et moi, qu'est-ce que je peux faire avec cette information ?", False),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="« Je vais le lire au complet, si vous permettez » : la phrase à retenir. "
             "Personne ne peut la refuser, et elle change la posture du locataire.")

    d.dialogue('Dialogue · 2 de 3', "Le renouvellement", [
        ("HÉLÈNE", "Si vous trouvez que l'augmentation est trop forte, vous avez dix "
                   "jours après la signature pour demander une révision au Tribunal.", True),
        ("NADÈGE", "Dix jours. Je le note. Le bail se termine quand ?", True),
        ("HÉLÈNE", "Le trente juin de l'année prochaine. Après, il se renouvellera "
                   "tout seul aux mêmes conditions, sauf si l'un de nous deux "
                   "envoie un avis.", True),
        ("NADÈGE", "Donc si je ne dis rien, je reste.", True),
        ("HÉLÈNE", "C'est exactement ça. Au Québec, le bail se renouvelle "
                   "automatiquement. C'est une protection pour le locataire.", True),
    ], notes="Point capital, et souvent contre-intuitif : ici, le silence protège le "
             "locataire — alors qu'à la séance A1, le silence lui coûtait cher. Faire "
             "expliciter la différence : avis de modification contre fin de bail.")

    d.dialogue('Dialogue · 3 de 3', "L'annexe et la sous-location", [
        ("NADÈGE", "Et cette feuille-là, avec les règlements de l'immeuble ?", True),
        ("HÉLÈNE", "C'est l'annexe. Elle fait partie du bail : pas de tapis dans "
                   "l'escalier, les poubelles le mardi, et pas de barbecue sur le "
                   "balcon.", True),
        ("NADÈGE", "Une dernière chose : si je dois partir avant la fin, est-ce que "
                   "j'ai le droit de sous-louer ?", True),
        ("HÉLÈNE", "Vous avez le droit de sous-louer ou de céder votre bail. Vous "
                   "devez m'aviser par écrit, et je ne peux refuser sans un motif "
                   "sérieux.", True),
    ], notes="L'annexe fait partie du bail même si elle n'y ressemble pas : c'est la "
             "source d'un grand nombre de conflits. Faire lire les annexes réelles "
             "apportées par les élèves.")

    d.tableau('Le bail · 1 de 2', "Qui, combien de temps, combien",
              ['La section', 'Ce qu\'elle contient'],
              [["L'identification", "les noms et l'adresse du logement"],
               ["La durée", "la date du début et celle de la fin"],
               ["Le loyer", "le montant, la date de paiement, ce qui est compris"]],
              cle=0,
              note="Les trois premières se lisent en une minute.",
              notes="Diapositive à photographier. C'est la grille de lecture du défi 3.")

    d.tableau('Le bail · 2 de 2', "Ce que peu de gens lisent",
              ['La section', 'Ce qu\'elle contient'],
              [["La section G", "le loyer le plus bas payé dans les 12 derniers mois"],
               ["Les travaux", "ce que le propriétaire s'engage à faire"],
               ["L'annexe", "les règlements — ils font partie du bail"]],
              cle=0,
              note="Cinq minutes suffisent si vous savez où regarder.",
              notes="Diapositive à photographier. Ce sont ces trois-là qui produisent les "
                    "conflits, justement parce qu'on ne les lit pas.")

    d.regle("Le bail se renouvelle tout seul",
            "Si personne n'envoie d'avis, le bail recommence aux mêmes conditions.",
            precision="Le locataire n'a rien à signer et rien à demander. La fin du bail "
                      "n'est pas la fin du droit d'habiter : le propriétaire ne peut "
                      "reprendre le logement que dans des cas précis, et il doit alors le "
                      "prouver devant le Tribunal.",
            notes="Diapositive à photographier. C'est une protection que beaucoup d'élèves "
                  "ignorent, et plusieurs ont déjà déménagé sans y être obligés.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue et le tableau.", [
        ("Le bail est un formulaire officiel, le même pour tout le Québec.", "vrai"),
        ("La section G indique le loyer le plus bas des douze derniers mois.", "vrai"),
        ("Nadège a trente jours pour demander une révision.", "faux — dix jours"),
        ("Le bail se renouvelle automatiquement.", "vrai — si personne n'envoie d'avis"),
        ("L'annexe ne fait pas partie du bail.", "faux — elle en fait partie"),
        ("Nadège a le droit de sous-louer ou de céder son bail.", "vrai"),
        ("La propriétaire peut refuser une sous-location sans raison.",
         "faux — il lui faut un motif sérieux"),
    ], corrige=True,
       notes="Faire justifier chaque réponse. Les deux dernières lignes sont les plus "
             "utiles dans la vie réelle.")

    d.piege("Signer sans lire l'annexe",
            "C'est juste les règlements de l'immeuble.",
            "L'annexe fait partie du bail : ce qui y est écrit vous engage.",
            "Pas de barbecue sur le balcon, poubelles le mardi, pas de tapis dans "
            "l'escalier : ces règles ont la même force que le reste du contrat. Les lire "
            "avant de signer prend deux minutes.",
            notes="Demander au groupe quels règlements existent dans leur immeuble. La "
                  "liste est toujours plus longue que prévu, et plusieurs les découvrent.")

    d.billet(
        "Relisez votre bail et trouvez trois choses.",
        exemples=[
            "La date de fin, le montant inscrit à la section G, une règle de l'annexe.",
            "Si vous n'avez pas votre bail, notez à qui vous allez le demander.",
        ],
        notes="Devoir de lecture réelle. C'est le devoir le plus souvent commenté par les "
              "élèves à la séance suivante : beaucoup découvrent quelque chose.")

    return d.save(dossier)
