# -*- coding: utf-8 -*-
"""C3 · La phrase négative.
Bloc C · couleur ambre (écriture) · 75 min.
Source : exercice `t2neg` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre='La phrase négative',
        chapeau="« Je n'ai pas de fièvre » est peut-être la phrase la plus utile de "
                "toute une consultation. Ce que vous n'avez pas compte autant que ce "
                "que vous avez.",
        duree='75 minutes')

    d.titre(notes="Relier tout de suite à A1 : Rosalie décide d'envoyer Yannick à la "
                  "clinique et non à l'urgence à cause de deux négations — pas de "
                  "fièvre, pas de rougeur.")

    d.objectifs([
        "construire une phrase négative avec ne … pas ;",
        "choisir entre ne … pas, ne … plus et ne … jamais ;",
        "écrire n' devant une voyelle ;",
        "transformer « du, de la, des » en « de » après une négation.",
    ])

    d.regle('La règle',
            "La négation est en deux morceaux qui encadrent le verbe conjugué.",
            precision="« Ne » se place juste avant le verbe, le second mot juste après. "
                      "Je ne travaille pas. Il ne court plus. Elle ne prend jamais. Le "
                      "verbe est toujours au milieu.",
            notes="Écrire la règle au tableau avec le verbe encadré par deux traits. "
                  "L'image visuelle vaut mieux que l'explication.")

    d.tableau('Analyse', "Trois négations, trois sens",
              ['La forme', 'Ce qu\'elle dit', 'Exemple'],
              [["ne … pas", "non, simplement", "Je ne travaille pas."],
               ["ne … plus", "c'était vrai avant", "Il ne court plus."],
               ["ne … jamais", "à aucun moment", "Elle ne prend jamais ça."]],
              cle=1,
              note="« Plus » suppose un avant et un après. « Jamais » n'admet aucune "
                   "exception. « Pas » ne dit rien de plus que non.",
              notes="Faire trouver au groupe une situation de santé pour chacune des "
                    "trois. « Je ne fume plus » est l'exemple qui vient toujours.")

    d.tableau('Analyse', "Où se placent les deux morceaux",
              ['Sujet', 'Ne', 'Verbe', 'Pas'],
              [["je", "ne", "travaille", "pas"],
               ["il", "ne", "court", "plus"],
               ["elle", "ne", "prend", "jamais"],
               ["je", "n'", "ai", "pas"]],
              cle=2,
              note="Le verbe conjugué est toujours entre les deux. Rien d'autre ne se "
                   "glisse là, sauf un pronom.",
              notes="Faire remarquer la dernière ligne : « ne » devient « n' » devant "
                    "« ai ». C'est le sujet de la diapo suivante.")

    d.regle("Devant une voyelle",
            "Ne perd son e et devient n' devant un verbe qui commence par une voyelle.",
            precision="Je n'ai pas de fièvre. Il n'est pas malade. Elle n'écoute pas. "
                      "Ce n'est pas un choix de style : c'est automatique, comme "
                      "« l'hôpital » au lieu de « le hôpital ».",
            notes="Faire lire « je ne ai pas » à voix haute : le groupe entendra "
                  "lui-même que c'est impossible à dire.")

    d.cartes('Ouvrir la mini-leçon', "Quatre choses à savoir en plus", [
        ("« du, de la, des » deviennent « de »",
         "J'ai de la fièvre devient je n'ai pas de fièvre. Je prends des médicaments "
         "devient je ne prends pas de médicaments. Une règle à part, très fréquente."),
        ("Le « ne » disparaît à l'oral",
         "« J'ai pas mal » s'entend partout au Québec. C'est correct entre amis, mais à "
         "l'écrit et devant un professionnel, gardez le « ne »."),
        ("Deux négations dans une phrase",
         "« Je ne prends plus jamais ce médicament » est possible : plus et jamais se "
         "combinent. Mais « pas » ne se combine avec rien."),
        ("Ne … rien, ne … personne",
         "Même construction : je ne sens rien, je ne connais personne ici. Le second "
         "morceau change, la place ne change pas."),
    ], notes="La première carte est celle qui compte le plus : c'est l'erreur la plus "
             "fréquente à l'écrit, et elle apparaît dans toutes les consultations.")

    d.pratique('Pratique · 1 de 3', 'Mettez à la forme négative',
               "Utilisez ne … pas. Attention aux voyelles.", [
        ("Il peut plier la jambe.", "Il ne peut pas plier la jambe."),
        ("J'ai de la fièvre.", "Je n'ai pas de fièvre."),
        ("Elle travaille cette semaine.", "Elle ne travaille pas cette semaine."),
        ("Yannick soulève des charges.", "Yannick ne soulève pas de charges."),
        ("Nous sommes en retard.", "Nous ne sommes pas en retard."),
        ("Vous prenez des médicaments.", "Vous ne prenez pas de médicaments."),
    ], corrige=True,
       notes="Les items 2, 4 et 6 contiennent la transformation « des, de la » en « de ». "
             "Les corriger ensemble, à la fin, pour que le groupe voie le motif.")

    d.piege('Le piège du « des »',
            "Je ne prends pas des médicaments.",
            "Je ne prends pas de médicaments.",
            "Après une négation, « du », « de la » et « des » deviennent tous « de ». "
            "C'est vrai pour la quantité, pas pour l'identité : « ce n'est pas du sucre, "
            "c'est du sel » reste correct, parce qu'on identifie au lieu de compter.",
            notes="Ne pas insister sur l'exception — la règle principale suffit à ce "
                  "niveau. La mentionner seulement si un élève la soulève.")

    d.piege("Le piège du « n' »",
            "Je ne ai pas mal.",
            "Je n'ai pas mal.",
            "Devant un verbe qui commence par une voyelle, « ne » devient toujours "
            "« n' ». Cela vaut pour ai, es, est, ai, écoute, examine — et pour « en » "
            "et « y » quand ils précèdent le verbe.",
            notes="Faire chercher dans le dialogue de C1 toutes les négations. Il y en a "
                  "deux, et une seule prend l'apostrophe.")

    d.pratique('Pratique · 2 de 3', "Pas, plus ou jamais ?",
               "Choisissez la négation qui convient au sens.", [
        ("Il a arrêté de courir après sa blessure. Il ne court ___.", "plus"),
        ("Elle refuse ce médicament depuis toujours. Elle n'en prend ___.", "jamais"),
        ("Aujourd'hui, je ne travaille ___.", "pas"),
        ("Depuis l'opération, il ne soulève ___ de charges lourdes.", "plus"),
        ("Je n'ai ___ eu de fracture de ma vie.", "jamais"),
    ], corrige=True,
       notes="Faire justifier chaque choix par un mot de la phrase : « depuis », "
             "« a arrêté », « de ma vie ». Le sens est dans le contexte, pas dans le "
             "verbe.")

    d.pratique('Pratique · 3 de 3', "Répondez négativement au triage",
               "Phrase complète, et ajoutez une précision utile.", [
        ("Est-ce que vous avez de la fièvre ?",
         "Non, je n'ai pas de fièvre, mais j'ai eu froid cette nuit."),
        ("Est-ce que vous prenez des médicaments ?",
         "Non, je ne prends pas de médicaments en ce moment."),
        ("Est-ce que vous pouvez plier la jambe ?",
         "Non, je ne peux plus la plier depuis hier."),
        ("Avez-vous déjà eu une fracture ?",
         "Non, je n'ai jamais eu de fracture."),
    ], corrige=True,
       notes="La consigne « ajoutez une précision » est le vrai exercice : une réponse "
             "négative sèche ferme la conversation, une réponse négative précisée "
             "l'ouvre.")

    d.billet(
        "Écrivez trois phrases négatives sur votre santé.",
        exemples=[
            "Une avec ne … pas, une avec ne … plus, une avec ne … jamais.",
            "Au moins une doit contenir « de » à la place de « du, de la, des ».",
        ],
        notes="Corriger surtout la transformation « des » en « de ». C'est l'erreur qui "
              "subsiste le plus longtemps, bien après la fin du module.")

    return d.save(dossier)
